"""Append source-backed BOE lifecycle notices while preserving published metadata.

Every change is a correction on the supplied published base. Existing repeal and
annulment fields are preserved; unambiguous whole-act repeals may remove files,
while qualified notices retain the historical wording and mark the act README.
"""
import copy,datetime as dt,json,re

def index_document(published,changes,day):
    import corpus_tables as tables
    result=copy.deepcopy(published)
    rows={row['id']:row for row in result['acts']}
    for change in changes:
        row=rows[change['id']]
        row['lifecycle_scope_unresolved']=change.get('scope_unresolved',not change['remove'])
        if change.get('note_file'):row['lifecycle_notice']=change['note_file']
        if change.get('later_provisions'):row['lifecycle_later_provisions']=change['later_provisions']
        if change.get('notice_historical'):
            row['lifecycle_notice_historical']=True
            row['lifecycle_notice_source']=change['notice_source_url']
        if change.get('cause_correction'):
            assert row.get('repealed_by')==change['cause_correction']['previous']
            row['repealed_by']=change['cause_correction']['by']
            row['repeal_cause_source']=change['notice_source_url']
        if change['kind']=='annulment':
            assert row.get('annulled')==change['date']
            continue
        assert not row.get('repealed') or row['repealed']==change['date']
        if row.get('repealed'):
            # Preserve the publisher's existing cause, including qualifications.
            continue
        act={'slug':row['path'],'id':row['id'],'title':row['title'],'short':row['short'],
             'law_kind':row['law_kind'],'enacted':row['enacted'],'published':row['published'],
             'in_force':row['in_force'],'status':'repealed','first_law':None,'url':row['url'],
             'repealed':change['date'],'repealed_by':change['by'],
             'versions':[{'from':row['in_force'] or row['published'],'units':{},'in_force_known':bool(row['in_force'])}]}
        generated=tables.acts_document({'acts':[act],'laws':{},'country':{'code':'ES'}},day)['acts'][0]
        for key in ('status','repealed','repealed_by'):row[key]=generated[key]
        row['repeal_source']=change['source_url']
        row['repeal_basis']=change['date_basis']
        row['status_note']='The BOE initial notice states this repeal date and cause.'
    return result

def build(repo,base,changes,docs,git):
    assert git(repo,'rev-parse','main').decode().strip()==base
    stream=bytearray();mark=0
    timestamp=int(git(repo,'show','-s','--format=%ct',base))
    def emit(day,message,files,delete=None):
        nonlocal mark
        mark+=1
        from zoneinfo import ZoneInfo
        when=dt.datetime.combine(dt.date.fromisoformat(day),dt.time(12),ZoneInfo('Europe/Madrid'))
        stamp=f'{int(when.timestamp())} {when.strftime("%z")}' if day>='1970-01-01' else f'{mark} +0000'
        body=message.encode('utf-8')
        stream.extend(f'commit refs/heads/main\nmark :{mark}\nauthor Lexifina <spain-law@lexifina.com> {stamp}\ncommitter Lexifina <spain-law@lexifina.com> {timestamp+mark} +0000\ndata {len(body)}\n'.encode()+body+b'\n')
        stream.extend(f'from {base if mark==1 else ":"+str(mark-1)}\n'.encode())
        if delete:stream.extend(f'D {delete}\n'.encode())
        for path,text in sorted(files.items()):
            body=text.encode('utf-8') if isinstance(text,str) else text
            stream.extend(f'M 100644 inline {path}\ndata {len(body)}\n'.encode()+body+b'\n')
        stream.extend(b'\n')
    for change in sorted(changes,key=lambda c:(c['date'],c['id'])):
        path=change['path'];date=change['date'];kind=change['kind']
        label='annulment' if kind=='annulment' else 'repeal'
        action='Remove the unambiguously repealed normative files; retain the unchanged BOE notice.' if change['remove'] else 'Mark the BOE lifecycle date; retain the existing wording and publisher notices, including qualifications.'
        section=f'\n\n## {label.capitalize()}\n\nBOE records this act as {"annulled" if kind=="annulment" else "repealed"} with effect from {date}. '
        if change.get('by'):section+=f'The recorded cause is {change["by"]}. '
        section+='See the publisher notice for qualifications and transitional provisions. Earlier wording remains available in the history.\n'
        if change.get('notice_historical'):
            section+=f'\nThe retained publisher notice reproduces an earlier BOE publication state and is historical. Its wording differs from the latest source notice used for this record. The dated lifecycle marker above and the act index give the recorded lifecycle date; consult the [BOE source]({change["notice_source_url"]}) for the current notice. No wording in the retained notice has been changed.\n'
        original=change['readme'];prefix,sep,blocks=original.partition('## Bloques')
        readme=prefix.rstrip()+section
        files={path+'/README.md':readme+(('\n## Bloques\n\n- [BOE publisher notice]('+change['note_file']+')\n') if change['remove'] else '\n'+sep+blocks)}
        if change['remove']:files[path+'/'+change['note_file']]=change['source_note']
        listed=change['files'] if change['remove'] else [path+'/README.md']
        end=change.get('corrects_to',docs['record_to'])
        message=f'Correction: {label} {change["id"]} from {date}\n\n{action}\n\nKind: correction\nIn-force: {date}\nCorrects: {path} {date}..{end}\nSupersedes: {change["supersedes"]}\nReason: {action}\nAct-path: {path}\nSource: {change["source_url"]}\nIn-force-basis: {change["date_basis"]}\n'
        if change.get('by'):message+=f'Norma: {change["by"]}\n'
        message+=''.join(f'Files: {p}\n' for p in listed)
        emit(date,message,files,path if change['remove'] else None)
    emit(docs['day'],'Spanish law: preserve BOE lifecycle dates and mark surviving repealed acts\n\nKind: documentation\n',docs['files'])
    stream.extend(b'done\n')
    git(repo,'fast-import','--quiet','--done',input=bytes(stream),timeout=300)
    return git(repo,'rev-parse','main').decode().strip()
