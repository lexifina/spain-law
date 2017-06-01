## ANEXO II

## Pago de tasas (cargo en cuenta directo)

1. Datos del formulario.

| N.º | POS. | LONG. | Tipo. | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (007). Tasas (no se pide al ciudadano). |
| 2 | 4 | 2 | An | Alta (01), Consulta (02). |
| 3 | 6 | 3 | N | Ceros. |
| 4 | 9 | 2 | N | Ceros. |
| 5 | 11 | 2 | An | Espacios en blanco. |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E). |
| 7 | 14 | 1 | An | Tipo de liquidación (I). |
| 8 | 15 | 9 | An | N.I.F. del sujeto pasivo (XNNNNNNNX). |
| 9 | 24 | 4 | An | Reservado. |
| 10 | 28 | 5 | N | Ceros. |
| 11 | 33 | 12 | N | Importe del ingreso. (Ajustado a la derecha y relleno de ceros a la izquierda). |
| 12 | 45 | 13 | An | Número de justificante. |
| 13 | 58 | 20 | N | Reservado. |
| 14 | 78 | 12 | N | Ceros. |
| 15 | 90 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del sujeto pasivo y el ordenante de la operación está apoderado). |
| 16 | 91 | 34 | An | Código IBAN. |
| 17 | 125 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 18 | 131 | 9 | An | Reservado [NIF del ordenante de la operación (XNNNNNNNX)]. |
| 19 | 140 | 9 | An | Reservado [NIF del primer representante del ordenante de la operación (persona jurídica) o blancos (XNNNNNNNX)]. |
| 20 | 149 | 9 | An | Reservado [NIF del segundo representante del ordenante de la operación (persona jurídica) o blancos (XNNNNNNNX)]. |
| 21 | 158 | 40 | An | Apellidos y nombre o razón social del sujeto pasivo. |
| 22 | 198 | 40 | An | Reservado (Apellidos y nombre o razón social del ordenante de la operación). |
| 23 | 238 | 40 | An | Reservado [Apellidos y nombre del primer representante del ordenante de la operación (persona jurídica) o blancos]. |
| 24 | 278 | 40 | An | Reservado [Apellidos y nombre del segundo representante del ordenante de la operación (persona jurídica) o blancos]. |
| 25 | 318 | 1 | N | Reservado [Forma de autenticación y firma del ordenante de la operación en el organismo (0=certificado-e, 1=Cl@ve PIN, 2=Otros, 3=Por empleado público autorizado)]. |
| 26 | 319 | 9 | An | Por empleado público autorizado: Número de soporte del DNI/NIE del ordenante de la operación. |
| 27 | 328 | 9 | An | Por empleado público autorizado: Tipo de documento del ordenante de la operación. |
| 28 | 337 | 163 | An | Reservado para posibles ampliaciones. |

2. Registro de orden de cargo.

| N.º | POS. | LONG. | Tipo. | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | N.I.F. del ordenante de la operación (XNNNNNNNX). |
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
| 12 | 49 | 1 | N | Campo instrumental. Siempre tomará el valor 0. |
| 13 | 50 | 4 | N | Reservado (Ceros). |
| 14 | 54 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 15 | 66 | 13 | An | Número de justificante. |
| 16 | 79 | 20 | N | Reservado. |
| 17 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 18 | 111 | 9 | An | N.I.F. del primer representante del ordenante de la operación (persona jurídica) o blancos (XNNNNNNNX). |
| 19 | 120 | 9 | An | N.I.F. del segundo representante del ordenante de la operación (persona jurídica) o blancos (XNNNNNNNX). |
| 20 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 21 | 145 | 4 | An | Espacios en blanco. |
| 22 | 149 | 40 | An | Apellidos y nombre o Razón social del sujeto pasivo. |
| 23 | 189 | 40 | An | Apellidos y nombre del primer representante del ordenante de la operación (persona jurídica) o del titular ordenante de la operación (persona física). |
| 24 | 229 | 40 | An | Apellidos y nombre del segundo representante del ordenante de la operación (persona jurídica) o blancos. |
| 25 | 269 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del sujeto pasivo y el ordenante de la operación está apoderado). |
| 26 | 270 | 31 | An | Apellidos y nombre o razón social del apoderado ordenante de la operación (sólo en caso de que el campo 25 tome el valor «1»). |
| 27 | 301 | 34 | An | Código IBAN. |
| 28 | 335 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 29 | 341 | 100 | An | Reservado. |

El MAC de 8 será generado a partir del contenido de las 120 primeras posiciones junto con el contenido de las posiciones 301 a 340, y constituye el Código Cifrado de Operación.

Los importes se expresan en céntimos de euro.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza SSL. La clave y sistema de este cifrado se acordará entre la Entidad y la A.E.A.T.

3. Registro de respuesta de la entidad colaboradora.

| N.º | POS. | LONG. | Tipo. | Descripción |
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
| 10 | 28 | 1 | N | Campo instrumental. Siempre tomará el valor 0. |
| 11 | 29 | 4 | N | Reservado (Ceros). |
| 12 | 33 | 12 | N | Importe del ingreso (ajustado a la derecha y relleno de ceros a la izquierda). |
| 13 | 45 | 13 | An | Número de justificante. |
| 14 | 58 | 20 | N | Reservado. |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 16 | 90 | 8 | N | Fecha de la operación de alta (AAAAMMDD). |
| 17 | 98 | 22 | An | Número de Referencia Completo (MMMTTTSSSSSSC0XXXXXXXX). |
| 18 | 120 | 2 | An | Código de retorno. |
| 19 | 122 | 1 | N | Marca de apoderado («0» si la cuenta es de titularidad del ordenante de la operación, y «1» si la cuenta de cargo es del sujeto pasivo y el ordenante de la operación está apoderado). |
| 20 | 123 | 34 | An | Código IBAN. |
| 21 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 21 | 211 | 189 | An | Explicación del horario para error 86 y explicación amplia del error, con teléfono de incidencias, para el error 87. |

> Se sustituye por el que figura en el anexo de la Resolución de 4 de abril de 2017, según establece su apartado 10. Ref. BOE-A-2017-4295

> Téngase en cuenta el periodo de adaptación establecido en el apartado 9 de la citada Resolución.

> Se sustituye por el que figura en el anexo de la Resolución de 11 de septiembre de 2014, según establece su apartado 1.9. Ref. BOE-A-2014-9468

> Téngase en cuenta el periodo de adaptación establecido en el apartado segundo de la citada Resolución.
