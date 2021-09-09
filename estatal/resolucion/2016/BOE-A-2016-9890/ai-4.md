## ANEXO IV

## Número de referencia completo (NRC) de devolución de depósitos

## Primero. Registros en la pasarela de depósitos de subastas de la Agencia Tributaria. Devolución de depósitos: Procedimiento general.

1. El Portal de Subastas de la AEBOE deberá remitir la siguiente información. El formato en que esta información se deba transmitir a los sistemas de información de la AEAT será determinado por el Departamento de Informática Tributaria:

– Operación (004).

– Tipo de operación: Alta (01), consulta (02).

– Concepto/modelo (961).

– NIF del titular del depósito.

– Apellidos y nombre o razón social del titular del depósito.

– NRC de constitución del depósito.

– Importe del depósito a devolver

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
| 4 | 28 | 3 | An | Tipo de operación de alta (004 Devolución de depósito). |
| 5 | 31 | 2 | An | Alta (01), consulta (02). |
| 6 | 33 | 3 | N | Concepto o modelo 961. |
| 7 | 36 | 3 | N | Ceros. |
| 8 | 39 | 9 | An | NIF titular del depósito (XNNNNNNNX). |
| 9 | 48 | 13 | N | Importe del depósito a devolver (ajustado a la derecha y relleno de ceros a la izquierda). |
| 10 | 61 | 20 | N | Reservado (ceros). |
| 11 | 81 | 22 | An | NRC de la constitución del depósito. |
| 12 | 103 | 8 | N | Fecha constitución de depósito (AAAAMMDD). |
| 13 | 111 | 9 | An | NIF del representante 1 o blancos. |
| 14 | 120 | 9 | An | NIF del representante 2 o blancos. |
| 15 | 129 | 16 | An | Reservado (blancos). |
| 16 | 145 | 4 | An | Letras de etiqueta del titular del depósito en personas físicas. |
| 17 | 149 | 40 | An | Apellidos y nombre o Razón social del titular del depósito. |
| 18 | 189 | 40 | An | Apellidos y nombre del representante 1 o blancos. |
| 19 | 229 | 40 | An | Apellidos y nombre del representante 2 o blancos. |
| 20 | 269 | 32 | An | Blancos. |
| 21 | 301 | 34 | An | Código IBAN. |
| 22 | 335 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 23 | 357 | 84 | An | Reservado. |

3. Registro de respuesta de la entidad de crédito.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (004). Devolución de Depósitos. |
| 2 | 4 | 2 | An | Alta (01), consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (961 para devolución). |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe del abono (ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 12 | N | Ceros. |
| 10 | 58 | 20 | N | Reservado. |
| 11 | 78 | 12 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |
| 19 | 400 | 50 | An | Reservado para posibles ampliaciones. |

## Segundo. Registros en la pasarela de depósitos de subastas de la Agencia Tributaria. Devolución de depósitos: Procedimiento excepcional.

1. El Portal de Subastas de la AEBOE deberá remitir la siguiente información. El formato en que esta información se deba transmitir a los sistemas de información de la AEAT será determinado por el Departamento de Informática Tributaria:

– Operación (006).

– Tipo de operación: Alta (01), consulta (02).

– Concepto/modelo (962).

– NIF del titular del depósito.

– Apellidos y nombre o razón social del titular del depósito.

– NRC de constitución del depósito.

– Importe del depósito a devolver

– Fecha de constitución del depósito.

– Código IBAN de la cuenta donde se constituyó el depósito.

‒ Código IBAN de la cuenta de destino de la devolución mediante transferencia.

– NIF del primer representante, si lo hubiera.

– Apellidos y nombre o razón social del primer representante, si lo hubiera.

– NIF del segundo representante, si lo hubiera.

– Apellidos y nombre o razón social del segundo representante, si lo hubiera.

‒ Tipo de autenticación.

2. Registro de orden de cargo.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 2 | 10 | 8 | N | Fecha (AAAAMMDD). |
| 3 | 18 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 28 | 3 | An | Tipo de Operación de alta (006 Devolución de depósito por Transferencia). |
| 5 | 31 | 2 | An | Alta (01), consulta (02). |
| 6 | 33 | 3 | N | Concepto o modelo 962. |
| 7 | 36 | 9 | An | NIF titular del depósito (XNNNNNNNX). |
| 8 | 45 | 13 | N | Importe del depósito a devolver (ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 58 | 20 | N | Reservado (ceros). |
| 10 | 78 | 20 | N | Reservado (ceros). |
| 11 | 98 | 22 | An | NRC de la constitución del depósito. |
| 12 | 120 | 9 | An | NIF del representante 1 o blancos. |
| 13 | 129 | 9 | An | NIF del representante 2 o blancos. |
| 14 | 138 | 8 | N | Fecha constitución de depósito (AAAAMMDD). |
| 15 | 146 | 7 | An | Ceros. |
| 16 | 153 | 16 | An | Reservado (blancos). |
| 17 | 169 | 4 | An | Letras de etiqueta del titular del depósito en personas físicas. |
| 18 | 173 | 40 | An | Apellidos y nombre o Razón social del titular del depósito. |
| 19 | 213 | 40 | An | Apellidos y nombre del representante 1 o blancos. |
| 20 | 253 | 40 | An | Apellidos y nombre del representante 2 o blancos. |
| 21 | 293 | 8 | An | Blancos. |
| 22 | 301 | 34 | An | Código IBAN desde donde se constituyó el depósito. |
| 23 | 335 | 34 | An | Código IBAN destino de la transferencia. |
| 24 | 369 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 25 | 391 | 50 | An | Reservado. |

3. Registro de respuesta de la entidad de crédito.

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación (006). Devolución de Depósitos por Transferencia. |
| 2 | 4 | 2 | An | Alta (01), consulta (02). |
| 3 | 6 | 3 | N | Concepto o modelo (962 para devolución por transferencia). |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe de la devolución (ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 12 | N | Ceros. |
| 10 | 58 | 20 | N | Reservado. |
| 11 | 78 | 12 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN destino de la devolución. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |
| 19 | 400 | 50 | An | Reservado para posibles ampliaciones. |

> Se sustituye por el apartado 1.4 de la Resolución de 6 de septiembre de 2021. Ref. BOE-A-2021-14666

> Téngase en cuenta para su aplicación el apartado segundo de la citada Resolución.

> Se modifica el título del apartado segundo y se añade el tercero por el apartado 1.2 y 3 de la Resolución de 4 de junio de 2018. Ref. BOE-A-2018-7835

> Esta actualización será de aplicación desde el 16 de julio de 2018, según establece el apartado 2 de la citada Resolución.
