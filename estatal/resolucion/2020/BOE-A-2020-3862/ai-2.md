## ANEXO II

## Liquidaciones con tarjeta

1. Datos del formulario

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (012). Liquidaciones practicadas por la Administración. |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | An | Concepto o modelo (para este tipo de operación su valor puede ser 002, 004, 008, 010, 012, 031, 032, 060, 061 o 069). |
| 4 | 9 | 2 | An | Ejercicio fiscal (para este tipo de operación su valor es 00). |
| 5 | 11 | 2 | An | Período (para este tipo de operación su valor son espacios en blanco). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación ( I ). |
| 8 | 15 | 9 | An | NIF del contribuyente (XNNNNNNNX). |
| 9 | 24 | 4 | An | Para este tipo de operación su valor son espacios en blanco. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 62 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 15 | 65 | 16 | An | Número de la tarjeta. |
| 16 | 81 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 17 | 85 | 12 | N | Reservado para el importe en la moneda en que esté denominada la cuenta restringida del abono (no se pide al ciudadano, es calculado). |

2. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular de la tarjeta y ordenante de la operación. |
| 2 | 10 | 6 | N | Fecha AAMMDD. |
| 3 | 16 | 10 | N | Hora HHMMSSSSSS. |
| 4 | 26 | 3 | An | Tipo de operación (012). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | An | Concepto o modelo (002 ó 004). |
| 7 | 34 | 2 | N | Ejercicio fiscal (00). |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | NIF del contribuyente (XNNNNNNNX). |
| 12 | 49 | 1 | N | Forma autenticación y firma orden pago (1= Cl@vePIN, 0=certificado-e). |
| 13 | 50 | 1 | N | Ceros. |
| 14 | 51 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 63 | 13 | An | Número de justificante. |
| 16 | 76 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 17 | 80 | 4 | An | Código del Merchant. |
| 18 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 19 | 87 | 16 | An | Número de la tarjeta. |
| 20 | 103 | 4 | N | Fecha de caducidad de la tarjeta. |
| 21 | 107 | 12 | N | Importe en la moneda en que esté denominada la cuenta restringida del abono. |
| 22 | 119 | 14 | An | Espacios en blanco. |
| 23 | 133 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 24 | 149 | 4 | An | Espacios en blanco. |
| 25 | 153 | 40 | An | Apellidos y nombre o razón social del contribuyente. |
| 26 | 193 | 40 | An | Apellidos y nombre del titular de la tarjeta. |
| 27 | 233 | 40 | An | Espacios en blanco. |
| 28 | 273 | 32 | N | Reservado para posibles ampliaciones. |

Los importes se expresan en céntimos de euro.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la entidad y la AEAT.

El cálculo del MAC no se verá afectado.

3. Registro de respuesta desde la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (012). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | An | Concepto o modelo (002 ó 004). |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF del contribuyente (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 2 | N | Ceros. |
| 11 | 30 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 42 | 13 | An | Número de justificante. |
| 13 | 55 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 59 | 4 | An | Código del Merchant. |
| 15 | 63 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 16 | 66 | 16 | An | Número de la tarjeta. |
| 17 | 82 | 4 | N | Fecha de caducidad de la tarjeta. |
| 18 | 86 | 12 | N | Importe en la moneda en que esté denominada la cuenta restringida del abono. |
| 19 | 98 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 20 | 106 | 22 | An | Número de referencia completo (DDAATTNNNNNNDCXXXXXXXX). |
| 21 | 128 | 2 | An | Código de retorno. |
| 22 | 130 | 81 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación extendida para el error 87. |
