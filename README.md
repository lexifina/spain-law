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

## Original build validation (2026-10-28)

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

## Repeals and unresolved validity

`data/acts.json` records BOE identifiers, lifecycle dates, causes and exhausted-validity flags. It records 1,559 dated repeals and 16 annulments. The original 1,159 repeal corrections remain unchanged. This append adds 415 dated lifecycle corrections: 0 remove unambiguously repealed files while retaining the unchanged BOE notice; 415 mark the act README and retain its wording and notices. Earlier wording remains available in the original history.

418 exhausted-validity records still have no resolved cessation date or cause. They remain labelled "as captured" without an in-force assertion. Missing text is explicitly marked in the index. Existing BOE repeal and annulment dates are preserved, and all existing causes (including unknown causes) are retained except BOE-A-2013-699: its cause is corrected to BOE-A-2023-12914 from the latest source notice at the recorded repeal date.

7 retained publisher notices differ from the latest publication state in the source evidence used for this record. They are preserved as historical notices, explicitly labelled in the act README and index, and linked to BOE for the current notice. Their wording has not been changed.

The text record ends on 2026-10-28. The reader reports a known BOE repeal or annulment on or after its date, including when a later query lies beyond the text cutoff; it provides no text for other dates beyond that cutoff. For retained wording with unresolved savings or transitional application, it reports that applicability requires separate analysis. The publisher-notice path in the index permits inspection within the text record; the unchanged source files remain directly inspectable in Git. A lifecycle status alone does not decide whether a saved provision applies to a particular case.

Source effective dates are recorded in In-force and author dates, with the existing pre-1970 convention. Appended committer timestamps preserve commit order. Earlier commits and tags are unchanged.

Retained BOE publisher notices remain readable through their published README links, including older notice-only acts without a lifecycle_notice field. Notice-only act directories and their documentation remain inspectable; the lifecycle guard applies to normative text.

The `on` command preserves the published reader's historical-record answers, including source versions retained after cessation; access does not establish revival or saved applicability. Use `current YYYY-MM-DD <act-or-block-path>` to apply recorded lifecycle boundaries and `status YYYY-MM-DD <act-or-block-path>` (or data/acts.json) for dated BOE repeal/annulment metadata. Source-dated later provisions are reported separately.

## Ordered same-day source versions

213 earlier BOE block versions on the same effective day are preserved as individually labelled correction commits, followed by the last source version of each affected block that day. The original commits and tags retain their published identities. The source index is `data/same-day-versions.json`; `Norma`, `Published`, and `Source-version-index` record the BOE provenance, including source states with identical wording. The end-of-day reader applies only the files named by each correction. These ordered records do not establish an intra-day period of applicability. 87 earlier versions are held for normative images, source/published-tip differences, future applicability, or whole-act reader compatibility; the text record still ends on 2026-10-28.


## Date corrections

Nine published block dates have source-backed correction records in [data/date-corrections.tsv](data/date-corrections.tsv). Seven dates are corrected; two retain earlier dates expressly stated by BOE. Later publisher notices of earlier events carry a `Retroactive` explanation. `Redates` identifies each original version. These records preserve the published normative files and the BOE repeal and annulment metadata.

The smoke checks validate dated normative records, labelled documentation and sourced corrections. An unchanged restored file retains its norm-authored historical provenance.
