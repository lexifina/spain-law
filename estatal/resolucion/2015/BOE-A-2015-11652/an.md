## ANEXO

## Sistema informático de intercambio de información entre el Catastro y los Notarios

Las especificaciones técnicas para el intercambio de información entre las Notarías y el Catastro precisan la descripción del protocolo, servicios disponibles y mensajes empleados, describiéndose sus características técnicas en el presente anexo.

El intercambio de información se realizará por medios telemáticos, de forma estructurada y normalizada, empleando servicios web implementados por la Dirección General del Catastro, previstos mediante WSDL (Web Service Description Language) y basados en mensajes XML (eXtensible Markup Language) cuya estructura y contenido se define mediante el correspondiente XML Schema.

Se utilizará el protocolo de comunicación SOAP (Simple Object Access Protocol), garantizándose la autenticidad, integridad y confidencialidad mediante las especificaciones de seguridad de WS-Security (Seguridad en Servicios Web). Como mecanismo de transmisión optimizado para el envío de datos binarios se utilizará MTOM (Message Transmission Optimization Mechanism).

La utilización de los diferentes servicios precisa el empleo de mensajes de petición y respuesta, mensajes XML definidos al detalle en sus correspondientes esquemas XML. Estos esquemas incluyen junto a la identificación del movimiento, la descripción de los elementos gráficos y alfanuméricos que identifican y definen el bien inmueble, así como la información administrativa de los expedientes involucrados.

Los detalles concretos de implementación y los formatos de los ficheros de intercambio previstos en la presente resolución, se encuentran disponibles en el Portal del Catastro (www.minhap.es) y en la Sede Electrónica de la Dirección General del Catastro (www.sedecatastro.gob.es).

A continuación se describen los principales bloques de los mensajes de petición y respuesta intercambiados en la invocación de los diferentes servicios.

Mensaje de petición

El mensaje de petición se compone de cuatro bloques:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_001.png)

– El bloque de control incluye información relativa a la organización solicitante y el usuario concreto.

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_002.png)

– El bloque de expediente indica la operación o acción solicitada, el código de dicha operación asignado por la entidad y, en caso de ser necesaria, la información administrativa correspondiente.

– En caso de operaciones de consulta, el bloque correspondiente identifica los elementos sobre los que se requiere información, que pueden ser expedientes catastrales previamente registrados o elementos de catastro (inmuebles o fincas).

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_003.png)

– El bloque de datos de entrada incluye la información concreta que se validará o actualizará mediante la invocación de los respectivos servicios de validación o actualización. La información puede referirse a expedientes catastrales o elementos de catastro.

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_004.png)

– En el caso de intercambio de elementos de catastro, cuando además de la información alfanumérica se requiera la aportación de información gráfica descriptiva de parcelas, se incluirán los ficheros con la representación gráfica de las mismas en formato GML (Geography Markup Language) INSPIRE (Directiva 2007/2/CE del Parlamento Europeo y del Consejo, de 14 de marzo de 2007, por la que se establece una infraestructura de información espacial en la Comunidad Europea), o bien la identificación, mediante su código seguro de verificación (CSV), de un documento electrónico catastral que incluya las descripciones gráficas previamente validadas.

Mensaje de respuesta

El mensaje de respuesta se compone de cuatro bloques:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_005.png)

– El bloque de expediente devuelve, en caso de que la operación se realice con éxito, el código del expediente catastral asignado.

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_006.png)

– El bloque de resultado devuelve el código que indica si la operación se ha resuelto con éxito.

– El bloque de información contendrá los resultados concretos de la consulta planteada, pudiendo contener información relativa a la tramitación de expedientes o información de elementos de catastro (fincas e inmuebles).

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_007.png)

Si la consulta realizada requiere proporcionar datos gráficos descriptivos de una parcela, estos se proporcionarán en formato GML INSPIRE.

– En caso de que se produzcan errores, en este bloque se identifican los elementos que no han superado la validación y se describen los errores encontrados.

![imagen](https://www.boe.es/datos/imagenes/disp/2015/260/11652_008.png)
