## ANEXO IX

## COMUNICACIÓN SALDOS CUENTAS RESTRINGIDAS TESORO PÚBLICO ESPECIFICACIONES TÉCNICAS

1. CARACTERÍSTICAS DE LA CONEXIÓN CON EL D.I.T. PARA INTERCAMBIO TELEMÁTICO DE FICHEROS

1) LÍNEA DE COMUNICACIÓN

Conexión X-25 IBERPAC

Características:

• Circuito Virtual Conmutado

• Tamaño de paquete: 128

• Tamaño ventana nivel 2:1 a 7 (se recomienda 7)

• Tamaño ventana nivel 3:1 a 7 (se recomienda 7)

2) PROGRAMA DE TRANSFERENCIA DE FICHEROS

EDITRAN ó TAF

3) LONGITUD DE REGISTRO:

58 CARACTERES

2. DISEÑO DE REGISTROS

2.1 DISEÑO DE REGISTRO ENTIDAD TRANSMISORA (TIPO-1)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1 - 1 | NUM. | TIPO DE REGISTRO 1 = CABECERA ENT. TRANSMISORA |
| 2 - 5 | NUM. | CÓDIGO DE ENTIDAD TRANSMISORA |
| 6 - 13 | NUM. | NÚMERO DE QUINCENA (AAAA MM QQ) |
|  |  | * AAAAMM01 para las quincenas que finalicen el 5 del mes |
|  |  | * AAAAMM02 para las quincenas que finalicen el 20 del mes |
| 14 - 58 | ALF. | FILLER (A BLANCOS) |

2.2 DISEÑO DE REGISTRO DE ENTIDAD COLABORADORA (TIPO-2)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1 - 1 | NUM. | TIPO DE REGISTRO 2 = CABECERA ENT. COLABORADORA |
| 2 - 5 | NUM. | CÓDIGO DE ENTI-DAD COLABORADORA |
| 6 - 13 | NUM. | NÚMERO DE QUINCENA (AAAAMMQQ) |
| 14 - 58 | ALF. | FILLER (A BLANCOS) |

2.3 DISEÑO DE REGISTRO DE DETALLE (TIPO-3)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1 - 1 | NUM. | TIPO DE REGISTRO 3 = DETALLE SALDO |
| 2 - 3 | NUM. | DELEGACIÓN A LA QUE CORRESPONDE LA CUENTA (PRESENTACIÓN CENTRALIZADA=57) |
| 4 - 11 | NUM. | NÚMERO DE QUINCENA (AAAAMMQQ) |
| 12 - 12 | ALF. | TIPO DE INGRESOS: |
|  |  | "A" = AUTOLIQUIDACIONES |
|  |  | "E" = AUTOLIQUID. ESPECIALES |
|  |  | "L" = LIQUIDACIONES (S.I.R.) |
| 13 - 27 | NUM. | SALDO DE LA CUENTA RESTRINGIDA AL DIA DE LA FECHA DEL FIN DE LA QUINCENA |
| 28 - 47 | NUM. | NÚMERO DE LA CUENTA RESTRINGIDA |
| 48 - 55 | NUM. | FECHA VENCIMIENTO QUINCENA (AAAAMMDD) |
| 56 - 58 | ALF. | FILLER (A BLANCOS) |

2.4 DISEÑO DE REGISTRO DE TOTALES E.C. (TIPO-4)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1 - 1 | NUM. | TIPO DE REGISTRO 4 = TOTALES E.C. |
| 2 - 5 | NUM. | CÓDIGO DE ENTI-DAD COLABORADORA |
| 6 - 13 | NUM. | NÚMERO DE QUINCENA (AAAAMMQQ) |
| 14 - 29 | NUM. | SUMATORIO DE SALDOS DE LA E.C. |
| 30 - 58 | ALF. | FILLER (A BLANCOS) |

2.5 DISEÑO DE REGISTRO DE TOTALES ENTIDAD TRANSMISORA (TIPO-5-)

| POSIC. | TIPO | DESCRIPCIÓN |
| --- | --- | --- |
| 1 - 1 | NUM. | TIPO DE REGISTRO 5 = TOTALES ENT. TRANSMISORA |
| 2 - 5 | NUM. | CÓDIGO DE ENTIDAD TRANSMISORA |
| 6 - 13 | NUM. | NÚMERO DE QUINCENA (AAAAMMQQ) |
| 14 - 16 | NUM | NÚMERO DE ENTIDADES COLABORADORAS INCLUIDAS EN LA TRANSMISIÓN |
| 17 - 22 | NUM. | NÚMERO TOTAL DE REGISTROS TRANSMITIDOS (TIPOS 1, 2, 3, 4 y 5) |
| 23 - 58 | ALF. | FILLER (A BLANCOS) |

3. VALIDACIONES

3.1 TIPO DE REGISTRO 1 (ENTIDAD TRANSMISORA)

• Tipo de registro distinto de 1

• Código de Entidad Transmisora no es un código válido

• Número de la quincena no se ajusta al formato.

• Número de la quincena es superior a la fecha de transmisión.

3.2 TIPO DE REGISTRO 2 (ENTIDAD COLABORADORA)

• Tipo de registro distinto de 2

• Código de Entidad Colaboradora no es un código válido

• Número de quincena no coincide con el de la Entidad Transmisora

3.3 TIPO DE REGISTRO 3 (DETALLE)

• Tipo de registro distinto de 3

• Delegación no válida (distinta de 57)

• Número de quincena no coincide con el de la Entidad Transmisora

• La información ha sido ya aceptada en una transmisión previa

• La presentación de la información no es correlativa

• Tipo de ingreso no es uno de los tres válidos, o está repetido

• Número de cuenta no es correcto.

• Fecha de vencimiento de quincena ilógica

• Falta alguna de las cuentas restringidas.

3.4 TIPO DE REGISTRO 4 (TOTALES E.C.)

• Tipo de registro distinto de 4

• Código de E.C. no coincide con el del tipo de registro 2

• Número de quincena no coincide con el de la Entidad Transmisora

• Saldo total por E.C. no coincide con la suma de los saldos de detalle

3.5 TIPO DE REGISTRO 5 (TOTALES ENTIDAD TRANSMISORA)

• Tipo de registro distinto de 5

• Código de Entidad Transmisora no coincide con el del tipo de registro 1

• Número de quincena no coincide con el de cabecera de la Entidad Transmisora

• Número de EE.CC. no coincide con las incluidas en la transmisión.

• Número total de registros no coincide con los registros incluidos en la transmisión.

RECHAZO DE LA TRANSMISIÓN

• Se rechazará toda la transmisión cuando se detecten errores en los registros 1 ó 5.

• Se rechazará solamente la información relativa a la Entidad colaboradora si el error se detecta en los registros de tipo 2, 3 ó 4. (Por tanto en caso de una transmisión efectuada por una Entidad transmisora que contenga varias Entidades colaboradoras el rechazo solo afectará a la Entidad o Entidades en las que se detecten los errores citados).

NOTAS:

1. Todas las Entidades colaboradoras deberán transmitir información en todas y cada una de las quincenas y en los tres tipos de ingreso Autoliquidaciones, Autoliquidaciones Especiales y Liquidaciones, incluso cuando en el período tratado no hayan recibido ingresos, en cuyo caso el saldo transmitido sería cero.

2. La validación de la información con la de los ingresos individuales no se verá afectada por la transmisión efectuada, ya que el cuadre del fichero se hará contra las órdenes de transferencia recibidas.

## ANEXO IX

CLAVE ENTIDAD: .......................... DENOMINACIÓN ENTIDAD.........................

QUINCENA: (AAAA-MM-NN) FECHA VENCIMIENTO: .............................

(NN representa el numero de quincena, será 01 si el saldo corresponde a la primera quincena y 02 si corresponde a la segunda)

SALDOS DE CUENTAS RESTRINGIDAS (COMUNICACIÓN MANUAL)

|  | CÓDIGO 021 | CÓDIGO 022 | CÓDIGO 023 | TOTAL SALDOS |
| --- | --- | --- | --- | --- |
| SALDO |  |  |  |  |

CÓDIGO 021= Saldo cuenta restringida de Autoliquidaciones.

CÓDIGO 022= Saldo cuenta restringida de Autoliquidaciones Especiales.

CÓDIGO 023= Saldo cuenta restringida de Liquidaciones practicadas por la Administración.
