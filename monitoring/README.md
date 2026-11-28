<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Supervisión: qué se lee y qué resulta

[English](README.en.md)

Cómo supervisa global-law todos los países: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Esta página hace lo mismo solo para España: cada vez que se lee una fuente oficial, cuándo y qué resultó (normas añadidas, modificadas y retiradas). La forma legible por máquina está en [data/checks/](../data/checks/) (JSON Lines, esquema `lexifina-check/1`), en `git log` como commits `Kind: check`, y mes a mes en [checks/](checks/).

**Última comprobación:** 2026-11-28 06:20 UTC, Legislación consolidada del BOE, normas estatales (datos abiertos): 1179 direcciones leídas; 13 añadidas, 63 modificadas, 7 retiradas; cambios encontrados; 85 sin publicar, 0 de ellas sin motivo. Avisos: `publish-lag`, `audit-disagrees`.

## Fuentes

| Fuente | Carpetas | Frecuencia | Última comprobación correcta | Último resultado | Estado |
| --- | --- | --- | --- | --- | --- |
| [Legislación consolidada del BOE, normas estatales (datos abiertos)](https://www.boe.es/datosabiertos/api/api.php) | `estatal/` | diaria | 2026-11-28 06:20 UTC | cambios encontrados | vigilada |

## Los últimos 30 días

| Inicio (UTC) | Fuente | Leídas | Añadidas | Modificadas | Retiradas | Sin publicar (sin motivo) | Resultado | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-28 05:28](checks/2026-11.md#es-boe-estatal-20261128t052859z) | boe-estatal | 1179 | 13 | 63 | 7 | 85 (0) | cambios encontrados `publish-lag` `audit-disagrees` | [22](https://github.com/lexifina/spain-law/compare/9da13e4ac389...114e9399ff39) |
| [2026-11-27 05:27](checks/2026-11.md#es-boe-estatal-20261127t052756z) | boe-estatal | 1140 | 2 | 31 | 0 | 79 (0) | cambios encontrados `publish-lag` `audit-disagrees` | [6](https://github.com/lexifina/spain-law/compare/be7dfa71924b...75d82c70ac6b) |
| [2026-11-26 05:27](checks/2026-11.md#es-boe-estatal-20261126t052734z) | boe-estatal | 1159 | 1 | 57 | 0 | 79 (0) | cambios encontrados `publish-lag` `audit-disagrees` | [23](https://github.com/lexifina/spain-law/compare/78a9ddb36211...738f519892b2) |
| [2026-11-25 05:24](checks/2026-11.md#es-boe-estatal-20261125t052409z) | boe-estatal | 1135 | 0 | 29 | 1 | 74 (0) | cambios encontrados `publish-lag` `audit-disagrees` | [16](https://github.com/lexifina/spain-law/compare/5cc5c45518d3...7e0583ee86b5) |
| [2026-11-24 06:24](checks/2026-11.md#es-boe-estatal-20261124t062451z) | boe-estatal | 1123 | 2 | 11 | 0 | 71 (0) | cambios encontrados `publish-lag` `audit-disagrees` | [15](https://github.com/lexifina/spain-law/compare/0b24cacff005...c9acb879b7ef) |
| [2026-11-23 12:45](checks/2026-11.md#es-boe-estatal-20261123t124518z) | boe-estatal | 1366 | 1 | 35 | 1 | 71 (0) | cambios encontrados `publish-lag` | [82](https://github.com/lexifina/spain-law/compare/d0ca342dba9b...1a9a766d2a9c) |
| [2026-11-23 01:06](checks/2026-11.md#es-boe-estatal-20261123t010631z) | boe-estatal | 10 | 0 | 0 | 0 | 343 (0) | sin cambios `publish-lag` | — |

## Compruébelo usted mismo

```
python tools/checktrail.py                      # la última comprobación de cada fuente
python tools/checktrail.py --day 2026-11-23     # todas las comprobaciones de un día
python tools/checktrail.py --act <id>           # cuándo se vio y se publicó una norma
git log --grep='^Kind: check' --format='%ci %s'  # las comprobaciones en el historial
```

Solo tiene fuerza jurídica la publicación oficial (el «Boletín Oficial del Estado» y los diarios oficiales autonómicos); los textos de este repositorio son copias para leer y buscar.
