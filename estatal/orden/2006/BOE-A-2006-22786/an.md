## ANEXO

## Reglamento Técnico del Sistema de Verificación de Datos de Identidad

## Primero. Descripción del Sistema de Verificación de Datos de Identidad.

El Sistema de Verificación de Datos de Identidad puesto a disposición de los Departamentos y Organismos de la Administración General del Estado por parte del Ministerio de Administraciones Públicas se establece como servicio horizontal para la consulta y comprobación de los datos del Documento de Identificación del Ciudadano custodiados por la Dirección General de la Policía y de la Guardia Civil en base a lo dispuesto en la Ley Orgánica 2/1986, de 13 de marzo, de Fuerzas y Cuerpos de Seguridad, que atribuye al Cuerpo Nacional de Policía, la función de expedición del Documento Nacional de Identidad y el control de entrada y salida del territorio nacional de españoles y extranjeros. Información que se encuentra registrada y custodiada en los ficheros de la Dirección General de la Policía y de la Guardia Civil, que soportan la gestión del documento nacional de identidad y la Tarjeta de Identificación de Extranjeros (Sus denominaciones, conforme a las Órdenes INT/1751/2002, de 20 de junio e INT/2190/2006, de 19 de junio, son ADDNIFIL y ADEXTTRA, respectivamente).

## Segundo. Adopción de medidas de seguridad, organizativas o técnicas de los organismos y aplicaciones que accedan al Sistema de Verificación de Datos de Identidad.

1. Con carácter general los organismos que accedan al Sistema de Verificación de Datos de Identidad cumplirán con las medidas de seguridad, conservación y normalización que se detallan en los Criterios de seguridad, normalización y conservación de las aplicaciones utilizadas para el ejercicio de potestades aprobados por el Consejo Superior de Administración Electrónica mediante Resolución de 26 de mayo de 2003 y revisiones posteriores.

2. El alcance e intensidad de aplicación de las medidas de seguridad, conservación y normalización vendrán determinadas por el resultado del análisis y gestión de riesgos que se realice, recomendándose a estos efectos la utilización de la Metodología de Análisis y Gestión de Riesgos de los Sistemas de Información (MAGERIT) del Consejo Superior de Administración Electrónica.

3. Lo dispuesto en esta Orden Ministerial se aplicará de conformidad con lo previsto en la Ley Orgánica 15/1999, de 13 de diciembre, de Protección de Datos de Carácter Personal y en el Reglamento de Medidas de Seguridad de los ficheros automatizados de datos de carácter personal aprobado por Real Decreto 994/1999, de 11 de junio.

## Tercero. Acceso al Sistema de Verificación de Datos de Identidad.

1. El acceso al Sistema de Verificación de Datos de Identidad se realizará a través del Sistema de Aplicaciones y Redes para las Administraciones Públicas, siguiendo el esquema de conexión que ésta tiene establecido para cualquier organismo público. Sólo en casos debidamente justificados y previa aprobación, por parte de la Secretaría del Consejo Superior de Administración Electrónica, de un plan para la ordenación de las comunicaciones se habilitarán temporalmente mecanismos de conexión alternativos.

2. El Sistema de Verificación de Datos de Identidad presentará dos formas alternativas de acceso para realizar las correspondientes consultas sobre la veracidad de ciertos datos de identidad:

Un interfaz accesible a través de un navegador de Internet, conforme al RFC 2616: Protocolo de Transferencia de Hipertexto - HTTP/1.1 del IETF, donde un empleado público, debidamente acreditado e identificado, podrá realizar consultas con sólo disponer de un navegador con acceso al Sistema de Aplicaciones y Redes para las Administraciones Públicas y firma electrónica.

Un interfaz automatizado de servicio web, conforme al estándar WSDL 1.1 o superior del W3C cuya definición inicial, y sucesivas actualizaciones, serán puestas a disposición de los Organismos a través del Consejo Superior de Administración Electrónica y su Comisión Permanente.

## Cuarto. Requisitos de autenticidad para el acceso al Sistema de Verificación de Datos de Identidad.

1. Los accesos al Sistema de Verificación de Datos de Identidad se efectuarán utilizando certificados electrónicos reconocidos.

2. Los certificados electrónicos que se utilicen para identificarse ante el Sistema de Verificación de Datos de Identidad deberán ser certificados reconocidos que cumpla la recomendación UIT X.509 versión 3 o superiores (ISO/IEC 9594-8 de 1997).

3. No podrán utilizarse certificados electrónicos caducados o revocados para acceder al Sistema de Verificación de Datos de Identidad.

## Quinto. Requisitos de confidencialidad del Sistema de Verificación de Datos de Identidad.

1. El Sistema de Verificación de Datos de Identidad ofrecerá consultas en las que, a partir del Número del Documento de Identificación del Ciudadano o Extranjero, se devolverá el total, o un subconjunto, de los datos incorporados en dicho documento:

Nombre y apellidos del titular del documento.

Lugar y fecha de nacimiento.

Nombre de los padres.

Sexo.

Estado de vigencia del Documento.

El conjunto de datos a los que tenga acceso cada usuario del sistema será establecido, previa autorización y justificación, por parte del responsable en la Organización Administrativa.

2. Sólo organismos públicos debidamente autorizados tendrán acceso al Sistema de Verificación de Datos de Identidad. En todo organismo público existirá un responsable o administrador delegado del sistema que autorizará los accesos al Sistema de Verificación de Datos de Identidad.

3. Para realizar la consulta al Sistema de Verificación de Datos de Identidad, será preciso el consentimiento del interesado cuyos datos se vayan a verificar, salvo que una norma con rango de ley autorice dicha consulta. Dicho consentimiento deberá constar en la solicitud de iniciación del procedimiento, o en cualquier otra comunicación posterior, siempre y cuando dicha comunicación sea previa a la consulta en el sistema, no pudiendo realizarse consulta alguna en caso de no contar con el consentimiento de forma fehaciente. Los impresos o formularios electrónicos de solicitudes de iniciación de procedimientos administrativos deberán adecuarse para recoger dicho consentimiento.

4. La consulta y el acceso a la información proporcionada por el Sistema de Verificación de Datos de Identidad deberá realizarse con una finalidad concreta, que quedará recogida en el momento de la consulta.

## Sexto. Requisitos de integridad de la información proporcionada por el Sistema de Verificación de Datos de Identidad.

Todas las consultas que se realicen al Sistema de Verificación de Datos de Identidad, así como las respuestas que devuelva el propio sistema, deberán haber sido firmadas electrónicamente. Esta firma electrónica tiene por objeto garantizar la integridad de los datos intercambiados como la identidad de las partes que intervienen y el no repudio de la consulta.

De la misma forma, todas las consultas que el Sistema de Verificación de Datos de Identidad deba realizar a la Dirección General de la Policía y de la Guardia Civil, así cómo las correspondientes respuestas obtenidas resultado de las mismas, habrán de ser debidamente firmadas electrónicamente para garantizar tanto la integridad de la información como la identidad de ambos organismos.

## Séptimo. Requisitos de disponibilidad de la información proporcionada por el Sistema de Verificación de Datos de Identidad.

El Sistema de Verificación de Datos de Identidad estará disponible los 7 días de la semana las 24 horas del día.

## Octavo. Garantías jurídicas del Sistema de Verificación de Datos de Identidad ante posibles recursos.

1. El servicio web proporcionado por este sistema sigue el estándar de intercambio de datos definido por «Sustitución de Certificados en Soporte Papel» del Consejo Superior de Administración Electrónica, que reúne, en base a la normativa vigente, las garantías jurídicas aplicables al intercambio de datos entre Administraciones Públicas.

2. El Sistema de Verificación de Datos de Identidad dispondrá de un módulo de auditoría, en el que quedarán registradas todas las consultas de datos de identidad realizadas, información de contexto asociada, como la identidad del solicitante, la fecha y la finalidad de la consulta, y aquellos eventos relevantes desencadenados a partir de la propia consulta. Se garantizará la integridad y no repudio de la información registrada mediante técnicas de firma electrónica y sellado de tiempo, estableciéndose, asimismo, medidas técnicas para garantizar la disponibilidad y recuperación de aquella información que no se mantenga on-line por motivos de eficiencia técnica o seguridad.

3. Para certificar la fecha y tiempo de las actividades y sucesos registrados en el Sistema de Verificación de Datos de Identidad se hará uso del Servicio de Sellado de Tiempo de la Plataforma de Firma Electrónica del Ministerio de Administraciones Públicas, sincronizada con el Real Instituto y Observatorio de la Armada, de conformidad con lo previsto sobre la hora legal en el Real Decreto 1308/1992, de 23 de octubre, por el que se declara el Laboratorio de la Armada como laboratorio depositario del patrón nacional de Tiempo y laboratorio asociado al centro Español de Metrología, y según las condiciones técnicas y protocolos que el citado Organismo establezca.

4. Sólo personal de la Administración Pública debidamente autorizado y acreditado podrá acceder a las funcionalidades de auditoría del Sistema de Verificación de Datos de Identidad.

## Noveno. Condiciones de la prestación del servicio.

1. La gestión del Sistema de Verificación de Datos de Identidad corresponde al Ministerio de Administraciones Públicas.

2. Los organismos públicos que hagan uso de este servicio estarán sujetos a las medidas de seguridad, los requisitos de autenticidad, integridad, confidencialidad, disponibilidad y criterios técnicos establecidos en esta Orden Ministerial.

3. Para poder acceder al Sistema de Verificación de Datos de Identidad, los Organismos Administrativos deberán designar a un responsable, tal y como se indica en el apartado segundo del punto quinto del presente anexo técnico, que será el encargado de autorizar a los accesos en su organismo. El nombramiento y cese de este responsable deberá ser comunicado al Ministerio de Administraciones Públicas, para la asignación de los permisos adecuados de acceso al sistema o la cancelación de los mismos.
