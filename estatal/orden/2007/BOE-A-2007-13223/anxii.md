## ANEXO XII

## PRESENTACIÓN CENTRALIZADA INGRESOS ENTIDADES COLABORADORAS ESPECIFICACIONES TÉCNICAS

1. CARACTERÍSTICAS DE LA CONEXIÓN CON EL D.I.T. PARA INTERCAMBIO TELEMÁTICO DE FICHEROS

1.1) LÍNEA DE COMUNICACIÓN

• Conexión X-25 IBERPAC

• Características:

– Circuito Virtual Conmutado

– Tamaño de paquete: 128

– Tamaño ventana nivel 2: 7

– Tamaño ventana nivel 3: 7

1.2) PROGRAMA DE TRANSFERENCIA DE FICHEROS: EDITRAN ó TAF.

1.3) LONGITUD DE REGISTRO: 90 CARACTERES

2. DISEÑO DE REGISTRO

2.1 DISEÑO DEL REGISTRO DE ENTIDAD TRANSMISORA (TIPO-1).

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 1 = CABECERA ENTIDAD TRANSMISORA |
| 2-5 | NUM. | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 6-6 | ALF. | TIPO DE PRESENTACIÓN |
|  |  | "I" = INGRESOS. |
|  |  | "A" = ANULACIONES |
| 7-7 | ALF. | TIPO DE INGRESOS |
|  |  | "A" = AUTOLIQUIDACIONES |
|  |  | "E" = AUTOLIQUIDACIONES ESPECIALES |
|  |  | "L" = LIQUIDACIONES |
|  |  | “T” = TASAS DEL TESORO |
|  |  | “Z” = TASAS DE ORGANISMOS AUTÓNOMOS |
|  |  | "G” = NRC´S» |
| 8-15 | NUM. | NÚMERO DE QUINCENA (AAAA MM QQ) |
|  |  | • AAAAMM01 para las quincenas que finalicen el 5 del mes |
|  |  | • AAAAMM02 para las quincenas que finalicen el 20 del mes |
| 16-17 | NUM. | DELEGACIÓN AEAT (PRESENTACIÓN CENTRALIZADA = 57) |
| 18-90 | ALF. | FILLER (A BLANCOS) |

2.2 DISEÑO DEL REGISTRO DE CABECERA DE ENTIDAD COLABORADORA (TIPO-2)

| POSIC | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 2 = CABECERA ENTIDAD COLABORADORA |
| 2-5 | NUM. | CÓDIGO DE ENTIDAD COLABORADORA. |
| 6-6 | ALF. | TIPO DE PRESENTACIÓN |
|  |  | "I" = INGRESOS. |
|  |  | "A" = ANULACIONES |
| 7-7 | ALF. | TIPO DE INGRESOS |
|  |  | "A" = AUTOLIQUIDACIONES |
|  |  | "E" = AUTOLIQUIDACIONES ESPECIALES |
|  |  | "L" = LIQUIDACIONES |
|  |  | “T” = TASAS DEL TESORO |
|  |  | “Z” = TASAS DE ORGANISMOS AUTÓNOMOS |
|  |  | “G” = NRC´S |
| 8-15 | NUM. | NÚMERO DE QUINCENA (AAAAMMQQ).AAAAMM01 PARA LAS QUINCENAS QUE FINALICEN EL 5 DEL MES. AAAAMM02 PARA LAS QUINCENAS QUE FINALICEN EL 20. |
| 16-17 | NUM. | DELEGACIÓN AEAT (PRESENTACIÓN CENTRALIZADA = 57) |
| 18-19 | NUM. | NÚMERO DE ORDEN DE LA TRANSMISIÓN.-Será el número que identifique las transmisiones de una E.C. en una quincena. La primera transmisión de la quincena siempre tendrá NÚMERO = 01. Las transmisiones correspondientes a aquellas previamente rechazadas por error no incrementan este contador. Siempre llevarán el número de la transmisión original en que se detectaron los errores. Si en una misma quincena hubiera transmisiones complementarias o sustitutivas de otras previamente aceptadas deberán ir incrementando este número. |
| 20-27 | NUM. | FECHA DE INGRESO (AAAAMMDD). Esta fecha sólo será necesario cumplimentarla en los registros con TIPO INGRESO = A (Autoliquidaciones) |
| 28-90 | ALF. | FILLER (A BLANCOS) |

2.3 DISEÑO DEL REGISTRO DE DETALLE DE AUTOLIQUIDACIONES (TIPO-3)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 3 = DETALLE. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA DEL REGISTRO EN LA E.C. EL PRIMER REGISTRO DE DETALLE TENDRÁ LA SECUENCIA 0000001. |
| 9-13 | NUM. | CÓDIGO DE ADMON. FISCAL DE CONTRIBUYENTE (DDAAA). |
| 14-15 | NUM. | FILLER (00). |
| 16-17 | NUM. | EJERCICIO DE LA AUTOLIQUIDACIÓN. |
| 18-19 | ALF. | PERÍODO DE LA AUTOLIQUIDACIÓN. |
| 20-22 | NUM. | MODELO DE LA AUTOLIQUIDACIÓN. |
| 23-35 | NUM. | NÚMERO DE JUSTIFICANTE DE LA AUTOLIQUIDACIÓN. |
| 36-36 | ALF. | EN BLANCO |
| 37-45 | ALF. | NIF DEL CONTRIBUYENTE. |
| 46-49 | ALF. | TRES LETRAS DEL PRIMER APELLIDO (solo en personas físicas) MAS DÍGITO DE CONTROL. (ANAGRAMA). EN CASO DE ETIQUETAS ANTIGUAS QUE NO INCORPOREN ESTE ANAGRAMA SE DEBERAN GRABAN EN ESTE DATO LOS 4 PRIMEROS CARACTERES DEL PRIMER APELLIDO |
| 50-53 | NUM. | CÓDIGO DE SUCURSAL DEL INGRESO. |
| 54-66 | NUM. | IMPORTE INGRESADO. |
| 67-74 | NUM. | FECHA DEL INGRESO DE LA AUTOLIQUIDACIÓN (AAAAMMDD). |
| 75-86 | ALF. | DATO ESPECIFICO. En los modelos de IRPF (100) la primera posición es el INDICADOR DE FRACCIONAMIENTO. Puede tener tres valores: |
|  |  | 1=No se fracciona el ingreso. |
|  |  | 2=Si se fracciona el ingreso y no se domicilia el segundo pago. |
|  |  | 3=Si se fracciona y el ingreso y si se domicilia el segundo pago. |
|  |  | Si existe fraccionamiento (valores 2 y 3) el resto del campo deberá llevar el importe total a ingresas (partida 99-CUOTA DIFERENCIAL) alineado por la derecha y relleno a ceros por la izquierda. |
| 87-90 | ALF. | FILLER (A BLANCOS) |

2.4 DISEÑO DEL REGISTRO DE SUBTOTALES PARA AUTOLIQUIDACIONES (TIPO-4).

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO 4 = SUBTOTALES. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA DEL REGISTRO. |
| 9-11 | NUM. | MODELO AL QUE CORRESPONDE EL SUBTOTAL. |
| 12-18 | NUM. | CONTADOR TOTAL DE REGISTROS (TIPO-3) DEL MODELO. |
| 19-32 | NUM. | SUMA DE LOS IMPORTES DE LOS REGISTROS DE DETALLE DEL MODELO. |
| 33-90 | ALF. | FILLER (A BLANCOS) |

2.5 DISEÑO DEL REGISTRO DE TOTALES (TIPO-5)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO = 5. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA DEL REGISTRO EN LA TRANSMISIÓN. |
| 9-11 | NUM. | CONTADOR DE REGISTROS DEL TIPO 4. |
| 12-18 | NUM. | CONTADOR TOTAL DE REGISTROS ( 2, 3 ,4 y 5). |
| 19-32 | NUM. | SUMA TOTAL DE LOS IMPORTES DE LOS REGISTROS DE DETALLE DE TODOS LOS MODELOS. |
| 33-36 | NUM. | CODIGO ENTIDAD COLABORADORA |
| 37-90 | ALF. | FILLER (A BLANCOS) |

2.6 DISEÑO DEL REGISTRO FINAL DEL SOPORTE (TIPO 6).

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO = 6. |
| 2-5 | NUM. | CÓDIGO DE LA ENTIDAD TRANSMISORA. |
| 6-7 | NUM. | NÚMERO DE ENTIDADES COLABORADORAS INCLUIDAS EN LA TRANSMISIÓN. |
| 8-14 | ALF. | NÚMERO TOTAL DE REGISTROS TRANSMITIDOS (TIPOS 1, 2, 3, 4, 5 Y 6) |
| 15-90 | ALF. | FILLER (A BLANCOS) |

2.7 DISEÑO DEL REGISTRO DE DETALLE DE INGRESOS DE LIQUIDACIONES PRACTICADAS POR LA ADMINISTRACIÓN (TIPO-3)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO. TIENE EL VALOR 3. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA DEL REGISTRO DE DETALLE, EN LA E.C. EL PRIMER REGISTRO DE DETALLE TENDRA EL VALOR 0000001. |
| 9-11 | NUM. | CÓDIGO DEL MODELO: |
|  |  | 002 = Abonaré A.E.A.T. |
|  |  | 003 = Diligencias de Embargo de Cuentas Bancarias |
|  |  | 004 = Talones de Actas |
|  |  | 008 = Documentos de ingreso asociados a diligencias de embargo |
|  |  | 010 = Documentos de igreso parcial o fuera de plazo |
|  |  | 012 = Abonaré Delegación Economía y Hacienda |
|  |  | 031 = Deudas de comercio exterior |
|  |  | 032 = Liquidaciones R.E.F. de Canarias |
|  |  | 060 = Ingresos de la Caja General de Depósitos |
|  |  | 061 = Cuotas de Derechos Pasivos |
|  |  | 069 = Otros ingresos no tributarios |
| 12-29 | ALF. | CLAVE DEL JUSTIFICANTE DE INGRESO. (ALINEADA POR LA IZQUIERDA) |
|  |  | Configuración: |
|  |  | a) Para modelos 002, 003, 004, 008, 010, 012 : pos. 1-2: Código Delegación (01-56) pos. 3-4: Dos últimas del año de emisión pos. 5-6: Tipo del justificante pos. 7-12: Numérico pos. 13: Carácter de control (*) resto: Blancos |
|  |  | b) Para modelos 031: 1-2: Código de Aduana (01-99) pos. 3-4: Dos últimas del año de emisión pos. 5-6: Tipo del justificante pos. 7-12: Numérico pos. 13: Carácter de control (*) resto: Blancos |
|  |  | c) Para modelos 032: 1-2: Código Delegación (91 ó 92) pos. 3-4: Dos últimas del año de emisión pos. 5-6: Tipo del justificante pos. 7-12: Numérico pos. 13: Carácter de control (*) resto: Blancos |
|  |  | d) Para modelos 060, 061 y 069: pos. 1-12 Numérico pos. 13 Carácter de control (*) resto: Blancos |
| 30-37 | NUM. | FECHA DE INGRESO (AAAAMMDD). |
| 38-50 | NUM. | IMPORTE DEL INGRESO. |
| 51-54 | NUM. | SUCURSAL DEL INGRESO. |
| 55 | ALF. | EN BLANCO |
| 56-64 | ALF. | NIF DEL DEUDOR |
| 65-90 | ALF. | FILLER (A BLANCOS) |

(*) Modelos 002, 004, 010, 012, 031, 032, 060, 061 y 069. El importe del ingreso se suma al número formado por las posiciones 1 a 12. Del número obtenido se calcula el dígito de control con el mismo algoritmo que en el NIF.

Modelos 003 y 008. Del número formado por las posiciones 1 a 12 se calcula el dígito de control con el algoritmo del NIF.

2.8 DISEÑO DEL REGISTRO DE DETALLE DE INGRESOS DE TASAS (TIPO-3)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO. TIENE EL VALOR 3. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA |
| 9-13 | NUM. | FILLER (A CEROS) |
| 14-26 | NUM. | NÚMERO DE JUSTIFICANTE |
| 27-35 | ALF. | NIF |
| 36-64 | ALF. | APELLIDOS Y NOMBRE |
| 65-72 | NUM. | FECHA DEL INGRESO (AAAAMMDD) |
| 73-84 | NUM | IMPORTE |
| 85-88 | NUM | SUCURSAL DEL INGRESO |
| 89-90 | ALF. | FILLER (A BLANCOS) |

2.9 DISEÑO DEL REGISTRO DE DETALLE DE ANULACIONES

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1-1 | NUM. | TIPO DE REGISTRO. TIENE EL VALOR 3. |
| 2-8 | NUM. | NÚMERO DE SECUENCIA |
| 9-30 | ALF. | NRC (NÚMERO DE REFERENCIA COMPLETO) |
| 31-39 | ALF.. | NIF |
| 40-40 | ALF. | TIPO: "I" = INGRESO |
| 41-44 | NUM | EJERCICIO (solo para tipos de ingreso “A” y “E”) |
| 45-46 | NUM. | PERIODO (solo para tipos de ingreso “A” y “E”) |
| 47-59 | NUM | IMPORTE |
| 60-63 | NUM | SUCURSAL DEL INGRESO |
| 64-71 | NUM | FECHA DEL INGRESO (AAAAMMDD) |
| 72-76 | NUM | FECHA DE LA ANULACIÓN (AAAAMMDD) |
| 89-90 | ALF. | FILLER (A BLANCOS) |
