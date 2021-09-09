## ANEXO II

## Número de referencia completo (NRC) de constitución de depósitos

1. El Portal de Subastas de la AEBOE deberá remitir la siguiente información. El formato en que esta información se deba transmitir a los sistemas de información de la AEAT será determinado por el Departamento de Informática Tributaria:

– Operación (003).

– Tipo de operación: Alta (01), consulta (02).

– Concepto/modelo (960).

– NIF del titular del depósito.

– Apellidos y nombre o razón social del titular del depósito.

– Importe del depósito.

– Fecha de constitución del depósito.

– Código IBAN.

– NIF del primer representante, si lo hubiera.

– Apellidos y nombre o razón social del primer representante, si lo hubiera.

– NIF del segundo representante, si lo hubiera.

– Apellidos y nombre o razón social del segundo representante, si lo hubiera.

– Tipo de autenticación.

2. Registro de orden de cargo.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 2 | 10 | 8 | N | Fecha (AAAAMMDD). |
| 3 | 18 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 28 | 3 | An | Tipo de operación de alta (003 constitución depósito). |
| 5 | 31 | 2 | An | Alta (01), consulta (02). |
| 6 | 33 | 3 | N | Concepto o modelo 960. |
| 7 | 36 | 4 | N | Ceros. |
| 8 | 40 | 9 | An | NIF titular del depósito (XNNNNNNNX). |
| 9 | 49 | 5 | An | Ceros. |
| 10 | 54 | 13 | N | Importe del depósito (ajustado a la derecha y relleno de ceros a la izquierda). |
| 11 | 67 | 16 | N | Ceros. |
| 12 | 83 | 20 | N | Reservado (ceros). |
| 13 | 103 | 8 | N | Fecha constitución de depósito(AAAAMMDD). |
| 14 | 111 | 9 | An | NIF del representante 1 o blancos. |
| 15 | 120 | 9 | An | NIF del representante 2 o blancos. |
| 16 | 129 | 16 | An | Reservado (blancos). |
| 17 | 145 | 4 | An | Letras de etiqueta del titular del depósito en personas físicas. |
| 18 | 149 | 40 | An | Apellidos y nombre o Razón social del titular del depósito. |
| 19 | 189 | 40 | An | Apellidos y nombre del representante 1 o blancos. |
| 20 | 229 | 40 | An | Apellidos y nombre del representante 2 o blancos. |
| 21 | 269 | 32 | An | Blancos. |
| 22 | 301 | 34 | An | Código IBAN. |
| 23 | 335 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 24 | 357 | 84 | An | Reservado. |

3. Registro de respuesta de la entidad de crédito.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (003). Constitución depósito. |
| 2 | 4 | 2 | An | Alta (01), consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (960 para constitución). |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | N.I.F. del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe del depósito (ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 12 | N | Ceros. |
| 10 | 58 | 20 | N | Reservado. |
| 11 | 78 | 12 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |
| 19 | 400 | 50 | An | Reservado para posibles ampliaciones. |

> Se sustituye por el apartado 1.4 de la Resolución de 6 de septiembre de 2021. Ref. BOE-A-2021-14666

> Téngase en cuenta para su aplicación el apartado segundo de la citada Resolución.
