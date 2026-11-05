## ANEXO I

## Elementos, infraestructuras y recursos que integran una red 5G

1. Descripción de la arquitectura de la red 5G-SA

Para el análisis requerido en el presente Esquema Nacional de Seguridad de redes y servicios 5G, se utiliza una arquitectura de red de referencia, siguiendo la recomendación del 3GPP y la especificación ETSI TS 123 501.

En la figura siguiente, se muestra un esquema simplificado de una arquitectura 5G-SA para escenarios de no-roaming (que será utilizada de forma genérica como base). Elementos no presentados en la figura son el UDR, UDSF, UCMF, CHF, 5G-EIR, NWDAF y SEPP.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_1.png)

Fig. 1: Arquitectura 5G según especificación ETSI TS 123 501

Estos elementos de red son funciones software que se despliegan sobre una infraestructura de virtualización (compuesta, a su vez, de hardware y software de virtualización), la cual puede ser dedicada y específica para una función de red, o común para varias funciones, incluso funciones de red de varios suministradores 5G. En este escenario, la infraestructura para hospedar las funciones de red virtualizadas puede estar diversificada tanto geográficamente como por suministradores 5G diferentes, tal y como se describirá más adelante en este documento.

Adicionalmente a los elementos de red, se despliegan un conjunto de Sistemas para la operación y gestión de la red GER (también denominados OSS, Operations Support System).

2. Identificación y descripción de los entornos de red 5G-SA

Con el objetivo de desglosar la complejidad de la arquitectura de una red 5G-SA, se divide la misma en entornos de red.

Un entorno de red es una agrupación de activos que tienen un cometido y unas características particulares dentro de la red que los diferencian del resto de entornos.

Se puede distinguir dos tipologías de entorno:

a) Entornos primarios: Se consideran entornos primarios aquellos propios de la tecnología o naturaleza de 5G que no existirían sin su despliegue.

b) Entornos secundarios: Se consideran entornos secundarios aquellos comunes en un operador de telecomunicaciones.

En la siguiente figura (figura 2) se puede apreciar una clasificación de la red 5G-SA por entornos:

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_2.png)

3. Entornos de red primarios

Dentro de los entornos de red primarios, se encuentra el Acceso Radio, el Núcleo de Red, el Transporte-Backhaul (SecGW), la Interconexión de Roaming y los Sistemas de Control, Gestión y Operación de la Red.

a) Acceso Radio: El entorno de acceso radio (RAN) se encarga de dotar de cobertura a los terminales para que estos se puedan conectar a la red. Destacan las siguientes funciones en el entorno:

1. Operación y mantenimiento del emplazamiento radio. El software permite configurar cada emplazamiento con una serie de células por tecnología para poder prestar servicio a los usuarios y, durante el funcionamiento de la estación base, supervisa su estado para detectar posibles problemas o averías, ante cuya aparición reportaría una alarma al sistema de gestión para que el operador sea consciente y resuelva el problema.

2. Señalización. Para que los usuarios puedan registrarse en la red y establecer servicios portadores para sus comunicaciones, es necesaria señalización entre los terminales, la estación base, y el núcleo de red, y parte de estas funciones las realiza el software de la estación base.

3. Gestión de recursos radio. Los recursos radio de una célula dada son compartidos entre distintos usuarios y el software de la estación base es el responsable de repartirlos entre dichos usuarios (calidad del enlace radio de cada usuario, demanda de velocidad, etc.). El software también puede distribuir a los usuarios entre las células de su estación base (o incluso con células de emplazamientos vecinos), para que el reparto de usuarios sea más homogéneo entre células vecinas.

4. Movilidad. el software de la estación base gestiona el traspaso de las comunicaciones de los usuarios entre distintas células, de su emplazamiento o de emplazamientos vecinos, a medida que los usuarios se desplazan por la red.

5. Transporte: La comunicación física con el resto de la red se realiza por medio de enlaces IP, eléctricos u ópticos, y la estación base tienen que encargarse de gestionar dichos enlaces (priorización entre los distintos tipos de tráfico que van por dichos enlaces, configuración de VLANs, supervisión del enlace, etc.).

La red 5G, en el plano de acceso radio (RAN), se implementa con un solo tipo de elemento de red denominado, de forma genérica, gNodoB (gNB). La mayoría de los suministradores 5G de Red de acceso radio disponen de distintos modelos de gNB, adaptados a distintos tipos de escenarios.

De forma genérica, existen los tipos siguientes:

1. Macro gNB: proporcionan mayor área de cobertura y capacidad de tráfico. Se instalan típicamente en azoteas de edificios o lugares con mucha visibilidad radioeléctrica, con el objetivo de dar cobertura y capacidad general.

2. Micro gNB: de menor potencia, orientados a dar cobertura en localizaciones concretas, ya sean pequeños espacios públicos (como plazas) o espacios de interior (como lugares de eventos, oficinas pequeñas, etc.), o bien para dar capacidad complementaria a la capa general o macro. Se instalan principalmente en puntos de alta demanda de capacidad, para absorber dicha demanda.

3. Sistemas gNB de cobertura de interiores: especializados en cubrir espacios de interiores grandes, con numerosos puntos radiantes de baja potencia, para distribuir la cobertura 5G por dicho espacio interior. Se instalan típicamente en grandes edificios de oficinas, estadios deportivos, metros, etc.

En este contexto, un emplazamiento de la Red de acceso radio 5G estará compuesto por una banda base y varias cabezas remotas y/o antenas activas. El número de cabezas remotas y antenas activas dependerá del número de bandas presentes en el emplazamiento, y del número de sectores.

El software del gNB es común a la banda base, a las cabezas remotas y a las antenas activas, y también es común entre los distintos sistemas de comunicaciones móviles presentes en el emplazamiento (2G, 3G, 4G y/o 5G). Mediante la interfaz NG la estación base se comunica con el Núcleo de red y mediante la interfaz aire con los terminales móviles.

b) Núcleo de red: El núcleo de la red 5G-SA se compone de una serie de funciones de red estandarizadas por el 3GPP que se comunican entre ellas por conexiones tipo SBI (Service Based Interfaces), permitiendo un mallado total en función de las necesidades de cada una de ellas.

Los principios clave de esta arquitectura 5G-SA son:

1. Separar las funciones del plano de usuario (UP) de las funciones del plano de control (CP), lo que permite escalabilidad independiente, evolución e implementaciones flexibles, por ejemplo, ubicación centralizada o ubicación distribuida (remota).

2. Modularizar el diseño de la función, por ejemplo, para permitir un corte de red flexible y eficiente.

3. Permitir que cada Función de Red (y sus Servicios asociados) interactúen con otras Funciones de red, directa o indirectamente a través de un Proxy.

4. Integrar diferentes tipos de acceso, por ejemplo, acceso 3GPP y acceso no 3GPP.

5. Soporta un marco de autenticación unificado.

6. Desacoplar en las funciones de red las funciones de lógica de tipo «stateless» y relacionadas con capacidad de cómputo, de las funciones de estado de tipo «statefull» relacionadas con capacidades de almacenamiento.

7. Permitir la exposición de datos de red de forma segura para el desarrollo de nuevos servicios en base a ellos.

8. Soporte de acceso simultáneo a servicios locales (con requisitos de baja latencia) y servicios centralizados.

9. Permitir y aceptar la itinerancia de tráfico con otras redes, según diferentes modelos de arquitectura.

El conjunto de funciones de núcleo de red definidas por el 3GPP es el siguiente:

1. AMF-Access and Mobility Management Function: función del plano de control de la red 5G. Sus principales funciones son la gestión del registro, la gestión de la movilidad, la gestión de la conexión, y la gestión de diversos aspectos relacionados con la seguridad y autorización de los accesos.

2. SMF-Session Management Function: función del plano de control que se encarga de la gestión de las sesiones (establecimiento, modificación y liberación), gestión y asignación de IP a los terminales de usuario. En resumen, es la responsable de interactuar con el plano de usuario, creando, actualizando o borrando sesiones PDU, a la vez que administra el contexto de la sesión con el UPF.

3. UPF-User Plane Function: función del plano de usuario. Es la responsable del reenvío, enrutamiento e inspección de paquetes, así como de la gestión de la calidad de servicio. Representa el punto de interconexión a la red de datos.

4. PFC-Policy Control Function: es la encargada de proporcionar reglas de políticas a las funciones de red del plano de control, incluyendo network slicing, roaming, gestión de movilidad, o políticas de calidad de servicio 5G. Para la ejecución de las políticas, accede a la información de suscripción del UDR.

5. NRF-Network Repository Function: es la encargada del descubrimiento de los servicios, y mantiene el perfil e instancias de red disponibles. Sus funciones principales son la gestión del servicio, el descubrimiento de servicios, y access token, permitiendo poner en comunicación a dos elementos de la red 5G.

6. SEPP-Security Edge Protection Proxy: es la función de red que permite una interconexión segura entre redes 5G, garantizando la confidencialidad y/o integridad de extremo a extremo entre la red de origen y la de destino, para todos los mensajes de roaming de interconexión 5G.

7. UDM-Unified Data Management: función del plano de control cuyas principales misiones son la generación de credenciales de autenticación, la gestión de identidades de usuario, la gestión de suscripción, la autorización de acceso basado en datos de suscripción, y almacenamiento y gestión de las funciones de red que dan servicio al usuario. El UDM utiliza los datos de suscripción almacenados en el UDR.

8. UDR-Unified Data Repository: es el repositorio unificado de datos de usuario. Estos datos se estructuran en diferentes categorías o tipos, y son accesibles a las diversas funciones de red mediante una serie de servicios expuestos para la gestión y consulta de los mismos (UDM, PCR, NRF…, entre otros).

9. AUSF-Authentication Server Function: es la función del plano de control de la red 5G que se encarga de la autenticación del usuario.

10. CHF-Charging Function: la funcionalidad de tarificación reside en el tarificador convergente (CCS, Converged Charging System), que ofrece las funcionalidades de tarificación online y offline. Entre sus funciones, está el OCF (Online Charging Function), para realizar el control online de las sesiones de datos, el CDF (Charging Data Function), para construir un CDR con la información de red recibida, el ABMF (Account Balance Management Function), para la gestión del saldo y controles de consumo, el RF (Rating Function), función para establecer un precio al uso recibido (tanto online como offline), y el CGF (Charging Gateway Function), para generar CDRs tarificados.

11. NEF-Network Exposure Function: proporciona un medio para exponer, de forma segura, los servicios y capacidades ofrecidos por las funciones de red de 5G.

12. 5G-EIR-5G-Equipment Identity Register: es una funcionalidad opcional que ofrece la capacidad de chequear el estatus de la identidad del terminal (IMEI) y comprobar que no se encuentre en una lista negra.

c) Transporte-Backhaul (SecGW): El Security Gateway (SecGW) proporciona el cifrado del tráfico del plano de control y del plano de usuario entre los entornos de Acceso Radio y de Núcleo de Red, evitando además exposiciones innecesarias de elementos críticos.

d) Interconexión Roaming: El entorno de Interconexión Roaming es necesario para la comunicación con el resto de los operadores de cara a permitir que un usuario de 5G pueda moverse de manera internacional ininterrumpiendo su servicio de voz o banda ancha.

En la siguiente figura (figura 3) se contiene la representación de un Entorno de Interconexión de Roaming:

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_3.png)

e) Sistemas de Control, Gestión y Operación y Servicios de Apoyo: El proceso de aseguramiento del núcleo de red 5G se apoya en un conjunto de sistemas de apoyo a la operación (OSS) que se muestran en la siguiente figura (figura 4).

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_4.png)

Estos sistemas OSS no forman parte de la prestación del servicio y, por tanto, fallos en su funcionamiento no afectan de forma directa a la disponibilidad de la red ni a la calidad del servicio prestado sobre ella. Sin embargo, la indisponibilidad de estos sistemas afectaría a la capacidad de supervisión, análisis, configuración y planificación de la red descrita en el punto anterior. Desde el punto de vista de la seguridad estos sistemas gestores están segmentados según el suministrador y por tanto una incidencia de seguridad en uno de ellos no afectaría a las funciones de red que no esté bajo el amparo de este OSS.

4. Entornos de red secundarios

Dentro de los entornos de red secundarios, se encuentran las Plataformas de Virtualización, la Infraestructura física, el Edge-Computing y el Network Slicing.

a) Plataformas de Virtualización y Orquestación: Muchos de los elementos de una red 5G son funciones «software» que se despliegan sobre una infraestructura de virtualización (que, a su vez, se compone de hardware y software de virtualización), la cual puede ser dedicada y específica para una función de red, o común para varias funciones (incluso funciones de red de varios suministradores). En este contexto, la infraestructura para hospedar las funciones de red virtualizadas está diversificada tanto geográficamente como por suministradores diferentes.

b) Infraestructura física: Los elementos y funciones de red pertenecientes a los distintos entornos requieren de una infraestructura física donde emplazarlos, cuya naturaleza, disponibilidad y seguridad dependerá obviamente de la criticidad del activo en concreto. Esta infraestructura física otorga a los elementos y funciones de red las necesidades básicas para un correcto funcionamiento.

c) MultiAccess Edge-Computing (MEC): El edge computing multiacceso es un tipo de arquitectura o entorno de red que pretende llevar las funciones de procesamiento de tráfico de usuario y cloud computing TI al extremo de la red con el objetivo garantizar el funcionamiento de nuevos casos de uso que requieren una latencia mínima.

En concepto, se define en términos más amplios como una evolución del cloud computing que utiliza las tecnologías móviles y de nube para separar los hosts de aplicaciones del centro de datos donde se encuentran y trasladarlos hacia el extremo de la red. Esto no sólo permite que los usuarios finales estén más cerca de las aplicaciones, sino también que los servicios informáticos estén más cerca de los datos que estas generan.

En este Edge-Computing conviven tanto aplicaciones de terceros, como funciones de red para procesar en el Edge el tráfico de usuario.

d) Network Slicing: Se trata de una forma de arquitectura que ofrece la posibilidad de crear, sobre una infraestructura física de virtualización común compartida, varias redes virtuales personalizadas y aisladas de manera lógica entre sí, otorgando a cada una de ellas una criticidad determinada en función de las necesidades específicas de aplicaciones, servicios, dispositivos, clientes u operadores.

Se prevé que, con esta tecnología, los operadores de redes y servicios 5G puedan implementar una segmentación de red para crear múltiples redes virtuales con diferentes tamaños de conectividad, adaptándose a las necesidades de conexión de los diferentes usuarios, asignado de forma específica los recursos necesarios para garantizar el servicio correcto.

En líneas generales, dentro del concepto network slicing, cada red virtual (o porción de la red) engloba un conjunto independiente de funciones lógicas de red que soportan los requerimientos del caso de uso particular. Cada uno de ellos se optimizará para brindar los recursos y razonamientos matemáticos de red para el servicio y el tráfico que será usado en la segmentación.

En el caso de la tecnología 5G-SA, capacidad, conectividad, variedad, velocidad, cobertura y seguridad se asignarán para satisfacer las demandas específicas de cada caso de uso.
