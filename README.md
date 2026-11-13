# El derecho estatal español como historial de git

**Español** · [English](README.en.md)

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/es/effort-dark.svg">
<img alt="El derecho español en este repositorio: qué contiene, los cambios por año de entrada en vigor, la completitud frente a las fuentes oficiales y la exactitud de lo que contiene" src="data/es/effort-light.svg" width="880">
</picture>

Forma parte de [lexifina/global-law](https://github.com/lexifina/global-law), un único historial de git para el derecho de todos los países: este es el derecho nacional de España, que global-law lee en `spain/national/acts/`.

Todas las normas consolidadas de ámbito Estatal de la legislación consolidada del BOE, como historial de git:
**un commit por norma modificadora y fecha de entrada en vigor**, con esa norma como autora, de modo que `git blame`
nombra la norma que redactó cada párrafo y `git log` enumera las modificaciones de un precepto en el orden en que
entraron en vigor.

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es). Textos consolidados de carácter
meramente informativo; solo son oficiales los textos publicados en el «Boletín Oficial del Estado». Véase LICENSE.

8.774 normas, 16.736 commits, 397.165 versiones de bloques, en vigor desde el
1835-11-27 hasta el 2026-10-28. Datos obtenidos el 2026-10-28.

## Las preguntas

| Pregunta | Comando |
| --- | --- |
| ¿Qué decía el art. 135 de la Constitución el 26 de septiembre de 2011? | `python tools/eslaw.py on 2011-09-26 estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| ¿Y el día después de que entrara en vigor la reforma? | `python tools/eslaw.py on 2011-09-27 estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| La Constitución entera en un día, en orden | `python tools/eslaw.py on 1992-08-28 estatal/constitucion/1978/BOE-A-1978-31229` |
| ¿Qué norma redactó cada párrafo? | `git blame main -- estatal/constitucion/1978/BOE-A-1978-31229/a135.md` |
| ¿Cuándo cambió el art. 49 y por qué norma? | `python tools/eslaw.py log estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| Lo mismo en git puro | `git log --format=%(trailers:key=In-force,valueonly,separator=)%x09%an main -- estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| ¿Qué cambió exactamente, palabra por palabra? | `git log -p --word-diff --format=%an main -- estatal/constitucion/1978/BOE-A-1978-31229/a49.md` |
| Todo lo que cambió una norma | `git log --format=%H%x09%s --grep=^Norma:.BOE-A-2011-15210$ main` |
| El artículo 1 del Código Civil a lo largo del tiempo | `python tools/eslaw.py log estatal/real-decreto/1889/BOE-A-1889-4763/a1.md` |
| ¿Qué tipos de norma hay? | `git ls-tree --name-only main estatal/` |
| ¿Cuántos commits hizo el editor sin norma? | `git rev-list --count --author=publisher@boe.invalid main` |

En PowerShell, ponga entre comillas simples los argumentos que contengan `%`, `(` o `,`.

## Las fechas

- **Fecha del commit = fecha de entrada en vigor** (fecha_vigencia de la versión del bloque), a las 12:00 en
  Europe/Madrid: CET (+0100), y CEST (+0200) desde el último domingo de marzo hasta el último domingo de octubre (la
  regla de la UE, aplicada a todos los años desde 1970). El día se lee igual en todas partes.
- Cada commit de derecho lleva `In-force: YYYY-MM-DD`; `Published:` es la fecha de publicación de la versión en el BOE
  (fecha_publicacion), `Enacted:` la fecha de la norma modificadora cuando ella misma está consolidada, y `Norma:` su
  identificador del BOE.
- **Git no puede almacenar fechas anteriores a 1970.** Los 332 commits en vigor antes de 1970 llevan fechas a partir
  de 1970-01-01T00:00:01Z, con un segundo de diferencia entre ellos, en orden; `In-force:` contiene la fecha real. Por
  tanto, no use nunca `git log --before` para fechas: use `tools/eslaw.py`, que lee `In-force:`.
- El primer commit de una norma es su primer texto en el registro del BOE, con la fecha del día en que entró en vigor
  y con la fecha de la norma y su fecha de publicación en el mensaje.
- Las versiones a las que el BOE asigna una fecha de entrada en vigor posterior al 2026-10-28 quedan fuera (295); no
  hay rama de futuro. Las versiones que el BOE da sin ninguna fecha de entrada en vigor no pueden situarse en el tiempo
  y quedan fuera (1.156, enumeradas por build/check_repo.py). Cuando un bloque tiene dos versiones el mismo día, la
  última en el orden del BOE es la vigente ese día (300 versiones anteriores del mismo día).
- Una versión puede entrar en vigor antes que otra que figura antes en la lista (entrada en vigor diferida): el texto
  de un día es la versión con la fecha de entrada en vigor más reciente igual o anterior a ese día, como en la propia
  vista a una fecha del BOE.

## Validación de la construcción original (2026-10-28)

- `build/check_repo.py`: cada versión de bloque (incluidas las que no cambiaron nada y, por tanto, no tienen commit
  propio) es idéntica, byte a byte, al archivo del último commit vigente en su fecha; y las palabras del XML de cada
  versión coinciden con las palabras de su archivo. Último resultado: 397.165 versiones de bloques comprobadas en sus fechas, 0 difieren; 0 difieren palabra por palabra del XML; archivos en la cabeza 326.037, faltan 0, sobran 0.
- Una segunda construcción a partir de los mismos datos da el mismo hash de `main`: una segunda construcción a partir de los mismos datos dio un historial de derecho idéntico (law-head 56dbb7491cbd, mismo hash para todos los commits de derecho).
- `tools/test_repo.py` ejecuta los comandos anteriores y comprueba blame, la herramienta por fecha, los trailers y los
  autores: 6/6 superadas.

## Qué significa «autor»

El autor de un commit es la norma (id_norma) que el BOE indica para las versiones de bloque que contiene: `BOE-A-2011-15210
(Reforma del artículo 135 de la Constitución Española, de 27 de septiembre de 2011)` en `boe-a-2011-15210@boe.invalid`, una
dirección que no puede existir. Las sentencias del Tribunal Constitucional que anulan texto aparecen como `BOE-T-...`. El
committer es siempre `Lexifina`. Las versiones sin id_norma, o con uno que no es un identificador del BOE (los datos
tienen `BOE-A-0-0` en 48 versiones y erratas como `BOE-A-201-9739`), se atribuyen a `Agencia Estatal Boletin Oficial del Estado (BOE)`
<publisher@boe.invalid>, con la etiqueta `Explained-by: none (...)`; el identificador se cita tal cual, nunca se
corrige (14 commits de este tipo).

## Lo que no muestra

- Solo los textos consolidados del BOE: las normas que el BOE no ha consolidado no están aquí, y el historial de cada
  norma empieza con su primer texto consolidado. El derecho autonómico (Autonómico) todavía no está incluido.
- Blame atribuye párrafos enteros; use `git log -p --word-diff` para las palabras.
- Las notas del texto (`> Se modifica por ...`) son las propias notas al pie del BOE, conservadas tal cual.
- Las mismas palabras pueden significar un derecho distinto: las disposiciones transitorias, las sentencias que
  interpretan sin anular y las normas que suspenden sin modificar cambian el derecho sin cambiar estos archivos.
- La regla general de España sobre la retroactividad (Código Civil art. 2.3; Constitución art. 9.3) se describe en
  corpus.json; este repositorio no decide si un cambio alcanza a un caso concreto.

## Estructura

`estatal/<rango>/<year>/<BOE id>/<block>.md`: una carpeta por norma, agrupadas por rango (ley, ley-organica,
real-decreto, orden, ...) y por el año de su identificador del BOE (así ninguna carpeta muestra más de 1.000 entradas en GitHub), un archivo por bloque (artículo, encabezado, preámbulo, disposición, anexo) con el nombre del identificador de bloque del BOE. Cada
archivo contiene los párrafos del bloque, uno por línea con una línea en blanco entre ellos; solo se añade marcado, nunca palabras: `## `
antes de los encabezados, `> ` antes de las notas del BOE y del texto citado, filas de tablas como `| a | b |`, imágenes
como enlaces. El `README.md` de cada norma enumera sus bloques en el orden del BOE. `normas.tsv` enumera todas las
normas con su fecha de última actualización.

La rama `law-head` marca el último commit de derecho. Tras cada actualización se añaden commits nuevos encima (solo
adición).

## Cómo se construye

Véase REPRODUCE.md. El constructor está en `build/`; ninguna IA ha redactado texto jurídico alguno y no se ejecuta
ningún modelo durante la construcción.

## Licencia

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es). Véase LICENSE.

Esta es una traducción de la versión inglesa ([README.en.md](README.en.md)); si difieren, prevalece la versión inglesa.

## Derogaciones y vigencia no resuelta

`data/acts.json` registra los identificadores del BOE, las fechas del ciclo de vida, las causas y los indicadores de vigencia agotada. Registra 1.559 derogaciones con fecha y 16 anulaciones. Las 1.159 correcciones de derogación originales se mantienen sin cambios. Esta adición incorpora 415 correcciones del ciclo de vida con fecha: 0 eliminan archivos inequívocamente derogados conservando sin cambios el aviso del BOE; 415 marcan el README de la norma y conservan su redacción y sus avisos. La redacción anterior sigue disponible en el historial original.

418 registros de vigencia agotada siguen sin fecha ni causa de cese resueltas. Siguen etiquetados como "as captured" (tal como se obtuvieron) sin afirmar que estén en vigor. El texto que falta se marca expresamente en el índice. Se conservan las fechas de derogación y anulación del BOE existentes, y se mantienen todas las causas existentes (incluidas las desconocidas) salvo la de BOE-A-2013-699: su causa se corrige a BOE-A-2023-12914 conforme al aviso más reciente de la fuente en la fecha de derogación registrada.

7 avisos del editor conservados difieren del estado de publicación más reciente en las pruebas de la fuente utilizadas para este registro. Se conservan como avisos históricos, etiquetados expresamente en el README de la norma y en el índice, y enlazados al BOE para el aviso vigente. Su redacción no se ha modificado.

El registro de textos termina el 2026-10-28. El lector informa de una derogación o anulación conocida del BOE en su fecha o después de ella, también cuando una consulta posterior queda más allá del límite de los textos; no proporciona texto para otras fechas posteriores a ese límite. Para la redacción conservada cuya aplicación ultraactiva o transitoria no está resuelta, indica que su aplicabilidad requiere un análisis aparte. La ruta de avisos del editor en el índice permite la consulta dentro del registro de textos; los archivos de origen sin cambios siguen pudiendo consultarse directamente en Git. Un estado del ciclo de vida, por sí solo, no decide si una disposición con ultraactividad se aplica a un caso concreto.

Las fechas de efecto de la fuente se registran en In-force y en las fechas de autor, con la convención existente para las anteriores a 1970. Las marcas de tiempo de committer añadidas preservan el orden de los commits. Los commits y etiquetas anteriores no cambian.

Los avisos del editor del BOE conservados siguen pudiendo leerse a través de los enlaces de README publicados, incluidas las normas antiguas que solo tienen aviso y carecen del campo lifecycle_notice. Los directorios de normas que solo tienen aviso y su documentación siguen pudiendo consultarse; la protección del ciclo de vida se aplica al texto normativo.

El comando `on` conserva las respuestas del registro histórico del lector publicado, incluidas las versiones de origen conservadas tras el cese; el acceso no implica reviviscencia ni aplicabilidad ultraactiva. Utilice `current YYYY-MM-DD <act-or-block-path>` para aplicar los límites del ciclo de vida registrados y `status YYYY-MM-DD <act-or-block-path>` (o data/acts.json) para los metadatos fechados de derogación o anulación del BOE. Las disposiciones posteriores fechadas por la fuente se indican por separado.

## Versiones de origen del mismo día, en orden

213 versiones anteriores de bloques del BOE del mismo día de efecto se conservan como commits de corrección etiquetados individualmente, seguidos de la última versión de origen de cada bloque afectado ese día. Los commits y etiquetas originales mantienen sus identidades publicadas. El índice de origen es `data/same-day-versions.json`; `Norma`, `Published` y `Source-version-index` registran la procedencia en el BOE, incluidos los estados de origen con redacción idéntica. El lector de fin de día aplica solo los archivos indicados en cada corrección. Estos registros ordenados no establecen un periodo de aplicabilidad dentro del día. 87 versiones anteriores quedan retenidas por imágenes normativas, diferencias entre la fuente y la punta publicada, aplicabilidad futura o compatibilidad del lector con normas completas; el registro de textos sigue terminando el 2026-10-28.


## Correcciones de fechas

Nueve fechas de bloques publicadas tienen registros de corrección respaldados por la fuente en [data/date-corrections.tsv](data/date-corrections.tsv). Se corrigen siete fechas; dos conservan fechas anteriores que el BOE indica expresamente. Los avisos posteriores del editor sobre hechos anteriores llevan una explicación `Retroactive`. `Redates` identifica cada versión original. Estos registros conservan los archivos normativos publicados y los metadatos de derogación y anulación del BOE.

Las comprobaciones rápidas (smoke checks) validan los registros normativos fechados, la documentación etiquetada y las correcciones respaldadas por la fuente. Un archivo restaurado sin cambios conserva su procedencia histórica atribuida a la norma.

## Más información

Del repositorio [lexifina/global-law](https://github.com/lexifina/global-law) (páginas en inglés):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): todas las funciones y lo que cada corpus debe admitir (`git blame`, `law.py`, herramientas MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): preguntas y respuestas · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proponer cambios · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): servidor MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): cómo se ha construido · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): lo actualizado que está cada corpus · [Supervisión](https://github.com/lexifina/global-law/tree/main/monitoring): si las actualizaciones funcionan · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): cómo se vigila cada fuente oficial para detectar cambios
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): la rapidez de las herramientas, medida
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): gráficos y conexiones a través del derecho de todo el mundo
- [Vulnerabilidades](https://github.com/lexifina/global-law/tree/main/vulnerabilities): errores en las normas tal como se publicaron
