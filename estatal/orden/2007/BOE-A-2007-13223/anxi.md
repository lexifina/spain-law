## ANEXO XI

## ÓRDENES DE TRANSFERENCIAS: TRANSMISIÓN DE INFORMACIÓN CON BANCO DE ESPAÑA

1. DISEÑO DE REGISTROS

1.1 DISEÑO DE REGISTRO DE CABECERA DE TRANSMISIÓN

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 1=CABECERA DE TRANSMISIÓN |
| 2-9 | NUM. | FECHA DE INGRESO (AAAA MM DD) |
| 10-17 | NUM. | FECHA DE TRANSMISIÓN (AAAA MM DD) |
| 18-42 | ALF. | FILLER (A BLANCOS) |

1.2 DISEÑO DE REGISTRO DE LA ORDEN DE TRANSFERENCIA

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 2 = CABECERA O.T. |
| 2-4 | NUM. | CÓDIGO DEL TIPO DE INGRESO |
|  |  | 021=AUTOLIQUIDACIONES |
|  |  | 022 = AUTOLIQUID. ESPECIALES |
|  |  | 023 = LIQUIDACIONES |
|  |  | 050=TASAS DEL TESORO |
|  |  | 051= TASAS DE ORGANISMOS AUTÓNOMOS. |
| 5-8 | NUM. | CÓDIGO DE ENTIDAD COLABORADORA |
| 9-16 | NUM. | NÚMERO DE QUINCENA (AAAA MM QQ) |
|  |  | • AAAAMM01 para las quincenas que finalicen el 5 del mes |
|  |  | • AAAAMM02 para las quincenas que finalicen el 20 del mes |
| 17-22 | NUM. | NÚMERO SECUENCIAL DE LA OPERACIÓN |
| 23-29 | NUM. | NÚMERO TOTAL DE INGRESOS DE LA ORDEN DE TRANSFERENCIA |
| 30-42 | NUM. | IMPORTE TOTAL DE LA ORDEN DE TRANSFERENCIA |

1.3 DISEÑO DE REGISTRO DE MODELO (SOLO PARA TIPOS 021 Y 022)

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 3 = MODELO DE AUTOLIQUIDACIÓN |
| 2-4 | NUM. | CÓDIGO DEL MODELO DE AUTOLIQUIDACIÓN |
| 5-11 | NUM. | NÚMERO DE INGRESOS DEL MODELO |
| 12-24 | NUM. | IMPORTE TOTAL DEL MODELO |
| 25-42 | ALF. | FILLER (A BLANCOS) |

1.4 DISEÑO DE REGISTRO DE TOTAL DE LAS ÓRDENES DE TRANSFERENCIA

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 4 = TOTAL ORDEN TRANSFERENCIA. |
| 2-4 | NUM. | CÓDIGO DE LA ORDEN DE TRANSFERENCIA |
|  |  | 021 = AUTOLIQUIDACIONES |
|  |  | 022 = AUTOLIQUIDAC ESPECIALES |
|  |  | 023 = LIQUIDACIONES |
|  |  | 050 = TASAS DEL TESORO |
|  |  | 051 = TASAS DE ORGANISMOS AUTÓNOMOS |
| 5-11 | NUM. | NÚMERO TOTAL DE INGRESOS DE LAS ÓRDENES DE TRANSFERENCIA |
| 12-24 | NUM. | IMPORTE TOTAL DE LAS ORDENES DE TRANSFERENCIA |
| 25-42 | ALF. | FILLER (A BLANCOS) |

1.5 DISEÑO DE REGISTRO DE FIN DE TRANSMISIÓN

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 5 = FINAL DE TRANSMISIÓN |
| 2-9 | NUM. | FECHA DE INGRESO (AAAA MM DD) |
| 10-17 | NUM. | FECHA DE TRANSMISIÓN (AAAA MM DD) |
| 18-22 | NUM. | NÚMERO TOTAL DE REGISTROS TRANSMITIDOS INCLUIDOS CABECERA Y FINAL |
| 23-36 | NUM. | IMPORTE TOTAL DE LA TRANSMISIÓN |
| 37-42 | ALF. | FILLER (A BLANCOS) |

2. VALIDACIONES

▪ Todos los registros recibidos serán sometidos a un proceso de validación.

▪ Cualquier error detectado, de los que a continuación se relacionan, implicará el rechazo de la transmisión.

2.1 TIPO DE REGISTRO 1 (CABECERA DE TRANSMISIÓN)

• Tipo de registro distinto de 1

• Fecha de ingreso ilógica.

• Fecha de ingreso duplicada (ya se ha recibido una transmisión de datos aceptada para esta fecha de ingreso).

• Fecha de transmisión ilógica

• Fecha de transmisión menor que la fecha de ingreso.

2.2 TIPO DE REGISTRO 2 (ORDEN DE TRANSFERENCIA)

• Tipo de registro distinto de 2

• Código de tipo de ingreso no válido (distinto de 021, 022, 023, 050 y 051)

• Código de tipo de ingreso fuera de orden (no se admite una orden de transferencia de un determinado código fuera del grupo al que corresponda).

• Código de Entidad no es un código válido en el Registro del Banco de España.

• Número de la quincena no se ajusta al formato establecido.

• Número de secuencia de la operación duplicado en el año del ingreso.

• Número total de ingresos = 0

• Importe total de orden de transferencia = 0

2.3 TIPO DE REGISTRO 3 (POR MODELO DE AUTOLIQUIDACIÓN)

• Tipo de registro distinto de 3

• Código de modelo no es válido según código de tipo de ingreso (ver ANEXOS -I y II)

• Número de ingresos = 0

• Importe total por modelo de autoliquidación = 0

• Sumatorio del número de ingresos de los modelos incluidos en la orden de transferencia no coincide con el número total de ingresos de la orden de transferencia (Registro TIPO-2).

• Sumatorio de los importes totales de los modelos incluidos en la orden de transferencia no coincide con el importe total de la orden de transferencia (Registro TIPO-2).

2.4 TIPO DE REGISTRO 4 (TOTAL ENTIDADES DE UN CÓDIGO DE TIPO DE INGRESO)

• Tipo de registro distinto de 4

• Código de tipo de ingreso no coincide con el de la cabecera de la orden de transferencia (registros TIPO-2 previos)

• Número total de ingresos no coincide con el sumatorio de ingresos de la orden de transferencia del mismo código (Registros TIPO-2 previos).

• Importe total no coincide con el sumatorio de importes de la orden de transferencia del mismo código (Registros TIPO-2 previos).

2.5 TIPO DE REGISTRO 5 (FIN DE TRANSMISIÓN)

• Tipo de registro distinto de 5

• Fecha de ingreso distinta de la del registro de cabecera (registro TIPO-1).

• Fecha de transmisión distinta de la del registro de cabecera (registro TIPO-1).

• Número total de registros no coincide con los registros recibidos.

• Importe total del registro no coincide con el sumatorio de importes de los registros TIPO-4.
