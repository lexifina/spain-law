## ANEXO I

## Autoliquidaciones con tarjeta

1. Datos del formulario

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (011). Autoliquidaciones. |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, Ej.: 100, 111,...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01,...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I). |
| 8 | 15 | 9 | An | NIF del contribuyente (XNNNNNNNX). |
| 9 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda (renta con fraccionamiento). |
| 13 | 57 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 61 | 3 | An | Reservado para ampliación número de tarjeta (000). |
| 15 | 64 | 16 | An | Número de la tarjeta. |
| 16 | 80 | 4 | N | Fecha de caducidad de la tarjeta. |
| 17 | 84 | 12 | N | Importe en la moneda en que esté denominada la cuenta restringida del abono (no se pide al ciudadano, es calculado). |

2. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular de la tarjeta y ordenante de la operación. |
| 2 | 10 | 6 | N | Fecha AAMMDD. |
| 3 | 16 | 10 | N | Hora HHMMSSSSSS. |
| 4 | 26 | 3 | An | Tipo de operación (011). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, Ej.: 100, 111,...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (ej.: 0A, 1T, 01,...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de autoliquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del contribuyente. |
| 12 | 49 | 1 | N | Forma autenticación y firma orden pago (1= Cl@vePIN, 0=certificado-e). |
| 13 | 50 | 4 | N | Ceros. |
| 14 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 66 | 12 | N | Importe total de la deuda (renta con fraccionamiento). |
| 16 | 78 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 17 | 82 | 4 | An | Código del Merchant. |
| 18 | 86 | 3 | An | Reservado para ampliación número de tarjeta (000). |
| 19 | 89 | 16 | An | Número de la tarjeta. |
| 20 | 105 | 4 | N | Fecha de caducidad de la tarjeta. |
| 21 | 109 | 12 | N | Importe en la moneda en que esté denominada la cuenta restringida del abono. |
| 22 | 121 | 14 | An | Espacios en blanco. |
| 23 | 135 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 24 | 151 | 4 | An | Letras de etiqueta del contribuyente en personas físicas. |
| 25 | 155 | 40 | An | Apellidos y nombre o razón social del contribuyente. |
| 26 | 195 | 40 | An | Apellidos y nombre del titular de la tarjeta. |
| 27 | 235 | 40 | An | Espacios en blanco. |
| 28 | 275 | 32 | N | Reservado para posibles ampliaciones. |

Los importes se expresan en céntimos de euro.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la entidad y la AEAT.

3. Registro de respuesta desde la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (011). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110,...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01,...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I). |
| 8 | 15 | 9 | An | NIF del contribuyente(XNNNNNNNX). |
| 9 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda (renta con fraccionamiento). |
| 13 | 57 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 61 | 4 | An | Código del Merchant. |
| 15 | 65 | 3 | An | Reservado para ampliación número de tarjeta (000). |
| 16 | 68 | 16 | An | Número de la tarjeta. |
| 17 | 84 | 4 | N | Fecha de caducidad de la tarjeta. |
| 18 | 88 | 12 | N | Importe en la moneda en que esté denominada la cuenta restringida del abono. |
| 19 | 100 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 20 | 108 | 22 | An | Número de referencia completo (MMMBBBBNNNNNDCXXXXXXXX). |
| 21 | 130 | 2 | An | Código de retorno. |
| 22 | 132 | 79 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |
