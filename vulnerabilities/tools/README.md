# Tools

The scripts behind this Spain-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/spain-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only spain-law and its commit.
`build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`, `dead_ref_select.py`, `dead_ref_rebut.py`,
`patch_es.py` and `late_ext_check.py` sit two folders above the scripts, next to `config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Applies `patch_es.py`, indexes the history and texts, adds this repository's history rows, and runs the detectors, Spain's `es_crossref.py` last (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `patch_es.py` | The two Spanish fixes below, in the copy of global-law's scripts (`python -X utf8 patch_es.py <scripts dir>`; a fix already in place is skipped) |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, the empty periods, and the citations of acts no longer in force |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (those whose old and new date are in one sentence, then the shortest gaps; here 51, all of the first kind) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `dead_ref_select.py` | Chooses the 40 strongest citations of acts no longer in force, one per citing provision and cited act, ties broken in a fixed order, for global-law's `triage/dead_ref_triage.py` |
| `dead_ref_rebut.py` | Adds the same second pass to that review |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Spanish and English, light and dark |
| `config.json` | The repository, the Spanish category names, the files that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `redo.py` | Runs `patch_detectors.py`, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews]`; `EMBED_FONTS` names the script that embeds the chart's fonts). It does not run `patch_es.py` or `es_crossref.py`; run those first |
| `late_ext_check.py` | Hand-check helper: for each empty period that survived the review, the lines of the extending commit's diff that change the old date, in Spanish and numeric forms |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(build/|data/|tools/|README|REPRODUCE|LICENSE|normas\.tsv|corpus\.json)'`; every norm
is under `estatal/`, so the review of lapsed time limits in law texts drew the same 40 flags as the review of all of them.

The detectors in this copy already carry every fix of `patch_detectors.py`. Changes made for this repository:

- `patch_es.py`, Spanish dates: the time-limit search now also reads "hasta el día 31 de diciembre de 2020" ("día" between
  "hasta el" and the date) and "31 de diciembre del 2020" or "del año 2020". Lapsed time limits went from 4,006 to 4,266,
  empty periods from 112 to 113.
- `patch_es.py`, currencies: "marco" (framework) and "escudo" (coat of arms) count as currencies only in lower case, not in
  "Decisión marco 2002/629/JAI" and not in "escudo 390 mm". Dead currencies went from 5,214 to 4,965; the 249 matches
  dropped are mostly headings and list items such as "Artículo 4. Marco en el que se habilita el tratamiento" and
  "1. Escudo, emblema o logotipo".
- `add_root.py`: a commit that restates another commit's text (spain-law's 75 restatements after BOE's same-day versions,
  authored by Lexifina, with a `Re-asserts:` trailer) is credited to the act of the commit it restates. Before, all 197
  same-day conflicts had "Lexifina" as one of their acts. Law commits here carry no `Kind:` trailer and count as law;
  `Kind: correction` (repeals, annulments, same-day versions, dates) and `Kind: documentation` are left out.
- `run.sh` also runs global-law's Spain-only `detectors/es_crossref.py` (citations of acts BOE lists as no longer in force).
  It needs only BOE's `vigencia_agotada` column, which this repository's `normas.tsv` carries, so it runs from the
  repository alone. The other Spain-only checks (organic-law reserve, missing enabling power) need citations a model
  extracts and were not run.
- `run_triage.sh` adds global-law's `triage/dead_ref_triage.py` for those citations, on the 40 chosen by `dead_ref_select.py`
  (written to `findings/runref/`), and `dead_ref_rebut.py`, which writes the reviewed records to
  `findings/run/dead_act_ref_triage.jsonl`.
- `build_vulns.py` reads `ranked_dead_act_ref.parquet` and its review (category "Citations of acts no longer in force");
  matches empty-period reviews on the whole of both contexts, not their first 80 characters (two flags of the same file
  with the same opening words had shared a review), and lapsed time limits on 400 characters of context; and counts a file named in `not_law_files` (each norm's `README.md`,
  its list of blocks) as not law wherever it is.
- `flags_chart.py` names eleven to thirteen categories in words in English.
- After the restatements were credited to their acts, the same-day conflicts were reviewed again; the other categories'
  reviews were kept, as their flags did not change.
