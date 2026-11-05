## ANEXO III

## Gestión de riesgos a nivel nacional

Una vez identificadas en el anexo II las distintas amenazas que afectan pormenorizadamente a las redes y servicios 5G, y con ello, la situación inicial de riesgo, la siguiente fase es prever aquellas medidas de seguridad necesarias para solventar, disminuir o paliar los riesgos identificados.

Estas medidas son:

1. Medidas de seguridad genéricas:

1.1 Configuraciones de seguridad para el equipamiento:

1.1.1 Configuraciones relacionadas con la identificación, autenticación, control, auditoría y monitorización en el acceso al plano de gestión de los nodos. Los nodos deben ser configurados con:

a) Políticas de gestión de identidad, permitiendo garantizar tanto la autenticación (verificar que quién accede es quién dice ser), como la autorización (acceder solo con los privilegios que sean estrictamente necesarios) cuando se accede a los nodos.

b) Políticas de gestión del ciclo de vida del usuario.

c) Capacidades de trazabilidad y políticas de auditoría, permitiendo que quede registrado todos los accesos (quién y cuándo se conecta y desconecta de los nodos), así como los comandos ejecutados y las alarmas que identifican un posible fallo en el equipo.

d) Buenas prácticas de seguridad cuando se definen y gestionan las credenciales y accesos de los usuarios, siempre forzando que las credenciales sean robustas.

e) Capacidad de ser configurados de tal manera que no den información detallada en el caso que falle el acceso y se establezcan políticas de bloqueo que dificulten la obtención de credenciales.

1.1.2 Bastionado:

a) Autoprotección de los nodos, asegurándose que solo estén activos los servicios necesarios para su correcto funcionamiento.

b) Los nodos deben tener la capacidad de separar el interfaz de gestión del de servicio, ya sea a través de un interfaz físico o lógico.

c) Los nodos deben ser capaces de detectar y manejar los paquetes malformados manteniendo los servicios sin afectación.

d) Los nodos deben ser capaces de hacer frente a altos volúmenes/picos de tráfico teniendo mecanismos de autorregulación para evitar el colapso de su CPU.

e) Capacidad adicional de proteger la información crítica y sensible que esté almacenada.

f) Los nodos/elementos de la red deben estar configurados de manera que no se permita iniciar a través de dispositivos de memoria no autorizados.

g) Los nodos deben configurarse de manera que no se pueda realizar una explotación maliciosa de las APIs que expongan.

1.1.3 Realización de pruebas de seguridad periódicas. Son necesarias para estudiar si han aparecido nuevas vulnerabilidades para los componentes del activo.

1.2 Seguridad de arquitectural y funcional.

1.2.1 Planos de red diferentes, así como áreas o ambientes de red con distinto nivel de exposición, deben ser aislados.

1.2.2 Control de flujo: Capacidad de limitar el tráfico a ciertas direcciones IPs, Protocolos, Aplicaciones, para evitar sobrecargar el enlace haciendo que un ataque sea más complicado de llevar a cabo.

1.3 Medidas de Seguridad en la Infraestructura Física:

a) Registro, validación y control de las autorizaciones de acceso físico a los emplazamientos críticos.

b) Controles de accesos físicos, mediante medios electrónicos y/o mecánicos, a las centrales de red y edificios relevantes.

c) Vigilancia física y seguridad electrónica del emplazamiento crítico.

d) Sistemas de seguridad electrónicos instalados y mantenidos en emplazamientos críticos.

1.4 Concienciación de seguridad hacia los empleados y la cadena de mando.

1.5 Formación de empleados en tecnología, seguridad y procesos.

1.6 Implementación de procesos claros de gestión de incidentes, teniendo un registro del histórico de incidentes propios y actualizado el conocimiento con los incidentes de la industria.

2. Medidas de seguridad específicas relacionadas con una red 5G.

2.1 Control de software:

a) Garantizar la integridad de la actualización del software antes de ser instalada, evitando la inyección de códigos maliciosos, troyanos o versiones no legítimas (manipuladas por un tercero).

b) Garantizar que no existan puertas traseras.

c) Garantizar que no existan vulnerabilidades (CVE) explotables conocidas de riesgo alto en el momento de despliegue del producto en planta.

d) Cumplimiento con certificaciones de seguridad reconocidas internacionalmente para los equipos.

2.2 Debe configurarse cifrado e integridad de las comunicaciones entre el terminal y la red a ambos niveles AS (Access Stratum)/NAS (Non Access Stratum), para proteger la privacidad del usuario en el interfaz aire. Esta medida se activa tanto en la RAN (AS), como en el Núcleo de Red (NAS).

2.3 Debe configurarse cifrado e integridad de las comunicaciones en el plano de control y en el plano de usuario entre el nodo de acceso radio (RAN) y el Núcleo de Red.

2.4 La privacidad de los usuarios debe ser garantizada en el interfaz aire.

2.5 Deben ser corroboradas las mejoras en los algoritmos de autenticación entre el terminal del usuario y la red que vienen de manera nativa con la tecnología 5G SA.

2.6 Mejoras nativas en los algoritmos de autenticación entre el dispositivo del usuario y la red, para garantizar mutuamente que la comunicación es legítima.

2.7 Los diferentes elementos que manejan el tráfico de señalización deben tener medidas para evitar la suplantación de los propios elementos de red en la red de roaming, así como la de los usuarios que no están en roaming.

2.8 La confidencialidad, integridad y autenticación deben ser garantizadas en las comunicaciones entre un operador origen y destino, usando protocolos/equipamiento/soluciones seguras (SEPP). La implementación de este requisito y su alcance dependerá de la estandarización final del protocolo a utilizar.

2.9 Es necesario establecer las políticas de seguridad correspondientes de cara a exponer en la interconexión únicamente los interfaces y mensajes necesarios para el servicio, evitando dar información innecesaria que pueda ser utilizada de forma fraudulenta.

2.10 Aislamiento de funciones de red virtualizadas: Clasificación de los diferentes elementos virtualizados en la infraestructura de acuerdo con diferentes niveles de exposición y la criticidad del elemento.

2.11 Aislamiento de tráficos: Diseño seguro de la arquitectura de virtualización para garantizar el tráfico necesario para el funcionamiento de la capa de virtualización, de esta forma la operación/funcionamiento de la red será garantizado.

2.12 Es necesario seguir las pautas de los Requisitos/Configuraciones de Seguridad del Equipamiento y Seguridad Arquitectural para todos y cada uno de los elementos que componen la arquitectura de virtualización.

2.13 Monitorización y Detección: Monitorización de la trazabilidad de accesos y comandos ejecutados en los elementos críticos de la red, de cara a poder identificar actividades ilegítimas en el momento de su realización y también de cara al análisis forense de posibles ataques.

2.14 Mitigación: Capacidades que permitan mitigar posibles ataques volumétricos que tengan como objetivo la denegación de servicio en los interfaces muy expuestos.

2.15 Entornos críticos: Las pruebas de funcionamiento de redundancia/recuperación (backup) en entornos críticos deben llevarse a cabo antes del despliegue de la solución.
