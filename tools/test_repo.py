"""Functional smoke test of the built Spanish law repository: the things a reader does with it work. Standard library only.

    python -X utf8 scripts/spain-law/test_repo.py [--repo ../spain-law] [--record]
    python -X utf8 tools/test_repo.py                   # from inside the repository

It asserts that:
1. `git blame` on an amended block names amending norms as authors of its lines;
2. tools/eslaw.py gives the text before and after a known amendment, and each equals the file at that commit;
3. `git log --follow` on a file lists its amending norms in the order they took effect;
4. every tag resolves, every normative/correction commit has an ISO `In-force:` trailer, and documentation is labelled;
5. maintainers author labelled documentation or sourced corrections; other authors are BOE norms or the publisher;
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
    def __init__(self, repo: Path, published_base=None):
        self.repo = repo
        self.published_base = published_base
        self.results = []

    def legacy_published(self, sha):
        """Only the explicit immutable published pin may contain pre-schema maintainer records."""
        assert self.published_base, f'{sha}: legacy record requires --pin <published baseline>'
        if not hasattr(self, '_published_commits'):
            self._published_commits = set(self.git('rev-list', self.published_base).split())
        assert sha in self._published_commits, f'{sha}: new maintainer record must declare Kind'

    def ancestor(self, target, sha):
        if not hasattr(self, '_linear'):
            self._linear = self.git('rev-list', '--count', '--merges', 'main').strip() == '0'
            self._positions = {commit: i for i, commit in enumerate(self.records())}
        if self._linear:
            matches = [commit for commit in self._positions if commit.startswith(target)] if len(target) != 40 else [target]
            assert len(matches) == 1 and matches[0] in self._positions, f'{sha}: missing/ambiguous provenance commit {target}'
            assert self._positions[matches[0]] > self._positions[sha], f'{sha}: provenance target is not an earlier ancestor'
        else:
            self.git('merge-base', '--is-ancestor', target, sha + '^')

    def records(self):
        if not hasattr(self, '_records'):
            fmt = '%x1d%H%x1f%an%x1f%ae%x1f%cn%x1f%ce%x1f%(trailers:only,unfold)'
            raw = self.git('log', '--format=' + fmt, 'main')
            self._records = {}
            for chunk in raw.split('\x1d')[1:]:
                sha, author, email, committer, committer_email, block = chunk.split('\x1f', 5)
                trailers = {}
                for key, value in re.findall(r'^([A-Za-z-]+):\s*(.*)$', block, re.M):
                    trailers.setdefault(key, []).append(value.strip())
                self._records[sha] = (author, email, committer, committer_email, trailers)
        return self._records

    def classification(self, sha):
        author, email, committer, committer_email, t = self.records()[sha]
        value = lambda key: t.get(key, [''])[0]
        kind, day = value('Kind').lower(), value('In-force')
        if author == 'Lexifina' and not kind and not day:
            self.legacy_published(sha)
            # Historical documentation predates Kind. Recognize it only when its actual delta contains no act file.
            changed = self.git('diff-tree', '--root', '--no-commit-id', '--name-only', '-r', sha).splitlines()
            assert not any(p.startswith('estatal/') for p in changed), f'{sha}: unlabelled maintainer changed an act'
            return 'documentation'
        if author == 'Lexifina' and not kind and day:
            self.legacy_published(sha)
            norma = value('Norma')
            assert LAW.match(norma), f'{sha}: legacy sourced record lacks a BOE norm'
            assert value('Source').startswith(('https://www.boe.es/', 'http://www.boe.es/')), f'{sha}: legacy record lacks official source'
            if value('Re-asserts'):
                assert re.fullmatch(r'[0-9a-f]{7,40}', value('Re-asserts')), f'{sha}: malformed legacy Re-asserts'
                self.ancestor(value('Re-asserts'), sha)
            else:
                assert value('Law').startswith(norma), f'{sha}: legacy same-day record lacks explicit law credit'
            return 'legacy sourced record'
        if kind == 'documentation':
            assert author == 'Lexifina' and not day, f'{sha}: invalid documentation identity/date'
            return 'documentation'
        if author == 'Lexifina':
            assert kind == 'correction', f'{sha}: unlabelled maintainer-authored normative commit'
            for key in ('In-force', 'Corrects', 'Supersedes', 'Reason', 'Act-path', 'Files'):
                assert value(key), f'{sha}: correction missing {key}'
            corrects = value('Corrects')
            assert re.fullmatch(r'[0-9a-f]{7,40}', corrects) or re.fullmatch(
                r'\S+ \d{4}-\d{2}-\d{2}\.\.(?:\d{4}-\d{2}-\d{2})?', corrects), f'{sha}: malformed Corrects'
            if re.fullmatch(r'[0-9a-f]{7,40}', corrects):
                self.ancestor(corrects, sha)
            assert value('Source') or value('Norma') or value('Law'), f'{sha}: correction lacks source/provenance'
            for redates in t.get('Redates', []):
                match = re.fullmatch(r'([0-9a-f]{7,40}) (\d{4}-\d{2}-\d{2}|no-date)', redates)
                assert match, f'{sha}: malformed Redates'
                self.ancestor(match[1], sha)
            return 'correction'
        assert LAW.match(author) or author == PUBLISHER, f'{sha}: unexpected normative author {author}'
        return 'law'

    def blame_revision(self, path):
        """Documentation may restore deleted files, but only identical source blobs retain their original blame."""
        blob = self.git('rev-parse', 'main:' + path).strip()
        for sha in self.git('log', '--follow', '--format=%H', 'main', '--', path).split():
            author = self.records()[sha][0]
            if not (LAW.match(author) or author == PUBLISHER):
                continue
            if self.git('rev-parse', sha + ':' + path).strip() == blob:
                return sha
        raise AssertionError(f'{path}: current blob has no identical norm-authored historical version')

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
        revision = self.blame_revision(path)
        out = self.git('blame', '--line-porcelain', revision, '--', path)
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
            out = self.git('log', '--follow', '--format=%H%x09%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main', '--', path)
            rows = [(a, d) for sha, a, d in (l.split('\t') for l in out.splitlines() if l)
                    if self.classification(sha) != 'documentation']
            assert len(rows) >= 2, f'{path}: {len(rows)} commits'
            days = [d.strip() for _, d in rows]
            assert days == sorted(days, reverse=True), f'{path}: not in date order {days}'
            assert all(LAW.match(a) or a == PUBLISHER or a == 'Lexifina' for a, _ in rows), f'{path}: authors {[a for a, _ in rows]}'
            checked.append(f'{path} {len(rows)} commits')
        return '; '.join(checked)

    def tags_and_trailers(self):
        tags = self.git('tag').split()
        if tags:
            query = '\n'.join('refs/tags/' + t + '^{commit}' for t in tags) + '\n'
            checked = subprocess.run(['git', 'cat-file', '--batch-check'], cwd=self.repo, input=query,
                                     capture_output=True, text=True, encoding='utf-8')
            assert checked.returncode == 0, checked.stderr
            resolved = checked.stdout.splitlines()
            assert len(resolved) == len(tags) and all(' commit ' in line for line in resolved), 'a tag does not resolve to a commit'
        docs = 0
        for sha, record in self.records().items():
            kind = self.classification(sha)
            day = record[4].get('In-force', [''])[0]
            if kind == 'documentation':
                docs += 1
            else:
                assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', day), f'{sha}: missing/malformed In-force {day!r}'
        assert self.classification(self.git('rev-parse', 'main').strip()) == 'documentation', 'main must end with documentation'
        return f'{len(tags)} tags resolve; {len(self.records()) - docs} dated law/correction commits; {docs} labelled documentation commits'

    def lexifina(self):
        maintainers = 0
        for sha, (author, email, committer, committer_email, _) in self.records().items():
            kind = self.classification(sha)
            assert committer == 'Lexifina' and committer_email == 'spain-law@lexifina.com', f'{sha}: invalid committer identity'
            if author == 'Lexifina':
                maintainers += 1
                assert email == 'spain-law@lexifina.com' and kind in ('documentation', 'correction', 'legacy sourced record'), f'{sha}: invalid maintainer author'
            else:
                assert email.endswith('@boe.invalid'), f'{sha}: normative author email not at boe.invalid'
        return f'{maintainers} maintainer commits classified and validated; all normative author and committer identities valid'

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
    ap.add_argument('--pin', default=None, help='immutable published baseline for read-only legacy metadata handling')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    s = Smoke(Path(args.repo) if args.repo else default_repo(), args.pin)
    s.check('blame names a norm', s.blame)
    s.check('text before and after an amendment', s.on_date)
    s.check('log --follow in date order', s.follow)
    s.check('tags resolve, In-force on every law commit', s.tags_and_trailers)
    s.check('maintainer documentation/corrections and norm identities', s.lexifina)
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
