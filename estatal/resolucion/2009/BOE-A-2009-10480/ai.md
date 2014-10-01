## ANEXO I

## Pago de autoliquidaciones (cargo en cuenta directo)

1. Datos del formulario.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (001). Autoliquidaciones (no se pide al ciudadano). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110,...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01,...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I o D). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Apellido (comienzo) en personas físicas. |
| 10 | 28 | 5 | N | Campo reservado (no se pide al ciudadano) |
| 11 | 33 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento). |
| 13 | 57 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2). |
| 14 | 58 | 20 | N | Reservado. |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. (No se pide al ciudadano. Es calculado.) |
| 16 | 90 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación y «1» si la cuenta de cargo es del obligado y el ordenante de la operación está apoderado). Con pin tomará el valor «0». |
| 17 | 91 | 34 | An | Código IBAN. |
| 18 | 125 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 19 | 131 | 100 | An | Reservado. |

Pos. = Posición.

N = Numérico.

Long. = Longitud.

An = Alfanumérico.

2. Registro de orden de cargo.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del titular del certificado electrónico / del PIN24H (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (001). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110,...). |
| 7 | 34 | 2 | N | Ejercicio fiscal (AA). |
| 8 | 36 | 2 | An | Período (Ej.: 0A, 1T, 01,...). |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración €. |
| 10 | 39 | 1 | An | Tipo de autoliquidación (I o D). |
| 11 | 40 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). Si el valor del campo 12 = «1», mismo NIF que campo 1. |
| 12 | 49 | 1 | N | Forma identificacióny autenticación orden pago (1=PIN, 0=Certificado-e) |
| 13 | 50 | 4 | N | Reservado (Ceros) |
| 14 | 54 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 66 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento –100 y 102–). |
| 16 | 78 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2 en 100). |
| 17 | 79 | 20 | N | Reservado. |
| 18 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. |
| 19 | 111 | 9 | An | NIF del primer representante o blancos (XNNNNNNNX). Con PIN (campo 12=»1») quedará en blanco. |
| 20 | 120 | 9 | An | NIF del segundo representante o blancos (XNNNNNNNX). Con PIN (campo 12=»1») quedará en blanco. |
| 21 | 129 | 16 | An | MAC de 8 con salida en hexadecimal. |
| 22 | 145 | 4 | An | Letras de etiqueta del obligado tributario en personas físicas. |
| 23 | 149 | 40 | An | Apellidos y Nombre o Razón Social del obligado tributario. |
| 24 | 189 | 40 | An | Apellidos y Nombre del primer representante (certificado persona jurídica) o del titular ordenante (certificado de persona física o PIN). |
| 25 | 229 | 40 | An | Apellidos y Nombre del segundo representante o blancos. Con PIN (campo 12=»1») quedará en blanco. |
| 26 | 269 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del obligado y el ordenante de la operación está apoderado). Con PIN (campo 12=»1») tomará el valor «0». |
| 27 | 270 | 31 | An | Apellidos y nombre o razón social del apoderado/titular del certificado (sólo en caso de que el campo 26 tome el valor «1»). |
| 28 | 301 | 34 | An | Código IBAN. |
| 29 | 335 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 30 | 341 | 100 | An | Reservado. |

El MAC de 8 será generado a partir del contenido de las 128 primeras posiciones junto con el contenido de las posiciones 301 a 340, y constituye el Código Cifrado de Operación.

Los importes se expresarán en céntimos de euro.

Mediante acuerdo entre la A.E.A.T. y la Entidad colaboradora interesada los datos de los campos 4 en adelante podrán ser transmitidos con un cifrado adicional al realizado por SSL.

3. Registro de respuesta de la entidad colaboradora.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (001). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (MMM, ej.: 100, 110,...). |
| 4 | 9 | 2 | N | Ejercicio fiscal (AA). |
| 5 | 11 | 2 | An | Período (ej.: 0A, 1T, 01,...). |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I o D). |
| 8 | 15 | 9 | An | N.I.F. del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 10 | 28 | 1 | N | Forma identificación y autenticación orden pago (1=PIN, 0=Certificado-e) |
| 11 | 29 | 4 | N | Reservado (Ceros) |
| 12 | 33 | 12 | N | Importe del ingreso/devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 13 | 45 | 12 | N | Importe total de la deuda (IRPF con fraccionamiento). |
| 14 | 57 | 1 | N | Opción de fraccionamiento, según normativa (1 ó 2). |
| 15 | 58 | 20 | N | Reservado. |
| 16 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono o solicitud de devolución. |
| 17 | 90 | 8 | N | Fecha de operación de alta (AAAAMMDD). |
| 18 | 98 | 22 | An | Número de Referencia Completo (MMMBBBBNNNNNDCXXXXXXXX). |
| 19 | 120 | 2 | An | Código de retorno. |
| 20 | 122 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del obligado y el ordenante de la operación está apoderado). Con PIN (campo 10=»1») tomará el valor «0». |
| 21 | 123 | 34 | An | Código IBAN |
| 22 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |

> Se sustituye por el que figura en el anexo de la Resolución de 11 de septiembre de 2014, según establece su apartado 1.9. Ref. BOE-A-2014-9468

> Téngase en cuenta el periodo de adaptación establecido en el apartado segundo de la citada Resolución.
