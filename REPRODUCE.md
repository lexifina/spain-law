# Reproducing the Spanish legislative record

The original record is preserved at commit `ee54e80899c6312724f34f48caab1a90d3a7985d`. Its source digest is
`fd12fb6533c711792ba54f678c88af0c7ba1feb94ec7ba0cde974a425b23a9d6`,
and its source snapshot is dated 2026-10-28. Original build facts, tool
versions and verification records remain in that commit's REPRODUCE.md:

```sh
git show ee54e80899c6312724f34f48caab1a90d3a7985d:REPRODUCE.md
```

## Source

Agencia Estatal Boletín Oficial del Estado consolidated legislation:
https://www.boe.es/datosabiertos/api/api.php

Basado en datos de la Agencia Estatal Boletín Oficial del Estado
(https://www.boe.es). The consolidated texts are informative; only the official
gazette texts are authoritative. Attribution and reuse conditions are in LICENSE.

## Repeal appendix

The inputs are the original normas.tsv, the initial BOE publisher notices and their
version publication and effective-date attributes. The helper module
`tools/append_repeals.py` exposes `make_plan`, `index_document` and `build`.
Its source inputs are the original boe.sqlite and parsed.sqlite records produced by
the original build. The public metadata uses corpus_tables from world-law-ops
revision `3d49b9e76aee06d9eaf4746ba9b43d8890a6cd25`.

The appendix records 1,159 unambiguous whole-act repeals. Each correction retains
the exact BOE notice and removes the other normative files for the stated interval.
Author dates and In-force use the source effective date; pre-1970 author timestamps
use the original convention of a 1970 timestamp with the true In-force trailer.
Appended committer timestamps increase from the published head. Correction ranges
run from the stated effective day to 2026-10-28; the reader rejects later
dates. Original commits and tags remain unchanged.

832 exhausted-validity records remain unresolved because of missing dates,
qualified effects, retained provisions, conflicting source facts or unverified
retroactivity. They are not asserted to be in force. Missing text is separately
marked in data/acts.json. No lifecycle dates are invented.

## Verification

The correction gate compares retained notice words with BOE XML and compares
unchanged files with the published base. The 30-act source sample compares repeal
dates and identifiers with BOE independently. The native tests cover blame,
historical amendment boundaries, file history, identities, tags and README commands.
The deterministic append uses the same published base and source facts.

## AI use

GPT-6 wrote the extraction and verification code. GPT-6 Astra independently
reviewed the source evidence and resulting changes. No model wrote or corrected
legislative wording.
