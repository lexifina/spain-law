"""Rebuild visualisations/el-derecho-espanol-en-20-graficos.html from this repository.

    python visualisations/src/make.py [--repo PATH] [--ref REF] [--history-ref REF] [--skip-extract]

Steps (all read-only on the repository; scratch output goes to visualisations/src/.build/):
  1. git log of REF (default origin/main), streamed: one line per commit with its author (the norm the BOE credits
     for the change), its trailers (In-force, Published, Enacted, Norma, Kind, Corrects, Redates) and the norms its
     message lists, with the number of blocks it wrote in each and whether it is that norm's first text  -> .build/log.tsv
  2. git log --name-status of HISTORY-REF (default origin/law-head, the last commit of the BOE build, so that the
     restore commit 57854db on main, which rewrote every file, does not count as a change):
     - for the Constitution, the Código Civil and the Código Penal, every file each commit added or modified
                                                                                        -> .build/codes-names.tsv
     - for every file under estatal/, how many commits added and modified it (and, for the most rewritten, which)
                                                                                        -> .build/file-mods.tsv
  3. the tree of REF: the number of files of each norm, and the blob ids the charts read  -> .build/norm-files.tsv
  4. the tables: normas.tsv, corpus.json, data/acts.json, data/date-corrections.tsv      -> .build/repo/
  5. the blobs the charts read, listed from the trees:
     - the BOE's notes (no.md) and related information (ir.md) of every real decreto-ley, as the BOE build left them
       on HISTORY-REF: they record the Congreso's convalidation or derogation             -> .build/rdl-notes.jsonl
     - the README.md (block list, in the BOE's order) of the Constitution, the Código Civil, the Código Penal and of
       the norms that hold the most rewritten blocks                                       -> .build/readmes.jsonl
     - every block of the Constitution, the Código Civil and the Código Penal              -> .build/codes.jsonl
     - the 40 blocks the most commits rewrote (for their headings)                         -> .build/top-blocks.jsonl
  6. prep.py turns those into .build/data.json; build.py fills page.tpl.html with it.
In a partial (blobless) clone the missing blobs are fetched in batches, some 4,000 small files in all; no other text
is read. The history is streamed line by line: nothing large is held in memory.
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument('--repo', default=os.path.abspath(os.path.join(HERE, '..', '..')))
ap.add_argument('--ref', default=None, help='default: origin/main if present, else HEAD')
ap.add_argument('--history-ref', default=None, help='default: origin/law-head if present, else the same as --ref')
ap.add_argument('--out', default=os.path.join(HERE, '..', 'el-derecho-espanol-en-20-graficos.html'))
ap.add_argument('--skip-extract', action='store_true', help='reuse .build/ from a previous run (prep and build only)')
a = ap.parse_args()
B = os.path.join(HERE, '.build')
os.makedirs(B, exist_ok=True)
NOLAZY = dict(os.environ, GIT_NO_LAZY_FETCH='1')
GIT = ['git', '-C', a.repo, '-c', 'core.quotepath=off']


def git(*args, **kw):
    return subprocess.run([*GIT, *args], check=True, capture_output=True, env=NOLAZY, **kw).stdout


def has(ref):
    return subprocess.run([*GIT, 'rev-parse', '--verify', '-q', ref], capture_output=True).returncode == 0


ref = a.ref or ('origin/main' if has('origin/main') else 'HEAD')
href = a.history_ref or ('origin/law-head' if has('origin/law-head') else ref)
sha = git('rev-parse', ref).decode().strip()
hsha = git('rev-parse', href).decode().strip()
print('ref', ref, sha, '| history', href, hsha, flush=True)

CONST = 'estatal/constitucion/1978/BOE-A-1978-31229'
CC = 'estatal/real-decreto/1889/BOE-A-1889-4763'
CP = 'estatal/ley-organica/1995/BOE-A-1995-25444'
CODES = [CONST, CC, CP]
TRAILERS = ['In-force', 'Published', 'Enacted', 'Norma', 'Kind', 'Corrects', 'Redates', 'Re-asserts', 'Laws-changed']
TGT = re.compile(r'^- (.*) \((BOE-[A-Z]-\d{4}-\d+)\): (.*)$')
MORE = re.compile(r' \.\.\. \(\+(\d+)\)$')


def fetch_missing(oids, batch=4000):
    """batched fetches for the blobs a partial clone does not have yet"""
    oids = sorted(set(oids))
    chk = subprocess.run([*GIT, 'cat-file', '--batch-check'], input=''.join(o + '\n' for o in oids).encode(),
                         capture_output=True, env=NOLAZY).stdout.decode().split('\n')
    missing = [l.split()[0] for l in chk if l.endswith(' missing')]
    for i in range(0, len(missing), batch):
        part = missing[i:i + batch]
        print('fetching', len(part), 'blobs', f'({i + len(part)} of {len(missing)})', flush=True)
        subprocess.run([*GIT, '-c', 'fetch.negotiationAlgorithm=noop', 'fetch', 'origin', '--no-tags', '--no-write-fetch-head',
                        '--recurse-submodules=no', '--filter=blob:none', '--stdin'], input=''.join(m + '\n' for m in part).encode(), check=False)


def read_blobs(items):
    """yield (path, bytes) for (oid, path) pairs, one blob at a time"""
    p = subprocess.Popen([*GIT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=NOLAZY)
    for oid, path in items:
        p.stdin.write((oid + '\n').encode()); p.stdin.flush()
        head = p.stdout.readline().split()
        if len(head) < 3:
            sys.exit('cannot read ' + path)
        data = p.stdout.read(int(head[2])); p.stdout.read(1)
        yield path, data
    p.stdin.close(); p.wait()


def jsonl(name, items):
    with open(os.path.join(B, name), 'w', encoding='utf-8', newline='\n') as out:
        for path, data in read_blobs(items):
            out.write(json.dumps({'p': path, 't': data.decode('utf-8', 'replace')}, ensure_ascii=False) + '\n')


def tree(r, *paths):
    """(path, oid) of every file of the tree of r under paths, streamed"""
    lt = subprocess.Popen([*GIT, 'ls-tree', '-r', '-z', r, '--', *paths], stdout=subprocess.PIPE, env=NOLAZY)
    buf = b''
    for chunk in iter(lambda: lt.stdout.read(1 << 16), b''):
        buf += chunk
        *ents, buf = buf.split(b'\0')
        for e in ents:
            meta, path = e.split(b'\t', 1)
            yield path.decode('utf-8'), meta.split()[2].decode()
    lt.wait()


def norm_of(path):
    """estatal/<rank>/<year>/<BOE id>/<block>.md -> the norm's folder"""
    p = path.split('/')
    return '/'.join(p[:4]) if len(p) >= 5 and p[0] == 'estatal' else None


if not a.skip_extract:
    # 1. the history of REF, streamed (a trailer that occurs more than once is joined with " ; ")
    fmt = '%x1e%H%x1f%an%x1f%ae%x1f%s%x1f%(trailers:unfold,separator=%x1d)%x1f%b'
    lg = subprocess.Popen([*GIT, 'log', ref, '--format=' + fmt], stdout=subprocess.PIPE, env=NOLAZY)
    n = 0
    with open(os.path.join(B, 'log.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        out.write('\t'.join(['i', 'sha', 'kind', 'author', 'subject'] + TRAILERS + ['targets']) + '\n')

        def emit(rec):
            global n
            rec = rec.decode('utf-8', 'replace').strip('\n')
            if not rec:
                return
            parts = rec.split('\x1f')
            h, an, ae, subj = parts[:4]
            tr = {}
            for t in (parts[4] if len(parts) > 4 else '').split('\x1d'):
                k, _, v = t.partition(': ')
                k = k.strip()
                if k and k != 'Files':
                    tr.setdefault(k, []).append(v.strip())
            kind = 'boe' if ae.endswith('@boe.invalid') else (tr.get('Kind', ['lexifina'])[0])
            tg = []
            for line in (parts[5] if len(parts) > 5 else '').split('\n'):
                m = TGT.match(line)
                if m:
                    blocks = m.group(3)
                    more = MORE.search(blocks)
                    nb = len([b for b in MORE.sub('', blocks).split(', ') if b]) + (int(more.group(1)) if more else 0)
                    tg.append([m.group(2), nb, ''])
                elif line.strip().startswith('First text of this norm') and tg:
                    tg[-1][2] = 'F'
            row = [str(n), h, kind, an, subj] + [' ; '.join(tr.get(k, [])) for k in TRAILERS] + ['|'.join(f'{i}:{b}:{f}' for i, b, f in tg)]
            out.write('\t'.join(x.replace('\t', ' ').replace('\n', ' ') for x in row) + '\n')
            n += 1
        buf = b''
        for chunk in iter(lambda: lg.stdout.read(1 << 16), b''):
            buf += chunk
            *recs, buf = buf.split(b'\x1e')
            for r in recs:
                emit(r)
        emit(buf)
    lg.wait()
    print('commits', n, flush=True)

    # 2. files written by each commit of the history ref: the codes in full, every file as counts
    lg = subprocess.Popen([*GIT, 'log', href, '--format=@@C %H', '--name-status', '--no-renames', '--', 'estatal'], stdout=subprocess.PIPE, env=NOLAZY)
    cur, cnt, shas, nc = None, {}, {}, 0
    with open(os.path.join(B, 'codes-names.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        for raw in lg.stdout:
            l = raw.decode('utf-8', 'replace').rstrip('\n')
            if l.startswith('@@C '):
                cur = l[4:]
                continue
            if not l or not cur:
                continue
            st, _, f = l.partition('\t')
            st = st[:1]
            if any(f.startswith(c + '/') for c in CODES):
                out.write(f'{cur}\t{st}\t{f}\n')
                nc += 1
            if f.endswith('/README.md'):
                continue
            c = cnt.get(f)
            if c is None:
                c = cnt[f] = [0, 0]
            if st == 'A':
                c[0] += 1
            elif st == 'M':
                c[1] += 1
                shas.setdefault(f, []).append(cur[:12])
    lg.wait()
    with open(os.path.join(B, 'file-mods.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        for f, (na, nm) in cnt.items():
            if nm:
                out.write(f'{f}\t{na}\t{nm}\t{",".join(shas[f]) if nm >= 12 else ""}\n')
    print('code file changes', nc, '| files ever modified', sum(1 for v in cnt.values() if v[1]), flush=True)
    top_files = sorted(((v[1], f) for f, v in cnt.items() if v[1]), reverse=True)[:60]
    del cnt, shas

    # 3. the tree of REF: files per norm, and the blob ids the charts read
    files, readme, code_blobs, tables, top_blobs = {}, {}, [], [], []
    topset = {f for _, f in top_files[:40]}
    for p, oid in tree(ref):
        if p in topset:
            top_blobs.append((oid, p))
        if p in ('normas.tsv', 'corpus.json', 'data/acts.json', 'data/date-corrections.tsv'):
            tables.append((oid, p))
            continue
        fo = norm_of(p)
        if not fo:
            continue
        if p.endswith('/README.md'):
            readme[fo] = oid
        else:
            files[fo] = files.get(fo, 0) + 1
        if fo in CODES and p.endswith('.md') and not p.endswith('/README.md'):
            code_blobs.append((oid, p))
    with open(os.path.join(B, 'norm-files.tsv'), 'w', encoding='utf-8', newline='\n') as out:
        for fo in sorted(set(files) | set(readme)):
            out.write(f'{fo}\t{files.get(fo, 0)}\n')
    print('norms in the tree', len(readme), '| code blocks', len(code_blobs), flush=True)

    # 4. the tables
    fetch_missing([o for o, _ in tables])
    R = os.path.join(B, 'repo')
    for path, data in read_blobs(tables):
        dst = os.path.join(R, *path.split('/'))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'wb') as fh:
            fh.write(data)

    # 5. the blobs the charts read
    notes = [(oid, p) for p, oid in tree(href, 'estatal/real-decreto-ley') if p.endswith('/no.md') or p.endswith('/ir.md')]
    want = set(CODES) | {norm_of(f) for _, f in top_files}
    readmes = [(readme[fo], fo + '/README.md') for fo in sorted(want) if fo in readme]
    print('rdl notes', len(notes), '| readmes', len(readmes), flush=True)
    fetch_missing([o for o, _ in notes + readmes + code_blobs + top_blobs])
    jsonl('rdl-notes.jsonl', notes)
    jsonl('readmes.jsonl', readmes)
    jsonl('codes.jsonl', code_blobs)
    jsonl('top-blocks.jsonl', top_blobs)

# 6. prep + build
env = dict(os.environ, HEAD_SHA=sha, HISTORY_SHA=hsha)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'prep.py'), B], check=True, env=env)
subprocess.run([sys.executable, '-X', 'utf8', os.path.join(HERE, 'build.py'), os.path.join(B, 'data.json'), os.path.abspath(a.out)], check=True)
