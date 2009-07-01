## ANEXO II

## Pago de tasas (cargo en cuenta directo)

1. Datos del formulario

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (007). Tasas (no se pide al ciudadano). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del obligado al pago (XNNNNNNNX). |
| 9 | 24 | 4 | An | Para este tipo de operación su valor son espacios en blanco. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso. (Ajustado a la derecha y relleno de ceros a la izquierda.) |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 20 | N | Código Cuenta Cliente. |
| 14 | 78 | 12 | N | Ceros. |
| 15 | 90 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |

2. Registro de datos reenviados por la A.E.A.T.

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (007). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Ceros. |
| 7 | 34 | 2 | N | Ceros. |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del sujeto pasivo (XNNNNNNNX). |
| 12 | 49 | 5 | N | Ceros. |
| 13 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 13 | An | Número de justificante. |
| 15 | 79 | 20 | N | Código Cuenta Cliente. |
| 16 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 17 | 111 | 9 | An | N.I.F. del primer representante o blancos (XNNNNNNNX). |
| 18 | 120 | 9 | An | N.I.F. del segundo representante o blancos (XNNNNNNNX). |
| 19 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 20 | 145 | 4 | An | Espacios en blanco. |
| 21 | 149 | 40 | An | Apellidos y Nombre o Razón Social del sujeto pasivo. |
| 22 | 189 | 40 | An | Apellidos y Nombre del primer representante (certificado de persona jurídica) o del titular firmante (certificado de persona física). |
| 23 | 229 | 40 | An | Apellidos y Nombre del segundo representante o blancos. |
| 24 | 269 | 100 | An | ACTION completo de la EE.CC. que acepta peticiones de NRC, que debe empezar por https:. |
| 25 | 369 | 4 | An | Método del formulario (POST). |
| 26 | 373 | 25 | An | Variables y valores a enviar al comienzo (opcional). |
| 27 | 398 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |

El MAC de 8 será generado a partir del contenido de las 120 primeras posiciones. Los importes se expresan en céntimos de euro.

3. Registro de orden de cargo

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (007). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Ceros. |
| 7 | 34 | 2 | N | Ceros. |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | N.I.F. del sujeto pasivo (XNNNNNNNX). |
| 12 | 49 | 5 | N | Ceros. |
| 13 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 13 | An | Número de justificante. |
| 15 | 79 | 20 | N | Código Cuenta Cliente. |
| 16 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 17 | 111 | 9 | An | N.I.F. del primer representante o blancos (XNNNNNNNX). |
| 18 | 120 | 9 | An | N.I.F. del segundo representante o blancos (XNNNNNNNX). |
| 19 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 20 | 145 | 4 | An | Espacios en blanco. |
| 21 | 149 | 40 | An | Apellidos y Nombre o Razón social del sujeto pasivo. |
| 22 | 189 | 40 | An | Apellidos y Nombre del primer representante (certificado persona jurídica) o del titular firmante (certificado de persona física). |
| 23 | 229 | 40 | An | Apellidos y Nombre del segundo representante o blancos. |
| 24 | 269 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |
| 25 | 270 | 31 | N | Apellidos y nombre o razón social del apoderado/titular del certificado (sólo en caso de que el campo 24 tome el valor «1»). |

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la Entidad y la A.E.A.T.

4. Registro de respuesta de la Entidad colaboradora

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (007). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del sujeto pasivo (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 20 | N | Código Cuenta Cliente. |
| 14 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 15 | 90 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 16 | 98 | 22 | An | Número de Referencia Completo (MMMTTTSSSSSSC0XXXXXXXX). |
| 17 | 120 | 2 | An | Código de retorno. |
| 18 | 122 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |
| 19 | 123 | 88 | N | Reservado para posibles ampliaciones. |
| 20 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |
