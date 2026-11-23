<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Supervisión: qué se lee y qué resulta

[English](README.en.md)

Cómo supervisa global-law todos los países: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Esta página hace lo mismo solo para España: cada vez que se lee una fuente oficial, cuándo y qué resultó (normas añadidas, modificadas y retiradas). La forma legible por máquina está en [data/checks/](../data/checks/) (JSON Lines, esquema `lexifina-check/1`), en `git log` como commits `Kind: check`, y mes a mes en [checks/](checks/).

**Última comprobación:** 2026-11-23 13:46 UTC, Legislación consolidada del BOE, normas estatales (datos abiertos): 1366 direcciones leídas; 1 añadidas, 35 modificadas, 1 retiradas; cambios encontrados; 71 sin publicar, 0 de ellas sin motivo. Avisos: `publish-lag`.

## Fuentes

| Fuente | Carpetas | Frecuencia | Última comprobación correcta | Último resultado | Estado |
| --- | --- | --- | --- | --- | --- |
| [Legislación consolidada del BOE, normas estatales (datos abiertos)](https://www.boe.es/datosabiertos/api/api.php) | `estatal/` | diaria | 2026-11-23 13:46 UTC | cambios encontrados | vigilada |

## Los últimos 30 días

| Inicio (UTC) | Fuente | Leídas | Añadidas | Modificadas | Retiradas | Sin publicar (sin motivo) | Resultado | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
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
