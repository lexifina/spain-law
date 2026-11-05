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
"""File-specific correction selection for Spain's existing reader."""
from functools import lru_cache

@lru_cache(maxsize=None)
def correction_rows():
    fmt='%H%x1e%(trailers:key=Kind,valueonly,separator=)%x1e%(trailers:key=Act-path,valueonly,separator=)%x1e%(trailers:key=Corrects,valueonly,separator=)%x1e%(trailers:key=Files,valueonly,separator=%x1f)%x1d'
    rows=[]
    for raw in git('log','--first-parent','--no-merges','--format='+fmt,'main').split('\x1d'):
        parts=raw.strip('\n').split('\x1e')
        if len(parts)!=5:continue
        sha,kind,act,corrects,files=[x.strip() for x in parts]
        if kind!='correction':continue
        match=re.search(r' (\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})?$',corrects)
        if match:rows.append((sha,act,match[1],match[2],frozenset(x.strip() for x in files.split('\x1f') if x.strip())))
    return rows

@lru_cache(maxsize=None)
def ordinary_rows(path):
    fmt='%H%x09%(trailers:key=In-force,valueonly,separator=)%x09%(trailers:key=Kind,valueonly,separator=)'
    rows=[]
    for line in git('log','--first-parent','--no-merges','--format='+fmt,'main','--',path).splitlines():
        parts=line.split('\t')
        if len(parts)!=3:continue
        sha,day,kind=[x.strip() for x in parts]
        if day and kind!='correction':rows.append((sha,day))
    return rows

def commit_on(day,path):
    # Corrections replace their listed files, not every sibling in their tree.
    for sha,act,start,end,files in correction_rows():
        if path not in files or day<start or end and day>end:continue
        if not end:
            next_days=[d for _,d in ordinary_rows(act) if d>start]
            if next_days and day>=min(next_days):continue
        return sha
    # Keep the published ordering of ordinary source restatements.
    return next((sha for sha,inf in ordinary_rows(path) if inf<=day),'')

def text_on(day,path):
    sha=commit_on(day,path)
    return git('show',f'{sha}:{path}',allow_missing=True) if sha else None

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

def render_tree(day,path,sha):
    """Read the ordinary act tree and overlay only listed correction files."""
    raw=git('ls-tree','-z',sha+':'+path)
    refs={};entries=[]
    for record in raw.split('\0'):
        meta,sep,name=record.partition('\t')
        if sep:entries.append((meta,path+'/'+name))
        if sep and meta.split()[1]=='blob' and name.endswith('.md'):
            refs[path+'/'+name]=meta.split()[2]
    if not refs:
        ended={row['path'] for row in facts() if any(row.get(key) and row[key]<=day for key in ('repealed','annulled'))}
        sys.stdout.write('\n'.join(meta+'\t'+name for meta,name in entries if name not in ended)+'\n')
        return 0
    corrected=set()
    for commit,act,start,end,files in correction_rows():
        if act!=path or day<start or end and day>end:continue
        if not end:
            future=[d for _,d in ordinary_rows(act) if d>start]
            if future and day>=min(future):continue
        for name in files:
            if name in corrected or not name.startswith(path+'/') or not name.endswith('.md'):continue
            refs[name]=commit+':'+name;corrected.add(name)
    names=list(refs)
    result=subprocess.run(['git','cat-file','--batch'],input=''.join(refs[n]+'\n' for n in names).encode(),capture_output=True)
    if result.returncode:raise RuntimeError(result.stderr.decode('utf-8','replace').strip())
    bodies={};offset=0
    for name in names:
        stop=result.stdout.index(b'\n',offset);header=result.stdout[offset:stop].split();offset=stop+1
        if len(header)<3:
            if re.fullmatch(r'[0-9a-f]{40}',refs[name]):raise RuntimeError('recorded law blob is unavailable: '+name)
            bodies[name]=None;continue
        size=int(header[2]);bodies[name]=result.stdout[offset:offset+size].decode('utf-8');offset+=size+1
    readme=bodies.get(path+'/README.md')
    if readme is not None:
        sys.stdout.write(readme.split('## Bloques')[0].rstrip()+'\n')
        for name in re.findall(r'\]\(([^)]+\.md)\)$',readme,re.M):
            body=bodies.get(path+'/'+name)
            if body is not None:sys.stdout.write('\n<!-- '+name+' -->\n'+body)
    else:
        sys.stdout.write('\n'.join(name for name in names if bodies.get(name) is not None)+'\n')
    return 0


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
    if kind.strip()=='blob':
        text=text_on(day,path)
        if text is None:return 1
        sys.stdout.write(text);return 0
    return render_tree(day,path,sha)

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
    if kind.strip()=='blob':
        text=text_on(day,path)
        if text is None:return 1
        sys.stdout.write(text);return 0
    return render_tree(day,path,sha)

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
