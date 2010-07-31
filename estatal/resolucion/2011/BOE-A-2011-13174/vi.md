## VI. Funciones y requisitos del sistema de intercambio

El sistema de intercambio utilizado para emisión y recepción de los mensajes definidos en los apartados anteriores funciona, en el espacio de intercambio SICRES, como elemento responsable de:

i. Centralizar el registro de operaciones de intercambio y garantizar la trazabilidad de las mismas.

ii. Gestionar la situación temporal de los «pre-asientos registrales».

iii. Proporcionar la seguridad en el transporte de la información a través de mecanismos de encriptación en el mensaje de datos de intercambio.

iv. Firma electrónica del mensaje de datos de intercambio.

Como ya se ha indicado, esta norma no establece los requisitos tecnológicos concretos que deben proporcionar el sistema que da soporte a un intercambio de asientos registrales, ya que SICRES 3.0 es independiente de la tecnología o plataforma sobre la que se realice la transmisión de los elementos que forman el intercambio propiamente dicho.

No obstante, sí se establecen unos principios básicos que deben ser cubiertos por el sistema de intercambio que se utilice, como son:

i. Integridad: Garantía de que la información no es modificada en los procesos de intercambio.

ii. Confidencialidad: Disponibilidad de la información solamente para usuarios autorizados.

iii. Autenticidad: Legitimidad del origen de la información.

iv. No repudio: Imposibilidad de negación ante terceros del envío y/o recepción por parte del emisor y/o receptor de la información.

v. Accesibilidad: Posibilidad de acceso eficiente solo para entidades autorizadas.

A continuación se desarrollan estos requisitos de seguridad y, posteriormente, las funciones que debe proporcionar el sistema de intercambio.

VI.1. Requisitos de seguridad

1. Autenticación de los sistemas implicados.

Además de la implementación de las políticas de seguridad para los usuarios de la plataforma de intercambio, se asegura la identidad de cada uno de los sistemas intervinientes en el espacio de intercambio.

Así, todos los sistemas que participen en el proceso de intercambio, incluidos los sistemas de las Entidades Registrales de Origen y destino, están correctamente identificados y validados en el espacio de intercambio.

2. Integridad.

La plataforma de intercambio proporciona los mecanismos necesarios, a fin de garantizar que el contenido completo de los mensajes de datos intercambiados permanezca inalterado durante el proceso de intercambio.

Este punto se asegura a través del protocolo de transporte de mensajes entre las Entidades Registrales de Origen y destino que utilice el sistema de intercambio, y la tecnología de transmisión de datos.

3. Garantía de no repudio.

La plataforma de intercambio provee de los mecanismos necesarios para garantizar el no repudio del mensaje de datos de intercambio.

VI.2 Gestión del proceso de intercambio

Como ya se ha mencionado, para iniciar el intercambio, la aplicación de registro de la Entidad Registral Origen genera el mensaje de datos de intercambio de forma completa y lo envía al sistema de gestión de intercambio.

La plataforma de intercambio es responsable de verificar la validez del mensaje de datos de intercambio según el formato establecido en esta norma.

Además, el sistema de gestión de intercambio es el encargado de garantizar la transmisión entre los sistemas de la Entidad Registral Origen y destino.

Posteriormente, la aplicación de registro de la Entidad Registral destino es la responsable de interpretar de forma correcta el fichero intercambiado.

Hasta que el intercambio concluye, la plataforma de intercambio tiene la misión de resolver de forma correcta la situación temporal del «pre-asiento registral» que desaparece cuando se produce la recepción completa de todos los ficheros que pudieran constituir un envío.

Dentro de cada espacio de intercambio debe definirse un conjunto de reglas que permitan la gestión del intercambio entre Entidades Registrales a través de un sistema de intercambio. Estas reglas permiten definir los mecanismos y herramientas para realizar el intercambio en condiciones adecuadas incluyendo:

i. La tecnología de comunicación entre los distintos agentes del intercambio.

ii. Los mecanismos y procedimientos específicos para el envío y recepción de ficheros, incluyendo mecanismos para fraccionamiento de ficheros (en su caso) y para garantizar la integridad y seguridad de los envíos.

iii. Las políticas específicas de protección de datos que deben ser de aplicación.

iv. Los mecanismos de trazabilidad de los intercambios y la información que se registre sobre los mismos.

v. Procedimientos detallados de gestión de errores y excepciones.

1. Gestión de envíos de mensajes y anexos.

La plataforma de intercambio debe realizar una gestión adecuada del envío de mensajes y los posibles documentos anexos asociados, que garantice la correcta identificación del registro completo en la Entidad Registral de destino y su posterior almacenamiento.

Para la generación del mensaje de datos de intercambio, o los ficheros anexos, cuando excedan determinados límites de tamaño, la plataforma de intercambio podrá incorporar mecanismos que permitan el envío de los anexos asociados de forma fraccionada.

En estos casos, las Entidades Registrales de Origen deben ser capaces de fragmentar el fichero anexo en tantos fragmentos como sea necesario. De igual manera, las Entidades Registrales de destino tienen que ser capaces de construir los fragmentos recibidos, ordenarlos y reconstruir el fichero anexo original.

2. Gestión del flujo.

Las operaciones de intercambio tienen definido un estado (definidos en el apartado V de la presente norma) en el que se indica la fase lógica dentro del proceso de intercambio en la que se encuentra el fichero, y los posibles eventos que pueden ocurrir.

3. Evitar duplicados.

El sistema de gestión de intercambio contiene los mecanismos necesarios para garantizar que los ficheros que se envíen o reciban por duplicado de manera errónea, sean identificados como tales.

Las Entidades Registrales deben implementar mecanismos y procedimientos que eviten la duplicación de asientos en caso de que se reciban varias veces, utilizando los datos «Identificador de Intercambio», «Identificador de Fichero» y «Número de Secuencia».

4. Gestión de mensajes.

El sistema de intercambio dispone de funcionalidades de gestión de mensajes de actividad, a fin de proporcionar información de seguimiento a la Entidad Registral de Origen, una vez realizado el intercambio, tal y como se describe en el apartado V.

La gestión y conservación de los anexos, entendidos estos como documentos electrónicos, se definen y normalizan en la NTI de Política de gestión de documentos electrónicos.

5. Conservación de la información del asiento registral.

Cuando los pre-asientos registrales intercambiados no se convierten en asientos firmes en la Entidad Registral de destino, esta no debe conservar el mensaje de datos de intercambio ni sus documentos adjuntos. Únicamente debe conservar traza de la transacción de intercambio realizada.

VI.3. Soporte del modo de prueba

El sistema de gestión de intercambio debe disponer de la capacidad de soportar el modo de prueba en el proceso de intercambio, de tal forma que permita realizar pruebas de intercambio.

El modelo de datos incluye un identificador para mensajes de datos de intercambio que indica que son una prueba que aparece detallado en los apartados IV.2 y IV.3.

VI.4. Directorio Común

El sistema de gestión de intercambio debe utilizar el Directorio Común que, establecido según lo dispuesto en el artículo 9 del R.D. 4/2010, de 8 de enero, y gestionado por el Ministerio de Política Territorial y Administración Pública (MPTAP), incluye la codificación de todos los Organismos, Entidades Registrales y Unidades de Gestión susceptibles de participar en el proceso de intercambio, proporcionando códigos únicos dentro del espacio de intercambio correspondiente.

VI.5. Control y gestión de errores

La plataforma de intercambio es responsable de realizar una gestión adecuada de los errores y excepciones que puedan ocurrir durante el proceso de intercambio, que facilite la restauración de información en la medida de lo posible.

1. Tipología de errores de intercambio.

Los principales errores que pueden ocurrir durante el intercambio registral pueden clasificarse, en base a la naturaleza del error, como:

i. Errores lógicos: relativos a errores en las validaciones en estructura y/o en contenido de los ficheros de intercambio y/o en direcciones de origen o destino. En definitiva, cualquier error no achacable a un problema tecnológico, pero que provoca que el resultado del intercambio no sea exitoso.

ii. Errores físicos: relativos a errores que se pueden asociar con la tecnología que interviene en el proceso de intercambio, como la no disponibilidad de máquinas, de elementos de la infraestructura de software, excepciones de código no controladas y otros.

iii. Errores de transmisión de datos: relativos a errores que pueden ocurrir durante la transmisión de datos debido a problemas en las comunicaciones.

La codificación de los errores aparece en el apartado VII.4.

Tabla 9. Descripción de errores de intercambio

| Tipo de error | Definición |
| --- | --- |
| Errores lógicos. | Errores de validación de los datos de intercambio. | Ocurren al resultar erróneas las validaciones lógicas de los datos del intercambio en formatos, datos requeridos y correspondencia entre descripciones de contenido y el contenido de los datos de intercambio. |
| Errores de direccionamiento. | Ocurren cuando la identidad del remitente o destinatario reflejada en el mensaje de datos de intercambio no se corresponde con el que debería enviar o recibir la información. |
| Errores en las reglas de intercambio. | Aparece un evento no esperado durante el intercambio registral. |
| Errores de ciclo de envío no completado. | No se puede completar el ciclo de envío completamente. |
| Errores físicos. | Se producen cuando ocurren errores, hardware o software, en alguno de los sistemas intervinientes. |
| Errores de transmisión de datos. | No se puede producir el intercambio, debido a que el sistema de destino o el de origen no están disponibles. |

2. Errores lógicos

Descripción de los errores lógicos.

i. Errores de validación de los datos de intercambio. Ocurren al resultar erróneas las validaciones lógicas de los datos del intercambio en formatos, datos requeridos y correspondencia entre descripciones de contenido y el contenido de los datos de intercambio.

ii. Errores de direccionamiento. Ocurren cuando la identidad del remitente o destinatario reflejada en el mensaje de datos de intercambio no se corresponde con el que debería enviar o recibir la información.

iii. Errores en las reglas de intercambio. Aparece un evento no esperado durante el intercambio registral.

iv. Errores de ciclo de envío no completado. No se puede completar el ciclo de envío completamente.

Tratamiento de los errores lógicos.

i. Errores de validación de los datos de intercambio. En el momento que se detecte esta falta de integridad en los datos de intercambio, se deberá interrumpir el proceso marcando como erróneo el mensaje de datos de intercambio. A continuación se deberá notificar al Origen de que no se ha podido interpretar correctamente los datos, informándole del código de error lógico ocurrido.

Una vez notificado, la Entidad Registral de Origen se dispondrá a analizar la naturaleza del error para realizar acciones de subsanación:

1. Si es relativo a una composición errónea del mensaje de datos de intercambio y anexos asociados, deberá recomponerlos y retransmitirlos.

2. Si el error es debido a una corrupción de datos durante la transmisión deberá simplemente retransmitirlos.

La operación deberá ser registrada como errónea en el log de operaciones del sistema de gestión del intercambio.

ii. Errores de direccionamiento. Se pueden producir por errores en la dirección del remitente o en el destinatario.

Si se produce un error en los datos del destinatario, es posible que sucedan dos escenarios:

1. Los datos llegan a una Entidad Registral de destino no esperada. En este caso, la Entidad destino deberá rechazar el registro recibido y notificar a la Entidad Origen de la ocurrencia de este suceso a través del sistema de gestión de intercambio.

2. Los datos llegan a un destino no esperado fuera del espacio de intercambio registral, es decir, no es enviado a una Entidad Registral. El error se podrá identificar por un aviso de error de direccionamiento proporcionado por el sistema de gestión de intercambio (por ejemplo «destino inalcanzable»), o al no recibirse la confirmación de la entrega pasado un tiempo preestablecido por parte de la Entidad Registral de Origen.

El tratamiento de estos errores se llevaría a cabo a través de la realización retransmisiones desde el sistema de intercambio o desde la Entidad Registral Origen, una vez solucionado el error de direcciones.

Si se produce un error en los datos del remitente, es posible que sucedan dos escenarios:

1. Se recibe una confirmación de entrega en una Entidad Registral de Origen no esperada. En este caso, la Entidad Origen deberá rechazar la confirmación.

2. La confirmación de entrega es enviada a una dirección fuera del espacio de nombres del intercambio registral. En este caso el error se detectará si la entidad Origen no recibe la confirmación de la entrega en un tiempo preestablecido o si al enviar la confirmación se produce un aviso de error de direccionamiento, por ejemplo «destino inalcanzable».

Para tratar los errores de destinatario se intentarán retransmisiones desde el sistema de intercambio o desde la Entidad Registral destino, una vez solucionado el error de direcciones.

Los errores de direcciones pueden estar motivados por entradas erróneas en el Directorio Común. En estos casos, se debe detectar (normalmente al aparecer errores de direccionamiento) y realizar la corrección de la entrada incorrecta.

Las operaciones anteriormente indicadas deberán ser registradas como erróneas en el log de operaciones del sistema de gestión de intercambio.

iii. Errores en las reglas de intercambio. Este error ocurrirá si aparece un evento no esperado durante el intercambio registral (por ejemplo, se recibe un segundo mensaje de control de confirmación de entrega correcta para un mismo Identificador de Intercambio).

En este caso, el sistema de gestión de intercambio se vuelve inconsistente, por lo que se deberá registrar el elemento que ha producido el evento, y realizar una notificación para solucionar el problema.

iv. Errores de ciclo de envío no completado. Este error ocurrirá si no se hubiera podido cerrar el ciclo de envío completo, al interrumpirse en alguno de sus pasos. Se detecta al sobrepasarse los límites de tiempo esperados para que un paso del ciclo se realice.

El Origen de este error puede ser variado, debido tanto a problemas lógicos como físicos. El tratamiento normal para estos casos es la retransmisión de los datos.

La operación errónea deberá ser registrada en el log del sistema de gestión de intercambio, indicando los reintentos efectuados y si fueron exitosos o no. Si al efectuar el número de reintentos determinado no se consiguiera cerrar el ciclo, el conjunto de datos objeto del error deberá ser marcado como erróneo notificando al sistema de intercambio la necesidad de un tratamiento para su subsanación.

3. Errores físicos.

Descripción de los errores físicos:

Se producen cuando ocurren errores, hardware o software, en alguno de los sistemas intervinientes.

Tratamiento de los errores físicos:

Los errores en el sistema de intercambio deben ser tratados según los procedimientos de operación que apliquen en cada caso.

Las operaciones de intercambio que se viesen afectadas por el error ocurrido se identificarán y restaurarán en la medida de lo posible.

4. Errores de transmisión.

Descripción de los errores de transmisión:

No se puede producir el intercambio, debido a que el sistema de destino o el de Origen no están disponibles.

Tratamiento de los errores de transmisión:

Si alguno de los sistemas no está disponible, el tratamiento normal será la realización de reintentos de envío.

La operación errónea deberá ser registrada en el log del sistema de gestión de intercambio, indicando los reintentos efectuados y si fueron exitosos o no. Si al efectuar el número de reintentos establecidos no se consiguiera cerrar el ciclo, el conjunto de datos objeto del error deberá ser marcado como erróneo notificando al sistema de gestión de intercambio de la necesidad de un tratamiento para su subsanación.

VI.6 Comunicación entre distintos sistemas de intercambio

Para un intercambio de asientos registrales es posibles que dos o más sistemas distintos se comuniquen entre sí. En ese caso, es necesario definir un conjunto de reglas específicas que apliquen al intercambio entre sistemas, independientemente de aquellas que se hayan definido para el intercambio interno en cada una de ellas.

En la siguiente figura se puede ver un caso de ejemplo de esta situación:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_013.png)

VI.7 Otras recomendaciones

Existen otros requerimientos de tecnología que pueden ser considerados como recomendaciones.

1. Registro de la actividad de intercambio.

Se recomienda, que el estado y la secuencia de las operaciones de intercambio se registren en un sistema centralizado del sistema de intercambio, que permita realizar la trazabilidad de las operaciones efectuadas.

Las aplicaciones de registro de las Entidades Registrales implicadas en un proceso de intercambio, podrán hacer uso de los datos de trazabilidad para proporcionar un servicio de seguimiento a los ciudadanos e instituciones que lo soliciten.

2. Persistencia en errores y excepciones.

Los datos del mensaje de datos de intercambio y el estado de sus operaciones a través del sistema de gestión de intercambio, deberían permanecer en un medio persistente cuando se produzcan errores o excepciones que impidan su envío/recepción. Se garantizará la perdurabilidad de registro y su estado, si ocurrieran errores en el proceso de intercambio.

3. Compatibilidad con SICRES 2.0.

Es recomendable que la plataforma de intercambio posibilite la realización de transformaciones del formato SICRES 3.0 a SICRES 2.0 (y viceversa).
