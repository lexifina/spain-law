"""Functional smoke test of the built Spanish law repository: the things a reader does with it work. Standard library only.

    python -X utf8 scripts/spain-law/test_repo.py [--repo ../spain-law] [--record]
    python -X utf8 tools/test_repo.py                   # from inside the repository

It asserts that:
1. `git blame` on an amended block names amending norms as authors of its lines;
2. tools/eslaw.py gives the text before and after a known amendment, and each equals the file at that commit;
3. `git log --follow` on a file lists its amending norms in the order they took effect;
4. every tag resolves, and every commit but the documentation commit has an ISO `In-force:` trailer;
5. no commit is authored by Lexifina except the documentation commit (the last one), the committer is always
   Lexifina, and every other author is a BOE norm or the labelled publisher;
6. every git or tool command in the README's table runs and prints something.
With --record the result is written to cache/verification.json next to this script (for REPRODUCE.md).
"""
import argparse
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAW = re.compile(r'^BOE-[A-Za-z]+-\d{4}-\d+( \(.+\))?$')
PUBLISHER = 'Agencia Estatal Boletin Oficial del Estado (BOE)'
CE = 'estatal/constitucion/1978/BOE-A-1978-31229'
CC = 'estatal/real-decreto/1889/BOE-A-1889-4763'


def default_repo() -> Path:
    if (HERE.parent / '.git').exists():
        return HERE.parent
    return HERE.parents[2] / 'spain-law'


class Smoke:
    def __init__(self, repo: Path):
        self.repo = repo
        self.results = []

    def git(self, *args: str) -> str:
        out = subprocess.run(['git', *args], cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'git {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def tool(self, *args: str) -> str:
        out = subprocess.run([sys.executable, 'tools/eslaw.py', *args], cwd=self.repo, capture_output=True, text=True,
                             encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'eslaw {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def check(self, name, fn):
        try:
            detail = fn() or ''
            self.results.append((name, True, detail))
            print(f'PASS {name}: {detail}')
        except AssertionError as exc:
            self.results.append((name, False, str(exc)))
            print(f'FAIL {name}: {exc}')

    def blame(self):
        path = f'{CE}/a135.md'
        out = self.git('blame', '--line-porcelain', 'main', '--', path)
        authors = {l[7:] for l in out.splitlines() if l.startswith('author ')}
        assert authors and all(LAW.match(a) or a == PUBLISHER for a in authors), f'unexpected authors {authors}'
        assert any(a.startswith('BOE-A-2011-15210') for a in authors), f'the 2011 reform is not among {authors}'
        return f'{path} lines by {", ".join(sorted(authors))}'

    def on_date(self):
        done = []
        for path, norma, before, after in [(f'{CE}/a135.md', 'BOE-A-2011-15210', '2011-09-26', '2011-09-27'),
                                           (f'{CE}/a49.md', 'BOE-A-2024-3099', '2024-02-16', '2024-02-17')]:
            sha = self.git('log', '--format=%H', f'--grep=^Norma: {norma}$', 'main', '--', path).split()
            assert len(sha) == 1, f'{path}: {len(sha)} commits by {norma}'
            inf = re.search(r'^In-force: (\S+)$', self.git('log', '-1', '--format=%B', sha[0]), re.M).group(1)
            assert inf == after, f'{norma} in force {inf}, expected {after}'
            a, b = self.tool('on', before, path), self.tool('on', after, path)
            assert a and b and a != b, f'{path}: no change between {before} and {after}'
            assert b == self.git('show', f'{sha[0]}:{path}'), f'{path} on {after} is not the file at {sha[0][:10]}'
            assert a == self.git('show', f'{sha[0]}~1:{path}'), f'{path} on {before} is not the file before {sha[0][:10]}'
            done.append(f'{path} {before} != {after}')
        whole = self.tool('on', '2000-01-01', CE)
        assert 'Artículo 135' in whole and 'Constitución' in whole, 'the whole Constitution on 2000-01-01 lacks art. 135'
        return '; '.join(done)

    def follow(self):
        checked = []
        for path in (f'{CE}/a135.md', f'{CE}/a49.md', f'{CC}/a1.md'):
            out = self.git('log', '--follow', '--format=%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main', '--', path)
            rows = [l.split('\t') for l in out.splitlines() if l]
            assert len(rows) >= 2, f'{path}: {len(rows)} commits'
            days = [d.strip() for _, d in rows]
            assert days == sorted(days, reverse=True), f'{path}: not in date order {days}'
            assert all(LAW.match(a) or a == PUBLISHER for a, _ in rows), f'{path}: authors {[a for a, _ in rows]}'
            checked.append(f'{path} {len(rows)} commits')
        return '; '.join(checked)

    def tags_and_trailers(self):
        tags = self.git('tag').split()
        for t in tags:
            self.git('rev-parse', '--verify', '-q', f'{t}^{{commit}}')
        rows = self.git('log', '--format=%H%x09%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main').splitlines()
        missing = [r for r in rows[1:] if not r.split('\t')[2].strip()]
        assert not missing, f'{len(missing)} commits without In-force, e.g. {missing[:2]}'
        assert not rows[0].split('\t')[2].strip(), 'documentation commit should carry no In-force'
        bad = [r for r in rows[1:] if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.split('\t')[2].strip())]
        assert not bad, f'malformed In-force {bad[:2]}'
        return f'{len(tags)} tags resolve; {len(rows) - 1} law commits carry In-force'

    def lexifina(self):
        rows = self.git('log', '--format=%H%x09%an%x09%ae%x09%cn%x09%ce', 'main').splitlines()
        by_lex = [r for r in rows if r.split('\t')[1] == 'Lexifina']
        assert len(by_lex) == 1 and by_lex[0] == rows[0], f'{len(by_lex)} commits by Lexifina'
        assert all(r.split('\t')[3] == 'Lexifina' and r.split('\t')[4] == 'spain-law@lexifina.com' for r in rows), 'other committer'
        authors = {r.split('\t')[1] for r in rows[1:]}
        odd = sorted(a for a in authors if not (LAW.match(a) or a == PUBLISHER))
        assert not odd, f'unexpected authors {odd[:5]}'
        assert all(r.split('\t')[2].endswith('@boe.invalid') for r in rows[1:]), 'an author email not at boe.invalid'
        return f'only the documentation commit {rows[0][:10]} is by Lexifina; {len(authors)} distinct authors'

    def readme(self):
        text = (self.repo / 'README.md').read_text(encoding='utf-8')
        table = text[text.index('## The questions'):text.index('## The dates')]
        cmds = [c for c in re.findall(r'`([^`]+)`', table) if c.startswith(('git ', 'python '))]
        assert len(cmds) >= 8, f'only {len(cmds)} commands found'
        for c in cmds:
            args = shlex.split(c)
            if args[0] == 'python':
                args[0] = sys.executable
            out = subprocess.run(args, cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
            assert out.returncode == 0, f'{c}: exit {out.returncode} {out.stderr.strip()[:200]}'
            assert out.stdout.strip(), f'{c}: printed nothing'
        return f'{len(cmds)} README commands ran and printed output'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=None)
    ap.add_argument('--record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    s = Smoke(Path(args.repo) if args.repo else default_repo())
    s.check('blame names a norm', s.blame)
    s.check('text before and after an amendment', s.on_date)
    s.check('log --follow in date order', s.follow)
    s.check('tags resolve, In-force on every law commit', s.tags_and_trailers)
    s.check('only the documentation commit is by Lexifina', s.lexifina)
    s.check('README commands run', s.readme)
    ok = all(r[1] for r in s.results)
    summary = f'{sum(r[1] for r in s.results)}/{len(s.results)} passed'
    print(summary)
    if args.record:
        p = HERE / 'cache' / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['smoke'] = {'summary': summary, 'results': [{'test': n, 'ok': o, 'detail': d} for n, o, d in s.results]}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
