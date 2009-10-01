## ANEXO IV

## Ficheros de órdenes de domiciliación de aplazamientos y fraccionamientos: Especificaciones técnicas

## 1. Cabecera Entidad Receptora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 1) |
| --- | --- |
| ENTIDAD RECEPTORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = A) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas(Formato AAAAMMDD) |
| LIBRE | 477 posiciones |

## 2. Cabecera Entidad Colaboradora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 2) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = A) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas(Formato AAAAMMDD) |
| LIBRE | 477 posiciones |

## 3. Cabecera Entidad Colaboradora y vencimiento

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 3) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| TIPO PRESENTACIÓN | 1 posición alfanumérica (Valor = A) |
| NIF AEAT | 9 posiciones alfanuméricas |
| FECHA ENVÍO | 8 posiciones numéricas (Formato AAAAMMDD) |
| FECHA VENCIMIENTO | 8 posiciones numéricas (Formato AAAAMMDD) |
| LIBRE | 469 posiciones |

## 4. Detalle

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 4) |
| --- | --- |
| NÚMERO DE SECUENCIA | 7 posiciones numéricas |
| ORGANISMO EMISOR | 7 posiciones numéricas |
| NIF CONTRIBUYENTE | 9 posiciones alfanuméricas |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL | 40 posiciones alfanuméricas |
| DOMICILIO CONTRIBUYENTE | 40 posiciones alfanuméricas |
| CÓDIGO POSTAL | 5 posiciones numéricas |
| MUNICIPIO | 12 posiciones alfanuméricas |
| NÚMERO DE EXPEDIENTE | 20 posiciones alfanuméricas |
| NÚMERO DE JUSTIFICANTE | 13 posiciones: 12 posiciones numéricas 1 posición alfanumérica |
| CLAVE DE LIQUIDACIÓN | 20 posiciones alfanuméricas |
| NÚMERO DE REFERENCIA | 12 posiciones numéricas |
| CÓDIGO DE PLAZO | 2 posiciones numéricas |
| IMPORTE DEL PLAZO | 13 posiciones num.(11 enteros y 2 decimales) |
| IMPORTE DE LOS INTERESES | 13 posiciones num.(11 enteros y 2 decimales) |
| IMPORTE DE TOTAL A INGRESAR | 13 posiciones num.(11 enteros y 2 decimales) |
| CÓDIGO CUENTA CARGO (CCC) | 20 posiciones numéricas |
| NIF PRESENTADOR/ASESOR | 9 posiciones numéricas |
| NOMBRE/RAZÓN SOCIAL PRESENTADOR | 40 posiciones alfanuméricas |
| FORMA DE PAGO (*) | 1 posición numérica (0=cargo CCC deudor; 1=cargo CCC presentador/colaborador social) |
| LIBRE | 203 posiciones |

## 5. Fin Entidad Colaboradora y vencimiento

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 5) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| NÚMERO TOTAL REGISTROS | 6 posiciones num. (Reg. Tipo 3, 4 y 5) |
| TOTAL IMPORTES A PAGAR | 13 posiciones num. (11 enteros y 2 decimales) |
| LIBRE | 476 posiciones |

## 6. Fin Entidad Colaboradora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 6) |
| --- | --- |
| ENTIDAD COLABORADORA | 4 posiciones numéricas |
| NÚMERO TOTAL REGISTROS | 6 posiciones num.(Reg. Tipo 2, 3, 4, 5 y 6) |
| TOTAL IMPORTES A PAGAR | 13 posiciones num. (11 enteros y 2 decimales) |
| LIBRE | 476 posiciones |

## 7. Fin Entidad Receptora

| TIPO REGISTRO | 1 posición alfanumérica (Valor = 7) |
| --- | --- |
| ENTIDAD RECEPTORA | 4 posiciones numéricas |
| NÚMERO ENTIDADES COLABORADORAS | 2 posiciones numéricas |
| NÚMERO TOTAL REGISTROS | 7 posiciones numéricas (Reg. Tipo 1, 2, 3, 4, 5, 6 y 7) |
| LIBRE | 486 posiciones |

(*) Tendrá el valor «0» mientras no se autorice expresamente la domiciliación en cuentas que no sean de titularidad del deudor.
