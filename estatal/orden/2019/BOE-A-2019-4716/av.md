## ANEXO V

## Seguimiento de las acciones formativas impartidas en modalidad de teleformación que se refieran a especialidades del Catálogo de Especialidades Formativas

De conformidad con el artículo 17 de la Ley 30/2015, de 9 de septiembre, las acciones formativas impartidas en modalidad de teleformación que se refieran a especialidades del Catálogo de Especialidades Formativas deberán ser objeto de un seguimiento y control efectivo por las administraciones competentes en sus respectivos ámbitos de gestión, que se realizará de forma virtual y presencial.

El seguimiento de carácter virtual se efectuará tanto mediante servicio web, como mediante visita virtual a la acción formativa realizada a través de la plataforma de teleformación, siguiendo las especificaciones indicadas en el presente anexo, sin perjuicio de las actuaciones de seguimiento presencial que se lleven también a cabo.

A. Seguimiento mediante servicio web

El servicio web de seguimiento es la tecnología de intercambio y transferencia de información, mediante la que cada administración laboral competente, con la periodicidad que precise, se conectará automáticamente con las plataformas de teleformación para obtener datos sobre las acciones formativas que se están impartiendo.

El servicio web de seguimiento, con el protocolo de conexión (SOAP) y las especificaciones publicadas en las páginas web de los servicios públicos de empleo del Sistema Nacional de Empleo, deberá estar implementado por las entidades de formación acreditadas e inscritas en la modalidad de teleformación.

Para efectuar el seguimiento mediante servicio web, la única fuente de información considerada válida para proporcionar datos de seguimiento será la URL de seguimiento que a este fin se consignó en la solicitud de acreditación o declaración responsable de inscripción, siendo solamente ésta la fuente que pueda proporcionar dichos datos. La entidad de formación acreditada o inscrita deberá implementar un servicio web que utilizará el Protocolo Simple Object Access Protocol (SOAP) 1.1 sobre HTTPS. Dicho servicio se ajustará a la definición WSDL publicada en las páginas web de los servicios públicos de empleo del Sistema Nacional de Empleo. Es a este servicio web al que invocarán los sistemas de las administraciones públicas competentes.

En el seguimiento mediante servicio web, la recogida, tratamiento y cesión de los datos para el seguimiento de las acciones formativas de formación profesional para el empleo referidas a especialidades del Catálogo de Especialidades Formativas que se impartan en la modalidad de teleformación, se efectuará a través del correspondiente tratamiento automatizado de datos, que deberá ser creado por cada entidad de formación acreditada e inscrita de conformidad con lo establecido en la Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales. La entidad de formación, como responsable del contenido del tratamiento, deberá informar previamente a toda persona física titular de los datos incluidos en el mismo, de la existencia de este tratamiento de datos personales, cuya exclusiva finalidad es realizar la evaluación, seguimiento y control de las acciones formativas desarrolladas por la entidad y cuyo destinatario es la administración laboral competente, recabando su consentimiento expreso para el tratamiento de los datos personales que le conciernen, así como de la posibilidad de ejercer los derechos de acceso, rectificación, supresión, limitación, portabilidad y oposición.

Cada entidad de formación deberá adoptar las medidas de índole técnica y organizativa necesarias que garanticen la seguridad e integridad de los datos de carácter personal contenidos en el fichero.

La confidencialidad de los datos de seguimiento intercambiados en los servicios web quedará garantizada ejecutando el servicio a través de SSL (Secure Sockets Layer), a fin de que los datos se mantengan ocultos para cualquier entidad que, durante la conexión, intente tener acceso a la transmisión de estos datos.

La autentificación de cada Administración Pública competente queda garantizada mediante la utilización del estándar Web Services Security UsernameToken Profile 1.0 OASIS Standard 200401, March 2004. Se emplearán credenciales de tipo wsse: PasswordText.

Las especificaciones referidas a tipo, formato y obligatoriedad de los datos que configuran el fichero estarán disponibles en las páginas web de los servicios públicos de empleo del Sistema Nacional de Empleo.

El servicio de seguimiento ofrecerá las siguientes operaciones:

– Crear el centro de formación (crearCentro), operación mediante la que cada Administración Pública competente asigna a la entidad de formación un código de propio y distintivo y le reporta los datos que la identifican y que fueron consignados en la correspondiente solicitud de acreditación o declaración responsable de inscripción.

– Obtener los datos identificativos del centro de formación (obtenerDatosCentro), operación mediante la que cada Administración Pública competente recoge los datos que identifican a la entidad de formación.

– Crear una acción formativa con su identificador (crearAccion), operación mediante la que cada Administración Pública competente asigna a la entidad de formación acreditada o inscrita un código de acción formativa y le reporta los datos que la identifican y que fueron consignados en la solicitud de autorización de la acción formativa.

– Obtener lista de identificaciones de las acciones formativas iniciadas en el centro de formación (obtenerListaAcciones), operación mediante la que cada Administración Pública competente extrae las acciones formativas que la entidad de formación acreditada o inscrita ha comenzado.

– Obtener los datos de la acción formativa identificada en la petición (obtenerAccion), operación mediante la que cada Administración Pública competente extrae los datos referentes a una acción formativa específica.

– Eliminar la acción formativa identificada en la petición (eliminarAccion), operación mediante la que cada Administración Pública competente suprime los datos referentes a una acción formativa específica.

El mensaje de petición correspondiente a cada una de las operaciones antes indicadas, que identificará la operación de que se trate, será:

– Para la operación crear el centro de formación (crearCentro), los datos identificativos del centro:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8960.png)

– Para la operación obtener los datos identificativos del centro de formación (obtenerDatosCentro), sin parámetros de entrada.

– Para la operación crear una acción formativa con su identificador (crearAccion), los datos referentes a dicha acción:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8594.png)

– Para la operación obtener la lista de identificaciones de las acciones formativas iniciadas en el centro de formación (obtenerListaAcciones), sin parámetros de entrada.

– Para la operación obtener los datos de la acción formativa identificada en la petición (obtenerAccion), el identificador de dicha acción:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8638.png)

– Para la operación eliminar una acción formativa identificada en la petición. (eliminarAccion), el identificador de dicha acción:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8685.png)

El mensaje de respuesta correspondiente a cada una de las operaciones del servicio de seguimiento repetirá el mensaje de entrada, añadiéndole una etiqueta <codigoRetorno> para indicar como se ha realizado la operación, así como los datos de seguimiento solicitados en la petición.

El código de retorno adopta los valores y significados que se especifican en la tabla siguiente:

| CódigoRetorno | crearCentro | obtenerDatosCentro | Crear Acción | obtenerListaAcciones | obtenerAccion | eliminarAccion |
| --- | --- | --- | --- | --- | --- | --- |
| -2 | WS no disponible | WS no disponible | WS no disponible | WS no disponible | WS no disponible | WS no disponible |
| -1 | Error inesperado | Error inesperado | Error inesperado | Error inesperado | Error inesperado | Error inesperado |
| 0 | Correcto | Correcto | Correcto | Correcto | Correcto | Correcto |
| 1 | Centro con acciones | – | Acción existente | Acción inexistente | Acción inexistente | Acción inexistente |
| 2 | Error en parámetro | – | Error en parámetro | – | Error en parámetro | Error en parámetro |

El código de retorno 2 (error en parámetro) se devolverá cuando se produzca un error debido al formato o a la ausencia de alguna etiqueta en el mensaje de entrada. ETIQUETA_ERROR tomará el valor de la etiqueta del elemento que haya provocado el error. De manera equivalente, el código de retorno -1 (error inesperado) podrá usar ETIQUETA_ERROR para indicar el tipo de error detectado. El código de retorno -2 (WS no disponible) se devolverá cuando por algún motivo controlado no se pueda atender a las peticiones de los servicios públicos de empleo del Sistema Nacional de Empleo.

Los datos de seguimiento que, junto con la etiqueta <codigoRetorno>, han de devolverse en el mensaje de respuesta de cada una de las operaciones son los siguientes:

– Para la operación crear el centro de formación (crearCentro):

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8817.png)

– Para la operación obtener los datos identificativos del centro de formación (obtenerDatosCentro):

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_8865.png)

– Para la operación crear una acción formativa con su identificador (crearAccion):

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_9014.png)

– Para la operación obtener lista de identificaciones de las acciones formativas iniciadas en el centro o entidad de formación (obtenerListaAcciones):

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_9062.png)

– Para la operación obtener los datos de la acción formativa identificada en la petición (obtenerAccion):

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_9104.png)

– Para la operación eliminar los datos de la acción formativa identificada en la petición (eliminarAccion), no devuelve parámetros de salida.

Una vez que a la entidad de formación acreditada o inscrita se le asigne el correspondiente código de centro para su inclusión en el Registro de Estatal de Entidades de formación, la Administración Pública competente invocará al servicio web de seguimiento, facilitando todos los datos de identificación que el citado centro de formación hizo constar en su solicitud de acreditación o declaración responsable de inscripción, así como el código de centro asignado. Esta es la situación inicial del servicio web de seguimiento, por lo que la entidad de formación habrá de eliminar cualquier acción formativa de prueba creada en el proceso de acreditación o inscripción.

El seguimiento de cada acción formativa se realizará desde la fecha de inicio prevista en la solicitud de autorización para el desarrollo de las acciones formativas, hasta treinta días naturales después de la fecha de finalización prevista para dicha acción.

Durante este período, la información sobre cada acción formativa debe estar disponible para su obtención por la administración laboral competente, pudiéndose eliminar únicamente cuando el período de seguimiento antes señalado haya concluido.

El seguimiento se llevará a cabo con la siguiente periodicidad:

a) Al comienzo de la acción formativa, una vez que se haya producido la comunicación de inicio de la misma.

b) Durante el desarrollo de cada acción formativa, con la periodicidad que determine la administración laboral competente.

c) Después de la finalización de la acción formativa, durante los 90 días naturales siguientes a que la misma tenga lugar, al objeto de obtener los resultados alcanzados.

Una vez que la Administración Pública competente obtenga los primeros datos de seguimiento sobre la actividad formativa de una entidad de formación concreta, la sucesiva información de esta naturaleza que se obtenga eliminará y sustituirá a la registrada la vez anterior, a fin de evitar datos erróneos, inexactos o duplicados.

Los códigos de centros de formación y de especialidades formativas utilizados en el seguimiento se refieren a centros y especialidades mantenidos en el Registro Estatal de Entidades de Formación y en el Catálogo de Especialidades Formativas y, por lo tanto, su origen se codificará siempre con el valor que corresponda al servicio público de empleo del Sistema Nacional de Empleo.

Las fechas obligatorias de inicio y fin que deben reportarse en el seguimiento se consignarán con carácter de previsión cuando aún no hayan ocurrido, pero deberán registrarse de forma exacta (fecha real) si ya han transcurrido.

Los datos de seguimiento sobre las acciones formativas iniciadas en la entidad de formación se estructuran en dos ámbitos:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/78/04716_9147.png)

La entidad de formación deberá tener siempre informados los datos identificativos de la entidad de formación, mientras que habrá de tener informados los elementos de la acción formativa en función de su situación:

a) En el momento de la autorización de la acción formativa y cuando como resultado de la misma la Administración Pública competente le asigne un código de identificación, solicitará al servicio web de la entidad de formación su creación con los datos aportados en la solicitud de autorización:

– Datos identificativos y descripción.

– Especialidades de la acción formativa:

• Centros de sesiones presenciales.

b) Desde el momento en que se realice la comunicación de inicio de la acción formativa:

– Especialidades de la acción formativa:

• Tutores-formadores.

• Datos de uso.

• Participantes.

– Especialidad del participante.

c) Con el avance de la acción formativa, si procede:

– Participantes.

– Especialidad del participante:

• Tutorías presenciales.

• Evaluación final.

• Resultados.

Una vez transcurridos 90 días naturales desde la fecha de finalización de la acción formativa, la entidad de formación podrá considerar, si así lo estima, que dicha acción no está ya sujeta a seguimiento.

B. Seguimiento en base a visita virtual

Para realizar las visitas técnicas de seguimiento de carácter virtual será preceptivo proporcionar a cada Administración Pública competente una dirección de acceso a la plataforma, así como sus correspondientes credenciales (usuario/contraseña), con permiso de administrador, pero sin posibilidad de modificar datos.

Durante las visitas virtuales se deberá tener acceso a los informes de seguimiento que genere la plataforma de teleformación. Tales informes deben poseer estas características:

a) Han de generarse automáticamente.

b) Deben realizarse por alumno, por curso (grupo de alumnos), en el caso de las acciones formativas de certificado de profesionalidad, por módulo/s y, en su caso, unidad/es formativa/s y por los intervalos de fechas que se requieran, coincidiendo con el inicio, el desarrollo y el final de cada acción formativa.

c) Tienen que referirse a todas las áreas y servicios de la acción formativa.

d) Deben suministrar información sobre totales, medias y porcentajes.

e) Tienen que poder imprimirse y exportarse a formato CSV o XML.

f) Dependiendo de su tipo, han de ser accesibles a cada alumno, a los tutores-formadores y a la Administración Pública competente, que a través de los mismos llevará a cabo el seguimiento y control de las acciones formativas impartidas.

g) Tienen que proporcionar datos resultantes de la monitorización y traza de las actividades llevadas a cabo por el alumnado durante la formación, concretándose, como mínimo, en un registro y en un informe estadístico y gráfico de la actividad desarrollada a través de la plataforma durante el proceso formativo tanto por cada participante, como el grupo de participantes en la acción formativa, en lo que se refiere a:

– Acceso a la plataforma o a sus diferentes partes (número y porcentaje), registrando tanto la asistencia (áreas o servicios visitados y fechas y horas en las que se visitaron) como la participación del alumnado (aportaciones o intervenciones realizadas mediante las herramientas de comunicación y colaboración, mensajes enviados), y controlando los tiempos invertidos.

– Actividades de aprendizaje realizadas en cada módulo/unidad formativa (cuando proceda) y en la acción formativa en su conjunto.

– Tiempo medio invertido en la realización de cada módulo/unidad formativa (cuando proceda) y de la acción formativa en su conjunto.

– Resultados obtenidos en todos los trabajos, actividades y pruebas de evaluación (on line y, en su caso, presenciales) realizadas durante el desarrollo de la acción formativa (clasificados por módulos y unidades formativas, cuando así proceda) y puntuación media alcanzada en las mismas.

– Resultados obtenidos en las pruebas de evaluación final de módulo formativo y, en su caso unidades formativas, así como en la especialidad formativa, número y porcentaje de alumnos que las han superado y puntuación obtenida.

– Para los casos en los que se supere la prueba final de evaluación del módulo formativo (puntuación mínima de 5), puntuación final de módulos formativos (resultante de sumar la puntuación media obtenida en la evaluación durante el proceso de aprendizaje, y la puntuación obtenida en la prueba de evaluación final del módulo, ponderándolas previamente con un peso de 30% y 70% respectivamente), con indicación de la convocatoria (primera o segunda) en que la puntuación final se haya obtenido.

– Número y porcentaje de alumnos que superen cada uno de los módulos que integran la acción formativa, así como número y porcentaje de alumnos que superen la totalidad de los módulos que configuran cada acción formativa.

– Número y porcentaje de alumnos que superen el módulo de formación práctica en centros de trabajo.

h) Deben facilitar, como mínimo, los siguientes datos sobre el alumnado participante, los tutores formadores y las acciones formativas impartidas:

– Perfil del alumnado (sexo; edad; nivel formativo; situación laboral; provincia/Comunidad Autónoma de residencia/trabajo; medio de conocimiento de la acción formativa; experiencia anterior en la realización de cursos on line; razones por las que se elige un curso en modalidad de teleformación; valoración general sobre la modalidad. Y para el caso de alumnado ocupado, categoría profesional, tamaño de su empresa, horario de la acción formativa).

– Altas, modificaciones y bajas del alumnado por módulo y acción formativa y fechas en las que se produjeron.

– Número y porcentaje de alumnos de inician, que completan y que abandonan cada módulo/acción formativa, con clasificación de las causas/motivos de la baja.

– Perfil de tutores-formadores de las acciones formativas impartidas (sexo, edad, nivel formativo, tiempo de experiencia profesional como docente, tiempo de experiencia profesional como docente de formación on line, tiempo de experiencia profesional en el ámbito de la unidad de competencia que imparte, competencia docente, situación contractual con el centro de formación –personal de plantilla o contratado para la impartición–).

– Identificación de las acciones formativas desarrolladas: número por Familia/Área Profesional y por nivel de cualificación, por Comunidad Autónoma y fechas de realización; número de módulos formativos impartidos por certificado de profesionalidad, por Familia/Área Profesional y por nivel de cualificación; número de unidades formativas impartidas por módulo formativo, por certificado de profesionalidad y por Familia/Área Profesional.
