# Spanish law in 20 charts

[Español](README.md)

Charts on every country's law, from the whole of global-law: [global-law visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations). These are the charts on Spain alone.

Twenty charts on Spanish state law, drawn only from the data in this repository: the 8,774 state norms (ámbito Estatal) of the BOE's consolidated legislation, one file per block (article, provision, annex); the 16,736 commits of the BOE build, one per amending norm and day of entry into force, with the norms and blocks each one changed; the status of the 8,821 norms in `data/acts.json`; and the BOE's notes on the Congreso's vote on each royal decree-law.

Open [`el-derecho-espanol-en-20-graficos.html`](el-derecho-espanol-en-20-graficos.html) in a browser. The page is one file with all its data inside; it loads only the d3 and topojson-client libraries, the world map of chart 3 and its fonts from the web. The controls at the top right switch the language (Spanish or English) and the theme (light or dark). Each chart names its data path in the repository, its record count and its limits, and has a table of every number under it. Hover over a mark for the exact values.

The charts are descriptive: they show what the record holds, not why.

## The charts

### I. The state law in force

#### 1. 6,782 state norms in force

The norms by rank and status, with their blocks: 65% of those in force are royal decrees or ministerial orders; 943 laws and organic laws.

![6,782 state norms in force](stills/en/01.png)

#### 2. The age of the law in force

The norms in force by the year of their date: 408 predate the Constitution, back to a Royal Order of 1835; the Criminal Procedure Act of 1882 and the Civil Code of 1889 among the oldest.

![The age of the law in force](stills/en/02.png)

#### 3. International agreements

The 179 bilateral agreements by state and subject, on a map: 103 are about tax; the nationality agreements are with 12 Ibero-American countries and, since 2021, France.

![International agreements](stills/en/03.png)

### II. How the law changes

#### 4. Who changes the law

The 20,024 changes since 1979 by the rank of the norm that makes them: royal decrees 31% since 2000; in 2020, royal decree-laws made 67% of the changes to laws.

![Who changes the law](stills/en/04.png)

#### 5. The most changed norms

The 20 norms changed by the most norms, by five-year period (the 1994 General Social Security Act, 102), and the articles rewritten most often (article 91 of the VAT Act, 41 times).

![The most changed norms](stills/en/05.png)

#### 6. Omnibus laws

The norms that changed the most norms at once: Law 62/2003, the budget's accompanying law, 94; budget laws and decree-laws since 2020.

![Omnibus laws](stills/en/06.png)

#### 7. Consolidated texts

The amending norms gathered by five texts until a consolidated text (texto refundido) or a new law replaced them: 102 for the 1994 General Social Security Act.

![Consolidated texts](stills/en/07.png)

### III. The Cortes and the Government

#### 8. Laws and decree-laws

Laws, organic laws and royal decree-laws per year and per Prime Minister: 39 decree-laws in 2020 against 14 laws; no ordinary law in 2016.

![Laws and decree-laws](stills/en/08.png)

#### 9. Laws by month

The laws of 2004–2026 by month: 21% in December; 537 days without an ordinary law between October 2015 and April 2017.

![Laws by month](stills/en/09.png)

#### 10. The convalidation of decree-laws

The Congreso's vote on each royal decree-law of 2020–2026: 10 of 128 repealed, 5 of them in 2026; a median of 17 days to the resolution.

![The convalidation of decree-laws](stills/en/10.png)

#### 11. Decree-laws amending one another

The decree-laws of 2020 that changed other decree-laws of the same year, as arcs: 57 changes, 15 of them to Royal Decree-law 8/2020.

![Decree-laws amending one another](stills/en/11.png)

#### 12. The budget laws

The day each budget law was published, counted from 1 January of its year: none for 1996, 2019, 2020, 2024, 2025 and 2026; the 2018 one on 4 July.

![The budget laws](stills/en/12.png)

### IV. The BOE's calendar

#### 13. The weekday of royal decrees

The weekday of the dates of royal decrees and decree-laws, year by year: Fridays from 1986 to 2019, Tuesdays from January 2020, Wednesdays from November 2025.

![The weekday of royal decrees](stills/en/13.png)

#### 14. From a norm's date to the BOE

The days from a norm's date to its publication: royal decrees took a median of 15 days in 1979–1999 and one since 2020.

![From a norm's date to the BOE](stills/en/14.png)

#### 15. Entry into force

The days from publication to entry into force: 63% of laws since 2020 take effect the next day; 59% before 1979 waited the Civil Code's twenty days.

![Entry into force](stills/en/15.png)

#### 16. The calendar

The days of the year on which the changes of 2000–2025 took effect (1 January, 9.9%), and the weekdays of publication and of entry into force.

![The calendar](stills/en/16.png)

### V. The Constitution, the codes and the courts

#### 17. The Constitution

The 169 articles of the Constitution and its four amendments (1992, 2011, 2024, 2026), each to one article; the organic laws changed most (the Organic Law of the Judiciary, 81).

![The Constitution](stills/en/17.png)

#### 18. The Civil Code

The 2,005 articles of the 1889 Civil Code coloured by when their current text was written: 1,276 keep the original wording.

![The Civil Code](stills/en/18.png)

#### 19. The Criminal Code

The 56 norms that changed the 1995 Criminal Code and the articles each wrote (Organic Law 1/2015, 276), and the articles rewritten most often.

![The Criminal Code](stills/en/19.png)

#### 20. The courts in the text

The judgments the BOE credits with changing a text: 192 of the Constitutional Court since 2008 and 341 Supreme Court rulings; the laws they changed most.

![The courts in the text](stills/en/20.png)

## Data

As of commit `9bf7a4447f` (history read on `law-head`, `56dbb7491c`); the BOE's data as of 28 October 2026.

| Dataset | Where in the repository | Records | Coverage |
| --- | --- | ---: | --- |
| Norms and their blocks | `estatal/<rank>/<year>/<BOE id>/` | 8,774 norms, 284,435 files | the state norms of the BOE's consolidated legislation; regional law is in other repositories |
| Status of each norm | `data/acts.json`, `normas.tsv` | 8,821 norms | in force, repealed, expired, annulled; dates of enactment, publication, entry into force and repeal |
| History | git log (`In-force:`, `Published:`, `Norma:`), `--name-status` on `law-head` | 16,736 commits, 20,352 changes of one norm by another | each norm's history starts at its first consolidated text; versions after 28 October 2026 are left out |
| Named norms | titles in `normas.tsv`, commit authors | 7,669 laws, organic laws, decree-laws, legislative decrees and royal decrees named with their date | the highest number of each year gives the count of laws, organic laws and decree-laws |
| BOE notes | `estatal/real-decreto-ley/<year>/<BOE id>/no.md`, `ir.md` (on `law-head`) | 116 royal decree-laws of 2017–2026 with a note | the Congreso's convalidation or repeal of royal decree-laws, systematic from 2020 |
| Texts read | the blocks of the Constitution, the Civil Code and the Criminal Code; 45 READMEs; 40 blocks | 3,639 blocks | article numbers, structure, and emptied articles |

## Limits

- **Only state law the BOE consolidates.** Regional law, norms the BOE does not consolidate, and norms repealed before the BOE consolidated them are not in the record; counts by year are of the norms the record holds.
- **Each norm's history starts at its first consolidated text.** For most norms that is the text as published; for a few old ones (the Commercial Code, the Criminal Procedure Act) it is a later text.
- **Highest numbers are minimums.** Before 1983 for laws and 2004 for decree-laws, the record names fewer than half of each year's norms and may miss the last ones (chart 8 draws those years lighter).
- **The Congreso's vote on decree-laws** is noted systematically only from 2020 (chart 10).
- **Categories are read from names and titles.** The rank of the norm that makes a change, the subject and other party of an agreement, budget and accompanying laws follow the rules in `src/prep.py`; whatever no rule recognises counts as "other".
- **Court rulings** count only when the BOE credits them with a change of text (chart 20).
- **2026 is partial** (to 28 October) and drawn lighter.

## Rebuilding

```sh
python visualisations/src/make.py            # history, trees, tables and texts -> src/.build/ -> el-derecho-espanol-en-20-graficos.html
node visualisations/src/stills.cjs           # images for these READMEs (needs Playwright; PLAYWRIGHT=<path> if not global)
```

`make.py` reads everything from git objects, so it also works in a blobless (`--filter=blob:none`) or `--no-checkout` clone, where it downloads only the tables (`normas.tsv`, `corpus.json`, `data/acts.json`, `data/date-corrections.tsv`), the notes of the royal decree-laws, the blocks of the Constitution, the Civil Code and the Criminal Code, and a few READMEs and blocks: about 4,000 small files. It reads `origin/main` (or `HEAD`) and the history of `origin/law-head` by default; `--ref` and `--history-ref` pick others. It writes nothing into the repository except the page and the `src/.build/` folder (which git ignores).

| File | What it does |
| --- | --- |
| `src/make.py` | extracts the history, the trees, the tables and the texts into `src/.build/`, then runs `prep.py` and `build.py` |
| `src/prep.py` | computes every number for the 20 charts and the data profile into `src/.build/data.json` |
| `src/page.tpl.html` | the page: text in both languages, the charts (d3), the tables |
| `src/build.py` | puts `data.json` into the template and writes the page |
| `src/stills.cjs` | draws each chart as a PNG into `stills/es/` and `stills/en/` |

## Source and licence

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es): the texts are the BOE's consolidated texts, reused under its reuse conditions (Resolution of 27 June 2024). They are informative only; only the texts published in the «Boletín Oficial del Estado» are official and authentic. The code and documentation are CC0 1.0. See [`LICENSE`](../LICENSE).
