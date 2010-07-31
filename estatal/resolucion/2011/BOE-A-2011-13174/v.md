## V. Descripción y estados del intercambio

En este apartado se describen los posibles estados en los que se puede encontrar el apunte registral objeto del intercambio.

Tal y como se introdujo en el apartado IV.1, el proceso de intercambio inicia y finaliza en la Entidad Registral Origen, ya sea en el propio ciudadano o en la Unidad de Tramitación de Origen.

A lo largo de todo este proceso, Entidad Registral Origen y destino se informan mutuamente sobre el estado del intercambio a través de sus respectivos campos:

i. Campo «Tipo de anotación» del segmento de datos «Internos y Control» del mensaje de datos de intercambio que emite la Entidad Registral Origen y destino.

ii. Campo «Tipo de mensaje» de los mensajes de control que envía la Entidad Registral destino.

De esta forma, el control sobre el estado del asiento registral a lo largo del proceso de intercambio se gestiona y controla de manera conjunta entre Origen y destino.

El inicio del intercambio viene marcado por la generación por parte de la Entidad Registral Origen del mensaje de datos de intercambio cuyo campo ‘Tipo de anotación’ tiene valor de Pendiente, y finaliza mediante el asentimiento del intercambio que la Entidad Registral destino notifica a través del envío del mensaje de control de tipo Confirmación.

Las Entidades Registrales deben implementar mecanismos y procedimientos que eviten la duplicación de asientos en caso de recepciones múltiples. Las herramientas para esta implementación son los datos «Identificador de Intercambio», «Identificador de Fichero» y «Número de Secuencia».

V.1 Generación del Identificador de Intercambio

La aplicación de registro de la Entidad Registral Origen, que interviene en el proceso de intercambio, es responsable de la generación de un identificador de intercambio único para cada operación en el espacio de intercambio del tipo:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_006.png)

Este identificador se mantiene durante todo el proceso de intercambio tanto en el sistema de gestión de intercambio como en la aplicación de registro de la Entidad Registral destino. En el apartado VII.1 se describen las reglas para la generación de este identificador.

V.2 Estados en el mensaje de datos de intercambio

Los estados que registra el mensaje de datos de intercambio en el campo de «Tipo de anotación» son:

i. Pendiente («01»): Indica que el mensaje de datos de intercambio está pendiente de envío al sistema de intercambio y que está pendiente de la asignación de un identificador del intercambio para iniciar el proceso.

ii. Envío («02»): Indica que el mensaje de datos de intercambio está en pleno proceso de intercambio, y por tanto, ha partido desde la Entidad Registral de Origen pero está pendiente aún de convertirse en registro en firme por la Entidad Registral de destino.

iii. Reenvío («03»): Indica que el mensaje de datos de intercambio es enviado de nuevo desde la Entidad Registral de destino.

La razón para el reenvío es, generalmente, que el destino indicado en el primer envío no corresponde. Cuando se da esta situación, la Entidad Registral de destino puede identificar la Entidad Registral de destino correcta y reenviarlo a esta en lugar de rechazar el envío que realizó la Entidad Registral Origen.

Esta secuencia de envíos y los valores que toma el campo «Tipo de anotación» aparecen en la siguiente figura.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_007.png)

iv. Rechazo («04»): Indica que el mensaje de datos de intercambio no ha sido aceptado por la Entidad Registral de destino.

En caso de rechazo, el mensaje de datos de intercambio puede ser enviado tanto a la Entidad Registral de Origen como a la Entidad Registral de Inicio.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_008.png)

V.3. Estados en los mensajes de control

La información de estado del intercambio que se refleja en los mensajes de control a través de los siguientes valores de «Tipo de mensaje»:

i. ACK-aceptación («01»): Notifica la recepción correcta del mensaje de datos de intercambio desde un punto de vista exclusivamente técnico, por lo que no constituye la confirmación de finalización correcta de todo el proceso de intercambio.

A continuación, se muestra una figura explicativa de la emisión de un mensaje de control tipo aceptación:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_009.png)

ii. Error («02»): Notifica la recepción errónea o incompleta del mensaje de datos de intercambio desde un punto de vista técnico. Los posibles tipos de errores que se pueden dar se identifican mediante un rango de error y el propio código de error. Este mensaje de control refleja el tipo de error a través de la codificación de errores que se detalla en el apartado VII.4.

La siguiente figura refleja la emisión de un mensaje de control tipo Error:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_010.png)

Esta situación, la Entidad Registral de Origen («A») puede enviar el mensaje de datos de intercambio a la Entidad Registral de destino («B»), reenviarlo o rechazarlo. A continuación se muestra un ejemplo de envío:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_011.png)

iii. Confirmación («03»): Una vez recibido el mensaje de datos de intercambio y todos sus documentos anexos, se acepta que el proceso de intercambio se ha realizado con éxito y por tanto, se notifica a la Entidad Registral de Inicio que la recepción ha sido correcta confirmando por tanto el asentimiento del intercambio completado.

La figura que sigue muestra la secuencia que provoca la emisión de un mensaje de control tipo confirmación:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_012.png)

El asentimiento es necesario para el correcto funcionamiento de los flujos de intercambio definidos, por lo que debe ser implementado por todas las Entidades Registrales para el intercambio de los asientos. El asentimiento permite confirmar que el asiento registral es correcto y corresponde a la Entidad Registral de destino por lo que debe emitirse tanto tras la recepción de un mensaje de datos de intercambio con «Tipo de anotación» envío como si se trata de un reenvío.

Si una Entidad Registral de Origen no recibe el asentimiento pasado un período de tiempo (predefinido en cada sistema de intercambio) debe reintentar el envío.
