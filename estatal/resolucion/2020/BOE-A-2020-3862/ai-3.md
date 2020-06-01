## ANEXO III

## Tasas con tarjeta

1. Datos del formulario

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (017). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF del sujeto pasivo (XNNNNNNNX). |
| 9 | 24 | 4 | N | Espacios en blanco. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 62 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 15 | 65 | 16 | An | Número de la tarjeta. |
| 16 | 81 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 17 | 85 | 9 | An | Reservado [NIF del ordenante de la operación y titular de la tarjeta (XNNNNNNNX)]. |
| 18 | 94 | 40 | An | Apellidos y nombre o razón social del sujeto pasivo. |
| 19 | 134 | 40 | An | Reservado (apellidos y nombre del ordenante de la operación y titular de la tarjeta). |
| 20 | 174 | 1 | N | Reservado [forma de autenticación y firma del ordenante de la operación y titular de la tarjeta en el organismo (0=certificado-e, 1=Cl@ve PIN, 2=Otros, 3=Por empleado público autorizado)]. |
| 21 | 175 | 9 | An | Por empleado público autorizado: Número de soporte del DNI/NIE del ordenante de la operación y titular de la tarjeta. |
| 22 | 184 | 9 | An | Por empleado público autorizado: Tipo de documento del ordenante de la operación. |
| 23 | 193 | 200 | An | Reservado para posibles ampliaciones. |

2. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del ordenante de la operación (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD. |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de operación (017). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Ceros. |
| 7 | 34 | 2 | N | Ceros. |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | NIF del sujeto pasivo (XNNNNNNNX). |
| 12 | 49 | 2 | N | Ceros. |
| 13 | 51 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 63 | 13 | An | Número de justificante. |
| 15 | 76 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 16 | 80 | 4 | An | Código del Merchant. |
| 17 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 87 | 16 | An | Número de la tarjeta. |
| 19 | 103 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 107 | 12 | N | Importe de la moneda en que está denominada la cuenta restringida del abono. |
| 21 | 119 | 14 | An | Espacios en blanco. |
| 22 | 133 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 23 | 149 | 4 | An | Espacios en blanco. |
| 24 | 153 | 40 | An | Apellidos y nombre o Razón social del sujeto pasivo. |
| 25 | 193 | 40 | An | Apellidos y nombre del titular de la tarjeta declarados por el ordenante de la operación. |
| 26 | 233 | 40 | An | Espacios en blanco. |
| 27 | 273 | 32 | N | Reservado para posibles ampliaciones. |

Los importes se expresan en céntimos de euro.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la entidad y la AEAT.

3. Registro de respuesta desde la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (017). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF del sujeto pasivo (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 2 | N | Ceros. |
| 11 | 30 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 42 | 13 | An | Número de justificante. |
| 13 | 55 | 4 | An | Código Banco de España de la entidad emisora de la tarjeta. |
| 14 | 59 | 4 | An | Código del Merchant. |
| 15 | 63 | 3 | An | Reservado para ampliaciones del número de tarjeta (000). |
| 16 | 66 | 16 | An | Número de la tarjeta. |
| 17 | 82 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 18 | 86 | 12 | N | Importe de la moneda en que esté denominada la cuenta restringida del abono. |
| 19 | 98 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 20 | 106 | 22 | An | Número de referencia completo (DDAATTNNNNNNDCXXXXXXXX). |
| 21 | 128 | 2 | An | Código de retorno. |
| 22 | 130 | 81 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias para el error 87. |
