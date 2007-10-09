## ANEXO VII

## GENERACIÓN DEL NRC-NORMAS TÉCNICAS

Generación de claves de cifrado por parte de la AEAT y de las Entidades colaboradoras

Las Entidades colaboradoras deberán emplear procedimientos de cifrado que utilicen el algoritmo DES para realizar funciones MAC (Message Authentication Code), ajustándose a la norma ANSI X9.9, opción 1, para generar códigos de autenticación de mensajes.

La AEAT generará y enviará, mediante el procedimiento que se describe a continuación, una clave privada para cada entidad colaboradora. Para ello:

Utilizando los procedimientos de cifrado mencionados anteriormente, la AEAT generará una clave de cifrado única para cada Entidad colaboradora y la guardará en un fichero cifrado.

La AEAT enviará a cada uno de los responsables designados por la Entidad colaboradora (según lo establecido en la disposición adicional primera) una parte de la clave (16 caracteres en hexadecimal, equivalentes a 8 bytes). La Entidad colaboradora generará, con un programa informático, su correspondiente clave de cifrado de la siguiente forma:

a. Se aplicará un XOR entre las dos partes de la clave, enviadas a los responsables, para obtener como resultado una clave de 8 bytes (clave «en limpio»).

b. La clave obtenida en a) servirá de entrada a los procedimientos de cifrado mencionados anteriormente que, en este caso, permitan obtener, con el algoritmo DES, una clave de cifrado tipo MAC, exclusiva para esa Entidad colaboradora, y guardarla en un fichero cifrado.

c. Una vez generada la clave, se procederá a validarla de la siguiente forma:

– Se utilizará un algoritmo de generación MAC de 4 con salida hexadecimal.

– Los datos de entrada serán:

– La clave recién generada, que se recuperará del fichero cifrado donde se guardó,

– La configuración «00000000» (ocho ceros en código EBCDIC, equivalentes en hexadecimal a: «F0F0F0F0F0F0F0F0»).

La salida obtenida será una «clave de contraste» formada por ocho caracteres hexadecimales. Si esta salida coincide con la clave de contraste enviada por la AEAT a uno de los dos responsables, significará que la generación de la clave de cifrado en esa Entidad ha sido correcta; en caso contrario, la Entidad colaboradora deberá ponerse en comunicación con la AEAT, a través de uno de los teléfonos de contacto que figuran en las cartas enviadas a los responsables

La clave así generada y guardada por la Entidad colaboradora en un fichero cifrado servirá, a partir del momento en que esté validada y contrastada correctamente, para generar en el futuro todos los NRCs entregados a los obligados que realicen, en dicha Entidad, ingresos/solicitudes de devolución dirigidos a la Agencia Estatal de Administración Tributaria.

Generación de la clave de cifrado en la Entidad colaboradora

![imagen](https://www.boe.es/datos/imagenes/disp/2007/163/13223_001.png)

Generación de un NRC (Número de Referencia Completo)

A) AUTOLIQUIDACIONES y AUTOLIQUIDACIONES ESPECIALES (excepto borradores de IRPF):

El NRC se generará a partir de los datos siguientes:

| Número de justificante (Generado por la Entidad) | MMMBBBBNNNNNDC | (14) | Siendo: MMM= Código de modelo BBBB= Código de Banco de España NNNNN= Número secuencial correlativo. D= Dígito de control del justificante C= Carácter de control complementario |
| --- | --- | --- | --- |
| NIF del obligado | XXXXXXXXX | (9) |  |
| Ejercicio fiscal | XX | (2) |  |
| Periodo | XX | (2) |  |
| Tipo de operación | X | (1) | I= Ingreso D= Devolución |
| Importe | XXXXXXXXXXXX | (12) |  |
|  | LONGITUD TOTAL | (40) | DATO DE LA OPERACIÓN |

![imagen](https://www.boe.es/datos/imagenes/disp/2007/163/13223_002.png)

Para generar el NRC es imprescindible que todos estos datos, a incluir en los procedimientos de cifrado, estén en EBCDIC (ver, más adelante, tabla de conversión ASCII, EBCDIC)

| MMM: | Código del modelo correspondiente a la presentación de que se trate |
| --- | --- |
| BBBB: | Código del Banco de España: Cuatro primeros dígitos del C.C.C. |
| NNNNN: | Número secuencial correlativo, comenzando por 00000, por cada código de modelo. Caso de llegar a 99999, se comenzaría por 00000. |

D: Dígito de Control del «MMMBBBBNNNNN», generado con el mismo algoritmo que el actual número de justificante de las autoliquidaciones.

MMMBBBBNNNNND: Conforman el número de justificante que utilizará la Entidad colaboradora para suministrar la información de detalle quincenal.

C: Carácter de control complementario, generado aplicando un algoritmo que será facilitado a una de las personas designadas por la Entidad colaboradora. Sólo se utilizará para el NRC.

NIF: NIF del obligado.

Ejercicio fiscal: Dos últimos dígitos del ejercicio fiscal al que corresponda la presentación.

Periodo : Los valores válidos correspondientes a presentaciones mensuales son: 01, 02, 03 ....,12. Para presentaciones trimestrales: 1T, 2T, 3T y 4T. Para presentaciones anuales o aperiódicas: 0A.

Tipo de autoliquidación: “I” para ingresos y “D” para solicitudes de devolución.

Importe: Se indicará la cifra (un número entero), ajustada a la derecha y rellena con ceros a la izquierda, hasta completar las 12 posiciones. Se expresará en céntimos de euro, para evitar el uso de decimales.”

Tabla de conversión ASCII/EBCDIC

| Denominación del carácter | Codificación hexadecimal |
| --- | --- |
| ASCII | EBCDIC |
| Espacio en blanco | 20 | 40 |
| A | 41 | C1 |
| B | 42 | C2 |
| C | 43 | C3 |
| D | 44 | C4 |
| E | 45 | C5 |
| F | 46 | C6 |
| G | 47 | C7 |
| H | 48 | C8 |
| I | 49 | C9 |
| J | 4A | D1 |
| K | 4B | D2 |
| L | 4C | D3 |
| M | 4D | D4 |
| N | 4E | D5 |
| O | 4F | D6 |
| P | 50 | D7 |
| Q | 51 | D8 |
| R | 52 | D9 |
| S | 53 | E2 |
| T | 54 | E3 |
| U | 55 | E4 |
| V | 56 | E5 |
| W | 57 | E6 |
| X | 58 | E7 |
| Y | 59 | E8 |
| Z | 5A | E9 |
| 0 | 30 | F0 |
| 1 | 31 | F1 |
| 2 | 32 | F2 |
| 3 | 33 | F3 |
| 4 | 34 | F4 |
| 5 | 35 | F5 |
| 6 | 36 | F6 |
| 7 | 37 | F7 |
| 8 | 38 | F8 |
| 9 | 39 | F9 |

B) LIQUIDACIONES PRACTICADAS POR LA ADMINISTRACIÓN:

Las normas técnicas de generación del NRC para los documentos de ingreso expedidos por la Administración son las indicadas anteriormente para autoliquidaciones y autoliquidaciones especiales, con la peculiaridad de que para los mismos la estructura del NRC se genera a partir de los datos siguientes:

B.1) Para modelos 002, 004, 008, 010, 031 y 032:

| Número de justificante (Asignado por la AEAT y último carácter de control calculado por la Entidad colaboradora) | DDAATTNNNNNNDC | (14) | Siendo: DD= Delegación o Aduana AA= Ejercicio TT= Tipo. NNNNNN= Número secuencial D= Carácter de control (calculado por la AEAT) C= Carácter de control complementario (calculado por la Entidad colaboradora) |
| --- | --- | --- | --- |
| NIF del deudor | XXXXXXXXX | (9) |  |
| Importe ingresado | XXXXXXXXXXXXX | (13) |  |
| Fecha de ingreso | AAAAMMDD | (8) |  |
| Código Banco de España | XXXX | (4) | Código de la Entidad colaboradora en la que se realiza el ingreso |
|  | LONGITUD TOTAL | (48) | DATO DE LA OPERACIÓN |

B.2) Para modelos 060, 061 y 069:

| Número dejustificante | NNNNNNNNNNNNDC | (14) | Siendo: NNNNNNNNNNNN= Número secuencial D= Carácter de control (calculado por la AEAT) C= Carácter de control complementario (calculado por la Entidad colaboradora) |
| --- | --- | --- | --- |
| NIF del deudor | XXXXXXXXX | (9) |  |
| Importe ingresado | XXXXXXXXXXXXX | (13) |  |
| Fecha de ingreso | AAAAMMDD | (8) |  |
| Código Banco de España | XXXX | (4) | Código de la Entidad colaboradora en la que se realiza el ingreso |
|  | LONGITUD TOTAL | (48) | DATO DE LA OPERACIÓN |

![imagen](https://www.boe.es/datos/imagenes/disp/2007/163/13223_003.png)

Para generar el NRC es imprescindible que todos estos datos, a incluir en los procedimientos de cifrado, estén en EBCDIC y que se sigan las normas genéricas respecto al NIF, al importe ingresado y al carácter 14 del justificante.

D: Carácter de control generado por la Administración para cada justificante de ingreso.

C: Carácter de control complementario generado aplicando el algoritmo facilitado a las Entidades colaboradoras junto con la clave privada de cifrado.

C) TASAS DE DEPARTAMENTOS MINISTERIALES Y ORGANISMOS PÚBLICOS.

Las normas técnicas de generación del NRC para los documentos de ingreso de tasas (modelos 790, 791, 990 y 991) son las indicadas anteriormente para liquidaciones practicadas por la AEAT, con la peculiaridad de que para los mismos la estructura del NRC se genera a partir de los datos siguientes:

| Número de justificante (Último carácter de control calculado por la Entidad colaboradora) | MMMTTTSSSSSSDC | (14) | Siendo: MMM= Código de modelo TTT= Código de tasa SSSSSS= Número secuencial D= Carácter de control. C= Carácter de control complementario (calculado por la Entidad colaboradora) |
| --- | --- | --- | --- |
| NIF del deudor | XXXXXXXXX | (9) |  |
| Importe ingresado | XXXXXXXXXXXXX | (13) |  |
| Fecha de ingreso | AAAAMMDD | (8) |  |
| Código Banco de España | XXXX | (4) | Código de la Entidad colaboradora en la que se realiza el ingreso |
|  | LONGITUD TOTAL | (48) | DATO DE LA OPERACIÓN |

![imagen](https://www.boe.es/datos/imagenes/disp/2007/163/13223_004.png)

D) BORRADORES DEL I.R.P.F.:

El NRC se generará a partir de los datos siguientes:

| Número de referencia (Asignado por la AEAT y último carácter de control calculado por la Entidad colaboradora) | MMMANNNNNNSSDC | (14) | Siendo: MMM= Código de modelo A= Código indicador del año NNNNNN= Número secuencial SS= Dígitos seguridad D= Dígito de control. C= Carácter de control complementario (calculado por la Entidad colaboradora) |
| --- | --- | --- | --- |
| NIF del sujeto pasivo | XXXXXXXXX | (9) |  |
| Ejercicio | AA | (2) |  |
| Período | 0A | (2) |  |
| Tipo de autoliquidación | X | (1) | I: ingreso, D: Devolución |
| Importe ingresado o solicitado a devolver | XXXXXXXXXXXXX | (13) | En la misma moneda en que esté denominada la cuenta restringida |
| Código Banco de España | XXXX | (4) | Código de la Entidad colaboradora en la que se realiza el ingreso |
| Fecha de confirmación del Borrado | AAAAMMDD | (8) |  |
| Reservado | 000 | (3) | Tres ceros |
|  | LONGITUD TOTAL | (56) | DATO DE LA OPERACIÓN |

![imagen](https://www.boe.es/datos/imagenes/disp/2007/163/13223_005.png)
