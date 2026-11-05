## ANEXO I

## Procedimientos y formatos de matrícula

1. Procedimientos aplicables

1.1 Características generales:

El Fichero Informativo de Vehículos Asegurados (en adelante FIVA) debe contener los datos relativos a todos los vehículos con estacionamiento habitual en España que estuvieran asegurados por la entidad aseguradora en la cobertura de responsabilidad civil de suscripción obligatoria que se especifican en el artículo 24 del Real Decreto 7/2001, de 12 de enero.

Todos los envíos se realizarán mediante el Sistema de Transferencia de Ficheros (en adelante STF) que sea utilizado por el servicio FIVA del Consorcio de Compensación de Seguros (actualmente sistema EDItran). Dicho sistema se contratará previamente por cada entidad aseguradora para que pueda ser dada de alta en el FIVA.

La entidad aseguradora debe contactar con el Centro de Proceso de Datos (en adelante CPD) para configurar la conexión.

La periodicidad de los envíos será diaria. Cada entidad aseguradora tendrá asignada una ventana horaria para el envío de la información.

El CPD procederá al tratamiento de toda la información recogida y, por tanto, a la actualización del FIVA, todos los días (excepto sábados, domingos y fiestas nacionales) a partir de las cero horas y hasta las cuatro horas.

En caso de imposibilidad de realizar el envío de un fichero se pondrá en marcha un procedimiento de excepción, consistente en la remisión al CPD de un soporte magnético con la información y las características señaladas en los apartados 2 y 3 de este anexo, y conforme se detalla en el procedimiento recogido en el apartado 1.6 del mismo.

Terminado el proceso de tratamiento de información, se generará un fichero de confirmación para cada una de las entidades aseguradoras que hubiese enviado datos.

Los registros rechazados y devueltos por el CPD a la entidad aseguradora deberán reenviarse por ésta en la siguiente sesión. A estos efectos, también se consideran registros rechazados todos aquellos envíos que contuvieran un fichero de carga o de actualización rechazado por un motivo concreto, que se pondrá en conocimiento de la entidad, y que, por lo tanto, no hubiese llegado a ser procesado por el CPD.

1.2 Mantenimiento del registro de las entidades aseguradoras en el FIVA.‒Alta de entidades:

Antes de realizar el primer envío, la entidad aseguradora comunicará al servicio FIVA del Consorcio de Compensación de Seguros el inicio de la actividad, y éste dará de alta a la entidad en la base de datos, requisito imprescindible para que puedan procesarse los ficheros de aquélla. Para ello, la entidad aportará los siguientes datos:

Clave de la entidad en el Registro de la Dirección General de Seguros y Fondos de Pensiones.

CIF de la entidad.

Domicilio (dirección, localidad, provincia y código postal).

Interlocutor:

Nombre y apellidos.

Teléfono.

Fax.

Correo electrónico.

Fecha de inicio efectivo de actividad.

Número remoto (identifica el STF).

Fin de actividad.

La entidad aseguradora que deje de operar en el seguro de suscripción obligatoria debe comunicar al Consorcio de Compensación de Seguros la fecha de finalización de su actividad con relación al FIVA, una vez tenga constancia de la baja de todas sus matrículas en el FIVA mediante el fichero de confirmación.

1.3 Ficheros de carga inicial y actualizaciones diarias.‒La primera remisión de datos o carga inicial se realizará tan pronto como la entidad aseguradora hubiese comenzado a operar, ya sea en régimen de derecho de establecimiento o de libre prestación de servicios.

Las entidades aseguradoras enviarán al FIVA diariamente las actualizaciones producidas en su cartera de seguros de automóviles de responsabilidad civil de suscripción obligatoria, tanto en lo que respecta a las nuevas altas como a las bajas.

La descripción de este fichero está especificada en el apartado 2 de este anexo I.

1.4 Fichero de confirmación.‒Este fichero podrá ser recogido por cada entidad aseguradora a partir de la hora de fin de tratamiento ya especificada en el apartado 1.1.

A través de la información que contiene este fichero, la entidad aseguradora conocerá el resultado completo del proceso y, por tanto, si el fichero enviado por ella ha sido tratado o ha sido rechazado, y el motivo del rechazo; y, en el caso de que el fichero hubiese sido tratado y no rechazado, la entidad conocerá qué registros del fichero han sido tratados y, en su caso, cuáles han sido rechazados y los motivos de los rechazos.

La descripción de este fichero está especificada en el apartado 2 de este anexo I.

1.5 Controles y avisos por deficiencias y errores en el envío de información por la entidad aseguradora.‒Los siguientes controles y avisos permiten a las entidades aseguradoras corregir las deficiencias que, en su caso, hubieren cometido en el envío de información al FIVA. Es esencial que las entidades aseguradoras estén especialmente atentas a la posible aparición de alguna de las situaciones que a continuación se describen y reaccionen inmediatamente ante las mismas, para garantizar así la fiabilidad de los datos que suministran al FIVA y la veracidad de los informes de aseguramiento de los vehículos que emite el Consorcio de Compensación de Seguros en cumplimiento de la función que en esta materia le asigna la legislación.

1.5.1 Rechazo por el FIVA del fichero de carga inicial o de actualización de datos completo.‒Una vez enviada la información por la entidad aseguradora, el sistema valida la información recibida y devuelve a la entidad un fichero de confirmación de la transmisión, que contiene dos tipos de registros, cuyo diseño se contiene en el apartado 2.4 de este anexo: El registro de cabecera, para identificar el lote confirmado, y el resto de registros.

El registro de cabecera puede adoptar varios códigos de control: Si la transmisión ha sido correcta, adoptará el valor 00; pero los valores distintos al 00 ponen de manifiesto la existencia de errores e indican que todos los datos transmitidos por la entidad aseguradora han sido rechazados y, por tanto, no han accedido al FIVA.

Por eso, ante ese aviso, la entidad aseguradora deberá enviar de inmediato el fichero con las correcciones necesarias, indicando como número de lote el inicialmente rechazado o, alternativamente, incorporar los registros que contiene el fichero rechazado en el siguiente fichero o lote que remita la entidad. En ambos casos la entidad recibirá el correspondiente fichero de confirmación. En las aplicaciones informáticas del CPD quedará constancia de todos los ficheros de confirmación que se hubieran producido para un mismo fichero de carga o de actualización.

El envío por una entidad en un día determinado de un único fichero se equiparará, en el caso de que el fichero fuese rechazado, a un día sin remisión de datos, a los efectos de lo señalado en el apartado 1.5.3.

1.5.2 Rechazo por el FIVA de registros concretos erróneos.–El resto de registros los envía la aplicación FIVA a la entidad aseguradora solamente en el caso de que el fichero se haya procesado, es decir, cuando el código de control del registro de cabecera, por no contener éste errores, adopta el valor 00 antes indicado y se hayan detectado registros erróneos, que se devolverán con indicación del consiguiente código de error expresivo del tipo de error que, en concreto, se hubiese producido, para facilitar así a la entidad aseguradora el conocimiento de los errores cometidos por ella y el motivo de los mismos. En estos casos, a diferencia del anterior, no se produce un rechazo del fichero completo, sino que se confirma que el fichero se ha procesado y, a su vez, se devuelven rechazados los registros erróneos que, en concreto, se han detectado. Por tanto, se actualiza así la información del FIVA en cuanto a los registros correctos, pero queda pendiente de actualizar por los registros erróneos.

Estos registros rechazados por el FIVA deberán reenviarse, corregidos, por la entidad aseguradora en la siguiente sesión.

1.5.3 Aviso por falta de envío diario de información al FIVA por parte de la entidad aseguradora.‒En el caso de que una entidad aseguradora no remita datos durante cinco días consecutivos, el CPD enviará un fax o un e-mail de aviso a la persona de contacto especificada, indicándole la obligatoriedad del envío diario de los mismos.

1.5.4 Otros avisos y controles.‒A través del CPD, se facilitará a las entidades aseguradoras información periódica sobre los vehículos con registros erróneos pendientes de resolver por la entidad; información sobre todas las matrículas aseguradas por la entidad que consten en el FIVA; o cualquier otro tipo de información que el Consorcio de Compensación de Seguros considere apropiado remitir, todo ello con la finalidad de que las entidades puedan comparar dichas informaciones con sus documentos y registros internos y subsanar con la necesaria rapidez las deficiencias que, en su caso, hubieran cometido en el suministro de información al FIVA.

Las entidades aseguradoras desarrollarán las aplicaciones informáticas necesarias para tratar adecuadamente, con arreglo a la finalidad expuesta en el párrafo anterior, la información recibida del CPD.

1.6 Definición del procedimiento de excepción.‒En el caso de que las líneas o los sistemas electrónicos de transferencia fallen y no se tenga certeza del momento de su recuperación, se utilizará un medio alternativo que garantice la recepción de los datos en el CPD o la recepción del fichero de confirmación por parte de la entidad aseguradora dentro del plazo previsto.

El procedimiento de excepción consiste en el envío de un soporte magnético desde la entidad aseguradora afectada al CPD o viceversa, de acuerdo con la secuencia que se describe a continuación:

Cuando la entidad aseguradora intente establecer la conexión con el CPD y no lo consiga, cursará aviso telefónico al CPD, donde se analizarán las causas de la incidencia. En función del diagnóstico de la incidencia y si el tiempo transcurrido desde su detección ha superado veinticuatro horas, se pondrá en marcha el procedimiento de excepción.

La entidad afectada generará el soporte magnético correspondiente y, para avisar del envío del mismo, contactará telefónicamente con el CPD, que comunicará a la entidad un control de acceso que deberá llevar adherido el soporte.

La entidad afectada enviará el soporte al CPD.

El CPD realizará las comprobaciones necesarias, estableciendo los mecanismos de seguridad adecuados para verificar la seguridad de la procedencia del envío.

La devolución del fichero de confirmación por parte del CPD, una vez realizados los procesos pertinentes, se hará previo contacto telefónico con el usuario responsable de avisar del envío del soporte, a la atención y dirección indicada por el usuario receptor responsable.

La entidad aseguradora realizará las comprobaciones necesarias, estableciendo los mecanismos de seguridad adecuados que garanticen la recepción del envío.

Todos estos envíos de información habrán de ir acompañados de acuse de recibo, donde constarán las horas de salida de los datos y de entrega en el destinatario, y de los mecanismos de seguridad que garanticen el origen del soporte.

La información afectada quedará registrada en los sistemas de gestión del CPD como efectivamente recibida o enviada, una vez se tenga constancia del acuse de recibo.

En el supuesto de que una entidad aseguradora tenga que realizar un envío ocasional de carácter masivo de registros de altas o bajas (verbigracia, traspaso de matrículas por fusión de entidades aseguradoras o cesión de cartera), y con la finalidad de no retrasar el horario establecido en este anexo para el proceso diario del CPD, también se puede enviar un soporte magnético, previo aviso telefónico al CPD y con las mismas garantías descritas anteriormente.

1.7 Comunicaciones entre las entidades aseguradoras y el Consorcio de Compensación de Seguros.‒Las entidades aseguradoras mantendrán actualizados los datos del interlocutor y coordinarán a través de éste todas las relaciones de la entidad con el servicio FIVA del Consorcio y con el CPD.

A su vez, el Consorcio de Compensación de Seguros facilitará a las entidades aseguradoras información actualizada sobre sus interlocutores en el servicio FIVA y en el CPD.

2. Formatos de los ficheros y datos

En este apartado se detallan los campos que componen los diferentes ficheros que se intercambian entre las entidades aseguradoras y el CPD para la carga, el mantenimiento y gestión del FIVA.

2.1 Fechas.‒Las cuatro fechas que trata el FIVA son las siguientes:

Fecha de inicio de vigencia del contrato de seguro: Corresponde a la fecha de entrada en vigor y, por tanto, de comienzo de las coberturas del contrato de seguro, de la solicitud o de la proposición.

Fecha de finalización del período de cobertura: Corresponde a la fecha de término del contrato de seguro, de la solicitud o de la proposición.

Fecha de cese de la vigencia del contrato de seguro: Corresponde a la fecha de cese de la vigencia del contrato. A estos efectos se entiende por cese de la vigencia del contrato cualquier forma de extinción del contrato, incluida la rescisión y la resolución, de acuerdo con la Ley de Contrato de Seguro.

Fecha de comunicación al centro de cálculo: Autoexplicativa. Es asignada automáticamente a la recepción.

2.2 Descripción general de los campos de los registros.‒El nombre de los campos vendrá especificado al final con XX, que se deberá interpretar como el sufijo que diferencia dichos campos de los distintos registros a que pertenecen.

CODENT-XX:

Clave con la que la entidad aseguradora está inscrita en la Dirección General de Seguros y Fondos de Pensiones.

Estará compuesto por cuatro dígitos: El primero será una letra (M, E, C, L) y los tres restantes numéricos.

NUMLOT-XX:

Identifica el número de lote o fichero de envío. Es un número de asignación secuencial para control de envío.

CONREG-XX:

Identifica el número de registros que contiene el fichero enviado, excluido el registro de cabecera. Es un campo de ocho posiciones, de carácter numérico.

CODCON-XX:

Código de control, que informa acerca de si el fichero ha sido efectivamente transmitido o si, por el contrario, no ha accedido al FIVA y, en este último supuesto, acerca de la deficiencia que ha impedido la transmisión.

00: Transmisión correcta.

01: Registro de cabecera no identificado.

02: Formato de clave de entidad erróneo.

03: Entidad no dada de alta en FIVA.

04: Remitente del fichero no corresponde a entidad de cabecera.

05: Formato fecha de envío erróneo.

06: Fecha de envío incorrecta.

07: Formato de número de registros erróneo.

08: Número de registros distinto de registros recibidos.

09: Formato de número de lote erróneo.

10: Lote duplicado.

11: Entidad sin actividad.

TIPMAT-XX:

Identifica el tipo de matrícula. Va unido al campo MATVEH-XX.

MATVEH-XX:

Identifica la matrícula del vehículo. Es un campo de 12 posiciones alfanumérico.

TIPVEH-XX:

Identifica la marca y modelo del vehículo. En tanto no se desarrolle un sistema de codificación de modelos de vehículos que pudiera ser aplicable a todas las entidades aseguradoras, este código estará integrado por las cuatro primeras letras de la marca del vehículo.

TIPACC-XX:

Identifica el tipo de acción a realizar con el registro, pudiendo ser las siguientes:

«A»: Alta

«B»: Baja.

«D»: Borrar el registro de errores pendientes de resolución.

FECVIG-XX:

Identifica la fecha de inicio de vigencia del contrato de seguro. Formato AAMMDD. El FIVA renovará automáticamente los siguientes períodos de vigencia en los contratos de cobertura anual (tipo C), salvo que la entidad envíe un registro de baja.

FECFIN-XX:

Identifica la fecha de finalización del período de cobertura de contrato de seguro. Formato AAMMDD. Este dato se consignará cuando el tipo de acción a realizar con el registro se identifique con «A» (alta).

FECENV-XX:

Identifica la fecha de envío al CPD. Formato AAMMDD. Debe ser menor o igual a la fecha del día.

FECCES-XX:

Identifica la fecha de cese de la vigencia del contrato de seguro. Formato AAMMDD. Este dato se consignará cuando el tipo de acción a realizar con el registro se identifique con «B» (baja).

TIPCON-XX:

Identifica el tipo de contrato de seguro, pudiendo ser los siguientes:

«C»: Contrato de cobertura anual.

«T»: Contrato de cobertura temporal.

«S»: Solicitud de seguro.

«P»: Proposición de seguro.

CODERR-XX:

Código de error. Identifica un error en un registro. Los valores posibles son:

12: Valor de tipo de matrícula incorrecto.

20: Falta el campo obligatorio matrícula.

21: Error en formato de matrícula.

24: Alta rechazada por solaparse con otro período.

25: Baja rechazada por encontrarse el registro dado de baja.

26: Baja rechazada por no identificar el vehículo (matrícula más marca).

27: Registro duplicado.

30: Falta el campo obligatorio marca vehículo.

31: Error en formato de marca vehículo.

32: Valor de marca de vehículo incorrecto.

42: Valor en tipo de acción incorrecto.

50: Fecha inicio período de cobertura obligatoria.

51: Error en formato de fecha de inicio del período de cobertura.

52: Valor de fecha de inicio del período de cobertura incorrecto.

60: Fecha fin período de cobertura o fecha de baja obligatoria.

61: Error en formato de fecha de fin de período de cobertura o fecha de baja.

62: Valor de fecha fin período de cobertura o fecha de baja incorrecto.

63: Fecha de fin de período de cobertura o baja anterior al de inicio de vigencia.

64: Fecha de baja menor a fecha fin período de cobertura del período anterior.

65: Baja fuera de período en contrato no renovable.

70: Falta el campo obligatorio tipo de contrato.

72: Error en valor de tipo de contrato.

FILLER: Campo disponible para uso futuro.

2.3 Diseño del fichero para la carga inicial y para las actualizaciones diarias.

Registro de cabecera:

| Orden | Campo | Nombre | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | Código entidad. | CODENT-21 | 4 | Alfanumérico. | Clave con la que la entidad está inscrita en la DGS. |
| 2 | Fecha envío. | FECENV-21 | 6 | Numérico. | (AAMMDD) Corresponde al año, mes y día en que se obtiene la información. |
| 3 | Número registros. | CONREG-21 | 8 | Numérico. | Número total de registros enviados. |
| 4 | Número de lote del envío. | NUMLOT-21 | 5 | Numérico. | Número secuencial de 0 a 99999. |
| 5 | Filler. | FILLER | 41 | Alfanumérico. | Disponible. |

Resto de registros:

| Orden | Campo | Nombre | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | Tipo formato matrícula | TIPMAT-22 | 2 | Alfanumérico. | Véase apartado 3 de este anexo. |
| 2 | Matrícula. | MATVEH-22 | 12 | Alfanumérico. | Véase apartado 3 de este anexo. |
| 3 | Abreviatura marca vehículo. | TIPVEH-22 | 9 | Alfanumérico. | Cuatro primeras posiciones del nombre de la marca del vehículo. |
| 4 | Tipo de acción. | TIPACC-22 | 1 | Alfanumérico. | «A» Alta vehículo. «B» Baja vehículo. «D» Borrar registro de error. |
| 5 | Fecha de inicio vigencia contrato. | FECVIG-22 | 6 | Numérico. | AAMMDD. |
| 6 | Fecha finalización del período de cobertura o fecha cese de vigencia. | FECFIN-22 FECCES-22 | 6 | Numérico. | AAMMDD. Si TIPACC-22 = «A». AAMMDD. Si TIPACC-22 = «B». |
| 7 | Tipo de contrato (*). | TIPCON-22 | 1 | Alfanumérico. | Identifica contrato anual, temporal, solicitud o proposición. |
| 8 | Filler. | FILLER | 27 | Alfanumérico. | Disponible. |

(*) Este campo identifica si es un documento de cobertura provisional (solicitud o proposición) o se trata de un contrato definitivo de cobertura anual o temporal. El valor de este campo puede ser:

«C»: Contrato de cobertura anual.

«T»: Contrato de cobertura temporal.

«S»: Solicitud de seguro.

«P»: Proposición de seguro.

2.4 Diseño del fichero de confirmación.

Registro de cabecera:

| Orden | Campo | Nombre | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | Código entidad. | CODENT-31 | 4 | Alfanumérico. | Clave con la que la entidad está inscrita en la DGS. |
| 2 | Número de lote confirmado. | NUMLOT-31 | 5 | Numérico. | Número secuencial de 0 a 99999. |
| 3 | Código de control (*). | CODCON-31 | 2 | Numérico. | Informa del resultado de la transmisión. |
| 4 | Número registros erróneos. | CONREG-31 | 8 | Numérico. | Número total de registros enviados. |
| 5 | Filler. | FILLER | 45 | Alfanumérico. | Disponible. |

(*) Los valores del código de control pueden ser:

00: Transmisión correcta.

01: Registro de cabecera no identificado.

02: Formato de clave de entidad erróneo.

03: Entidad no dada de alta en FIVA.

04: Remitente del fichero no corresponde a entidad de cabecera.

05: Formato fecha de envío erróneo.

06: Fecha de envío incorrecta.

07: Formato de número de registros erróneo.

08: Número de registros distinto de registros recibidos.

09: Formato de número de lote erróneo.

10: Lote duplicado.

11: Entidad sin actividad.

Los valores distintos de «00» supondrán el rechazo de todos los datos transmitidos y, por tanto, se deberá enviar el fichero con las correcciones necesarias e indicando, como número de lote, el inicial rechazado.

Resto de registros: (Sólo en caso de código de control con valor 00).

| Orden | Campo | Nombre | Longitud | Formato | Observaciones |
| --- | --- | --- | --- | --- | --- |
| 1 | Tipo formato matrícula. | TIPMAT-32 | 2 | Alfanumérico. | Véase apartado 3 de este anexo. |
| 2 | Matrícula. | MATVEH-32 | 12 | Alfanumérico. | Véase apartado 3 de este anexo. |
| 3 | Abreviatura marca vehículo. | TIPVEH-32 | 9 | Alfanumérico. | Cuatro primeras posiciones del nombre de la marca del vehículo. |
| 4 | Tipo de acción. | TIPACC-32 | 1 | Alfanumérico. | «A» alta vehículo. «B» baja vehículo. «D» Borrar registro de error. |
| 5 | Fecha de inicio vigencia contrato. | FECVIG-32 | 6 | Numérico. | AAMMDD. |
| 6 | Fecha finalización del período de cobertura o fecha cese de vigencia. | FECFIN-3 FECCES-32 | 6 | Numérico. | AAMMDD. Si TIPACC-22 = «A». AAMMDD. Si TIPACC-22 = «B». |
| 7 | Tipo de contrato. | TIPCON-32 | 1 | Alfanumérico. | Identifica contrato anual, temporal, solicitud o proposición. |
| 8 | Código de error (*). | CODERR-32 | 2 | Numérico. | Error detectado en registro. |
| 9 | Filler. | FILLER | 25 | Alfanumérico. | Disponible. |

(*) Los valores del código de error pueden ser:

12: Valor de tipo de matrícula incorrecto.

20: Falta el campo obligatorio matrícula.

21: Error en formato de matrícula.

24: Alta rechazada por solaparse con otro período.

25: Baja rechazada por encontrarse el registro dado de baja.

26: Baja rechazada por no identificar el vehículo (matricula + marca).

27: Registro duplicado.

30: Falta el campo obligatorio marca vehículo.

31: Error en formato de marca vehículo.

32: Valor de marca de vehículo incorrecto.

42: Valor en tipo de acción incorrecto.

50: Fecha inicio período de cobertura obligatoria.

51: Error en formato de fecha de inicio del período de cobertura.

52: Valor de fecha de inicio del período de cobertura incorrecto.

60: Fecha fin período cobertura o fecha de baja obligatoria.

61: Error en formato de fecha de fin de período de cobertura o fecha de baja.

62: Valor de fecha fin período de cobertura o fecha de baja incorrecto.

63: Fecha de fin de período de cobertura o baja anterior al de inicio de vigencia.

64: Fecha de baja menor a fecha fin período de cobertura del período anterior.

65: Baja fuera de período en contrato no renovable.

70: Falta el campo obligatorio tipo de contrato.

72: Error en valor de tipo de contrato.

Los registros rechazados por el CPD deberán reenviarse, corregidos, en la siguiente sesión.

3. Diseño de la estructura y del tipo de matrículas.

Siendo la matrícula el dato fundamental, es imprescindible que tenga un formato común para todas las entidades.

Dicho formato se ha determinado teniendo en cuenta la estructura de matrículas prevista en el Código de Circulación y en el Real Decreto 2822/1998, de 23 de diciembre, por el que se aprueba el Reglamento General de Vehículos («Boletín Oficial del Estado» de 26 de enero de 1999), y en la Orden de 15 de septiembre de 2000 («Boletín Oficial del Estado» de 16 de septiembre de 2000), por la que se modifica el anexo VIII de dicho Reglamento.

Ante la diversidad de formatos contenidos en la normativa mencionada, es necesario establecer un código de «tipo de matrícula» para posibilitar la diferenciación de las mismas.

Los formatos de la matrícula y del tipo de matrícula son:

Matrícula (12X): 12 posiciones alfanuméricas.

Tipo de matrícula (2X): 2 posiciones alfanuméricas.

Matrículas del Parque Automovilístico Español

| Tipo | Formato | Ejemplos | Observaciones |
| --- | --- | --- | --- |
| « » | 4N 3X 5X 2X 6N 2X 2X (*) | 1234 BCD V-1234-AB MA-123456 | Nueva matrícula vehículos automóviles (Orden de 15 de septiembre de 2000, «Boletín Oficial del Estado» del 16). Vehículos automóviles (matrícula actual). Vehículos automóviles (matrícula antigua). |
| E | 2X 6N 2X 2X (*) (1) | AL-12345-VE | Vehículos especiales. |
| E1 | 1X 4N 3X 4X (1) | E-2345-BCD | Vehículos especiales (3). |
| R | 2X 6N 1X 3X (*) (1) | TO-123456-R | Remolques y semirremolques. |
| R1 | 1X 4N 3X 4X (1) | R-2345-BCD | Remolques y semirremolques (3). |
| C | 1X 4N 3X 4X (1) | C-2345-BCD | Ciclomotores (3). |
| D | 2X 3N 3N 4X (1) | CD-012-012 | En régimen diplomático (3). |
| T | 2N 2X 4N 4N (*) (MMAA) | 12-GI-1234 XI93 | Turística. |
| T1 | 1X 4N 3X 4X (1) | T-2345-BCD | Turística (3). |
| H | 1X 4N 3X 4X (1) | H-2345-BCD | Vehículo histórico (3). |
| TE | 2X 4N 1X 2N 3X (*) (1) | SA-1234-T-12 M-1234-R-12 | Temporal a cinco días. Temporal a treinta días |
| TT | 1X 4N 3X 4X (1) | P-2345-BCD | Autorización temporal a particulares y empresas (3). |
| P | 2X 2N 1X 4N 3X (*) (1) (SAA) | CA-12-P-1234 ISEM/93 B-12-T-1234 2SEM/94 | Pruebas. Transportes. |
| I | 2X 3X 4N 3X (*) (1) | BU-ITV-1234 | Inspección Técnica de Vehículos. |
| M | 3X 6N 2X 1X (2) | DGP-1234-AB PGC-123456 | Vehículos del Estado (3). |
| M1 | 3X 2X 6N 1X (2) | PME-VE-234567 | Vehículos del Estado (3). |
| K | 12X | 12-NXT-92 | Otras. |

(*) Validar con Tabla de Provincias

(1) Valor constante y fijo.

(2) Validar contra tabla de matrículas de vehículos pertenecientes al Estado.

(3) Reglamento General de Vehículos. Anexo XVIII (Placas de matrículas) del Real Decreto 2822/1998, de 23 de diciembre («Boletín Oficial del Estado» 26 de enero de 1999).

Tipo ” ” (blancos):

Vehículos automóviles (Orden de 15 de septiembre de 2000).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 4N | Campo numérico de cuatro posiciones desde 0000 al 9999 ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ, Q, CH y LL. |
| 5X | Campo vacío relleno con blancos. |

Vehículos automóviles (matrícula actual y antigua).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos, para validar con la tabla de provincias. |
| 6N | Campo numérico de seis posiciones, desde 000000 al 999999 ajustado a la derecha y relleno con ceros. |
| 2X | Campo alfanumérico de dos posiciones, desde A a ZZ, ajustado a la derecha y relleno con blancos. Si el campo anterior es superior a 9999, este campo debe contener blancos. |
| 2X | Campo alfanumérico de dos posiciones relleno con blancos. |

Tipo «E». Vehículos especiales.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos para validar con la tabla de provincias. |
| 6N | Campo numérico de seis posiciones, desde 000000 al 999999, ajustado a la derecha y relleno con ceros. |
| 2X | Este campo debe contener el valor fijo «VE». |
| 2X | Campo vacío relleno con blancos. |

Tipo «E1». Vehículos especiales (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con valor fijo «E». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «R». Remolques y semirremolques.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos para validar con la tabla de provincias. |
| 6N | Campo numérico de seis posiciones, desde 000000 al 999999, ajustado a la derecha y relleno con ceros. |
| 1X | Este campo debe contener el valor fijo «R». |
| 3X | Campo vacío relleno con blancos. |

Tipo «R1». Remolques y semirremolques.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con valor fijo «E». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «C». Ciclomotores (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con valor fijo «C». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «D». En Régimen Diplomático (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Valor fijo «CD», «OI», «CC» o «TA». |
| 3N | Tres dígitos del 000 al 999. Ajustados a la derecha y rellenos con ceros. |
| 3N | Tres dígitos del 000 al 999. Ajustados a la derecha y rellenos con ceros. |
| 4X | Campo vacío relleno con blancos. |

Tipo «T». Turística.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2N | Dos dígitos del 00 al 99. Ajustados a la derecha y rellenos con ceros. |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos, para validar con la tabla de provincias. |
| 4N | Cuatro dígitos del 0000 al 9999. Ajustados a la derecha y rellenos con ceros. |
| 4N | Mes y año. Formato MMAA (No obligatorio). |

Tipo «T1». Turística (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con valor fijo «T». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «H». Vehículo Histórico (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con valor fijo «H». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «TE». Temporal a cinco/treinta días.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos para validar con la tabla de provincias. |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y rellenos con ceros. |
| 1X | Este campo debe contener el valor fijo «T» o «R». |
| 2N | Campo numérico de dos posiciones, desde 00 al 99, ajustado a la derecha y relleno con ceros. |
| 3X | Campo vacío relleno con blancos. |

Tipo «TT». Autorización temporal a particulares y empresas (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 1X | Campo alfanumérico con los posibles valores «P», «V» o «S». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo alfanumérico de tres posiciones, desde BBB a ZZZ. Se suprimen vocales y Ñ y Q. |
| 4X | Campo vacío relleno con blancos. |

Tipo «P». Pruebas o transportes.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos para validar con la tabla de provincias. |
| 2N | Campo numérico de dos posiciones, desde 00 al 99, ajustado a la derecha y relleno con ceros. |
| 1X | Este campo debe contener el valor fijo «T» o «P». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3N | (SAA) 1 ó 2 (semestre), AA (año). No obligatorio. |

Tipo «I». Inspección Técnica de Vehículos (ITV).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 2X | Código de provincia de dos caracteres alfabéticos ajustados a la izquierda y relleno con blancos para validar con la tabla de provincias. |
| 3X | Este campo debe contener el valor fijo «ITV». |
| 4N | Campo numérico de cuatro posiciones, desde 0000 al 9999, ajustado a la derecha y relleno con ceros. |
| 3X | Campo vacío relleno con blancos. |

Tipo «M». Vehículos del Estado (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 3X | Ver tabla de organismos oficiales. Tres caracteres alfabéticos. Ajustados a la izquierda y rellenos con blancos. |
| 6N | Campo numérico de seis posiciones, desde 000000 al 999999, ajustado a la derecha y relleno con ceros. |
| 2X | Campo alfabético de dos posiciones, desde A ZZ, ajustado a la derecha y relleno con blancos. Si el campo anterior es superior a 9999, este campo debe contener blancos. |
| 1X | Campo vacío relleno con blancos. |

Tipo «M1». Vehículos del Estado V. E. (Real Decreto 2822/1998).

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 3X | Ver tabla de organismos oficiales. Tres caracteres alfabéticos. Ajustados a la izquierda y rellenos con blancos. |
| 2X | Campo alfanumérico de dos posiciones rellenos a blancos, salvo cuando se trate de vehículos especiales, que tendrán el valor fijo «VE». |
| 6N | Campo numérico de seis posiciones, desde 000000 al 999999 ajustado a la derecha y relleno con ceros. |
| 1X | Campo alfanumérico de una posición relleno con blancos. |

Tipo «K». Otras.

Instrucciones de grabación

| Formato | Observaciones |
| --- | --- |
| 12X | 12 caracteres alfanuméricos ajustados a la izquierda y rellenos con blancos. Sin validación. Recomendable utilizar una referencia que sirva para localizar el vehículo, con NIF o CIF del tomador, abreviación del número de bastidor o matrícula local. |

La matrícula tipo «K» se creó por la derogada Resolución de 8 de marzo de 1996, con la finalidad de que constasen en el Fichero aquellos vehículos que, estando asegurados, no precisaran de matriculación por las Jefaturas Provinciales de Tráfico.

El CPD remitirá a cada entidad aseguradora antes del 26 de enero de 2002, fecha de finalización del período transitorio para la matriculación de los ciclomotores (disposición transitoria cuarta del Real Decreto 2822/1998), información de cada una de las matrículas con aseguramiento vigente que constan en el FIVA con el tipo «K» para que cada entidad envíe al FIVA las actualizaciones precisas para identificar cada ciclomotor por la matrícula que conste en la Jefatura Provincial de Tráfico.

Las entidades aseguradoras que tuvieran registrados en el FIVA otra clase de vehículos con tipo «K» procederán también a revisar dichos registros para, en su caso, actualizar la información de dichos vehículos con los tipos de matrícula que les sea de aplicación conforme al contenido de este apartado 3.

Tabla de provincias

| Código matrícula | Descripción |
| --- | --- |
| A | Alicante. |
| AB | Albacete. |
| AL | Almería. |
| AV | Ávila. |
| B | Barcelona. |
| BA | Badajoz. |
| BI | Vizcaya. |
| BU | Burgos. |
| C | A Coruña/La Coruña. |
| CA | Cádiz. |
| CC | Cáceres. |
| CE | Ceuta. |
| CO | Córdoba. |
| CR | Ciudad Real. |
| CS | Castelló/Castellón. |
| CU | Cuenca. |
| GC | Las Palmas. |
| GI, GE | Girona/Gerona. |
| GR | Granada. |
| GU | Guadalajara. |
| H | Huelva. |
| HU | Huesca. |
| J | Jaén. |
| L | Lleida/Lérida. |
| LE | León. |
| LO | La Rioja. |
| LU | Lugo. |
| M | Madrid. |
| MA | Málaga. |
| ML | Melilla. |
| MU | Murcia. |
| NA | Navarra. |
| O | Asturias. |
| OU, OR | Ourense/Orense. |
| P | Palencia. |
| IB, PM | Illes Balears/Baleares. |
| PO | Pontevedra. |
| S | Cantabria. |
| SA | Salamanca. |
| SE | Sevilla. |
| SG | Segovia. |
| SO | Soria. |
| SS | Guipúzcoa. |
| T | Tarragona. |
| TE | Teruel. |
| TF | Santa Cruz de Tenerife. |
| TO | Toledo. |
| V | València/Valencia. |
| VA | Valladolid. |
| VI | Álava. |
| Z | Zaragoza. |
| ZA | Zamora. |

Tabla de siglas de los vehículos pertenecientes al Estado

| Código matrícula | Descripción |
| --- | --- |
| A | AENA. |
| DGP | Dirección General de Policía. |
| EA | Ejército del Aire. |
| ET | Ejército de Tierra. |
| FN | Armada (Fuerza Naval). |
| MF | Parque del Ministerio de Fomento. |
| MMA | Ministerio Medio Ambiente. |
| MOP | Ministerio de Obras Públicas. |
| PGC | Parque Guardia Civil. |
| PME | Parque Móvil del Estado. |
| PMM | Parque Móvil Ministerial. |

> Redactado conforme a la corrección de erratas y errores publicada en BOE núm. 74 de 27 de marzo de 2001. Ref. BOE-A-2001-5985
