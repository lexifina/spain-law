## PO. 10.11. Tratamiento e intercambio de Información entre Operador del Sistema, encargados de la lectura, comercializadores y resto de agentes

1. Objeto.

El objeto de este documento es definir el tratamiento de la información relativa a los datos de medida de los puntos de los que los distribuidores son los encargados de la lectura.

Este documento define los flujos de información de medidas entre los concentradores secundarios de los distribuidores y el concentrador principal y resto de participantes del sistema.

2. Ámbito de aplicación.

Este procedimiento es de aplicación a los participantes del sistema de información de medidas de puntos frontera de los que los distribuidores son encargados de lectura.

Este documento aplica a los concentradores secundarios definidos en el Reglamento unificado de puntos de medida que gestionen datos de medidas de clientes y/o puntos frontera de generación de los que el distribuidor es encargado de la lectura.

3. Responsabilidades.

Los encargados de la lectura son responsables del desarrollo, instalación, administración, mantenimiento y operación de los concentradores secundarios de acuerdo al Reglamento unificado de puntos de medida junto con lo indicado en este documento.

Los propietarios de concentradores secundarios que, sin ser encargados de la lectura, suministren las medidas a sus encargados son responsables del desarrollo, instalación, administración, mantenimiento y operación del concentrador secundario de acuerdo a lo indicado en este documento.

4. Procesos de los concentradores secundarios.

4.1 Recepción de las medidas de los puntos de medida.

4.1.1 Puntos de medida con conexión directa al concentrador secundario del encargado de la lectura.

El concentrador secundario del encargado de la lectura deberá recibir las lecturas de los registradores y / o contadores que son directamente leídos por el propio encargado de la lectura, de acuerdo con los plazos establecidos en el procedimiento de operación P.O.10.5. «Cálculo del Mejor Valor de Energía en los Puntos Frontera y Cierres de Energía del Sistema de Información de Medidas Eléctricas».

4.1.2 Puntos de medida cuyas lecturas son enviadas desde un concentrador secundario cuyo titular no es el encargado de la lectura.

El concentrador secundario del encargado de la lectura podrá obtener medidas a través de otros concentradores siempre que las mismas procedan de registradores que tengan operativa la firma electrónica y envíen al concentrador secundario del encargado de la lectura toda la información requerida dentro de los plazos recogidos en el P.O. 10.5.

El canal y protocolo de comunicación entre los concentradores será el definido en el apartado 6 de este procedimiento.

4.2 Gestión de datos estructurales.

En cada concentrador secundario se mantendrán actualizados los datos estructurales de puntos de medida, puntos frontera y agregaciones del/los encargado/s de la lectura a los que da servicio dicho concentrador secundario, de acuerdo a lo indicado en el Reglamento unificado de puntos de medida.

Los responsables de los concentradores secundarios deberán intercambiar la información con los distintos comercializadores y/o representantes para la carga inicial del inventario y/o modificaciones de acuerdo al canal y protocolo de comunicación definido en el apartado 6 de este procedimiento antes de la puesta en servicio de los mismos. Sólo se considerarán las notificaciones que se comuniquen por las vías anteriormente indicadas.

El concentrador secundario del encargado de la lectura realizará, al menos, la carga y mantenimiento de los datos estructurales correspondientes a:

• Altas de puntos frontera de clientes y de generación de los que el distribuidor es encargado de lectura y sus datos asociados.

• Altas de agregaciones de puntos frontera de clientes y de generación de los que el distribuidor es encargado de lectura.

• Cambios de comercializador, cambios de datos o bajas de fronteras.

• Bajas de agregaciones de puntos frontera de clientes y de generación de los que el distribuidor es encargado de lectura.

• Corrección de errores en altas, bajas y modificaciones de los datos anteriores.

El operador del sistema gestionará datos estructurales hasta que afecten a meses de los que se haya realizado el cierre posterior a la corrección de medidas por aplicación del artículo 15 del Real Decreto 1110/2007, de 24 de agosto.

4.3 Tratamiento de datos de medidas por los encargados de la lectura.

El concentrador secundario validará las medidas procedentes de los puntos de medida de los que es encargado de la lectura de acuerdo a lo indicado en el P.O. 10.5.

Independientemente de lo anterior cualquier participante en una medida podrá notificar incidencias en las mismas de acuerdo a lo indicado en el P.O. 10.5.

El concentrador secundario del encargado de lectura calculará el mejor valor horario de los puntos frontera de los que es encargado de la lectura de acuerdo a lo indicado en el P.O. 10.5.

El concentrador secundario del encargado de la lectura calculará las agregaciones de los puntos de los que es participe de acuerdo al P.O. 10.6. «Agregaciones de puntos de medida»

El concentrador secundario del encargado de la lectura deberá gestionar y recibir las objeciones de medidas de las que es encargado de la lectura de acuerdo a lo indicado en el P.O. 10.5.

4.4 Puesta a disposición de comercializadores, consumidores directos a mercado y/o representantes de las medidas y datos estructurales.

La información de datos estructurales y de medidas disponible en los concentradores secundarios de los encargados de la lectura deberá ser puesta a disposición de los comercializadores, consumidores directos a mercado y/o representantes de acuerdo a los plazos establecidos en el P.O. 10.5.

El intercambio de información de incidencias u objeciones se realizará de acuerdo a los plazos indicados en el P.O. 10.5.

El intercambio de información se realizará utilizando los canales y protocolos descritos en el apartado 6 de este documento.

En el Anexo de este documento se indica la información mínima a poner a disposición del resto de participantes.

5. Intercambio de información entre participantes.

5.1 Flujo de información de medidas entre concentrador principal y concentradores secundarios de encargados de la lectura.

5.1.1 Intercambio de información de medidas.

Los concentradores secundarios de encargados de la lectura son responsables de poner a disposición del concentrador principal los datos de medidas de los que son responsables de acuerdo a los plazos establecidos en el P.O. 10.5.

5.1.2 Intercambio de información de datos estructurales.

Los concentradores secundarios de los encargados de la lectura son responsables de poner a disposición del concentrador principal los datos estructurales de los que son responsables de acuerdo a lo indicado en el P.O. 10.4 «Concentradores de medidas eléctricas y sistemas de comunicaciones» y el P.O. 10.6.

5.1.3 Intercambio de información tras el cierre provisional.

El intercambio de información de datos como consecuencia de la apertura del periodo de objeción de medidas se realizará con los plazos indicados en el P.O. 10.5 utilizando el canal y protocolo de comunicación definido en el apartado 6 de este procedimiento.

5.1.4 Intercambio de información entre concentrador secundario de encargados de la lectura y resto de participantes.

El intercambio de información entre los concentradores secundarios de encargados de la lectura y los comercializadores/clientes/representantes que se indican en el Anexo se realizará de acuerdo a los plazos indicados en el P.O. 10.5 y de acuerdo a los canales y protocolos definidos en el apartado 6 de este procedimiento.

6. Canales y protocolos de comunicación.

6.1 Comunicaciones entre registradores y concentrador secundario del encargado de la lectura.

Para puntos tipo 1, 2 y 3 se realizará de acuerdo a lo indicado en el P.O. 10.4.

Para puntos tipo 4 y 5, los encargados de lectura podrán utilizar los protocolos descritos en el Reglamento unificado de puntos de medida.

6.2 Comunicaciones entre concentrador principal y concentrador secundario del encargado de la lectura.

El canal o canales de comunicación entre el concentrador principal y cada concentrador secundario será el definido en el P.O. 10.4.

Los formatos de los mensajes intercambiados serán los definidos en el documento «Ficheros para el intercambio de información de medidas». Los mensajes que se indiquen en este documento podrán ser publicados desde el concentrador principal a los participantes que no dispongan de un concentrador secundario asociado.

6.3 Comunicaciones entre otros concentradores secundarios y concentrador secundario del encargado de la lectura.

El canal o canales de comunicación entre el concentrador secundario del encargado de la lectura y otros concentradores secundarios de libre instalación será el definido en el P.O. 10.4.

Los formatos de los mensajes intercambiados serán los definidos en el documento «Ficheros para el intercambio de información de medidas».

6.4 Comunicaciones entre participantes y concentrador secundario del encargado de la lectura.

Sin perjuicio de lo establecido en el procedimiento de operación P.O. 10.13 «procedimiento por el que los distribuidores intercambian información con los comercializadores de energía eléctrica, y ponen a disposición de los comercializadores y los consumidores los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión», los formatos de los mensajes a intercambiar serán los definidos en el documento «Ficheros para el intercambio de información de medidas.»

Sin perjuicio de lo establecido en el procedimiento de operación P.O. 10.13, el canal o canales entre los concentradores secundarios de los encargados de la lectura y sus participantes serán aquellos que cada encargado de la lectura establezca que deberá cumplir con los requisitos que se indican a continuación.

6.4.1 Características generales.

Deberá cumplir los siguientes requisitos:

• Utilización de estándares existentes en el mercado.

• Facilidad de integración con las distintas soluciones informáticas disponibles por participantes y distribuidores.

• Flexibilidad de configuración, permitiendo accesos tanto automáticos como manuales a la información disponible. Dicho acceso deberá realizarse por agentes autorizados y se deberá garantizar la integridad y la seguridad de la información y el sistema en su conjunto, evitando accesos no autorizados, mediante la oportuna protección.

• Economía de explotación, evitando la utilización de productos con licencia, los desarrollos costosos de software y la utilización de equipos informáticos complejos.

• Seguridad de la información a intercambiar.

6.4.2 Descripción.

El sistema adoptado deberá estar basado en arquitecturas cliente – servidor sobre Internet. El encargado de la lectura actuará como servidor mientras que los participantes actuarán como clientes.

El intercambio de información se realizará mediante ficheros descritos en el documento «Ficheros para el intercambio de información de medidas», para lo cual el encargado de la lectura deberá disponer de un servidor en el cual existirán carpetas diferenciadas para cada participante.

El participante podrá conectarse manualmente al servidor, para lo cual necesitará únicamente un ordenador personal dotado de un navegador estándar con certificado digital, o podrá intercambiar la información de forma automática, para lo cual necesitará adicionalmente un software desarrollado específicamente.

6.4.3 Procesos.

El sistema deberá soportar, de acuerdo a los formatos y procedimientos que se establezcan, los siguientes procesos:

• Publicación de ficheros por parte del encargado de la lectura.

• Envío de ficheros por parte de los participantes.

• Lectura automática por parte del participante de los ficheros publicados por el encargado de la lectura.

• Lectura automática por parte del encargado de la lectura de los ficheros enviados por los participantes.

• Lectura manual por parte del participante de los ficheros publicados por el encargado de la lectura.

6.4.4 Mecanismos de seguridad.

El sistema deberá estar dotado de los siguientes mecanismos de seguridad:

• Autentificación mediante certificados digitales de todas las entidades, tanto distribuidores como el resto de participantes.

• Posibilidad de conexión cifrada en los intercambios de información.

• Seguridad incorporada en los servidores de ficheros para protegerlos de accesos no autorizados.

• Integridad en la transferencia de información, asegurando su transmisión sin errores.

• Trazabilidad de la información intercambiada, guardando registro de las transmisiones y dando la posibilidad de eliminar la información descargada por los usuarios, siempre que no sea metrológicamente relevante.

• Aseguramiento de que cada agente tiene acceso únicamente a los datos de los que es partícipe.

6.4.5 Modificaciones y ampliación de las informaciones a intercambiar entre participantes.

El operador del sistema podrá proponer nuevas informaciones a intercambiar entre los participantes del sistema de medidas e incorporarlas en el documento «Ficheros para el intercambio de información de medidas».

En los casos en los que los participantes afectados acepten el envío de nueva información, éstos deberán implementar los nuevos mensajes definidos en un plazo inferior a tres meses desde su definición por parte de operador del sistema.

6.5 Comunicaciones entre participantes y concentrador principal.

Los formatos de los mensajes a intercambiar serán los definidos en el documento «Ficheros para el intercambio de información de medidas».

El canal o canales entre el concentrador principal y los participantes serán aquellos que el operador del sistema establezca y deberá cumplir los siguientes requisitos:

• Utilización de estándares existentes en el mercado.

• Facilidad de integración con las distintas soluciones informáticas disponibles por participantes.

• Evitar los desarrollos costosos de software y la utilización de equipos informáticos complejos.

• Seguridad y confidencialidad de la información a intercambiar.
