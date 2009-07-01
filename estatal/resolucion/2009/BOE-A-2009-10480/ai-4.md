## ANEXO III

## Pago de autoliquidaciones (tarjeta)

1. Datos del formulario

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (011). Autoliquidaciones. |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Apellidos (comienzo) en personas físicas. |
| 10 | 28 | 5 | N | Código de Administración. (No se pide al ciudadano.) |
| 11 | 33 | 12 | N | Importe del ingreso. (Ajustado a la derecha y relleno de ceros a la izquierda.) |
| 12 | 45 | 12 | N | Importe total de la deuda. (Renta con fraccionamiento.) |
| 13 | 57 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 61 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 15 | 64 | 16 | An | Número de la tarjeta. |
| 16 | 80 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 17 | 84 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. (No se pide al ciudadano. Es calculado.) |

2. Registro de datos reenviados por la A.E.A.T.

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular de la tarjeta y del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (011). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 5 | N | Código de Administración. |
| 13 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 12 | N | Importe total de la deuda. (Renta con fraccionamiento.) |
| 15 | 78 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 16 | 82 | 4 | An | Código del Merchant. |
| 17 | 86 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 89 | 16 | An | Número de la tarjeta. |
| 19 | 105 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 109 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 21 | 121 | 14 | An | Espacios en blanco. |
| 22 | 135 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 23 | 151 | 4 | An | Letras de etiqueta del obligado tributario en personas físicas. |
| 24 | 155 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 25 | 195 | 40 | An | Apellidos y Nombre del titular de la tarjeta declarados por el titular del certificado. |
| 26 | 235 | 40 | An | Espacios en blanco. |
| 27 | 275 | 100 | An | ACTION completo de la EE.CC. que acepta peticiones de NRC, que debe empezar por https:. |
| 28 | 375 | 4 | An | Método del formulario (POST). |
| 29 | 379 | 25 | An | Variables y valores a enviar al comienzo (opcional). |

El MAC de 8 será generado a partir de los datos de las 120 primeras posiciones y constituye el Código Cifrado de Operación.

3. Registro de orden de cargo

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular de la tarjeta y del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (011). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 5 | N | Código de Administración. |
| 13 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 12 | N | Importe total de la deuda. (Renta con fraccionamiento –100 y 102–.) |
| 15 | 78 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 16 | 82 | 4 | An | Código del Merchant. |
| 17 | 86 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 89 | 16 | An | Número de la tarjeta. |
| 19 | 105 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 109 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 21 | 121 | 14 | An | Espacios en blanco. |
| 22 | 135 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 23 | 151 | 4 | An | Letras de etiqueta del obligado tributario en personas físicas. |
| 24 | 155 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 25 | 195 | 40 | An | Apellidos y Nombre del titular de la tarjeta declarados por el titular del certificado. |
| 26 | 235 | 40 | An | Espacios en blanco. |
| 27 | 275 | 32 | N | Reservado para posibles ampliaciones. |

Mediante acuerdo entre la A.E.A.T. y la entidad colaboradora interesada los datos de los campos 4 a 26 pueden ser transmitidos con un cifrado adicional al realizado por SSL.

4. Registro de respuesta de la Entidad colaboradora

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (011). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 10 | 28 | 5 | N | Código de Administración. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda. (Renta con fraccionamiento.) |
| 13 | 57 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 61 | 4 | An | Código del Merchant. |
| 15 | 65 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 16 | 68 | 16 | An | Número de la tarjeta. |
| 17 | 84 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 18 | 88 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 19 | 100 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 20 | 108 | 22 | An | Número de Referencia Completo (MMMBBBBNNNNNDCXXXXXXXX). |
| 21 | 130 | 2 | An | Código de retorno. |
| 22 | 132 | 79 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |
