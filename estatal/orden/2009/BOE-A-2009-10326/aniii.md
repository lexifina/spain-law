## ANEXO III

## Ficheros de órdenes de domiciliación de autoliquidaciones: Especificaciones técnicas

Longitud de registro: 300.

1. Cabecera Entidad receptora.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 1). |
| --- | --- |
| ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
| TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
| NIF AEAT. | 9 posiciones alfanuméricas. |
| FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
| LIBRE. | 277 posiciones alfanuméricas. |

2. Cabecera Entidad colaboradora.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 2). |
| --- | --- |
| ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
| TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
| NIF AEAT. | 9 posiciones alfanuméricas. |
| FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
| LIBRE. | 277 posiciones alfanuméricas. |

3. Cabecera Entidad colaboradora y vencimiento.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 3). |
| --- | --- |
| ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
| TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
| NIF AEAT. | 9 posiciones alfanuméricas. |
| FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
| FECHA VENCIMIENTO. | 8 posiciones numéricas (Formato AAAAMMDD). |
| LIBRE. | 269 posiciones alfanuméricas. |

4. Detalle.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 4). |
| --- | --- |
| NIF PRIMER DECLARANTE. | 9 posiciones alfanuméricas. |
| ANAGRAMA. | 4 posiciones alfanuméricas. |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL PRIMER DECLARANTE. | 40 posiciones alfanuméricas. |
| NIF SEGUNDO DECLARANTE. | 9 posiciones alfanuméricas. |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL SEGUNDO DECLARANTE. | 40 posiciones alfanuméricas. |
| CÓDIGO ADMINISTRACIÓN FISCAL. | 5 posiciones numéricas. |
| MODELO. | 3 posiciones numéricas. |
| EJERCICIO FISCAL. | 4 posiciones numéricas. |
| PERÍODO. | 2 posiciones alfanuméricas. |
| JUSTIFICANTE. | 13 posiciones numéricas. |
| IMPORTE A PAGAR. | 13 posiciones numéricas (11 enteros y 2 decimales). |
| IMPORTE TOTAL DECLARACIÓN (*). | 13 posiciones numéricas(11 enteros y 2 decimales). |
| OPCIÓN FRACCIONAMIENTO (*). | 1 posición numérica (1=no fracciona, 2=fracciona y no domicilia, 3= fracciona y domicilia 2.º plazo). |
| CÓDIGO CUENTA CARGO (CCC). | 20 posiciones numéricas. |
| NIF PRESENTADOR/ASESOR. | 9 posiciones alfanuméricas (irá relleno a blancos). |
| NOMBRE/RAZÓN SOCIAL PRESENTADOR. | 40 posiciones alfanuméricas (irá relleno a blancos). |
| FORMA DE PAGO (**). | 1 posición numérica (0=cargo CCC obligado tributario; 1=cargo CCC presentador/asesor). |
| IBAN. | 4 posiciones alfanuméricas. |
| NRC PREGENERADO INTERNAMENTE POR LA AEAT. | 22 posiciones alfanuméricas. |
| LIBRE. | 47 posiciones alfanuméricas. |

(*) Campos que únicamente tienen contenido cuando el modelo sea el 100 (Impuesto sobre la Renta de las Personas Físicas. Declaración anual o borrador de declaración).

(**) Tendrá el valor "0" mientras no se autorice expresamente la domiciliación en cuentas que no sean de titularidad del obligado al pago.

5. Fin entidad colaboradora y vencimiento.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 5). |
| --- | --- |
| ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
| NUMERO TOTAL REGISTROS. | 8 posiciones núm. (Registros tipos 3, 4 y 5). |
| TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
| LIBRE. | 274 posiciones alfanuméricas. |

6. Fin entidad colaboradora.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 6). |
| --- | --- |
| ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
| NÚMERO TOTAL REGISTROS. | 8 posiciones numéricas (Registros tipos 2, 3, 4, 5 y 6). |
| TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
| LIBRE. | 274 posiciones alfanuméricas. |

7. Fin entidad receptora.

| TIPO REGISTRO. | 1 posición alfanumérica (Valor = 7). |
| --- | --- |
| ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
| NÚMERO ENTIDADES COLABORADORAS. | 2 posiciones numéricas. |
| NÚMERO TOTAL REGISTROS. | 9 posiciones numéricas (Registros tipos 1, 2, 3, 4, 5, 6 y 7). |
| LIBRE. | 284 posiciones alfanuméricas. |

> Se modifica por el art. 2.2 de la Orden HFP/915/2021, de 1 de septiembre. Ref. BOE-A-2021-14453#as

> Téngase en cuenta para su aplicación la disposición final 3.a) de la citada Orden. Ref. BOE-A-2021-14453#df-3

> Se modifican los apartados 5 a 7 por el art. 2 de la Orden HAC/785/2020, de 21 de julio. Ref. BOE-A-2020-9552#as

> Esta modificación no será de aplicación hasta el 1 de septiembre de 2020, según establece la disposición final de la citada Orden.

> Se modifica por el art. único.8 de la Orden HAC/350/2019, de 5 de marzo. Ref. BOE-A-2019-4493
