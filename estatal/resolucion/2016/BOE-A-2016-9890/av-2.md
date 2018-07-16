## ANEXO VI

## Ingreso de depósitos: Registros en la pasarela de Depósitos de Subastas de la Agencia Tributaria

1. Registro de orden de cargo.

| N.º | POS. | LONG. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 2 | 10 | 8 | N | Fecha AAAAMMDD. |
| 3 | 18 | 10 | N | Hora HHMMSSSSSS. |
| 4 | 28 | 3 | An | Tipo de operación de alta. 005 Ingreso de Depósitos. |
| 5 | 31 | 2 | An | Alta 01, Consulta 02. |
| 6 | 33 | 3 | N | Ceros. |
| 7 | 36 | 4 | N | Ceros. |
| 8 | 40 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 9 | 49 | 4 | N | Ceros. |
| 10 | 53 | 13 | N | Importe del ingreso. (Ajustado a la derecha y relleno de ceros a la izquierda). |
| 11 | 66 | 13 | An | Número de justificante (en el caso de consulta irá a blancos). |
| 12 | 79 | 20 | N | Reservado. |
| 13 | 99 | 22 | An | NRC de la constitución del depósito. |
| 14 | 121 | 8 | N | AAAAMMDD fecha constitución depósito. |
| 15 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 16 | 145 | 4 | An | Letras de etiqueta del titular del depósito en personas físicas. |
| 17 | 149 | 120 | An | Blancos. |
| 18 | 269 | 32 | An | Blancos. |
| 19 | 301 | 34 | An | Código IBAN. |
| 20 | 335 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 21 | 341 | 100 | An | Reservado. |

El MAC de 8 será generado a partir del contenido de las 128 primeras posiciones junto con el contenido de las posiciones 301 a 340.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza el SSL. La clave y sistema de este cifrado se acordará entre la Entidad y la Agencia Tributaria.

2. Registro de comunicación del NRC.

| N.º | POS. | LONG. | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación. 005 Ingreso de Depósitos. |
| 2 | 4 | 2 | An | Alta 01, Consulta 02. |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe del ingreso. (Ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 13 | An | Número de justificante (en el caso de consulta irá a blancos). |
| 10 | 59 | 20 | N | Reservado. |
| 11 | 79 | 11 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de referencia completo. (DDAATTNNNNNDCyXXXXXXXXX). |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |

> Téngase en cuenta que esta actualización, establecida por el apartado 1.4 de la Resolución de 4 de junio de 2018. Ref. BOE-A-2018-7835, será de aplicación desde el 16 de julio de 2018, según determina su apartado 2.

> Se modifica por el apartado 1.4 de la Resolución de 4 de junio de 2018. Ref. BOE-A-2018-7835.

> Esta modificación será de aplicación desde el 16 de julio de 2018, según determina el apartado 2 de la citada Resolución.
