## ANEXO 2

## Fichero informático de captura de las bonificaciones a aplicar en el IBI el ejercicio de efectos de los Procedimientos de Valoración Colectiva.

Nombre genérico del fichero: BONIFVALCO-DGC

(Revisión 25-06-2009. Histórico de cambios al final del documento).

Tipo de registros: Tamaño fijo.

Longitud de los registros: 120 caracteres.

El envío del fichero de intercambio se realizará preferentemente por medios telemáticos a través de la Sede Electrónica del Catastro. Si, excepcionalmente, no se utilizase este sistema, se deberán seguir las instrucciones específicas dictadas para esa ocasión por la Dirección General del Catastro acerca del tipo de soporte y sus características.

Estructura del fichero:

Contendrá los siguientes tipos de registros:

Tipo 01: Registro de cabecera. Existirá uno para todo el fichero independientemente del tamaño y de que el fichero recoja la información correspondiente a un solo municipio o varios.

Tipo 56: Registro de bonificación. Existirán tantos como bienes inmuebles urbanos estén incluidos en el procedimiento de Valoración Colectiva.

Tipo 90: Registro de cola. Existirá uno para todo el fichero, incluso si este contiene la información de bonificaciones referente a varios municipios.

Detalle de la estructura:

| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de cabecera |
| Tipo de Registro | 1 | 2 | N | Tipo de registro (01). |
|  |
| Identificación de la entidad generadora | 3 | 1 | X | Tipo de entidad generadora (A ayuntamientos, C entidades con convenio). |
|  | 4 | 3 | N | Código de la Gerencia de la DGC. |
|  | 7 | 3 | N | Código de la entidad generadora asignado por la Gerencia de la DGC. |
|  | 10 | 30 | X | Nombre de la entidad generadora. |
| 37 |
| Datos del fichero | 40 | 8 | N | Fecha de generación del fichero (formato (AAAAMMDD). |
|  | 48 | 6 | N | Hora de generación del fichero (formato HHMMSS). |
|  | 54 | 4 | X | Tipo de fichero (UBOV). |
|  | 58 | 39 | X | Descripción del contenido del fichero. |
|  | 97 | 12 | X | Identificador del envío (siempre se cumplimentará en la DGC). |
|  | 109 | 4 | N | Ejercicio de referencia de los datos (ejercicio de efectos de la revisión). |
| 73 |
|  | 113 | 8 | X | Relleno con espacios |
|  | Longitud |  |  | 120 |
| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de datos de bonificación |
| Tipo de Registro | 1 | 2 | N | Tipo de registro (56). |
|  |
| Identificación del inmueble | 3 | 2 | N | Código de Delegación del MEH. |
|  | 5 | 3 | N | Código del Municipio (según DGC). |
|  |  |  |  | Referencia Catastral. |
|  | 8 | 7 | X | Primera parte: identificación por coordenadas UTM de la manzana, y número secuencial de parcela. |
|  | 15 | 7 | X | Segunda parte: posición de la manzana en la Hoja del Plano Parcelario en la que se ubica el centroide de la manzana. |
|  | 22 | 4 | N | Número secuencial del bien inmueble fiscal (Número de Cargo) dentro de la parcela catastral. |
|  | 26 | 1 | X | Primer carácter de control. |
|  | 27 | 1 | X | Segundo carácter de control. |
|  | 28 | 8 | X | Campo Intencionadamente en blanco. |
| 33 |
| Datos de la bonificación/exención (1/2) | 36 | 12 | N | Importe de la bonificación/exención expresado en céntimos de euro. |
|  | 48 | 7 | N | Tipo impositivo aplicado al bien inmueble expresado con 3 enteros y 4 decimales. |
|  | 55 | 12 | N | Cuota liquida del Impuesto de Bienes Inmuebles, expresada en céntimos de euro. |
| 31 |
|  | 67 | 11 | X | Campo Intencionadamente en Blanco. |
| 11 |
| Datos de la bonificación/exención (2/2) | 78 | 5 | N | Porcentaje límite de incremento recogido en el artículo 74.2 del TRLRHL, expresado con tres enteros y dos decimales. |
| 5 |
| Relleno final | 83 | 38 | X | Relleno con espacios. |
|  | Longitud | 120 |
| Grupo de Datos | Posición inicial | Longitud | Formato | Descripción |
| --- | --- | --- | --- | --- |
| Registro de cola |
| Tipo de Registro | 1 | 2 | N | Tipo de registro (90). |
|  |
| Datos de cola | 3 | 7 | N | Número total de registros de tipo igual a 56 (registros de datos de bonificación). |
|  | 10 | 15 | N | Valor total de las bonificaciones, como suma de las bonificaciones contenidas en los registros de tipo 56. |
|  | 25 | 96 | X | Relleno a espacios. |
|  | Longitud |  |  | 120 |

HISTÓRICO DE REVISIONES

• 25-06-2009

Se corrigen erratas en el formato y se aclara el significado de ciertos campos.

Cabecera.

| Identificación de la entidad generadora | 3 | 1 | X | Tipo de entidad generadora (A ayuntamientos, C entidades con convenio). |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  | 54 | 4 | X | Tipo de fichero (UBOV). |
|  | 58 | 39 | X | Descripción del contenido del fichero. |

Tipo de Registro 56

|  | 28 | 8 | X | Campo Intencionadamente en blanco. |
| --- | --- | --- | --- | --- |

• 29-09-2008

Se corrige errata en el número de posiciones en blanco en el tipo de registro 56.

• 15-07-2008

Se incluye el porcentaje límite de incremento recogido en el artículo 74.2 del TRLRHL. Esta valor, dada su variabilidad, debe ser consignado a nivel de bien inmueble.

Se elimina la obligación de consignar el número fijo.
