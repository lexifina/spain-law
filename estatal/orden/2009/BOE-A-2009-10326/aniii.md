## ANEXO III

## Ficheros de órdenes de domiciliación de autoliquidaciones: Especificaciones técnicas

## 1. Cabecera Entidad Receptora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 1) |
| --- | --- |
| ENTIDAD RECEPTORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = M) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas(Formato AAAAMMDD) |
| LIBRE | 227 posiciones alfanuméricas |

## 2. Cabecera Entidad Colaboradora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 2) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = M) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas(Formato AAAAMMDD) |
| LIBRE | 227 posiciones alfanuméricas |

## 3. Cabecera Entidad Colaboradora y vencimiento

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 3) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = M) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas(Formato AAAAMMDD) |
| FECHA VENCIMIENTO | 8 posiciones numéricas(Formato AAAAMMDD) |
| LIBRE | 219 posiciones alfanuméricas |

## 4. Detalle

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 4) |
| --- | --- |
| NIF PRIMER DECLARANTE | 9 posiciones alfanuméricas |
| ANAGRAMA | 4 posiciones alfanuméricas |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL PRIMER DECLARANTE | 40 posiciones alfanuméricas |
| NIF SEGUNDO DECLARANTE | 9 posiciones alfanuméricas |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL SEGUNDO DECLARANTE | 40 posiciones alfanuméricas |
| CÓDIGO ADMINISTRACIÓN FISCAL | 5 posiciones numéricas |
| MODELO | 3 posiciones numéricas |
| EJERCICIO FISCAL | 4 posiciones numéricas |
| PERÍODO | 2posiciones alfanuméricas. |
| JUSTIFICANTE | 13 posiciones numéricas |
| IMPORTE A PAGAR | 13 posiciones numéricas (11 enteros y 2 decimales) |
| IMPORTE TOTAL DECLARACIÓN (*) | 13 posiciones numéricas(11 enteros y 2 decimales) |
| OPCIÓN FRACCIONAMIENTO (*) | 1 posición numérica (1=no fracciona, 2=fracciona y no domicilia, 3= fracciona y domicilia 2º plazo) |
| CÓDIGO CUENTA CARGO (CCC) | 20 posiciones numéricas |
| NIF PRESENTADOR/ASESOR | 9 posiciones alfanuméricas |
| NOMBRE/RAZÓN SOCIAL PRESENTADOR | 40 posiciones alfanuméricas |
| FORMA DE PAGO (**) | 1 posición numérica (0=cargo CCC obligado tributario; 1=cargo CCC presentador/asesor) |
| LIBRE | 23 posiciones alfanuméricas |

## 5. Fin Entidad Colaboradora y vencimiento

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 5) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| NUMERO TOTAL REGISTROS | 6 posiciones num. (Registros tipos 3, 4 y 5) |
| TOTAL IMPORTES A PAGAR | 13 posiciones num. (11 enteros y 2 decimales) |
| LIBRE | 226 posiciones alfanuméricas |

## 6. Fin Entidad Colaboradora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 6) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| NÚMERO TOTAL REGISTROS | 6 posiciones numéricas (Registros tipos 2, 3, 4, 5 y 6) |
| TOTAL IMPORTES A PAGAR | 13 posiciones num. (11 enteros y 2 decimales) |
| LIBRE | 226 posiciones alfanuméricas |

## 7. Fin Entidad Receptora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 7) |
| --- | --- |
| ENTIDAD RECEPTORA | 4 posiciones numéricas |
| NÚMERO ENTIDADES COLABORADORAS | 2 posiciones numéricas |
| NÚMERO TOTAL REGISTROS | 7 posiciones numéricas (Registros tipos 1, 2, 3, 4, 5, 6 y 7) |
| LIBRE | 236 posiciones alfanuméricas |

(*) Campos que únicamente tienen contenido cuando el modelo sea el 100 (Impuesto sobre la Renta de las Personas Físicas. Declaración anual o borrador de declaración).

(**) Tendrá el valor «0» mientras no se autorice expresamente la domiciliación en cuentas que no sean de titularidad del obligado al pago.
