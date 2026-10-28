# Spanish state law as git history

Every consolidated state-level (ámbito Estatal) norm in the BOE's consolidated legislation (legislación consolidada),
as a git history: **one commit per amending norm per in-force date**, authored by that norm, so `git blame` names the
norm that wrote each paragraph and `git log` lists a provision's amendments in the order they took effect.

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es). Textos consolidados de carácter
meramente informativo; only the texts published in the «Boletín Oficial del Estado» are official. See LICENSE.

8,774 norms, 16,736 commits, 397,165 block versions, in force from
1835-11-27 to 2026-10-28. Data retrieved 2026-10-28.

## The questions

| Question | Command |
| --- | --- |
| What did art. 135 of the Constitution say on 26 Sept 2011? | `python tools/eslaw.py on 2011-09-26 estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| And the day after the reform took effect? | `python tools/eslaw.py on 2011-09-27 estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| The whole Constitution on a day, in order | `python tools/eslaw.py on 1992-08-28 estatal/constitucion/1978/BOE-A-1978-31229` |
| Which norm wrote each paragraph? | `git blame main -- estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| When did art. 49 change, and by which norm? | `python tools/eslaw.py log estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| The same in raw git | `git log --format=%(trailers:key=In-force,valueonly,separator=)%x09%an main -- estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| What exactly changed, word by word? | `git log -p --word-diff --format=%an main -- estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| Everything one norm changed | `git log --format=%H%x09%s --grep=^Norma:.BOE-A-2011-15210$ main` |
| Article 1 of the Código Civil over time | `python tools/eslaw.py log estatal/real-decreto/1889/BOE-A-1889-4763/a1.md` |
| Which kinds of norm are there? | `git ls-tree --name-only main estatal/` |
| How many commits did the publisher make with no norm? | `git rev-list --count --author=publisher@boe.invalid main` |

In PowerShell, quote arguments containing `%`, `(` or `,` with single quotes.

## The dates

- **Commit date = in-force date** (fecha_vigencia of the block version), at 12:00 Europe/Madrid: CET (+0100), and
  CEST (+0200) from the last Sunday of March up to the last Sunday of October (the EU rule, applied to every year
  from 1970). The day reads the same everywhere.
- Every law commit carries `In-force: YYYY-MM-DD`; `Published:` is the BOE publication date of the version
  (fecha_publicacion), `Enacted:` the date of the amending norm when it is itself consolidated, and `Norma:` its BOE id.
- **Git cannot store dates before 1970.** The 332 commits in force before 1970 are dated
  1970-01-01T00:00:01Z onwards, one second apart, in order; `In-force:` holds the real date. So never use
  `git log --before` for dates: use `tools/eslaw.py`, which reads `In-force:`.
- A norm's first commit is its first text in the BOE's record, dated the day it entered into force, with the date of
  the norm and its publication date in the message.
- Versions the BOE gives with an in-force date after 2026-10-28 are left out (295); there is no
  future branch. Versions the BOE gives without any in-force date cannot be placed in time and are left out
  (1156, listed by build/check_repo.py). Where a block has two versions on the same day, the last in
  the BOE's order is the one in force that day (300 earlier same-day versions).
- A version can come into force before an earlier-listed one (deferred entry into force): the text on a day is the
  version with the latest in-force date on or before it, as the BOE's own point-in-time view.

## How it is checked

- `build/check_repo.py`: every block version (including those that changed nothing and so have no commit of their
  own) equals, byte for byte, the file at the last commit in force on its date; and the words of every version's XML
  equal the words of its file. Last result: 397,165 block versions checked on their dates, 0 differ; 0 differ word for word from the XML; head files 326,037, missing 0, extra 0.
- A second build from the same data gives the same `main` hash: a second build from the same data gave the identical law history (law-head 56dbb7491cbd, same hash for all law commits).
- `tools/test_repo.py` runs the commands above and checks blame, the on-date tool, trailers and authors:
  6/6 passed.

## What "author" means

The author of a commit is the norm (id_norma) that the BOE names for the block versions in it: `BOE-A-2011-15210
(Reforma del artículo 135 de la Constitución Española, de 27 de septiembre de 2011)` at `boe-a-2011-15210@boe.invalid`, an
address that cannot exist. Rulings of the Tribunal Constitucional that annul text appear as `BOE-T-...`. The committer is
always `Lexifina`. Versions with no id_norma, or with one that is not a BOE identifier (the data has `BOE-A-0-0` for 48
versions and typos such as `BOE-A-201-9739`), are committed by `Agencia Estatal Boletin Oficial del Estado (BOE)`
<publisher@boe.invalid>, labelled `Explained-by: none (...)`; the identifier is quoted, never corrected
(14 such commits).

## What it does not show

- Only the BOE's consolidated texts: norms the BOE has not consolidated are not here, and the history of each norm
  starts with its first consolidated text. Regional (Autonómico) law is not included yet.
- Blame credits whole paragraphs; use `git log -p --word-diff` for the words.
- Notes in the text (`> Se modifica por ...`) are the BOE's own footnotes, kept as they are.
- The same words can mean different law: transitional provisions, rulings that interpret without annulling, and
  norms that suspend without amending change the law without changing these files.
- Spain's default rule on retroactivity (Código Civil art. 2.3; Constitución art. 9.3) is described in corpus.json;
  this repository does not decide whether a change reaches a given case.

## Layout

`estatal/<rango>/<year>/<BOE id>/<block>.md`: one folder per norm, grouped by rank (ley, ley-organica, real-decreto,
orden, ...) and by the year in its BOE id (so no folder lists more than 1,000 entries on GitHub), one file per block (article, heading, preamble, provision, annex) named by the BOE's block id. Each file
holds the block's paragraphs, one per line with a blank line between; markup only, never words, is added: `## `
before headings, `> ` before the BOE's notes and quoted text, table rows as `| a | b |`, images as links. Each norm's
`README.md` lists its blocks in the BOE's order. `normas.tsv` lists every norm with its last update date.

The `law-head` branch marks the last law commit. After each update new commits are added on top (append only).

## How it is built

See REPRODUCE.md. The builder is in `build/`; no AI wrote any legal text and no model runs at build time.

## Licence

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es). See LICENSE.
