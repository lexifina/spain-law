"""Spanish law on a date, including the explicitly ranged repeal corrections.

python tools/eslaw.py on YYYY-MM-DD estatal/<rango>/<year>/<BOE-id>[/block.md]
python tools/eslaw.py log estatal/<rango>/<year>/<BOE-id>[/block.md]

Law versions are selected by In-force; corrections are applied only to their
listed act and date range. A directory lists its entries on that date.
"""
import json,re,subprocess,sys
DATE=re.compile(r'\d{4}-\d{2}-\d{2}$')
def git(*args,allow_missing=False):
    p=subprocess.run(['git',*args],capture_output=True,text=True,encoding='utf-8')
    if p.returncode and not allow_missing:raise RuntimeError(p.stderr.strip())
    return None if p.returncode else p.stdout
def facts():
    raw=git('show','main:data/acts.json',allow_missing=True)
    return json.loads(raw)['acts'] if raw else []
def commit_on(day,path):
    lines=git('log','--first-parent','--no-merges','--format=%H%x09%(trailers:key=In-force,valueonly,separator=)%x09%(trailers:key=Kind,valueonly,separator=)%x09%(trailers:key=Act-path,valueonly,separator=)%x09%(trailers:key=Corrects,valueonly,separator=)','main','--',path).splitlines()
    ordinary=[];corrections=[]
    for line in lines:
        sha,inf,kind,act,corrects=[s.strip() for s in line.split('\t')]
        if not inf or inf>day:continue
        if kind=='correction':
            if path!=act and not path.startswith(act+'/'):continue
            match=re.search(r' (\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})?$',corrects)
            if not match or day<match[1] or match[2] and day>match[2]:continue
            corrections.append((sha,inf))
        else:ordinary.append((sha,inf))
    if corrections:return corrections[0][0]
    # Published same-day/backfill restatements are ordered explicitly in main.
    # Preserve the published reader's first eligible commit for ordinary text.
    return ordinary[0][0] if ordinary else ''
def show(day,path):
    path=path.rstrip('/')
    manifest=json.loads(git('show','main:corpus.json'))
    cutoff=manifest.get('record_to')
    if cutoff and day>cutoff:
        print(f'{path}: date {day} is outside the verified record, which ends {cutoff}',file=sys.stderr);return 1
    sha=commit_on(day,path)
    if not sha:
        print(f'{path}: nothing in force on {day} in this record',file=sys.stderr);return 1
    kind=git('cat-file','-t',f'{sha}:{path}',allow_missing=True)
    if kind is None:
        row=next((r for r in facts() if path==r['path'] or path.startswith(r['path']+'/')),None)
        label=f'repealed from {row["repealed"]} by {row["repealed_by"]}' if row and row.get('repealed') else 'absent in the selected version'
        print(f'{path}: {label}',file=sys.stderr);return 1
    if kind.strip()=='blob':sys.stdout.write(git('show',f'{sha}:{path}'));return 0
    entries=git('ls-tree',sha,path+'/').splitlines()
    names=[line.split('\t',1)[1] for line in entries]
    if path+'/README.md' in names:
        readme=git('show',f'{sha}:{path}/README.md')
        sys.stdout.write(readme.split('## Bloques')[0].rstrip()+'\n')
        for fname in re.findall(r'\]\(([^)]+\.md)\)$',readme,re.M):
            text=git('show',f'{sha}:{path}/{fname}',allow_missing=True)
            if text is not None:sys.stdout.write(f'\n<!-- {fname} -->\n'+text)
        return 0
    repealed={r['path'] for r in facts() if r.get('repealed') and r['repealed']<=day}
    sys.stdout.write('\n'.join(line for line in entries if line.split('\t',1)[1] not in repealed)+'\n')
    return 0
def main(args):
    try:
        if len(args)>=3 and args[0]=='on' and DATE.fullmatch(args[1]):return show(args[1],args[2])
        if len(args)>=2 and DATE.fullmatch(args[0]):return show(args[0],args[1])
        if len(args)>=2 and args[0]=='log':
            out=git('log','--first-parent','--format=%(trailers:key=In-force,valueonly,separator=)%x09%an','main','--',args[1])
            sys.stdout.write('\n'.join(line for line in out.splitlines() if line.split('\t')[0])+'\n');return 0
        print(__doc__,file=sys.stderr);return 2
    except RuntimeError as exc:print(str(exc),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main(sys.argv[1:]))
