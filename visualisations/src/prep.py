"""Compute every number of the 20 charts into .build/data.json (run by make.py).

    python -X utf8 visualisations/src/prep.py visualisations/src/.build

Reads only what make.py extracted from git objects: log.tsv (the history), codes-names.tsv and file-mods.tsv (files
written per commit), norm-files.tsv (files per norm), repo/ (normas.tsv, corpus.json, data/acts.json,
data/date-corrections.tsv), rdl-notes.jsonl, readmes.jsonl and codes.jsonl (blobs). Writes .build/data.json and
.build/prep.log (the checks printed along the way).
"""
import collections, csv, datetime, json, os, re, statistics, sys

B = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), '.build')
R = os.path.join(B, 'repo')
HEAD, HIST = os.environ.get('HEAD_SHA', ''), os.environ.get('HISTORY_SHA', '')
LOG = open(os.path.join(B, 'prep.log'), 'w', encoding='utf-8', newline='\n')
csv.field_size_limit(1 << 30)


def say(*a):
    print(*a)
    print(*a, file=LOG)


D = datetime.date.fromisoformat
DAYS = lambda a, b: (D(b) - D(a)).days
OUT = {}
MES = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
       'septiembre': 9, 'setiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}

# ------------------------------------------------------------------ tables
NORMAS = {}
with open(os.path.join(R, 'normas.tsv'), encoding='utf-8', newline='') as fh:
    for r in csv.DictReader(fh, delimiter='\t'):
        NORMAS[r['id']] = {'rank': r['path'].split('/')[1], 'rango': r['rango'], 'path': r['path'], 'date': r['fecha_disposicion'],
                           'pub': r['fecha_publicacion'], 'upd': r['fecha_actualizacion'], 'va': r['vigencia_agotada'], 'title': r['titulo']}
ACTS = {a['id']: a for a in json.load(open(os.path.join(R, 'data', 'acts.json'), encoding='utf-8'))['acts']}
CORPUS = json.load(open(os.path.join(R, 'corpus.json'), encoding='utf-8'))
RECORD_TO = CORPUS['record_to']
assert set(NORMAS) == set(ACTS), 'normas.tsv and acts.json list different norms'
say('norms', len(NORMAS), '| record to', RECORD_TO)
FILES = {}
for line in open(os.path.join(B, 'norm-files.tsv'), encoding='utf-8'):
    fo, n = line.rstrip('\n').split('\t')
    FILES[fo.rsplit('/', 1)[1]] = int(n)
TEXT = {i for i in NORMAS if FILES.get(i, 0) > 0}
say('norms with text', len(TEXT))

# ------------------------------------------------------------------ history
TR = ['In-force', 'Published', 'Enacted', 'Norma', 'Kind', 'Corrects', 'Redates', 'Re-asserts', 'Laws-changed']
AUTH = re.compile(r'^(BOE-[A-Z]-\d{4}-\d+)(?: \((.*)\))?$')
COMMITS, CORR = [], []
redate = {}
with open(os.path.join(B, 'log.tsv'), encoding='utf-8', newline='') as fh:
    rd = csv.reader(fh, delimiter='\t', quoting=csv.QUOTE_NONE)
    head = next(rd)
    for row in rd:
        c = dict(zip(head, row))
        if c['kind'] == 'boe':
            m = AUTH.match(c['author'])
            tg = []
            for t in filter(None, c['targets'].split('|')):
                i, nb, f = t.split(':')
                tg.append((i, int(nb), f == 'F'))
            COMMITS.append({'sha': c['sha'], 'aid': m.group(1) if m else None, 'aname': (m.group(2) or None) if m else None, 'author': c['author'],
                            'inf': c['In-force'], 'pub': c['Published'] or None, 'enacted': c['Enacted'] or None, 'tg': tg, 'subject': c['subject']})
        else:
            CORR.append(c)
            for rdt in filter(None, c['Redates'].split(' ; ')):
                s, d = rdt.split()
                redate[s] = d
for c in COMMITS:
    if c['sha'] in redate:
        c['inf0'], c['inf'] = c['inf'], redate[c['sha']]
say('boe commits', len(COMMITS), '| other commits', len(CORR), '| redated', sum(1 for c in COMMITS if 'inf0' in c), 'of', len(redate))
assert all(re.match(r'^\d{4}-\d{2}-\d{2}$', c['inf']) for c in COMMITS)

# ------------------------------------------------------------------ norm names
KINDS = [('Real Decreto-ley', r'Real Decreto[- ][Ll]ey'), ('Real Decreto Legislativo', r'Real Decreto Legislativo'), ('Ley Orgánica', r'Ley Orgánica'),
         ('Real Decreto', r'Real Decreto'), ('Ley', r'Ley')]
NAMED = re.compile(r'(?<![\w-])(' + '|'.join(f'(?:{rx})' for _, rx in KINDS) + r')\s+(\d+)/(\d{4}),?\s+de\s+(\d{1,2})\s+de\s+([a-záéíóú]+)', re.I)


def kind_of(s):
    for k, rx in KINDS:
        if re.fullmatch(rx, s, re.I):
            return k
    return None


def parse_named(s):
    """(kind, number, year, date) of every norm named like 'Real Decreto-ley 9/2025, de 29 de julio' in s"""
    out = []
    for m in NAMED.finditer(s):
        k = kind_of(m.group(1))
        mo = MES.get(m.group(5).lower())
        if not k or not mo:
            continue
        if k == 'Ley' and re.search(r'(Decreto[- ]|Foral\s*)$', s[:m.start()], re.I):
            continue   # "Decreto Ley 3/2010", a regional decree-law, is not "Ley 3/2010"
        try:
            dt = datetime.date(int(m.group(3)), mo, int(m.group(4)))
        except ValueError:
            continue
        out.append((k, int(m.group(2)), int(m.group(3)), dt.isoformat()))
    return out


def named_key(s):
    p = parse_named(s or '')
    return p[0] if p else None


# every norm of those five kinds named in the record: by the title of a norm (its own date first) or by a commit's author
NAMES = {}       # (kind, n, year) -> date
NAME_SRC = {}    # (kind, n, year) -> 'normas' | 'author'
conflicts = []
for i, r in NORMAS.items():
    m = re.match(r'^(Real Decreto[- ][Ll]ey|Real Decreto Legislativo|Ley Orgánica|Real Decreto|Ley)\s+(\d+)/(\d{4})\b', r['title'])
    if m and kind_of(m.group(1)):
        NAMES[(kind_of(m.group(1)), int(m.group(2)), int(m.group(3)))] = r['date']
        NAME_SRC[(kind_of(m.group(1)), int(m.group(2)), int(m.group(3)))] = 'normas'
for c in COMMITS:
    if not c['aname']:
        continue
    for k, n, y, dt in parse_named(c['aname'])[:1]:
        key = (k, n, y)
        if key in NAMES:
            if NAMES[key] != dt:
                conflicts.append((key, NAMES[key], dt, c['aname']))
            continue
        NAMES[key] = dt
        NAME_SRC[key] = 'author'
say('named norms', len(NAMES), collections.Counter(k for k, _, _ in NAMES), '| date conflicts (title date kept)', len(conflicts))
for x in conflicts[:12]:
    say('   conflict', x)


# the rank of a norm credited as author: from its name, or from normas.tsv when the record holds it
def rank_of_name(n):
    n = re.sub(r'^(?:la|el|los|las|lo indicado de la)\s+', '', n or '', flags=re.I).strip()
    if re.match(r'Ley Orgánica', n): return 'ley-organica'
    if re.match(r'Real Decreto[- ]ley', n, re.I): return 'real-decreto-ley'
    if re.match(r'Real Decreto Legislativo', n, re.I): return 'real-decreto-legislativo'
    if re.match(r'(Reglamento aprobado por )?Real Decreto', n, re.I): return 'real-decreto'
    if re.match(r'Decreto[- ]ley', n, re.I): return 'decreto-ley'
    if re.match(r'Ley Foral', n): return 'other'
    if re.match(r'Ley\b', n): return 'ley'
    if re.match(r'Decreto', n): return 'decreto'
    if re.match(r'(Real )?Orden', n, re.I): return 'orden'
    if re.match(r'(Resoluci[oó]n|RESOLUCI)', n, re.I): return 'resolucion'
    if re.match(r'Circular', n): return 'circular'
    if re.match(r'Instrucci[oó]n', n): return 'instruccion'
    if re.match(r'Sentencia \d+/\d{4}', n): return 'tc'
    if re.match(r'(Sentencia|Auto)\b', n): return 'ts'
    if re.match(r'Reforma de', n): return 'constitucion'
    if re.match(r'(Instrumento|Tratado|Protocolo|Convenio|Acuerdo Multilateral|Canje|Enmienda|Aplicaci[oó]n provisional)', n, re.I): return 'acuerdo-internacional'
    if re.match(r'Acuerdo', n): return 'acuerdo'
    if re.match(r'Reglamento', n): return 'reglamento'
    return 'other'


def author_rank(c):
    if c['aname']:
        r = rank_of_name(c['aname'])
        if r != 'other' or not c['aid'] or c['aid'] not in NORMAS:
            return r
    if c['aid'] in NORMAS:
        return NORMAS[c['aid']]['rank']
    return 'unnamed'


for c in COMMITS:
    c['ar'] = author_rank(c)
    c['y'] = int(c['inf'][:4])
say('author ranks', collections.Counter(c['ar'] for c in COMMITS).most_common())
# rank groups for who changes the law
AGROUP = {'ley': 'L', 'ley-organica': 'L', 'real-decreto-ley': 'RDL', 'real-decreto-legislativo': 'RDLeg', 'real-decreto': 'RD', 'orden': 'O',
          'resolucion': 'Res', 'circular': 'Res', 'instruccion': 'Res', 'tc': 'J', 'ts': 'J'}
# norms with the rank of law: by folder, and the codes the BOE files under the decree that published them
LAWRANK = {'constitucion', 'ley', 'ley-organica', 'real-decreto-ley', 'real-decreto-legislativo', 'decreto-ley'}
LAW_CODES = {'BOE-A-1889-4763', 'BOE-A-1885-6627', 'BOE-A-1882-6036', 'BOE-A-1946-2453'}   # Código Civil, Código de Comercio, LECrim, Ley Hipotecaria
is_law = lambda i: NORMAS[i]['rank'] in LAWRANK or i in LAW_CODES

# the changes: one per commit and norm, other than the norm's first text and other than a norm writing its own later parts
CH = []
for c in COMMITS:
    for i, nb, first in c['tg']:
        if first or i == c['aid']:
            continue
        CH.append((c, i, nb))
say('changes', len(CH), '| self-written later parts left out', sum(1 for c in COMMITS for i, nb, f in c['tg'] if not f and i == c['aid']))
AMEND = collections.defaultdict(set)   # norm -> the norms that changed it
for c, i, nb in CH:
    AMEND[i].add(c['aid'] or c['author'])

# ------------------------------------------------------------------ c01: the norms by rank and status
RKORD = ['constitucion', 'ley-organica', 'ley', 'real-decreto-ley', 'real-decreto-legislativo', 'real-decreto', 'orden', 'resolucion',
         'circular', 'instruccion', 'acuerdo-internacional', 'decreto', 'decreto-ley', 'acuerdo', 'reglamento']
STATUS = ['in force', 'expired', 'repealed', 'annulled', 'not yet in force', 'as captured']
c01 = {'ranks': {}, 'files': 0}
for rk in RKORD:
    ids = [i for i, r in NORMAS.items() if r['rank'] == rk]
    st = collections.Counter(ACTS[i]['status'] for i in ids)
    c01['ranks'][rk] = {'n': len(ids), 'st': {s: st.get(s, 0) for s in STATUS}, 'files': sum(FILES.get(i, 0) for i in ids),
                        'files_in_force': sum(FILES.get(i, 0) for i in ids if ACTS[i]['status'] == 'in force'), 'notext': sum(1 for i in ids if i not in TEXT)}
assert sum(v['n'] for v in c01['ranks'].values()) == len(NORMAS)
c01['files'] = sum(FILES.values())
c01['annulled'] = sorted([[i, NORMAS[i]['title'], ACTS[i].get('repealed')] for i in NORMAS if ACTS[i]['status'] == 'annulled'], key=lambda r: r[0])
c01['notyet'] = sorted([[i, NORMAS[i]['title']] for i in NORMAS if ACTS[i]['status'] == 'not yet in force'])
OUT['c01'] = c01
say('c01', {k: (v['n'], v['st']['in force']) for k, v in c01['ranks'].items()})

# ------------------------------------------------------------------ c02: the law in force by year of enactment
CONST_DAY = '1978-12-29'   # the Constitution's day of entry into force (its first commit)


def g2(rk):
    return {'ley': 'L', 'ley-organica': 'L', 'real-decreto-ley': 'RDL', 'decreto-ley': 'RDL', 'real-decreto-legislativo': 'RDL', 'real-decreto': 'D', 'decreto': 'D',
            'orden': 'O', 'acuerdo-internacional': 'I'}.get(rk, 'X')


inforce = [i for i, a in ACTS.items() if a['status'] == 'in force' and NORMAS[i]['rank'] != 'constitucion']
yrs = collections.defaultdict(collections.Counter)
for i in inforce:
    yrs[int(ACTS[i]['enacted'][:4])][g2(NORMAS[i]['rank'])] += 1
pre = [i for i in inforce if ACTS[i]['enacted'] < CONST_DAY]
ERA = [('m', '0000', '1931-04-14'), ('r', '1931-04-14', '1939-04-01'), ('f', '1939-04-01', '1975-11-20'), ('t', '1975-11-20', CONST_DAY), ('c', CONST_DAY, '9999')]
era_of = lambda d: next(e for e, a, b in ERA if a <= d < b)
eras = collections.defaultdict(collections.Counter)
for i in inforce:
    eras[era_of(ACTS[i]['enacted'])][g2(NORMAS[i]['rank'])] += 1
oldest = sorted(inforce, key=lambda i: ACTS[i]['enacted'])[:16]
OUT['c02'] = {'years': {y: dict(v) for y, v in sorted(yrs.items())}, 'eras': {e: dict(v) for e, v in eras.items()}, 'pre': len(pre), 'n': len(inforce),
              'pre_by': dict(collections.Counter(g2(NORMAS[i]['rank']) for i in pre)),
              'oldest': [[i, NORMAS[i]['rank'], ACTS[i]['enacted'], NORMAS[i]['title'], len(AMEND.get(i, ()))] for i in oldest]}
say('c02 in force (without the Constitution)', len(inforce), 'pre-constitutional', len(pre), OUT['c02']['pre_by'])
say('   eras', {e: sum(v.values()) for e, v in eras.items()})

# ------------------------------------------------------------------ c03: international agreements, by the other party
# the other party is read from the title: [ISO 3166 code, the patterns that name it]; states that no longer exist are kept apart
PARTY = [('CO', r'Colombia'), ('CL', r'Chile|Hispano-Chileno'), ('PE', r'Per[uú]\b'), ('PY', r'Paraguay'), ('VA', r'Santa Sede'), ('GT', r'Guatemala'),
         ('NI', r'Nicaragua'), ('BO', r'Bolivia'), ('CR', r'Costa Rica'), ('EC', r'Ecuador'), ('CH', r'Suiz[ao]'), ('HN', r'Honduras'), ('AT', r'Austria'),
         ('DO', r'Rep[uú]blica Dominicana'), ('PT', r'Portugal|Portuguesa|hispano-portugues'), ('MX', r'Mexican|M[eé]xico'), ('US', r'Estados Unidos de Am[eé]rica'),
         ('AR', r'Argentin'), ('NL', r'Pa[ií]ses Bajos'), ('JP', r'Jap[oó]n'), ('BR', r'Brasil'), ('IT', r'Italia'), ('SE', r'Suecia'), ('RO', r'Ruman[ií]a'),
         ('CA', r'Canad[aá]'), ('PL', r'Polonia'), ('MA', r'Marruecos'), ('GB', r'Reino Unido'), ('FI', r'Finlandia'), ('LU', r'Luxemburgo'),
         ('HU', r'Hungr[ií]a'), ('TN', r'T[uú]nez'), ('AU', r'Australia'), ('VE', r'Venezuela'), ('BG', r'Bulgaria'), ('HK', r'Hong Kong'), ('CN', r'China'),
         ('IN', r'\bIndia\b'), ('PH', r'Filipinas'), ('KR', r'Corea'), ('IE', r'Irlanda(?! del Norte)'), ('FR', r'Franc[eé]sa|Francia'), ('TH', r'Tailandia'),
         ('UA', r'Ucrania'), ('MD', r'Moldov?a|Moldavia'), ('UY', r'Uruguay'), ('ID', r'Indonesia'), ('MK', r'[Mm]acedoni'), ('RU', r'Federaci[oó]n (de )?Rus'),
         ('NO', r'Noruega'), ('IL', r'Israel'), ('CU', r'Cuba'), ('SI', r'Eslovenia'), ('GR', r'Hel[eé]nica|Grecia'), ('IS', r'Islandia'), ('AD', r'Andorra'),
         ('TR', r'Turqu[ií]a'), ('BE', r'B[eé]lgica'), ('IR', r'Ir[aá]n\b'), ('DZ', r'Argel'), ('AL', r'Albania'), ('LT', r'Lituania'), ('EE', r'Estonia'),
         ('LV', r'Letonia'), ('EG', r'Egipto'), ('MT', r'\bMalta\b'), ('NZ', r'Nueva Zelanda'), ('MR', r'Mauritania'), ('VN', r'Vietnam'), ('HR', r'Croacia'),
         ('AE', r'Emiratos [AÁ]rabes'), ('SA', r'Arabia Saud'), ('MY', r'Malasia'), ('ZA', r'Sud[aá]frica'), ('KZ', r'Kazajst[aá]n'), ('AW', r'Aruba'),
         ('AN', r'Antillas Holandesas'), ('TT', r'Trinidad y Tobago'), ('JM', r'Jamaica'), ('SV', r'El Salvador'), ('RS', r'Serbia'), ('BA', r'Bosnia'),
         ('PA', r'Panam[aá]'), ('BS', r'Bahamas'), ('BB', r'Barbados'), ('SM', r'San Marino'), ('PK', r'Pakist[aá]n'), ('GE', r'Georgia'),
         ('DE', r'Alemania'), ('SG', r'Singapur'), ('AM', r'Armenia'), ('KW', r'Kuwait'), ('SN', r'Senegal'), ('CY', r'Chipre'), ('NG', r'Nigeria'),
         ('OM', r'Om[aá]n\b'), ('UZ', r'Uzbekist[aá]n'), ('QA', r'Catar'), ('AZ', r'Azerbaiy[aá]n'), ('CV', r'Cabo Verde'), ('BY', r'Bielorrusia'),
         ('SU', r'Uni[oó]n de Rep[uú]blicas Socialistas Sovi[eé]ticas'), ('CS', r'Checoslovaquia'), ('YU', r'Yugoslavia')]
SUBJ = [('tax', r'doble (imposici[oó]n|tributaci[oó]n)|evasi[oó]n fiscal|intercambio de informaci[oó]n en materia (tributaria|fiscal)|cumplimiento fiscal|en materia de fiscalidad|tratados fiscales'),
        ('ss', r'Seguridad Social'), ('nat', r'[Nn]acionalidad'), ('pen', r'[Ee]xtradici[oó]n|asistencia (judicial|jur[ií]dica) en materia penal'),
        ('trn', r'transportes? (internacional|por carretera)'), ('va', r'Santa Sede')]
c03 = {'rows': [], 'multi': [], 'n': 0}
for i, r in sorted(NORMAS.items(), key=lambda kv: kv[1]['date']):
    if r['rank'] != 'acuerdo-internacional':
        continue
    t = r['title']
    parties = [k for k, rx in PARTY if re.search(rx, t)]
    if 'HK' in parties and 'CN' in parties:
        parties.remove('CN')
    if 'AW' in parties or 'AN' in parties:
        parties = [p for p in parties if p != 'NL']
    subj = next((k for k, rx in SUBJ if re.search(rx, t, re.I)), 'other')
    if subj == 'va':
        parties = ['VA']
    row = [i, r['date'], subj, parties, t, ACTS[i]['status']]
    c03['n'] += 1
    (c03['rows'] if len(parties) == 1 else c03['multi']).append(row)
    if len(parties) > 1:
        say('   c03 several parties', parties, t[:120])
mli = [c for c in COMMITS if c['aid'] == 'BOE-A-2021-21097']
c03['mli'] = {'norms': len({i for c in mli for i, nb, f in c['tg'] if not f and i != c['aid']}), 'days': sorted({c['inf'] for c in mli})}
OUT['c03'] = c03
say('c03 agreements', c03['n'], 'bilateral', len(c03['rows']), 'parties', len({r[3][0] for r in c03['rows']}), 'other', len(c03['multi']),
    dict(collections.Counter(r[2] for r in c03['rows'])), '| MLI changed', c03['mli'])
say('   nationality', [(r[3][0], r[1][:4]) for r in c03['rows'] if r[2] == 'nat'])

# ------------------------------------------------------------------ c04: who changes the law, by year
AG = ['L', 'RDL', 'RDLeg', 'RD', 'O', 'Res', 'J', 'X']
agroup = lambda c: AGROUP.get(c['ar'], 'X')
Y0, Y1 = 1979, int(RECORD_TO[:4])
c04 = {'years': list(range(Y0, Y1 + 1)), 'all': {g: [0] * (Y1 - Y0 + 1) for g in AG}, 'law': {g: [0] * (Y1 - Y0 + 1) for g in AG},
       'before': sum(1 for c, i, nb in CH if c['y'] < Y0)}
for c, i, nb in CH:
    if Y0 <= c['y'] <= Y1:
        g = agroup(c)
        c04['all'][g][c['y'] - Y0] += 1
        if is_law(i):
            c04['law'][g][c['y'] - Y0] += 1
c04['n'] = sum(sum(v) for v in c04['all'].values())
c04['unnamed'] = sum(1 for c, i, nb in CH if Y0 <= c['y'] <= Y1 and c['ar'] == 'unnamed')
OUT['c04'] = c04
since = lambda g, k='all', y0=2000: sum(c04[k][g][y - Y0] for y in range(y0, Y1 + 1))
tot00 = sum(since(g) for g in AG)
say('c04 changes', c04['n'], 'since 2000 shares', {g: round(100 * since(g) / tot00, 1) for g in AG})
for y in (2012, 2020, 2021, 2022):
    lt = sum(c04['law'][g][y - Y0] for g in AG)
    say('   changes to laws', y, lt, 'RDL share', round(100 * c04['law']['RDL'][y - Y0] / lt, 1), 'L share', round(100 * c04['law']['L'][y - Y0] / lt, 1))

# ------------------------------------------------------------------ c05: the most changed norms, and the most rewritten blocks
BINS = [(0, 1979, 'pre'), (1979, 1985, '1979'), (1985, 1990, '1985'), (1990, 1995, '1990'), (1995, 2000, '1995'), (2000, 2005, '2000'), (2005, 2010, '2005'),
        (2010, 2015, '2010'), (2015, 2020, '2015'), (2020, 2025, '2020'), (2025, 2027, '2025')]
bin_of = lambda y: next(k for a, b, k in BINS if a <= y < b)
NCH = collections.Counter(i for c, i, nb in CH)
top = sorted(AMEND, key=lambda i: (-len(AMEND[i]), -NCH[i]))[:20]
c05 = {'bins': [k for _, _, k in BINS], 'rows': [], 'dist': {}}
for i in top:
    per = collections.defaultdict(set)
    for c, t, nb in CH:
        if t == i:
            per[bin_of(c['y'])].add(c['aid'] or c['author'])
    c05['rows'].append({'id': i, 'rank': NORMAS[i]['rank'], 'title': NORMAS[i]['title'], 'n': len(AMEND[i]), 'ch': NCH[i], 'status': ACTS[i]['status'],
                        'from': ACTS[i]['in_force'], 'to': ACTS[i]['repealed'], 'bins': {k: len(v) for k, v in per.items()}})
# all norms with text: how many norms changed each
dist = collections.Counter()
for i in TEXT:
    n = len(AMEND.get(i, ()))
    dist['0' if n == 0 else '1' if n == 1 else '2-4' if n <= 4 else '5-19' if n <= 19 else '20+'] += 1
c05['dist'] = dict(dist)
c05['median_law'] = statistics.median(len(AMEND.get(i, ())) for i in TEXT if NORMAS[i]['rank'] in ('ley', 'ley-organica') and ACTS[i]['status'] == 'in force')
# the most rewritten blocks (files modified by the most commits of the BOE build)
heads = {}
for line in open(os.path.join(B, 'readmes.jsonl'), encoding='utf-8'):
    j = json.loads(line)
    fo = j['p'].rsplit('/', 1)[0]
    for m in re.finditer(r'^- \[(.*?)\]\(([^)]+)\)$', j['t'], re.M):
        heads[fo + '/' + m.group(2)] = m.group(1)
texts1 = {}
if os.path.exists(os.path.join(B, 'top-blocks.jsonl')):
    for line in open(os.path.join(B, 'top-blocks.jsonl'), encoding='utf-8'):
        j = json.loads(line)
        texts1[j['p']] = j['t'].strip().split('\n', 1)[0].lstrip('#').strip()
MODS = []
for line in open(os.path.join(B, 'file-mods.tsv'), encoding='utf-8'):
    f, na, nm, shas = line.rstrip('\n').split('\t')
    MODS.append((int(nm), f, shas))
MODS.sort(reverse=True)
sha_inf = {c['sha'][:12]: c['inf'] for c in COMMITS}
c05['blocks'] = []
for nm, f, shas in MODS[:30]:
    i = f.split('/')[3]
    c05['blocks'].append({'f': f, 'id': i, 'm': nm, 'head': heads.get(f, f.rsplit('/', 1)[1]), 'line': texts1.get(f, ''), 'title': NORMAS[i]['title'],
                          'rank': NORMAS[i]['rank'], 'dates': sorted(sha_inf.get(s, '') for s in shas.split(',') if s)})
c05['files_modified'] = len(MODS)
OUT['c05'] = c05
say('c05 top', [(NORMAS[r['id']]['title'][:40], r['n']) for r in c05['rows'][:6]], '| dist', c05['dist'], '| median law', c05['median_law'])
say('   blocks', [(b['head'], b['m'], b['title'][:30], b['line'][:40]) for b in c05['blocks'][:8]])

# ------------------------------------------------------------------ c06: omnibus norms
OMN = collections.defaultdict(lambda: {'t': set(), 'law': set(), 'nb': 0, 'days': set(), 'y': None})
for c, i, nb in CH:
    k = c['aid'] or c['author']
    o = OMN[k]
    o['t'].add(i)
    o['nb'] += nb
    o['days'].add(c['inf'])
    if is_law(i):
        o['law'].add(i)
    o['name'] = c['aname'] or c['author']
    o['ar'] = c['ar']


def omni_kind(k, o):
    t = NORMAS[k]['title'] if k in NORMAS else o['name']
    if re.match(r'Ley \d+/\d{4}, de \d+ de \w+, de medidas fiscales, administrativas y de(l)? orden social', t, re.I): return 'acomp'
    if re.match(r'Ley \d+/\d{4}, de \d+ de \w+, de Presupuestos Generales del Estado', t, re.I): return 'pge'
    if o['ar'] == 'real-decreto-ley': return 'rdl'
    if o['ar'] in ('ley', 'ley-organica'): return 'ley'
    if o['ar'] == 'acuerdo-internacional': return 'intl'
    if o['ar'] == 'real-decreto': return 'rd'
    return 'other'


omni = sorted(OMN.items(), key=lambda kv: (-len(kv[1]['t']), -kv[1]['nb']))
c06 = {'rows': [], 'big': {}, 'years': c04['years']}
for k, o in omni[:16]:
    t = NORMAS[k]['title'] if k in NORMAS else o['name']
    c06['rows'].append({'id': k, 'name': o['name'], 'title': t, 'kind': omni_kind(k, o), 'n': len(o['t']), 'law': len(o['law']), 'nb': o['nb'],
                        'days': sorted(o['days'])[:1] + sorted(o['days'])[-1:], 'ndays': len(o['days'])})
# changes per year from norms that changed ten norms or more, by kind
BIG = {k for k, o in OMN.items() if len(o['t']) >= 10}
kinds = ['acomp', 'pge', 'rdl', 'ley', 'other']
c06['big'] = {kd: [0] * len(c04['years']) for kd in kinds}
c06['all'] = [0] * len(c04['years'])
for c, i, nb in CH:
    if not (Y0 <= c['y'] <= Y1):
        continue
    c06['all'][c['y'] - Y0] += 1
    k = c['aid'] or c['author']
    if k in BIG:
        kd = omni_kind(k, OMN[k])
        c06['big'][kd if kd in kinds else 'other'][c['y'] - Y0] += 1
c06['nbig'] = len(BIG)
c06['acomp'] = sorted([[k, OMN[k]['name'], len(OMN[k]['t'])] for k in OMN if omni_kind(k, OMN[k]) == 'acomp'], key=lambda r: r[1][-4:])
c06['pge'] = len([k for k in OMN if omni_kind(k, OMN[k]) == 'pge'])
OUT['c06'] = c06
say('c06 top', [(r['name'][:40], r['kind'], r['n']) for r in c06['rows'][:8]], '| norms changing 10+', len(BIG))
say('   acompañamiento', [(r[1], r[2]) for r in c06['acomp']])

# ------------------------------------------------------------------ c07: consolidated texts (textos refundidos) and what replaced them
LINES = [('ss', ['BOE-A-1994-14960', 'BOE-A-2015-11724']), ('et', ['BOE-A-1995-7730', 'BOE-A-2015-11430']),
         ('mv', ['BOE-A-1988-18764', 'BOE-A-2015-11435', 'BOE-A-2023-7053']), ('tr', ['BOE-A-1990-6396', 'BOE-A-2015-11722']),
         ('is', ['BOE-A-2004-4456', 'BOE-A-2014-12328'])]
c07 = {'lines': []}
for key, ids in LINES:
    segs = []
    for j, i in enumerate(ids):
        a = ACTS[i]
        steps = collections.Counter()
        seen = set()
        for c, t, nb in sorted((x for x in CH if x[1] == i), key=lambda x: x[0]['inf']):
            k = c['aid'] or c['author']
            if k in seen:
                continue
            seen.add(k)
            steps[c['inf']] += 1
        nxt = ids[j + 1] if j + 1 < len(ids) else None
        if nxt:   # the next text repealed this one, or took effect on the day this one was repealed
            assert (ACTS[i]['repealed_by'] or '').find(nxt) >= 0 or ACTS[i]['repealed'] == ACTS[nxt]['in_force'], (i, ACTS[i]['repealed_by'], nxt)
        segs.append({'id': i, 'title': NORMAS[i]['title'], 'rank': NORMAS[i]['rank'], 'date': NORMAS[i]['date'], 'from': a['in_force'], 'to': a['repealed'], 'status': a['status'],
                     'steps': sorted(steps.items()), 'n': len(seen)})
    c07['lines'].append({'k': key, 'segs': segs})
c07['rdleg'] = {'n': len([i for i in NORMAS if NORMAS[i]['rank'] == 'real-decreto-legislativo']),
                'replaced': len([i for i in NORMAS if NORMAS[i]['rank'] == 'real-decreto-legislativo' and ACTS[i]['status'] == 'repealed'])}
OUT['c07'] = c07
say('c07', [(l['k'], [(s['title'][:30], s['n'], s['from'], s['to']) for s in l['segs']]) for l in c07['lines']])

# ------------------------------------------------------------------ c08: laws, organic laws and decree-laws per year, and per president
# each of the three is numbered from 1 every year, so the highest number named in the record is how many there were at least
GOV = [('suarez', '1976-07-03'), ('calvo', '1981-02-26'), ('gonzalez', '1982-12-02'), ('aznar', '1996-05-05'), ('zapatero', '2004-04-17'),
       ('rajoy', '2011-12-21'), ('sanchez', '2018-06-02')]
gov_of = lambda d: [g for g, s in GOV if s <= d][-1]
K3 = ['Ley', 'Ley Orgánica', 'Real Decreto-ley']
YA = 1979
c08 = {'years': list(range(YA, Y1 + 1)), 'max': {}, 'named': {}, 'gov': {}, 'amb': {}, 'govs': GOV, 'record_to': RECORD_TO}
for k in K3:
    byy = collections.defaultdict(dict)
    for (kk, n, y), dt in NAMES.items():
        if kk == k:
            byy[y][n] = dt
    c08['max'][k] = [max(byy[y]) if byy.get(y) else 0 for y in c08['years']]
    c08['named'][k] = [len(byy[y]) if byy.get(y) else 0 for y in c08['years']]
    per, amb = collections.Counter(), collections.Counter()
    for y in c08['years']:
        d = byy.get(y, {})
        if not d:
            continue
        for n in range(1, max(d) + 1):
            if n in d:
                per[gov_of(d[n])] += 1
                continue
            lo = max((m for m in d if m < n), default=None)
            hi = min((m for m in d if m > n), default=None)
            g1 = gov_of(d[lo]) if lo else gov_of(f'{y}-01-01')
            g2_ = gov_of(d[hi]) if hi else gov_of(min(f'{y}-12-31', RECORD_TO))
            if g1 == g2_:
                per[g1] += 1
            else:
                amb[f'{g1}|{g2_}'] += 1
    c08['gov'][k] = dict(per)
    c08['amb'][k] = dict(amb)
# the decree-laws dated in each year whose number is named (for the share each year), and years with no ordinary law at all
c08['no_ley'] = [y for y, m in zip(c08['years'], c08['max']['Ley']) if m == 0]
OUT['c08'] = c08
for k in K3:
    say('c08', k, 'per president', c08['gov'][k], 'ambiguous', c08['amb'][k])
say('   2016', {k: c08['max'][k][2016 - YA] for k in K3}, '2020', {k: c08['max'][k][2020 - YA] for k in K3}, 'years with no ordinary law', c08['no_ley'])

# ------------------------------------------------------------------ c09: laws by month, 2004-2026, and the longest stretches without an ordinary law
M0 = 2004
c09 = {'y0': M0, 'cells': {}, 'gaps': []}
lawdates = sorted((dt, k, n, y) for (k, n, y), dt in NAMES.items() if k in ('Ley', 'Ley Orgánica') and y >= M0)
for dt, k, n, y in lawdates:
    key = dt[:7]
    c09['cells'].setdefault(key, [0, 0])[0 if k == 'Ley' else 1] += 1
# completeness of the named laws in these years
c09['complete'] = {k: sum(c08['named'][k][y - YA] for y in range(M0, Y1 + 1)) for k in ('Ley', 'Ley Orgánica')}
c09['max'] = {k: sum(c08['max'][k][y - YA] for y in range(M0, Y1 + 1)) for k in ('Ley', 'Ley Orgánica')}
ordl = [x for x in lawdates if x[1] == 'Ley']
gaps = sorted(((DAYS(ordl[j][0], ordl[j + 1][0]), ordl[j], ordl[j + 1]) for j in range(len(ordl) - 1)), reverse=True)[:6]
c09['gaps'] = [[g, a[0], f'{a[2]}/{a[3]}', b[0], f'{b[2]}/{b[3]}'] for g, a, b in gaps]
# organic laws inside the gaps
for g in c09['gaps']:
    g.append([f'{n}/{y}' for dt, k, n, y in lawdates if k == 'Ley Orgánica' and g[1] < dt < g[3]])
c09['last_to_record'] = DAYS(ordl[-1][0], RECORD_TO)
c09['last'] = [ordl[-1][0], f'{ordl[-1][2]}/{ordl[-1][3]}']
mon = collections.Counter(int(dt[5:7]) for dt, k, n, y in lawdates if y <= 2025)
c09['months'] = [mon.get(m, 0) for m in range(1, 13)]
OUT['c09'] = c09
say('c09 named', c09['complete'], 'of', c09['max'], '| gaps', c09['gaps'][:4], '| months', c09['months'], '| since last law', c09['last_to_record'], c09['last'])

# ------------------------------------------------------------------ c10: the Congreso's vote on each decree-law (convalidation), 2020-2026
NOTE = re.compile(r'(convalidad[oa]s?|derogad[oa]s?|deroga)\b.{0,120}?por Acuerdo del Congreso de los Diputados,? publicad[oa] por Resoluci[oó]n de (\d+) de (\w+) de (\d{4})\.? Ref\. (BOE-A-\d+-\d+)', re.S)
notes = collections.defaultdict(str)
for line in open(os.path.join(B, 'rdl-notes.jsonl'), encoding='utf-8'):
    j = json.loads(line)
    notes[j['p'].split('/')[3]] += '\n' + j['t']
c10 = {'rows': [], 'fixed': []}
for i, r in NORMAS.items():
    if r['rank'] != 'real-decreto-ley' or r['date'] < '2017-01-01':
        continue
    m = NOTE.search(notes.get(i, ''))
    out, rdate, ref = 'none', None, None
    if m:
        out = 'conv' if m.group(1).startswith('convalid') else 'derog'
        rdate = datetime.date(int(m.group(4)), MES[m.group(3).lower()], int(m.group(2))).isoformat()
        ref = m.group(5)
        if rdate < r['date']:   # a note that gives a year before the decree-law's own: read with the decree-law's year
            fixed = rdate
            rdate = str(int(r['date'][:4]) + (1 if rdate[5:] < r['date'][5:] else 0)) + rdate[4:]
            c10['fixed'].append([i, fixed, rdate])
    kn = named_key(r['title'])
    c10['rows'].append([i, r['date'], r['pub'], out, rdate, ref, kn[1] if kn else None, r['title'], ACTS[i]['status']])
c10['rows'].sort(key=lambda x: (x[1], x[6] or 0))
c10['max'] = {y: c08['max']['Real Decreto-ley'][y - YA] for y in range(2017, Y1 + 1)}
OUT['c10'] = c10
cy = collections.defaultdict(collections.Counter)
for row in c10['rows']:
    cy[row[1][:4]][row[3]] += 1
say('c10', {y: dict(v) for y, v in sorted(cy.items())}, '| fixed', c10['fixed'])
dd = [DAYS(row[1], row[4]) for row in c10['rows'] if row[3] == 'conv' and row[1] >= '2020']
say('   days from the decree-law to the resolution: median', statistics.median(dd), 'max', max(dd), 'over 30', sum(1 for d in dd if d > 30), 'of', len(dd))

# ------------------------------------------------------------------ c11: decree-laws that changed decree-laws, 2020
RY = 2020
rdl20 = {}
for i, r in NORMAS.items():
    kn = named_key(r['title'])
    if r['rank'] == 'real-decreto-ley' and kn and kn[2] == RY:
        rdl20[i] = {'n': kn[1], 'date': r['date'], 'title': r['title']}
arcs = collections.defaultdict(lambda: [0, 0, set()])
for c, i, nb in CH:
    if c['aid'] in rdl20 and i in rdl20:
        a = arcs[(c['aid'], i)]
        a[0] += 1; a[1] += nb; a[2].add(c['inf'])
c11 = {'nodes': [[i, v['n'], v['date'], v['title']] for i, v in sorted(rdl20.items(), key=lambda kv: kv[1]['n'])],
       'arcs': [[a, b, v[0], v[1], sorted(v[2])] for (a, b), v in sorted(arcs.items())], 'y': RY}
# every change to a 2020 decree-law, by whom, to the end of the record
inn = collections.defaultdict(lambda: collections.Counter())
for c, i, nb in CH:
    if i in rdl20:
        inn[i][c['ar'] if c['ar'] in ('real-decreto-ley', 'ley', 'ley-organica', 'real-decreto') else 'other'] += 1
c11['in'] = {i: dict(v) for i, v in inn.items()}
c11['by_year'] = {}
for y in range(2008, Y1 + 1):
    tot = sum(1 for c, i, nb in CH if c['y'] == y and NORMAS[i]['rank'] == 'real-decreto-ley')
    rr = sum(1 for c, i, nb in CH if c['y'] == y and NORMAS[i]['rank'] == 'real-decreto-ley' and c['ar'] == 'real-decreto-ley')
    c11['by_year'][y] = [tot, rr]
OUT['c11'] = c11
say('c11 nodes', len(c11['nodes']), 'arcs', len(c11['arcs']), 'changes', sum(a[2] for a in c11['arcs']), '| most changed',
    sorted(((sum(v.values()), rdl20[i]['n']) for i, v in inn.items()), reverse=True)[:5])

# ------------------------------------------------------------------ c12: the budget laws (Leyes de Presupuestos Generales del Estado)
PGE = re.compile(r'^Ley (\d+)/(\d{4}), de (\d+) de (\w+), de Presupuestos Generales del Estado para (?:el año )?(\d{4})\.?$')
c12 = {'rows': {}, 'y0': 1983}
for i, r in NORMAS.items():
    m = PGE.match(r['title'])
    if m:
        by = int(m.group(5))
        c12['rows'][by] = {'id': i, 'n': f'{m.group(1)}/{m.group(2)}', 'date': r['date'], 'pub': r['pub'], 'title': r['title'],
                           'changed': len(OMN[i]['t']) if i in OMN else 0, 'law': len(OMN[i]['law']) if i in OMN else 0}
yrs12 = range(c12['y0'], Y1 + 1)
c12['missing'] = [y for y in yrs12 if y not in c12['rows']]
c12['late'] = sorted([(DAYS(f'{y}-01-01', v['pub']), y) for y, v in c12['rows'].items() if y >= c12['y0']], reverse=True)[:6]
OUT['c12'] = c12
say('c12 budget laws', sorted(c12['rows']), '| none for', c12['missing'], '| latest', c12['late'])

# ------------------------------------------------------------------ c13: the weekday of the date of royal decrees and decree-laws
c13 = {'years': list(range(1977, Y1 + 1)), 'wd': {}, 'runs': []}
wdy = collections.defaultdict(lambda: [0] * 7)
wdm = collections.defaultdict(lambda: [0] * 7)
for (k, n, y), dt in NAMES.items():
    if k not in ('Real Decreto', 'Real Decreto-ley') or not (1977 <= y <= Y1) or dt[:4] != str(y):
        continue
    w = D(dt).weekday()
    wdy[y][w] += 1
    wdm[dt[:7]][w] += 1
c13['wd'] = {y: wdy[y] for y in c13['years']}
c13['n'] = sum(sum(v) for v in wdy.values())
# runs of months in which one weekday holds most of the dates (months with fewer than four norms left out)
runs, cur = [], None
for ym in sorted(wdm):
    v = wdm[ym]
    if sum(v) < 4:
        continue
    w = max(range(7), key=lambda q: v[q])
    if v[w] / sum(v) < 0.5:
        continue
    if cur and cur[2] == w:
        cur[1] = ym
    else:
        cur = [ym, ym, w]
        runs.append(cur)
c13['runs'] = runs
# the months in which one weekday holds most dates (four norms or more in the month): the first and last of three stretches
dom = {ym: max(range(7), key=lambda q: v[q]) for ym, v in wdm.items() if sum(v) >= 4 and max(v) / sum(v) >= 0.5}
first_after = lambda s, wd: min(ym for ym in dom if ym >= s and dom[ym] == wd)
last_before = lambda e, wd: max(ym for ym in dom if ym <= e and dom[ym] == wd)
wed2 = first_after('2025-01', 2)
wy = [y for y in range(1977, 1991) if sum(wdy[y]) and wdy[y][2] / sum(wdy[y]) > 0.5]   # the earlier years in which most dates are Wednesdays
c13['stretches'] = [[f'{min(wy)}-01', f'{max(wy)}-12', 2], [first_after('2019-01', 1), last_before(wed2, 1), 1], [wed2, max(dom), 2]]
c13['wed_years'] = wy
c13['month'] = {ym: v for ym, v in wdm.items() if ym[:4] in ('1982', '1983', '1985', '1986', '2019', '2020', '2025', '2026')}
say('c13 stretches', c13['stretches'])
OUT['c13'] = c13
say('c13 dated', c13['n'], '| runs', [(a, b, 'LMXJVSD'[w]) for a, b, w in runs if a != b])

# ------------------------------------------------------------------ c14: from the date of a norm to its publication in the BOE
PUBG = {'ley': 'L', 'ley-organica': 'L', 'real-decreto-ley': 'RDL', 'real-decreto': 'RD', 'orden': 'O'}
pubrows = {}
for i, r in NORMAS.items():
    g = PUBG.get(r['rank'])
    if g and r['date'] and r['pub']:
        pubrows[i] = (g, r['date'], r['pub'])
for c in COMMITS:   # amending norms the record does not hold: date from the name, publication from the commit
    if c['aid'] and c['aid'] not in pubrows and c['aid'] not in NORMAS and c['pub']:
        g = PUBG.get(c['ar'])
        kn = named_key(c['aname'])
        if g and kn:
            pubrows[c['aid']] = (g, kn[3], c['pub'])
lag = collections.defaultdict(list)
neg = 0
for i, (g, d0, d1) in pubrows.items():
    dd = DAYS(d0, d1)
    if dd < 0:
        neg += 1
        continue
    lag[(g, int(d0[:4]))].append(dd)
c14 = {'groups': ['L', 'RDL', 'RD', 'O'], 'years': list(range(1979, Y1 + 1)), 'med': {}, 'n': {}, 'le1': {}, 'neg': neg, 'dist': {}}
for g in c14['groups']:
    c14['med'][g] = [statistics.median(lag[(g, y)]) if len(lag[(g, y)]) >= 3 else None for y in c14['years']]
    c14['n'][g] = [len(lag[(g, y)]) for y in c14['years']]
    c14['le1'][g] = [sum(1 for x in lag[(g, y)] if x <= 1) for y in c14['years']]
    for per, a, b in (('1979', 1979, 2000), ('2000', 2000, 2010), ('2010', 2010, 2020), ('2020', 2020, Y1 + 1)):
        v = [x for y in range(a, b) for x in lag[(g, y)]]
        c14['dist'][f'{g}|{per}'] = {'n': len(v), 'med': statistics.median(v) if v else None,
                                     'b': [sum(1 for x in v if x <= 1), sum(1 for x in v if 2 <= x <= 7), sum(1 for x in v if 8 <= x <= 30), sum(1 for x in v if x > 30)]}
OUT['c14'] = c14
say('c14 norms', len(pubrows), 'negative', neg, {k: (v['n'], v['med']) for k, v in c14['dist'].items()})

# ------------------------------------------------------------------ c15: from publication to entry into force (first texts)
first = {}
for c in COMMITS:
    for i, nb, f in c['tg']:
        if f and (i not in first or c['inf'] < first[i]):
            first[i] = c['inf']
VG = {'ley': 'L', 'ley-organica': 'L', 'real-decreto-ley': 'RDL', 'real-decreto-legislativo': 'L', 'real-decreto': 'RD', 'orden': 'O'}
VC = ['before', 'same', 'next', 'short', 'twenty', 'month', 'half', 'long']


def vcat(d):
    return 'before' if d < 0 else 'same' if d == 0 else 'next' if d == 1 else 'short' if d < 20 else 'twenty' if d == 20 else 'month' if d <= 31 else 'half' if d <= 183 else 'long'


c15 = {'cats': VC, 'per': {}, 'years': list(range(1979, Y1 + 1)), 'ly': {}, 'left_out': 0}
per15 = lambda y: 'pre' if y < 1979 else '1979' if y < 2000 else '2000' if y < 2010 else '2010' if y < 2020 else '2020'
ly = collections.defaultdict(collections.Counter)
for i, d1 in first.items():
    r = NORMAS[i]
    g = VG.get(r['rank']) or ('L' if i in LAW_CODES else None)
    if not g:
        continue
    dd = DAYS(r['pub'], d1)
    if dd > 5 * 365:    # the BOE's first version is a later text, not the one published (Código de Comercio, LECrim)
        c15['left_out'] += 1
        continue
    y = int(r['pub'][:4])
    c15['per'].setdefault(f'{g}|{per15(y)}', collections.Counter())[vcat(dd)] += 1
    if g == 'L' and y >= 1979:
        ly[y][vcat(dd)] += 1
c15['per'] = {k: dict(v) for k, v in c15['per'].items()}
c15['ly'] = {y: dict(ly[y]) for y in c15['years']}
OUT['c15'] = c15
for k in ('L|pre', 'L|1979', 'L|2000', 'L|2010', 'L|2020', 'RDL|2020', 'RD|2020', 'O|2020'):
    v = c15['per'].get(k, {})
    n = sum(v.values())
    say('c15', k, n, {c: f"{100 * v.get(c, 0) / n:.0f}%" for c in VC if v.get(c)})
say('   left out (first version years after publication)', c15['left_out'])

# ------------------------------------------------------------------ c16: the calendar of entry into force, 2000-2025
C0, C1 = 2000, 2025
c16 = {'y0': C0, 'y1': C1, 'md': collections.Counter(), 'wd_inf': [0] * 7, 'wd_pub': [0] * 7, 'n': 0, 'npub': 0}
for c, i, nb in CH:
    if C0 <= c['y'] <= C1:
        c16['md'][c['inf'][5:]] += 1
        c16['wd_inf'][D(c['inf']).weekday()] += 1
        c16['n'] += 1
pubs = {}
for c in COMMITS:
    if c['aid'] and c['pub'] and C0 <= int(c['pub'][:4]) <= C1:
        pubs[c['aid']] = c['pub']
for p in pubs.values():
    c16['wd_pub'][D(p).weekday()] += 1
c16['npub'] = len(pubs)
c16['md'] = dict(c16['md'])
c16['y1jan'] = {y: [sum(1 for c, i, nb in CH if c['inf'] == f'{y}-01-01'), sum(1 for c, i, nb in CH if c['y'] == y)] for y in range(C0, C1 + 1)}
OUT['c16'] = c16
top_md = sorted(c16['md'].items(), key=lambda kv: -kv[1])[:5]
say('c16 changes', c16['n'], 'top days', [(k, v, f'{100 * v / c16["n"]:.1f}%') for k, v in top_md], '| publication weekdays', c16['wd_pub'], '| in force', c16['wd_inf'])

# ------------------------------------------------------------------ the codes: blocks in the BOE's order, and the commits that wrote them
CODE_TEXT = {}
for line in open(os.path.join(B, 'codes.jsonl'), encoding='utf-8'):
    j = json.loads(line)
    CODE_TEXT[j['p']] = j['t']
EMPTY = re.compile(r'^\(?\s*(Derogad[oa]s?|Suprimid[oa]s?|Sin contenido|Anulad[oa]s?)\s*\)?\.?$', re.I)


def body_of(t):
    return '\n'.join(l for l in t.split('\n') if not l.startswith('>') and not l.startswith('#')).strip()


def code_blocks(fo):
    """the README's block list: [(file, heading)] in the BOE's order"""
    rd = next(json.loads(l)['t'] for l in open(os.path.join(B, 'readmes.jsonl'), encoding='utf-8') if json.loads(l)['p'] == fo + '/README.md')
    return [(fo + '/' + m.group(2), m.group(1)) for m in re.finditer(r'^- \[(.*?)\]\(([^)]+)\)$', rd, re.M)]


writes = collections.defaultdict(list)   # file -> [(in-force, author, status)]
sha_c = {c['sha']: c for c in COMMITS}
for line in open(os.path.join(B, 'codes-names.tsv'), encoding='utf-8'):
    s, st, f = line.rstrip('\n').split('\t')
    c = sha_c.get(s)
    if c:
        writes[f].append((c['inf'], c['aid'] or c['author'], st, c['aname'] or c['author']))
for f in writes:
    writes[f].sort()


def art_no(h):
    m = re.match(r'^Art(?:[íi]culo|s?\.?)\s*(\d+)', h)
    return int(m.group(1)) if m else None


# ------------------------------------------------------------------ c17: the Constitution
CE = 'estatal/constitucion/1978/BOE-A-1978-31229'
blocks = code_blocks(CE)
part, arts = None, []
for f, h in blocks:
    if re.match(r'^(T[IÍ]TULO|DISPOSICIONES|PRE[AÁ]MBULO)', h, re.I) or re.match(r'^(Disposici[oó]n)', h):
        if re.match(r'^T[IÍ]TULO', h, re.I):
            part = h
    if re.match(r'^Art[íi]culo \d+', h):
        w = writes.get(f, [])
        arts.append([art_no(h), part, [x[0] for x in w if x[2] == 'M'], [x[3] for x in w if x[2] == 'M']])
reforms = sorted({(x[0], x[3]) for f in writes if f.startswith(CE + '/') for x in writes[f] if x[2] == 'M'})
c17 = {'arts': arts, 'reforms': reforms, 'blocks': len(blocks)}
CMP = ['BOE-A-1979-23709', 'BOE-A-1985-11672', 'BOE-A-1985-12666', 'BOE-A-1995-25444', 'BOE-A-1980-21166', 'BOE-A-2006-7899', 'BOE-A-2018-16673', 'BOE-A-1979-30177']
c17['cmp'] = [[i, NORMAS[i]['title'], len(AMEND.get(i, ())), ACTS[i]['in_force']] for i in CMP if i in NORMAS]
OUT['c17'] = c17
say('c17 articles', len(arts), 'blocks', len(blocks), '| reformed', [(a[0], a[2]) for a in arts if a[2]], '| reforms', reforms, '| cmp', [(r[1][:30], r[2]) for r in c17['cmp']])

# ------------------------------------------------------------------ c18: the Código Civil article by article
CCF = 'estatal/real-decreto/1889/BOE-A-1889-4763'
blocks = code_blocks(CCF)
book, rows18 = None, []
for f, h in blocks:
    if re.match(r'^(T[IÍ]TULO PRELIMINAR|LIBRO)', h):
        book = h
    if re.match(r'^Arts?\b', h) or re.match(r'^Art\.', h):
        w = writes.get(f, [])
        t = CODE_TEXT.get(f, '')
        empty = bool(EMPTY.match(body_of(t)))
        rows18.append([h, book, w[0][0] if w else None, w[-1][0] if w else None, len([x for x in w if x[2] == 'M']), empty, w[-1][3] if w else None])
artf18 = {f for f, h in blocks if re.match(r'^Arts?\b', h) or re.match(r'^Art\.', h)}
rf18 = collections.defaultdict(lambda: [None, set(), set()])
for f in artf18:
    for inf, au, st, nm in writes.get(f, []):
        if inf == '1889-08-16' and st == 'A':
            continue
        rf18[au][0] = nm
        rf18[au][1].add(f)
        rf18[au][2].add(inf)
c18 = {'rows': rows18, 'books': [b for b in dict.fromkeys(r[1] for r in rows18)],
       'reforms': sorted([[k, v[0], min(v[2]), len(v[1])] for k, v in rf18.items()], key=lambda r: -r[3])[:12], 'nreforms': len(rf18)}
OUT['c18'] = c18
orig = [r for r in rows18 if r[4] == 0 and not r[5]]
say('c18 article blocks', len(rows18), 'books', c18['books'], '| never changed', len(orig), '| emptied', sum(1 for r in rows18 if r[5]),
    '| first dates', collections.Counter(r[2] for r in rows18).most_common(3))

# ------------------------------------------------------------------ c19: the Código Penal and its reforms
CPF = 'estatal/ley-organica/1995/BOE-A-1995-25444'
blocks = code_blocks(CPF)
artf = {f: h for f, h in blocks if re.match(r'^Art[íi]culo', h)}
ref = collections.defaultdict(lambda: {'arts': set(), 'blocks': set(), 'days': set(), 'name': None})
for f, w in writes.items():
    if not f.startswith(CPF + '/'):
        continue
    for inf, au, st, nm in w:
        if st != 'M' and inf == '1996-05-24' and au == 'BOE-A-1995-25444':
            continue
        if au == 'BOE-A-1995-25444' and st == 'A' and inf <= '1996-05-24':
            continue
        r = ref[au]
        r['name'] = nm
        r['days'].add(inf)
        r['blocks'].add(f)
        if f in artf:
            r['arts'].add(f)
c19 = {'reforms': sorted([[k, v['name'], sorted(v['days'])[0], len(v['arts']), len(v['blocks']), len(v['days'])] for k, v in ref.items()], key=lambda r: r[2]),
       'arts': len(artf)}
artm = collections.Counter()
for f in artf:
    artm[f] = len([x for x in writes.get(f, []) if x[2] == 'M'])
c19['top'] = [[artf[f], n, [x[0] for x in writes[f] if x[2] == 'M']] for f, n in artm.most_common(12)]
c19['never'] = sum(1 for f in artf if artm[f] == 0 and not EMPTY.match(body_of(CODE_TEXT.get(f, ''))))
c19['emptied'] = sum(1 for f in artf if EMPTY.match(body_of(CODE_TEXT.get(f, ''))))
OUT['c19'] = c19
say('c19 reforms', len(c19['reforms']), 'article blocks', c19['arts'], 'never changed', c19['never'], 'emptied', c19['emptied'],
    '| largest', sorted([(r[3], r[1]) for r in c19['reforms']], reverse=True)[:6], '| top arts', [(a[0], a[1]) for a in c19['top'][:5]])

# ------------------------------------------------------------------ c20: the courts in the text
c20 = {'tc': collections.defaultdict(lambda: [set(), 0]), 'ts': collections.defaultdict(lambda: [set(), 0]), 'tc_norms': collections.Counter(), 'ts_ranks': collections.Counter(),
       'tc_ranks': collections.Counter()}
for c, i, nb in CH:
    if c['ar'] not in ('tc', 'ts'):
        continue
    nm = c['aname'] or ''
    if c['ar'] == 'tc':
        y = int(re.match(r'Sentencia \d+/(\d{4})', nm).group(1))
    else:   # the ruling's date in its name, else its number's year, else the year of its BOE identifier
        m = re.search(r'de \d{1,2} de [a-záéíóú]+ de (\d{4})', nm) or re.search(r'TS \d+/(\d{4})', nm)
        y = int(m.group(1)) if m else int(c['aid'].split('-')[2])
    d = c20[c['ar']][y]
    d[0].add(c['aid'] or nm)
    d[1] += nb
    if c['ar'] == 'tc':
        c20['tc_norms'][i] += 1
        c20['tc_ranks'][NORMAS[i]['rank']] += 1
    else:
        c20['ts_ranks'][NORMAS[i]['rank']] += 1
for k in ('tc', 'ts'):
    c20[k] = {y: [len(v[0]), v[1]] for y, v in sorted(c20[k].items())}
c20['tc_top'] = [[i, NORMAS[i]['title'], n] for i, n in c20['tc_norms'].most_common(12)]
c20['tc_ranks'] = dict(c20['tc_ranks']); c20['ts_ranks'] = dict(c20['ts_ranks'])
del c20['tc_norms']
c20['annulled'] = [[i, NORMAS[i]['title'], ACTS[i].get('repealed')] for i in NORMAS if ACTS[i]['status'] == 'annulled']
OUT['c20'] = c20
say('c20 tc', {y: v for y, v in c20['tc'].items()}, '\n    ts', {y: v for y, v in c20['ts'].items()})
say('   tc ranks', c20['tc_ranks'], '| ts ranks', c20['ts_ranks'], '| tc top', [(r[1][:40], r[2]) for r in c20['tc_top'][:5]])

# ------------------------------------------------------------------ profile and write
OUT['profile'] = {'norms': len(NORMAS), 'text': len(TEXT), 'files': sum(FILES.values()), 'commits': len(COMMITS), 'corrections': sum(1 for c in CORR if c['kind'] == 'correction'),
                  'changes': len(CH), 'record_to': RECORD_TO, 'built': datetime.date.today().isoformat(), 'head': HEAD, 'history': HIST,
                  'history_from': CORPUS.get('history_from'), 'in_force': sum(1 for a in ACTS.values() if a['status'] == 'in force'),
                  'repealed': sum(1 for a in ACTS.values() if a['status'] == 'repealed'), 'pre': OUT['c02']['pre'],
                  'named': len(NAMES), 'rdl_notes': sum(1 for r in OUT['c10']['rows'] if r[3] != 'none')}
with open(os.path.join(B, 'data.json'), 'w', encoding='utf-8', newline='\n') as fh:
    json.dump({'charts': {k: v for k, v in OUT.items() if k != 'profile'}, 'profile': OUT['profile']}, fh, ensure_ascii=False, separators=(',', ':'), default=list)
say('data.json', os.path.getsize(os.path.join(B, 'data.json')), 'bytes')
