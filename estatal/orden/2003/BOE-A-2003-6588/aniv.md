## ANEXO IV

## Registro de comunicación del NRC

| N.º | Pos. | Long. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de Operación (007) |
| 2 | 4 | 2 | An | Alta (01), Consulta (02) |
| 3 | 6 | 3 | N | Ceros |
| 4 | 9 | 2 | N | Ceros |
| 5 | 11 | 2 | An | Espacios en blanco |
| 6 | 13 | 1 | An | Tipo de moneda de la declaración (E) |
| 7 | 14 | 1 | An | Tipo de autoliquidación (I) |
| 8 | 15 | 9 | An | N.I.F. del contribuyente (XNNNNNNNX) = campo 1 |
| 9 | 24 | 4 | An | Espacios en blanco |
| 10 | 28 | 5 | N | Ceros |
| 11 | 33 | 12 | N | Importe del ingreso (ajustado a la dcha. y relleno de ceros a la izda.) |
| 12 | 45 | 13 | An | Número de justificante |
| 13 |
| 14 | 58 | 20 | N | Código Cuenta Cliente |
| 15 | 78 | 12 | N | Importe en la moneda en que esté denominada la Cuenta Restringida del abono. |
| 16 | 90 | 8 | N | Fecha de la operación (AAAAMMDD) |
| 17 | 98 | 22 | An | Número de Referencia Completo (MMMMSSSSSSCOXXXXXXXX) |
| 18 | 120 | 2 | An | Código de retorno |
| 19 | 122 | 89 | N | Reservado para posibles ampliaciones |
| 20 | 211 | 189 | An | Explicación del horario (para error 86 y 87) |
