## ANEXO

## Formato de suministro de información a la Dirección General del Catastro de las alteraciones catastrales relativas a los documentos autorizados o inscritos por Notarios y Registradores de la Propiedad

## 1. Estructura del formato de suministro de información

El fichero se remitirá en disquetes de 3 1/2’’, sin perjuicio de la posibilidad de su transmisión a través de otros medios electrónicos, informáticos o telemáticos que determinen conjuntamente la Dirección General del Catastro y la Dirección de los Registros y del Notariado.

El fichero estará codificado en ASCII.

La longitud de cada registro será de 491 caracteres.

Al final de cada registro figurará un retorno de carro CR como separador de registro. Este carácter no está contabilizado en la longitud del registro, ni figura en la descripción del mismo.

El fichero estará compuesto por dos tipos de registro: De cabecera o identificador del fichero, y de detalle o movimiento:

a) Datos del registro de identificación del fichero:

Cada fichero, conjunto de registros, se identifica con un registro de cabecera, denominado de identificación del fichero, en donde se especifica la procedencia, fecha de generación y período al que corresponden los movimientos que contiene. Incluye los campos que se describen, especificando su significado, su longitud en caracteres y el tipo de datos a que corresponde.

Este registro es obligatorio y debe ser el primer registro del fichero, debiendo contener 01 en el campo «Tipo de registro» (posiciones 1 y 2 del registro).

La longitud del registro será de 491 posiciones, al igual que los registros de detalle.

b) Datos del registro de movimientos:

Estos registros deben contener 02 en el campo «Tipo de registro» (posiciones 1 y 2 del registro).

Al introducir la información correspondiente a una escritura o inscripción registral se incluirá un registro para cada inmueble que figure en la misma, indicando como transmitente, en caso de haber más de uno, el que figure como titular catastral.

Cada movimiento, uno para cada inmueble, se describe con cuatro bloques de información y se corresponde con un solo registro del fichero. Estos bloques son:

1. Bloque de identificación del movimiento.

2. Bloque de identificación del bien inmueble.

3. Bloque de identificación del transmitente.

4. Bloque de identificación del nuevo titular.

1. El bloque de identificación del movimiento tipifica e identifica el movimiento que se ha de efectuar. En el mismo deben incluirse los datos básicos mínimos de la alteración catastral de que es objeto el bien inmueble. Además, aporta información sobre si se ha presentado o no la referencia catastral exigida en la normativa vigente (artículos 50 y 55 de la Ley 13/1996), así como al tipo de referencia catastral que se aporta, de acuerdo con los criterios establecidos en los artículos 51 y 53 de la Ley 13/1996, indicando si se incorpora o no a la escritura o inscripción.

2. El bloque de identificación del bien inmueble aporta, además de la referencia catastral, otros datos que en caso de duda puedan colaborar a la identificación del bien en cuestión, así como facilitar la posterior coordinación entre el Catastro y el Registro de la Propiedad.

3. El bloque de identificación del transmitente debe contener los datos de quien transmite el bien o derecho objeto de la alteración catastral. En caso de que existan más de uno se reseñará preferentemente al que figure como titular catastral, proporcionando información sobre el número total de cotitulares, incluyendo al que figura identificado, sin aportar la identificación del resto.

4. El bloque de identificación del nuevo titular debe contener los datos de la persona que deba aparecer como nuevo titular catastral, de acuerdo con lo establecido en el artículo 65 de la Ley 39/1988, de 28 de diciembre, reguladora de las Haciendas Locales. Asimismo, si existe más de un titular, deben incluirse la identificación de uno de ellos, preferentemente aquel que tenga mayor coeficiente en la propiedad del bien, que será el que figurará como titular catastral, indicando el número total de cotitulares, incluyendo al que figura identificado, sin aportar la identificación del resto.

## 2. Descripción de los registros del fichero

Registro de identificación del fichero

| Grupo de datos | Posición inicial | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- |
| Tipo de Registro. | 1 | 2 | N | Tipo de registro (01). |
| Identificación del fichero. | 3 | 5 | N | Código de Registro de la Propiedad origen de la información (código provincia 2 dígitos, código registro 3 dígitos). |
| 8 | 9 | N | Código de Notaría origen de la información (código provincia 2 dígitos, código poblacion 4 dígitos, código Notaría 3 dígitos). |
| 17 |  |  | Fecha de generación. |
| 17 | 2 | N | Día. |
| 19 | 2 | N | Mes. |
| 21 | 4 | N | Año. |
|  |  |  | Fecha de inicio del período. |
| 25 | 2 | N | Día. |
| 27 | 2 | N | Mes. |
| 29 | 4 | N | Año. |
|  |  |  | Fecha de fin de período. |
| 33 | 2 | N | Día. |
| 35 | 2 | N | Mes. |
| 37 | 4 | N | Año. |
| 41 | 450 | X | Relleno. |
| Total | 491 |  |  |  |

Registro de datos de movimientos

| Grupo de datos | Posición inicial | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- |
| Tipo de Registro. | 1 | 2 | N | Tipo de registro (02). |
| Identificación del movimiento. |  |  |  | Fecha de escritura o documento. |
| 3 | 2 | N | Día. |
| 5 | 2 | N | Mes. |
| 7 | 4 | N | Año. |
| 11 | 1 | N | Clase de alteración catastral. |
|  |  |  | Se clasifica de acuerdo con las siguientes codificaciones: |
|  |  |  | 1 = Cambio de dominio simple (sin alteración del bien). |
|  |  |  | 2 = Obra nueva en construcción. |
|  |  |  | 3 = Obra nueva terminada. |
|  |  |  | 4 = Otras alteraciones catastrales. |
|  |  |  | 5 = Actos de naturaleza urbanística. |
| 12 | 1 | N | Cumplimiento artículo 50 de la Ley 13/1996. Se indicará si se ha cumplido el artículo con la siguiente codificación: |
|  |  |  | 1 = RC de la finca incorporada. |
|  |  |  | 2 = RC de la finca incorporada y dudosa. |
|  |  |  | 3 = RC incorporada de la finca de origen (artículo 51.5). |
|  |  |  | 4 = RC presentada no incorporada. |
|  |  |  | 5 = No se ha presentado RC. |
| Identificación del bien inmueble. | 13 | 20 | X | Referencia catastral. |
| 33 | 14 | N | Número de finca registral (sección 2 dígitos, número finca 6 dígitos, subfinca 6 dígitos). Se cumplimenta si la información procede de un Registro. |
| 47 | 8 | N | Número de protocolo (año 4 dígitos, protocolo 4 dígitos). Se cumplimenta si la información procede de una Notaría. |
| 55 | 12 | N | Precio o valor declarado de transmisión. |
| 67 |  |  | Domicilio tributario. |
| 67 | 2 | N | Código de provincia (INE). |
| 69 | 3 | N | Código de municipio (INE). |
| 72 | 25 | X | Nombre del municipio. |
| 97 | 15 | X | Nombre de la entidad menor. |
| 112 | 5 | X | Tipo de vía (sigla). |
| 117 | 25 | X | Nombre de la vía. |
| 142 | 4 | N | Número de la vía. |
| 146 | 1 | X | Duplicado. |
| 147 | 4 | X | Bloque. |
| 151 | 2 | X | Escalera. |
| 153 | 2 | N | Planta. |
| 155 | 3 | X | Puerta. |
| 158 | 25 | X | Resto dirección no estructurada. |
| 183 | 6 | N | Aproximación postal en kilómetro. |
| 189 | 5 | N | Distrito postal. |
| Identificación del transmitente. | 194 | 4 | N | Número de cotitulares, en el caso de que exista más de uno se indicará el número total, incluyendo al que figura identificado. |
| 198 | 9 | X | NIF (en caso de cotitularidad, indicar preferentemente el del titular catastral). |
| 207 | 62 | X | Apellidos y nombre o razón social. |
| Identificación del nuevo titular. | 269 | 4 | X | Número de cotitulares, en el caso de que exista más de uno se indicará el número total, incluyendo al que figura identificado. |
| 273 | 20 | X | Descripción de la cotitularidad, aclarando lo que motiva la comunidad de bienes (herederos de XXXXXX, y hermanos, y cónyuge, sociedad de gananciales,...). |
| 293 | 9 | X | NIF del titular catastral (artículo 65 de la Ley reguladora de las Haciendas Locales). En caso de cotitularidad, indicar el del cotitular principal o el del que se desea figure como titular catastral. |
| 302 | 62 | X | Apellidos y nombre o razón social del titular catastral (artículo 65 de la Ley reguladora de las Haciendas Locales). |
| 364 |  |  | Domicilio. |
| 364 | 2 | N | Código de provincias (INE). |
| 366 | 3 | N | Código de municipio (INE). |
| 369 | 40 | X | Nombre de municipio. |
| 409 | 5 | X | Tipo de vía (sigla). |
| 414 | 25 | X | Nombre de la vía. |
| 439 | 4 | N | Número de la vía. |
| 443 | 1 | X | Duplicado. |
| 444 | 4 | X | Bloque. |
| 448 | 2 | X | Escalera. |
| 450 | 2 | N | Planta. |
| 452 | 3 | X | Puerta. |
| 455 | 25 | X | Resto dirección no estructurada. |
| 480 | 6 | N | Aproximación postal en kilómetro. |
| 486 | 5 | N | Distrito postal. |
| Total | 491 |  |  |  |
