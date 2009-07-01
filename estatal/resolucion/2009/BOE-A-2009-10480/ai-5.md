## ANEXO III bis

## Pago de liquidaciones practicadas por la Administración (tarjeta)

1. Datos del formulario

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (012). Liquidaciones practicadas por la Administración. |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo. (Para este tipo de operación su valor puede ser 002, 004, 008, 010, 012, 031, 032, 060, 061 ó 069.) |
| 4 | 9 | 2 | N | Ejercicio fiscal. (Para este tipo de operación su valor es 00.) |
| 5 | 11 | 2 | An | Período. (Para este tipo de operación su valor son espacios en blanco.) |
| 6 | 13 | 1 | An | Tipo de moneda de la liquidación (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del obligado al pago (XNNNNNNNX). |
| 9 | 24 | 4 | An | Para este tipo de operación su valor son espacios en blanco. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 62 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 15 | 65 | 16 | An | Número de la tarjeta. |
| 16 | 81 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 17 | 85 | 12 | N | Reservado para el importe en la moneda en que esté denominada la Cuenta Restringida del abono. (No se pide al ciudadano. Es calculado.) |

2. Registro de datos reenviados por la A.E.A.T.

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular de la tarjeta y del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (012). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (002, 004, 008, 010, 012, 031, 032, 060, 061 ó 069). |
| 7 | 34 | 2 | N | Ejercicio fiscal (00). |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la liquidación (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del obligado al pago (XNNNNNNNX). |
| 12 | 49 | 2 | N | Ceros. |
| 13 | 51 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 63 | 13 | An | Número de justificante. |
| 15 | 76 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 16 | 80 | 4 | An | Código del Merchant. |
| 17 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 87 | 16 | An | Número de la tarjeta. |
| 19 | 103 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 107 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 21 | 119 | 14 | An | Espacios en blanco. |
| 22 | 133 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 23 | 149 | 4 | An | Espacios en blanco. |
| 24 | 153 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 25 | 193 | 40 | An | Apellidos y Nombre del titular de la tarjeta declarados por el titular del certificado. |
| 26 | 233 | 40 | An | Espacios en blanco. |
| 27 | 273 | 100 | An | ACTION completo de la EE.CC. que acepta peticiones de NRC, que debe empezar por https:. |
| 28 | 373 | 4 | An | Método del formulario (POST). |
| 29 | 377 | 25 | An | Variables y valores a enviar al comienzo (opcional). |

El MAC de 8 será generado a partir del contenido de las 120 primeras posiciones.

3. Registro de orden de cargo

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular de la tarjeta y del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (012). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (002, 004, 008, 010, 012, 031, 032, 060, 061 ó 069). |
| 7 | 34 | 2 | N | Ejercicio fiscal (00). |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la liquidación (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del obligado al pago (XNNNNNNNX). |
| 12 | 49 | 2 | N | Ceros. |
| 13 | 51 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 63 | 13 | An | Número de justificante. |
| 15 | 76 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 16 | 80 | 4 | An | Código del Merchant. |
| 17 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 87 | 16 | An | Número de la tarjeta. |
| 19 | 103 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 107 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 21 | 119 | 14 | An | Espacios en blanco. |
| 22 | 133 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 23 | 149 | 4 | An | Espacios en blanco. |
| 24 | 153 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 25 | 193 | 40 | An | Apellidos y Nombre del titular de la tarjeta declarados por el titular del certificado. |
| 26 | 233 | 40 | An | Espacios en blanco. |
| 27 | 273 | 32 | N | Reservado para posibles ampliaciones. |

Existe la posibilidad de que los datos de los campos 4 a 26 incluido se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la Entidad y la A.E.A.T.

4. Registro de respuesta de la Entidad colaboradora

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (012). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (002, 004, 008, 010, 012, 031, 032, 060, 061 ó 069). |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la liquidación (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del obligado al pago (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 2 | N | Ceros. |
| 11 | 30 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 42 | 13 | An | Número de justificante. |
| 13 | 55 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 59 | 4 | An | Código del Merchant. |
| 15 | 63 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 16 | 66 | 16 | An | Número de la tarjeta. |
| 17 | 82 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 18 | 86 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 19 | 98 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 20 | 106 | 22 | An | Número de Referencia Completo (DDAATTNNNNNNDCXXXXXXXX). |
| 21 | 128 | 2 | An | Código de retorno. |
| 22 | 130 | 81 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |
