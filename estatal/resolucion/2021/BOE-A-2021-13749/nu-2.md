## IV. Modelo de datos para el intercambio de asientos entre Entidades Registrales

IV.1 Definición y características generales de SICRES 4.0.

SICRES 4.0 constituye el modelo de datos para el intercambio de asientos entre Entidades Registrales. Esta versión de SICRES, alineada con la filosofía de sus predecesoras, tiene como finalidad contribuir a garantizar la interconexión entre organizaciones, permitiendo así, un servicio de mayor calidad a los ciudadanos tal y como marca la Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas.

Las principales características de SICRES 4.0 que la diferencian de sus versiones anteriores son:

i. Reordenación, actualización e incorporación de campos. El modelo de intercambio SICRES 4.0 agrupa y reordena los campos de los distintos segmentos para dotarlos de mayor contenido semántico y facilitar su interpretación. Asimismo, se eliminan o actualizan campos obsoletos y se incorporan nuevos campos.

ii. Referenciación de documentos electrónicos. Se sustituye el intercambio de los ficheros de los documentos electrónicos objeto de registro e intercambio, por el intercambio de referencias a tales documentos electrónicos. De este modo, se optimiza el funcionamiento de la Plataforma de Intercambio y se superan limitaciones de la misma.

iii. Metadatado para automatización del tratamiento de los asientos registrales y sus documentos anexos. Se incorporan en el intercambio registral nuevos metadatos destinados a facilitar la automatización del tratamiento de los asientos y los documentos electrónicos. Asimismo, se incorpora la posibilidad de intercambiar otros metadatos no definidos a priori, bien sea para cubrir necesidades futuras, o bien sea para cubrir necesidades particulares de cada organismo.

Durante el período de transición de las aplicaciones de registro de SICRES 3.0 a SICRES 4.0 se garantizará la interoperabilidad entre ambas normas. La plataforma de intercambio de asientos registrales SIR se encargará de garantizar la compatibilidad y la comunicación entre aplicaciones de registro que utilicen diferentes versiones de la norma.

El modelo conceptual de espacio de intercambio bajo SICRES 4.0 aparece en la siguiente figura:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/190/13749_10140202_1.png)

Según este esquema, el espacio de intercambio engloba todo el proceso de intercambio desde la Unidad de Tramitación Origen hasta la Unidad Tramitación Destino proporcionando un contexto único a cada uno de los intercambios. Dentro de este espacio, destacan los siguientes elementos:

Unidades de Tramitación de Origen y Destino: Entidades, o unidades pertenecientes a dichas entidades, responsables de la tramitación de los documentos registrados. La identificación de ambas Unidades debe ser única a través de Directorios unificados, como se indica en el apartado VI.4 de esta norma.

Entidad Registral de Origen y Destino. Entidades, o unidades pertenecientes a dichas entidades, que, bien sea por medio del personal al servicio del mismo, o bien sea por medio de actuación automatizada, se encarga tanto de inscribir los asientos de entrada y salida en el Registro Electrónico de la Administración u Organismo, como de llevar a cabo el proceso de intercambio registral, responsabilizándose del envío y recepción de Mensajes de Datos de Intercambio y Mensajes de Control, desde el punto de vista técnico y de comunicación, pero sin implicación en la tramitación de los documentos. La identificación de ambas Entidades Registrales debe ser única a través de Directorios unificados, como se indica en el apartado VI.4 de esta norma.

Mensaje de datos de intercambio. Es creado y emitido por la Entidad Registral de Origen y alberga, además de campos para el control e identificación, la información del asiento registral y los documentos correspondientes adjuntos. Su estructura y formato se definen en el apartado IV.2 de esta norma.

Mensajes de control. Son emitidos por la Entidad Registral destino o por el propio sistema de intercambio y proporcionan información de estado para la gestión de la operación de intercambio. Su estructura y formato se definen en el apartado IV.3 de esta norma.

Sistema de intercambio. Proporciona la gestión del intercambio y la comunicación directa con las Entidades Registrales Origen y Destino. Sus funciones y requisitos técnicos deben cumplir lo establecido en el apartado VI de esta norma.

Plataforma de intercambio. Comprende el Sistema de intercambio y las Entidades Registrales de Origen y de Destino.

El proceso de intercambio inicia y finaliza en la Entidad Registral de Origen, punto de contacto con el ciudadano o Unidad de Tramitación que origina la creación del asiento registral.

El inicio viene marcado por la generación del mensaje de datos de intercambio en la Entidad Registral Origen conteniendo la información del asiento. A través del sistema de intercambio, este mensaje es recibido en la Entidad Registral destino, que, si procede, confirma la recepción correcta al Origen a través del mensaje de control correspondiente.

Los intercambios disfrutan de un contexto único dentro del espacio SICRES mediante la asignación de un identificador del intercambio único a cada proceso de transacción que es generado por la aplicación de registro de la Entidad Registral de Origen y acompaña tanto al mensaje de datos de intercambio como a los mensajes de control relacionados. La generación del identificador del intercambio se detalla en el apartado V.1 de esta NTI.

IV.2 Estructura y contenido del mensaje de datos de intercambio.

El mensaje de datos de intercambio de SICRES4.0 es el mensaje que alberga la información objeto del intercambio. Su codificación se especifica con un ejemplo de implementación del modelo en XML en el Anexo 2 de esta norma.

Este mensaje está compuesto por los 7 segmentos que aparecen en la figura y cuya descripción funcional se desarrolla a continuación.

![imagen](https://www.boe.es/datos/imagenes/disp/2021/190/13749_10140203_1.png)

Segmento de Origen (o Remitente).

| Segmento de Origen (o Remitente) | ☑ Obligatorio ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de Origen. | Alfanumérico. | 21 | Obligatorio. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Decodificación de Entidad Registral de Origen. | Alfanumérico. | 120 | Opcional. | Descripción de la Entidad Registral de Origen. |
| Código de la Unidad de Tramitación de Origen. | Alfanumérico. | 21 | Condicional. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. La cumplimentación de este campo es obligatoria cuando el emisor del registro es un órgano u organismo perteneciente o dependiente de una Administración Pública. |
| Decodificación de la Unidad de Tramitación de Origen. | Alfanumérico. | 120 | Opcional. | Descripción de la Unidad de Tramitación Origen. |

Tabla 1. Datos de Origen (o Remitente)

La cumplimentación de la Unidad de Tramitación de Origen será obligatoria cuando el emisor del registro sea un órgano u organismo perteneciente o dependiente de una Administración Pública, como se indica en el comentario del campo.

Sin embargo, no será obligatoria la cumplimentación de este campo en los reenvíos o rechazos que se realicen de registros emitidos por Administraciones Públicas. Asimismo, tampoco será obligatoria la cumplimentación, en envíos registrales que se traten de rectificaciones de intercambios previos. Es decir, en envíos registrales que realicen órganos y organismos de las Administraciones Públicas como consecuencia de haber confirmado por error un registro que habían recibido.

B) Segmento de destino.

| Segmento de destino (o destinatario) | ☑ Obligatorio ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de Destino. | Alfanumérico. | 21 | Obligatorio. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Decodificación Entidad Registral de Destino. | Alfanumérico. | 120 | Opcional. | Descripción de Entidad Registral de destino. |
| Código de la Unidad de Tramitación de Destino. | Alfanumérico. | 21 | Condicional. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. La cumplimentación de este campo es obligatoria cuando el destinatario del registro es un órgano u organismo perteneciente o dependiente de una Administración Pública. |
| Decodificación de la Unidad de Tramitación de Destino. | Alfanumérico. | 120 | Opcional. | Descripción de la Unidad de Tramitación de destino. |

Tabla 2. Datos de destino

C) Segmento de Interesado.

Este segmento comprende los datos que identifican al Interesado y su Representante en la entidad mensaje de datos de intercambio. Este segmento se puede declarar de forma múltiple. Su condicionalidad se define en los comentarios de los campos «Datos del Interesado» y «Datos del Representante».

| Segmento de Interesado | ☑ Condicional ☑ Múltiple |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Datos del Interesado. | Tipo complejo. (Datos Persona). |  | Condicional. | Este campo comprende todos los datos personales del interesado; tanto datos de identidad, como datos de contacto e información relativa a los canales de notificaciones. Este campo deberá cumplimentarse siempre que el intercambio se realice en el marco de un procedimiento administrativo en el cual existe y se conoce el interesado. En cualquier caso, será obligatorio siempre que se trate de un registro de entrada. También deberá tenerse en cuenta que será obligatorio siempre que se indique Representante. Estos campos deberán cumplimentarse con independencia de que la información sea redundante con la ya indicada en los Segmentos de Origen o Destino. Se compone de los siguientes campos: Datos de identificación, Datos de contacto, Receptor notificaciones y Canales de notificación. |
| Datos del Representante. | Tipo complejo. (Datos Persona). |  | Condicional. | Este campo comprende todos los datos personales del representante; tanto datos de identidad, como datos de contacto e información relativa a los canales de notificación. Este campo no podrá cumplimentarse si no se ha cumplimentado el campo «Datos del Interesado». Se compone de los siguientes campos: Datos de identificación, Datos de contacto, Receptor notificaciones y Canales de notificación. |
| Observaciones. | Alfanumérico. | 160 | Opcional. | Observaciones del Interesado y/o del Representante. |
| Tipo complejo: Datos Persona. |
| Datos de identificación. | Tipo complejo. (Datos Identificación). |  | Obligatorio. | Se compone de los siguientes campos: «Tipo de persona», «Tipo de Documento de Identificación», «Documento de Identificación», «Razón social», «Código de Directorios Unificado», «Nombre», «Primer apellido» y «Segundo apellido». |
| Datos de contacto. | Tipo complejo (Datos Contacto). |  | Opcional. | Se compone de los siguientes campos: «Dirección postal», «Dirección Electrónica Habilitada», «Correo electrónico», «Teléfono» y «Teléfono móvil». |
| Receptor de notificaciones. | Booleano. |  | Opcional. | En escenarios con múltiples interesados y/o representantes, por medio de los valores booleanos «true» o «false», permite seleccionar expresamente cuál de los interesados o representantes será el que reciba las notificaciones. Tal y como el artículo 7 de la Ley 39/2015, por defecto, las notificaciones se remitirán al primer interesado que se consigne. |
| Canales de notificación y aviso. | Tipo complejo. (Canales Notificación). |  | Opcional. | De acuerdo con la Ley 39/2015, permite indicar preferencias en cuanto a los canales de recepción de notificaciones y avisos de notificaciones. |
| Tipo complejo: Datos Identificación. |
| Tipo de persona. | Alfanumérico. | 1 | Obligatorio. | «1» = Persona física. «2» = Persona jurídica. |
| Tipo de Documento de Identificación. | Alfanumérico. | 1 | Obligatorio. | Identificación del interesado o representante: ‘N’ = NIF. ‘C’ = CIF. ‘P’ = Pasaporte. ‘E’ = Documento de identificación de extranjeros. ‘X’ = Otros de persona física. ‘O’ = Código de Origen. |
| Documento de Identificación. | Alfanumérico. | 256 | Obligatorio. | Alfanumérico con la sintaxis adecuada en función del campo «Tipo de Documento de Identidad». |
| Razón Social. | Alfanumérico. | 80 | Condicional. | Obligatorio si es persona jurídica. |
| Código de Directorios Unificados. | Alfanumérico. | 21 | Opcional. | Código del Interesado dentro de alguno de los Directorios Unificados contemplados en el Apartado VI.4 de esta norma. Dependiendo del directorio empleado, permitirá, entre otros, obtener información complementaria del interesado o identificar unidades dentro de la estructura jerárquica en la que se pueda descomponer el interesado. |
| Nombre. | Alfanumérico. | 30 | Condicional. | Obligatorio si es persona física. |
| Primer apellido. | Alfanumérico. | 30 | Condicional. | Obligatorio si es persona física. |
| Segundo apellido. | Alfanumérico. | 30 | Opcional. |  |
| Tipo complejo: Datos Contacto. |
| Dirección postal. | Tipo complejo. (Dirección Postal). |  | Condicional. | Se compone de los siguientes campos: «País», «Provincia», «Municipio», «Dirección» y «Código Postal». Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación. |
| Correo electrónico. | Alfanumérico. | 160 | Condicional. | Dirección de correo electrónico. Obligatorio cumplimentarlo si se solicita aviso de puesta a disposición de la notificación por correo electrónico. |
| Teléfono móvil. | Alfanumérico. | 20 | Condicional. | Obligatorio cumplimentarlo si se solicita aviso de puesta a disposición de la notificación por SMS. |
| Teléfono fijo. | Alfanumérico. | 20 | Opcional. |  |
| Tipo complejo: Dirección Postal. |
| País. | Alfanumérico. | 4 | Condicional. | Atributo según catálogo del INE. Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación. |
| Provincia. | Alfanumérico. | 2 | Condicional. | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación y el país es España. |
| Municipio. | Alfanumérico. | 5 | Condicional. | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación y el país es España. |
| Dirección. | Alfanumérico. | 160 | Condicional. | Dirección. Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación. |
| Código postal. | Alfanumérico. | 5 | Condicional. | Atributo según catálogo del anexo de la OM del Padrón (11/7/1997). Obligatorio cumplimentarlo si se establece el canal no telemático como canal preferente de notificación y el país es España. |
| Tipo complejo: Canales Notificación. |
| Canal preferente de notificación. | Alfanumérico. | 1 | Opcional. | Permite indicar, en el caso de personas físicas, el canal preferente para la recepción de las notificaciones, de acuerdo con la Ley 39/2015: «1» = Notificación en papel. «2» = Notificación por medios electrónicos (siendo la administración quién, para cada trámite, decidirá si se efectúa por comparecencia en sede electrónica o en DEHú,o en ambas, pero debiendo ser en todo caso accesible desde el Punto de Acceso General). |
| Solicita aviso de notificación por SMS. | Booleano. |  | Opcional. | Permite al interesado indicar si desea recibir por este canal aviso de puesta a disposición de la notificación. |
| Solicita aviso de notificación por correo electrónico. | Booleano. |  | Opcional. | Permite al interesado indicar si desea recibir por este canal aviso de puesta a disposición de la notificación. |

Tabla 3. Datos de Interesado

Los campos «Dirección postal», «Correo electrónico» o «Teléfono móvil» son condicionales de modo que, se pueden cumplimentar voluntariamente, en cualquier caso, pero deben cumplimentarse obligatoriamente si el canal de contacto en cuestión ha sido seleccionado expresamente en el campo «Canal preferente de notificaciones», en «Solicita aviso de puesta a disposición de la notificación por correo electrónico» o en «Solicita aviso de puesta a disposición de la notificación por SMS», respectivamente.

El campo «Canal preferente de notificaciones» no podrá tener el valor «1» para interesados obligados a relacionarse electrónicamente con las administraciones.

D) Segmento de Asiento.

| Segmento de Asiento | ☑ Obligatorio ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Modo de registro. | Alfanumérico. | 2 | Obligatorio. | "01" = Registro presencial en Oficina de Asistencia en Materia de Registro. "02" = Registro electrónico (desde sede electrónica, registros electrónicos generales o particulares u otros servicios electrónicos). |
| Tipo del registro. | Alfanumérico. | 1 | Obligatorio. | "0" = Registro de entrada. "1" = Registro de salida. |
| Número de registro en la Entidad Registral de Origen o Inicio. | Alfanumérico. | 20 | Obligatorio. | Número de registro en la Entidad Registral de Origen o Inicio. |
| Fecha y hora de registro en Origen o Inicio. | Alfanumérico. | 19 | Obligatorio. | Formato AAAAMMDDHHMMSSZ. |
| Timestamp de registro en Origen o Inicio. | Alfanumérico. | Variable | Opcional. | Sello de tiempo del registro en Origen o Inicio. |
| Fecha y hora de presentación por el interesado. | Alfanumérico. | 19 | Obligatorio. | Formato AAAAMMDDHHMMSSZ. Coincidirá con la de registro si se registra en el mismo momento en el que se presenta por el interesado. |
| Timestamp de presentación por el interesado. | Alfanumérico. | Variable | Opcional. | Sello de tiempo de la presentación por el interesado. |
| «Abstract» o Resumen. | Alfanumérico. | 240 | Obligatorio. |  |
| Código SIA. | Alfanumérico. |  | Opcional. | Código del procedimiento o servicio en el marco del cual se realiza la tramitación administrativa. Se obtendrá del Sistema de Información Administrativa. |
| Número de expediente. | Alfanumérico. |  | Opcional. | Número del expediente objeto de la tramitación administrativa. Deberá emplearse el formato normalizado de Identificador de expediente establecido en la NTI de Expediente Electrónico. |
| Código de asunto según destino. | Alfanumérico. | 16 | Opcional. | Codificación del asunto en destino, si la solicitud incluye ese dato. Se procurará definir solicitudes que incluyan el código para permitir el manejo automatizado del asiento en destino. |
| Referencia externa. | Alfanumérico. | 16 | Opcional. | Cualquier referencia que el destino precise conocer y sea conocida por el solicitante (matrícula de vehículo, número de recibo cuyo importe se reclama, etc.). |
| Otros metadatos generales. | Tipo complejo. (Metadatos). |  | Condicional. | Secuencia de campos del tipo «Campo» y «Valor» empleados para transmitir atributos del asiento que atiendan a necesidades generales. |
| Otros metadatos particulares. | Tipo complejo. (Metadatos). |  | Opcional. | Secuencia de campos del tipo «Campo» y «Valor» empleados para transmitir atributos del asiento que atiendan a necesidades particulares de la Unidad de Tramitación de Destino. |
| Tipo complejo: Metadatos. |
| Campo. | Alfanumérico. | 80 | Opcional. | Nombre del metadato (general o particular) que se intercambia. |
| Valor. | Alfanumérico. | Variable | Opcional. | Valor del metadato (general o particular) indicado en el campo «Campo» anterior. |

Tabla 4. Datos de Asunto

El formato de las fechas y horas de registro y presentación es yyyyMMddHHmmssZ, donde Z representa la variación en horas y minutos respecto a GMT (Ejemplo: 20200917124020+0200).

Los campos «Otros metadatos generales», «Otros metadatos particulares», «Campo» y «Valor» permiten intercambiar otros metadatos relativos al asiento adicionales a los ya transmitidos en campos nativos de la norma SICRES.

En el caso de «Otros metadatos generales», el listado de atributos a intercambiar (es decir, el listado de posibles contenidos del campo «Campo») será acordado y fijado por las Administraciones Públicas, con independencia de la aprobación de la NTI y pudiendo ser modificado a lo largo del tiempo. Los atributos de este listado podrán tener carácter opcional, condicional u obligatorio, por lo que deberán ser implementados por todas las Entidades Registrales.

En el caso de «Otros metadatos particulares», el listado de atributos a intercambiar (es decir, el listado de posibles contenidos del campo «Campo») será determinado por la Unidad de Tramitación de Destino que lo desee atendiendo a sus necesidades particulares, pudiendo establecerse un único listado a emplear por todos los orígenes, o listados particulares para determinados orígenes. Estos atributos serán siempre opcionales.

E) Segmento de Anexo.

Este segmento comprende datos e información relativa a los documentos electrónicos que son objeto de registro e intercambio. En el caso de justificantes de registro, su intercambio como documento anexo es opcional.

El segmento contiene la referencia única del documento electrónico a intercambiar. Esta referencia única consiste en un conjunto de campos con metadatos que permiten al destino la identificación unívoca del documento, la localización del repositorio en el que se encuentra almacenado y, en su caso, la acreditación de permisos para su acceso. Los campos y formatos de la referencia única del documento serán acordados y establecidos por las Administraciones Públicas al margen de esta NTI y pudiendo ser modificados a lo largo del tiempo. Esta información se recoge en la «Especificación del Sistema de referenciación de documentos en las AAPP» del Foro por el Documento Electrónico – Documentación para la Tramitación Automatizada (https://administracionelectronica.gob.es/comunidades/verPestanaDocumentacion.htm?idComunidad=141).

Este segmento es opcional y puede declararse de forma múltiple.

| Segmento de Anexo | ☑ Opcional ☑ Múltiple |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Nombre del fichero anexado. | Alfanumérico. | 80 | Obligatorio. | Nombre del fichero original, incluyendo la extensión del fichero. |
| Identificador de fichero. | Alfanumérico. | 50 | Obligatorio. | Se compondrá siguiendo la normalización definida en el Anexo 1B. |
| Tipo de anexo. | Alfanumérico. | 2 | Obligatorio. | Indica el tipo de documento: – ‘01’ = Justificante de registro. – ‘02’ = Documento adjunto. – ‘03’ = Otro. |
| Tipo MIME. | Alfanumérico. | 80 | Opcional. | Tipo del fichero Anexo. |
| Anexo. | Tipo complejo (Especificación del Sistema de referenciación de documentos en las AAPP). |  | Opcional. | Metadatos y referencia al documento electrónico registrado e intercambiado. Su estructura cumplirá la Especificación del Sistema de referenciación de documentos en las AAPP. |
| Resumen. | Alfanumérico. | 160 | Opcional. | Texto con descripción breve del contenido y naturaleza del anexo. |
| Código del formulario. | Alfanumérico. | 80 | Opcional. | Código del formulario o documento normalizado anexado. |
| Otros metadatos generales. | Tipo complejo. (Metadato). |  | Opcional. | Secuencia de campos del tipo «Campo» y «Valor» empleados para transmitir atributos del anexo que atiendan a necesidades generales. |
| Otros metadatos particulares. | Tipo complejo. (Metadato). |  | Condicional. | Secuencia de campos del tipo «Campo» y «Valor» empleados para transmitir atributos del anexo que atiendan a necesidades particulares de la Unidad de Tramitación de Destino. |
| Observaciones. | Alfanumérico. | 160 | Opcional. | Observaciones del fichero adjunto. |
| Tipo complejo: Metadato. |
| Campo. | Alfanumérico. | 80 | Opcional. | Nombre del metadato (general o particular) que se intercambia. |
| Valor. | Alfanumérico. | Variable | Opcional. | Valor del metadato (general o particular) indicado en el campo «Campo» anterior. |

Tabla 5. Datos de Anexo

F) Segmento de Internos y Control.

| Segmento de Internos y Control | ☑ Obligatorio ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Identificador de Intercambio. | Alfanumérico. | 33 | Obligatorio. | Identificador de Intercambio único de la operación. Se compondrá siguiendo la normalización definida en el Anexo 1 A. |
| Tipo de transporte de entrada. | Alfanumérico. | 2 | Opcional. | Formas de llegada al registro de entrada: – ‘01’ = Servicio de Mensajeros. – ‘02’ = Correo postal. – ‘03’ = Correo postal certificado. – ‘04’ = Burofax. – ‘05’ = En mano. – ‘06’ = Fax. – ‘07’ = Otros. – ‘08’ = Otros medios electrónicos. |
| Número de transporte de entrada. | Alfanumérico. | 40 | Opcional. | Referencia del transporte. Código. En el caso de certificados, número del mismo. |
| Nombre de usuario. | Alfanumérico. | 80 | Opcional. | Nombre del usuario de Origen. |
| Contacto de usuario. | Alfanumérico. | 160 | Opcional. | Contacto del usuario de Origen (teléfono o dirección de correo electrónico). |
| Aplicación y versión emisora. | Alfanumérico. | 20 | Opcional. | Identifica la aplicación y su versión. |
| Tipo de Anotación. | Alfanumérico. | 2 | Obligatorio. | Indica el motivo de la anotación (siguiendo la normalización definida en el apartadoV.2). Los únicos valores posibles para el mensaje de datos de intercambio son: – ‘01’= Pendiente (sin Identificador de Intercambio). – ‘02’ = Envío. – ‘03’ = Reenvío. |
| Descripción del Tipo de Anotación. | Alfanumérico. | 160 | Opcional. |  |
| Documentación física y/o soportes. | Número. | 1 | Obligatorio. | Indica si el fichero va acompañado de documentación física. – ‘1’ = Acompaña documentación física (u otros soportes) requerida. – ‘2’ = Acompaña documentación física (u otros soportes) complementaria. – ‘3’ = No acompaña documentación física ni otros soportes. |
| Observaciones del apunte. | Alfanumérico. | 160 | Opcional. | Observaciones del registro de datos de intercambio recogidos por el funcionario de registro. |
| Indicador de prueba. | Número. | 1 | Opcional. | Indica si el asiento registral es una prueba. – ‘0’ = Normal. – ‘1’ = Prueba. |
| Identificador de intercambio previo. | Alfanumérico. | 33 | Opcional. | En caso de que el intercambio registral se trate de una rectificación de un intercambio previo, es decir, se trate de un envío como consecuencia de haber confirmado por error un registro recibido, este campo permitirá vincular este intercambio registral con el previo. |
| Código Entidad Registral de Inicio. | Alfanumérico. | 21 | Obligatorio. | Código único de la Entidad Registral de Inicio obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Decodificación Entidad Registral de Inicio. | Alfanumérico. | 120 | Opcional. | Descripción de la Entidad Registral de Inicio. |
| Código de la Unidad de Tramitación de Inicio. | Alfanumérico. | 21 | Opcional. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Decodificación de la Unidad de Tramitación de Inicio. | Alfanumérico. | 120 | Opcional. | Descripción de la Unidad de Tramitación Inicio. |

Tabla 6. Datos de Internos y Control

Las consideraciones a tener en cuenta para asignar valor al campo ‘Documentación física y/o soportes’ son:

i. Acompaña documentación física (u otros soportes) requerida (‘1’). Indica que el mensaje de datos de intercambio debe ser tratado junto con documentación física (u otros soportes) necesaria para su trámite. Por tanto, no se puede aceptar y reenviar (si aplica) el fichero de intercambio hasta que toda la documentación física requerida haya sido recibida en la Entidad Registral de destino. Tampoco se puede dar número de registro oficial a la entrada, dándole temporalmente el tratamiento de ‘pre-asiento’, hasta disponer de la documentación física requerida.

Ejemplo de este caso, sería un intercambio en el que se realiza copia electrónica auténtica sólo de una parte de los documentos presentados, o cuando dichas copias no se pueden realizar (no se dispone de medios o el soporte no permite la digitalización correcta, como en el caso de sobres cerrados).

ii. Acompaña documentación física (u otros soportes) complementaria (‘2’). Indica que se envía documentación física (u otros soportes) que acompaña al mensaje de datos de intercambio, pero que ésta no es estrictamente necesaria para su trámite. Por tanto, se podría aceptar, pero no se podría reenviar (si aplica) el fichero de intercambio hasta que toda la documentación física haya sido recibida en la Entidad Registral de destino.

iii. No acompaña documentación física ni otros soportes (‘3’). Indica que el mensaje de datos de intercambio no se acompaña de ninguna documentación física ni otros soportes. Por tanto, se podría aceptar y reenviar (si aplica) el fichero de intercambio en cuanto llegue a la Entidad Registral de destino.

Además, este segmento incorpora la posibilidad de incluir información sobre la Entidad Registral de Inicio, cuya localización es necesaria para que un mensaje de datos de intercambio, que ha sido rechazado, pueda ser reenviado a la Entidad Registral que originó el proceso de intercambio, sin perder el rastro de la Entidad Registral que generó el reenvío. El modo en que el mensaje de datos de intercambio es reenviado a la Entidad Registral de Inicio se desarrolla en el apartado V de esta norma.

![imagen](https://www.boe.es/datos/imagenes/disp/2021/190/13749_10143168_1.png)

Del mismo modo, el segmento incorpora también la posibilidad de incluir información sobre la Unidad de Tramitación de Inicio.

G) Segmento de Formulario Genérico.

| Segmento de Formulario Genérico | ☑ Opcional ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Expone. | Alfanumérico. | 4000 | Obligatorio. | Exposición de los hechos y antecedentes relacionados con la solicitud. |
| Solicita. | Alfanumérico. | 4000 | Obligatorio. | Descripción del objeto de la solicitud. |

Tabla 7. Datos de Formulario Genérico

Este segmento opcional permite el intercambio del contenido de los formularios de propósito general que se implementan en los registros electrónicos.

Si se utiliza, además de incluir los datos específicos de este segmento, el formulario genérico se deberá incluir como documento anexo en el segmento de Anexo.

Esto permite que se puedan intercambiar formularios genéricos tanto con registros electrónicos con registros presenciales.

IV.3 Estructura y contenido del mensaje de control.

La entidad mensaje de control en SICRES 4.0 es un fichero que contiene la información de control y notificación acerca del estado de una operación de intercambio.

A continuación se definen los campos que componen un mensaje de control a utilizar, no así, el formato en que se implementen dentro del sistema de gestión de intercambio.

| Segmento de Mensaje de Control | ☑ Obligatorio ☑ Único |
| --- | --- |
| SICRES 4.0 |
| Descripción | Tipo | Longitud | Obligación | Comentarios |
| Código Entidad Registral de Origen. | Alfanumérico. | 21 | Obligatorio. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Código Entidad Registral de Destino. | Alfanumérico. | 21 | Obligatorio. | Código único obtenido de Directorios Unificados indicados en el apartado VI.4. |
| Identificador de Intercambio. | Alfanumérico. | 33 | Obligatorio. | Identificador de Intercambio único de la operación. Se compondrá siguiendo la normalización definida en el Anexo 1A. |
| Tipo de mensaje. | Alfanumérico. | 2 | Obligatorio. | Indica el tipo de mensaje (siguiendo la normalización definida en el apartado V.3). Los valores que el tipo de mensaje de control puede tomar son: – ‘01’ = ACK (aceptación). – ‘02’ = Error. – ‘03’ = Confirmación. – ‘04’ = ACK a Confirmación. – ‘05’ = Rechazo. – ‘06’ = ACK a Rechazo. |
| Descripción del mensaje. | Alfanumérico. | 1024 | Opcional. | Texto descriptivo del mensaje de control. |
| Número de registro de entrada en destino. | Alfanumérico. | 20 | Opcional. | Número de registro de entrada en la Entidad Registral destino. Utilizado para completar el ciclo de envío. |
| Fecha y hora de entrada en destino. | Alfanumérico. | 19 | Opcional. | Formato AAAAMMDDHHMMSSZ. |
| Indicador de prueba. | Número. | 1 | Obligatorio. | Indica si el mensaje es una prueba. – ‘0’ =Normal. – ‘1’ =Prueba. |
| Identificador de fichero. | Alfanumérico. | 50 | Opcional. | Identificador del mensaje de datos que se tiene que reenviar en caso de error. Se compondrá siguiendo la normalización definida en el Anexo 1 B, con tipo de fichero = ‘01’ (anexo). Es opcional y múltiple, dado que el error puede producirse durante el envío de cualquiera de los ficheros: mensaje de datos de intercambio y Anexos (opcionales y múltiples). |
| Código de error. | Alfanumérico. | 4 | Opcional. | Identifica el tipo de error que se ha producido durante el envío del mensaje de datos de intercambio. Se compondrá siguiendo la normalización definida en el Anexo 1.D. Este valor sólo será aplicable en el caso de que el campo ‘Tipo de Mensaje’ tome el valor ‘Error’, codificado como ‘02’. |

Tabla 8. Datos de Mensaje de control
