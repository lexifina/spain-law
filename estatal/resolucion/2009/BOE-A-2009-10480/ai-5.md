## ANEXO III bis

## Pago de liquidaciones practicadas por la Administración (Tarjeta)

1. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular de la tarjeta y ordenante de la operación. |
| 2 | 10 | 6 | N | Fecha AAMMDD. |
| 3 | 16 | 10 | N | Hora HHMMSSSSSS. |
| 4 | 26 | 3 | An | Tipo de Operación (012). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | An | Concepto o modelo. Por ejemplo: 002, 004, 008, 010, 012, 031, 032, 060, 061 o 069. |
| 7 | 34 | 2 | N | Ejercicio fiscal (00). |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | NIF del obligado al pago (XNNNNNNNX). |
| 12 | 49 | 1 | N | Forma autenticación y firma orden pago (1= Cl@vePIN, 0=certificado-e). |
| 13 | 50 | 1 | N | Ceros. |
| 14 | 51 | 12 | N | Importe del ingreso(ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 63 | 13 | An | Número de justificante. |
| 16 | 76 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 17 | 80 | 4 | An | Código del Merchant. |
| 18 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 19 | 87 | 16 | An | Número de la tarjeta. |
| 20 | 103 | 4 | N | Fecha de caducidad de la tarjeta. |
| 21 | 107 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 22 | 119 | 14 | An | Espacios en blanco. |
| 23 | 133 | 16 | An | Reservado (blancos). |
| 24 | 149 | 4 | An | Espacios en blanco. |
| 25 | 153 | 40 | An | Apellidos y Nombre o Razón Social del contribuyente. |
| 26 | 193 | 40 | An | Apellidos y Nombre del titular de la tarjeta. |
| 27 | 233 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 28 | 255 | 18 | An | Reservado (espacios en blanco). |
| 29 | 273 | 32 | N | Reservado para posibles ampliaciones. |

2. Registro de respuesta de la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (012). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | An | Concepto o modelo. Por ejemplo: 002, 004, 008, 010, 012, 031, 032, 060, 061 o 069. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF del obligado al pago (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 2 | N | Ceros. |
| 11 | 30 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 42 | 13 | An | Número de justificante. |
| 13 | 55 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 59 | 4 | An | Código del Merchant. |
| 15 | 63 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 16 | 66 | 16 | An | Número de la tarjeta. |
| 17 | 82 | 4 | N | Fecha de caducidad de la tarjeta. |
| 18 | 86 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 19 | 98 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 20 | 106 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 21 | 128 | 2 | An | Código de retorno. |
| 22 | 130 | 81 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación extendida para el error 87. |

> Se sustituye por el que figura en el anexo de la Resolución de 2 de septiembre de 2021, según establece su apartado primero.6. Ref. BOE-A-2021-14454

> Se suprime el punto 2 y los puntos 3 y 4 se renumeran como 2 y 3, y se modifica la descripción del campo Nº 1 de los nuevos puntos 2 y 3, por el apartado 1.10 de la Resolución de 11 de septiembre de 2014. Ref. BOE-A-2014-9468

> Téngase en cuenta el periodo de adaptación establecido en el apartado segundo de la citada Resolución.
