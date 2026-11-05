"""Append source-backed whole-act repeal corrections to a Spanish law repository.

The original history, tags and normative wording are preserved. Inputs are the
repository's normas.tsv, its published note blocks, and the original BOE XML cache.
Public acts metadata uses corpus_tables from the specified pinned toolchain.
"""
import argparse,csv,datetime as dt,gzip,hashlib,io,json,pathlib,re,sqlite3,sys

MONTHS={m:i+1 for i,m in enumerate('enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre'.split())}
IDENT=re.compile(r'BOE-[A-Z]-\d{4}-\d+')
def iso(value):
    if not value:return None
    if len(value)==8:value=f'{value[:4]}-{value[4:6]}-{value[6:]}'
    try:return dt.date.fromisoformat(value).isoformat()
    except ValueError:return None
def date_from_note(text):
    prefix=r'(?:con efectos (?:a partir del?|desde el|desde|del|de|a)|derogada(?:,)? (?:a partir del?|desde(?: el)?))'
    matches=re.findall(prefix+r' (\d{1,2}) de ([a-z]+) de (\d{4})',text,re.I)
    dates={dt.date(int(y),MONTHS[m.lower()],int(d)).isoformat() for d,m,y in matches}
    if len(dates)>1:raise ValueError('conflicting explicit effective dates')
    if not dates and re.search(r'\befectos\b|derogada(?:,)? (?:a partir|desde)',text,re.I):
        raise ValueError('effective-date wording requires separate source analysis')
    return next(iter(dates)) if dates else None
def whole_repeal(text):
    if not re.search(r'\bNorma derogada\b',text,re.I):return False
    # Qualifiers can preserve normative text or make the date conditional. Such
    # cases need a scoped source analysis before any whole-act removal.
    limited=re.search(r'\b(?:salvo|except\w*|excepci[oó]n\w*|salvedad|parcialmente|en aquellos|en lo que|en tanto|en la forma|si bien|sin perjuicio|no obstante|a partir del momento|cuando|en el mismo d[ií]a|d[ií]a en el que|entre en vigor|ser[aá] de aplicaci[oó]n|condici\w*|supeditad\w*|mantien\w*|mantendr\w*|continu\w*|seguir\w*|subsist\w*|permanec\w*|perviven\w*|transitori\w*|con efectos para|se aplicar[aá])\b',text,re.I)
    return not limited
def prefetch(repo,oids,git):
    query=('\n'.join(sorted(set(oids)))+'\n').encode()
    present=git(repo,'--no-lazy-fetch','cat-file','--batch-check=%(objectname) %(objecttype)',input=query)
    missing=[line.split()[0].decode() for line in present.splitlines() if line.endswith(b' missing')]
    if missing:
        print('Prefetching',len(missing),'source-identified blobs',flush=True)
        git(repo,'-c','fetch.negotiationAlgorithm=noop','fetch','--no-tags','--no-write-fetch-head','--recurse-submodules=no','--filter=blob:none','origin','--stdin',input=('\n'.join(missing)+'\n').encode(),timeout=600)
def blob_batch(repo,specs,run,record):
    # All input blobs have been prefetched together; this process makes no network request.
    import subprocess
    p=subprocess.Popen(['git','cat-file','--batch'],cwd=repo,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    record(p.pid)
    result={}
    try:
        for spec in specs:
            p.stdin.write((spec+'\n').encode());p.stdin.flush()
            h=p.stdout.readline().split()
            if len(h)!=3 or h[1]!=b'blob':raise ValueError('Missing input '+spec)
            size=int(h[2]);result[spec]=p.stdout.read(size);assert p.stdout.read(1)==b'\n'
    finally:
        p.stdin.close();p.wait()
    return result
def make_plan(repo,base,cache,day,git,record):
    import boe
    raw=git(repo,'show',base+':normas.tsv')
    rows=list(csv.DictReader(io.StringIO(raw.decode('utf-8')),delimiter='\t'))
    tree={}
    for item in git(repo,'ls-tree','-rz',base).split(b'\0'):
        if not item:continue
        meta,path=item.split(b'\t',1);tree[path.decode('utf-8')]=meta.split()[2].decode()
    act_files={}
    for path in tree:
        parts=path.split('/')
        if len(parts)>=5 and parts[0]=='estatal':
            act_files.setdefault('/'.join(parts[:4]),[]).append(path)
    db=sqlite3.connect(f'file:{cache / "boe.sqlite"}?mode=ro',uri=True)
    parsed=sqlite3.connect(f'file:{cache / "parsed.sqlite"}?mode=ro',uri=True)
    from xml.etree import ElementTree as ET
    fvig={r[0]:iso(r[1]) for r in parsed.execute('select id,fvig from laws')}
    publication={r[0]:iso(r[1]) for r in parsed.execute('select id,fpub from laws')}
    proposed=[];held=[]
    for row in rows:
        if row['vigencia_agotada']!='S':continue
        ident=row['id'];path=row['path']
        got=db.execute('select status,body from cache where url=?',(f'https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ident}/texto',)).fetchone()
        if not got or got[0]!=200:
            held.append({'id':ident,'reason':'no successful source XML'});continue
        root=ET.fromstring(gzip.decompress(got[1]))
        hits=[]
        for block in root.findall(".//bloque[@tipo='nota_inicial']"):
            versions=[v for v in block.findall('version') if iso(v.get('fecha_vigencia')) and iso(v.get('fecha_vigencia'))<=day]
            if not versions:continue
            # A later-published BOE correction can move a repeal to an earlier
            # effective date. Select by publication provenance, not the largest
            # effective date, then require equality with the published note.
            version=max(enumerate(versions),key=lambda x:(iso(x[1].get('fecha_publicacion')) or '',x[0]))[1]
            text=' '.join(''.join(version.itertext()).split())
            if not whole_repeal(text):continue
            try:explicit_date=date_from_note(text)
            except (ValueError,KeyError):continue
            if explicit_date and explicit_date!=iso(version.get('fecha_vigencia')):continue
            date=explicit_date or iso(version.get('fecha_vigencia'))
            refs=set(IDENT.findall(text))
            # A version's id_norma can be a later timing amendment. Attribute
            # the repeal only to the single explicit identifier in this notice.
            by=next(iter(refs)) if len(refs)==1 else None
            if not by or not IDENT.fullmatch(by) or by.endswith('-0-0') or by==ident:continue
            repealer_publication=publication.get(by) or iso(version.get('fecha_publicacion'))
            if repealer_publication and date<repealer_publication:continue
            names=parsed.execute('select fname from blocks where law=? and block=? and tipo=?',(ident,block.get('id'),'nota_inicial')).fetchall()
            if len(names)!=1:continue
            fname=names[0][0]+'.md'
            if path+'/'+fname not in tree or path+'/README.md' not in tree:continue
            hits.append({'id':ident,'path':path,'date':date,'version_from':iso(version.get('fecha_vigencia')),'by':by,'note':text,'note_file':fname,'source_note':boe.render(version),
                         'date_basis':'BOE notice effective-date sentence' if explicit_date else 'BOE notice version fecha_vigencia',
                         'published':iso(version.get('fecha_publicacion')),
                         'source_url':f'https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{ident}/texto'})
        if not hits:
            held.append({'id':ident,'reason':'vigencia_agotada=S without an unambiguous dated whole-act repeal in the published initial note'});continue
        chosen=max(hits,key=lambda x:x['date'])
        if chosen['date']>day:
            held.append({'id':ident,'reason':'repeal takes effect after the snapshot date'});continue
        proposed.append(chosen)
    needed=sorted({n['path']+'/'+file for n in proposed for file in [n['note_file'],'README.md']})
    oids=sorted({tree[p] for p in needed})
    if oids:prefetch(repo,oids,git)
    blobs=blob_batch(repo,[base+':'+p for p in needed],git,record)
    accepted=[]
    for n in proposed:
        actual=blobs[base+':'+n['path']+'/'+n['note_file']].decode('utf-8')
        if actual!=n['source_note']:
            held.append({'id':n['id'],'reason':'published note differs from cached source XML version'});continue
        n['readme']=blobs[base+':'+n['path']+'/README.md'].decode('utf-8')
        n['files']=sorted(act_files[n['path']])
        accepted.append(n)
    accepted.sort(key=lambda n:(n['date'],n['id']))
    commits={}
    log=git(repo,'log','--format=%H%x09%(trailers:key=In-force,valueonly,separator=)%x09%(trailers:key=Norma,valueonly,separator=)',base).decode('utf-8')
    for line in log.splitlines():
        sha,date,norma=line.split('\t');commits.setdefault((date.strip(),norma.strip()),sha)
    for n in accepted:n['supersedes']=commits.get((n['version_from'],n['by']),'none')
    return rows,fvig,accepted,held,tree
def index_document(rows,fvig,repeals,tree,day):
    import corpus_tables as T
    import corpus_standard as S
    byid={n['id']:n for n in repeals};acts=[]
    for row in rows:
        r=byid.get(row['id']);exists=row['path']+'/README.md' in tree
        commencement=fvig.get(row['id'])
        status='repealed' if r else 'not yet in force' if commencement and commencement>day else 'as captured' if row['vigencia_agotada']=='S' or not exists else 'in force'
        rango=row['rango'].lower()
        kind='constitution' if 'constitución' in rango else 'act' if rango.startswith('ley') else 'decree-law' if 'decreto-ley' in rango or 'decreto legislativo' in rango else 'decree' if 'decreto' in rango else 'regulation' if rango in ('orden','resolución') else 'other'
        if kind not in S.LAW_KINDS:kind='other'
        act={'slug':row['path'],'id':row['id'],'title':row['titulo'],'short':row['id'],'law_kind':kind,
             'enacted':iso(row['fecha_disposicion']),'published':iso(row['fecha_publicacion']),
             'in_force':fvig.get(row['id']),'status':status,'first_law':None,
             'url':'https://www.boe.es/buscar/act.php?id='+row['id'],
             'versions':[{'from':fvig.get(row['id']) or iso(row['fecha_publicacion']) or day,'units':{},'in_force_known':bool(fvig.get(row['id']))}]}
        if r:act.update(repealed=r['date'],repealed_by=r['by'])
        acts.append(act)
    doc=T.acts_document({'acts':acts,'laws':{},'country':{'code':'ES'}},day)
    for row,fact in zip(doc['acts'],rows):
        row['vigencia_agotada']=fact['vigencia_agotada']
        row['text_not_in_record']=fact['path']+'/README.md' not in tree
        r=byid.get(row['id'])
        if r:row.update(repeal_source=r['source_url'],repeal_basis=r['date_basis'])
        elif fact['vigencia_agotada']=='S':row['status_note']='BOE marks vigencia agotada; the cessation date and cause are unresolved.'
    return doc
def build(repo,base,repeals,docs,git,ref='main'):
    if git(repo,'rev-parse',ref).decode().strip()!=base:
        raise ValueError('the append target must still equal the reviewed published base')
    stream=bytearray();mark=0
    base_timestamp=int(git(repo,'show','-s','--format=%ct',base).decode().strip())
    def emit(date,author,email,message,files,delete=None):
        nonlocal mark
        mark+=1
        # The published builder's pre-1970 convention retains the true date in In-force.
        if date<'1970-01-01':stamp=f'{mark} +0000'
        else:
            from zoneinfo import ZoneInfo
            noon=dt.datetime.combine(dt.date.fromisoformat(date),dt.time(12),ZoneInfo('Europe/Madrid'))
            stamp=f'{int(noon.timestamp())} {noon.strftime("%z")}'
        msg=message.encode('utf-8')
        stream.extend(f'commit refs/heads/{ref}\nmark :{mark}\nauthor {author} <{email}> {stamp}\ncommitter Lexifina <spain-law@lexifina.com> {base_timestamp+mark} +0000\ndata {len(msg)}\n'.encode()+msg+b'\n')
        stream.extend(f'from {base if mark==1 else ":"+str(mark-1)}\n'.encode())
        if delete:stream.extend(f'D {delete}\n'.encode())
        for path,body in sorted(files.items()):
            if isinstance(body,str):body=body.encode('utf-8')
            stream.extend(f'M 100644 inline {path}\ndata {len(body)}\n'.encode()+body+b'\n')
        stream.extend(b'\n')
    for n in repeals:
        path=n['path'];date=n['date'];by=n['by']
        readme=n['readme'].split('## Bloques')[0].rstrip()+f'\n\n## Repeal\n\nThis act was repealed with effect from {date} by {by}. The BOE publisher notice is retained below. Earlier normative text remains available in the history.\n\n## Bloques\n\n- [BOE publisher notice]({n["note_file"]})\n'
        msg=f'Correction: repeal {n["id"]} from {date}\n\nThe BOE initial note attributes the repeal to {by}. Earlier law commits are preserved.\n\nKind: correction\nIn-force: {date}\nCorrects: {path} {date}..{docs["record_to"]}\nSupersedes: {n["supersedes"]}\nReason: Record the whole-act repeal stated in the BOE initial note; retain the notice and remove the repealed normative files.\nAct-path: {path}\nNorma: {by}\nSource: {n["source_url"]}\nIn-force-basis: {n["date_basis"]}\n'+''.join(f'Files: {p}\n' for p in n['files'])
        emit(date,'Lexifina','spain-law@lexifina.com',msg,{path+'/README.md':readme,path+'/'+n['note_file']:n['source_note']},delete=path)
    emit(docs['day'],'Lexifina','spain-law@lexifina.com','Spanish acts: source-backed repeal metadata and append-only reading\n\nKind: documentation\n',docs['files'])
    stream.extend(b'done\n')
    git(repo,'fast-import','--quiet','--done',input=bytes(stream),timeout=300)
    return git(repo,'rev-parse',ref).decode().strip()
