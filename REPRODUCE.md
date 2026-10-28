# How this repository was made

Everything needed to rebuild `main` hash for hash.

## Source

- Agencia Estatal Boletín Oficial del Estado, open-data API for consolidated legislation:
  https://www.boe.es/datosabiertos/api/api.php
  - `GET /datosabiertos/api/legislacion-consolidada?limit=5000&offset=N` (JSON): every consolidated norm. The API
    caps one page at 10,000 rows even with `limit=-1`, so the list is read in pages.
  - `GET /datosabiertos/api/legislacion-consolidada/id/<id>/texto` (XML): every block of a norm with every version
    (`<version id_norma fecha_publicacion fecha_vigencia>`).
  - `GET /datosabiertos/api/legislacion-consolidada/id/<id>/analisis` (JSON): the norms that amended it, for the
    short titles of amending norms that are not themselves consolidated.
- Retrieved 2026-10-28: 17,647 cached answers, sha256 over all of them
  (URL order) `fd12fb6533c711792ba54f678c88af0c7ba1feb94ec7ba0cde974a425b23a9d6`.
- Terms checked before the bulk fetch: the reuse conditions at https://www.boe.es/informacion/aviso_legal/index.php
  allow commercial and non-commercial reuse, including derived works, with attribution (see LICENSE).
  https://www.boe.es/robots.txt has rules for `User-agent: *` only, none covering /datosabiertos/, no Crawl-delay and
  no rules for AI agents.
- Rate: at most 4 requests at once, User-Agent `lexifina-spain-law/1.0 (...; spain-law@lexifina.com)`, every answer
  (404s too) cached on disk. 17,646 requests (4 list pages, 8,821 /texto, 8,821 /analisis), every one HTTP 200; 4 concurrent, no pause between requests, about 455 requests a minute (avg 588 ms per /texto, 455 ms per /analisis), 1.34 GB of XML and JSON in 39 minutes; no 429 or 5xx answers, so no slower rate was needed. The server sends no gzip even when asked
  (`Accept-Encoding: gzip`), so the cache stores answers gzipped.

## Commands, in order

```
cd scripts/spain-law               # the builder folder in the Lexifina monorepo; a copy is in build/
python -X utf8 fetch.py list
python -X utf8 fetch.py texts --ambito Estatal --analisis
python -X utf8 parse.py --ambito Estatal
python -X utf8 build.py --repo ../../../spain-law --today 2026-10-28 --docs-date 2026-10-28
python -X utf8 check_repo.py --repo ../../../spain-law --today 2026-10-28 --record
python -X utf8 test_repo.py --repo ../../../spain-law --record
python -X utf8 build.py --repo ../../../spain-law --today 2026-10-28 --docs-date 2026-10-28 --verify-rebuild
```

`--today` is the data's retrieval day (versions in force later are left out); `--docs-date` dates this documentation
commit. Both are fixed arguments, never the run day.

## Tools

git version 2.46.0.windows.1; Python 3.12.10 (standard library only).

| File | git blob |
| --- | --- |
| build/fetch.py | `537500863fa215a23a2e1aec5ac37f271061e4ff` |
| build/parse.py | `642609d63876c22cfd7d045cf3876f515e18513e` |
| build/boe.py | `2dcb5ffbed5eacfc5815a9a73fa921394235f05a` |
| build/build.py | `b16023fffd01d11e966848e70e3a0069a75d0f47` |
| build/reproduce.py | `600c45932b5d1030663b34bb2251a3b218fdebe7` |
| build/check_repo.py | `53f7ba7c8019fdb8e0d8ae1cda0a7e48f7981c2d` |
| build/test_repo.py | `6f7d4e6b4ec07a52e53a91cbe9d446a4e033d654` |

## Build facts

```
{
 "clamped": 332,
 "commits": 16736,
 "files_written": 410868,
 "first_in_force": "1835-11-27",
 "future_versions": 295,
 "groups_without_change": 13,
 "last_in_force": "2026-10-28",
 "law_commits": 16722,
 "laws_written": 8774,
 "publisher_commits": 14,
 "versions": 397165,
 "versions_unchanged": 77
}
```

## Checks (previous build from the same data)

```
{
 "check": {
  "checked": 397165,
  "differ": 0,
  "ok": true,
  "summary": "397,165 block versions checked on their dates, 0 differ; 0 differ word for word from the XML; head files 326,037, missing 0, extra 0",
  "words_differ": 0
 },
 "rebuild": {
  "ok": true,
  "summary": "a second build from the same data gave the identical law history (law-head 56dbb7491cbd, same hash for all law commits)"
 },
 "same_day": 300,
 "smoke": {
  "results": [
   {
    "detail": "estatal/constitucion/1978/BOE-A-1978-31229/a135.md lines by BOE-A-1978-31229 (Constitución Española), BOE-A-2011-15210 (Reforma de 27 de septiembre de 2011)",
    "ok": true,
    "test": "blame names a norm"
   },
   {
    "detail": "estatal/constitucion/1978/BOE-A-1978-31229/a135.md 2011-09-26 != 2011-09-27; estatal/constitucion/1978/BOE-A-1978-31229/a49.md 2024-02-16 != 2024-02-17",
    "ok": true,
    "test": "text before and after an amendment"
   },
   {
    "detail": "estatal/constitucion/1978/BOE-A-1978-31229/a135.md 2 commits; estatal/constitucion/1978/BOE-A-1978-31229/a49.md 2 commits; estatal/real-decreto/1889/BOE-A-1889-4763/a1.md 2 commits",
    "ok": true,
    "test": "log --follow in date order"
   },
   {
    "detail": "0 tags resolve; 16736 law commits carry In-force",
    "ok": true,
    "test": "tags resolve, In-force on every law commit"
   },
   {
    "detail": "only the documentation commit 59bc07f41d is by Lexifina; 15953 distinct authors",
    "ok": true,
    "test": "only the documentation commit is by Lexifina"
   },
   {
    "detail": "11 README commands ran and printed output",
    "ok": true,
    "test": "README commands run"
   }
  ],
  "summary": "6/6 passed"
 },
 "undated": 1156
}
```

## Decisions made by hand

- Scope: every norm with ámbito Estatal in the BOE's consolidated list.
- One file per block, not per norm: git fast-import deltas a blob only against the previous blob it wrote, so with
  one file per norm and many norms per commit the pack would hold every version of a large code in full.
- Same-day versions of one block: the last in the BOE's order is kept. Undated versions are left out.
- Date rule: noon Europe/Madrid with the EU summer-time rule for every year (Spain's 1974–1980 summer times differ).
- Short author names: the citation part of the title (`Ley 15/2015, de 2 de julio`); for norms that are not
  consolidated, the BOE's own wording in the analysis of the amended norm (`por Ley 2/2020, de ...`).

## What the AI did

The builder was written and run by Claude Code with Claude Opus 5.5 (`claude-opus-5-5`), directed by Lexifina. No
AI wrote any legal text, summary or commit content: every word of law comes from the BOE, and commit messages are
assembled by code from the BOE's metadata. No model runs at build time.
