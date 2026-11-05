## ANEXO I

## Especificaciones técnicas sobre los procesos de transmisión centralizada de diligencias de embargo de cuentas bancarias, recepción de las trabas y comunicación de resultados (EDITRAN)

1. Descripción general del procedimiento

El intercambio de información mediante EDITRAN entre el Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (D.I.T.) y las Entidades de crédito para el embargo de cuentas bancarias repite todos los meses un ciclo del tipo:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/311/20269_001.png)

Las diligencias, las trabas y los resultados de validación de las mismas pertenecientes a un mismo ciclo se identifican por una fecha. El campo que contiene esta fecha en todos los ficheros recibe el nombre de FECHA DE COMIENZO DE CICLO.

Cada Entidad de crédito utilizará una Entidad Transmisora para el intercambio de información. Una Entidad transmisora podrá dar servicio a varias Entidades de crédito, con la restricción de que para un mismo ciclo todas las transmisiones correspondientes a una Entidad de crédito (diligencias, trabas y resultado de validación de trabas) se realizarán a través de la misma Entidad Transmisora.

Las diligencias correspondientes a una Entidad de crédito que se transmiten a una Entidad Transmisora en un mismo fichero se agrupan en lo que en este documento se denomina «envío», que queda identificado por los campos CÓDIGO DE ENTIDAD DE CRÉDITO y NÚMERO DE ENVÍO. En consecuencia, un fichero de diligencias puede contener envíos correspondientes a distintas Entidades de crédito, cuya numeración será independiente.

En las transmisiones en las que el origen de la información sea el D.I.T. (diligencias y resultados de validación) el último registro del fichero transmitido será un registro de control, cuya estructura será similar tanto si se transmiten diligencias como si se transmiten resultados de validación; sin embargo, habrá diferencias en el contenido de los campos, según se detalla más adelante en este documento. Este registro de control no existirá en el fichero de trabas, transmitido por las Entidades al D.I.T.

Sea cual sea el origen de la información, la iniciativa de la comunicación corresponderá a las Entidades Transmisoras, en las fechas y plazos que se indican en este documento. La recepción por parte de estas Entidades de los ficheros con origen en el D.I.T. supone el borrado de los mismos y su sustitución por un fichero con un único registro de control, que indica que se ha realizado dicha recepción.

De esta forma, la Entidad Transmisora siempre tendrá a su disposición un registro con los datos de estado del ciclo, evitando la posibilidad de que se recupere un fichero vacío, en caso de que la Entidad Transmisora intente una nueva recepción en ese ciclo, o en el caso de que no hubiera diligencias para la Entidad en ciclos sucesivos.

1.1. Fases de un ciclo.

Se describen a continuación las tres transmisiones que forman parte del procedimiento de intercambio de información para embargo de cuentas:

| Información Transmitida | Origen de la información | Destino de la información |
| --- | --- | --- |
| Diligencias de embargo. | D.I.T. | Entidades. |
| Trabas. | Entidades. | D.I.T. |
| Resultados de validación. | D.I.T. | Entidades. |

1.1.1 Transmisión a las entidades de diligencias de embargo de cuentas.

El último día de cada mes, o el inmediato hábil posterior, el D.I.T. generará un fichero por Entidad Transmisora con los envíos de diligencias de embargo de cuentas para aquellas Entidades de crédito a la que aquélla dé servicio y en ese ciclo tuvieran diligencias.

Este fichero estará disponible para su recuperación por las Entidades Transmisoras durante los dos DÍAS HÁBILES SIGUIENTES al día de su generación.

El horario para la transmisión será:

– De lunes a jueves, desde las 08,00 a las 20,00 horas.

– Los viernes, desde las 08,00 hasta las 15,00 horas.

Cada fichero mensual de diligencias de una Entidad Transmisora contendrá diligencias de embargo de al menos una Entidad de crédito. Cada Entidad Transmisora deberá comprobar, en los días y horas especificados, si existe el fichero de diligencias de embargo de cuentas disponible para ser recuperado. Aquellas Entidades Transmisoras para las que no existan diligencias en un ciclo encontrarán el registro de control correspondiente al último ciclo finalizado.

1.1.2 Transmisión de las trabas de cuentas bancarias desde las entidades al departamento de informática tributaria.

EN EL PLAZO DE CUATRO DÍAS HÁBILES, contados a partir de la fecha de recepción del fichero de diligencias de embargo de cuentas, cada Entidad Transmisora transmitirá al D.I.T. el fichero con las trabas realizadas.

La Entidad Transmisora deberá transmitir las trabas realizadas por cada Entidad de crédito en el momento que las tenga disponibles, sin esperar a tener las de todas las Entidades de las que sea transmisora, ya que el tratamiento de cada una de ellas es independiente y los resultados de validación pueden ser diferentes para una Entidad de crédito que para otras. De este modo podrán procesarse con mayor agilidad los posibles rechazos de trabas de las Entidades de crédito afectadas. En cualquier caso, en el plazo de cuatro días deberán haber sido transmitidas la totalidad de las trabas de todas las Entidades de crédito tratadas por una Entidad Transmisora.

1.1.3 Transmisión a las entidades del resultado de la validación de las trabas.

El D.I.T. pondrá a disposición de las Entidades Transmisoras el resultado de la validación de las trabas dentro de los dos días hábiles siguientes a la recepción del fichero que contiene las trabas, tanto si éste es correcto (envío aceptado), como si es incorrecto (envío rechazado).

Si la Entidad Transmisora da servicio a varias Entidades de crédito y transmite al D.I.T. trabas sólo de algunas de ellas, el D.I.T. podrá responder con el resultado de la validación de estas trabas, sin esperar a recibir las del resto de Entidades de crédito. En el caso de que la Entidad Transmisora no recoja el fichero de resultados de la validación antes de efectuar una nueva transmisión de trabas, el resultado de la validación de la segunda transmisión se acumulará en el fichero destinado a la Entidad Transmisora a continuación de los registros existentes.

Es decir, los resultados de la validación no se borran hasta que la Entidad no pida la transmisión del fichero y ésta finalice correctamente, quedando en el fichero un único registro de control.

Cuando el D.I.T. rechace un envío de trabas a una Entidad de crédito, ésta deberá transmitir de nuevo Todas las trabas de ese envío, una vez subsanados los errores que se hayan indicado, en el plazo de dos días hábiles desde la recepción de los errores.

Si la Entidad Transmisora da servicio a más de una Entidad de crédito, la aceptación o rechazo del envío de cada una de ellas es independiente. Una vez aceptado un envío de una Entidad de crédito, éste no deberá ser retransmitido al D.I.T. Si el D.I.T. recibe un envío de una Entidad de crédito previamente aceptado en el ciclo en curso, responderá con un código de error 115 en el registro de cabecera de Entidad de crédito. Este es el único caso en el que un error en la validación no supone el rechazo de un envío.

1.2. Admisión del fichero de trabas realizadas por las entidades de crédito.

Porcentaje máximo de errores: 0 %.

Máximo de registros erróneos: 0 %.

Cualquier error en el registro de cabecera o de fin de Entidad Transmisora dará lugar al rechazo del fichero completo (lo que en este documento es denominado «rechazo global»). El mismo efecto tendrá un error en la secuencia de registros.

Cualquier error en el registro de cabecera, de detalle o de fin de Entidad de crédito dará lugar al rechazo completo del envío de la Entidad de crédito correspondiente.

El único error que no provocará el rechazo de un envío de una Entidad de crédito es la retransmisión de las trabas de un envío previamente aceptado en el mismo ciclo. La respuesta contendrá, para la Entidad de crédito de que se trate, un par de registros de tipo 1 y 3, en el primero de los cuales se incluirá el código de error (115).

1.3 Esquema general de procesos y plazos de ejecución.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/311/20269_002.png)

2. Estructura del fichero de diligencias de embargo de cuentas.

El fichero para cada Entidad Transmisora, que contendrá información de diligencias de embargo de cuentas para tantas Entidades de crédito como sea necesario, tiene la estructura siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/311/20269_003.png)

* El fichero de una Entidad Transmisora para un mes concreto se identifica por el campo «FECHA DE COMIENZO DE CICLO».

** La parte del fichero que corresponde a una Entidad de Crédito determinada (un envío) se identifica por la combinación de los campos «CÓDIGO DE ENTIDAD DE DEPOSITO» y «NÚMERO DE ENVÍO».

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD. Los campos que reflejen una hora serán numéricos de 7 posiciones, utilizando el formato HHMMSSD. Los campos numéricos que carezcan de contenido estarán rellenos con ceros; no se consideran válidos en estos campos los espacios en blanco.

2.1 Fichero de diligencias de embargo de cuentas. Registro de cabecera de entidad transmisora. Registro tipo 0.

El primer registro, para cada Entidad Transmisora, será un registro de cabecera, con la siguiente configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: ‘0’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 - 15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16 - 23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘D’ (DILIGENCIAS DE EMBARGO). |
| 25 - 500 | ALF. | 476 | POSICIONES LIBRES DE CONTENIDO. |

2.2. Fichero de diligencias de embargo de cuentas. Registro de cabecera de entidad de crédito. Registro tipo 1.

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘1’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO. |
| 8 - 15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN). FORMATO: AAAANNNN. |
| 16 - 23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘D’ (DILIGENCIAS DE EMBARGO DE CUENTAS). |
| 25 - 32 | NUM. | 8 | FECHA DE GENERACIÓN DEL ENVÍO MENSUAL DE DILIGENCIAS. |
| 33 - 36 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 37 - 37 | ALF. | 1 | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE DILIGENCIAS. CONTENIDO: ‘E’ (CÉNTIMOS DE EURO). |
| 38 - 170 | ALF. | 133 | MENSAJE INFORMATIVO PARA EL DEUDOR: «Si desea mayor información sobre el expediente de embargo, puede dirigirse al teléfono de la Agencia Tributaria XXX-XXX-XXX» (*). |
| 171-500 | ALF. | 330 | POSICIONES LIBRES DE CONTENIDO. |

(*) Se incluirá el número de teléfono de información que en cada momento establezca la Agencia Estatal de Administración Tributaria.

2.3 Fichero de diligencias de embargo de cuentas. Registro de detalle de diligencia de embargo. Registro tipo 2.

Los registros de detalle que sigan al registro de cabecera de Entidad de crédito tendrá la configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE DILIGENCIA DE EMBARGO. CONTENIDO: ‘2’. |  |
| 2 - 10 | ALF. | 9 | NIF/CI DEL DEUDOR. |  |
| 11 - 50 | ALF. | 40 | NOMBRE/RAZON SOCIAL DEL DEUDOR. |  |
| 51 - 52 | ALF. | 2 | SIGLAS DE LA VIA PÚBLICA | DATOS DEL DOMICILIO DEL DEUDOR. |
| 53 - 77 | ALF. | 25 | NOMBRE DE LA VIA PÚBLICA |
| 78 - 82 | NUM. | 5 | NÚMERO DEL PORTAL |
| 83 - 83 | ALF. | 1 | LETRA DEL PORTAL |
| 84 - 85 | ALF. | 2 | ESCALERA |
| 86 - 87 | ALF. | 2 | PISO |
| 88 - 89 | ALF. | 2 | PUERTA |
| 90 - 101 | ALF. | 12 | NOMBRE DEL MUNICIPIO |
| 102 - 106 | NUM. | 5 | CÓDIGO POSTAL |
| 107 - 119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |  |
| 120 - 134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |  |
| 135 - 142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |  |
| 143 - 157 | NUM. | 15 | POSICIONES LIBRES DE CONTENIDO. |  |
| 158 - 158 | ALF. | 1 | POSICIONES LIBRES DE CONTENIDO. |  |
| 159 - 174 | NUM. | 16 | POSICIONES LIBRES DE CONTENIDO. |  |
| 175 - 194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1. |  |
| 195 - 211 | NUM. | 17 | POSICIONES LIBRES DE CONTENIDO. |  |
| 212 - 231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2. |  |
| 232 - 248 | NUM. | 17 | POSICIONES LIBRES DE CONTENIDO. |  |
| 249 - 268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3. |  |
| 269 - 500 | ALF. | 232 | POSICIONES LIBRES DE CONTENIDO. |  |

2.4 Fichero de diligencias de embargo de cuentas. Registro de fin de entidad de crédito. Registro tipo 3.

Al final de los registros de detalle de cada Entidad de crédito, el fichero contiene un registro totalizador de las diligencias incluidas en el fichero para dicha Entidad, que quedan identificadas por un número de envío.

El formato será el siguiente:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘3’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO. |
| 8 - 13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 14 - 28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 29 - 32 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 33 - 500 | ALF. | 468 | POSICIONES LIBRES DE CONTENIDO. |

2.5 Fichero de diligencias de embargo de cuentas. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero se incluye un registro de fin de Entidad Transmisora, con la siguiente configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN ENTIDAD TRANSMISORA. CONTENIDO: ‘8’. |
| 2 - 5 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 6 - 13 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 14 - 500 | ALF. | 487 | POSICIONES LIBRES DE CONTENIDO. |

2.6 Fichero de diligencias de embargo de cuentas. Registro de control para la entidad transmisora. Registro tipo 9.

Se incluye a continuación la descripción de cada campo del registro de tipo 9 en el fichero de diligencias.

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 - 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA. CONTENIDO: ‘9’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 - 15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16 - 24 | ALF. | 9 | POSICIONES LIBRES DE CONTENIDO. |
| 25 - 27 | NUM. | 3 | NÚMERO DE ENTIDADES DE CRÉDITO INCLUIDAS EN EL FICHERO DE DILIGENCIAS. |
| 28 - 28 | ALF. | 1 | INDICADOR DE ESTADO DE LAS DILIGENCIAS PARA LA ENTIDAD TRANSMISORA. CONTENIDO: «P» (PENDIENTE DE RECUPERAR POR LA ENTIDAD TRANSMISORA) ó ‘R’ (RECIBIDAS POR LA ENTIDAD TRANSMISORA). |
| 29 - 31 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 32 - 34 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 35 - 37 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 38 - 40 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 41 - 43 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 44 - 44 | ALF. | 1 | ESTADO GENERAL DE LA ENTIDAD TRANSMISORA PARA EL CICLO MENSUAL. CONTENIDO: «P» (EN PROCESO). |
| 45 - 52 | NUM. | 8 | FECHA DE ALTA DEL REGISTRO. |
| 53 - 59 | NUM. | 7 | HORA DE ALTA DEL REGISTRO. |
| 60 -500 | ALF. | 441 | POSICIONES LIBRES DE CONTENIDO. |

3. Estructura del fichero de trabas de cuentas bancarias.

El fichero de trabas tiene la siguiente estructura:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/311/20269_004.png)

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros. No se consideran válidos en estos campos los espacios en blanco.

3.1 Fichero de trabas de cuentas. Registro de cabecera de entidad transmisora. Registro tipo O.

El fichero de trabas comenzará con un registro de cabecera de Entidad Transmisora, con la siguiente configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: ‘0’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 - 15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16 - 23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS. |
| 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘T’ (TRABAS). |
| 25 - 400 | ALF. | 376 | POSICIONES LIBRES DE CONTENIDO. |

3.2 Fichero de trabas de cuentasregistro de cabecera de entidad de créditoregistro tipo 1.

El primer registro, para cada Entidad de crédito, será un registro de cabecera, con la siguiente configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘1’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO. |
| 8 - 15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN) . |
| 16 - 23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS. |
| 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘T’ (TRABAS). |
| 25 - 28 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 29 - 29 | ALF. |  | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE TRABAS. CONTENIDO: ‘E’ (CÉNTIMOS DE EURO). |
| 30 -400 | ALF. | 371 | POSICIONES LIBRES DE CONTENIDO. |

3.3 Fichero de trabas de cuentas. Registro de detalle de trabas realizadas. Registro tipo 2.

En este registro las Entidades de crédito informan del resultado de las trabas realizadas conforme a la diligencia de embargo recibida del D.I.T..

Cada diligenda enviada por el D.I.T. contendrá hasta 3 Códigos de Cuenta Cliente que corresponderán al mismo deudor, Entidad de crédito y sucursal. Cuando en las cuentas incluidas en la diligencia no se pueda trabar el total indicado en la misma, la Entidad deberá extender el embargo a otras cuentas del mismo deudor, Entidad y sucursal, si éstas existen, con máximo de 6 cuentas en total. En la respuesta de las Entidades no deberá alterarse el orden ni el contenido de las cuentas enviadas en el fichero del D.I.T.; las cuentas adicionales deberán añadirse a continuadón de ellas, sin dejar cuentas vacías.

Si habiendo actuado contra seis cuentas sin lograr la traba de la cantidad indicada en la diligencia, el deudor dispone de más cuentas en la misma Entidad y sucursal, se reflejará esta circunstancia poniendo en el fichero de trabas un ‘1’ en el campo INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO.

El campo CÓDIGO DE RESULTADO DE TRABA podrá tomar los valores:

00 SIN ACTUACIÓN.

01 TRABA REALIZADA.

02 NIF NO TITULAR DE LA CUENTA COMUNICADA.

03 INEXISTENCIA DE SALDO (SALDO CERO O NEGATIVO).

04 SALDO NO DISPONIBLE.

05 CUENTA INEXISTENTE O CANCELADA.

06 OTROS MOTIVOS.

07 TRABA CONDICIONADA.

08 CUENTA EXCLUIDA DEL PROCEDIMIENTO.

09 SALDO PIGNORADO.

10 SITUACIÓN CONCURSAL.

Cuando en la diligencia enviada a la Entidad se solicite el embargo de varias cuentas y se produzca la traba del importe total indicado en la diligencia en una o varias de estas cuentas, siendo innecesario actuar sobre el resto, el código de traba que corresponderá a las cuentas en las que se ha realizado traba será 01 y en aquellas sobre las que no se ha actuado será 00. Este será el único caso en que se acepte el código 00 (sin actuación).

Los registros de detalle que sigan al registro de cabecera de Entidad de crédito tendrán el siguiente contenido:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE TRABAS DE DILIGENCIA DE EMBARGO. CONTENIDO: ‘2’. |
| 2 - 10 | ALF. | 9 | NIF/CI DEL DEUDOR. |
| 11 - 50 | ALF. | 40 | NOMBRE/RAZON SOCIAL DEL DEUDOR. |
| 51 - 52 | ALF. | 2 | SIGLAS DE LA VIA PÚBLICA | DATOS DEL DOMICILIO DEL DEUDOR. |
| 53 - 77 | ALF. | 25 | NOMBRE DE LA VIA PÚBLICA |
| 78 - 82 | NUM. | 5 | NÚMERO DEL PORTAL |
| 83 - 83 | ALF. | 1 | LETRA DEL PORTAL |
| 84 - 85 | ALF. | 2 | ESCALERA |
| 86 - 87 | ALF. | 2 | PISO |
| 88 - 89 | ALF. | 2 | PUERTA |
| 90 - 101 | ALF. | 12 | NOMBRE DEL MUNICIPIO |
| 102 - 106 | NUM. | 5 | CÓDIGO POSTAL |
| 107 - 119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |
| 120 - 134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |
| 135 - 142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |
| 143 - 157 | NUM. | 15 | IMPORTE TOTAL TRABADO. |
| 158 - 158 | ALF. | 1 | INDICADOR DE EXISTENCIA DE MAS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO. CONTENIDO: ‘0’ (NO EXISTEN MAS CUENTAS) O ‘1’ (EXISTEN MAS CUENTAS) |
| 159 - 166 | NUM. | 8 | FECHA DE LA TRABA O ACTUACION. |
| 167 - 174 | NUM. | 8 | FECHA LIMITE DE INGRESO DEL IMPORTE TRABADO. SI NO HAY IMPORTE TRABADO SE RELLENARA CON CEROS. |
| 175 - 194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1 (CCC1). |
| 195 - 196 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC1. |
| 197 - 211 | NUM. | 15 | IMPORTE TRABADO EN CCC1. |
| 212 - 231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2 (CCC2). |
| 232 - 233 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC2. |
| 234 - 248 | NUM. | 15 | IMPORTE TRABADO EN CCC2. |
| 249 - 268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3 (CCC3). |
| 269 - 270 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC3. |
| 271 - 285 | NUM. | 15 | IMPORTE TRABADO EN CCC3. |
| 286 - 305 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 4 (CCC4). |
| 306 - 307 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC4. |
| 308 - 322 | NUM. | 15 | IMPORTE TRABADO EN CCC4. |
| 323 - 342 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 5 (CCC5). |
| 343 - 344 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC5. |
| 345 - 359 | NUM. | 15 | IMPORTE TRABADO EN CCC5. |
| 360 - 379 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 6 (CCC6). |
| 380 - 381 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC6. |
| 382 - 396 | NUM. | 15 | IMPORTE TRABADO EN CCC6. |
| 397 - 400 | ALF. | 4 | POSICIONES LIBRES DE CONTENIDO. |

3.4 Fichero de trabas de cuentas. Registro de fin de entidad de crédito. Registro tipo 3.

Al final de los registros de detalle de cada Entidad, deberá incluirse un registro totalizador de las trabas. El formato será el siguiente:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘3’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO. |
| 8 - 13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 14 - 28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 29 - 43 | NUM. | 15 | IMPORTE TOTAL TRABADO POR LA ENTIDAD DE CRÉDITO. |
| 44 - 47 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 48 - 400 | ALF. | 353 | POSICIONES LIBRES DE CONTENIDO. |

3.5 Fichero de trabas de cuentas. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero se incluye un registro de fin de Entidad Transmisora, o de fin de fichero, con la siguiente configuración:

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN ENTIDAD TRANSMISORA. CONTENIDO: ‘8’. |
| 2 - 5 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 6 - 13 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS. |
| 14 - 400 | ALF. | 387 | POSICIONES LIBRES DE CONTENIDO. |

4. Estructura del fichero resultado de la validación de trabas.

La estructura del fichero resultado de la validación de trabas variará según el resultado de la misma:

a) Si se produce el rechazo global para una Entidad Transmisora, sin respuesta específica para cada Entidad de crédito, el fichero de respuesta contendrá tres registros: de tipo O (cabecera de Entidad Transmisora), 8 (fin de Entidad Transmisora) y 9 (registro de control), respectivamente. En estos registros se indicará el motivo del rechazo.

| ENTIDAD TRANSMISORA | TIPO 0 |
| --- | --- |
| FIN ENTIDAD TRANSMISORA | TIPO 8 |
| REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA | TIPO 9 |

Los tres registros se enviarán siempre; si en el fichero de trabas transmitido por la Entidad no existieran estos registros, se generarían con los datos mínimos precisos y con los errores que hayan podido detectarse.

b) Cuando no se produce el rechazo global para una Entidad Transmisora, la aceptación o rechazo se realiza individualmente para cada una de la Entidades de crédito a la que aquélla dé servicio en el ciclo en curso. En la estructura anterior se introducirá, entre el registro de tipo O y el registro de tipo 8 la respuesta que corresponda a cada una de las Entidades de crédito a la que se esté respondiendo. El código indicando la aceptación o rechazo para cada Entidad estará incluido en el registro de cabecera de Entidad de crédito (tipo 1).

La respuesta será diferente, según se acepte o rechace el envío de la Entidad de crédito, e induso puede variar según la causa del rechazo:

– Para aquellas Entidades de crédito cuyo envío se acepta, la parte correspondiente del fichero de respuesta tendrá la forma:

| ENTIDAD DE CRÉDITO N | TIPO 1 (aceptado) |
| --- | --- |
| FIN ENTIDAD DE CRÉDITO N | TIPO 3 |

– Para aquellas Entidades de crédito en las que el error se produzca en el registro de cabecera de Entidad de crédito del fichero de trabas, la estructura de la parte del fichero de validación correspondiente a esa Entidad será:

| ENTIDAD DE CRÉDITO N | TIPO 1 (rechazado) |
| --- | --- |
| FIN ENTIDAD DE CRÉDITO N | TIPO 3 |

Los registros de detalle no se validan en este caso.

– Cuando siendo correcto el registro de cabecera de Entidad de crédito se produzcan errores en los registros de detalle o de fin de Entidad, en la validación se incluirán, además de los registros de cabecera y fin de Entidad de crédito, los registros de detalle (de tipo 2) erróneos, si los hay, con la indicación del error que contienen; los registros de detalle correctos no se incluyen en la respuesta. Para la Entidad de crédito en cuestión, la parte del fichero de validación será (suponiendo que hay errores en X registros de detalle):

| ENTIDAD DE CRÉDITO N | TIPO 1 (rechazado) |
| --- | --- |
| ERRORES TRABAS DILIGENCIA 1 ERRORES TRABAS DILIGENCIA 2 – – – ERRORES TRABAS DILIGENCIA X | TIPO 2 |
| FIN ENTIDAD DE CRÉDITO N | TIPO 3 |

En general, la respuesta para los registros erróneos de cualquier tipo tendrá la siguiente configuración:

– Una primera parte que será igual al registro erróneo transmitido por la Entidad (las 400 primeras posiciones del registro de resultados)

– A continuación, el código de error y número de campo en que éste se produce, conforme a la numeración que se indica en la descripción de los registros que se hace a continuación, hasta un máximo de 20 errores por registro (posiciones 401-500).

No siempre va a ser posible utilizar esta configuración, pues puede haber errores (particularmente en registros de tipo O y 1) para los que, en lugar de repetir exactamente el registro erróneo, se reconstruirá el contenido de algunos de sus campos.

Se incluye un ejemplo, para el caso de 4 Entidades de crédito, de las que:

– Se rechaza el envío de la Entidad 1 por contener errores en N registros de detalle.

– Se rechaza el envío de la Entidad 2 por errores en el registro de cabecera de Entidad de crédito

– Se acepta el envío de la Entidad 3.

– Se rechaza el envío de la Entidad 4 por errores solamente en el registro de fin de Entidad de crédito.

| ENTIDAD TRANSMISORA | TIPO 0 |
| --- | --- |
| ENTIDAD DE CRÉDITO 1 | TIPO 1 (rechazado) |
| ERRORES TRABAS DILIGENCIA 1 ERRORES TRABAS DILIGENCIA 2 – – – ERRORES TRABAS DILIGENCIA N | TIPO 2 |
| FIN ENTIDAD DE CRÉDITO 1 | TIPO 3 |
| ENTIDAD DE CRÉDITO 2 | TIPO 1 (rechazado) |
| FIN ENTIDAD DE CRÉDITO 2 | TIPO 3 |
| ENTIDAD DE CRÉDITO 3 | TIPO 1 (rechazado) |
| FIN ENTIDAD DE CRÉDITO 3 | TIPO 3 |
| ENTIDAD DE CRÉDITO 4 | TIPO 1 (rechazado) |
| ENTIDAD DE CRÉDITO 4 | TIPO 3 |
| FIN ENTIDAD TRANSMISORA | TIPO 8 |
| REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA | TIPO 9 |

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD. Los campos que reflejen una hora serán numéricos de 7 posiciones, utilizando el formato HHMMSSD.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros; no se consideran válidos en estos campos los espacios en blanco.

4.1 Fichero de resultados en la validación de trabas. Registro de cabecera de entidad transmisora. Registro tipo O.

El primer registro del fichero de resultados de la validación será la cabecera de Entidad Transmisora, con la siguiente configuración:

| N.º CAMPO | POSICIÓN | TIPO | LONG. | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: ‘0’. |
| 2 | 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. |
| 3 | 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 4 | 8 - 15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 5 | 16 - 23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS (cuando se produzca el rechazo global del fichero de trabas) o FECHA DE PROCESO DE VALIDACIÓN (en el resto de los casos). |
| 6 | 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘R’ (RESULTADO DE VALIDACIÓN DEL FICHERO DE TRABAS). |
| 7 | 25 - 400 | ALF. | 376 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401 - 403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI CÓDIGO DE ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES). |
|  | 404 - 405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406 - 408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409 - 410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411 - 413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414 - 415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416 -418 | NUM. | 3 | CÓDIGO DE ERROR-4 |
|  | 419 - 420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4 |
|  | 421 - 423 | NUM. | 3 | CÓDIGO DE ERROR-5 |
|  | 424 - 425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5 |
|  | 426 - 428 | NUM. | 3 | CÓDIGO DE ERROR-6 |
|  | 429 - 430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6 |
|  | 431 - 433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434 - 435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436 - 438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439 - 440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441 - 443 | NUM. | 3 | CÓDIGO DE ERROR- 9. |
|  | 444 - 445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446 - 448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449 - 450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451 - 453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454 - 455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456 - 458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459 - 460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461 - 463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464 - 465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466 - 468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469 - 470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471 - 473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474 - 475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476 - 478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479 - 480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481 - 483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484 - 485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486 - 488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489 - 490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491 - 493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494 - 495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496 - 498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499 - 500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el DIT reproduce los datos transmitidos por las Entidades.

4.2 Fichero de resultados en la validación de trabas. Registro de cabecera de entidad de crédito. Registro tipo 1.

El primer registro, para cada Entidad de crédito, será un registro de cabecera, con la siguiente configuración:

| N.º CAMPO | POSICIÓN | TIPO | LONG. | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘1’. |
| 2 | 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 3 | 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO. |
| 4 | 8 - 15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN). FORMATO: AAAANNNN |
| 5 | 16 - 23 | NUM. | 8 | FECHA DE PROCESO DE VALIDACIÓN (si el registro 1 no contiene errores; el FORMATO es: AAAAMMDD) o FECHA DE CREACIÓN DEL FICHERO DE TRABAS (si el registro de tipo 1 contiene errores). |
| 6 | 24 - 24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: ‘R’ (RESULTADOS DE VALIDACIÓN DE TRABAS), si el registro 1 no tiene errores, o lo que contuviera el fichero de trabas, si el registro 1 los contiene. |
| 7 | 25 - 28 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 | 29 - 29 | ALF. | 1 | INDICADOR DE ENVÍO ACEPTADO O RECHAZADO. CONTENIDO: ‘A’ (ACEPTADO EL ENVÍO DE TRABAS) O ‘R’ (RECHAZADO EL ENVÍO DE TRABAS). |
| 9 | 30 - 30 | ALF. | 1 | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE TRABAS. CONTENIDO: ‘E’ (CÉNTIMOS DE EURO). |
| 10 | 31 - 400 | ALF. | 370 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401 - 403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI CÓDIGO DE ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES) |
|  | 404 - 405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406 - 408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409 - 410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411 - 413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414 - 415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416 - 418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419 - 420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421 - 423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424 - 425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426 - 428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429 - 430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431 - 433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434 - 435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436 - 438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439 - 440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441 - 443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444 - 445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446 - 448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449 - 450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451 - 453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454 - 455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456 - 458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459 - 460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461 - 463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464 - 465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466 - 468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469 - 470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471 - 473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474 - 475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476 - 478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479 - 480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481 - 483 | NUM. | 3 | CÓDIGO DE ERROR-17 |
|  | 484 - 485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486 - 488 | NUM. | 3 | CÓDIGO DE ERROR -18 |
|  | 489 - 490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491 - 493 | NUM. | 3 | CÓDIGO DE ERROR-19 |
|  | 494 - 495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496 - 498 | NUM. | 3 | CÓDIGO DE ERROR-20 |
|  | 499 - 500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el DIT reproduce los datos transmitidos por las Entidades.

4.3 Fichero de resultados en la validación de trabas. Registro de detalle de errores en trabas. Registro tipo 2.

Los registros de detalle que sigan al registro de cabecera de Entidad de crédito, tendrán el siguiente formato:

| N.º CAMPO | POSICIÓN | TIPO | LONG. | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE ERRORES EN LA VALIDACIÓN DE TRABAS. CONTENIDO: ‘2’. |
| 2 | 2 - 10 | ALF. | 9 | NIF/CI DEL DEUDOR |
| 3 | 11 - 106 | ALF. | 96 | POSICIONES LIBRES DE CONTENIDO. |
| 4 | 107 - 119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |
| 5 | 120 - 134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |
| 6 | 135 - 142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |
| 7 | 143 - 157 | NUM. | 15 | IMPORTE TOTAL TRABADO. |
| 8 | 158 - 158 | ALF. | 1 | INDICADOR DE EXISTENCIA DE MAS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO. |
| 9 | 159 - 166 | NUM. | 8 | FECHA DE LA TRABA O ACTUACION. |
| 10 | 167 - 174 | NUM. | 8 | FECHA LIMITE DE INGRESO DEL IMPORTE TRABADO. |
| 11 | 175 - 194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1 (CCC1). |
| 12 | 195 - 196 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC1. |
| 13 | 197 - 211 | NUM. | 15 | IMPORTE TRABADO EN CCC1. |
| 14 | 212 - 231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2 (CCC2). |
| 15 | 232 - 233 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC2. |
| 16 | 234 - 248 | NUM. | 15 | IMPORTE TRABADO EN CCC2. |
| 17 | 249 - 268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3 (CCC3). |
| 18 | 269 - 270 | NUM. | 2 | CÓDIGO RESULTADO DE TRABA EN CCC 3. |
| 19 | 271 - 285 | NUM. | 15 | EN IMPORTE TRABADO CCC3 |
| 20 | 286 - 305 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 4 (CCC4). |
| 21 | 306 - 307 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC4. |
| 22 | 308 - 322 | NUM. | 15 | IMPORTE TRABADO EN CCC4. |
| 23 | 323 - 342 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 5 (CCC5). |
| 24 | 343 - 344 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC5. |
| 25 | 345 - 359 | NUM. | 15 | IMPORTE TRABADO EN CCC5. |
| 26 | 360 - 379 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 6 (CCC6). |
| 27 | 380 - 381 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC6. |
| 28 | 382 - 396 | NUM. | 15 | IMPORTE TRABADO EN CCC6. |
| 29 | 397 - 400 | ALF. | 4 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401 - 403 | NUM. | 3 | CÓDIGO DE ERROR-1. |
|  | 404 - 405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406 - 408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409 - 410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411 - 413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414 - 415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416 - 418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419 - 420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421 - 423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424 - 425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426 - 428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429 - 430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431 - 433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434 - 435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436 - 438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439 - 440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441 - 443 | NUM. | 3 | CÓDIGO DE ERROR- 9. |
|  | 444 - 445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446 - 448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449 - 450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451 - 453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454 - 455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456 - 458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459 - 460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461 - 463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464 - 465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466 - 468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469 - 470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471 - 473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474 - 475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476 - 478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479 - 480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481 - 483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484 - 485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486 - 488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489 - 490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491 - 493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494 - 495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496 - 498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499 - 500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el DIT reproduce los datos transmitidos por las Entidades.

4.4 Fichero resultado de validación de trabas. Registro de fin de entidad de crédito. Registro tipo 3.

Tras los registros de detalle erróneos de cada Entidad de crédito, se incluirá un registro de cierre de los resultados de la validación para esa Entidad. Este registro de fin de Entidad de crédito existirá incluso aunque no haya errores para la misma y se acepte el envío; su formato será el siguiente:

| N.º CAMPO | POSICIÓN | TIPO | LONG. | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD DE CRÉDITO. CONTENIDO: ‘3’. |
| 2 | 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. |
| 3 | 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD DE CRÉDITO |
| 4 | 8 -13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 5 | 14 - 28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO. |
| 6 | 29 - 43 | NUM. | 15 | IMPORTE TOTAL TRABADO POR LA ENTIDAD DE CRÉDITO. |
| 7 | 44 - 47 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 | 48 -400 | ALF. | 353 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401 -403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI EL CÓDIGO ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES) |
|  | 404 -405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406 - 408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409 - 410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411 - 413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414 - 415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416 - 418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419 - 420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421 - 423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424 - 425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426 - 428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429 - 430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431 - 433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434 - 435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436 - 438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439 - 440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441 - 443 | NUM. | 3 | CÓDIGO DE ERROR- 9. |
|  | 444 - 445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446 - 448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449 - 450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451 - 453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454 - 455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456 - 458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459 - 460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461 - 463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464 - 465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466 - 468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469 - 470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471 - 473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474 - 475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476 - 478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479 - 480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481 - 483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484 - 485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486 - 488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489 - 490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491 - 493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494 - 495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496 - 498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499 - 500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el DIT reproduce los datos transmitidos por las Entidades.

4.5 Fichero de resultados en la validación de trabas. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero deberá incluirse un registro de fin de Entidad Transmisora. Este registro tendrá la siguiente configuración:

| N.º CAMPO | POSICIÓN | TIPO | LONG. | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD TRANSMISORA. CONTENIDO: ‘8’. |
| 2 | 2 -5 | NUM. | 4 | CÓDIGO DE ENTIDAD DE TRANSMISORA. |
| 3 | 6 -13 | NUM. | 8 | FECHA DE PROCESO DE VALIDACIÓN (si el registro de tipo 8 no contiene errores; el FORMATO es: AAAAMMDD) o FECHA DE CREACIÓN DEL FICHERO DE TRABAS (si el registro de tipo 8 sí los contiene). |
| 4 | 14 - 400 | ALF. | 387 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401 -403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI EL CÓDIGO ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES) |
|  | 404 -405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406 -408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409 -410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411 -413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414 -415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416 - 418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419 - 420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421 - 423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424 - 425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5 |
|  | 426 - 428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429 - 430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431 - 433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434 - 435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR ERROR-7. |
|  | 436 - 438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439 - 440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441 - 443 | NUM. | 3 | CÓDIGO DE ERROR- 9. |
|  | 444 - 445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446 - 448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449 - 450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451 - 453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454 - 455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456 - 458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459 - 460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461 - 463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464 - 465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466 - 468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469 - 470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471 - 473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474 - 475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476 - 478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479 - 480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481 - 483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484 - 485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486 - 488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489 - 490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491 - 493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494 - 495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496 - 498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499 - 500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el DIT reproduce los datos transmitidos por las Entidades.

4.6 Fichero de resultado de la validación de trabas. Registro de control para la entidad transmisora. Registro tipo 9.

Se incluye a continuación la descripción de cada campo del registro de tipo 9 en el fichero de diligencias.

| POSICIÓN | TIPO | LONGITUD | DESCRIPCIÓN DEL CAMPO |
| --- | --- | --- | --- |
| 1 - 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA. CONTENIDO: ‘9’. |
| 2 - 3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4 - 7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 - 15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16 - 24 | ALF. | 9 | POSICIONES LIBRES DE CONTENIDO. |
| 25 - 27 | NUM. | 3 | NÚMERO DE ENTIDADES DE CRÉDITO INCLUIDAS EN EL FICHERO DE DILIGENCIAS. |
| 28 - 28 | ALF. | 1 | INDICADOR DE ESTADO DE LAS DILIGENCIAS PARA LA ENTIDAD TRANSMISORA. CONTENIDO: ‘R’ (RECIBIDAS POR LA ENTIDAD TRANSMISORA). |
| 29 - 31 | NUM. | 3 | NÚMERO DE ENTIDADES DE CRÉDITO DE LAS QUE HA TRANSMITIDO TRABAS LA ENTIDAD TRANSMISORA EN EL CICLO EN CURSO. |
| 32 - 34 | NUM. | 3 | NÚMERO DE ENTIDADES DE CRÉDITO CORRESPONDIENTES A LA ENTIDAD TRANSMISORA CUYOS ENVÍOS HAN SIDO RECHAZADOS EN EL CICLO EN CURSO. |
| 35 - 37 | NUM. | 3 | NÚMERO DE ENTIDADES DE CRÉDITO CORRESPONDIENTES A LA ENTIDAD TRANSMISORA CUYOS ENVÍOS HAN SIDO ACEPTADOS EN EL CICLO EN CURSO. |
| 38 - 40 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 41 - 43 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 44 - 44 | ALF. | 1 | ESTADO GENERAL DE LA ENTIDAD TRANSMISORA PARA EL CICLO MENSUAL. CONTENIDO: “P” (EN PROCESO) O “F” (FINALIZADO). |
| 45 - 52 | NUM. | 8 | FECHA DE ALTA DEL REGISTRO. |
| 53 - 59 | NUM. | 7 | HORA DE ALTA DEL REGISTRO. |
| 60 -500 | ALF. | 441 | POSICIONES LIBRES DE CONTENIDO. |

5. Relación de códigos de error en los resultados de la validación

| ERRORES COMUNES A TODOS LOS TIPOS DE REGISTRO |
| --- |
| 601 | Error de secuencia de registros. |
| 602 | DELEGACIÓN DE LA AGENCIA RECEPTORA DEL FICHERO distinta de 57. |
| 608 | FECHA DE COMIENZO DE CICLO incorrecta. |
| REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA (TIPO 0) |
| --- |
| 003 | CÓDIGO DE ENTIDAD TRANSMISORA incorrecto. |
| 006 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS errónea. |
| 007 | INDICADOR DE TIPO DE FICHERO distinto de ‘T’. |
| REGISTRO DE CABECERA DE ENTIDAD DE CRÉDITO (TIPO 1) |
| --- |
| 103 | CÓDIGO DE ENTIDAD DE CRÉDITO incorrecto. |
| 105 | NÚMERO DE ENVÍO inexistente. |
| 106 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS errónea. |
| 107 | INDICADOR DE TIPO DE FICHERO distinto de ‘T’. |
| 110 | CÓDIGO DE ENTIDAD TRANSMISORA no corresponde con la que comenzó el ciclo. |
| 112 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del contenido en el registro de cabecera de Entidad Transmisora. |
| 113 | NÚMERO DE ENVÍO no numérico. |
| 114 | INDICADOR DE MONEDA distinto de ‘E’. |
| 115 | Envío para esta Entidad de crédito previamente aceptado en este ciclo |
| REGISTRO DE DETALLE (TIPO 2) |
| --- |
| 202 | NIF DEL DEUDOR no cumplimentado. |
| 203 | NIF DEL DEUDOR incorrecto o distinto del incluido en la diligencia transmitida a la Entidad. |
| 204 | NÚMERO DE DILIGENCIA DE EMBARGO no cumplimentado o incorrecto. |
| 205 | NÚMERO DE DILIGENCIA DE EMBARGO inexistente en el fichero de diligencias transmitido a la Entidad. |
| 206 | IMPORTE TOTAL A EMBARGAR distinto del que figuraba en la diligencia transmitida a la Entidad. |
| 207 | FECHA DE GENERACIÓN DE LA DILIGENCIA incorrecta o distinta de la que figura en la diligencia transmitida a la Entidad. |
| 208 | IMPORTE TOTAL TRABADO no numérico o superior al importe a embargar indicado en la diligencia transmitida a la Entidad. |
| 209 | IMPORTE TOTAL TRABADO no coincide con la suma de los importes trabados en cada una de las cuentas incluidas en la diligencia. |
| 210 | INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO, igual a “1” cuando no se han cumplimentado las 6 cuentas posibles a aportar. |
| 211 | FECHA DE TRABA O ACTUACIÓN no cumplimentada, incorrecta o menor que la fecha de generación de la diligencia. |
| 212 | FECHA LÍMITE DE INGRESO DEL IMPORTE TRABADO incorrecta, menor que la fecha de traba, no cumplimentada (siendo distinto de cero el importe total trabado) o distinta de ceros (siendo cero el importe total trabado). |
| 213 | Error en CÓDIGO DE CUENTA CLIENTE (1-6): Se comprueba que se incluyen, sin alteraciones y en el mismo orden, las mismas cuentas que figuraban en el fichero de diligencias transmitido a la Entidad. Para las cuentas añadidas por la Entidad se comprueba que son correctas y corresponden con la misma Entidad de crédito y sucursal que figuraban en las cuentas originales. Las cuentas añadidas deben figurar a continuación de las cuentas que se incluían en el fichero de diligencias, sin dejar huecos entre ellas. |
| 214 | CÓDIGO DE RESULTADO DE TRABA (1-6) distinto de los valores admitidos (00 a 10). |
| 215 | IMPORTE TRABADO EN CUENTA (1-6) no numérico o superior al IMPORTE TOTAL A EMBARGAR de la diligencia. |
| 216 | CÓDIGO DE RESULTADO DE TRABA (1-6) incoherente con el IMPORTE TRABADO EN CUENTA (1-6). Este error se produce cuando: - El código de resultado (1-6) no es “01”, “04” o “07”, siendo mayor que 0 el importe trabado en la cuenta (1-6). - El código de resultado (1-6) es “01”, siendo nulo el importe trabado en la cuenta (1-6). |
| 217 | Existen CÓDIGOS DE CUENTA CLIENTE duplicados. |
| 218 | IMPORTE TOTAL A EMBARGAR no numérico. |
| 219 | INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO distinto de O ó 1. |
| REGISTRO DE FIN DE ENTIDAD DE CRÉDITO (TIPO 3) |
| --- |
| 303 | CÓDIGO DE ENTIDAD DE CRÉDITO distinto del que figura en el registro de cabecera de Entidad de crédito. |
| 304 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO distinto al contenido en el fichero de diligencias transmitido a la Entidad o distinto del número de registros de detalle contenidos en el fichero de trabas devuelto por ésta. |
| 305 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD DE CRÉDITO distinto al contenido en el fichero de diligencias transmitido a la Entidad. |
| 306 | IMPORTE TOTAL TRABADO POR LA ENTIDAD DE CRÉDITO descuadrado con importe total acumulado de los registros de detalle. |
| 308 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del que figura en el registro de cabecera de Entidad de crédito. |
| REGISTRO DE FIN DE ENTIDAD TRANSMISORA (TIPO 8) |
| --- |
| 804 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del contenido en el registro de cabecera de Entidad Transmisora. |
| 805 | FECHA DE CREACIÓN DEL FICHERO DE TRABAS distinta de la del registro de cabecera de Entidad Transmisora. |

6. Características de la conexión con el D.I.T. para el intercambio telemático de ficheros.

A) LINEA DE COMUNICACIONES

Conexión X-25 IBERPAC

Características:

– Circuito virtual conmutado.

– Tamaño de paquete: 128.

– Tamaño ventana nivel 2: 7.

– Tamaño ventana nivel 3: 7.

B) PROGRAMA DE TRANSFERENCIA DE FICHEROS

EDITRAN SOFTWARE DE INDRA
