## ANEXO II

## Medidas de seguridad

## 1. Disposiciones generales

1. Para lograr el cumplimiento de los principios básicos y requisitos mínimos establecidos, se aplicarán las medidas de seguridad indicadas en este anexo, las cuales serán proporcionales a:

a) Las dimensiones de seguridad relevantes en el sistema a proteger.

b) La categoría del sistema de información a proteger.

2. Las medidas de seguridad se dividen en tres grupos:

a) Marco organizativo [org]. Constituido por el conjunto de medidas relacionadas con la organización global de la seguridad.

b) Marco operacional [op]. Formado por las medidas a tomar para proteger la operación del sistema como conjunto integral de componentes para un fin.

c) Medidas de protección [mp]. Se centran en proteger activos concretos, según su naturaleza y la calidad exigida por el nivel de seguridad de las dimensiones afectadas.

## 2. Selección de medidas de seguridad

1. Para la selección de las medidas de seguridad se seguirán los pasos siguientes:

a) Identificación de los tipos de activos presentes.

b) Determinación de las dimensiones de seguridad relevantes, teniendo en cuenta lo establecido en el anexo I.

c) Determinación del nivel correspondiente a cada dimensión de seguridad, teniendo en cuenta lo establecido en el anexo I.

d) Determinación de la categoría del sistema, según lo establecido en el Anexo I.

e) Selección de las medidas de seguridad apropiadas de entre las contenidas en este Anexo, de acuerdo con las dimensiones de seguridad y sus niveles, y, para determinadas medidas de seguridad, de acuerdo con la categoría del sistema.

2. A los efectos de facilitar el cumplimiento de lo dispuesto en este anexo, cuando en un sistema de información existan sistemas que requieran la aplicación de un nivel de medidas de seguridad diferente al del sistema principal, podrán segregarse de este último, siendo de aplicación en cada caso el nivel de medidas de seguridad correspondiente y siempre que puedan delimitarse la información y los servicios afectados.

3. La relación de medidas seleccionadas se formalizará en un documento denominado Declaración de Aplicabilidad, firmado por el responsable de la seguridad del sistema.

4. La correspondencia entre los niveles de seguridad exigidos en cada dimensión y las medidas de seguridad, es la que se indica en la tabla siguiente:

| Dimensiones | MEDIDAS DE SEGURIDAD |
| --- | --- |
| Afectadas | B | M | A |
|  |  |  |  | org | Marco organizativo |
| categoría | aplica | = | = | org.1 | Política de seguridad |
| categoría | aplica | = | = | org.2 | Normativa de seguridad |
| categoría | aplica | = | = | org.3 | Procedimientos de seguridad |
| categoría | aplica | = | = | org.4 | Proceso de autorización |
| Dimensiones | MEDIDAS DE SEGURIDAD |
| --- | --- |
| Afectadas | B | M | A |
|  |  |  |  | op | Marco operacional |
|  |  |  |  | op.pl | Planificación |
| categoría | aplica | + | ++ | op.pl.1 | Análisis de riesgos |
| categoría | aplica | = | = | op.pl.2 | Arquitectura de seguridad |
| categoría | aplica | = | = | op.pl.3 | Adquisición de nuevos componentes |
| D | n.a. | aplica | = | op.pl.4 | Dimensionamiento / Gestión de capacidades |
| categoría | n.a. | n.a. | aplica | op.pl.5 | Componentes certificados |
|  |  |  |  | op.acc | Control de acceso |
| A T | aplica | = | = | op.acc.1 | Identificación |
| I C A T | aplica | = | = | op.acc.2 | Requisitos de acceso |
| I C A T | n.a. | aplica | = | op.acc.3 | Segregación de funciones y tareas |
| I C A T | aplica | = | = | op.acc.4 | Proceso de gestión de derechos de acceso |
| I C A T | aplica | + | ++ | op.acc.5 | Mecanismo de autenticación |
| I C A T | aplica | + | ++ | op.acc.6 | Acceso local (local logon) |
| I C A T | aplica | + | = | op.acc.7 | Acceso remoto (remote login) |
|  |  |  |  | op.exp | Explotación |
| categoría | aplica | = | = | op.exp.1 | Inventario de activos |
| categoría | aplica | = | = | op.exp.2 | Configuración de seguridad |
| categoría | n.a. | aplica | = | op.exp.3 | Gestión de la configuración |
| categoría | aplica | = | = | op.exp.4 | Mantenimiento |
| categoría | n.a. | aplica | = | op.exp.5 | Gestión de cambios |
| categoría | aplica | = | = | op.exp.6 | Protección frente a código dañino |
| categoría | n.a. | aplica | = | op.exp.7 | Gestión de incidencias |
| T | n.a. | n.a. | aplica | op.exp.8 | Registro de la actividad de los usuarios |
| categoría | n.a. | aplica | = | op.exp.9 | Registro de la gestión de incidencias |
| T | n.a. | n.a. | aplica | op.exp.10 | Protección de los registros de actividad |
| categoría | aplica | + | = | op.exp.11 | Protección de claves criptográficas |
|  |  |  |  | op.ext | Servicios externos |
| categoría | n.a. | aplica | = | op.ext.1 | Contratación y acuerdos de nivel de servicio |
| categoría | n.a. | aplica | = | op.ext.2 | Gestión diaria |
| D | n.a. | n.a. | aplica | op.ext.9 | Medios alternativos |
|  |  |  |  | op.cont | Continuidad del servicio |
| D | n.a. | aplica | = | op.cont.1 | Análisis de impacto |
| D | n.a. | n.a. | aplica | op.cont.2 | Plan de continuidad |
| D | n.a. | n.a. | aplica | op.cont.3 | Pruebas periódicas |
|  |  |  |  | op.mon | Monitorización del sistema |
| categoría | n.a. | n.a. | aplica | op.mon.1 | Detección de intrusión |
| categoría | n.a. | n.a. | aplica | op.mon.2 | Sistema de métricas |
| Dimensiones | MEDIDAS DE SEGURIDAD |
| --- | --- |
| Afectadas | B | M | A |
|  |  |  |  | mp | Medidas de protección |
|  |  |  |  | mp.if | Protección de las instalaciones e infraestructuras |
| categoría | aplica | = | = | mp.if.1 | Áreas separadas y con control de acceso |
| categoría | aplica | = | = | mp.if.2 | Identificación de las personas |
| categoría | aplica | = | = | mp.if.3 | Acondicionamiento de los locales |
| D | aplica | + | = | mp.if.4 | Energía eléctrica |
| D | aplica | = | = | mp.if.5 | Protección frente a incendios |
| D | n.a. | aplica | = | mp.if.6 | Protección frente a inundaciones |
| categoría | aplica | = | = | mp.if.7 | Registro de entrada y salida de equipamiento |
| D | n.a. | n.a. | aplica | mp.if.9 | Instalaciones alternativas |
|  |  |  |  | mp.per | Gestión del personal |
| categoría | n.a. | aplica | = | mp.per.1 | Caracterización del puesto de trabajo |
| categoría | aplica | = | = | mp.per.2 | Deberes y obligaciones |
| categoría | aplica | = | = | mp.per.3 | Concienciación |
| categoría | aplica | = | = | mp.per.4 | Formación |
| D | n.a. | n.a. | aplica | mp.per.9 | Personal alternativo |
|  |  |  |  | mp.eq | Protección de los equipos |
| categoría | aplica | + | = | mp.eq.1 | Puesto de trabajo despejado |
| A | n.a. | aplica | + | mp.eq.2 | Bloqueo de puesto de trabajo |
| categoría | aplica | = | + | mp.eq.3 | Protección de equipos portátiles |
| D | n.a. | aplica | = | mp.eq.9 | Medios alternativos |
|  |  |  |  | mp.com | Protección de las comunicaciones |
| categoría | aplica | = | + | mp.com.1 | Perímetro seguro |
| C | n.a. | aplica | + | mp.com.2 | Protección de la confidencialidad |
| I A | aplica | + | ++ | mp.com.3 | Protección de la autenticidad y de la integridad |
| categoría | n.a. | n.a. | aplica | mp.com.4 | Segregación de redes |
| D | n.a. | n.a. | aplica | mp.com.9 | Medios alternativos |
|  |  |  |  | mp.si | Protección de los soportes de información |
| C | aplica | = | = | mp.si.1 | Etiquetado |
| I C | n.a. | aplica | + | mp.si.2 | Criptografía |
| categoría | aplica | = | = | mp.si.3 | Custodia |
| categoría | aplica | = | = | mp.si.4 | Transporte |
| C | n.a. | aplica | = | mp.si.5 | Borrado y destrucción |
|  |  |  |  | mp.sw | Protección de las aplicaciones informáticas |
| categoría | n.a. | aplica | = | mp.sw.1 | Desarrollo |
| categoría | aplica | + | ++ | mp.sw.2 | Aceptación y puesta en servicio |
|  |  |  |  | mp.info | Protección de la información |
| categoría | aplica | = | = | mp.info.1 | Datos de carácter personal |
| C | aplica | + | = | mp.info.2 | Calificación de la información |
| C | n.a. | n.a. | aplica | mp.info.3 | Cifrado |
| I A | aplica | + | ++ | mp.info.4 | Firma electrónica |
| T | n.a. | n.a. | aplica | mp.info.5 | Sellos de tiempo |
| C | aplica | = | = | mp.info.6 | Limpieza de documentos |
| D | n.a. | aplica | = | mp.info.9 | Copias de seguridad (backup) |
|  |  |  |  | mp.s | Protección de los servicios |
| categoría | aplica | = | = | mp.s.1 | Protección del correo electrónico |
| categoría | aplica | = | = | mp.s.2 | Protección de servicios y aplicaciones web |
| D | n.a. | aplica | + | mp.s.8 | Protección frente a la denegación de servicio |
| D | n.a. | n.a. | aplica | mp.s.9 | Medios alternativos |

En las tablas del presente Anexo se emplean las siguientes convenciones:

a) Para indicar que una determinada medida de seguridad se debe aplicar a una o varias dimensiones de seguridad en algún nivel determinado se utiliza la voz «aplica».

b) «n.a.» significa «no aplica».

c) Para indicar que las exigencias de un nivel son iguales a los del nivel inferior se utiliza el signo «=».

d) Para indicar el incremento de exigencias graduado en función de del nivel de la dimensión de seguridad, se utilizan los signos «+» y «++».

e) Para indicar que una medida protege específicamente una cierta dimensión de seguridad, ésta se explicita mediante su inicial.

f) En las tablas del presente anexo se han empleado colores verde, amarillo y rojo de la siguiente forma: el color verde para indicar que una cierta medida se aplica en sistemas de categoría BÁSICA o superior; el amarillo para indicar las medidas que empiezan a aplicarse en categoría MEDIA o superior; el rojo para indicar las medidas que sólo son de aplicación en categoría ALTA.

## 3. Marco organizativo [org]

El marco organizativo está constituido por un conjunto de medidas relacionadas con la organización global de la seguridad.

3.1 Política de seguridad [org.1].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

La política de seguridad será aprobada por el órgano superior competente que corresponda, de acuerdo con lo establecido en el artículo 11, y se plasmará en un documento escrito, en el que, de forma clara, se precise, al menos, lo siguiente:

a) Los objetivos o misión de la organización.

b) El marco legal y regulatorio en el que se desarrollarán las actividades.

c) Los roles o funciones de seguridad, definiendo para cada uno, los deberes y responsabilidades del cargo, así como el procedimiento para su designación y renovación.

d) La estructura del comité o los comités para la gestión y coordinación de la seguridad, detallando su ámbito de responsabilidad, los miembros y la relación con otros elementos de la organización.

e) Las directrices para la estructuración de la documentación de seguridad del sistema, su gestión y acceso.

La política de seguridad debe referenciar y ser coherente con lo establecido en el Documento de Seguridad que exige el Real Decreto 1720/2007, en lo que corresponda.

3.2 Normativa de seguridad [org.2].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se dispondrá de una serie de documentos que describan:

a) El uso correcto de equipos, servicios e instalaciones.

b) Lo que se considerará uso indebido.

c) La responsabilidad del personal con respecto al cumplimiento o violación de estas normas: derechos, deberes y medidas disciplinarias de acuerdo con la legislación vigente.

3.3 Procedimientos de seguridad [org.3].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se dispondrá de una serie de documentos que detallen de forma clara y precisa:

a) Cómo llevar a cabo las tareas habituales.

b) Quién debe hacer cada tarea.

c) Cómo identificar y reportar comportamientos anómalos.

3.4 Proceso de autorización [org.4].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se establecerá un proceso formal de autorizaciones que cubra todos los elementos del sistema de información:

a) Utilización de instalaciones, habituales y alternativas.

b) Entrada de equipos en producción, en particular, equipos que involucren criptografía.

c) Entrada de aplicaciones en producción.

d) Establecimiento de enlaces de comunicaciones con otros sistemas.

e) Utilización de medios de comunicación, habituales y alternativos.

f) Utilización de soportes de información.

g) Utilización de equipos móviles. Se entenderá por equipos móviles ordenadores portátiles, PDA, u otros de naturaleza análoga.

## 4. Marco operacional [op]

El marco operacional está constituido por las medidas a tomar para proteger la operación del sistema como conjunto integral de componentes para un fin.

4.1 Planificación [op.pl].

4.1.1 Análisis de riesgos [op.pl.1].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | + | ++ |

Categoría BÁSICA

Bastará un análisis informal, realizado en lenguaje natural. Es decir, una exposición textual que describa los siguientes aspectos:

a) Identifique los activos más valiosos del sistema.

b) Identifique las amenazas más probables.

c) Identifique las salvaguardas que protegen de dichas amenazas.

d) Identifique los principales riesgos residuales.

Categoría MEDIA

Se deberá realizar un análisis semi-formal, usando un lenguaje específico, con un catálogo básico de amenazas y una semántica definida. Es decir, una presentación con tablas que describa los siguientes aspectos:

a) Identifique y valore cualitativamente los activos más valiosos del sistema.

b) Identifique y cuantifique las amenazas más probables.

c) Identifique y valore las salvaguardas que protegen de dichas amenazas.

d) Identifique y valore el riesgo residual.

Categoría ALTA

Se deberá realizar un análisis formal, usando un lenguaje específico, con un fundamento matemático reconocido internacionalmente. El análisis deberá cubrir los siguientes aspectos:

a) Identifique y valore cualitativamente los activos más valiosos del sistema.

b) Identifique y cuantifique las amenazas posibles.

c) Identifique las vulnerabilidades habilitantes de dichas amenazas.

d) Identifique y valore las salvaguardas adecuadas.

e) Identifique y valore el riesgo residual.

4.1.2 Arquitectura de seguridad [op.pl.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

La seguridad del sistema será objeto de un planteamiento integral detallando, al menos, los siguientes aspectos:

a) Documentación de las instalaciones:

1.º Áreas.

2.º Puntos de acceso.

b) Documentación del sistema:

1.º Equipos.

2.º Redes internas y conexiones al exterior.

3.º Puntos de acceso al sistema (puestos de trabajo y consolas de administración).

c) Esquema de líneas de defensa:

1.º Puntos de interconexión a otros sistemas o a otras redes, en especial si se trata de Internet.

2.º Cortafuegos, DMZ, etc.

3.º Utilización de tecnologías diferentes para prevenir vulnerabilidades que pudieran perforar simultáneamente varias líneas de defensa.

d) Sistema de identificación y autenticación de usuarios:

1.º Uso de claves concertadas, contraseñas, tarjetas de identificación, biometría, u otras de naturaleza análoga.

2.º Uso de ficheros o directorios para autenticar al usuario y determinar sus derechos de acceso.

e) Controles técnicos internos:

1.º Validación de datos de entrada, salida y datos intermedios.

f) Sistema de gestión con actualización y aprobación periódica.

4.1.3 Adquisición de nuevos componentes [op.pl.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se establecerá un proceso formal para planificar la adquisición de nuevos componentes del sistema, proceso que:

a) Atenderá a las conclusiones del análisis de riesgos: [op.pl.1].

b) Será acorde a la arquitectura de seguridad escogida: [op.pl.2].

c) Contemplará las necesidades técnicas, de formación y de financiación de forma conjunta.

4.1.4 Dimensionamiento / gestión de capacidades [op.pl.4].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

Con carácter previo a la puesta en explotación, se realizará un estudio previo que cubrirá los siguientes aspectos:

a) Necesidades de procesamiento.

b) Necesidades de almacenamiento de información: durante su procesamiento y durante el periodo que deba retenerse.

d) Necesidades de comunicación.

e) Necesidades de personal: cantidad y cualificación profesional.

f) Necesidades de instalaciones y medios auxiliares.

4.1.5 Componentes certificados [op.pl.5].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | no aplica | aplica |

Categoría ALTA

Se utilizarán preferentemente sistemas, productos o equipos cuyas funcionalidades de seguridad y su nivel hayan sido evaluados conforme a normas europeas o internacionales y que estén certificados por entidades independientes de reconocida solvencia.

Tendrán la consideración de normas europeas o internacionales, ISO/IEC 15408 u otras de naturaleza y calidad análogas.

Tendrán la consideración de entidades independientes de reconocida solvencia las recogidas en los acuerdos o arreglos internacionales de reconocimiento mutuo de los certificados de la seguridad de la tecnología de la información u otras de naturaleza análoga.

4.2 Control de acceso. [op.acc].

El control de acceso cubre el conjunto de actividades preparatorias y ejecutivas para que una determinada entidad, usuario o proceso, pueda, o no, acceder a un recurso del sistema para realizar una determinada acción.

El control de acceso que se implante en un sistema real será un punto de equilibrio entre la comodidad de uso y la protección de la información. En sistemas de nivel Bajo, se primará la comodidad, mientras que en sistemas de nivel Alto se primará la protección.

En todo control de acceso se requerirá lo siguiente:

a) Que todo acceso esté prohibido, salvo concesión expresa.

b) Que la entidad quede identificada singularmente [op.acc.1].

c) Que la utilización de los recursos esté protegida [op.acc.2].

d) Que se definan para cada entidad los siguientes parámetros: a qué se necesita acceder, con qué derechos y bajo qué autorización [op.acc.4].

e) Serán diferentes las personas que autorizan, usan y controlan el uso [op.acc.3].

f) Que la identidad de la entidad quede suficientemente autenticada [mp.acc.5].

g) Que se controle tanto el acceso local ([op.acc.6]) como el acceso remoto ([op.acc.7]).

Con el cumplimiento de todas las medidas indicadas se garantizará que nadie accederá a recursos sin autorización. Además, quedará registrado el uso del sistema ([op.exp.8]) para poder detectar y reaccionar a cualquier fallo accidental o deliberado.

Cuando se interconecten sistemas en los que la identificación, autenticación y autorización tengan lugar en diferentes dominios de seguridad, bajo distintas responsabilidades, en los casos en que sea necesario, las medidas de seguridad locales se acompañarán de los correspondientes acuerdos de colaboración que delimiten mecanismos y procedimientos para la atribución y ejercicio efectivos de las responsabilidades de cada sistema ([op.ext]).

4.2.1 Identificación [op.acc.1].

| dimensiones | A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

La identificación de los usuarios del sistema se realizará de acuerdo con lo que se indica a continuación:

a) Se asignará un identificador singular para cada entidad (usuario o proceso) que accede al sistema, de tal forma que:

1.º Se puede saber quién recibe y qué derechos de acceso recibe.

2.º Se puede saber quién ha hecho algo y qué ha hecho.

b) Las cuentas de usuario se gestionarán de la siguiente forma:

1.º Cada cuenta estará asociada a un identificador único.

2.º Las cuentas deben ser inhabilitadas en los siguientes casos: cuando el usuario deja la organización; cuando el usuario cesa en la función para la cual se requería la cuenta de usuario; o, cuando la persona que la autorizó, da orden en sentido contrario.

3.º Las cuentas se retendrán durante el periodo necesario para atender a las necesidades de trazabilidad de los registros de actividad asociados a las mismas. A este periodo se le denominará periodo de retención.

4.2.2 Requisitos de acceso [op.acc.2].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

Los requisitos de acceso se atenderán a lo que a continuación se indica:

a) Los recursos del sistema se protegerán con algún mecanismo que impida su utilización, salvo a las entidades que disfruten de derechos de acceso suficientes.

b) Los derechos de acceso de cada recurso, se establecerán según las decisiones de la persona responsable del recurso, ateniéndose a la política y normativa de seguridad del sistema.

c) Particularmente se controlará el acceso a los componentes del sistema y a sus ficheros o registros de configuración.

4.2.3 Segregación de funciones y tareas [op.acc.3].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

El sistema de control de acceso se organizará de forma que se exija la concurrencia de dos o más personas para realizar tareas críticas, anulando la posibilidad de que un solo individuo autorizado, pueda abusar de sus derechos para cometer alguna acción ilícita.

En concreto, se separarán al menos las siguientes funciones:

a) Desarrollo de operación.

b) Configuración y mantenimiento del sistema de operación.

c) Auditoría o supervisión de cualquier otra función.

4.2.4 Proceso de gestión de derechos de acceso [op.acc.4].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

Los derechos de acceso de cada usuario, se limitarán atendiendo a los siguientes principios:

a) Mínimo privilegio. Los privilegios de cada usuario se reducirán al mínimo estrictamente necesario para cumplir sus obligaciones. De esta forma se acotan los daños que pudiera causar una entidad, de forma accidental o intencionada.

b) Necesidad de conocer. Los privilegios se limitarán de forma que los usuarios sólo accederán al conocimiento de aquella información requerida para cumplir sus obligaciones.

c) Capacidad de autorizar. Sólo y exclusivamente el personal con competencia para ello, podrá conceder, alterar o anular la autorización de acceso a los recursos, conforme a los criterios establecidos por su responsable.

4.2.5 Mecanismo de autenticación [op.acc.5].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | ++ |

Los mecanismos de autenticación frente al sistema se adecuarán al nivel del sistema atendiendo a las consideraciones que siguen.

Las guías CCN-STIC desarrollarán los mecanismos concretos adecuados a cada nivel.

Nivel BAJO

a) Se admitirá el uso de cualquier mecanismo de autenticación: claves concertadas, o dispositivos físicos (en expresión inglesa »tokens») o componentes lógicos tales como certificados software u otros equivalentes o mecanismos biométricos.

b) En el caso de usar contraseñas se aplicarán reglas básicas de calidad de las mismas.

c) Se atenderá a la seguridad de los autenticadores de forma que:

1.º Los autenticadores se activarán una vez estén bajo el control efectivo del usuario.

2.º Los autenticadores estarán bajo el control exclusivo del usuario.

3.º El usuario reconocerá que los ha recibido y que conoce y acepta las obligaciones que implica su tenencia, en particular el deber de custodia diligente, protección de su confidencialidad e información inmediata en caso de pérdida.

4.º Los autenticadores se cambiarán con una periodicidad marcada por la política de la organización, atendiendo a la categoría del sistema al que se accede.

5.º Los autenticadores se retirarán y serán deshabilitados cuando la entidad (persona, equipo o proceso) que autentican termina su relación con el sistema.

Nivel MEDIO

a) No se recomendará el uso de claves concertadas.

b) Se recomendará el uso de otro tipo de mecanismos del tipo dispositivos físicos (tokens) o componentes lógicos tales como certificados software u otros equivalentes o biométricos.

c) En el caso de usar contraseñas se aplicarán políticas rigurosas de calidad de la contraseña y renovación frecuente.

Nivel ALTO

a) Los autenticadores se suspenderán tras un periodo definido de no utilización.

b) No se admitirá el uso de claves concertadas.

c) Se exigirá el uso de dispositivos físicos (tokens) personalizados o biometría.

d) En el caso de utilización de dispositivos físicos (tokens) se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

e) Se emplearán, preferentemente, productos certificados [op.pl.5].

Tabla resumen de mecanismos de autenticación admisibles

|  |  | Nivel |
| --- | --- | --- |
|  |  | BAJO | MEDIO | ALTO |
| algo que se sabe | claves concertadas | sí | Con cautela | no |
| algo que se tiene | Tokens | si | sí | criptográficos |
| algo que se es | Biometría | sí | sí | + doble factor |

4.2.6 Acceso local [op.acc.6].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | ++ |

Se considera acceso local al realizado desde puestos de trabajo dentro de las propias instalaciones de la organización. Estos accesos tendrán en cuenta el nivel de las dimensiones de seguridad:

Nivel BAJO

a) Se prevendrán ataques que puedan revelar información del sistema sin llegar a acceder al mismo. La información revelada a quien intenta acceder, debe ser la mínima imprescindible (los diálogos de acceso proporcionarán solamente la información indispensable).

b) El número de intentos permitidos será limitado, bloqueando la oportunidad de acceso una vez efectuados un cierto número de fallos consecutivos.

c) Se registrarán los accesos con éxito, y los fallidos.

d) El sistema informará al usuario de sus obligaciones inmediatamente después de obtener el acceso.

Nivel MEDIO

Se informará al usuario del último acceso efectuado con su identidad.

Nivel ALTO

a) El acceso estará limitado por horario, fechas y lugar desde donde se accede.

b) Se definirán aquellos puntos en los que el sistema requerirá una renovación de la autenticación del usuario, mediante identificación singular, no bastando con la sesión establecida.

4.2.7 Acceso remoto [op.acc.7].

| dimensiones | I C A T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | = |

Se considera acceso remoto al realizado desde fuera de las propias instalaciones de la organización, a través de redes de terceros.

Nivel BAJO

Se garantizará la seguridad del sistema cuando accedan remotamente usuarios u otras entidades, lo que implicará proteger tanto el acceso en sí mismo (como [op.acc.6]) como el canal de acceso remoto (como en [mp.com.2] y [mp.com.3]).

Nivel MEDIO

Se establecerá una política específica de lo que puede hacerse remotamente, requiriéndose autorización positiva.

4.3 Explotación [op.exp].

4.3.1 Inventario de activos [op.exp.1].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se mantendrá un inventario actualizado de todos los elementos del sistema, detallando su naturaleza e identificando a su responsable; es decir, la persona que es responsable de las decisiones relativas al mismo.

4.3.2 Configuración de seguridad [op.exp.2].

| dimensiones | Todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se configurarán los equipos previamente a su entrada en operación, de forma que:

a) Se retiren cuentas y contraseñas estándar.

b) Se aplicará la regla de «mínima funcionalidad»:

1.º El sistema debe proporcionar la funcionalidad requerida para que la organización alcance sus objetivos y ninguna otra funcionalidad,

2.º No proporcionará funciones gratuitas, ni de operación, ni de administración, ni de auditoría, reduciendo de esta forma su perímetro al mínimo imprescindible.

3.º Se eliminará o desactivará mediante el control de la configuración, aquellas funciones que no sean de interés, no sean necesarias, e incluso, aquellas que sean inadecuadas al fin que se persigue.

c) Se aplicará la regla de «seguridad por defecto»:

1.º Las medidas de seguridad serán respetuosas con el usuario y protegerán a éste, salvo que se exponga conscientemente a un riesgo.

2.º Para reducir la seguridad, el usuario tiene que realizar acciones conscientes.

3.º El uso natural, en los casos que el usuario no ha consultado el manual, será un uso seguro.

4.3.3 Gestión de la configuración [op.exp.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Se gestionará de forma continua la configuración de los componentes del sistema de forma que:

a) Se mantenga en todo momento la regla de «funcionalidad mínima» ([op.exp.2]).

b) Se mantenga en todo momento la regla de «seguridad por defecto» ([op.exp.2]).

c) El sistema se adapte a las nuevas necesidades, previamente autorizadas ([op.acc.4]).

d) El sistema reaccione a vulnerabilidades reportadas ([op.exp.4]).

e) El sistema reaccione a incidencias (ver [op.exp.7]).

4.3.4 Mantenimiento [op.exp.4].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Para mantener el equipamiento físico y lógico que constituye el sistema, se aplicará lo siguiente:

a) Se atenderá a las especificaciones de los fabricantes en lo relativo a instalación y mantenimiento de los sistemas.

b) Se efectuará un seguimiento continuo de los anuncios de defectos.

c) Se dispondrá de un procedimiento para analizar, priorizar y determinar cuándo aplicar las actualizaciones de seguridad, parches, mejoras y nuevas versiones. La priorización tendrá en cuenta la variación del riesgo en función de la aplicación o no de la actualización.

4.3.5 Gestión de cambios [op.exp.5].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Se mantendrá un control continuo de cambios realizados en el sistema, de forma que:

a) Todos los cambios anunciados por el fabricante o proveedor serán analizados para determinar su conveniencia para ser incorporados, o no.

b) Antes de poner en producción una nueva versión o una versión parcheada, se comprobará en un equipo que no esté en producción, que la nueva instalación funciona correctamente y no disminuye la eficacia de las funciones necesarias para el trabajo diario. El equipo de pruebas será equivalente al de producción en los aspectos que se comprueban.

c) Los cambios se planificarán para reducir el impacto sobre la prestación de los servicios afectados.

d) Mediante análisis de riesgos se determinará si los cambios son relevantes para la seguridad del sistema. Aquellos cambios que impliquen una situación de riesgo de nivel alto serán aprobados explícitamente de forma previa a su implantación.

4.3.6 Protección frente a código dañino [op.exp.6].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se considera código dañino: los virus, los gusanos, los troyanos, los programas espías, conocidos en terminología inglesa como «spyware», y en general, todo lo conocido como «malware».

Se dispondrá de mecanismos de prevención y reacción frente a código dañino con mantenimiento de acuerdo a las recomendaciones del fabricante.

4.3.7 Gestión de incidencias [op.exp.7].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Se dispondrá de un proceso integral para hacer frente a los incidentes que puedan tener un impacto en la seguridad del sistema, incluyendo:

a) Procedimiento de reporte de incidentes reales o sospechosos, detallando el escalado de la notificación.

b) Procedimiento de toma de medidas urgentes, incluyendo la detención de servicios, el aislamiento del sistema afectado, la recogida de evidencias y protección de los registros, según convenga al caso.

c) Procedimiento de asignación de recursos para investigar las causas, analizar las consecuencias y resolver el incidente.

d) Procedimientos para informar a las partes interesadas, internas y externas.

e) Procedimientos para:

1.º Prevenir que se repita el incidente.

2.º Incluir en los procedimientos de usuario la identificación y forma de tratar el incidente.

3.º Actualizar, extender, mejorar u optimizar los procedimientos de resolución de incidencias.

La gestión de incidentes que afecten a datos de carácter personal tendrá en cuenta lo dispuesto en la Ley Orgánica 15/1999, de 13 de diciembre, y normas de desarrollo, sin perjuicio de cumplir, además, las medidas establecidas por este real decreto.

4.3.8 Registro de la actividad de los usuarios [op.exp.8].

| dimensiones | T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se registrarán todas las actividades de los usuarios en el sistema, de forma que:

a) El registro indicará quién realiza la actividad, cuando la realiza y sobre qué información.

b) Se incluirá la actividad de los usuarios y, especialmente, la de los operadores y administradores del sistema en cuanto pueden acceder a la configuración y actuar en el mantenimiento del mismo.

c) Deben registrarse las actividades realizadas con éxito y los intentos fracasados.

d) La determinación de qué actividades debe en registrarse y con qué niveles de detalle se determinará a la vista del análisis de riesgos realizado sobre el sistema ([op.pl.1]).

4.3.9 Registro de la gestión de incidencias [op.exp.9].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Se registrarán todas las actuaciones relacionadas con la gestión de incidencias, de forma que:

a) Se registrará el reporte inicial, las actuaciones de emergencia y las modificaciones del sistema derivadas del incidente.

b) Se registrará aquella evidencia que pueda, posteriormente, sustentar una demanda judicial, o hacer frente a ella, cuando el incidente pueda llevar a actuaciones disciplinarias sobre el personal interno, sobre proveedores externos o a la persecución de delitos. En la determinación de la composición y detalle de estas evidencias, se recurrirá a asesoramiento legal especializado.

c) Como consecuencia del análisis de las incidencias, se revisará la determinación de los eventos auditables.

4.3.10 Protección de los registros de actividad [op.exp.10].

| dimensiones | T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se protegerán los registros del sistema, de forma que:

a) Se determinará el periodo de retención de los registros.

b) Se asegurará la fecha y hora. Ver [mp.info.5].

c) Los registros no podrán ser modificados ni eliminados por personal no autorizado.

d) Las copias de seguridad, si existen, se ajustarán a los mismos requisitos.

4.3.11 Protección de claves criptográficas [op.exp.11].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | + | = |

Las claves criptográficas se protegerán durante todo su ciclo de vida: (1) generación, (2) transporte al punto de explotación, (3) custodia durante la explotación, (4) archivo posterior a su retirada de explotación activa y (5) destrucción final.

Categoría BÁSICA

a) Los medios de generación estarán aislados de los medios de explotación.

b) Las claves retiradas de operación que deban ser archivadas, lo serán en medios aislados de los de explotación.

Categoría MEDIA

a) Se usarán programas evaluados o dispositivos criptográficos certificados.

b) Se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

4.4 Servicios externos [op.ext].

Cuando se utilicen recursos externos a la organización, sean servicios, equipos, instalaciones o personal, deberá tenerse en cuenta que la delegación se limita a las funciones.

La organización sigue siendo en todo momento responsable de los riesgos en que se incurre en la medida en que impacten sobre la información manejada y los servicios finales prestados por la organización.

La organización dispondrá las medidas necesarias para poder ejercer su responsabilidad y mantener el control en todo momento.

4.4.1 Contratación y acuerdos de nivel de servicio [op.ext.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Previa a la utilización de recursos externos se establecerán contractualmente las características del servicio prestado y las responsabilidades de las partes. Se detallará lo que se considera calidad mínima del servicio prestado y las consecuencias de su incumplimiento.

4.4.2 Gestión diaria [op.ext.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Para la gestión diaria del sistema, se establecerán los siguientes puntos:

a) Un sistema rutinario para medir el cumplimiento de las obligaciones de servicio y el procedimiento para neutralizar cualquier desviación fuera del margen de tolerancia acordado ([op.ext.1]).

b) El mecanismo y los procedimientos de coordinación para llevar a cabo las tareas de mantenimiento de los sistemas afectados por el acuerdo.

c) El mecanismo y los procedimientos de coordinación en caso de incidencias y desastres (ver [op.exp.7]).

4.4.3 Medios alternativos [op.ext.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Estará prevista la provisión del servicio por medios alternativos en caso de indisponibilidad del servicio contratado. El servicio alternativo disfrutará de las mismas garantías de seguridad que el servicio habitual.

4.5 Continuidad del servicio [op.cont].

4.5.1 Análisis de impacto [op.cont.1].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

Se realizará un análisis de impacto que permita determinar:

a) Los requisitos de disponibilidad de cada servicio medidos como el impacto de una interrupción durante un cierto periodo de tiempo.

b) Los elementos que son críticos para la prestación de cada servicio.

4.5.2 Plan de continuidad [op.cont.2].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se desarrollará un plan de continuidad que establezca las acciones a ejecutar en caso de interrupción de los servicios prestados con los medios habituales. Este plan contemplará los siguientes aspectos:

a) Se identificarán funciones, responsabilidades y actividades a realizar.

b) Existirá una previsión de los medios alternativos que se va a conjugar para poder seguir prestando los servicios.

c) Todos los medios alternativos estarán planificados y materializados en acuerdos o contratos con los proveedores correspondientes.

d) Las personas afectadas por el plan recibirán formación específica relativa a su papel en dicho plan.

e) El plan de continuidad será parte integral y armónica de los planes de continuidad de la organización en otras materias ajenas a la seguridad.

4.5.3 Pruebas periódicas [op.cont.3].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se realizarán pruebas periódicas para localizar y, corregir en su caso, los errores o deficiencias que puedan existir en el plan de continuidad

4.6 Monitorización del sistema [op.mon].

El sistema estará sujeto a medidas de monitorización de su actividad.

4.6.1 Detección de intrusión [op.mon.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | no aplica | aplica |

Categoría ALTA

Se dispondrán de herramientas de detección o de prevención de intrusión.

4.6.2 Sistema de métricas [op.mon.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | no aplica | aplica |

Categoría ALTA

Se establecerá un conjunto de indicadores que mida el desempeño real del sistema en materia de seguridad, en los siguientes aspectos:

a) Grado de implantación de las medidas de seguridad.

b) Eficacia y eficiencia de las medidas de seguridad.

c) Impacto de los incidentes de seguridad.

## 5. Medidas de protección [mp]

Las medidas de protección, se centrarán en proteger activos concretos, según su naturaleza, con el nivel requerido en cada dimensión de seguridad.

5.1 Protección de las instalaciones e infraestructuras [mp.if].

5.1.1 Áreas separadas y con control de acceso [mp.if.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

El equipamiento de instalará en áreas separadas específicas para su función.

Se controlarán los accesos a las áreas indicadas de forma que sólo se pueda acceder por las entradas previstas y vigiladas.

5.1.2 Identificación de las personas [mp.if.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

El mecanismo de control de acceso se atendrá a lo que se dispone a continuación:

a) Se identificará a todas las personas que accedan a los locales donde hay equipamiento que forme parte del sistema de información.

b) Se registrarán las entradas y salidas de personas.

5.1.3 Acondicionamiento de los locales [mp.if.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Los locales donde se ubiquen los sistemas de información y sus componentes, dispondrán de elementos adecuados para el eficaz funcionamiento del equipamiento allí instalado. Y, en especial:

a) Condiciones de temperatura y humedad.

b) Protección frente a las amenazas identificadas en el análisis de riesgos.

c) Protección del cableado frente a incidentes fortuitos o deliberados.

5.1.4 Energía eléctrica [mp.if.4].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | = |

Nivel BAJO

Los locales donde se ubiquen los sistemas de información y sus componentes dispondrán de la energía eléctrica, y sus tomas correspondientes, necesaria para su funcionamiento, de forma que en los mismos:

a) Se garantizará el suministro de potencia eléctrica.

b) Se garantizará el correcto funcionamiento de las luces de emergencia.

Nivel MEDIO

Se garantizará el suministro eléctrico a los sistemas en caso de fallo del suministro general, garantizando el tiempo suficiente para una terminación ordenada de los procesos, salvaguardando la información.

5.1.5 Protección frente a incendios [mp.if.5].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

Los locales donde se ubiquen los sistemas de información y sus componentes se protegerán frente a incendios fortuitos o deliberados, aplicando al menos la normativa industrial pertinente.

5.1.6 Protección frente a inundaciones [mp.if.6].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

Los locales donde se ubiquen los sistemas de información y sus componentes se protegerán frente a incidentes fortuitos o deliberados causados por el agua.

5.1.7 Registro de entrada y salida de equipamiento [mp.if.7].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se llevará un registro pormenorizado de toda entrada y salida de equipamiento, incluyendo la identificación de la persona que autoriza de movimiento.

5.1.8 Instalaciones alternativas [mp.if.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se garantizará la existencia y disponibilidad de instalaciones alternativas para poder trabajar en caso de que las instalaciones habituales no estén disponibles. Las instalaciones alternativas disfrutarán de las mismas garantías de seguridad que las instalaciones habituales.

5.2 Gestión del personal [mp.per].

5.2.1 Caracterización del puesto de trabajo [mp.per.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

Cada puesto de trabajo se caracterizará de la siguiente forma:

a) Se definirán las responsabilidades relacionadas con cada puesto de trabajo en materia de seguridad. La definición se basará en el análisis de riesgos.

b) Se definirán los requisitos que deben satisfacer las personas que vayan a ocupar el puesto de trabajo, en particular, en términos de confidencialidad.

c) Dichos requisitos se tendrán en cuenta en la selección de la persona que vaya a ocupar dicho puesto, incluyendo la verificación de sus antecedentes laborales, formación y otras referencias.

5.2.2 Deberes y obligaciones [mp.per.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

1. Se informará a cada persona que trabaje en el sistema, de los deberes y responsabilidades de su puesto de trabajo en materia de seguridad.

a) Se especificarán las medidas disciplinarias a que haya lugar.

b) Se cubrirá tanto el periodo durante el cual se desempeña el puesto, como las obligaciones en caso de término de la asignación, o traslado a otro puesto de trabajo.

c) Se contemplará el deber de confidencialidad respecto de los datos a los que tenga acceso, tanto durante el periodo que estén adscritos al puesto de trabajo, como posteriormente a su terminación.

2. En caso de personal contratado a través de un tercero:

a) Se establecerán los deberes y obligaciones del personal.

b) Se establecerán los deberes y obligaciones de cada parte.

c) Se establecerá el procedimiento de resolución de incidentes relacionados con el incumplimiento de las obligaciones.

5.2.3 Concienciación [mp.per.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se realizarán las acciones necesarias para concienciar regularmente al personal acerca de su papel y responsabilidad para que la seguridad del sistema alcance los niveles exigidos.

En particular, se recordará regularmente:

a) La normativa de seguridad relativa al buen uso de los sistemas.

b) La identificación de incidentes, actividades o comportamientos sospechosos que deban ser reportados para su tratamiento por personal especializado.

c) El procedimiento de reporte de incidencias de seguridad, sean reales o falsas alarmas.

5.2.4 Formación [mp.per.4].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se formará regularmente al personal en aquellas materias que requieran para el desempeño de sus funciones, en particular en lo relativo a:

a) Configuración de sistemas.

b) Detección y reacción a incidentes.

c) Gestión de la información en cualquier soporte en el que se encuentre. Se cubrirán al menos las siguientes actividades: almacenamiento, transferencia, copias, distribución y destrucción.

5.2.5 Personal alternativo [mp.per.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se garantizará la existencia y disponibilidad de otras personas que se puedan hacer cargo de las funciones en caso de indisponibilidad del personal habitual. El personal alternativo deberá estar sometido a las mismas garantías de seguridad que el personal habitual.

5.3 Protección de los equipos [mp.eq].

5.3.1 Puesto de trabajo despejado [mp.eq.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | + | = |

Categoría BÁSICA

Se exigirá que los puestos de trabajo permanezcan despejados, sin más material encima de la mesa que el requerido para la actividad que se está realizando en cada momento

Categoría MEDIA

Este material se guardará en lugar cerrado cuando no se esté utilizando.

5.3.2 Bloqueo de puesto de trabajo [mp.eq.2].

| dimensiones | A |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | + |

Nivel MEDIO

El puesto de trabajo se bloqueará al cabo de un tiempo prudencial de inactividad, requiriendo una nueva autenticación del usuario para reanudar la actividad en curso.

Nivel ALTO

Pasado un cierto tiempo, superior al anterior, se cancelarán las sesiones abiertas desde dicho puesto de trabajo.

5.3.3 Protección de portátiles [mp.eq.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | + |

Categoría BÁSICA

Los equipos que abandonen las instalaciones de la organización y no puedan beneficiarse de la protección física correspondiente, con un riesgo manifiesto de pérdida o robo, serán protegidos adecuadamente.

Sin perjuicio de las medidas generales que les afecten, se adoptarán las siguientes:

a) Se llevará un inventario de equipos portátiles junto con una identificación de la persona responsable del mismo y un control regular de que está positivamente bajo su control.

b) Se establecerá un canal de comunicación para informar, al servicio de gestión de incidencias, de pérdidas o sustracciones.

c) Se establecerá un sistema de protección perimetral que minimice la visibilidad exterior y controle las opciones de acceso al interior cuando el equipo se conecte a redes, en particular si el equipo se conecta a redes públicas.

d) Se evitará, en la medida de lo posible, que el equipo contenga claves de acceso remoto a la organización. Se considerarán claves de acceso remoto aquellas que sean capaces de habilitar un acceso a otros equipos de la organización, u otras de naturaleza análoga.

Categoría ALTA

a) Se dotará al dispositivo de detectores de violación que permitan saber el equipo ha sido manipulado y activen los procedimientos previstos de gestión del incidente.

b) La información de nivel alto almacenada en el disco se protegerá mediante cifrado.

5.3.4 Medios alternativos [mp.eq.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | No aplica | aplica | = |

Se garantizará la existencia y disponibilidad de medios alternativos de tratamiento de la información para el caso de que fallen los medios habituales. Estos medios alternativos estarán sujetos a las mismas garantías de protección.

Igualmente, se establecerá un tiempo máximo para que los equipos alternativos entren en funcionamiento.

5.4 Protección de las comunicaciones [mp.com].

5.4.1 Perímetro seguro [mp.com.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | + |

Categoría BÁSICA

Se dispondrá un sistema cortafuegos que separe la red interna del exterior. Todo el tráfico deberá atravesar dicho cortafuegos que sólo dejara transitar los flujos previamente autorizados.

Categoría ALTA

a) El sistema de cortafuegos constará de dos o más equipos de diferente fabricante dispuestos en cascada.

b) Se dispondrán sistemas redundantes.

5.4.2 Protección de la confidencialidad [mp.com.2].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | + |

Nivel MEDIO

a) Se emplearán redes privadas virtuales cuando la comunicación discurra por redes fuera del propio dominio de seguridad.

b) Se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

Nivel ALTO

a) Se emplearán, preferentemente, dispositivos hardware en el establecimiento y utilización de la red privada virtual.

b) Se emplearán, preferentemente, productos certificados [op.pl.5].

5.4.3 Protección de la autenticidad y de la integridad [mp.com.3].

| dimensiones | I A |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | ++ |

Nivel BAJO

a) Se asegurará la autenticidad del otro extremo de un canal de comunicación antes de intercambiar información alguna (ver [op.acc.5]).

b) Se prevendrán ataques activos, garantizando que al menos serán detectados. y se activarán los procedimientos previstos de tratamiento del incidente Se considerarán ataques activos:

1.º La alteración de la información en transito

2.º La inyección de información espuria

3.º El secuestro de la sesión por una tercera parte

Nivel MEDIO

a) Se emplearán redes privadas virtuales cuando la comunicación discurra por redes fuera del propio dominio de seguridad.

b) Se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

Nivel ALTO

a) Se valorará positivamente en empleo de dispositivos hardware en el establecimiento y utilización de la red privada virtual.

b) Se emplearán, preferentemente, productos certificados [op.pl.5].

5.4.4 Segregación de redes [mp.com.4].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | no aplica | aplica |

La segregación de redes acota el acceso a la información y, consiguientemente, la propagación de los incidentes de seguridad, que quedan restringidos al entorno donde ocurren.

Categoría ALTA

La red se segmentará en segmentos de forma que haya:

a) Control de entrada de los usuarios que llegan a cada segmento.

b) Control de salida de la información disponible en cada segmento.

c) Las redes se pueden segmentar por dispositivos físicos o lógicos. El punto de interconexión estará particularmente asegurado, mantenido y monitorizado (como en [mp.com.1]).

5.4.5 Medios alternativos [mp.com.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se garantizará la existencia y disponibilidad de medios alternativos de comunicación para el caso de que fallen los medios habituales. Los medios alternativos de comunicación:

a) Estarán sujetos y proporcionar las mismas garantías de protección que el medio habitual.

b) Garantizarán un tiempo máximo de entrada en funcionamiento.

5.5 Protección de los soportes de información [mp.si].

5.5.1 Etiquetado [mp.si.1].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

Los soportes de información se etiquetarán de forma que, sin revelar su contenido, se indique el nivel de seguridad de la información contenida de mayor calificación.

Los usuarios han de estar capacitados para entender el significado de las etiquetas, bien mediante simple inspección, bien mediante el recurso a un repositorio que lo explique.

5.5.2 Criptografía. [mp.si.2].

| dimensiones | I C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | + |

Esta medida se aplica, en particular, a todos los dispositivos removibles. Se entenderán por dispositivos removibles, los CD, DVD, discos USB, u otros de naturaleza análoga.

Nivel MEDIO

Se aplicarán mecanismos criptográficos que garanticen la confidencialidad y la integridad de la información contenida.

Nivel ALTO

a) Se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

b) Se emplearán, preferentemente, productos certificados [op.pl.5].

5.5.3 Custodia [mp.si.3].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Se aplicará la debida diligencia y control a los soportes de información que permanecen bajo la responsabilidad de la organización, mediante las siguientes actuaciones:

a) Garantizando el control de acceso con medidas físicas ([mp.if.1] y [mp.if.7]) ó lógicas ([mp.si.2]), o ambas.

b) Garantizando que se respetan las exigencias de mantenimiento del fabricante, en especial, en lo referente a temperatura, humedad y otros agresores medioambientales.

5.5.4 Transporte [mp.si.4].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

El responsable de sistemas garantizará que los dispositivos permanecen bajo control y que satisfacen sus requisitos de seguridad mientras están siendo desplazados de un lugar a otro.

Para ello:

a) Se dispondrá de un registro de salida que identifique al transportista que recibe el soporte para su traslado.

b) Se dispondrá de un registro de entrada que identifique al transportista que lo entrega.

c) Se dispondrá de un procedimiento rutinario que coteje las salidas con las llegadas y levante las alarmas pertinentes cuando se detecte algún incidente.

d) Se utilizarán los medios de protección criptográfica ([mp.si.2]) correspondientes al nivel de calificación de la información contenida de mayor nivel.

e) Se gestionarán las claves según [op.exp.11].

5.5.5 Borrado y destrucción [mp.si.5].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

La medida de borrado y destrucción de soportes de información se aplicará a todo tipo de equipos susceptibles de almacenar información, incluyendo medios electrónicos y no electrónicos.

a) Los soportes que vayan a ser reutilizados para otra información o liberados a otra organización serán objeto de un borrado seguro de su anterior contenido.

b) Se destruirán de forma segura los soportes, en los siguientes casos:

1.º Cuando la naturaleza del soporte no permita un borrado seguro.

2.º Cuando así lo requiera el procedimiento asociado al tipo de la información contenida,.

c) Se emplearán, preferentemente, productos certificados [op.pl.5].

5.6 Protección de las aplicaciones informáticas [mp.sw].

5.6.1 Desarrollo de aplicaciones [mp.sw.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | no aplica | aplica | = |

Categoría MEDIA

a) El desarrollo de aplicaciones se realizará sobre un sistema diferente y separado del de producción, no debiendo existir herramientas o datos de desarrollo en el entorno de producción.

b) Se aplicará una metodología de desarrollo reconocida que:

1.º Tome en consideración los aspectos de seguridad a lo largo de todo el ciclo de vida.

2.º Trate específicamente los datos usados en pruebas.

3.º Permita la inspección del código fuente.

c) Los siguientes elementos serán parte integral del diseño del sistema:

1.º Los mecanismos de identificación y autenticación.

2.º Los mecanismos de protección de la información tratada.

3.º La generación y tratamiento de pistas de auditoría.

d) Las pruebas anteriores a la implantación o modificación de los sistemas de información no se realizarán con datos reales, salvo que se asegure el nivel de seguridad correspondiente.

5.6.2 Aceptación y puesta en servicio [mp.sw.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | + | ++ |

Categoría BÁSICA

Antes de pasar a producción se comprobará el correcto funcionamiento de la aplicación.

a) Se comprobará que:

1.º Se cumplen los criterios de aceptación en materia de seguridad.

2.º No se deteriora la seguridad de otros componentes del servicio.

b) Las pruebas se realizarán en un entorno aislado (pre-producción).

c) Las pruebas de aceptación no se realizarán con datos reales, salvo que se asegure el nivel de seguridad correspondiente.

Categoría MEDIA

Se realizarán las siguientes inspecciones previas a la entrada en servicio:

a) Análisis de vulnerabilidades.

b) Pruebas de penetración.

Categoría ALTA

Se realizarán las siguientes inspecciones previas a la entrada en servicio:

a) Análisis de coherencia en la integración en los procesos.

b) Se considerará la oportunidad de realizar una auditoría de código fuente.

5.7 Protección de la información [mp.info].

5.7.1 Datos de carácter personal [mp.info.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Cuando el sistema trate datos de carácter personal, se estará a lo dispuesto en la Ley Orgánica 15/1999, de 13 de diciembre, y normas de desarrollo, sin perjuicio de cumplir, además, las medidas establecidas por este real decreto.

Lo indicado en el párrafo anterior también se aplicará, cuando una disposición con rango de ley se remita a las normas sobre datos de carácter personal en la protección de información.

5.7.2 Calificación de la información [mp.info.2].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | = |

Nivel BAJO

1. Para calificar la información se estará a lo establecido legalmente sobre la naturaleza de la misma.

2. La política de seguridad establecerá quién es el responsable de cada información manejada por el sistema.

3. La política de seguridad recogerá, directa o indirectamente, los criterios que, en cada organización, determinarán el nivel de seguridad requerido, dentro del marco establecido en el artículo 43 y los criterios generales prescritos en el Anexo I.

4. El responsable de cada información seguirá los criterios determinados en el apartado anterior para asignar a cada información el nivel de seguridad requerido, y será responsable de su documentación y aprobación formal.

5. El responsable de cada información en cada momento tendrá en exclusiva la potestad de modificar el nivel de seguridad requerido, de acuerdo a los apartados anteriores.

Nivel MEDIO

Se redactarán los procedimientos necesarios que describan, en detalle, la forma en que se ha de etiquetar y tratar la información en consideración al nivel de seguridad que requiere; y precisando cómo se ha de realizar:

a) Su control de acceso.

b) Su almacenamiento.

c) La realización de copias.

d) El etiquetado de soportes.

e) Su transmisión telemática.

f) Y cualquier otra actividad relacionada con dicha información.

5.7.3 Cifrado de la información [mp.info.3].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Para el cifrado de información se estará a lo que se indica a continuación:

a) La información con un nivel alto en confidencialidad se cifrará tanto durante su almacenamiento como durante su transmisión. Sólo estará en claro mientras se está haciendo uso de ella.

b) Para el uso de criptografía en las comunicaciones, se estará a lo dispuesto en [mp.com.2].

c) Para el uso de criptografía en los soportes de información, se estará a lo dispuesto en [mp.si.2].

5.7.4 Firma electrónica [mp.info.4].

| dimensiones | I A |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | + | ++ |

La firma electrónica es un mecanismo de prevención del repudio; es decir, previene frente a la posibilidad de que en el futuro el signatario pudiera desdecirse de la información firmada.

La firma electrónica garantiza la autenticidad del signatario y la integridad del contenido.

Cuando se emplee firma electrónica:

a) El signatario será la parte que se hace responsable de la información, en la medida de sus atribuciones.

b) Se dispondrá de una Política de Firma Electrónica, aprobada por el órgano superior competente que corresponda.

Nivel BAJO

Se empleará cualquier medio de firma electrónica de los previstos en la legislación vigente.

Nivel MEDIO

1. Los medios utilizados en la firma electrónica serán proporcionados a la calificación de la información tratada. En todo caso:

a) Se emplearán algoritmos acreditados por el Centro Criptológico Nacional.

b) Se emplearán, preferentemente, certificados reconocidos.

c) Se emplearán, preferentemente, dispositivos seguros de firma.

2. Se garantizará la verificación y validación de la firma electrónica durante el tiempo requerido por la actividad administrativa que aquélla soporte, sin perjuicio de que se pueda ampliar este período de acuerdo con lo que establezca la política de firma electrónica y de certificados que sea de aplicación. Para tal fin:

a) Se adjuntará a la firma, o se referenciará, toda la información pertinente para su verificación y validación:

1.º Certificados.

2.º Datos de verificación y validación.

b) Se protegerán la firma y la información mencionada en el apartado anterior con un sello de tiempo.

c) El organismo que recabe documentos firmados por el administrado verificará y validará la firma recibida en el momento de la recepción, anexando o referenciando sin ambigüedad la información descrita en los epígrafes a) y b).

d) La firma electrónica de documentos por parte de la Administración anexará o referenciará sin ambigüedad la información descrita en los epígrafes a) y b).

Nivel ALTO

Se aplicarán las medidas de seguridad referentes a firma electrónica exigibles en la nivel Medio, además de las siguientes:

a) Se usarán certificados reconocidos.

b) Se usarán dispositivos seguros de creación de firma.

c) Se emplearán, preferentemente, productos certificados [op.pl.5].

5.7.5 Sellos de tiempo [mp.info.5].

| dimensiones | T |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Los sellos de tiempo prevendrán la posibilidad del repudio posterior:

1. Los sellos de tiempo se aplicarán a aquella información que sea susceptible de ser utilizada como evidencia electrónica en el futuro.

2. Los datos pertinentes para la verificación posterior de la fecha serán tratados con la misma seguridad que la información fechada a efectos de disponibilidad, integridad y confidencialidad.

3. Se renovarán regularmente los sellos de tiempo hasta que la información protegida ya no sea requerida por el proceso administrativo al que da soporte.

4. Se utilizarán productos certificados (según [op.pl.5]) o servicios externos admitidos.

Véase [op.exp.10].

5.7.6 Limpieza de documentos [mp.info.6].

| dimensiones | C |
| --- | --- |
| nivel | bajo | medio | alto |
|  | aplica | = | = |

En el proceso de limpieza de documentos, se retirará de estos toda la información adicional contenida en campos ocultos, meta-datos, comentarios o revisiones anteriores, salvo cuando dicha información sea pertinente para el receptor del documento.

Esta medida es especialmente relevante cuando el documento se difunde ampliamente, como ocurre cuando se ofrece al público en un servidor web u otro tipo de repositorio de información.

Se tendrá presente que el incumplimiento de esta medida puede perjudicar:

a) Al mantenimiento de la confidencialidad de información que no debería haberse revelado al receptor del documento.

b) Al mantenimiento de la confidencialidad de las fuentes u orígenes de la información, que no debe conocer el receptor del documento.

c) A la buena imagen de la organización que difunde el documento por cuanto demuestra un descuido en su buen hacer.

5.7.7 Copias de seguridad (backup) [mp.info.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | aplica | = |

Nivel MEDIO

Se realizarán copias de respaldo que permitan recuperar datos perdidos accidental o intencionadamente con una antigüedad determinada.

Las copias de respaldo disfrutarán de la misma seguridad que los datos originales en lo que se refiere a integridad, confidencialidad, autenticidad y trazabilidad. En particular, se considerará la conveniencia o necesidad de que las copias de seguridad estén cifradas para garantizar la confidencialidad.

Las copias de respaldo deberán abarcar:

a) Información de trabajo de la organización.

b) Aplicaciones en explotación, incluyendo los sistemas operativos.

c) Datos de configuración, servicios, aplicaciones, equipos, u otros de naturaleza análoga.

d) Claves utilizadas para preservar la confidencialidad de la información.

5.8 Protección de los servicios [mp.s].

5.8.1 Protección del correo electrónico (e-mail) [mp.s.1].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

El correo electrónico se protegerá frente a las amenazas que le son propias, actuando del siguiente modo:

a) La información distribuida por medio de correo electrónico, se protegerá, tanto en el cuerpo de los mensajes, como en los anexos.

b) Se protegerá la información de encaminamiento de mensajes y establecimiento de conexiones.

c) Se protegerá a la organización frente a problemas que se materializan por medio del correo electrónico, en concreto:

1.º Correo no solicitado, en su expresión inglesa «spam».

2.º Programas dañinos, constituidos por virus, gusanos, troyanos, espías, u otros de naturaleza análoga.

3.º Código móvil de tipo «applet».

d) Se establecerán normas de uso del correo electrónico por parte del personal determinado. Estas normas de uso contendrán:

1.º Limitaciones al uso como soporte de comunicaciones privadas.

2.º Actividades de concienciación y formación relativas al uso del correo electrónico.

5.8.2 Protección de servicios y aplicaciones web [mp.s.2].

| dimensiones | todas |
| --- | --- |
| categoría | básica | media | alta |
|  | aplica | = | = |

Los subsistemas dedicados a la publicación de información deberán ser protegidos frente a las amenazas que les son propias.

a) Cuando la información tenga algún tipo de control de acceso, se garantizará la imposibilidad de acceder a la información obviando la autenticación, en particular tomando medidas en los siguientes aspectos:

1.º Se evitará que el servidor ofrezca acceso a los documentos por vías alternativas al protocolo determinado.

2.º Se prevendrán ataques de manipulación de URL.

3.º Se prevendrán ataques de manipulación de fragmentos de información que se almacena en el disco duro del visitante de una página web a través de su navegador, a petición del servidor de la página, conocido en terminología inglesa como «cookies».

4.º Se prevendrán ataques de inyección de código.

b) Se prevendrán intentos de escalado de privilegios.

c) Se prevendrán ataques de «cross site scripting».

d) Se prevendrán ataques de manipulación de programas o dispositivos que realizan una acción en representación de otros, conocidos en terminología inglesa como «proxies» y, sistemas especiales de almacenamiento de alta velocidad, conocidos en terminología inglesa como «cachés».

5.8.3 Protección frente a la denegación de servicio [mp.s.8].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | No aplica | aplica | + |

Nivel MEDIO

Se establecerán medidas preventivas y reactivas frente a ataques de denegación de servicio (DOS Denial of Service). Para ello:

a) Se planificará y dotará al sistema de capacidad suficiente para atender a la carga prevista con holgura.

b) Se desplegarán tecnologías para prevenir los ataques conocidos.

Nivel ALTO

a) Se establecerá un sistema de detección de ataques de denegación de servicio.

b) Se establecerán procedimientos de reacción a los ataques, incluyendo la comunicación con el proveedor de comunicaciones.

c) Se impedirá el lanzamiento de ataques desde las propias instalaciones perjudicando a terceros.

5.8.4 Medios alternativos [mp.s.9].

| dimensiones | D |
| --- | --- |
| nivel | bajo | medio | alto |
|  | no aplica | no aplica | aplica |

Nivel ALTO

Se garantizará la existencia y disponibilidad de medios alternativos para prestar los servicios en el caso de que fallen los medios habituales. Estos medios alternativos estarán sujetos a las mismas garantías de protección que los medios habituales.

## 6. Desarrollo y complemento de las medidas de seguridad

Las medidas de seguridad se desarrollarán y complementarán según lo establecido en la disposición final segunda.

## 7. Interpretación

La interpretación del presente anexo se realizará según el sentido propio de sus palabras, en relación con el contexto, antecedentes históricos y legislativos, entre los que figura lo dispuesto en las instrucciones técnicas CCN-STIC correspondientes a la implementación y a diversos escenarios de aplicación tales como sedes electrónicas, servicios de validación de certificados electrónicos, servicios de fechado electrónico y validación de documentos fechados, atendiendo el espíritu y finalidad de aquellas.

> Redactado conforme a la corrección de errores publicada en BOE núm. 61, de 11 de marzo de 2010. Ref. BOE-A-2010-4054
