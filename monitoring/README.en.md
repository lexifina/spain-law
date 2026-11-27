<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Español](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Spain only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-27 06:17 UTC, BOE consolidated legislation, state norms (open data): 1140 addresses read; 2 added, 31 changed, 0 removed; changes found; 79 not published, 0 of them with no reason. Flags: `publish-lag`, `audit-disagrees`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [BOE consolidated legislation, state norms (open data)](https://www.boe.es/datosabiertos/api/api.php) | `estatal/` | daily | 2026-11-27 06:17 UTC | changes found | watched |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-27 05:27](checks/2026-11.md#es-boe-estatal-20261127t052756z) | boe-estatal | 1140 | 2 | 31 | 0 | 79 (0) | changes found `publish-lag` `audit-disagrees` | [6](https://github.com/lexifina/spain-law/compare/be7dfa71924b...75d82c70ac6b) |
| [2026-11-26 05:27](checks/2026-11.md#es-boe-estatal-20261126t052734z) | boe-estatal | 1159 | 1 | 57 | 0 | 79 (0) | changes found `publish-lag` `audit-disagrees` | [23](https://github.com/lexifina/spain-law/compare/78a9ddb36211...738f519892b2) |
| [2026-11-25 05:24](checks/2026-11.md#es-boe-estatal-20261125t052409z) | boe-estatal | 1135 | 0 | 29 | 1 | 74 (0) | changes found `publish-lag` `audit-disagrees` | [16](https://github.com/lexifina/spain-law/compare/5cc5c45518d3...7e0583ee86b5) |
| [2026-11-24 06:24](checks/2026-11.md#es-boe-estatal-20261124t062451z) | boe-estatal | 1123 | 2 | 11 | 0 | 71 (0) | changes found `publish-lag` `audit-disagrees` | [15](https://github.com/lexifina/spain-law/compare/0b24cacff005...c9acb879b7ef) |
| [2026-11-23 12:45](checks/2026-11.md#es-boe-estatal-20261123t124518z) | boe-estatal | 1366 | 1 | 35 | 1 | 71 (0) | changes found `publish-lag` | [82](https://github.com/lexifina/spain-law/compare/d0ca342dba9b...1a9a766d2a9c) |
| [2026-11-23 01:06](checks/2026-11.md#es-boe-estatal-20261123t010631z) | boe-estatal | 10 | 0 | 0 | 0 | 343 (0) | no change `publish-lag` | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
