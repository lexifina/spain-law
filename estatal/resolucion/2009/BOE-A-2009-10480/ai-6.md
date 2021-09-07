## ANEXO IV

## Pago de tasas (Tarjeta)

1. Registro de orden de cargo

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular de la tarjeta y ordenante de la operación (XNNNNNNNX). |
| 2 | 10 | 6 | N | Fecha (AAMMDD). |
| 3 | 16 | 10 | N | Hora (HHMMSSSSSS). |
| 4 | 26 | 3 | An | Tipo de Operación (017). |
| 5 | 29 | 2 | An | Alta (01), Consulta (02). |
| 6 | 31 | 3 | N | Ceros. |
| 7 | 34 | 2 | N | Ceros. |
| 8 | 36 | 2 | An | Espacios en blanco. |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E). |
| 10 | 39 | 1 | An | Tipo de liquidación (I). |
| 11 | 40 | 9 | An | NIF del obligado tributario (XNNNNNNNX). |
| 12 | 49 | 2 | N | Ceros. |
| 13 | 51 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 14 | 63 | 13 | An | Número de justificante. |
| 15 | 76 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 16 | 80 | 4 | An | Código del Merchant. |
| 17 | 84 | 3 | An | Reservado para ampliación del número de tarjeta (000). |
| 18 | 87 | 16 | An | Número de la tarjeta. |
| 19 | 103 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 20 | 107 | 12 | N | Importe de la moneda en que está denominada la Cuenta Restringida del abono. |
| 21 | 119 | 14 | An | Espacios en blanco. |
| 22 | 133 | 16 | An | Reservado (blancos). |
| 23 | 149 | 4 | An | Espacios en blanco. |
| 24 | 153 | 40 | An | Apellidos y nombre o Razón social del obligado tributario. |
| 25 | 193 | 40 | An | Apellidos y nombre del titular de la tarjeta declarados por el ordenante de la operación. |
| 26 | 233 | 22 | An | Número de Referencia Completo generado por la AEAT. Solo en operaciones de alta, no de consulta. |
| 27 | 255 | 18 | An | Reservado (espacios en blanco). |
| 28 | 273 | 32 | N | Reservado para posibles ampliaciones. |

2. Registro de respuesta de la entidad colaboradora

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (017). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | NIF del obligado tributario (XNNNNNNNX). |
| 9 | 24 | 4 | An | Espacios en blanco. |
| 10 | 28 | 2 | N | Ceros. |
| 11 | 30 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 42 | 13 | An | Número de justificante. |
| 13 | 55 | 4 | An | Código Banco de España de la Entidad Emisora de la tarjeta. |
| 14 | 59 | 4 | An | Código del Merchant. |
| 15 | 63 | 3 | An | Reservado para ampliaciones del número de tarjeta (000). |
| 16 | 66 | 16 | An | Número de la tarjeta. |
| 17 | 82 | 4 | N | Fecha de caducidad de la tarjeta (MMAA). |
| 18 | 86 | 12 | N | Importe de la moneda en que esté denominada la Cuenta Restringida del abono. |
| 19 | 98 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 20 | 106 | 22 | An | Número de Referencia Completo recibido en la orden de cargo o asociado al ingreso en caso de consulta. |
| 21 | 128 | 2 | An | Código de retorno. |
| 22 | 130 | 81 | N | Reservado para posibles ampliaciones. |
| 23 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias para el error 87. |

Aplicable a todos los anexos:

Pos. = Posición.

N = Numérico.

Long. = Longitud.

An = Alfanumérico.

– Los importes se expresan en céntimos de euro.

– Todas las comunicaciones entre la Agencia Tributaria y las entidades colaboradoras adheridas a los servicios de pago se realizarán desde la Agencia Tributaria haciendo uso de un certificado electrónico cualificado que permita a las entidades colaboradoras determinar la autenticidad, integridad y no repudio de la información transmitida. No será necesaria, por lo tanto, la inclusión de ningún proceso de cifrado adicional. Las entidades colaboradoras deberán validar que dichas peticiones estén asociadas al certificado electrónico de la Agencia Tributaria, no admitiendo las peticiones realizadas con otros certificados distintos de los comunicados por la Agencia Tributaria en cada momento. Será responsabilidad de las entidades colaboradoras validar esta información de autenticación antes de procesar la operación de pago, no siendo la Agencia Tributaria responsable de los perjuicios generados en caso de que la entidad colaboradora no realizara dicha validación.

– Al servicio provisto por las entidades colaboradoras se le enviará por el método POST del protocolo HTTP un documento de texto plano y recibirá una respuesta que contiene a su vez un documento de texto plano, de acuerdo a los formatos definidos de Registro de Orden de Cargo y Registro de Respuesta de Entidad Colaboradora.

> Se sustituye por el que figura en el anexo de la Resolución de 2 de septiembre de 2021, según establece su apartado primero.6. Ref. BOE-A-2021-14454

> Se sustituye por el que figura en el anexo de la Resolución de 4 de abril de 2017, según establece su apartado 10. Ref. BOE-A-2017-4295

> Téngase en cuenta el periodo de adaptación establecido en el apartado 9 de la citada Resolución.

> Se suprime el punto 2 y los puntos 3 y 4 se renumeran como 2 y 3, y se modifica la descripción del campo Nº 1 de los nuevos puntos 2 y 3, por el apartado 1.10 de la Resolución de 11 de septiembre de 2014. Ref. BOE-A-2014-9468

> Téngase en cuenta el periodo de adaptación establecido en el apartado segundo de la citada Resolución.
