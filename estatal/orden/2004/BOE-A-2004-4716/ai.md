## ANEXO I

Se utilizará el mismo fichero para la «Cuenta restringida de ingresos procedentes de operadores extracomunitarios», como para la «Cuenta restringida de ingresos procedentes de otros Estados Comunitarios», con la información de detalle en cuanto a formato y datos necesarios de los ingresos producidos.

Especificaciones técnicas:

1. Programa de transferencia de ficheros: EDITRAN.

2. Longitud de registro: 600 caracteres.

3. Estructura del fichero:

Registro de Cabecera.

Registros de Detalle.

Registro de Final de soporte.

4. Diseño de registros.

Definición del Registro de Cabecera:

| FMT | Nombre | Observaciones/valor del campo |
| --- | --- | --- |
| N1 | Código de registro. | 1 |
| N3 | Identificador de la cuenta. | 060-Ordenantes Extracomunitarios. 061-Estados Comunitarios. |
| N8 | Fecha de abono. | Fecha de abono del ingreso. Formato AAAAMMDD. Será la fecha contable. |
| N2 | Número de Orden del Soporte. | Indica el número de soporte para cada fecha de abono. |
| A586 | Libre. | Disponible para uso futuro. |

Definición del Registro de Detalle:

| FMT | Nombre | Observaciones/valor del campo |
| --- | --- | --- |
| N1 | Código de registro. | 2 |
| A160 | Ordenante. | Ordenante de la operación. |
| N14,2 | Importe en divisas. | Importe en moneda si es diferente del euro. |
| N13,2 | Importe en euros. | Contravalor en euros de la operación. Debería ser siempre en euros. |
| A3 | Moneda. | Nombre ISO de la moneda utilizada (ejemplo: USD, EUR). |
| A210 | Concepto. | Concepto de pago, texto libre. |
| A195 | Libre. | Disponible para uso futuro. |

Definición del Registro de Final:

| FMT | Nombre | Observaciones/valor del campo |
| --- | --- | --- |
| N1 | Código de registro. | 9 |
| A14,2 | Importe total en euros. | Se corresponde con el total de todos los ingresos contenidos en los registros de detalle. |
| A583 | Libre. | Disponible para uso futuro. |

Características de los registros:

Los campos numéricos estarán alineados a la derecha, rellenando con ceros a la izquierda y los alfanuméricos se alinearán a la izquierda, rellenando con blancos a la derecha.

Los campos numéricos sin datos estarán rellenos con ceros. Los alfanuméricos, en la misma circunstancia, se rellenarán con blancos.

Los campos de fecha se ajustarán siempre al formato AAAAMMDD.

Los campos definidos como «Libre» contendrán siempre blancos.
