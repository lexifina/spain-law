## ANEXO II

## Pago de tasas (Cargo en cuenta directo)

1. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del ordenante de la operación (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (007). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Ceros. |
| 7 | 34 | 2 | N | Ceros. |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | NIF del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 1 | N | Campo instrumental. Siempre tomará el valor 0. |
| 13 | 50 | 4 | N | Reservado (ceros). |
| 14 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 66 | 13 | An | Número de justificante. |
| 16 | 79 | 20 | N | Reservado (ceros). |
| 17 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 18 | 111 | 9 | An | NIF del primer representante del ordenante de la operación (persona jurídica o blancos (XNNNNNNNX). |
| 19 | 120 | 9 | An | NIF del segundo representante del ordenante de la operación (persona jurídica o blancos) (XNNNNNNNX). |
| 20 | 129 | 16 | An | Reservado (blancos). |
| 21 | 145 | 4 | An | Espacios en blanco. |
| 22 | 149 | 40 | An | Apellidos y Nombre o Razón social del obligado tributario. |
| 23 | 189 | 40 | An | Apellidos y Nombre del primer representante del ordenante de la operación (persona jurídica) o del titular ordenante de la operación (persona física). |
| 24 | 229 | 40 | An | Apellidos y Nombre del segundo representante del ordenante de la operación (persona jurídica o blancos). |
| 25 | 269 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del obligado tributario y el ordenante de la operación está apoderado). |
| 26 | 270 | 31 | An | Apellidos y nombre o razón social del apoderado ordenante de la operación (solo en caso de que el campo 25 tome el valor «1»). |
| 27 | 301 | 34 | An | Código IBAN. |
| 28 | 335 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 29 | 357 | 84 | An | Reservado. |

2. Registro de respuesta de la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (007). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 1 | N | Campo instrumental. Siempre tomará el valor 0. |
| 11 | 29 | 4 | N | Reservado (ceros). |
| 12 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 13 | 45 | 13 | An | Número de justificante. |
| 14 | 58 | 20 | N | Reservado. |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 16 | 90 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 17 | 98 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 18 | 120 | 2 | An | Código de retorno. |
| 19 | 122 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del obligado tributario y el ordenante de la operación está apoderado). |
| 20 | 123 | 34 | An | Código IBAN. |
| 21 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 21 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |

> Se sustituye por el que figura en el anexo de la Resolución de 2 de septiembre de 2021, según establece su apartado primero.6. Ref. BOE-A-2021-14454

> Se sustituye por el que figura en el anexo de la Resolución de 4 de abril de 2017, según establece su apartado 10. Ref. BOE-A-2017-4295

> Téngase en cuenta el periodo de adaptación establecido en el apartado 9 de la citada Resolución.

> Se sustituye por el que figura en el anexo de la Resolución de 11 de septiembre de 2014, según establece su apartado 1.9. Ref. BOE-A-2014-9468

> Téngase en cuenta el periodo de adaptación establecido en el apartado segundo de la citada Resolución.
