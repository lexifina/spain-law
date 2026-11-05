## Artículo segundo. Modificación de la Orden EHA/1658/2009, de 12 de junio, por la que se establecen el procedimiento y las condiciones para la domiciliación del pago de determinadas deudas a través de cuentas abiertas en las entidades de crédito que prestan el servicio de colaboración en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria.

La Orden EHA/1658/2009, de 12 de junio, por la que se establecen el procedimiento y las condiciones para la domiciliación del pago de determinadas deudas a través de cuentas abiertas en las entidades de crédito que prestan el servicio de colaboración en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria, queda modificada como sigue:

Uno. Se modifica el artículo 2, que queda redactado del modo siguiente:

> «Artículo 2. Requisitos de las cuentas designadas para el adeudo de domiciliaciones.

> Las cuentas designadas por los obligados al pago para llevar a cabo el cargo del importe de las deudas domiciliadas deberán cumplir las siguientes condiciones:

> a) Ser de titularidad del obligado al pago. En todo caso, el titular deberá estar identificado en la cuenta mediante un número de identificación proporcionado por la Agencia Estatal de Administración Tributaria.

> En los supuestos en los que la deuda domiciliada corresponda a declaraciones anuales del Impuesto sobre la Renta de las Personas Físicas, será suficiente que la cuenta de domiciliación sea de titularidad de cualquiera de los declarantes.

> En aquellos casos en los que la deuda domiciliada corresponda a una autoliquidación del Impuesto sobre la Renta de no Residentes, modelo 210, la cuenta designada deberá ser de titularidad del obligado tributario o de la persona que realiza la autoliquidación.

> b) Tratarse de una cuenta a la vista o de ahorro que admita la domiciliación de pagos.

> c) Estar abiertas en una Entidad de crédito autorizada para actuar como colaboradora en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria.

> Los obligados a los que se refiere el artículo 35.4 de la Ley 58/2003, de 17 de diciembre, General Tributaria podrán domiciliar el pago de las deudas a las que se refiere el artículo 1 de la presente Orden, siempre que lo contemple el contrato de apertura de la cuenta designada al efecto y ésta reúna todos los requisitos anteriormente enumerados y, en particular, el que se refiere a la titularidad.

> Carecerán de efectos las órdenes de domiciliación en cuentas que no reúnan los requisitos anteriores, por lo que el obligado deberá responder ante la Agencia Estatal de Administración Tributaria de la posible falta de pago o del pago fuera de plazo del importe domiciliado, en los términos que establezca la normativa vigente en cada caso y ello sin perjuicio de la posibilidad de subsanación prevista en los artículos 3 y 4 de la presente Orden respecto de aquellas órdenes de domiciliación que resulten defectuosas.»

Dos. Se modifica el anexo III «Ficheros de órdenes de domiciliación de autoliquidaciones: Especificaciones técnicas», que queda redactado del siguiente modo:

> «ANEXO III

> Ficheros de órdenes de domiciliación de autoliquidaciones: Especificaciones técnicas

> Longitud de registro: 300.

> 1. Cabecera Entidad receptora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 1). |
> | --- | --- |
> | ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | LIBRE. | 277 posiciones alfanuméricas. |

> 2. Cabecera Entidad colaboradora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 2). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | LIBRE. | 277 posiciones alfanuméricas. |

> 3. Cabecera Entidad colaboradora y vencimiento.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 3). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = M). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | FECHA VENCIMIENTO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | LIBRE. | 269 posiciones alfanuméricas. |

> 4. Detalle.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 4). |
> | --- | --- |
> | NIF PRIMER DECLARANTE. | 9 posiciones alfanuméricas. |
> | ANAGRAMA. | 4 posiciones alfanuméricas. |
> | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL PRIMER DECLARANTE. | 40 posiciones alfanuméricas. |
> | NIF SEGUNDO DECLARANTE. | 9 posiciones alfanuméricas. |
> | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL SEGUNDO DECLARANTE. | 40 posiciones alfanuméricas. |
> | CÓDIGO ADMINISTRACIÓN FISCAL. | 5 posiciones numéricas. |
> | MODELO. | 3 posiciones numéricas. |
> | EJERCICIO FISCAL. | 4 posiciones numéricas. |
> | PERÍODO. | 2 posiciones alfanuméricas. |
> | JUSTIFICANTE. | 13 posiciones numéricas. |
> | IMPORTE A PAGAR. | 13 posiciones numéricas (11 enteros y 2 decimales). |
> | IMPORTE TOTAL DECLARACIÓN (*). | 13 posiciones numéricas(11 enteros y 2 decimales). |
> | OPCIÓN FRACCIONAMIENTO (*). | 1 posición numérica (1=no fracciona, 2=fracciona y no domicilia, 3= fracciona y domicilia 2.º plazo). |
> | CÓDIGO CUENTA CARGO (CCC). | 20 posiciones numéricas. |
> | NIF PRESENTADOR/ASESOR. | 9 posiciones alfanuméricas (irá relleno a blancos). |
> | NOMBRE/RAZÓN SOCIAL PRESENTADOR. | 40 posiciones alfanuméricas (irá relleno a blancos). |
> | FORMA DE PAGO (**). | 1 posición numérica (0=cargo CCC obligado tributario; 1=cargo CCC presentador/asesor). |
> | IBAN. | 4 posiciones alfanuméricas. |
> | NRC PREGENERADO INTERNAMENTE POR LA AEAT. | 22 posiciones alfanuméricas. |
> | LIBRE. | 47 posiciones alfanuméricas. |

> (*) Campos que únicamente tienen contenido cuando el modelo sea el 100 (Impuesto sobre la Renta de las Personas Físicas. Declaración anual o borrador de declaración).

> (**) Tendrá el valor "0" mientras no se autorice expresamente la domiciliación en cuentas que no sean de titularidad del obligado al pago.

> 5. Fin entidad colaboradora y vencimiento.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 5). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | NUMERO TOTAL REGISTROS. | 8 posiciones núm. (Registros tipos 3, 4 y 5). |
> | TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | LIBRE. | 274 posiciones alfanuméricas. |

> 6. Fin entidad colaboradora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 6). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | NÚMERO TOTAL REGISTROS. | 8 posiciones numéricas (Registros tipos 2, 3, 4, 5 y 6). |
> | TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | LIBRE. | 274 posiciones alfanuméricas. |

> 7. Fin entidad receptora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 7). |
> | --- | --- |
> | ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
> | NÚMERO ENTIDADES COLABORADORAS. | 2 posiciones numéricas. |
> | NÚMERO TOTAL REGISTROS. | 9 posiciones numéricas (Registros tipos 1, 2, 3, 4, 5, 6 y 7). |
> | LIBRE. | 284 posiciones alfanuméricas.» |

Tres. Se modifica el anexo IV «Ficheros de órdenes de domiciliación de aplazamientos y fraccionamientos: Especificaciones técnicas» que queda redactado del siguiente modo:

> «ANEXO IV

> Ficheros de órdenes de domiciliación de aplazamientos y fraccionamientos: Especificaciones técnicas

> 1. Cabecera entidad receptora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 1). |
> | --- | --- |
> | ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = A). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas(Formato AAAAMMDD). |
> | LIBRE. | 477 posiciones. |

> 2. Cabecera entidad colaboradora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 2). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = A). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas(Formato AAAAMMDD). |
> | LIBRE. | 477 posiciones. |

> 3. Cabecera entidad colaboradora y vencimiento.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 3). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | TIPO PRESENTACIÓN. | 1 posición alfanumérica (Valor = A). |
> | NIF AEAT. | 9 posiciones alfanuméricas. |
> | FECHA ENVÍO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | FECHA VENCIMIENTO. | 8 posiciones numéricas (Formato AAAAMMDD). |
> | LIBRE. | 469 posiciones. |

> 4. Detalle.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 4). |
> | --- | --- |
> | NÚMERO DE SECUENCIA. | 7 posiciones numéricas. |
> | ORGANISMO EMISOR. | 7 posiciones numéricas. |
> | NIF CONTRIBUYENTE. | 9 posiciones alfanuméricas. |
> | APELLIDOS Y NOMBRE O RAZÓN SOCIAL. | 40 posiciones alfanuméricas. |
> | DOMICILIO CONTRIBUYENTE. | 40 posiciones alfanuméricas. |
> | CÓDIGO POSTAL. | 5 posiciones numéricas. |
> | MUNICIPIO. | 12 posiciones alfanuméricas. |
> | NÚMERO DE EXPEDIENTE. | 20 posiciones alfanuméricas. |
> | NÚMERO DE JUSTIFICANTE. | 13 posiciones: 12 posiciones numéricas 1 posición alfanumérica. |
> | CLAVE DE LIQUIDACIÓN. | 20 posiciones alfanuméricas. |
> | NÚMERO DE REFERENCIA. | 12 posiciones numéricas. |
> | CÓDIGO DE PLAZO. | 2 posiciones numéricas. |
> | IMPORTE DEL PLAZO. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | IMPORTE DE LOS INTERESES. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | IMPORTE DE TOTAL A INGRESAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | CÓDIGO CUENTA CARGO (CCC). | 20 posiciones numéricas. |
> | NIF PRESENTADOR/ASESOR. | 9 posiciones numéricas (irá relleno a blancos). |
> | NOMBRE/RAZÓN SOCIAL PRESENTADOR. | 40 posiciones alfanuméricas (irá relleno a blancos). |
> | FORMA DE PAGO (*). | 1 posición numérica (0=cargo CCC deudor; 1=cargo CCC presentador/colaborador social). |
> | IBAN. | 4 posiciones alfanuméricas. |
> | MODELO. | 3 posiciones numéricas (002, 069). |
> | NRC-ONLINE. | 22 posiciones alfanuméricas. |
> | LIBRE. | 174 posiciones. |

> 5. Fin entidad colaboradora y vencimiento.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 5). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | NÚMERO TOTAL REGISTROS. | 6 posiciones núm. (Reg. Tipo 3, 4 y 5). |
> | TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | LIBRE. | 476 posiciones. |

> 6. Fin entidad colaboradora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 6). |
> | --- | --- |
> | ENTIDAD COLABORADORA. | 4 posiciones numéricas. |
> | NÚMERO TOTAL REGISTROS. | 6 posiciones núm.(Reg. Tipo 2, 3, 4, 5 y 6). |
> | TOTAL IMPORTES A PAGAR. | 13 posiciones núm. (11 enteros y 2 decimales). |
> | LIBRE. | 476 posiciones. |

> 7. Fin entidad Receptora.

> | TIPO REGISTRO. | 1 posición alfanumérica (Valor = 7). |
> | --- | --- |
> | ENTIDAD RECEPTORA. | 4 posiciones numéricas. |
> | NÚMERO ENTIDADES COLABORADORAS. | 2 posiciones numéricas. |
> | NÚMERO TOTAL REGISTROS. | 7 posiciones numéricas (Reg. Tipo 1, 2, 3, 4, 5, 6 y 7). |
> | LIBRE. | 486 posiciones. |

> (*) Tendrá el valor "0" mientras no se autorice expresamente la domiciliación en cuentas que no sean de titularidad del obligado al pago.

> El código IBAN (ESXX) irá en las posiciones 298 a la 301 (ambas incluidas).»
