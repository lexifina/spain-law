## II. La política de firma electrónica

II.1 Definición y contenido.

1. Según la definición del Real Decreto 4/2010, de 8 de enero, una política de firma electrónica es el «conjunto de normas de seguridad, de organización, técnicas y legales para determinar cómo se generan, verifican y gestionan firmas electrónicas, incluyendo las características exigibles a los certificados de firma».

2. Una política de firma electrónica y de certificados definirá:

a) Los procesos de creación, validación y conservación de firmas electrónicas.

b) Características y requisitos de los sistemas de firma electrónica, certificados y sellos de tiempo.

3. Toda política de firma electrónica basada en certificados incluirá:

a) Definición del alcance y ámbito de aplicación, que concretará su relación con otras políticas existentes, marco o particulares, así como la identificación de los actores involucrados y los usos de la firma electrónica.

b) Datos para la identificación del documento y del responsable de su gestión.

c) Reglas comunes para el firmante y verificador de la firma electrónica que incluirán:

i. Formatos admitidos de firma electrónica y reglas de uso de algoritmos.

ii. Reglas de creación de firma.

iii. Reglas de validación de firma.

d) Reglas de confianza, que incluirán los requisitos establecidos para certificados, sellos de tiempo y firmas longevas.

e) Otras reglas opcionales a fijar por cada organización, como podrán ser:

i. Reglas específicas de compromisos que cada organización podrá establecer para cada uno de los servicios que presta, estableciendo requisitos específicos necesarios para que la firma sea válida en cada caso.

ii. Reglas de certificados de atributos mediante las que cada organización podrá establecer información adicional a añadir a los certificados digitales en función de sus necesidades y del contexto.

f) Definición de condiciones para el archivado y custodia de firmas electrónicas.

g) Descripción de consideraciones de gestión de la política que se aplicarán a dicho documento.

II.2 Datos identificativos de la política.

1. El documento de política de firma incluirá la siguiente información para su identificación:

a) Nombre del documento.

b) Versión.

c) Identificador (OID-Object IDentifier) de la política.

d) URI (Uniform Resource Identifier) de referencia de la política.

e) Fecha de expedición.

f) Ámbito de aplicación.

2. La política de firma incluirá la definición de su periodo de validez y las consideraciones respecto a los periodos de transición que procedan.

3. Para la identificación de su gestor, la política de firma electrónica basada en certificados incluirá:

a) Nombre del gestor de la política.

b) Dirección de contacto.

c) OID del gestor de la política de firma.

II.3 Actores involucrados en la firma electrónica.

Los actores involucrados en el proceso de creación y validación de una firma electrónica serán:

a) Firmante: persona que posee un dispositivo de creación de firma y que actúa en nombre propio o en nombre de una persona física o jurídica a la que representa.

b) Verificador: entidad, ya sea persona física o jurídica, que valida o verifica una firma electrónica apoyándose en las condiciones exigidas por la política de firma concreta por la que se rige la plataforma de relación electrónica o el servicio concreto al que se esté invocando. Podrá ser una entidad de validación de confianza o una tercera parte que esté interesada en la validez de una firma electrónica.

c) Prestador de servicios de certificación (PSC): Persona física o jurídica que expide certificados electrónicos o presta otros servicios en relación con la firma electrónica.

d) Emisor y gestor de la política de firma: entidad que se encarga de generar y gestionar el documento de política de firma, por el cual se deben regir el firmante, el verificador y los prestadores de servicios en los procesos de generación y validación de firma electrónica.

II.4 Usos de la firma electrónica.

Las políticas de firma electrónica podrán definir condiciones para la aplicación de una firma electrónica basada en certificados con los siguientes propósitos:

a) Firma de transmisiones de datos, como herramienta para proporcionar seguridad al intercambio, garantizando la autenticación de los actores involucrados en el proceso, la integridad del contenido del mensaje de datos enviado y el no repudio de los mensajes en una comunicación telemática.

b) Firma de contenido como herramienta para garantizar la autenticidad, integridad y no repudio de aquel, con independencia de que forme parte de una transmisión de datos.

II.5 Interacción con otras políticas.

1. Cada organización valorará la necesidad y conveniencia de desarrollar una política propia frente a la posibilidad de utilizar una política marco existente.

2. La definición del alcance y ámbito de aplicación de una política de firma electrónica se realizará considerando su interacción con otras políticas de firma electrónica, y asegurando que:

a) Su desarrollo es interoperable con la política marco, en caso de políticas de firma particulares.

b) Define las condiciones de utilización y convivencia con otras políticas particulares, si se trata de una política marco.

3. En toda política de firma electrónica se asegurará que:

a) Las extensiones o restricciones establecidas para las reglas de creación o validación de firma atienden a la validación de los formatos de firma establecidos en esta NTI y política marco si procede, de forma que se garantice la interoperabilidad entre las diferentes organizaciones.

b) Incluye, si procede, la referencia a la URL de la política marco de firma electrónica en la que se inscribe, con indicación expresa de la versión.

c) Las firmas que se generen siguiendo políticas marco o particulares, incluyen un campo donde se indique de forma explícita la política a la que pertenecen.

d) Para que otras aplicaciones puedan interpretar las reglas de una política particular correctamente, dicha política está disponible en formato XML (eXtensible Markup Language) y ASN.1 (Abstract Syntax Notation One).

II.6 Gestión de la política de firma.

1. La política de firma electrónica incluirá la descripción básica de su proceso de gestión, estableciendo las directrices para su mantenimiento, actualización y publicación, e identificando al responsable de llevar a cabo estas tareas.

2. El gestor de la política de firma mantendrá actualizada la versión de la política de firma atendiendo a:

a) Modificaciones motivadas por necesidades propias de la organización.

b) Cambios en políticas relacionadas.

c) Cambios en los certificados electrónicos emitidos por los prestadores de servicios de certificación referenciados en la política de firma.

3. Para facilitar la validación de firmas electrónicas creadas atendiendo a versiones anteriores de una política, se podrá mantener un repositorio con el historial de versiones anteriores que provea la ubicación de cada versión.

II.7 Archivado y custodia.

1. Atendiendo a las necesidades y normativa específicas de su ámbito, las políticas de firma podrán contemplar la definición de condiciones y responsabilidades para el archivado y custodia de las firmas electrónicas en sus diferentes aplicaciones.

2. Para garantizar la fiabilidad de una firma electrónica a lo largo del tiempo, se podrán utilizar:

a) Firmas longevas mediante las que se añadirá información del estado del certificado asociado, incorporando un sello de tiempo, así como los certificados que conforman la cadena de confianza, aplicando las reglas de confianza para firmas longevas descritas en el subapartado IV.3.

b) Otros métodos técnicos que impedirán la modificación de la firma para la que se ha verificado su validez, de acuerdo a los requisitos establecidos en la política de firma correspondiente, y que habrá sido almacenada en un sistema en un momento del tiempo determinado. Todos los cambios que se realicen sobre el sistema en el que se encuentra almacenada la firma podrán auditarse para asegurar que dicha firma no ha sido modificada. Los requisitos de seguridad de dichos sistemas cumplirán con las condiciones de los niveles de seguridad establecidos por el Real Decreto 3/2010, de 8 de enero, por el que se regula el Esquema Nacional de Seguridad en el ámbito de la Administración Electrónica.

3. Cada política de firma definirá un servicio para mantener las evidencias de validez de las firmas longevas y gestionar la actualización de las firmas. Dicho servicio especificará los mecanismos y condiciones bajo los que se archiva y custodia tanto la propia firma como los certificados e informaciones de estado utilizadas en su validación.

4. El almacenamiento de los certificados y las informaciones de estado podrá realizarse dentro del fichero resultante de la firma electrónica o en un depósito específico:

a) En caso de almacenar los certificados y las informaciones de estado dentro de la firma, se sellarán también dichas informaciones, siguiendo las modalidades de firmas AdES -X o -A.

b) Si los certificados y las informaciones de estado se almacenan en un depósito específico, se sellarán de forma independiente.

5. La protección de la firma electrónica frente a la posible obsolescencia de los algoritmos y el aseguramiento de sus características a lo largo del tiempo de validez, se realizará a través de uno de los siguientes procesos:

a) Utilización de mecanismos de resellado, para añadir, cuando el anterior sellado este próximo a su caducidad, un sello de fecha y hora de archivo con un algoritmo más robusto.

Las políticas de firma podrán definir la aplicación de mecanismos de resellado para facilitar la conservación de la firma electrónica.

b) Almacenamiento de la firma electrónica en un depósito seguro, garantizando la protección de la firma contra falsificaciones y asegurando la fecha exacta en que se guardó la firma electrónica.

Las operaciones de fechado se realizarán con marcas de fecha y hora, no siendo necesario su sellado de tiempo.

6. La definición de medidas y procedimientos para archivado y custodia de firmas electrónicas se realizará atendiendo con proporcionalidad a los diferentes usos de la firma electrónica contemplados en el alcance y ámbito de aplicación de la política.

7. Para archivado y gestión de documentos electrónicos firmados, se atenderá a lo establecido en la NTI de Política de gestión de documentos electrónicos.
