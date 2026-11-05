"""Dated Spanish law records and BOE lifecycle status.

python tools/eslaw.py on YYYY-MM-DD estatal/<rango>/<year>/<BOE-id>[/block.md]
python tools/eslaw.py current YYYY-MM-DD estatal/<rango>/<year>/<BOE-id>[/block.md]
python tools/eslaw.py status YYYY-MM-DD estatal/<rango>/<year>/<BOE-id>[/block.md]
python tools/eslaw.py log estatal/<rango>/<year>/<BOE-id>[/block.md]

The on command preserves access to the dated historical record. It does not
establish legal applicability or revival. The current command applies recorded
lifecycle boundaries; status reports dated BOE repeal/annulment metadata.
Corrections apply only to their listed act and date range.
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
def is_publisher_record(row,path):
    """Recognize retained BOE notices from metadata or published README links."""
    act=row['path']
    if path==act+'/README.md':return True
    notice=row.get('lifecycle_notice')
    if notice and path==act+'/'+notice:return True
    readme=git('show','main:'+act+'/README.md',allow_missing=True) or ''
    notices={act+'/'+name for name in re.findall(r'^- \[BOE publisher notice\]\(([^)]+\.md)\)$',readme,re.M)}
    if path in notices:return True
    if path==act and notices:
        entries=git('ls-tree','--name-only','main',act+'/').splitlines()
        return bool(entries) and set(entries)<={act+'/README.md'}|notices
    return False

def show_current(day,path):
    path=path.rstrip('/')
    rows=facts()
    row=next((r for r in rows if path==r['path'] or path.startswith(r['path']+'/')),None)
    if row:
        ended=[(row.get('repealed'),'repealed'),(row.get('annulled'),'annulled')]
        ended=sorted((date,label) for date,label in ended if date and date<=day)
        if ended:
            date,label=ended[0]
            cause=(' by '+str(row['repealed_by'])) if label=='repealed' and row.get('repealed_by') else ''
            notice=row.get('lifecycle_notice')
            inspecting_notice=is_publisher_record(row,path)
            if inspecting_notice and row.get('lifecycle_notice_historical'):
                print(f'{path}: historical publisher notice; BOE lifecycle metadata records {label} from {date}{cause}; current source: {row["lifecycle_notice_source"]}',file=sys.stderr)
            later=row.get('lifecycle_later_provisions',{}).get(path.rsplit('/',1)[-1])
            after_later=later and later['from']<=day and (not later.get('until') or day<later['until'])
            if after_later:
                print(f'{path}: BOE records the act {label} from {date}; this provision has a later amendment by {later["by"]} from {later["from"]}',file=sys.stderr)
            if not inspecting_notice and not after_later:
                scope='; retained wording may have saved or transitional application; this reader cannot determine applicability' if row.get('lifecycle_scope_unresolved') else ''
                print(f'{path}: BOE records {label} from {date}{cause}{scope}',file=sys.stderr);return 1
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
    repealed={r['path'] for r in rows if any(r.get(key) and r[key]<=day for key in ('repealed','annulled'))}
    sys.stdout.write('\n'.join(line for line in entries if line.split('\t',1)[1] not in repealed)+'\n')
    return 0
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
def status(day,path):
    row=next((r for r in facts() if path==r['path'] or path.startswith(r['path']+'/')),None)
    if row is None:
        print(f'{path}: act is not in this record',file=sys.stderr);return 1
    manifest=json.loads(git('show','main:corpus.json'))
    checked=manifest.get('lifecycle_checked_on',manifest.get('record_to'))
    if checked and day>checked:
        print(f'{path}: date {day} is outside the lifecycle record, which ends {checked}',file=sys.stderr);return 1
    ended=sorted((date,label) for date,label in [(row.get('repealed'),'repealed'),(row.get('annulled'),'annulled')] if date and date<=day)
    later=row.get('lifecycle_later_provisions',{}).get(path.rsplit('/',1)[-1])
    active_later=later if later and later['from']<=day and (not later.get('until') or day<later['until']) else None
    result={'id':row['id'],'path':row['path'],'day':day,'repealed':row.get('repealed'),'repealed_by':row.get('repealed_by'),'annulled':row.get('annulled'),'cessation_effective':bool(ended),'recorded_lifecycle':ended[0][1] if ended else None,'scope_unresolved':bool(row.get('lifecycle_scope_unresolved')),'later_source_provision':active_later,'source':row.get('repeal_source') or row['url']}
    print(json.dumps(result,ensure_ascii=False,sort_keys=True));return 0

def main(args):
    try:
        if len(args)>=3 and args[0]=='status' and DATE.fullmatch(args[1]):return status(args[1],args[2])
        if len(args)>=3 and args[0]=='current' and DATE.fullmatch(args[1]):return show_current(args[1],args[2])
        if len(args)>=3 and args[0]=='on' and DATE.fullmatch(args[1]):return show(args[1],args[2])
        if len(args)>=2 and DATE.fullmatch(args[0]):return show(args[0],args[1])
        if len(args)>=2 and args[0]=='log':
            out=git('log','--first-parent','--format=%(trailers:key=In-force,valueonly,separator=)%x09%an','main','--',args[1])
            sys.stdout.write('\n'.join(line for line in out.splitlines() if line.split('\t')[0])+'\n');return 0
        print(__doc__,file=sys.stderr);return 2
    except RuntimeError as exc:print(str(exc),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main(sys.argv[1:]))
