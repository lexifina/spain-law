## ANEXO IV

## Levantamiento telemático de trabas: descripción general y especificaciones técnicas.

1. Descripción general del procedimiento.

Las órdenes de levantamiento de embargo serán remitidas telemáticamente a todas las Entidades de crédito adheridas al procedimiento que se regula en la presente Resolución.

El objetivo del presente anexo es establecer las especificaciones técnicas por las que habrán de regirse los envíos telemáticos de las órdenes de levantamiento de embargo.

El intercambio telemático (vía EDITRAN) de información entre el Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (en adelante D.I.T.) y las Entidades de crédito para el embargo de cuentas repite todos los meses un ciclo que finaliza con la recepción por parte de dichas Entidades del fichero de aceptación de los resultados de las trabas por ellas realizadas.

Al igual que en el resto del procedimiento, para el intercambio telemático de la información correspondiente a órdenes de levantamiento de embargos cada Entidad de crédito utilizará una Entidad transmisora (que podrá ser la propia Entidad de crédito u otra Entidad diferente). Una Entidad transmisora podrá dar servido a varias Entidades de crédito, con la restricción de que para un mismo ciclo todas las transmisiones correspondientes a una Entidad de crédito (incluyendo las de órdenes de levantamiento de embargo) se realizarán a través de la misma Entidad transmisora.

Las órdenes de levantamiento de aquellas Entidades de crédito gestionadas por una misma Entidad transmisora que se produzcan en un mismo día se agruparán en un único fichero, con la estructura que se detalla más adelante. Este fichero solo contendrá información para las Entidades de crédito para las que existan órdenes de levantamiento en ese día. Si no existieran órdenes de levantamiento para ninguna de las Entidades de crédito que son servidas por una misma Entidad transmisora no se generará fichero de levantamientos, por lo que dicha transmisora encontrará el registro de control correspondiente a la última transmisión de levantamientos que se hubiera realizado.

Pam la comunicación de las órdenes de levantamiento se utilizará un fichero distinto del empleado para diligencias, trabas o resultados de validación de trabas, ya que una misma Entidad transmisora puede transmitir en días distintos la trabas correspondientes a las diferentes Entidades de crédito a las que da servicio, pudiendo cada una de ellas tener una fecha de traba distinta, y dado que la aceptación o rechazo de estas trabas son independientes, una Entidad transmisora puede recibir en el mismo día órdenes de levantamientos correspondientes a Entidades de crédito cuyos resultados de traba hayan sido aceptados con anterioridad y respuestas (de aceptación o de rechazo) de las Entidades de crédito pendientes.

La comunicación de los levantamientos de embargo será unidireccional, puesto que no habrá respuesta por parte de las entidades. En los casos en que por motivos técnicos o por errores en los ficheros, las Entidades no pudieran recuperar o tratar correctamente las órdenes de levantamiento recibidas, se pondrán en contacto con el D.I.T., a los efectos que resulten procedentes.

La comunicación de las órdenes de levantamiento se realizará a las Entidades transmisoras todos los días hábiles, si bien únicamente se encontrarán levantamientos para una entidad de crédito entre el día siguiente al de aceptación por el D.I.T. del fichero de resultado de traba y el vigésimo día natural contado desde el siguiente a la fecha en la que se hubiera producido la traba en la correspondiente Entidad de crédito. En ningún caso el D.I.T. incluirá en el fichero órdenes de levantamiento una vez transcurrido el aludido plazo.

Al igual que en el resto de transmisiones de información que afectan al procedimiento regulado en esta Resolución, para la de las órdenes de levantamiento de embargo la iniciativa de la comunicación corresponderá a las Entidades transmisoras, en las fechas y horas que se indican seguidamente.

La recepción por parte de estas Entidades de los ficheros con origen en el D.I.T. supondrá el borrado de los mismos y su sustitución por un fichero con un único registro de control, que indica que se ha producida dicha recepción.

El horario de las transmisiones será, de lunes a viernes, desde las 17,00 hasta las 23,00 horas.

Al igual que las diligencias de embargo, las trabas y los resultados de validación de éstas, los levantamientos pertenecientes a un mismo ciclo se identificarán por medio de una fecha a la que se ha denominado «fecha de comienzo de ciclo».

En principio, los ciclos no deben solaparse. No obstante, si en un mismo día existiesen órdenes de levantamiento de embargo correspondientes a dos ciclos consecutivos, se concatenarían en el mismo fichero dos bloques de registros, uno para cada ciclo, con la estructura que se indica más adelante en este mismo anexo. El registro de cabecera de cada uno de estos bloques indicará a qué ciclo corresponden las órdenes de levantamiento que en él se contienen.

Si por algún motivo una Entidad transmisora no recuperase algún día el fichero de levantamientos, se concatenarán a este fichero las órdenes de levantamiento correspondientes al día siguiente.

2. Estructura del fichero del levantamiento de trabas.

El fichero de levantamientos tendrá la siguiente estructura:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/311/20269_007.png)

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros. No se consideraran válidos en estos campos los espacios en blanco.

3. Características de la conexión con el d.i.t. para el intercambio telemático de ficheros.

3.1) Fichero de levantamiento de trabas de cuentas. Registro de cabecera de Entidad Transmisora. Registro Tipo 0.

El fichero de levantamiento de trabas comenzará con un registro de cabecera de Entidad Transmisora, con la siguiente configuración:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de Entidad transmisora. Contenido «0». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de Entidad transmisora. |
| 8-15 | 8 | NUM. | Fecha de comienzo de ciclo. |
| 16-23 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 24 | 1 | ALF. | Indicador de tipo de fichero. Contenido «L» (levantamientos). |
| 25-400 | 376 | ALF. | Posiciones libres de contenido. |

3.2) Fichero de levantamiento de trabas de cuentas. Registro de cabecera de Entidad de crédito. Registro Tipo 1.

El primer registro para cada Entidad de crédito será un registro de cabecera con la siguiente configuración:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de Entidad de crédito. Contenido «1». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de Entidad de crédito. |
| 8-15 | 8 | NUM. | Número de envío (Año y número orden). |
| 16-23 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 24 | 1 | ALF. | Indicador de tipo de fichero. Contenido «L» (levantamientos). |
| 25-28 | 4 | NUM. | Código de Entidad transmisora. |
| 29 | 1 | ALF: | Indicador de moneda Contenido «E» (céntimos de euro). |
| 30-400 | 371 | ALF. | Posiciones libres de contenido. |

3.3) Fichero de levantamiento de trabas de cuentas. Registro de detalle de trabas realizadas. Registro Tipo 2.

Los registros de detalle que sigan al registro de cabecera de Entidad de crédito tendrán el contenido siguiente:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de detalle de levantamiento de trabas. Contenido «2». |
| 2-10 | 9 | ALF. | NIF/CIF del deudor. |
| 11-50 | 40 | ALF. | Nombre y apellidos/Razón social del deudor |
| 51-106 | 56 | ALF. | Posiciones libres de contenido. |
| 107-119 | 13 | ALF. | Número de diligencia de embargo. |
| 120-134 | 15 | NUM. | Importe total a embargar. |
| 135-142 | 8 | NUM. | Fecha de generación de la diligencia. |
| 143-157 | 15 | NUM. | Importe total trabado. |
| 158 | 1 | ALF. | Posición de contenido libre. |
| 159-166 | 8 | NUM. | Fecha de la traba. |
| 167-174 | 8 | NUM. | Fecha límite de ingreso del importe trabado. |
| 175-194 | 20 | NUM. | Código Cuenta Cliente 1 (CCC1) |
| 195-196 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC1 |
| 197-211 | 15 | NUM. | Importe a levantaren CCC1 |
| 212-231 | 20 | NUM. | Código Cuenta Cliente 2 (CCC2) |
| 232-233 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC2 |
| 234-248 | 15 | NUM. | Importe a levantar en CCC2 |
| 249-268 | 20 | NUM. | Código Cuenta Cliente 3 (CCC3) |
| 269-270 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC3 |
| 271-285 | 15 | NUM. | Importe a levantar en CCC3 |
| 286-305 | 20 | NUM. | Código Cuenta Cliente 4 (CCC4) |
| 306-307 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC4 |
| 308-322 | 15 | NUM. | Importe a levantar en CCC4 |
| 323-342 | 20 | NUM. | Código Cuenta Cliente 5 (CCC5) |
| 343-344 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC5 |
| 345-359 | 15 | NUM. | Importe a levantar en CCC5 |
| 360-379 | 20 | NUM. | Código Cuenta Cliente 6 (CCC6) |
| 380-381 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC6 |
| 382-396 | 15 | NUM. | Importe a levantar en CCC6 |
| 397-400 | 4 | ALF. | Posiciones libres de contenido. |

Los códigos de tipos de levantamiento serán:

– Levantamiento total del embargo en esa cuenta.

– Levantamiento parcial del embargo en esa cuenta.

– No hay levantamiento en esa cuenta.

Los códigos pueden ser diferentes para las cuentas incluidas en una misma diligencia de embargo.

La estructura de este registro es un reflejo de la utilizada en el registro de detalle del fichero de resultados de trabas. Se incluirán en él tantas cuentas como haya en este último registro y en el mismo orden. Sólo podrán incluirse levantamientos en aquellas cuentas en las que se hubiera producido traba y el importe levantado no podrá superar al trabado.

Para una misma cuenta podrán produdrse varias órdenes de levantamiento en días distintos dentro del mismo ciclo mensual. Cada una de ellas es independiente de las restantes, no acumulándose en los levantamientos sucesivos el importe de los transmitidos con anterioridad.

3.4) Fichero de levantamiento de trabas de cuentas. Registro de fin de Entidad de crédito. Registro Tipo 3.

Al final de los registros de detalle de cada Entidad, deberá incluirse un registro totalizador de los levantamientos. El formato será el siguiente:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de fin de Entidad de crédito. Contenido «3». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57». |
| 4-7 | 4 | NUM. | Código de Entidad de crédito. |
| 8-13 | 6 | NUM. | Número de diligendas con levantamientos incluidas en el envío a la Entidad de crédito. |
| 14-28 | 15 | NUM. | Importe total a levantar de las diligencias incluidas en el envío a la Entidad de crédito. |
| 29-43 | 15 | NUM. | Posiciones libres de contenido. |
| 44-47 | 4 | NUM. | Código de la Entidad transmisora |
| 48-400 | 353 | ALF. | Posiciones libres de contenido. |

3.5) Fichero de levantamiento de trabas de cuentas. Registro de fin de Entidad Transmisora. Registro Tipo 8.

Al final del fichero se incluye un registro de fin de Entidad Transmisora, o de fin de fichero, con la siguiente configuración:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de Entidad transmisora. Contenido «8». |
| 2-5 | 4 | NUM. | Código de Entidad transmisora. |
| 6-13 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 14-400 | 387 | ALF. | Posiciones libres de contenido. |

3.6) Fichero de levantamiento de trabas de cuentas. Registro de control para la Entidad Transmisora. Registro Tipo 9.

A continuación se incluye la descripción de cada campo del registro de tipo 9 en el fichero de levantamientos:

| POSICIÓN | LONGITUD | TIPO | DESCRIPCIÓN |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de control para la Entidad Transmisora. Contenido «9». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de Entidad Transmisora. |
| 8-15 | 8 | NUM. | Fecha de comienzo de ciclo.. |
| 16-24 | 9 | ALF.. | Posidones libres de contenido. |
| 25-27 | 3 | NUM.. | Número de Entidades de crédito incluidas en el fichero de levantamientos. |
| 28 | 1 | ALF. | Indicador de estado de los levantamientos para la Entidad Transmisora. Contenido «P» (pendiente de recuperar por la Entidad Transmisora) ó «R» (recibidas por la Entidad Transmisora). |
| 29-44 | 16 | ALF: | Posidones libres de contenido. |
| 45-52 | 8 | NUM.. | Fecha de alta del registro. |
| 53-59 | 7 | NUM. | Hora de alta del registro. |
| 60-400 | 341 | ALF: | Posidones libres de contenido. |

Este registro contendrá, en caso de ausencia de nuevos datos de levantamientos, una «R» en la posición 28.

Para mantener la coherencia del procedimiento, cuando una Entidad Transmisora comience a funcionar con este sistema, antes de que se produzca la transmisión del primer fichero con levantamientos el D.I.T. generará y pondrá a disposición de la Entidad un fichero con un único registro de tipo 9 en el que los campos «NUMERO DE ENTIDADES DE CRÉDITO INCLUIDAS EN EL FICHERO DE LEVANTAMIENTOS» y «FECHA DE COMIENZO DE CICLO» estarán rellenos con ceros, situación que se repetirá en ausencia de nuevos datos.

Con ello se evita que se produzca un error en la comunicación cuando la Entidad intente recuperar un fichero de levantamientos, una vez aceptados los resultados de alguna de las Entidades de crédito a las que da servicio, sin que haya realizado todavía ningún levantamiento.

Este es el único caso en el que un campo de tipo fecha («FECHA DE COMIENZO DE CICLO») carece de una estructura AAAAMMDD válida, puesto que estará relleno con ceros.

4. Características de la conexión con el D.I.T. para el intercambio telemático de ficheros.

4.1) Línea de comunicaciones.

– Conexión X-25 IBERPAC.

– Características:

Circuito virtual conmutado.

Tamaño de paquete: 128.

Tamaño ventana nivel 2: 7.

Tamaño ventana nivel 3: 7.

4.2) Programa de transferencia de ficheros.

EDITRAN SOFTWARE DE INDRA
