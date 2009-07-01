## ANEXO I

## Pago de autoliquidaciones (cargo en cuenta directo)

1. Datos del formulario

| N.º | POS. | LONG. | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (001). Autoliquidaciones (no se pide al ciudadano). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I o D). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Apellido (comienzo) en personas físicas. |
| 10 | 28 | 5 | N | Código de Administración (no se pide al ciudadano). |
| 11 | 33 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento). |
| 13 | 57 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2). |
| 14 | 58 | 20 | N | Código Cuenta Cliente. |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. (No se pide al ciudadano. Es calculado.) |
| 16 | 90 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |

Pos. = Posición.

N = Numérico.

Long. = Longitud.

An = Alfanumérico.

2. Registro de datos reenviados por la A.E.A.T.

| N.º | POS. | LONG. | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (001). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de autoliquidación (I o D). |
| 11 | 40 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 5 | N | Código de Administración. |
| 13 | 54 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento). |
| 15 | 78 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2). |
| 16 | 79 | 20 | N | Código Cuenta Cliente. |
| 17 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. (No se pide al ciudadano. Es calculado.) |
| 18 | 111 | 9 | An | NIF del primer representante o blancos (XNNNNNNNX). |
| 19 | 120 | 9 | An | NIF del segundo representante o blancos (XNNNNNNNX). |
| 20 | 129 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 21 | 145 | 4 | An | Letras de etiqueta del obligado tributario en personas físicas. |
| 22 | 149 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 23 | 189 | 40 | An | Apellidos y Nombre del primer representante o blancos. |
| 24 | 229 | 40 | An | Apellidos y Nombre del segundo representante o blancos. |
| 25 | 269 | 100 | An | ACTION completo de la EE.CC. que acepta peticiones de NRC, que debe empezar por https:. |
| 26 | 369 | 4 | An | Método del formulario (POST). |
| 27 | 373 | 25 | An | Variables y valores a enviar al comienzo (opcional). |
| 28 | 398 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |

El MAC de 8 será generado a partir de los datos de las 128 primeras posiciones y constituye el Código Cifrado de Operación.

Los importes se expresarán en céntimos de euro.

3. Registro de orden de cargo

| N.º | POS. | LONG. | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular del certificado de firma electrónica (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (001). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (Ej.: 0A, 1T, 01, ...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de autoliquidación (I o D). |
| 11 | 40 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 5 | N | Código de Administración. |
| 13 | 54 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 66 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento –100 y 102–). |
| 15 | 78 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2 en 100). |
| 16 | 79 | 20 | N | Código Cuenta Cliente. |
| 17 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. |
| 18 | 111 | 9 | An | NIF del primer representante o blancos (XNNNNNNNX). |
| 19 | 120 | 9 | An | NIF del segundo representante o blancos (XNNNNNNNX). |
| 20 | 129 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 21 | 145 | 4 | An | Letras de etiqueta del obligado tributario en personas físicas. |
| 22 | 149 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 23 | 189 | 40 | An | Apellidos y Nombre del primer representante (certificado persona jurídica) o del titular firmante (certificado de persona física). |
| 24 | 229 | 40 | An | Apellidos y Nombre del segundo representante o blancos. |
| 25 | 269 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |
| 26 | 270 | 31 | N | Apellidos y nombre o razón social del apoderado/titular del certificado (sólo en caso de que el campo 25 tome el valor «1»). |

Mediante acuerdo entre la A.E.A.T. y la Entidad colaboradora interesada los datos de los campos 4 en adelante podrán ser transmitidos con un cifrado adicional al realizado por SSL.

4. Registro de respuesta de la Entidad colaboradora

| N.º | POS. | LONG. | TIPO. | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (001). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110, ...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01, ...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I o D). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 10 | 28 | 5 | N | Código de Administración. |
| 11 | 33 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento). |
| 13 | 57 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2). |
| 14 | 58 | 20 | N | Código Cuenta Cliente. |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. |
| 16 | 90 | 8 | N | Fecha de operación de alta (AAAAMMDD). |
| 17 | 98 | 22 | An | Número de Referencia Completo (MMMBBBBNNNNNDCXXXXXXXX). |
| 18 | 120 | 2 | An | Código de retorno. |
| 19 | 122 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del firmante de la operación, y «1» si la cuenta de cargo es del obligado y el firmante de la operación está apoderado). |
| 20 | 123 | 88 | N | Reservado para posibles ampliaciones. |
| 21 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |
