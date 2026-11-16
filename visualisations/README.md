# El derecho español en 20 gráficos

[English](README.en.md)

Gráficos del derecho de todos los países, a partir de todo global-law: [global-law visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations). Aquí, solo los de España.

Veinte gráficos del derecho estatal español, dibujados solo con los datos de este repositorio: las 8.774 normas de ámbito estatal de la legislación consolidada del BOE, con un archivo por bloque (artículo, disposición, anexo); los 16.736 commits de la construcción a partir del BOE, uno por norma modificadora y día de entrada en vigor, con las normas y los bloques que cambió cada uno; la situación de las 8.821 normas de `data/acts.json`, y las notas del BOE sobre la votación del Congreso de cada real decreto-ley.

Abra [`el-derecho-espanol-en-20-graficos.html`](el-derecho-espanol-en-20-graficos.html) en un navegador. La página es un solo archivo con todos sus datos dentro; de la web solo carga las bibliotecas d3 y topojson-client, el mapa del mundo del gráfico 3 y sus fuentes tipográficas. Los botones de arriba a la derecha cambian el idioma (español o inglés) y el tema (claro u oscuro). Cada gráfico indica su fuente en el repositorio, el número de registros y sus límites, y debajo tiene una tabla con todas las cifras. Pase el cursor sobre un elemento para ver los valores exactos.

Los gráficos son descriptivos: muestran lo que contiene el registro, no sus causas.

## Los gráficos

### I. El derecho estatal en vigor

#### 1. 6.782 normas estatales en vigor

Las normas por rango y situación, con sus bloques: el 65 % de las que están en vigor son reales decretos u órdenes ministeriales; 943 son leyes y leyes orgánicas.

![6.782 normas estatales en vigor](stills/es/01.png)

#### 2. La edad del derecho vigente

Las normas en vigor por el año de su fecha: 408 son anteriores a la Constitución, hasta una Real Orden de 1835; entre las más antiguas, la Ley de Enjuiciamiento Criminal de 1882 y el Código Civil de 1889.

![La edad del derecho vigente](stills/es/02.png)

#### 3. Los acuerdos internacionales

Los 179 acuerdos bilaterales por Estado y materia, sobre un mapa: 103 son fiscales; los de nacionalidad, con 12 países iberoamericanos y, desde 2021, Francia.

![Los acuerdos internacionales](stills/es/03.png)

### II. Cómo cambia el derecho

#### 4. Quién cambia el derecho

Los 20.024 cambios desde 1979 por el rango de la norma que los hace: los reales decretos, el 31 % desde 2000; en 2020, los reales decretos-leyes hicieron el 67 % de los cambios en las leyes.

![Quién cambia el derecho](stills/es/04.png)

#### 5. Las normas más modificadas

Las 20 normas que más normas han modificado, por periodos de cinco años (la Ley General de la Seguridad Social de 1994, 102), y los artículos reescritos más veces (el 91 de la Ley del IVA, 41).

![Las normas más modificadas](stills/es/05.png)

#### 6. Leyes ómnibus

Las normas que cambiaron más normas a la vez: la Ley 62/2003, de acompañamiento de los presupuestos, 94; las leyes de presupuestos y, desde 2020, los decretos-leyes.

![Leyes ómnibus](stills/es/06.png)

#### 7. Textos refundidos

Las normas modificadoras que reunieron cinco textos hasta que un texto refundido o una ley nueva los sustituyó: 102 la Ley General de la Seguridad Social de 1994.

![Textos refundidos](stills/es/07.png)

### III. Las Cortes y el Gobierno

#### 8. Leyes y decretos-leyes

Leyes, leyes orgánicas y reales decretos-leyes por año y por presidente del Gobierno: 39 decretos-leyes en 2020 frente a 14 leyes; ninguna ley ordinaria en 2016.

![Leyes y decretos-leyes](stills/es/08.png)

#### 9. Leyes por mes

Las leyes de 2004 a 2026 por mes: el 21 % en diciembre; 537 días sin una ley ordinaria entre octubre de 2015 y abril de 2017.

![Leyes por mes](stills/es/09.png)

#### 10. La convalidación de los decretos-leyes

El voto del Congreso sobre cada real decreto-ley de 2020 a 2026: 10 de 128 derogados, 5 de ellos en 2026; una mediana de 17 días hasta la resolución.

![La convalidación de los decretos-leyes](stills/es/10.png)

#### 11. Decretos-leyes que se modifican entre sí

Los decretos-leyes de 2020 que cambiaron otros decretos-leyes del mismo año, en arcos: 57 cambios, 15 de ellos en el Real Decreto-ley 8/2020.

![Decretos-leyes que se modifican entre sí](stills/es/11.png)

#### 12. Las leyes de presupuestos

El día en que se publicó cada ley de presupuestos, contado desde el 1 de enero de su año: ninguna para 1996, 2019, 2020, 2024, 2025 y 2026; la de 2018, el 4 de julio.

![Las leyes de presupuestos](stills/es/12.png)

### IV. El calendario del BOE

#### 13. El día de la semana de los reales decretos

El día de la semana de las fechas de los reales decretos y decretos-leyes, año a año: viernes de 1986 a 2019, martes desde enero de 2020, miércoles desde noviembre de 2025.

![El día de la semana de los reales decretos](stills/es/13.png)

#### 14. Del día de la norma al BOE

Los días entre la fecha de una norma y su publicación: un real decreto tardaba una mediana de 15 días en 1979–1999 y uno desde 2020.

![Del día de la norma al BOE](stills/es/14.png)

#### 15. La entrada en vigor

Los días entre la publicación y la entrada en vigor: el 63 % de las leyes desde 2020 rige al día siguiente; antes de 1979, el 59 % esperaba los veinte días del Código Civil.

![La entrada en vigor](stills/es/15.png)

#### 16. El calendario

Los días del año en que entraron en vigor los cambios de 2000 a 2025 (el 1 de enero, 9,9 %) y los días de la semana de publicación y de entrada en vigor.

![El calendario](stills/es/16.png)

### V. La Constitución, los códigos y los tribunales

#### 17. La Constitución

Los 169 artículos de la Constitución y sus cuatro reformas (1992, 2011, 2024 y 2026), de un artículo cada una; las leyes orgánicas más modificadas (la del Poder Judicial, 81).

![La Constitución](stills/es/17.png)

#### 18. El Código Civil

Los 2.005 artículos del Código Civil de 1889, coloreados según cuándo se escribió su texto vigente: 1.276 conservan la redacción original.

![El Código Civil](stills/es/18.png)

#### 19. El Código Penal

Las 56 normas que han modificado el Código Penal de 1995 y los artículos que escribió cada una (la Ley Orgánica 1/2015, 276), y los artículos reescritos más veces.

![El Código Penal](stills/es/19.png)

#### 20. Los tribunales en el texto

Las sentencias a las que el BOE atribuye un cambio de texto: 192 del Tribunal Constitucional desde 2008 y 341 sentencias y autos del Supremo; las leyes que más cambiaron.

![Los tribunales en el texto](stills/es/20.png)

## Datos

En el commit `9bf7a4447f` (historial leído en `law-head`, `56dbb7491c`); datos del BOE hasta el 28 de octubre de 2026.

| Datos | Dónde en el repositorio | Registros | Cobertura |
| --- | --- | ---: | --- |
| Normas y sus bloques | `estatal/<rango>/<año>/<id. del BOE>/` | 8.774 normas, 284.435 archivos | las normas de ámbito estatal de la legislación consolidada del BOE; el derecho autonómico está en otros repositorios |
| Situación de cada norma | `data/acts.json`, `normas.tsv` | 8.821 normas | en vigor, derogada, de vigencia agotada, anulada; fechas de disposición, publicación, entrada en vigor y derogación |
| Historial | git log (`In-force:`, `Published:`, `Norma:`), `--name-status` en `law-head` | 16.736 commits, 20.352 cambios de una norma por otra | el historial de cada norma empieza en su primer texto consolidado; las versiones posteriores al 28 de octubre de 2026 no están |
| Normas nombradas | títulos de `normas.tsv`, autores de los commits | 7.669 leyes, leyes orgánicas, decretos-leyes, decretos legislativos y reales decretos nombrados con su fecha | el número más alto de cada año da cuántas leyes, leyes orgánicas y decretos-leyes hubo |
| Notas del BOE | `estatal/real-decreto-ley/<año>/<id. del BOE>/no.md`, `ir.md` (en `law-head`) | 116 reales decretos-leyes de 2017 a 2026 con nota | la convalidación o derogación por el Congreso de los reales decretos-leyes, sistemática desde 2020 |
| Textos leídos | los bloques de la Constitución, el Código Civil y el Código Penal; 45 README; 40 bloques | 3.639 bloques | números de artículo, estructura y artículos vacíos |

## Límites

- **Solo el derecho estatal que el BOE consolida.** No están el derecho autonómico, las normas que el BOE no consolida ni las derogadas antes de que el BOE las consolidara; los recuentos por año son de las normas que contiene el registro.
- **El historial de cada norma empieza en su primer texto consolidado.** En la mayoría es el texto publicado; en algunas antiguas (el Código de Comercio, la Ley de Enjuiciamiento Criminal) es un texto posterior.
- **Los números más altos son mínimos.** Antes de 1983 para las leyes y de 2004 para los decretos-leyes, el registro nombra menos de la mitad de las de cada año y puede no nombrar las últimas (el gráfico 8 dibuja esos años más claros).
- **El voto del Congreso sobre los decretos-leyes** consta de forma sistemática solo desde 2020 (gráfico 10).
- **Las categorías se leen en nombres y títulos.** El rango de la norma que hace un cambio, la materia y el Estado de un acuerdo, las leyes de presupuestos y de acompañamiento siguen las reglas de `src/prep.py`; lo que ninguna regla reconoce cuenta como «otras».
- **Las sentencias** cuentan solo cuando el BOE les atribuye un cambio de texto (gráfico 20).
- **2026 está incompleto** (hasta el 28 de octubre) y se dibuja más claro.

## Reconstrucción

```sh
python visualisations/src/make.py            # historial, árboles, tablas y textos -> src/.build/ -> el-derecho-espanol-en-20-graficos.html
node visualisations/src/stills.cjs           # imágenes de estos README (necesita Playwright; PLAYWRIGHT=<ruta> si no es global)
```

`make.py` lo lee todo de los objetos de git, así que también funciona en un clon sin blobs (`--filter=blob:none`) o con `--no-checkout`, en el que descarga solo las tablas (`normas.tsv`, `corpus.json`, `data/acts.json`, `data/date-corrections.tsv`), las notas de los reales decretos-leyes, los bloques de la Constitución, el Código Civil y el Código Penal, y algunos README y bloques: unos 4.000 archivos pequeños. Lee por defecto `origin/main` (o `HEAD`) y el historial de `origin/law-head`; `--ref` y `--history-ref` eligen otros. No escribe nada en el repositorio salvo la página y la carpeta `src/.build/` (que git ignora).

| Archivo | Qué hace |
| --- | --- |
| `src/make.py` | extrae el historial, los árboles, las tablas y los textos a `src/.build/` y luego ejecuta `prep.py` y `build.py` |
| `src/prep.py` | calcula todas las cifras de los 20 gráficos y el perfil de los datos en `src/.build/data.json` |
| `src/page.tpl.html` | la página: los textos en los dos idiomas, los gráficos (d3) y las tablas |
| `src/build.py` | pone `data.json` en la plantilla y escribe la página |
| `src/stills.cjs` | dibuja cada gráfico como PNG en `stills/es/` y `stills/en/` |

## Fuente y licencia

Basado en datos de la Agencia Estatal Boletín Oficial del Estado (https://www.boe.es): los textos son los textos consolidados del BOE, reutilizados conforme a sus condiciones de reutilización (Resolución de 27 de junio de 2024). Son de carácter meramente informativo; únicamente tienen la consideración de oficiales y auténticos los textos publicados en el «Boletín Oficial del Estado». El código y la documentación son CC0 1.0. Véase [`LICENSE`](../LICENSE).
