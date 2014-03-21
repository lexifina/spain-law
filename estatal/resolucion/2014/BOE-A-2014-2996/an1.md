## ANEXO 1

## Fichero informático de remisión del Padrón Catastral (bienes inmuebles urbanos, rústicos y de características especiales)

Nombre genérico del fichero: PAD-DGC

Tipo de registros: Tamaño fijo.

Longitud de los registros: 1000 caracteres (los caracteres 999 y 1000 se corresponden con retorno de carro/alimentación de línea).

El envío del fichero de intercambio se realizará preferentemente por medios telemáticos a través de la Sede Electrónica del Catastro. Si, excepcionalmente, no se utilizase este sistema, se deberán seguir las instrucciones específicas dictadas para esa ocasión por la Dirección General del Catastro acerca del tipo de soporte y sus características.

Estructura del fichero:

Contendrá los siguientes tipos de registros:

Tipo 01: Registro de cabecera. Existirá uno para todo el fichero independientemente del tamaño del Padrón catastral y de que el fichero recoja la información correspondiente a un solo municipio o a varios.

Tipo 53: Registro de Bien Inmueble/Sujeto pasivo. Existirán tantos como bienes inmuebles urbanos, rústicos o unidades singularizadas dentro de un bien inmueble de características especiales estén incluidas en el Padrón catastral.

Tipo 54: Registro de Titular Catastral. Existirán tantos como titulares de los bienes inmuebles urbanos, rústicos o unidades singularizadas dentro de un bien inmueble de características especiales existan en el Padrón catastral.

Tipo 55: Registro de Bien Inmueble de Características Especiales. Existirá un único registro por Bien Inmueble de Características Especiales presente en cada municipio. Este registro precederá a los registros 53 y 54 de sus unidades singularizadas.

Tipo 90: Registro de cola. Existirá uno para todo el fichero, incluso si este contiene la información de Padrón catastral referente a varios municipios.

El padrón se confecciona con toda la información que, en el momento de su emisión, se conoce sobre la realidad inmobiliaria el uno de enero del correspondiente año. Las situaciones, que referidas a dicha fecha, sean conocidas con posterioridad se comunicarán mediante el formato DOC. El formato DOC no es más que una sucesión de registros de padrón de diferentes años. La Gerencia expresa para unos determinados bienes inmuebles lo que ahora sabe acerca de ejercicios anteriores, y que en su día no supo por diferentes motivos (retrasos en la gestión, resolución de recursos, subsanación de discrepancias, etc.).

El resultado en avance el Procedimiento de Valoración Colectiva será comunicado al ayuntamiento y/o entidades gestoras del IBI empleando la estructura de fichero aquí definida.

Registro de cabecera

| Grupo de Datos | Posición | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de cabecera |
| Tipo de Registro | 1 | 2 | N | Tipo de registro (01). |
|  |
| Identificación de la entidad generadora | 3 | 1 | X | Tipo de entidad generadora (G). |
|  | 4 | 9 | X | Código de la entidad generadora del fichero. |
|  |  |  |  | – Gerencia del Catastro: Código de la Delegación MEH 2 dígitos, siete blancos). |
|  | 13 | 27 | X | Nombre de la Gerencia del Catastro. |
| 37 |
| Datos del fichero | 40 | 8 | N | Fecha de generación del fichero (formato (AAAAMMDD). |
|  | 48 | 6 | N | Hora de generación del fichero (formato HHMMSS). |
|  | 54 | 4 | X | Tipo de fichero (CPAD Padrón, CDOC formato DOC). |
|  | 58 | 39 | X | Descripción del contenido del fichero. |
|  | 97 | 21 | X | Nombre del fichero (cumplimentado por la DGC). |
|  | 118 | 3 | X | Código de la entidad destinataria (cumplimentado por la DGC). |
| 81 |
| Datos específicos del formato | 121 | 4 | N | Ejercicio del padrón IBI. |
|  | 125 | 100 | X | Comentarios. |
| 104 |
| Relleno final | 225 | 776 | X | Relleno con espacios. |
|  | Longitud | 1000 |

Registro de Bien Inmueble/Sujeto pasivo

| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de Bien Inmueble/Sujeto pasivo |
| Tipo de registro | 1 | 2 | N | Tipo de registro (53). |
|  |
| Identificación del bien inmueble | 3 5 | 2 3 | N N | Código de Delegación del MEH. Código del Municipio (según DGC). |
|  | 8 | 2 | X | Clase del Bien inmueble (UR, RU, BI). |
|  |  |  |  | Referencia Catastral: |
|  | 10 | 14 | X | Parcela catastral. |
|  | 24 | 4 | N | Número secuencial del bien inmueble (Número de Cargo) dentro de la referencia catastral. |
|  | 28 | 1 | X | Primer carácter de control. |
|  | 29 | 1 | X | Segundo carácter de control. |
|  | 30 | 8 | N | Número fijo del Bien Inmueble (asignado por la Gerencia del Catastro) |
|  | 38 | 15 | X | Campo para la identificación del Bien Inmueble asignado por el Ayuntamiento. |
| 50 |
| Domicilio Tributario/Localización del bien inmueble | 53 55 80 | 2 25 3 | N X N | Código de Provincia (INE). Nombre Provincia. Código del Municipio (DGC). |
|  | 83 | 3 | N | Código de Municipio (INE). Excluido el último dígito de control. |
|  | 86 | 40 | X | Nombre del Municipio. |
|  | 126 | 30 | X | Nombre de la entidad menor, en caso de existir. |
|  | 156 | 5 | N | Código de vía pública (DGC). |
|  | 161 | 5 | X | Tipo de vía o sigla pública. |
|  | 166 | 25 | X | Nombre de la vía pública. |
|  | 191 | 4 | N | Primer número de policía. |
|  | 195 | 1 | X | Primera letra (carácter de duplicado). |
|  | 196 | 4 | N | Segundo número de policía. |
|  | 200 | 1 | X | Segunda letra (carácter de duplicado). |
|  | 201 | 5 | N | Kilómetro (expresado con tres enteros y dos decimales). |
|  | 206 | 4 | X | Bloque. |
|  | 210 | 2 | X | Escalera. |
|  | 212 | 3 | X | Planta. |
|  | 215 | 3 | X | Puerta. |
|  | 218 | 25 | X | Texto de dirección no estructurada. |
|  | 243 | 5 | N | Código postal. |
|  | 248 | 2 | N | Distrito municipal, en caso de existir. |
|  | 250 | 3 | N | Código del municipio origen en caso de agregación (DGC). |
|  | 253 | 2 | N | Código de la zona de concentración. |
|  | 255 | 3 | N | Código de polígono. |
|  | 258 | 5 | N | Código de parcela. |
|  | 263 | 30 | X | Nombre del paraje. |
| 240 |
| Datos económicos del bien Inmueble | 293 | 4 | N | Ejercicio del padrón catastral. Año al cual se calculan Valor Catastral y Base Liquidable. |
|  | 297 | 12 | N | Valor Catastral expresado en céntimos de euro. |
|  | 309 | 12 | N | Valor catastral del Suelo (urbano y rústico construido) expresado en céntimos de euro. |
|  |  |  |  | En bienes rústicos el valor de los cultivos puede obtenerse como diferencia del valor catastral menos el valor del suelo y el valor de la construcción. |
|  | 321 | 12 | N | Valor catastral de la Construcción expresado en céntimos de euro. |
|  | 333 | 12 | N | Base liquidable expresada en céntimos de euro en el municipio. |
|  | 345 | 1 | X | Clave de grupo de los bienes inmuebles de características especiales, o de uso de los bienes inmuebles, según codificación establecida en los cuadros 1 y 2 que figuran al final de este anexo. |
|  | 346 | 12 | N | Importe del valor catastral afectado por bonificación/exención en caso de bienes rústicos, expresado en céntimos de euro. |
|  | 358 | 1 | X | Clave de la bonificación / exención de bienes rústicos aplicable: A, L, R, J, C, de acuerdo con el cuadro 3. |
|  | 359 | 10 | N | Superficie del elemento o elementos constructivos asociados al cargo, en el caso de procedimientos de valoración de fincas construidas (en metros cuadrados). |
|  | 369 | 10 | N | Superficie del elemento o elementos del suelo asociados al cargo, en el caso de procedimientos de valoración de suelos o parcelas rústicas (en metros cuadrados). |
|  | 379 | 9 | N | Coeficiente de propiedad respecto a la finca, en caso de división horizontal, o cuota del concesionario en el caso de BICE, expresado con tres enteros y seis decimales. |
| 95 |
| Datos para el cálculo de la base liquidable | 388 | 12 | N | Importe, en caso de existir, del Valor Base, expresado en céntimos de euro, en caso de revisiones totales o valoraciones colectivas totales posteriores a 1997. |
|  | 400 | 1 | X | Código de procedencia del Valor Base, en caso de procedimientos de valoración colectiva total posterior a 1997. |
|  |  |  |  | • V: Base Liquidable anterior. |
|  |  |  |  | • M: Aplicación del coeficiente de incremento medio. |
|  |  |  |  | • S: Incorporación de suelo. V.B.= 0. |
|  |  |  |  | • N: Sólo para BICE (BL no aplicable). |
|  |  |  |  | • D: Valor base obtenido tras aplicar coeficientes de decremento. |
|  | 401 | 4 | N | Primer ejercicio de vigencia (IBI) del Valor Catastral o ejercicio del último valor actualizado por coeficientes de decremento. Aplicable en caso de procedimientos de valoración colectiva total posterior a 2002. |
|  | 405 | 12 | N | Valor catastral en el primer ejercicio de su vigencia (IBI), o último valor catastral actualizado por coeficientes de decremento, expresado en céntimos de euro. Aplicable en caso de procedimientos de valoración colectiva total posterior a 2002. |
|  | 417 | 4 | N | Ejercicio de revisión total o valoración colectiva total. |
|  | 421 | 4 | N | Ejercicio de valoración colectiva parcial, o ejercicio de la última aplicación de coeficientes de decremento aplicado. Si no existiera, coincidirá con el de valoración colectiva total. |
|  | 425 | 2 | N | Campo intencionadamente en blanco. |
| 39 |
| Información de la titularidad del bien inmueble | 427 | 2 | X | Código del derecho prevalente para IBI de los titulares: CA: Concesión administrativa. DS: Derecho de superficie. |
|  |  |  |  | US: Usufructo. |
|  |  |  |  | PR: Propiedad. |
|  | 429 | 4 | N | Número de titulares correspondientes al derecho prevalente del bien. |
|  | 433 | 1 | N | Tipo de titulares del derecho prevalente. |
|  |  |  |  | 1: Titular único. |
|  |  |  |  | 2: Matrimonio. |
|  |  |  |  | 3: Comunidad de bienes formalmente constituida. |
|  |  |  |  | 4: Comunidad de bienes no formalmente constituida. |
|  | 434 | 20 | X | Complemento de la información de titularidad. |
| 27 |
| Identificación del sujeto pasivo del IBI | 454 463 | 9 60 | X X | NIF. Primer apellido, segundo apellido, y nombre, o razón social. |
|  | 523 | 8 | N | Clave de identificación interna. |
| 77 |
| Domicilio fiscal del sujeto pasivo del IBI | 531 533 | 2 25 | N X | Código de Provincia (INE). Nombre de Provincia. |
|  | 558 | 3 | N | Código del Municipio (DGC). |
|  | 561 | 3 | N | Código de Municipio (INE). Excluido el último dígito de control. |
|  | 564 | 40 | X | Nombre del Municipio. |
|  | 604 | 30 | X | Nombre de la entidad menor, en caso de existir. |
|  | 634 | 5 | N | Código de vía pública (DGC). |
|  | 639 | 5 | X | Tipo de vía o sigla de vía pública. |
|  | 644 | 25 | X | Nombre de la vía pública. |
|  | 669 | 4 | N | Primer número de la vía. |
|  | 673 | 1 | X | Primera letra (carácter de duplicado). |
|  | 674 | 4 | N | Segundo número en la vía. |
|  | 678 | 1 | X | Segunda letra (carácter de duplicado). |
|  | 679 | 5 | N | Kilómetro (expresado con tres enteros y dos decimales). |
|  | 684 | 4 | X | Bloque. |
|  | 688 | 2 | X | Escalera. |
|  | 690 | 3 | X | Planta. |
|  | 693 | 3 | X | Puerta. |
|  | 696 | 25 | X | Texto de dirección no estructurada. |
|  | 721 | 5 | N | Código Postal. |
|  | 726 | 5 | N | Apartado de Correos. |
| 200 |
| Datos del cónyuge | 731 | 9 | X | NIF del cónyuge en caso de matrimonio. |
|  | 740 | 60 | X | Apellidos y nombre del cónyuge en caso de matrimonio. |
| 69 |
| Información de la alteración | 800 | 4 | X | Clase de alteración comunicada en padrón frente al padrón anterior (ver cuado 4). |
|  | 804 | 4 | X | Tipo de expediente de alteración físico económica. |
|  | 808 | 8 | N | Fecha de la alteración físico económica. |
|  | 816 | 4 | N | Ejercicio del expediente físico económico. |
|  | 820 | 2 | X | Campo intencionadamente en blanco. |
|  | 822 | 8 | X | Referencia del expediente de la DGC origen de la alteración. |
|  | 830 | 3 | N | Código de la entidad de registro del expediente de la DGC origen de la alteración. Código de la forma 9xx donde xx es : |
|  |  |  |  | – El código de la Gerencia en que se registró el expediente. |
|  |  |  |  | – 98 para expedientes registrados en OVC. |
|  | 833 | 4 | N | Ejercicio del expediente origen físico económico en entidad colaboradora caso de existir. |
|  | 837 | 13 | X | Referencia del expediente origen físico económico en entidad colaboradora caso de existir. |
|  | 850 | 3 | N | Código de la entidad colaboradora origen del expediente físico económico según codificación establecida por la DGC. |
| 53 |
| BICE al que pertenece la unidad singularizada | 853 | 20 | X | Referencia catastral del BICE al que pertenece la unidad singularizada. |
| 20 |
| Datos tributarios | 873 | 2 | N | Código de Delegación del MEH del municipio donde tributa el bien inmueble. |
|  | 875 | 3 | N | Código del Municipio (según DGC) donde tributa el bien inmueble. |
|  | 878 | 12 | N | Base imponible expresada en céntimos de euro (coincidente con el valor catastral excepto en el caso de BICE). |
| 5 |
| Relleno final | 890 | 111 | X | Relleno con espacios. |
| 1000 |

Registro de titular catastral

| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de titular catastral |
| Tipo de registro | 1 | 2 | N | Tipo de registro (54). |
|  |
| Identificación del Bien Inmueble | 3 | 2 | N | Código de Delegación del MEH. |
|  | 5 | 3 | N | Código del Municipio (DGC). |
|  | 8 | 2 | X | Clase del Bien inmueble. |
|  |  |  |  | Referencia Catastral. |
|  | 10 | 14 | X | Parcela catastral. |
|  | 24 | 4 | N | Número secuencial del bien inmueble (Número de Cargo) dentro de la parcela catastral. |
|  | 28 | 1 | X | Primer carácter de control. |
|  | 29 | 1 | X | Segundo carácter de control. |
|  | 30 | 8 | N | Número fijo del Bien Inmueble (asignado por la Gerencia del Catastro). |
|  | 38 | 15 | X | Campo para la identificación del Bien Inmueble asignado por el Ayuntamiento. |
| 50 |
| Datos del derecho del titular sobre el Bien | 53 | 2 | X | Código del derecho. PR : Propietario. |
|  |  |  |  | NP : Nuda Propiedad. |
|  |  |  |  | US : Usufructuario. |
|  |  |  |  | CA : Concesión administrativa. |
|  |  |  |  | DS : Derecho de superficie. |
|  | 55 | 5 | N | Porcentaje del titular sobre el bien con un determinado derecho (tres enteros, dos decimales, sin separadores). |
| 7 |
| Identificación del titular catastral | 60 | 9 | X | NIF del titular catastral. |
|  | 69 | 60 | X | Primer apellido, segundo apellido, y nombre, o razón social. |
|  | 129 | 8 | X | Clave de identificación interna. |
| 77 |
| Domicilio fiscal del titular catastral | 137 | 2 | N | Código de Provincia (INE). |
|  | 139 | 25 | X | Nombre de Provincia. |
|  | 164 | 3 | N | Código del Municipio (DGC). |
|  | 167 | 3 | N | Código de Municipio (INE). Excluido el último dígito de control. |
|  | 170 | 40 | X | Nombre del Municipio. |
|  | 210 | 30 | X | Nombre de la entidad menor, en caso de existir. |
|  | 240 | 5 | N | Código de vía pública (DGC). |
|  | 245 | 5 | X | Tipo de vía o sigla de vía pública. |
|  | 250 | 25 | X | Nombre de la vía pública. |
|  | 275 | 4 | N | Primer número de policía. |
|  | 279 | 1 | X | Primera letra (carácter de duplicado). |
|  | 280 | 4 | N | Segundo número de policía. |
|  | 284 | 1 | X | Segunda letra (carácter de duplicado). |
|  | 285 | 5 | N | Kilómetro (expresado con tres enteros y dos decimales). |
|  | 290 | 4 | X | Bloque. |
|  | 294 | 2 | X | Escalera. |
|  | 296 | 3 | X | Planta. |
|  | 299 | 3 | X | Puerta. |
|  | 302 | 25 | X | Texto de dirección no estructurada. |
|  | 327 | 5 | N | Código Postal. |
|  | 332 | 5 | N | Apartado de Correos. |
| 200 |
| Datos de la CB formalmente constituida | 337 | 9 | X | NIF de la Comunidad de Bienes formalmente constituida a la que pertenece el titular catastral en caso de existir. |
|  | 346 | 60 | X | Denominación de la Comunidad de Bienes en caso de existir. |
| 69 |
| Información de la alteración jurídica | 406 410 | 4 8 | X N | Tipo de expediente de alteración jurídica. Fecha de la alteración jurídica. |
|  | 418 | 4 | N | Ejercicio del expediente jurídico. |
|  | 422 | 2 | X | Campo intencionadamente en blanco. |
|  | 424 | 8 | X | Referencia del expediente de la DGC origen de la alteración. |
|  | 432 | 3 | N | Código de la entidad de registro del expediente de la DGC origen de la alteración. Código de la forma 9xx donde xx es: |
|  |  |  |  | – El código de la Gerencia en que se registró el expediente. |
|  |  |  |  | – 98 para expedientes registrados en OVC. |
|  | 435 | 4 | N | Ejercicio del expediente origen jurídico en entidad colaboradora caso de existir. |
|  | 439 | 13 | X | Referencia del expediente origen jurídico en entidad colaboradora caso de existir. |
|  | 452 | 3 | N | Código de la entidad colaboradora origen del expediente jurídico según codificación establecida por la DGC. |
|  | 455 | 4 | N | Ejercicio del padrón catastral. |
| 53 |
| Relleno final | 459 | 542 | X | Relleno con espacios. |
|  | Longitud |  |  | 1000 |

Registro de Bien Inmueble de Características Especiales por Municipio

| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de Bien Inmueble de Características Especiales por Municipio |
| Tipo de registro | 1 | 2 | N | Tipo de registro (55). |
|  |
| Identificación del bien inmueble | 3 8 | 5 2 | X X | Campo intencionadamente en blanco. Clase del Bien inmueble (BI). |
|  |  |  |  | Referencia Catastral: |
|  | 10 | 14 | X | Parcela catastral. |
|  | 24 | 4 | N | Número secuencial del bien inmueble (Número de Cargo) dentro de la referencia catastral. |
|  | 28 | 1 | X | Primer carácter de control. |
|  | 29 | 1 | X | Segundo carácter de control. |
|  |  |
|  | 30 | 23 | X | Campo intencionadamente en blanco. |
| 50 |
| Descripción del Bien Inmueble | 53 203 | 150 90 | X X | Descripción del Bien Inmueble de características Especiales. Campo intencionadamente en blanco. |
| 240 |
| Datos económicos del bien Inmueble | 293 | 4 | N | Ejercicio del padrón catastral. Año al cual se calculan Valor Catastral y Base Liquidable. |
|  | 297 | 12 | N | Valor Catastral del BICE expresado en céntimos de euro. |
|  | 309 | 12 | N | Valor catastral del suelo del BICE expresado en céntimos de euro. |
|  | 321 | 12 | N | Valor catastral de la Construcción del BICE expresado en céntimos de euro. |
|  | 333 | 12 | N | Base liquidable del BICE en el municipio expresada en céntimos de euro. |
|  | 345 | 1 | X | Clave de grupo de los bienes inmuebles de características especiales, según codificación establecida en el cuadro 1 que figuran al final de este documento. |
|  | 346 | 12 | N | Base imponible del BICE en el municipio expresada en céntimos de euro. |
|  | 358 | 30 | X | Campo intencionadamente en blanco. |
| 95 |
|  | 388 | 39 | X | Campo intencionadamente en blanco. |
| 39 |
| Datos tributarios | 427 | 2 | N | Código de Delegación del MEH del municipio donde tributa el bien inmueble. |
|  | 429 | 3 | N | Código del Municipio (según DGC) donde tributa el bien inmueble. |
|  |  |  |  |  |
| Relleno final | 432 | 569 | X | Relleno con espacios. |
| 1000 |

Registro de cola

| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de cola |
| Tipo de registro | 1 | 2 | N | Tipo de registro (90). |
|  |
| Datos de cola | 3 | 7 | N | Número total de registros de tipo igual a 53 (registros de Bien Inmueble/Sujeto pasivo) correspondientes a bienes de clase urbana. |
|  | 10 17 | 7 7 | N N | Número total de registros de tipo igual a 54 (registros de titular catastral) correspondientes a bienes de clase urbana. Número total de registros de tipo igual a 53 (registros de Bien Inmueble/Sujeto pasivo) correspondientes a bienes de clase rústica. |
|  | 24 31 | 7 7 | N N | Número total de registros de tipo igual a 54 (Registros de titular catastral) correspondientes a bienes de clase rústica Número total de registros de tipo igual a 53 (registros de Bien Inmueble/Sujeto pasivo) correspondientes a bienes de características especiales. |
|  | 38 45 | 7 14 | N N | Número total de registros de tipo igual a 54 (registros de titular catastral) correspondientes a bienes de características especiales. Valor catastral total de los bienes de clase urbana, como suma de los valores catastrales contenidos en los registros de Bien Inmueble de clase urbana. |
|  | 59 | 14 | N | Valor catastral total del suelo de los bienes de clase urbana, como suma de los valores catastrales del suelo contenidos en los registros de Bien Inmueble de clase urbana. |
|  | 73 | 14 | N | Valor catastral total de la construcción de los bienes de clase urbana, como suma de los valores catastrales de construcción contenidos en los registros de Bien Inmueble de clase urbana. |
|  | 87 | 14 | N | Base Liquidable total de los bienes de clase urbana, como suma de las bases liquidables contenidas en los registros de Bien Inmueble de clase urbana. |
|  | 101 | 14 | N | Valor catastral total de los bienes de clase rústica, como suma de los valores catastrales contenidos en los registros de Bien Inmueble de clase rústica. |
|  | 115 | 14 | N | Valor catastral total del suelo de los bienes de clase rústica, como suma de los valores catastrales del suelo contenidos en los registros de Bien Inmueble de clase rústica. |
|  | 129 | 14 | N | Valor catastral total de la construcción de los bienes de clase rústica, como suma de los valores catastrales de construcción contenidos en los registros de Bien Inmueble de clase rústica. |
|  | 143 | 14 | N | Base Liquidable total de los bienes de clase rústica, como suma de las bases liquidables contenidas en los registros de Bien Inmueble de clase rústica. |
|  | 157 | 14 | N | Valor catastral total de los bienes de características especiales, como suma de los valores catastrales contenidos en los registros de Bien Inmueble de características especiales. |
|  | 171 | 14 | N | Valor catastral total del suelo de los bienes de características especiales, como suma de los valores catastrales del suelo contenidos en los registros de Bien Inmueble de características especiales. |
|  | 185 | 14 | N | Valor catastral total de la construcción de los bienes de características especiales, como suma de los valores catastrales de construcción contenidos en los registros de Bien Inmueble de características especiales. |
|  | 199 | 14 | N | Base Liquidable total de los bienes de características especiales, como suma de las bases liquidables contenidas en los registros de Bien Inmueble de características especiales. |
|  | 213 | 7 | N | Número total de registros de tipo igual a 55 (registros de BICE) correspondientes a bienes de características especiales. |
| 217 |
| Relleno final | 220 | 781 | X | Relleno con espacios. |
|  | Longitud |  | 1000 |

CUADRO 1. GRUPOS DE LOS BIENES INMUEBLES DE CARACTERÍSTICAS ESPECIALES

| Código | Grupo según artículo 2.7 Ley del catastro inmobiliario |
| --- | --- |
| 1 | a) Inmuebles destinados a la producción de energía eléctrica y gas, al refino de petróleo y centrales nucleares. |
| 2 | b) Presas, saltos de agua y embalses. |
| 3 | c) Autopistas, carreteras y túneles de peaje. |
| 4 | d) Aeropuertos y puertos comerciales. |

CUADRO 2. CODIFICACIÓN DE LOS USOS DE LOS BIENES INMUEBLES

| Código | Uso |
| --- | --- |
| A | Almacén -Estacionamiento |
| V | Residencial |
| I | Industrial |
| O | Oficinas |
| C | Comercial |
| K | Deportivo |
| T | Espectáculos |
| G | Ocio y Hostelería |
| Y | Sanidad y Beneficencia |
| E | Cultural |
| R | Religioso |
| M | Obras de urbanización y jardinería, suelos sin edificar |
| P | Edificio singular |
| B | Almacén agrario |
| J | Industrial agrario |
| Z | Agrario |

CUADRO 3. CLAVE DE LOS BENEFICIOS FISCALES APLICABLES

| Estado, CC.AA, Municipios, Iglesia, Asociaciones confesionales, Cruz Roja, Gobiernos extranjeros, Convenios internacionales. | TRLRHL Art. 62.1, apartados a, b, c, d, e, | A |
| --- | --- | --- |
| Centros docentes concertados. | TRLRHL Art. 62.2, apartado a |  |
| Fundaciones. | Ley 30/1994 |  |
| Montes Vecinales en Mano común y montes comunales. | TRLRHL Art. 62.1 apartado b |  |
| Montes poblados con especies de crecimiento lento (madera y corcho). | TRLRHL Art. 62.1 apartado f | L |
|  | Ley 19/1995 |  |
|  | RD 378/93. RD 152/96 |  |
| Repoblaciones forestales y tramos en regeneración de masas arboladas… | TRLRHL Art. 62.2, apartado c | R |
| Monumentos y jardines históricos. | TRLRHL Art. 62.2, apartado b | J |
| Cooperativas Agrarias Protegidas (bonificación del 95%). | Ley 20/1990 | C |

CUADRO 4. CLASE DE ALTERACIÓN COMUNICADA FRENTE AL PADRÓN ANTERIOR

| CONT | Información continuista con respecto al padrón anterior (posible incremento por Ley de Presupuestos). |
| --- | --- |
| EV01 | Modificación de la información físico económica (nuevo valor), sin cambio de titularidad. |
| EV03 | Modificación de la información físico económica (nuevo valor) y de titularidad. |
| EN01 | Cambio de titularidad, sin alteración de valor. |

HISTÓRICO DE REVISIONES

• 11-12-2013

Se adapta la explicación del cálculo de la Base liquidable a lo dispuesto en el artículo 68.4 del TRLRHL. En el caso de decremento de valores al aplicar coeficientes, se fijan nuevas formas de calcular el valor base, el componente individual de la reducción, y su distribución a lo largo de los años que resten.

Los elementos de cálculo en el caso del formato DOC serán los correspondientes para cada ejercicio reflejado.

• 20-03-2011

Expresión de las componentes del cálculo de las unidades singularizadas BICE.

Los últimos 1.000 caracteres de cada registro son retorno de carro y alimentación de línea (OD, OA en hexadecimal) facilitándose su visualización.

• 11-06-2008

Se aclara que el registro 55 (BICE) precederá a los registros 53 y 54 de sus respectivas unidades singularizadas.

• 04-03-2008

Se aclara que la Bl de la unidad singularizada BICE es en el municipio concreto. El valor catastral de la unidad singularizada se reparte entre municipios, dando lugar a bases imponibles que llevan aparejada su correspondiente base liquidable.

| 333 | 12 | N | Base liquidable expresada en céntimos de euro en el municipio. |
| --- | --- | --- | --- |

• 15-02-2008

Se matiza de nuevo el origen del valor base. EN BICE el valor base va ligado al valor catastral, y no a la base.

| 400 | 1 | X | Código de procedencia del Valor Base: |
| --- | --- | --- | --- |
|  |  |  | V: Doble del Valor Catastral anterior. |
|  |  |  | M: 80% del nuevo valor catastral. |

• 13-02-2008

Se corrige la definición del campo relativo al origen del valor base dentro del registro 55

| 400 | 1 | X | Código de procedencia del Valor Base: |
| --- | --- | --- | --- |
|  |  |  | V: Doble de la Base Liquidable anterior. |
|  |  |  | M: 80% del nuevo valor catastral. |

Se corrige la errata en cuanto a contenido del campo Descripción del Bien Inmueble poniendo su campo como alfanumérico e incidiendo en que se incluye un literal con su descripción

| 53 | 150 | X | Descripción literal del Bien Inmueble de características Especiales. |
| --- | --- | --- | --- |

• 17-12-2007

Se expresa explícitamente la base imponible de una unidad singularizada en el municipio correspondiente.

| 878 | 12 | N | Base imponible expresada en céntimos de euro (coincidente con el valor catastral excepto en el caso de BICE). |
| --- | --- | --- | --- |

• 1-11-2007 (formato 2008)

Modificaciones al formato padrón para incluir la información de BICE:

– Se crea el tipo de registro 55. Existirán tanto como BICE y municipios implicados.

– Se añade al tipo de registro 53 la ligazón con el tipo de registro 55. Se distingue para BICE entre municipio donde se tributa, y municipio donde radica la unidad singularizada.

– Se añade el contador de registros 55 en el registro de cola.

• 27-12-2006

Se especifica el significado del campo «Valor catastral del Suelo», explicitando que no lleva incluida la componente de valor achacable a los cultivos agrarios. El valor de suelo y valor de la construcción, serán las componentes del valor sujetas a reducción en bienes rústicos sujetos a procedimiento de valoración colectiva posteriores a 2006.

| 309 | 12 | N | Valor catastral del Suelo (urbano y rústico construido) expresado en céntimos de euro. En bienes rústicos el valor de los cultivos puede obtenerse como diferencia del valor catastral menos el valor del suelo y el valor de la construcción. |
| --- | --- | --- | --- |

• 29-10-2006

OVC es capaz de dar números de registro válidos en Catastro. Este número se emplea por la Gerencia sin necesidad de reasignar otro número a su llegada, de tal forma que cualquier ciudadano pueda preguntar (Línea Directa, presencialmente) por dicho número. Este número se empleará también por los agentes externos en sus intercambios (de entrada, o de salida) con Catastro.

Para ello, ha sido necesario modificar los formatos de intercambio para representar la entidad de registro del expediente en la DGC. Hasta ahora se empleaba el código 999 para representar dicha entidad, sin diferenciar, ahora se pasa a emplear 9xx (donde xx es el código de la Gerencia) o 998 para OVC.

Se ha modificado:

Registro 53 de sujeto pasivo:

| 820 | 2 | X | Campo intencionadamente en blanco. |
| --- | --- | --- | --- |
| 822 | 8 | X | Referencia del expediente de la DGC origen de la alteración. |
| 830 | 3 | N | Código de la entidad de registro del expediente de la DGC origen de la alteración. Código de la forma 9xx donde xx es: |
|  |  |  | – El código de la Gerencia que se registró el l expediente. |
|  |  |  | – 98 para expedientes registrados en OVC. |

Registro 54 de titular catastral:

| 422 | 2 | X | Campo intencionadamente en blanco. |
| --- | --- | --- | --- |
| 424 | 8 | X | Referencia del expediente de la DGC origen de la alteración. |
| 432 | 3 | N | Código de la entidad de registro del expediente de la DGC origen de la alteración. Código de la forma 9xx donde xx es: |
|  |  |  | – El código de la Gerencia que se registró el l expediente. |
|  |  |  | – 98 para expedientes registrados en OVC. |
