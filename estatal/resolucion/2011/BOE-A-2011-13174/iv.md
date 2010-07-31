## IV. Modelo de datos para el intercambio de asientos entre Entidades Registrales

IV.1 Definición y características generales de SICRES 3.0

SICRES 3.0 constituye el modelo de datos para el intercambio de asientos entre Entidades Registrales. Esta versión de SICRES, alineada con la filosofía de sus predecesoras, tiene como finalidad contribuir a garantizar la interconexión entre organizaciones, permitiendo así un servicio de mayor calidad a los ciudadanos tal y como marca la Ley 11/2007, de 22 de junio, y su normativa de desarrollo.

Las principales características de SICRES 3.0 que la diferencian de sus versiones anteriores son:

i. Optimización del modelo para agrupar funcionalidades comunes y evitar redundancias. El modelo de intercambio de SICRES 3.0 se basa en una reestructuración de los ámbitos o segmentos funcionales, acompañada de la definición de nuevos campos que amplían la funcionalidad del sistema.

ii. Orientación a arquitecturas de intermediación. La norma SICRES 3.0 es independiente de la tecnología de intermediación utilizada para realizar el intercambio registral.

iii. Incorporación de ficheros adjuntos a los intercambios.

iv. Mejora en los mecanismos de control del intercambio, como es la garantía de unicidad de la operación de intercambio a través de un identificador único.

El modelo conceptual de espacio de intercambio bajo SICRES 3.0 aparece en la siguiente figura:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_001.png)

Según este esquema, el espacio de intercambio engloba todo el proceso de intercambio desde la Unidad de Tramitación Origen hasta la Unidad Tramitación destino proporcionando un contexto único a cada uno de los intercambios. Dentro de este espacio, destacan los siguientes elementos:

i. Unidades de Tramitación de Origen y Destino. Unidades de cada organización responsables de la tramitación del registro y, respectivamente, de enviar y recibir la información objeto de intercambio. La identificación de ambas unidades es única a través del Directorio Común que se indica en el apartado 0 de esta norma.

ii. Entidad Registral de Origen y destino. Entendidas como la unidad administrativa u órgano que se encarga de inscribir los asientos de entrada y salida de documentos en el Registro oficial de la organización a la que pertenece. Son responsables respectivamente del envío y recepción del mensaje de datos de intercambio (a través de las aplicaciones de registro), pero solo a nivel técnico o de comunicación sin implicación en la tramitación de los documentos. La identificación de las Entidades Registrales también es única a través del Directorio Común que se indica en el apartado VI.4 de esta norma.

iii. Mensaje de datos de intercambio1. Es la unidad de datos o fichero principal del intercambio. Es creado y emitido por la Entidad Registral de Origen y alberga, además de campos para el control e identificación, la información del asiento registral y los documentos correspondientes adjuntos. Su estructura y formato se definen en el apartado IV.2 de esta norma.

1 Entidad «Fichero de intercambio» en versiones anteriores de SICRES.

iv. Mensajes de control. Son emitidos por la Entidad Registral destino o por el propio sistema de intercambio y proporcionan información de estado para la gestión de la operación de intercambio. Su estructura y formato se definen en el apartado IV.3 de esta norma.

v. Sistema de intercambio. Proporciona la gestión del intercambio y la comunicación directa con las Entidades Registrales Origen y destino. Sus funciones y requisitos técnicos deben cumplir lo establecido en el apartado VI de esta norma.

vi. Plataforma de intercambio. Comprende el Sistema de intercambio y las Entidades Registrales de Origen y de destino.

El proceso de intercambio inicia y finaliza en la Entidad Registral de Origen, punto de contacto con el ciudadano o Unidad de Tramitación que origina la creación del asiento registral.

El inicio viene marcado por la generación del mensaje de datos de intercambio en la Entidad Registral Origen conteniendo la información del asiento. A través del sistema de intercambio, este mensaje es recibido en la Entidad Registral destino, que, si procede, confirma la recepción correcta al Origen a través del mensaje de control correspondiente.

Los intercambios disfrutan de un contexto único dentro del espacio SICRES mediante la asignación de un identificador del intercambio único a cada proceso de transacción que es generado por la aplicación de registro de la Entidad Registral de Origen y acompaña tanto al mensaje de datos de intercambio como a los mensajes de control relacionados. La generación del identificador del intercambio se detalla en el apartado VII.1 de esta NTI.

IV.2 Estructura y contenido del mensaje de datos de intercambio

El mensaje de datos de intercambio de SICRES 3.0 es el mensaje o contenedor XML que alberga la información objeto del intercambio. Su codificación se especifica en el apartado VII.2 de esta norma.

Este mensaje está compuesto por los 7 segmentos que aparecen en la figura y cuya descripción funcional se desarrolla a continuación.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_002.png)

Tabla 1. Datos de Origen (o Remitente)

1. Segmento de Origen (o Remitente)

| Segmento de Origen (o Remitente) | ☑ Obligatorio |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de Origen. | Alfanumérico | 21 | Obligatorio | Código único obtenido del Directorio Común. |
| Decodificación de Entidad Registral de Origen. | Alfanumérico | 80 | Opcional | Descripción de la Entidad Registral de Origen. |
| Número de registro de entrada (en Origen). | Alfanumérico | 20 | Obligatorio | Número de registro de entrada en la Entidad Registral Origen. |
| Fecha y hora de entrada (en Origen)2. | Alfanumérico | 14 | Obligatorio | Formato AAAAMMDDHHMMSS. |
| Timestamp de entrada. | Alfanumérico | Variable | Opcional | Sello de tiempo del registro de entrada en Origen. |
| Código de la Unidad de Tramitación de Origen | Alfanumérico | 21 | Opcional | Código único obtenido del Directorio Común. |
| Decodificación de la Unidad de Tramitación Origen. | Alfanumérico | 80 | Opcional | Descripción de la Unidad de Tramitación de Origen. |

2 Corresponde con la fecha y hora de presentación por parte del ciudadano.

Tabla 2. Datos de destino

2. Segmento de destino

| Segmento de destino (o destinatario) | ☑ Obligatorio |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de destino. | Alfanumérico | 21 | Obligatorio | Código único obtenido del Directorio Común. |
| Decodificación Entidad Registral de destino. | Alfanumérico | 80 | Opcional | Descripción de Entidad Registral de destino. |
| Código de la Unidad de Tramitación de destino. | Alfanumérico | 21 | Opcional | Código único obtenido del Directorio Común. |
| Decodificación de la Unidad de Tramitación de destino. | Alfanumérico | 80 | Opcional | Descripción de la Unidad de Tramitación de destino. |

Tabla 3. Datos de interesado

3. Segmento de interesado

Este segmento comprende los datos que identifican al Interesado y su Representante en la entidad mensaje de datos de intercambio. Este segmento se puede declarar de forma múltiple.

| Segmento de interesado | ☑ Obligatorio |
| --- | --- |
| ☑ Múltiple |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Descripción de identificación de interesado. Tipo. | Alfanumérico | 1 | Opcional | Identificación del interesado: – «N» = NIF. – «C» = CIF. – «P» = Pasaporte. – «E» = Documento de identificación de extranjeros. – «X» = Otros de persona física. – «O» = Código de origen. |
| Documento de identificación del interesado. | Alfanumérico | 17 | Opcional | Alfanumérico con sintaxis adecuada en función del campo documento de identificación. |
| Razón social del interesado. | Alfanumérico | 80 | Condicional | Si es persona jurídica. Es necesario que se registre la razón social o el nombre y primer apellido. |
| Nombre del interesado. | Alfanumérico | 30 | Condicional | Texto. Es necesario que se registre la razón social o el nombre y primer apellido. |
| Primer apellido del interesado. | Alfanumérico | 30 | Condicional | Texto. Es necesario que se registre la razón social o el nombre y primer apellido. |
| Segundo apellido del interesado. | Alfanumérico | 30 | Opcional | Identificación del interesado: – «N» = NIF. – «C» = CIF. – «P» = Pasaporte. – «E» = Documento de identificación de extranjeros. – «X» = Otros de persona física. – «O» = Código de origen. |
| Documento de identificación del Representante. | Alfanumérico | 17 | Opcional | Alfanumérico con sintaxis adecuada en función del campo Documento de identificación. |
| Razón social del Representante. | Alfanumérico | 80 | Opcional | Si es persona jurídica. |
| Nombre del Representante. | Alfanumérico | 30 | Opcional | Texto. |
| Primer apellido del Representante. | Alfanumérico | 30 | Opcional | Texto. |
| Segundo apellido del Representante. | Alfanumérico | 30 | Opcional | Texto. |
| País del interesado. | Alfanumérico | 4 | Condicional | Atributo según catálogo del INE. |
| Provincia del interesado. | Alfanumérico | 2 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Municipio del interesado. | Alfanumérico | 5 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Dirección del interesado. | Alfanumérico | 160 | Condicional | Dirección postal del interesado. |
| Código postal del interesado. | Alfanumérico | 5 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Correo electrónico del interesado. | Alfanumérico | 160 | Opcional | Correo electrónico. |
| Teléfono de contacto del interesado. | Alfanumérico | 20 | Opcional | Teléfono de contacto. |
| Dirección electrónica del interesado. | Alfanumérico | 160 | Condicional | En caso de disponer de buzón de notificaciones telemáticas seguras. |
| Canal preferente de notificación del interesado. | Alfanumérico | 2 | Condicional | Canal de preferencia para el contacto de la administración. A fecha de emisión de la norma, los canales habilitados son: – «01» = Dirección postal. – «02» = Dirección electrónica habilitada. – «03» = Comparecencia electrónica. |
| País del Representante. | Alfanumérico | 4 | Condicional | Atributo según catálogo del INE. |
| Provincia del Representante. | Alfanumérico | 2 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Municipio del Representante. | Alfanumérico | 5 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Dirección del Representante. | Alfanumérico | 160 | Condicional | Dirección postal del Representante. |
| Código postal del Representante. | Alfanumérico | 5 | Condicional | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). |
| Correo electrónico del Representante. | Alfanumérico | 160 | Opcional | Correo electrónico del Representante. |
| Teléfono de contacto del Representante. | Alfanumérico | 20 | Opcional | Teléfono de contacto del Representante. |
| Dirección electrónica del Representante. | Alfanumérico | 160 | Condicional | En caso de disponer de buzón de notificaciones telemáticas seguras. |
| Canal preferente de notificación del Representante. | Alfanumérico | 2 | Condicional | Canal de preferencia para el contacto de la administración. A fecha de emisión de la norma, los canales habilitados son: – «01» = Dirección postal. – «02» = Dirección electrónica habilitada. – «03» = Comparecencia electrónica. |
| Observaciones | Alfanumérico | 160 | Condicional | Observaciones del interesado y/o del Representante. |

Los campos relacionados con canales de comunicación permiten la introducción por separado de distintas vías de notificación para el interesado y el representante. La obligatoriedad de cumplimentar estos campos depende de las siguientes condiciones:

i. Existencia de un canal de notificación (para el Interesado o para el Representante).

ii. Obligación de cierta información acerca del canal preferente para la notificación:

1. Si el «Canal preferente de notificación (del Interesado o del Representante)» toma el valor de dirección postal («01»), es obligatorio rellenar los campos «País (del Interesado o del Representante)» y «Dirección (del Interesado o Representante)».

2. Si el «Canal preferente de notificación (del Interesado o del Representante)» toma el valor de dirección electrónica habilitada («02»), es obligatorio rellenar el campo correspondiente «Dirección electrónica habilitada (del Interesado o del Representante)».

3. Si el campo «País (del Interesado o del Representante)» contiene el valor «España» (0724) entonces es obligatorio rellenar los campos «Código postal (del Interesado o del Representante)» o «Provincia (del Interesado o del Representante)’ y «Municipio (del Interesado o del Representante)».

Tabla 4. Datos de Asunto

4. Segmento de Asunto

| Segmento de Asunto | ☑ Obligatorio |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| «Abstract» o resumen. | Alfanumérico | 240 | Obligatorio | Texto. |
| Código de asunto según destino. | Alfanumérico | 16 | Opcional | Codificación del asunto en destino, si la solicitud incluye ese dato. Se procurará definir solicitudes que incluyan el código para permitir el manejo automatizado del asiento en destino. |
| Referencia externa. | Alfanumérico | 16 | Opcional | Cualquier referencia que el destino precise conocer y sea conocida por el solicitante (matrícula de vehículo, número de recibo cuyo importe se reclama, etc.). |
| Número de expediente. | Alfanumérico | 80 | Opcional | Número del expediente objeto de la tramitación administrativa. |

5. Segmento de Anexo

Este segmento comprende los datos relativos a los documentos electrónicos que, adicionalmente, pueden formar parte del intercambio a través del mensaje de datos de intercambio.

Tal y como se ha indicado, SICRES 3.0 permite la inclusión de documentos adjuntos o anexos que pueden integrarse directamente en el Mensaje de datos de intercambio o, si fuese necesario, pueden ser intercambiados de manera independiente.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_003.png)

Si los documentos anexos se intercambian embebidos en el Mensaje de datos de intercambio, su contenido se incluye en el segmento «de Anexo» codificado en base64 tal y como se indica a continuación.

Si el documento se intercambia de manera independiente, el fichero debe utilizar la nomenclatura que se indica en el apartado VII.2 para este tipo de mensajes.

Este segmento es opcional y puede declararse de forma múltiple.

Tabla 5. Datos de Anexo

| Segmento de Anexo | ☑ Opcional |
| --- | --- |
| ☑ Múltiple |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Descripción del fichero anexado. | Alfanumérico | 80 | Obligatorio | Nombre del fichero original. |
| Identificador de fichero. | Alfanumérico | 50 | Obligatorio | Se compondrá siguiendo la normalización definida en el apartado VII.2. |
| Validez del documento3. | Alfanumérico | 2 | Opcional | Indica la categoría de autenticidad del documento4: – «01» = Copia (el documento adjunto en el proceso de intercambio es una copia del original sin estar cotejada por ningún organismo oficial y, por tanto, sin validez jurídica). – «02» = Copia compulsada (el documento adjunto en el proceso de intercambio es una copia del original y cotejada por un organismo oficial y, por tanto, con validez jurídica). – «03» = Copia original (el documento adjunto en el proceso de intercambio es una copia del documento pero con exactamente la misma validez jurídica que el original). – «04» = Original (el documento adjunto en el proceso de intercambio es original electrónico). |
| Tipo de documento5. | Alfanumérico | 2 | Obligatorio | Indica el tipo de documento: – «01» = Formulario (el documento adjunto es un formulario con campos rellenos por el ciudadano remitente). – «02» = Documento adjunto al formulario (además del formulario, otro documento es adjuntado, acompañando al formulario). – «03» = Fichero técnico interno (el documento adjunto es un fichero interno. Por lo general, estos ficheros pueden resultar útiles para la Entidad Registral de destino, pero no son ficheros para presentar directamente a los usuarios de gestión). |
| Certificado. | Alfanumérico | Variable | Opcional | Certificado del fichero Anexo (parte pública). |
| Firma del documento. | Alfanumérico | Variable | Opcional | Firma electrónica del fichero Anexo. |
| Timestamp. | Alfanumérico | Variable | Opcional | Sello de tiempo del fichero Anexo. |
| Validación OSCP del certificado. | Alfanumérico | Variable | Opcional | Validación del certificado. |
| Hash. | Alfanumérico | Variable | Obligatorio | Huella binaria del fichero Anexo que garantiza la integridad de los archivos enviados. |
| Tipo MIME. | Alfanumérico | 20 | Opcional | Tipo del fichero Anexo. |
| Anexo. | Alfanumérico | Variable | Opcional | Fichero Anexo codificado en Base64. |
| Identificador del documento firmado. | Alfanumérico | 50 | Opcional | Si el Anexo es firma de otro documento, se especifica el «identificador de fichero» objeto de la firma. Este campo tomará el valor de sí mismo para indicar que contiene firma embebida. |
| Observaciones. | Alfanumérico | 50 | Opcional | Observaciones del fichero adjunto. |

3 Permite indicar la validez del documento anexado. La validez del documento es la categoría de autenticidad y validez jurídica del documento adjunto durante el proceso de intercambio

4 El tipo de copia puede tener que adaptarse conforme a los esquemas de valores de la NTI de Documento electrónico una vez aprobada.

5 El tipo del documento es la categoría en cuanto a la forma que toma el documento adjunto durante el proceso de intercambio

Tabla 6. Datos de Internos y Control

6. Segmento de Internos y Control

| Segmento de Internos y Control | ☑ Obligatorio |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Tipo de transporte de entrada. | Alfanumérico | 2 | Opcional | Formas de llegada al registro de entrada. – «01» = Servicio de Mensajeros. – «02» = Correo postal. – «03» = Correo postal certificado. – «04» = Burofax. – «05» = En mano. – «06» = Fax. – «07» = Otros. |
| Número de transporte de entrada. | Alfanumérico | 20 | Opcional | Referencia del transporte. Código. En el caso de certificados, número del mismo. |
| Nombre de usuario. | Alfanumérico | 80 | Opcional | Nombre de usuario de Origen. |
| Contacto de usuario. | Alfanumérico | 160 | Opcional | Contacto del usuario de Origen (teléfono o dirección de correo electrónico). |
| Identificador de intercambio. | Alfanumérico | 33 | Obligatorio | Identificador de intercambio único de la operación. Se compondrá siguiendo la normalización definida en el apartado VII.1. |
| Aplicación y versión emisora. | Alfanumérico | 4 | Opcional | Identifica la aplicación y su versión. |
| Tipo de Anotación. | Alfanumérico | 2 | Obligatorio | Indica el motivo de la anotación (siguiendo la normalización definida en el aparado V.2). Los únicos valores posibles para el mensaje de datos de intercambio son: – «01» = Pendiente (sin identificador de intercambio). – «02» = Envío. – «03» = Reenvío. – «04» = Rechazo. |
| Descripción del Tipo de Anotación. | Alfanumérico | 80 | Opcional | Descripción del tipo de Anotación. |
| Tipo de Registro. | Alfanumérico | 1 | Obligatorio | – «0» = Registro de entrada. – «1» = Registro de salida. |
| Documentación física y/o soportes. | Número | 1 | Obligatorio | Indica si el fichero va acompañado de documentación física: – «1» = Acompaña documentación física (u otros soportes) requerida. – «2» = Acompaña documentación física (u otros soportes) complementaria. – «3» = No acompaña documentación física ni otros soportes. |
| Observaciones del apunte. | Alfanumérico | 50 | Opcional | Observadores del registro de datos de intercambio recogidos por el funcionario de registro. |
| Indicador de pruebas. | Número | 1 | Obligatorio | Indica si el asiento registral es una prueba: – «0» = Normal. – «1» = Prueba. |
| Código Entidad Registral de inicio. | Alfanumérico | 21 | Obligatorio | Código único de la Entidad Registral de inicio obtenido del Directorio Común. |
| Decodificación Entidad Registral de inicio. | Alfanumérico | 80 | Opcional | Descripción de la Entidad Registral de inicio. |

Las consideraciones a tener en cuenta para asignar valor al campo «Documentación física y/o soportes» son:

i. Acompaña documentación física (u otros soportes) requerida («1»). Indica que el mensaje de datos de intercambio debe ser tratado junto con documentación física (u otros soportes) necesaria para su trámite. Por tanto, no se puede aceptar y reenviar (si aplica) el fichero de intercambio hasta que toda la documentación física requerida haya sido recibida en la Entidad Registral de destino. Tampoco se puede dar número de registro oficial a la entrada, dándole temporalmente el tratamiento de «pre-asiento», hasta disponer de la documentación física requerida.

Ejemplo de este caso sería un intercambio en el que se realiza copia electrónica auténtica sóolo de una parte de los documentos presentados, o cuando dichas copias no se pueden realizar (no se dispone de medios o el soporte no permite la digitalización correcta, como en el caso de sobres cerrados).

ii. Acompaña documentación física (u otros soportes) complementaria («2»). Indica que se envía documentación física (u otros soportes) que acompaña al mensaje de datos de intercambio, pero que esta no es estrictamente necesaria para su trámite. Por tanto, se podría aceptar, pero no se podría reenviar (si aplica) el fichero de intercambio hasta que toda la documentación física haya sido recibida en la Entidad Registral de destino.

Un ejemplo de esta situación se produce cuando la Entidad Registral de Origen genera copias electrónicas auténticas de documentación presentada en soporte papel y tanto las copias electrónicas como el soporte original en papel, son enviados a la Entidad Registral de destino.

iii. No acompaña documentación física ni otros soportes («3»). Indica que el mensaje de datos de intercambio no se acompaña de ninguna documentación física ni otros soportes. Por tanto, se podría aceptar y reenviar (si aplica) el fichero de intercambio en cuanto llegue a la Entidad Registral de destino.

Además, este segmento incorpora la posibilidad de incluir información sobre la Entidad Registral de Inicio, cuya localización es necesaria para que un mensaje de datos de intercambio, que ha sido rechazado, pueda ser reenviado a la Entidad Registral que originó el proceso de intercambio, sin perder el rastro de la Entidad Registral que generó el reenvío. El modo en que el mensaje de datos de intercambio es reenviado a la Entidad Registral de Inicio se desarrolla en el apartado V de esta norma.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_004.png)

7. Segmento de Formulario Genérico

Este segmento opcional permite el intercambio del contenido de los formularios de propósito general que se implementan en los registros electrónicos.

En caso de uso, además de incluir los datos específicos en este segmento, el formulario genérico debe incluirse como documento en el segmento de Anexo («Datos de Anexo»).

Esto permite que se puedan intercambiar formularios genéricos tanto con registros electrónicos como con registros presenciales. De esta manera, se facilita que los registros presenciales puedan recibir este tipo de formularios sin necesidad de implementar los datos específicos incluidos en este segmento.

Tabla 7. Datos de Formulario Genérico

| Segmento de Formulario Genérico | ☑ Opcional |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Expone. | Alfanumérico | 4.000 | Obligatorio | Exposición de los hechos y antecedentes relacionados con la solicitud. |
| Solicita. | Alfanumérico | 4.000 | Obligatorio | Descripción del objeto de la solicitud. |

IV.3. Estructura y contenido del mensaje de control

La entidad mensaje de control en SICRES 3.0 es un fichero que contiene la información de control y notificación acerca del estado de una operación de intercambio. Estos mensajes son generados por la Entidad Registral destino o por el propio sistema de intercambio, para la gestión del flujo del intercambio.

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_005.png)

A continuación se definen los campos que componen un mensaje de control a utilizar, no así el formato en que se implementen dentro del sistema de gestión de intercambio.

Tabla 8. Datos de Mensaje de Control

| De Mensaje de Control | ☑ Obligatorio |
| --- | --- |
| ☑ Único |
| SICRES 3.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de Origen. | Alfanumérico | 21 | Obligatorio | Código único obtenido del Directorio Común. |
| Código Entidad Registral de destino. | Alfanumérico | 21 | Obligatorio | Código único obtenido del Directorio Común. |
| Identificador de intercambio. | Alfanumérico | 33 | Obligatorio | Identificador de intercambio único de la operación. Se compondrá siguiendo la normalización en el apartado VII.1. |
| Tipo de mensaje. | Alfanumérico | 2 | Obligatorio | Indica el tipo de mensaje (siguiendo la normalización definida en el apartado V.3). Los valores que el tipo de mensaje de control puede tomar son: – «01» = ACK (acepción). – «02» = Error. – «01» = Confirmación. |
| Descripción del mensaje. | Alfanumérico | 1024 | Opcional | Texto descriptivo del mensaje de control. |
| Número de registro de entrada en destino. | Alfanumérico | 20 | Opcional | Número de registro de entrada en la Entidad Registral destino. Utilizado para completar el ciclo de envío. |
| Fecha y hora de entrada en destino. | Alfanumérico | 14 | Opcional | Formato AAAAMMDDHHMMSS. |
| Indicador de prueba. | Número | 1 | Obligatorio | Indica si el mensaje es una prueba: – «0» = Normal. – «1» = Prueba. |
| Identificador de fichero. | Alfanumérico | 50 | Opcional | Identificador del mensaje de datos de que se tiene que reenviar en caso de error. Se compondrá siguiendo la normalización definida en el apartado VII.2, con tipo de fichero= «01» (anexo). Es opcional y múltiple, dado que el error puede producirse durante el envío de cualquiera de los ficheros mensaje de datos de intercambio y anexos (opcionales y múltiples). |
| Código de error. | Alfanumérico | 4 | Opcional | Identifica el tipo de error que se ha producido durante el envío del mensaje de datos de intercambio. Se compondrá siguiendo la normalización definida en el apartado VII.4. Este valor sólo será aplicable en el caso de que el campo «Tipo de Mensaje» tome el valor «Error», codificado como «02». |
