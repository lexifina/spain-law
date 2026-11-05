## ANEXO III

## Procedimiento de consulta electrónica del FIVA

1. Condiciones del procedimiento

1.1 Será utilizado por las entidades aseguradoras de los vehículos implicados en el accidente, ya sea por subrogación en los derechos y acciones de su asegurado, ya sea en virtud de su obligación de asistencia jurídica judicial y extrajudicial derivada de los seguros de defensa jurídica que habitualmente se suscriben junto con el seguro de responsabilidad civil de automóviles, de suscripción obligatoria.

1.2 La adhesión de la entidad aseguradora al procedimiento de consulta electrónica al FIVA implicará la suscripción de un Protocolo de adhesión con el Consorcio de Compensación de Seguros, en el que la entidad se comprometerá a utilizar dicho procedimiento en todas sus consultas de información, sin que pueda compatibilizar dicho procedimiento con el procedimiento manual; a utilizar los procedimientos de subsanación de errores que establezca el Consorcio de Compensación de Seguros; y a mantener actualizados los procesos necesarios para enviar la información, ajustándose a los criterios, formas y plazos establecidos en la normativa legal reguladora del FIVA.

1.3 El Consorcio de Compensación de Seguros podrá suspender la posibilidad de uso por la aseguradora del sistema de consulta electrónica cuando ésta dejase de cumplir alguno de los requisitos de adhesión y funcionamiento del procedimiento.

2. Fundamento técnico del procedimiento

El procedimiento se basa en el envío y recepción de fichero con dos tipos de registros EDI de longitud fija de 325 caracteres: CEFIVA para las consultas y REFIVA para las respuestas. Cada registro contendrá un mensaje que describirá la forma de interpretar el contenido de la información que incorpora.

Los mensajes que se han definido son los siguientes:

| Código | Descripción breve | Descripción general |
| --- | --- | --- |
| 801 | Solicitud al FIVA de información en formato electrónico. | Lo utilizarán las entidades aseguradoras para solicitar información al FIVA y que éste le responda en formato electrónico. |
| 802 | Respuesta afirmativa del FIVA en formato electrónico. | Lo enviará el FIVA, indicando la entidad en la cual figura asegurado un vehículo. |
| 803 | Solicitud al FIVA de informe. | Lo utilizan las entidades aseguradoras para solicitar información al FIVA y que éste responda, excepcionalmente, mediante un informe escrito en soporte papel. |
| 804 | Aviso. Informe emitido. | Lo envía el FIVA indicando a la entidad que ha sido emitido el informe solicitado. |
| 806 | Respuesta negativa del FIVA. | Lo envía el FIVA indicando que no consta aseguramiento del vehículo consultado en entidad alguna. Si en el plazo de un mes se recibe alguna información, se remitirá la respuesta electrónica o informe oportuno. No obstante, se recuerda que la entrada en funcionamiento del FIVA fue el 14 de junio de 1996 y, por tanto, la información de no constancia de seguro en fecha anterior a la indicada no implica que el vehículo careciera del Seguro Obligatorio de Automóviles en ese momento. |

3. Descripción del procedimiento

3.1 La entidad aseguradora enviará al FIVA un registro CEFIVA, con el mensaje 801, o, excepcionalmente, con el mensaje 803, si desea un informe escrito.

3.2 La entidad aseguradora deberá emitir las solicitudes de información en el formato de escrito en este anexo, pudiendo solicitar la respuesta en formato electrónico o, excepcionalmente, en formato de informe, pero no en soporte magnético.

3.3 Las solicitudes deben cumplir los siguientes requisitos:

Se deberán realizar siempre de una manera centralizada, a través de la aseguradora, identificada por la clave con la que está inscrita en la Dirección General de Seguros y Fondos de Pensiones y su número de CIF, sin que una vez aportada la copia del mismo sea necesario remitirlo en cada solicitud, de conformidad con lo dispuesto en el artículo 35.f) de la Ley 30/1992, de Régimen Jurídico de las Administraciones Públicas y del Procedimiento Administrativo Común, salvo que hubiera modificaciones en el mismo.

En caso de que la petición sea de Informe, ésta deberá estar vinculada a un procedimiento judicial o expediente administrativo concreto que justifique dicha petición.

La aseguradora, además de indicar la matrícula del vehículo objeto de la consulta, deberá indicar el tipo de daños (personales, materiales o ambos), el CIF, la clave con la que figura inscrita en la Dirección General de Seguros y Fondos de Pensiones, la matrícula propia y el número de expediente de siniestro y de la póliza de seguro que consten en el registro exigido por el Reglamento de Ordenación y Supervisión de los Seguros Privados (en adelante ROSSP).

3.4 El aplicativo FIVA validará la petición, verificando:

Que la entidad comunica todos los datos obligatorios en el formato adecuado.

Que la matrícula comunicada como propia consta efectivamente en el FIVA como asegurada en dicha entidad en la fecha del siniestro.

Que la entidad comunica el número de expediente de siniestro.

Que la entidad comunica el número de póliza.

Que, en el caso excepcional de solicitarse informe escrito, en el registro se especifica el número de procedimiento judicial o administrativo y de la instancia que lo requiere, verificándose también que se cumplimentan el resto de los datos variables para emisión de informe.

3.5 Para cada solicitud correcta el sistema generará tantos registros de respuesta REFIVA como registros consten para el vehículo a consultar en la fecha de siniestro.

Si la matrícula a consultar en la fecha de siniestro figurara asegurada por una entidad que comunicó la baja con posterioridad a la fecha de siniestro y con efectividad de la baja anterior a la fecha de siniestro indicada, el sistema informará de la fecha de comunicación de la baja y de la fecha de efecto de la misma; en caso contrario, en la respuesta los campos de las fechas indicadas irán en blanco.

Si la entidad en la que figura asegurada la matrícula ha desaparecido por fusión, absorción o ha cedido la cartera del ramo de automóviles, el sistema informará del código de la nueva entidad aseguradora, su razón social y la fecha de fusión, absorción o cesión de cartera.

Si la matrícula no figura asegurada en ninguna entidad, el sistema lo notificará con el mensaje 806, pero la solicitud permanecerá durante un mes en el sistema por si se recibiera una comunicación de aseguramiento. En este caso se volverá a enviar el mensaje con la entidad aseguradora en la cual figura asegurado el vehículo en la fecha del siniestro. Si durante un mes no se recibe alta de la matrícula, la solicitud será borrada de las pendientes.

Si la entidad solicita informe, además de los mensajes electrónicos, el Consorcio de Compensación de Seguros expedirá los informes correspondientes.

Los informes siempre se dirigirán a la dirección consignada por la entidad en el registro de petición.

3.6 La respuesta estará disponible para la entidad aseguradora desde las seis horas del día siguiente a la fecha en que se formuló la consulta.

3.7 La aseguradora siempre recibirá un registro EDI con acuse de recibo, indicándole si la respuesta ha sido resuelta constando o no aseguramiento, o si la solicitud ha sido rechazada con algún código de error.

4. Descripción de los registros

Registro de solicitud de información

| Número | Nivel | Posición inicial | Longitud | Tipo de dato | Descripción | Formato |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 03 | 1 | 4 | N | Número de lote. | Secuencial. |
| 2 | 03 | 5 | 5 | N | Número de registro. | Secuencial. |
| 3 | 03 | 10 | 6 | AN | Tipo de registro. | CEFIVA. |
| 4 | 03 | 16 | 3 | N | Código de mensaje. | 801 \| 803. |
| 5 | 03 | 19 | 8 | N | Fecha de la petición. | AAAAMMDD. |
| 6 | 03 | 27 | 6 | N | Hora de la petición. | HHMMSS. |
| 7 | 03 | 33 | 4 | AN | Código de la entidad peticionaria. | Según DGS. |
| 8 | 03 | 37 | 10 | AN | C.I.F. |  |
| 9 | 03 | 47 | 24 | AN | N.o Expediente siniestro. Art. 65.1.c) ROSSP. |  |
| 10 | 03 | 71 | 24 | AN | N.o Póliza. Art. 65.1.c) ROSSP. |  |
| 11 | 03 | 95 | 2 | AN | Tipo matrícula a consultar. | Formato FIVA. |
| 12 | 03 | 97 | 12 | AN | Matrícula a consultar. | Formato FIVA. |
| 13 | 03 | 109 | 8 | N | Fecha a consultar. | AAAAMMDD. |
| 14 | 03 | 117 | 2 | AN | Tipo matricula asegurado. | Formato FIVA. |
| 15 | 03 | 119 | 12 | AN | Matrícula asegurado. | Formato FIVA. |
| 16 | 03 | 131 | 1 | AN | Tipo de daños. | P \| M \| A. |
| 17 | 03 | 132 | 6 | AN | Código de error. | (*). |
| 18 | 03 | 138 | 174 | AN | Datos variables para informe. |  |
| 19 | 05 | 138 | 24 | AN | N.o Procedimiento. |  |
| 20 | 05 | 162 | 24 | AN | Instancia. |  |
| 21 | 05 | 186 | 35 | AN | Dirección envío informe. |  |
| 22 | 05 | 221 | 5 | AN | Código postal envío informe. |  |
| 23 | 05 | 226 | 35 | AN | Localidad envío informe. |  |
| 24 | 05 | 261 | 20 | AN | Provincia envío informe. |  |
| 25 | 05 | 281 | 31 | AN | Nombre y apellidos del solicitante. |  |
| 26 | 03 | 312 | 14 | AN | Disponible. |  |

(*) Estructura y valores del código de error.

La estructura del código de error es la siguiente:

Posición 1: Valor fijo E.

Posición 2-3: Indica el tipo de error:

20. El código de mensaje no está permitido en el Tipo de Registro.

21. Estructura de registro errónea, se produce cuando el campo tipo de registro tenga un valor distinto de los permitidos.

22. La entidad emisora del mensaje no coincide con la definida para EDItran.

23. Petición de información de la matrícula del vehículo que nos facilitan como asegurado en la propia entidad que formula la consulta.

24. No constar en el FIVA, en la fecha del siniestro, la matrícula del vehículo asegurado por la entidad que solicita la información.

25. Ya se ha emitido original y duplicado del informe para esta consulta.

26. Ya se ha dado respuesta sobre la misma matrícula y la misma fecha.

27. Campo obligatorio no presente en el registro.

28. Error en el formato del campo.

29. Valor de campo erróneo.

Posiciones 4-5: Indica el número del campo erróneo. Siempre y cuando el error se deba a presencia, formato o valor de uno de los campos.

Registro de respuesta electrónica del FIVA

| Número | Nivel | Posición inicial | Longitud | Tipo de dato | Descripción | Formato |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 03 | 1 | 4 | N | Número de lote. | Secuencial. |
| 2 | 03 | 5 | 5 | N | Número de registro. | Secuencial. |
| 3 | 03 | 10 | 6 | AN | Tipo de registro. | REFIVA. |
| 4 | 03 | 16 | 3 | N | Código de mensaje. | 802 \| 804 \| 806. |
| 5 | 03 | 19 | 8 | N | Fecha de la respuesta. | AAAAMMDD. |
| 6 | 03 | 27 | 6 | N | Hora de la respuesta. | HHMMSS. |
| 7 | 03 | 33 | 4 | AN | Clave de la entidad peticionaria. | Según DGS. |
| 8 | 03 | 37 | 10 | AN | CIF. |  |
| 9 | 03 | 47 | 2 | AN | Tipo matrícula a consultar. | Formato FIVA. |
| 10 | 03 | 49 | 12 | AN | Matrícula a consultar. | Formato FIVA. |
| 11 | 03 | 61 | 24 | AN | N.o Expediente siniestro. Art.65.1.c) ROSSP. |  |
| 12 | 03 | 85 | 8 | N | Fecha que se consulta. | AAAAMMDD. |
| 13 | 03 | 93 | 122 | AN | Datos variables para respuesta. |  |
| 14 | 05 | 93 | 4 | AN | Clave de entidad aseguradora. |  |
| 15 | 05 | 97 | 35 | AN | Domicilio de la entidad aseguradora. |  |
| 16 | 05 | 132 | 8 | AN | Fecha de fusión o absorción. |  |
| 17 | 05 | 140 | 4 | AN | Clave de la nueva entidad aseguradora. |  |
| 18 | 05 | 144 | 35 | AN | Domicilio nueva entidad aseguradora. |  |
| 19 | 05 | 179 | 10 | AN | Disponible (*). |  |
| 20 | 05 | 189 | 10 | AN | Disponible (*). |  |
| 21 | 05 | 199 | 8 | AN | Fecha de comunicación de la baja. |  |
| 22 | 05 | 207 | 8 | AN | Fecha de la baja. |  |
| 23 | 03 | 215 | 111 | AN | Disponible. |  |

(*) Estos campos estaban asignados inicialmente al número de teléfono y número de fax del interlocutor designado por la entidad aseguradora del vehículo consultado. Dado que los destinatarios de la información contenida en el FIVA son los tramitadores de siniestros no se considera procedente facilitar estos datos.

5. Descripción de campos utilizados en los registros (por orden alfabético)

| Nombre del campo | Descripción |
| --- | --- |
| C.I.F. | C.I.F. de la entidad peticionaria. |
| Código entidad aseguradora. | Clave con la que la entidad que asegura al vehículo especificado en la fecha de siniestro está inscrita en la D.G.S. |
| Código de error. | Código por el que se ha rechazado la consulta, el formato es Emmnn, donde mm es el motivo y nn en el campo al cual se refiere. |
| Código de la entidad peticionaria. | Clave con la que la entidad aseguradora que emite la petición está inscrita en la D.G.S. |
| Código de la nueva entidad aseguradora. | Clave con la que la nueva entidad aseguradora donde figura asegurado el vehículo por haber desaparecido la anterior por fusión, absorción o cesión de cartera está inscrita en la D.G.S. |
| Código de mensaje. | Describe la interpretación que se debe hacer del contenido del registro. Los valores posibles son los descritos en el apartado descripción de los mensajes. |
| Código postal envío informe. | Código postal. |
| Datos variables para informe. | Los informes se dirigen a la dirección que figura en el registro de petición. |
| Datos variables para respuesta. | Datos variables en función de la respuesta que se ofrece. |
| Destinatario envío informe. | Destinatario del informe. |
| Dirección envío informe. | Dirección a la que se envía el informe. |
| Disponible. | Reservado para uso futuro. |
| Domicilio entidad aseguradora. | Domicilio social de la entidad aseguradora en la que figura asegurado el vehículo. |
| Domicilio nueva entidad aseguradora. | Nuevo domicilio social de la entidad aseguradora en la que figura asegurado el vehículo por haber desaparecido la anterior por fusión, absorción o cesión de cartera. |
| Fecha de siniestro. | Fecha en la que se desea conocer la entidad en la cual figura asegurada la matrícula a consultar. |
| Fecha de comunicación de la baja. | Fecha en que la entidad en la cual figura el vehículo que se consulta comunicó la baja. |
| Fecha de fusión, absorción o cesión de cartera. | Fecha en que la entidad donde figura asegurado el vehículo ha sido absorbida, se ha fusionado o ha cedido la cartera a la entidad especificada en el campo. Razón social de la nueva entidad. |
| Fecha de la baja. | Fecha de efecto de la baja. |
| Fecha de la petición. | Fecha en que la petición llega al FIVA. |
| Fecha de la respuesta. | Fecha en que el FIVA emite la respuesta. |
| Hora de la petición. | Hora en que la petición llega al FIVA. |
| Hora de la respuesta. | Hora en que el FIVA emite la respuesta. |
| Instancia. | Organismo o juzgado ante el cual debe presentarse el informe. |
| Localidad envío informe. | Localidad donde se desea recibir el informe. |
| Matrícula a consultar. | Matrícula que se desea consultar. |
| Matrícula asegurado. | Matrícula del asegurado propio. |
| Número de lote. | Número identificador del fichero que remite la entidad al FIVA. |
| Número de registro. | Número identificador del registro dentro del fichero que remite la entidad al FIVA. |
| N.o expediente siniestro. | Número de expediente al que corresponde el siniestro. [Art. 65.1.c) ROSSP]. |
| N.o póliza. | N.o póliza. [Art. 65.1.c) ROSSP]. |
| N.o procedimiento judicial o administrativo. | N.o del procedimiento o del expediente que se tramita por el organismo o juzgado indicado en el campo «Instancia», al que está vinculada la petición de informe. |
| Provincia envío informe. | Provincia donde se desea recibir el informe. |
| Tipo de daños. | Tipo de daños. P-T Daños personales, M-T Daños materiales, A-T Ambos. |
| Tipo de registro. | Identificador del contenido del registro, los valores posibles son CEFIVA y REFIVA. |
| Tipo matrícula a consultar. | Tipo de matrícula que se desea consultar. |
| Tipo matricula asegurado. | Tipo de matrícula del asegurado propio. |

6. Datos de las sesiones EDItran

Especificaciones para las sesiones EDItran para la consulta electrónica de información al FIVA:

EDITRAN/P

|  | Entidad | Servicio FIVA |
| --- | --- | --- |
| Versión. |  |  |
| Código remoto. |  | 000080950 |
| Nombre. |  | SERVICIO FIVA |
| Aplicación. | FIVA08 | FIVA08 |
| Standard de comunicación. | X.25 X.28 TCP/IP |  |
| Nro. reg./bloque emisión. | 010 | 010 |
| Longitud tampón. | 4050 | 4050 |
| Cobro revertido. | S N | N |
| Extremo llamante. | L | R |
| Forma de pago. | L | R |
| Sentido tráfico. | X | X |
| Llamada automática. | S | S |
| CRC. | S | S |
| Desconexión autom. | S | S |
| Servidor/cliente. | C | S |
| ASCII/EBCDIC. | A E |  |
| Compresión. | S N |  |
| Hora inicio. | 06:00:00 | 06:00:00 |
| Hora fin. | 00:00:00 | 00:00:00 |
| Time-out. |  | 100 |
| Nro. máximo reintentos. |  | 3 |
| Sincronismo aplic. | S N | N |
| NRI local. |  | 3140263010 3140262510 3140256810 |
| NRI remoto. | 3140263010 3140262510 3140256810 |  |
| Criptografía. | N | N |

EDITRAN/G

|  | Entidad | Servicio FIVA |
| --- | --- | --- |
| Versión. |  | 3.1 |
| Compresión. | F N | F |
| ASCII/EBCDIC. | A E |  |
| Traducción ASCII/EBCDIC. | S N |  |
| Criterio división. | N | N |
| Formato ficheros aplic. | F | F |
| Longitud registros aplic. | 325 | 325 |
| Incrementar no presentación. | N | N |
| Aplicación EDItran/P. | FIVA08 | FIVA08 |

La entidad deberá rellenar los datos que la corresponda y marcará con una X la opción correcta.

Los campos en blanco relativos a SERVICIO FIVA dependerán del parámetro correspondiente que fije la entidad.

> Redactado el punto 3 conforme a la corrección de erratas y errores publicada en BOE núm. 74 de 27 de marzo de 2001. Ref. BOE-A-2001-5985
