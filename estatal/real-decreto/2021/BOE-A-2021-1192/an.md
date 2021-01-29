## ANEXO

## Instrucción nacional de notificación y gestión de ciberincidentes

1. Obligatoriedad de notificación

Los incidentes se asociarán a uno de los niveles de peligrosidad e impacto establecidos en esta instrucción, teniendo en cuenta la obligatoriedad de notificación de todos aquellos que se categoricen con un nivel CRÍTICO, MUY ALTO o ALTO para todos aquellos sujetos obligados a los que les sea aplicable esta «Instrucción nacional de notificación y gestión de ciberincidentes». En ese caso, los sujetos obligados deberán comunicar, en tiempo y forma, los incidentes que registren en sus redes y sistemas de información y que estén obligados a notificar por superar los umbrales de impacto o peligrosidad establecidos en esta instrucción.

Para la notificación de los incidentes de ciberseguridad se utilizará como criterio de referencia el nivel de peligrosidad que se asigne a un incidente, sin perjuicio de que a lo largo del desarrollo, mitigación o resolución del mismo, se categorice con un determinado nivel de impacto que haga aconsejable la comunicación del incidente a la autoridad competente o CSIRT de referencia.

En todo caso, cuando un determinado suceso pueda asociarse a más de un tipo de incidente debido a sus características potenciales, este se asociará a aquel que tenga un nivel de peligrosidad superior de acuerdo a los criterios expuestos en esta Instrucción.

2. Clasificación/taxonomía de los ciberincidentes

La siguiente Clasificación/Taxonomía de los ciberincidentes está alineada con la taxonomía aprobada por la Agencia de la Unión Europea para la Ciberseguridad (ENISA).

Esta Clasificación/Taxonomía de los ciberincidentes se empleará para la asignación de una clasificación específica a un incidente registrado en las redes y sistemas de información cuando se realice la comunicación a la autoridad competente o CSIRT de referencia.

Tabla 1. Clasificación/Taxonomía de los ciberincidentes

| Clasificación | Tipo de incidente | Descripción y ejemplos prácticos |
| --- | --- | --- |
| Contenido abusivo. | Spam. | Correo electrónico masivo no solicitado. El receptor del contenido no ha otorgado autorización válida para recibir un mensaje colectivo. |
| Delitos de odio, contra la libertad o el honor. | Contenido difamatorio o discriminatorio. Ej.: ciberacoso, racismo, amenazas a una persona o dirigidas contra colectivos. |
| Pornografía infantil, contenido sexual o violento inadecuado. | Material que represente de manera visual contenido relacionado con pornografía infantil, apología de la violencia, etc. |
| Contenido dañino. | Sistema infectado. | Sistema infectado con malware. Ej.: sistema, computadora o teléfono móvil infectado con un rootkit. |
| Servidor C&C (Mando y Control). | Conexión con servidor de Mando y Control (C&C) mediante malware o sistemas infectados. |
| Distribución de malware. | Recurso usado para distribución de malware. Ej.: recurso de una organización empleado para distribuir malware. |
| Configuración de malware. | Recurso que aloje ficheros de configuración de malware Ej.: ataque de webinjects para troyano. |
| Obtención de información. | Escaneo de redes (scanning). | Envío de peticiones a un sistema para descubrir posibles debilidades. Se incluyen también procesos de comprobación o testeo para recopilar información de alojamientos, servicios y cuentas. Ej.: peticiones DNS, ICMP, SMTP, escaneo de puertos. |
| Análisis de paquetes (sniffing). | Observación y grabación del tráfico de redes. |
| Ingeniería social. | Recopilación de información personal sin el uso de la tecnología. Ej.: mentiras, trucos, sobornos, amenazas. |
| Intento de intrusión. | Explotación de vulnerabilidades conocidas. | Intento de compromiso de un sistema o de interrupción de un servicio mediante la explotación de vulnerabilidades con un identificador estandarizado (véase CVE). Ej.: desbordamiento de buffer, puertas traseras, cross site scripting (XSS). |
| Intento de acceso con vulneración de credenciales. | Múltiples intentos de vulnerar credenciales. Ej.: intentos de ruptura de contraseñas, ataque por fuerza bruta. |
| Ataque desconocido. | Ataque empleando exploit desconocido. |
| Intrusión. | Compromiso de cuenta con privilegios. | Compromiso de un sistema en el que el atacante ha adquirido privilegios. |
| Compromiso de cuenta sin privilegios. | Compromiso de un sistema empleando cuentas sin privilegios. |
| Compromiso de aplicaciones. | Compromiso de una aplicación mediante la explotación de vulnerabilidades de software. Ej.: inyección SQL. |
| Robo. | Intrusión física. Ej.: acceso no autorizado a Centro de Proceso de Datos. |
| Disponibilidad. | DoS (Denegación de servicio). | Ataque de denegación de servicio. Ej.: envío de peticiones a una aplicación web que provoca la interrupción o ralentización en la prestación del servicio. |
| DDoS (Denegación distribuida de servicio). | Ataque de denegación distribuida de servicio. Ej.: inundación de paquetes SYN, ataques de reflexión y amplificación utilizando servicios basados en UDP. |
| Mala configuración. | Configuración incorrecta del software que provoca problemas de disponibilidad en el servicio. Ej.: Servidor DNS con el KSK de la zona raíz de DNSSEC obsoleto. |
| Sabotaje. | Sabotaje físico. Ej.: cortes de cableados de equipos o incendios provocados. |
| Interrupciones. | Interrupciones por causas ajenas. Ej.: desastre natural. |
| Compromiso de la información. | Acceso no autorizado a información. | Acceso no autorizado a información. Ej.: robo de credenciales de acceso mediante interceptación de tráfico o mediante el acceso a documentos físicos. |
| Modificación no autorizada de información. | Modificación no autorizada de información. Ej.: modificación por un atacante empleando credenciales sustraídas de un sistema o aplicación o encriptado de datos mediante ransomware. |
| Pérdida de datos. | Pérdida de información Ej.: pérdida por fallo de disco duro o robo físico. |
| Fraude. | Uso no autorizado de recursos. | Uso de recursos para propósitos inadecuados, incluyendo acciones con ánimo de lucro. Ej.: uso de correo electrónico para participar en estafas piramidales. |
| Derechos de autor. | Ofrecimiento o instalación de software carente de licencia u otro material protegido por derechos de autor. Ej.: Warez. |
| Suplantación. | Tipo de ataque en el que una entidad suplanta a otra para obtener beneficios ilegítimos. |
| Phishing. | Suplantación de otra entidad con la finalidad de convencer al usuario para que revele sus credenciales privadas. |
| Vulnerabilidad. | Criptografía débil. | Servicios accesibles públicamente que puedan presentar criptografía débil. Ej.: servidores web susceptibles de ataques POODLE/FREAK. |
| Amplificador DDoS. | Servicios accesibles públicamente que puedan ser empleados para la reflexión o amplificación de ataques DDoS. Ej.: DNS open-resolvers o Servidores NTP con monitorización monlist. |
| Servicios con acceso potencial no deseado. | Ej.: Telnet, RDP o VNC. |
| Revelación de información. | Acceso público a servicios en los que potencialmente pueda relevarse información sensible. Ej.: SNMP o Redis. |
| Sistema vulnerable. | Sistema vulnerable. Ej.: mala configuración de proxy en cliente (WPAD), versiones desfasadas de sistema. |
| Otros. | Otros. | Todo aquel incidente que no tenga cabida en ninguna categoría anterior. |
| APT. | Ataques dirigidos contra organizaciones concretas, sustentados en mecanismos muy sofisticados de ocultación, anonimato y persistencia. Esta amenaza habitualmente emplea técnicas de ingeniería social para conseguir sus objetivos junto con el uso de procedimientos de ataque conocidos o genuinos. |

3. Nivel de peligrosidad del ciberincidente

El indicador de peligrosidad determina la potencial amenaza que supondría la materialización de un incidente en los sistemas de información o comunicación del ente afectado, así como para los servicios prestados o la continuidad de negocio en caso de haberla. Este indicador se fundamenta en las características intrínsecas a la tipología de amenaza y su comportamiento.

Los incidentes se asociarán a alguno de los siguientes niveles de peligrosidad: CRÍTICO, MUY ALTO, ALTO, MEDIO, BAJO.

Nivel crítico:

– APT.

Nivel muy alto:

– Distribución de malware.

– Configuración de malware.

– Robo.

– Sabotaje.

– Interrupciones.

Nivel alto:

– Pornografía infantil, contenido sexual o violento inadecuado.

– Sistema infectado.

– Servidor C&C (Mando y Control).

– Compromiso de aplicaciones.

– Compromiso de cuentas con privilegios.

– Ataque desconocido.

– DoS (Denegación de servicio).

– DDoS (Denegación distribuida de servicio).

– Acceso no autorizado a información.

– Modificación no autorizada de información.

– Pérdida de datos.

– Phishing.

Nivel medio:

– Discurso de odio.

– Ingeniería social.

– Explotación de vulnerabilidades conocidas.

– Intento de acceso con vulneración de credenciales.

– Compromiso de cuentas sin privilegios.

– Desconfiguración.

– Uso no autorizado de recursos.

– Derechos de autor.

– Suplantación.

– Criptografía débil.

– Amplificador DDoS.

– Servicios con acceso potencial no deseado.

– Revelación de información.

– Sistema vulnerable.

Nivel bajo:

– Spam.

– Escaneo de redes (scanning).

– Análisis de paquetes (sniffing).

– Otros.

4. Nivel de impacto del ciberincidente

El indicador de impacto de un ciberincidente se determinará evaluando las consecuencias que tal ciberincidente ha tenido en las funciones y actividades de la organización afectada, en sus activos o en los individuos afectados. De acuerdo a ello, se tienen en cuenta aspectos como las consecuencias potenciales o materializadas que provoca una determinada amenaza en un sistema de información y/o comunicación, así como en la propia entidad afectada (organismos públicos o privados, y particulares).

Los criterios empleados para la determinación del nivel de impacto asociado a un ciberincidente atienden a los siguientes parámetros:

– Impacto en la Seguridad Nacional o en la seguridad ciudadana.

– Efectos en la prestación de un servicio esencial o en una infraestructura crítica.

– Tipología de la información o sistemas afectados.

– Grado de afectación a las instalaciones de la organización.

– Posible interrupción en la prestación del servicio normal de la organización.

– Tiempo y costes propios y ajenos hasta la recuperación del normal funcionamiento de las instalaciones.

– Pérdidas económicas.

– Extensión geográfica afectada.

– Daños reputacionales asociados.

Los incidentes se asociarán a alguno de los siguientes niveles de impacto: CRÍTICO, MUY ALTO, ALTO, MEDIO, BAJO, SIN IMPACTO.

Nivel crítico:

– Afecta apreciablemente a la Seguridad Nacional.

– Afecta a la seguridad ciudadana, con potencial peligro para la vida de las personas.

– Afecta a una infraestructura crítica.

– Afecta a sistemas clasificados SECRETO.

– Afecta a más del 90 % de los sistemas de la organización.

– Interrupción en la prestación del servicio superior a 24 horas y superior al 50 % de los usuarios.

– El ciberincidente precisa para resolverse más de 100 Jornadas-Persona.

– Impacto económico superior al 0,1 % del Producto Interior Bruto (PIB) actual.

– Extensión geográfica supranacional.

– Daños reputacionales muy elevados y cobertura continua en medios de comunicación internacionales.

Nivel muy alto:

– Afecta a la seguridad ciudadana con potencial peligro para bienes materiales.

– Afecta apreciablemente a actividades oficiales o misiones en el extranjero.

– Afecta a un servicio esencial.

– Afecta a sistemas clasificados RESERVADO.

– Afecta a más del 75 % de los sistemas de la organización.

– Interrupción en la prestación del servicio superior a 8 horas y superior al 35 % de los usuarios.

– El ciberincidente precisa para resolverse entre 30 y 100 Jornadas-Persona.

– Impacto económico entre el 0,07 % y el 0,1 % del PIB actual.

– Extensión geográfica superior a 4 Comunidades Autónomas (CC.AA.) o un territorio de Interés Singular (TIS, se considera como tal a las ciudades de Ceuta y Melilla y a cada una de las islas que forman los archipiélagos de las islas Baleares y las islas Canarias).

– Daños reputacionales a la imagen del país (marca España).

– Daños reputacionales elevados y cobertura continua en medios de comunicación nacionales.

Nivel alto:

– Afecta a más del 50 % de los sistemas de la organización.

– Interrupción en la prestación del servicio superior a 1 hora y superior al 10 % de usuarios.

– El ciberincidente precisa para resolverse entre 5 y 30 Jornadas-Persona.

– Impacto económico entre el 0,03 % y el 0,07 % del PIB actual.

– Extensión geográfica superior a 3 CC.AA.

– Daños reputacionales de difícil reparación, con eco mediático (amplia cobertura en los medios de comunicación) y afectando a la reputación de terceros.

Nivel medio:

– Afecta a más del 20 % de los sistemas de la organización.

– Interrupción en la presentación del servicio superior al 5 % de usuarios.

– El ciberincidente precisa para resolverse entre 1 y 5 Jornadas-Persona.

– Impacto económico entre el 0,001 % y el 0,03 % del PIB actual.

– Extensión geográfica superior a 2 CC.AA.

– Daños reputacionales apreciables, con eco mediático (amplia cobertura en los medios de comunicación).

Nivel bajo:

– Afecta a los sistemas de la organización.

– Interrupción de la prestación de un servicio.

– El ciberincidente precisa para resolverse menos de 1 Jornada-Persona.

– Impacto económico entre el 0,0001 % y el 0,001 % del PIB actual.

– Extensión geográfica superior a 1 CC.AA.

– Daños reputacionales puntuales, sin eco mediático.

Sin impacto:

– No hay ningún impacto apreciable.

5. Información a notificar a la autoridad competente en caso de incidente

El sujeto obligado comunicará, en la notificación inicial, todos aquellos campos acerca de los que tenga conocimiento en ese momento de acuerdo a la siguiente tabla, siendo posteriormente preceptiva la cumplimentación de todos los campos de la tabla en la notificación final del incidente.

Tabla 2. Información a notificar a la autoridad competente en caso de incidente

| Qué notificar | Descripción |
| --- | --- |
| Asunto. | Frase que describa de forma general el incidente. Este campo lo heredarán todas las notificaciones asociadas al incidente. |
| OSE/PSD. | Denominación del operador de servicios esenciales o proveedor de servicios digitales que notifica. |
| Sector estratégico. | Energía, transporte, financiero, etc. |
| Fecha y hora del incidente. | Indicar con la mayor precisión posible cuándo ha ocurrido el ciberincidente. |
| Fecha y hora de detección del incidente. | Indicar con la mayor precisión posible cuándo se ha detectado el ciberincidente. |
| Descripción. | Describir con detalle lo sucedido. |
| Recursos tecnológicos afectados. | Indicar la información técnica sobre el número y tipo de activos afectados por el ciberincidente, incluyendo direcciones IP, sistemas operativos, aplicaciones, versiones…. |
| Origen del incidente. | Indicar la causa del incidente si se conoce. Apertura de un fichero sospechoso, conexión de un dispositivo USB, acceso a una página web maliciosa, etc. |
| Taxonomía (clasificación). | Posible clasificación y tipo de ciberincidente en función de la taxonomía descrita. |
| Nivel de peligrosidad. | Especificar el nivel de peligrosidad asignado a la amenaza. |
| Nivel de impacto. | Especificar el nivel de impacto asignado al incidente. |
| Impacto transfronterizo. | Indicar si el incidente tiene impacto transfronterizo en algún Estado miembro de la Unión Europea. |
| Plan de acción y contramedidas. | Actuaciones realizadas hasta el momento en relación al ciberincidente. Indicar el Plan de acción seguido junto con las contramedidas implantadas. |
| Afectación. | Indicar si el afectado es una empresa o un particular, y las afectaciones según el nivel de impacto asignado. |
| Medios necesarios para la resolución (J-P). | Capacidad empleada en la resolución del incidente en Jornadas-Persona. |
| Impacto económico estimado (Si se conoce). | Costes asociados al incidente, tanto de carácter directo como indirecto. |
| Extensión geográfica (Si se conoce). | Local, autonómico, nacional, supranacional, etc. |
| Daños reputacionales (Si se conocen). | Afectación a la imagen corporativa del operador. |
| Adjuntos. | Indicar la relación de documentos adjuntos que se aportan para ayudar a conocer la causa del problema o a su resolución (capturas de pantalla, ficheros de registro de información, correos electrónicos, etc.). |
| Regulación afectada. | ENS / RGPD / NIS / PIC / Otros. |
| Se requiere actuación de FFCCSE. | Si / No. |

6. Ventana temporal de reporte

Todos aquellos sujetos obligados que se vean afectados por un incidente de obligada notificación a la autoridad competente, a través del CSIRT de referencia, remitirán, en tiempo y forma, aquellas notificaciones inicial, intermedia y final requeridas de acuerdo a la siguiente ventana temporal de reporte.

– La notificación inicial es una comunicación consistente en poner en conocimiento y alertar de la existencia de un incidente.

– La notificación intermedia es una comunicación mediante la que se actualizarán los datos disponibles en ese momento relativos al incidente comunicado.

– La notificación final es una comunicación final mediante la que se amplían y confirman los datos definitivos relativos al incidente comunicado.

No obstante lo anterior, se aportarán todas aquellas notificaciones adicionales intermedias o posteriores que se consideren necesarias.

Tabla 3. Ventana temporal de reporte

| Nivel de peligrosidad o impacto | Notificación inicial | Notificación intermedia | Notificación final |
| --- | --- | --- | --- |
| CRÍTICO. | Inmediata. | 24/48 horas. | 20 días. |
| MUY ALTO. | Inmediata. | 72 horas. | 40 días. |
| ALTO. | Inmediata. | – | – |
| MEDIO. | – | – | – |
| BAJO. | – | – | – |

Los tiempos reflejados en la tabla 3 para la «notificación intermedia» y la «notificación final» tienen como referencia el momento de remisión de la «notificación inicial». La «notificación inicial» tiene como referencia de tiempo el momento de tener conocimiento del incidente.

7. Definiciones y conceptos

La descripción de las conductas aquí incluidas tiene carácter técnico y se entiende a los meros efectos de la notificación y gestión de ciberincidentes. Como tal, es independiente tanto de la calificación de los hechos, como de la aplicación por parte de la autoridad judicial de los tipos penales establecidos en la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal.

Contenido abusivo:

– Correo masivo no solicitado (spam): correo electrónico no solicitado que se envía a un gran número de usuarios, o bien una alta tasa de correos electrónicos enviados a un mismo usuario en un corto espacio de tiempo.

– Acoso: referido a acoso virtual o ciberacoso, se trata del uso de medios de comunicación digitales para acosar a una persona, o grupo de personas, mediante ataques personales, divulgación de información privada o íntima, o falsa.

– Extorsión: obligar a una persona o mercantil, mediante el empleo de violencia o intimidación, a realizar u omitir actos con la intención de producir un perjuicio a esta, o bien con ánimo de lucro de la que lo provoca.

– Mensajes ofensivos: comunicaciones no esperadas o deseadas, así como acciones o expresiones que lesionan la dignidad de otra persona, menoscabando su fama o atentando contra su propia estimación.

– Delito: cualquier acción tipificada como delito de acuerdo a lo establecido en la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal.

– Pederastia: cualquier comportamiento relacionado con los descritos en el título VIII la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal, relativos a la captación o utilización de menores de edad o personas con discapacidad necesitadas de especial protección en actos que atenten contra su indemnidad o libertad sexual.

– Racismo: cualquier infracción penal, incluyendo infracciones contra las personas o las propiedades, donde la víctima, el local o el objetivo de la infracción se elija por su real o percibida, conexión, simpatía, filiación, apoyo o pertenencia a un grupo social, raza, religión o condición sexual.

– Apología de la violencia: exposición, ante una concurrencia de personas o por cualquier medio de difusión, de ideas o doctrinas que ensalcen el crimen o enaltezcan a su autor.

Contenido dañino:

– Malware (código dañino): palabra que deriva de los términos malicious y software. Cualquier pieza de software que lleve a cabo acciones como extracción de datos u otro tipo de alteración de un sistema puede categorizarse como malware. Así pues malware es un término que engloba varios tipos de programas dañinos.

– Virus: tipo de malware cuyo principal objetivo es modificar o alterar el comportamiento de un sistema informático sin el permiso o consentimiento del usuario. Se propaga mediante la ejecución en el sistema de software, archivos o documentos con carga dañina, adquiriendo la capacidad de replicarse de un sistema a otro. Los métodos más comunes de infección se dan a través de dispositivos extraíbles, descargas de Internet y archivos adjuntos en correos electrónicos. No obstante también puede hacerlo a través de scripts, documentos, y vulnerabilidades XSS presentes en la web. Es reseñable que un virus requiere la acción humana para su propagación a diferencia de otro malware, véase Gusano.

– Gusano: programa malicioso que tiene como característica principal su alto grado de dispersabilidad. Su fin es replicarse a nuevos sistemas para infectarlos y seguir replicándose a otros equipos informáticos, aprovechándose de todo tipo de medios como el correo electrónico, IRC, FTP, correo electrónico, P2P y otros protocolos específicos o ampliamente utilizados.

– Troyano: tipo de malware que se enmascara como software legítimo con la finalidad de convencer a la víctima para que instale la pieza en su sistema. Una vez instalado, el software dañino tiene la capacidad de desarrollar actividad perjudicial en segundo plano. Un troyano no depende una acción humana y no tiene la capacidad de replicarse, no obstante puede tener gran capacidad dañina en un sistema a modo de troyanos o explotando vulnerabilidades de software.

– Programa espía (spyware): tipo de malware que espía las actividades de un usuario sin su conocimiento o consentimiento. Estas actividades pueden incluir keyloggers, monitorizaciones, recolección de datos así como robo de datos. Los spyware se pueden difundir como un troyano o mediante explotación de software.

– Rootkit: conjunto de software dañino que permite el acceso privilegiado a áreas de una máquina, mientras que al mismo tiempo se oculta su presencia mediante la corrupción del Sistema Operativo u otras aplicaciones. Denotar que por maquina se entiende todo el espectro de sistemas IT, desde smartphones hasta ICS. El propósito por tanto de un rootkit es enmascarar eficazmente payloads y permitir su existencia en el sistema.

– Dialer: tipología de malware que se instala en una máquina y, de forma automática y sin consentimiento del usuario, realiza marcaciones telefónicas a número de tarificación especial. Estas acciones conllevan costes económicos en la víctima al repercutir el importe de la comunicación.

– Ransomware: se engloba bajo este epígrafe a aquel malware que infecta una máquina, de modo que el usuario es incapaz de acceder a los datos almacenados en el sistema. Normalmente la víctima recibe posteriormente algún tipo de comunicación en la que se le coacciona para que se pague una recompensa que permita acceder al sistema y los archivos bloqueados.

– Bot dañino: una botnet es el nombre que se emplea para designar a un conjunto de máquinas controladas remotamente con finalidad generalmente maliciosa. Un bot es una pieza de software maliciosa que recibe órdenes de un atacante principal que controla remotamente la máquina. Los servidores C&C habilitan al atacante para controlar los bots y que ejecuten las órdenes dictadas remotamente.

– RAT: del inglés Remote Access Tool, se trata de una funcionalidad específica de control remoto de un sistema de información, que incorporan determinadas familias o muestras de software dañino (malware).

– C&C: del inglés Command and Control, se refiere a paneles de mando y control (también referenciados como C2), por el cual atacantes cibernéticos controlan determinados equipos zombie infectados con muestras de la misma familia de software dañino. El panel de comando y control actúa como punto de referencia, control y gestión de los equipos infectados.

– Conexión sospechosa: todo intercambio de información a nivel de red local o pública, cuyo origen o destino no esté plenamente identificado, así como la legitimidad de los mismos.

Obtención de información:

– Escaneo de puertos (Scanning): análisis local o remoto mediante software, del estado de los puertos de una máquina conectada a una red. La finalidad de esta acción es la de obtener información relativa a la identificación de los servicios activos y las posibles vulnerabilidades que puedan existir en la red.

– Escaneo de red (Scanning): análisis local o remoto mediante software, del estado de una red. La finalidad de esta acción es la de obtener información relativa a la identificación de los servicios activos y las posibles vulnerabilidades que puedan existir en la red.

– Escaneo de tecnologías: análisis local o remoto mediante software, de las tecnologías presentes o disponibles en una red determinada o un sistema de información concreto, mediante el cual se obtienen las referencias del hardware/software presente, así como su versión, y potenciales vulnerabilidades.

– Transferencia de zona DNS (AXFR IXFR): transacción de los servidores DNS utilizada para la replicación de las bases de datos entre un servidor primario y los secundarios. Estas transacciones pueden ser completas (AXFR) o incrementales (IXFR).

– Análisis de paquetes (Sniffing): análisis mediante software del tráfico de una red con la finalidad de capturar información. El tráfico que viaje no cifrado podrá ser capturado y leído por un atacante.

– Ingeniería social: técnicas que buscan la revelación de información sensible de un objetivo, generalmente mediante el uso de métodos persuasivos y con ausencia de voluntad o conocimiento de la víctima.

– Phishing: estafa cometida a través de medios telemáticos mediante la cual el estafador intenta conseguir, de usuarios legítimos, información confidencial (contraseñas, datos bancarios, etc.) de forma fraudulenta empleando métodos de ingeniería social.

– Spear Phishing: variante del phishing mediante la que el atacante focaliza su actuación sobre un objetivo concreto.

Intrusiones:

– Explotación: cualquier práctica mediante la cual un atacante cibernético vulnera un sistema de información y/o comunicación, con fines ilícitos o para los cuales no está debidamente autorizado.

– Inyección SQL: tipo de explotación, consistente en la introducción de cadenas mal formadas de SQL, o cadenas que el receptor no espera o controla debidamente; las cuales provocan resultados no esperados en la aplicación o programa objetivo, y por la cual el atacante produce efectos inesperados y para los que no está autorizado en el sistema objetivo.

– Cross Site Scripting XSS (Directo o Indirecto): ataque que trata de explotar una vulnerabilidad presente en aplicaciones web, por la cual un atacante inyecta sentencias mal formadas o cadenas que el receptor no espera o controla debidamente.

– Cross Site Request Forgery (CSFR): falsificación de petición en sitios cruzados. Es un tipo de exploit dañino de un sitio web en el que comandos no autorizados son transmitidos por un usuario en el cual el sitio web confía. Esta vulnerabilidad es conocida también por otros nombres como XSRF, enlace hostil, ataque de un clic, cabalgamiento de sesión, y ataque automático. Al contrario que en los ataques XSS, los cuales explotan la confianza que un usuario tiene en un sitio en particular, el Cross Site Request Forgery explota la confianza que un sitio tiene en un usuario en particular.

– Defacement: tipología de ataque a sitios web en el que se implementa un cambio en la apariencia visual de la página. Para ello suelen emplearse técnicas como inyecciones SQL o algún tipo de vulnerabilidad existente en la página o en el servidor.

– Inclusión de ficheros (RFI y LFI): vulnerabilidad que permite a un atacante mostrar o ejecutar archivos remotos alojados en otros servidores a causa de una mala programación de la página que contiene funciones de inclusión de archivos. La inclusión local de archivos (LFI) es similar a la vulnerabilidad de Inclusión de archivos remotos, excepto que en lugar de incluir archivos remotos solo se pueden incluir archivos locales, es decir, archivos en el servidor actual para su ejecución.

– Evasión de sistemas de control: proceso por el cual una muestra de software dañino, o un conjunto de acciones orquestadas por un atacante cibernético, consiguen vulnerar o esquivar los sistemas o políticas de seguridad establecidas por un determinado sistema de información y comunicación.

– Pharming: ataque informático que aprovecha vulnerabilidades de los servidores DNS (Domain Name System). Al tratar de acceder el usuario al sitio web, el navegador redirigirá automáticamente al usuario a una dirección IP donde se aloja una web maliciosa que suplanta la auténtica, y en la que el atacante podrá obtener información sensible de los usuarios.

– Ataque por fuerza bruta: proceso por el cual un atacante trata de vulnerar un sistema de validación por credenciales de acceso, contraseña o similar, mediante el empleo de todas las combinaciones posibles, con el fin de acceder a sistemas de información y/o comunicación para los cuales no tiene privilegios o autorización.

– Ataque por diccionario: proceso por el cual un atacante trata de vulnerar un sistema de validación por credenciales de acceso, contraseña o similar, mediante el empleo de un diccionario previamente generado con determinadas combinaciones de caracteres, con el fin de acceder a sistemas de información y/o comunicación para los cuales no tiene privilegios o autorización.

– Robo de credenciales de acceso: acceso o sustracción no autorizada a credenciales de acceso a sistemas de información y/o comunicación.

Disponibilidad:

– DoS (Denial of Service) o ataque de denegación de servicio: conjunto de técnicas que tienen por objetivo dejar un servidor inoperativo. Mediante este tipo de ataques se busca sobrecargar un servidor y de esta forma impedir que los usuarios legítimos puedan utilizar los servicios por prestados por él. El ataque consiste en saturar con peticiones de servicio al servidor, hasta que este no puede atenderlas, provocando su colapso.

– DDoS (Distributed Denial of Service) o denegación distribuida de servicio: variante de DoS en el que la remisión de peticiones se lleva a cabo de forma coordinada desde varios puntos hacia un mismo destino. Para ello se emplean redes de bots, generalmente sin el conocimiento de los usuarios.

– Mala configuración: fallo de configuración en el software que está directamente asociado con una pérdida de disponibilidad de un servicio.

– Sabotaje/Terrorismo/Vandalismo: ataques implementados con el objetivo de provocar la interrupción o degradación de la prestación de un servicio, provocando daños relevantes en la continuidad del servicio de una institución o daños reputacionales relevantes cometidos con propósitos ideológicos, políticos o religiosos.

– Disrupción sin intención dañina: acciones que pueden provocar la interrupción o degradación de la prestación de un servicio, provocando daños relevantes en la continuidad del servicio de una institución o daños reputaciones relevantes.

– Inundación SYN o UDP: procedimientos usados para la realización de ataque DoS o DDoS consistente en iniciar una gran cantidad de sesiones impidiendo al servidor atender las peticiones licitas.

– DNS Open-Resolver: servidor DNS capaz resolver consultas DNS recursivas procedentes de cualquier origen de Internet. Este tipo de servidores suele emplearse por usuarios malintencionados para la realización de ataques DDoS.

Compromiso de la información:

– Acceso no autorizado a la información o ciberespionaje: proceso por el cual un usuario no autorizado accede a consultar contenido para el cual no está autorizado.

– Modificación no autorizada de información: proceso por el cual un usuario no autorizado accede a modificar contenido para el cual no está autorizado.

– Borrado no autorizado de información: proceso por el cual un usuario no autorizado accede a borrar contenido para el cual no está autorizado.

– Exfiltración de información: proceso por el cual un usuario difunde información en canales o fuentes en las cuales no está prevista o autorizada la compartición de esa información.

– Acceso no autorizado a sistemas: proceso por el cual un usuario accede sin vulnerar ningún servicio, sistema o red, a sistemas de información y/o comunicación para los cuales no está debidamente autorizado, o no tiene autorización tácita o manifiesta.

– Ataque POODLE / Ataque FREAK: proceso por el que se consigue que un servidor haga uso de un protocolo de comunicaciones no seguro, que originalmente no estaba previsto, con el objetivo de poder exfiltrar información.

Fraude:

– Uso no autorizado de recursos: empleo de tecnologías y/o servicios por usuarios que no están debidamente autorizados por la Dirección o negociado competente.

– Suplantación de identidad: actividad maliciosa en la que un atacante se hace pasar por otra persona para cometer algún tipo de fraude o acoso.

– Derechos de propiedad intelectual: la propiedad intelectual es el conjunto de derechos que corresponden a los autores y a otros titulares (artistas, productores, organismos de radiodifusión…) respecto de las obras y prestaciones fruto de su creación.

– Otros fraudes: engaño económico con la intención de conseguir un beneficio, y con el cual alguien resulta perjudicado.

Vulnerabilidades:

– Tecnología vulnerable: conocimiento por parte de los administradores de tecnologías, servicios o redes, de vulnerabilidades presentes en estas.

– Política de seguridad precaria: política de seguridad de la organización deficiente, mediante la cual existe la posibilidad de que durante un espacio de tiempo determinado, atacantes cibernéticos realizaron accesos no autorizados a sistemas de información, no pudiendo determinar fehacientemente este extremo.

Otros:

– Ciberterrorismo: delitos informáticos previstos en los artículo 197 bis y ter y 264 a 264 quater de la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal cuando dichos delitos se cometan con las finalidades previstas en el artículo 573.1 del mismo texto. Estas finalidades son:

• Subvertir el orden constitucional, o suprimir o desestabilizar gravemente el funcionamiento de las instituciones políticas o de las estructuras económicas o sociales del Estado, u obligar a los poderes públicos a realizar un acto o a abstenerse de hacerlo.

• Alterar gravemente la paz pública.

• Desestabilizar gravemente el funcionamiento de una organización internacional.

• Provocar un estado de terror en la población o en una parte de ella.

– Daños informáticos PIC: delitos informáticos previstos en los artículos 264.2 3.º y 4.º de la Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal, relacionadas con el borrado, dañado, alteración, supresión, o inaccesibilidad de datos, programas informáticos o documentos electrónicos de una Infraestructura Crítica. Así como conductas graves relacionadas con los términos anteriores que afecten a la prestación de un servicio esencial.

– APT (Advanced Persistent Threat o Amenaza Persistente Avanzada)/AVT (Advanced Volatility Threat): ataques dirigidos contra organizaciones concretas, sustentados en mecanismos muy sofisticados de ocultación, anonimato y persistencia. Esta amenaza habitualmente emplea técnicas de ingeniería social para conseguir sus objetivos junto con el uso de procedimientos de ataque conocidos o genuinos.

– Dominios DGA: procedimiento para generar de forma dinámica dominios donde se alojarán los servidores de Comando y Control, técnica usada en redes Botnet para dificultar su detención.

– Criptografía: técnica que consiste en cifrar un mensaje, conocido como texto en claro, convirtiéndolo en un mensaje cifrado o criptograma, que resulta ilegible para todo aquel que no conozca la clave mediante la cual ha sido cifrado.

– Proxy: ordenador, generalmente un servidor, intermedio usado en las comunicaciones entre otros dos equipos, siendo normalmente usado de manera trasparente para el usuario.

General:

– Ciberseguridad: la capacidad de las redes y sistemas de información de resistir, con un nivel determinado de fiabilidad, toda acción que comprometa la disponibilidad, autenticidad, integridad o confidencialidad de los datos almacenados, transmitidos o tratados, o los servicios correspondientes ofrecidos por tales redes y sistemas de información o accesibles a través de ellos.

– Ciberespacio: espacio virtual que engloba todos los sistemas TIC. El ciberespacio se apoya en la disponibilidad de Internet como red de redes, enriquecida con otras redes de transporte de datos.

– Redes y sistemas de información: se entiende por este concepto uno de los tres siguientes puntos:

• Las redes de comunicaciones electrónicas, tal y como vienen definidas en el número 31 del anexo II de la Ley 9/2014, de 9 de mayo, General de Telecomunicaciones.

• Todo dispositivo o grupo de dispositivos interconectados o relacionados entre sí en el que uno o varios de ellos realizan, mediante un programa, el tratamiento automático de datos digitales.

• Los datos digitales almacenados, tratados, recuperados o transmitidos mediante elementos contemplados anteriormente para su funcionamiento, utilización, protección y mantenimiento.

– Seguridad en redes y sistemas de información: la capacidad de las redes y sistemas de información de resistir, con un nivel determinado de fiabilidad, toda acción que comprometa la disponibilidad, autenticidad, integridad o confidencialidad de los datos almacenados, transmitidos o tratados, o los servicios correspondientes ofrecidos por tales redes y sistemas de información o accesibles a través de ellos.

– Operador de servicios esenciales: entidad pública o privada que se identifique considerando los factores establecidos en el artículo 6 del Real Decreto-ley 12/2018, de 7 de septiembre, que preste dichos servicios en alguno de los sectores estratégicos definidos en el anexo de la Ley 8/2011, de 28 de abril.

– Servicio digital: servicio de la sociedad de la información entendido en el sentido recogido en la letra a) del anexo de la Ley 34/2002, de 11 de julio, de servicios de la sociedad de la información y de comercio electrónico.

– Proveedor de servicios digitales: persona jurídica que presta un servicio digital.

– Ciberincidente: todo hecho que tenga efectos adversos reales en la seguridad de las redes y sistemas de información.

– Gestión de ciberincidentes: todos los procedimientos seguidos para detectar, analizar y limitar un incidente y responder ante este.

– Ciberamenaza: amenaza a los sistemas y servicios presentes en el ciberespacio o alcanzables a través de este.

– Taxonomía: clasificación u ordenación en grupos de objetos o sujetos que poseen unas características comunes.

– RGPD: Reglamento General de Protección de Datos, Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos y por el que se deroga la Directiva 95/46/CE.

– OpenPGP: estándar basado en el programa PGP, del inglés Pretty Good Privacy, cuya finalidad es proteger la información mediante el uso de criptografía de clave pública, así como facilitar la autenticación de documentos gracias a firmas digitales.

– Webinject: herramienta gratuita y de código abierto diseñada principalmente para automatizar la prueba de las aplicaciones y servicios web.

– Telnet: protocolo de red que permite acceder a otra máquina para manejarla remotamente como si estuviéramos sentados delante de ella.

– RDP (Remote Desktop Protocol): protocolo propietario que permite la comunicación en la ejecución de una aplicación entre un terminal y un servidor.

– VNC (Virtual Network Computing): programa de software libre basado en una estructura cliente-servidor que permite observar remotamente las acciones del ordenador servidor a través de un ordenador cliente.

– SNMP (Simple Network Management Protocol): protocolo de red utilizado para el intercambio de mensajes para la administración de dispositivos en red.

– Redis: motor de base de datos en memoria, basado en el almacenamiento en tablas de hashes.

– ICMP (Internet Control Message Protocol): protocolo de control de mensajes de Internet.

– Copia de seguridad limpia: punto de restauración de un sistema de la que se tiene la seguridad de no estar comprometida.
