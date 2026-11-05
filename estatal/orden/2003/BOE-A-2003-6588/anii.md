## ANEXO II

## Registro de datos reenviados por la A.E.A.T.

| N.º | Pos. |  | Long. | Tipo |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF (XNNNNNNNX) del titular de la cuenta y del certificado de firma electrónica |
| 2 | 10 | 6 | N | Fecha AAMMDD |
| 3 | 16 | 10 | N | Hora HHMMSSSSSS |
| 4 | 26 | 3 | An | Tipo de Operación (007) |
| 5 | 29 | 2 | An | Alta (01), Consulta (02) |
| 6 | 31 | 3 | N | Ceros |
| 7 | 34 | 2 | N | Ceros |
| 8 | 36 | 2 | An | Espacios en blanco |
| 9 | 38 | 1 | An | Tipo de moneda de la declaración (E) |
| 10 | 39 | 1 | An | Tipo de autoliquidación (I) |
| 11 | 40 | 9 | An | N.I.F. del contribuyente (XNNNNNNNX) = campo 1 |
| 12 | 49 | 5 | N | Ceros |
| 13 | 54 | 12 | N | Importe del ingreso (ajustado a la dcha. y relleno de ceros a la izda. |
| 14 15 | 66 | 13 | An | Número de justificante |
| 16 | 79 | 20 | N | Código Cuenta Cliente |
| 17 | 99 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 18 | 111 | 9 | An | N.I.F. del Representante 1 o espacios en blanco |
| 19 | 120 | 9 | An | N.I.F. del Representante 2 o espacios en blanco |
| 20 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado |
| 21 | 145 | 4 | An | Espacios en blanco |
| 22 | 149 | 40 | An | Apellidos y Nombre o Razón Social del contribuyente |
| 23 | 189 | 40 | An | Apellidos y Nombre del Representante 1 o espacios en blanco |
| 24 | 229 | 40 | An | Apellidos y Nombre del Representante 2 o espacios en blanco |
| 25 | 269 | 100 | An | ACTION completo de la EE.CC. que acepta peticiones de NRC, que debe empezar por https: |
| 26 | 369 | 4 | An | Método del formulario (POST) |
| 27 | 373 | 25 | An | Variables y valores a enviar al comienzo (opcional) |

El MAC de 8 será generado a partir de las datos de las 120 primeras posiciones. Los importes se expresan en céntimos de Euros.
