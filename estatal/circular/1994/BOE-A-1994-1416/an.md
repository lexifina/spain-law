## ANEXO

## Normas técnicas de elaboración de los ficheros informáticos

1. Tipos de ficheros.–Los ficheros contendrán registros de longitud fija, admitiéndose dos soportes distintos de presentación: Cinta magnética y disquete.

Las características técnicas de los mismos serán las siguientes:

1.1 Soporte: Cinta magnética. Código de grabación: EBCDIC. Densidad de grabación: 1.600 ó 6.250 bpi. Número de pistas: Nueve. Etiquetas internas: Sin etiquetas internas con marca de final de cinta.

1.2 Soporte: Disquete. Código: ASCIL. Tipo texto, separándose los registros con los caracteres CR/LF (en hexadecimal ASCII «0D0A»), y siendo la marca fin de fichero EOF (en hexadecimal ASCII «1A»). Tamaño de disquetes: 5.1/4’’ ó 3,5’’. Capacidad: 1,2 MB para 5 1/4’’ y 1,44 MB para 3,5’’. Sin etiqueta de volumen. Sin subdirectorios.

2. Nombres de los ficheros.–Los nombres externos de los diferentes ficheros serán los siguientes:

Ordenes: Fichero de órdenes.

Ejecuci: Ficheros de ejecuciones.

Desglos: Fichero de desgloses.

3. Diseño de registros e instrucciones generales.–3.1 Los ficheros contendrán un primer registro de cabecera con los datos siguientes:

Nombre externo del fichero: (7 primeras posiciones).

Fecha de generación: Formato AAAAMMDD (posiciones 8 a 15).

Identificación de la entidad que envía el fichero: (posiciones 16 a 95).

Resto: Se completará con blancos (posiciones 96 a final de registro) y un registro de cola que contendrá el número de registros que le preceden en el fichero completado hasta el final con blancos.

3.2 Si un campo sólo puede tomar valores en un rango discreto o debe tener un formato determinado, el rango o el formato viene indicado en la columna de observaciones.

3.3 Los campos alfanuméricos sin información se rellenarán con blancos y los numéricos con ceros.

3.4 A los efectos de su inclusión en el fichero de órdenes, se entenderá que cada orden se refiere a una única operación y a un único valor, con indepedencia de que el ordenante haya ordenado varias operaciones en el mismo acto. A cada operación sobre cada valor se le deberá asignar un código de orden distinto.

3.5 A los efectos de su inclusión en el fichero de órdenes, la modificación de una orden anterior se considerará como dos nuevas órdenes, una de anulación de la primera y otra con la información de la orden resultante después de la modificación.

3.6 La información sobre las órdenes que las entidades reciban sobre traspasos de valores representados en anotaciones en cuenta o título y las actuaciones posteriores de las entidades sobre dichas órdenes se incluirán únicamente en el fichero de órdenes de la siguiente forma:

Las entidades que reciban la orden de sus clientes la incluirán en su fichero de órdenes el día de recepción de la misma con estado de la orden como pendiente de ejecución hasta la fecha en la que comunique, cuando así esté obligada, el traspaso al Servicio de Compensación y Liquidación de Valores para valores incorporados al mismo, o a la otra Entidad para el resto de valores. El estado de la orden ese día será el de ejecutada.

Las entidades que participen de forma pasiva en el traspaso deberán incluir la orden en la fecha en que reciban la comunicación del Servicio de Compensación y Liquidación de Valores, o de la otra entidad a que se refiere el párrafo anterior, según los valores estén incorporados o no a dicho Servicio. El estado de la orden será el de pendiente de ejecución hasta la fecha efectiva del traspaso, que será el último día en que la orden figure en su fichero y el estado de la orden ese día de referencia será el de ejecutada.

3.7 En el caso de que un desglose haga referencia a más de una ejecución existirán, al menos, tantos registros en el fichero de desgloses como ejecuciones a que haga referencia el mismo, incluyendo en cada uno el código de ejecución correspondiente y repitiendo el resto de los datos.

3.8 Por otra parte, si una ejecución incluida en el fichero de desgloses engloba a más de una orden, o parte de una orden, por cada una de ellas se generará un registro en el fichero de desgloses con el código de orden correspondiente y repitiendo el resto de los datos.

3.9 En consecuencia, en el fichero de desgloses existirá un registro por cada pareja orden-ejecución diferente a que hagan referencia los desgloses incluidos en el mismo, indicando en cada uno de ellos el código de operación desglosada, el código de ejecución y el código de orden correspondientes.

Fichero de órdenes: ÓRDENES.

| Número | Posición | Nombre del campo | Formato | Longitud | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-8 | Fecha de referencia | N | 8 | Formato: AAAAMMDD Contendrá la fecha en la que la orden ha estado vigente (un registro por cada día de vigencia de la orden). |
| 2 | 9-24 | Código de orden | X | 16 | Identificador único y absoluto para cada orden. |
| 3 | 25-32 | Fecha de recepción | N | 8 | Formato: AAAAMMDD |
| 4 | 33-38 | Hora de recepción | N | 6 | Formato: HHMMSS |
| 5 | 39-48 | N.I.F. Ordenante | X | 10 |  |
| 6 | 49-88 | Ordenante | X | 40 | Se identificará al ordenante por su denominación. |
| 7 | 89-90 | Tipo de operación ordenada | X | 2 | Se identificará mediante las siguientes claves: CO: Compra. VE: Venta. SP: Suscripción en mercado primario. CV: Conversión. TI: Inicio de traspaso. TC: Compleción de traspaso. AC: Anulación de una orden anterior. OT: Otra. |
| 8 | 91-92 | Operación de deuda anotada | N | 2 | Se identificará mediante las siguientes claves: 01: Operación a vencimiento. 02: Operación de compra o venta con compromiso de reventa o recompra a fecha fija. 03: Operación de compra o venta con compromiso de reventa o recompra a la vista. 04: Operación simultánea. |
| 9 | 93-101 | Número de valores | N | 9 |  |
| 10 | 102-113 | Código de identificación de valor | X | 12 | Se usará el código ISIN para aquellos valores que lo posean o el código que otorgue el correspondiente mercado cuando no exista el código ISIN. Se completará con blancos si no se dispone de código. |
| 11 | 114-153 | Denominación del valor | X | 40 | Se identificará el valor por su denominación. |
| 12 | 154-155 | Estado de la orden | X | 2 | Se identificará mediante las siguientes claves: EE: Ejecutada. Orden cuya ejecución haya sido realizada por la entidad en la fecha de referencia (campo 1). PJ: Parcialmente ejecutada. Orden ejecutada parcialmente por la entidad y que podrá generar nuevas ejecuciones. PE: Pendiente de ejecución. Orden recibida por la entidad cuya validez permanezca al final del día de referencia y que deberá ser ejecutada por la propia entidad. TT: Transmitida. Orden recibida por la entidad y que haya sido transmitida en el día de referencia a otra entidad para su ejecución. PT: Pendiente de transmisión. Orden recibida por la entidad cuya validez permanezca al final del día de referencia y para cuya ejecución tenga que ser transmitida a otra entidad. |
| 13 | 156-163 | Plazo de validez de la orden | N | 8 | Formato: AAAAMMDD |
| 14 | 164-167 | Código de entidad de destino | N | 4 | Se indicará el código de la entidad de acuerdo con los siguientes criterios: - Número de registro en el Banco de España.-Para Bancos y Entidades de Crédito. - Número de registro en la Comisión Nacional del Mercado de Valores + 3.500.-Para Sociedades y Agencias de Valores. - No se completará para entidades no inscritas en los registros oficiales del Banco de España y la Comisión Nacional del Mercado de Valores. |
| 15 | 168-207 | Entidad de destino | X | 40 | Se identificará a la entidad de destino por su denominación. |
| 16 | 208-211 | Código de entidad origen del traspaso | N | 4 | Se indicará el código de la entidad de acuerdo con el criterio establecido para el campo número 14. |
| 17 | 212-251 | Entidad origen del traspaso | X | 40 | Se identificará a la entidad origen del traspaso por su denominación. |
| 18 | 252-255 | Código de entidad receptora del traspaso | N | 4 | Se indicará el código de la entidad de acuerdo con el criterio establecido para el campo número 14. |
| 19 | 256-295 | Entidad receptora del traspaso | X | 40 | Se identificará a la entidad receptora del traspaso por su denominación. |
| 20 | 296-311 | Código de la orden anulada | X | 16 | Solo se completará en anulaciones de órdenes y contendrá el código identificador de la orden a la que anula. |
| 21 | 312-361 | Comentarios | X | 50 | Aclaración a los campos anteriores siempre que resulte necesario. Se indicará además en este apartado la referencia al contrato o al mandato genérico o específico recibido por la entidad cuando la operación sea transmitida a otra entidad para su ejecución. |
| 22 | 362-363 | Final de registro | X | 2 | Siempre: |

Fichero de ejecuciones: EJECUCI.

| Número | Posición | Nombre del campo | Formato | Longitud | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-8 | Fecha de contratación | N | 8 | Formato: AAAAMMDD |
| 2 | 9-14 | Hora de contratación | N | 6 | Formato. HHMMSS |
| 3 | 15-30 | Código de ejecución | X | 16 | Identificador único y absoluto para cada ejecución. |
| 4 | 31-32 | Mercado | X | 2 | Se identificará mediante las siguientes claves: 03: Bolsa de Valores de Valencia. 04: Bolsa de Valores de Barcelona. 05: Bolsa de Valores de Bilbao. 06: Bolsa de Valores de Madrid. 07: MEFF Renta Variable. 08: MEFF Renta Fija. 10: Mercado AIAF. 11: Bolsas de Valores extranjeras. 12: Mercados de Derivados extranjeros. 13: Otros mercados nacionales. 14: Otros mercados extranjeros. |
| 5 | 33-34 | Forma de contratación bursátil | X | 2 | Se identificará mediante las siguientes claves: AP: Aplicaciones. OP: Operaciones especiales con contrapartida por cuenta propia. OM: Operaciones especiales entre miembros. TR: Tomas de razón. RO: Resto de operaciones bursátiles. |
| 6 | 35-36 | Tipo de contratación | X | 2 | Se identificará mediante las siguientes claves: CO: Compra. VE: Venta. SP: Suscripción en mercado primario. CV: Conversión. OT: Otra. |
| 7 | 37-48 | Código de identificación de valor | X | 12 | Se usará el código ISIN para aquellos valores que los posean o el código que otorgue el correspondiente mercado cuando no exista código ISIN. Se completará con blancos si no se dispone de código. |
| 8 | 49-88 | Denominación del valor | X | 40 | Se identificará el valor con su denominación. |
| 9 | 89-96 | Fecha valor | N | 8 | Formato: AAAAMMDD |
| 10 | 97-105 | Número de valores | N | 9 |  |
| 11 | 106-117 | Efectivo de contratación | N | 12 |  |
| 12 | 118-120 | Moneda | X | 3 | Código alfabético de la norma ISO4217 |
| 13 | 121-170 | Comentarios | X | 50 | Aclaración de los campos anteriores siempre que resulte necesario. Se indicará además en este apartado la referencia al contrato o al mandato genérico específico recibido por la entidad cuando estas operaciones son ejecutadas por la entidad. |
| 14 | 171-172 | Final de registro | X | 2 | Siempre: |

Fichero de desgloses: DESGLOS

| Número | Posición | Nombre del campo | Formato | Longitud | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | 1-8 | Fecha de referencia. | N | 8 | Formato: AAAAMMDD. Contendrá la fecha de liquidación de la operación. Cuando se trate de operaciones bursátiles será la fecha teórica de liquidación. |
| 2 | 9-24 | Código de orden. | X | 16 | Debe coincidir con el incluido en el Fichero de órdenes para el orden que ha generado el desglose, salvo en los siguientes casos que identificarán mediante estas claves: CP: Operaciones ejecutadas por cuenta propia por la entidad. MG: Operaciones ejecutadas en virtud de mandatos genéricos o específicos. RO: Resto de operaciones que se ejecuten sin orden expresa del cliente. Cuando el desglose corresponda a una operación que no haya requerido la generación del Fichero de órdenes (punto 2.1 de la norma 4.a ) se indicará en este apartado el Código de Orden que vincule el desglose con el Archivo de Justificantes de Órdenes. |
| 3 | 25-40 | Código de ejecución. | X | 16 | Debe coincidir con el incluido en el fichero de ejecuciones para la ejecución que ha generado el desglose. |
| 4 | 41-56 | Código de operación. | X | 16 | Para el caso bursátil será el número de operación que se intercambia con el Servicio de Compensación y Liquidación de Valores. |
| 5 | 57-65 | Número de valores. | N | 9 |  |
| 6 | 66-77 | Efectivo de liquidación. | N | 12 | Los importes en euros se expresarán en céntimos de euro, sin comas. Los importes en otras monedas se expresarán en cifras enteras, sin incluir decimales. |
| 7 | 78-80 | Moneda. | X | 3 | Código alfabético de la norma ISO4217. |
| 8 | 81-84 | Código de entidad liquidadora. | X | 4 | Se indicará el código de la entidad de acuerdo con los siguientes criterios: Número de registro en el Banco de España.-Para bancos y entidades de crédito. Número de registro en la Comisión Nacional del Mercado de Valores + 3500.-Para sociedades y agencias de valores. No se completará para entidades no inscritas en los registros oficiales del Banco de España y la Comisión Nacional del Mercado de Valores. |
| 9 | 85-124 | Entidad liquidadora. | X | 40 | Se identificará a la entidad liquidadora por su denominación. |
| 10 | 125-174 | Comentario. | X | 50 | Aclaración a los campos anteriores siempre que resulte necesario. Cuando el campo «Código de orden» se haya completado con la clave MG se incluirá en este apartado la referencia identificativa del mandato recibido. |
| 11 | 175-176 | Final de registro. | X | 2 | Siempre: «CR» «LF». |

> Se modifica por la norma 2.IV de la Circular 7/1998, de 14 de junio. Ref. BOE-A-1998-30048.
