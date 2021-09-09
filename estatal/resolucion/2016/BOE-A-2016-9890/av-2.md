## ANEXO VI

## Ingreso de depósitos en el Tesoro Público: Registros en la pasarela de depósitos de subastas de la Agencia Tributaria

1. El Portal de Subastas de la AEBOE deberá remitir la siguiente información. El formato en que esta información se deba transmitir a los sistemas de información de la AEAT será determinado por el Departamento de Informática Tributaria:

– Operación (005).

– Tipo de operación: Alta (01), consulta (02).

– NIF del titular del depósito.

– Apellidos y nombre o razón social del titular del depósito.

– NRC de constitución del depósito.

‒ Importe del ingreso (debe coincidir con el importe de constitución).

– Fecha de constitución del depósito.

– Código IBAN donde se constituyó el depósito.

– Tipo de autenticación.

– Identificador de subastas AEAT, si procede.

2. Registro de orden de cargo.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 2 | 10 | 8 | N | Fecha (AAAAMMDD). |
| 3 | 18 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 28 | 3 | An | Tipo de Operación de alta (005Ingreso de depósitos). |
| 5 | 31 | 2 | An | Alta (01), consulta (02). |
| 6 | 33 | 3 | N | Ceros. |
| 7 | 36 | 4 | N | Ceros. |
| 8 | 40 | 9 | An | NIF titular del depósito (XNNNNNNNX). |
| 9 | 49 | 4 | N | Ceros. |
| 10 | 53 | 13 | N | Importe del Ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 11 | 66 | 13 | An | Número de justificante(en el caso de consulta irá a blancos). |
| 12 | 79 | 20 | N | Reservado (ceros). |
| 13 | 99 | 22 | An | NRC de la constitución del depósito. |
| 14 | 121 | 8 | N | Fecha constitución de depósito(AAAAMMDD). |
| 15 | 129 | 16 | An | Reservado (blancos). |
| 16 | 145 | 4 | N | Letras de etiqueta del titular del depósito en personas físicas. |
| 17 | 149 | 120 | An | Blancos. |
| 18 | 269 | 32 | An | Blancos. |
| 19 | 301 | 34 | An | Código IBAN. |
| 20 | 335 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 21 | 357 | 84 | An | Reservado. |

3. Registro de respuesta de la entidad de crédito.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (005). Ingreso de Depósitos. |
| 2 | 4 | 2 | An | Alta (01), consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | N.I.F. del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe del Ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 13 | An | Número de justificante (en el caso de consulta irá a blancos). |
| 10 | 59 | 20 | N | Reservado. |
| 11 | 79 | 11 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |

> Se sustituye por el apartado 1.4 de la Resolución de 6 de septiembre de 2021. Ref. BOE-A-2021-14666

> Téngase en cuenta para su aplicación el apartado segundo de la citada Resolución.

> Se modifica por el apartado 1.4 de la Resolución de 4 de junio de 2018. Ref. BOE-A-2018-7835.

> Esta modificación será de aplicación desde el 16 de julio de 2018, según determina el apartado 2 de la citada Resolución.
