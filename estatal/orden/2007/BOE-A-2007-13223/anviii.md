## ANEXO VIII

## SUMINISTRO POR TELEPROCESO DE LOS EXTRACTOS DE LAS CUENTAS RESTRINGIDAS-ESPECIFICACIONES TÉCNICAS

1. Características de la conexión con el DIT para intercambio telemático de ficheros

1. Línea de comunicación

Conexión X-25 IBERPAC

Características:

Circuito virtual conmutado

Tamaño paquete: 128

Tamaño ventana nivel 2:7

Tamaño ventana nivel 3:7

2. Programa de transferencia de ficheros

EDITRAN

3. Longitud de registro: 80 caracteres

2. Diseño de registros

2.1 Registro de cabecera de cuenta

| Posic. | Tipo | Descripción |
| --- | --- | --- |
| 1-2 | Num. | Código registro ‘11’ |
| 3-6 | Num. | Clave de la entidad |
| 7-10 | Num. | Clave de oficina |
| 11-20 | Num. | Nº de cuenta |
| 21-26 | Num. | Fecha inicial (AAMMDD) |
| 27-32 | Num. | Fecha final (AAMMDD) |
| 33-33 | Alf.. | Clave debe o haber del saldo inicial (“D” o “H”) |
| 34-47 | Num. | Importe saldo inicial |
| 48-80 | Alf. | Libre |

2.2 Registro principal de movimientos

| Posic. | Tipo | Descripción |
| --- | --- | --- |
| 1-2 | Num. | Código registro ‘22’ |
| 3-6 | Alf. | Libre |
| 7-10 | Num. | Oficina |
| 11-16 | Num. | Fecha operación (AAMMDD) |
| 17-22 | Num. | Fecha valor (AAMMDD) |
| 23-24 | Num. | Concepto común |
|  |  | 21 – Abono normal |
|  |  | 22 – Abono retroactivo |
|  |  | 23 – Cargo por anulación |
|  |  | 24 – Cargo por abono B.España |
| 25-27 | Alf. | Libre |
| 28-28 | Alf.. | Clave debe o haber (“D” o “H”) |
| 29-42 | Num. | Importe |
| 43-80 | Alf. | Libre |

2.3 Registro final de cuenta

| Posic. | Tipo | Descripción |
| --- | --- | --- |
| 1-2 | Num. | Código registro ‘33’ |
| 3-6 | Num. | Clave entidad |
| 7-10 | Num. | Clave oficina |
| 11-20 | Num. | Nº de cuenta |
| 21-25 | Num. | Nº apuntes Debe |
| 26-39 | Num. | Total importes Debe |
| 40-44 | Num. | Nº apuntes Haber |
| 45-58 | Num. | Total importe Haber |
| 59-59 | Alf.. | Clave debe o haber del saldo final (“D” o “H”) |
| 60-73 | Num. | Saldo final |
| 74-80 | Alf. | Libre |

2.4 Registro de fin de fichero

| Posic. | Tipo | Descripción |
| --- | --- | --- |
| 1-2 | Num. | Código registro ‘88’ |
| 3-20 | Num. | Nueves |
| 21-26 | Num. | Nº total de registros (incluidos los de cabecera de cuenta y fin de fichero) |
| 27-80 | Alf. | Libre |

3. Validaciones

3.1 Tipo de registro 11 (cabecera de cuenta)

Código de registro distinto de 11

Código de entidad incorrecto

Código de oficina incorrecto

Número de cuenta erróneo

Fechas ilógicas

Saldo no numérico

3.2 Tipo de registro 22 (movimientos de la cuenta)

Código de registro distinto 22

Fecha operación ilógica

Fecha valor ilógica

Concepto común distinto de los esperados

Importe no numérico

3.3 Tipo de registro 33 (final de cuenta)

Código de registro distinto de 33

Código de entidad incorrecto

Código de oficina incorrecto

Número de cuenta erróneo

Número apuntes debe erróneo

Importe debe erróneo

Número apuntes haber erróneo

Importe haber erróneo

Saldo final erróneo

3.4 Tipo de registro 88 (final de fichero)

Código de registro distinto de 88

Número de registros erróneo

Rechazo de la transmisión.–Cualquier error detectado en el proceso de validación, ocasionará el rechazo de toda la transmisión.
