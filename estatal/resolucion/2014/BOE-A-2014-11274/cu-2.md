## Cuarto. Sistema de comunicaciones.

El establecimiento de las comunicaciones entre el SG-SCECI, los EMCC y en su caso los SGdD, deberá satisfacer los siguientes requisitos:

4.1 Alcance.

Comprenderá todos los equipos, redes e instalaciones necesarios para establecer la comunicación entre los equipos EMCC, en su caso los SGdD, hasta la interfaz con los equipos del SG-SCECI en el Punto de Presencia del proveedor del servicio de comunicaciones (PoP) en las instalaciones principal y de respaldo del Operador del Sistema. El Operador del Sistema indicará a cada proveedor del servicio de gestión de la demanda de interrumpibilidad, la localización de las instalaciones del Operador del Sistema que le correspondan.

Los equipos terminales situados en los PoP serán parte del sistema de comunicaciones.

4.2 Características generales.

El sistema de comunicaciones entre el SG-SCECI, los EMCC y en su caso los SGdD, atenderá a lo siguiente:

a) Permitirá el establecimiento de canales de comunicación permanentes para uso exclusivo del Protocolo de Comunicación.

b) Existirá comunicación redundante, sin punto único de fallo, entre cada equipo EMCC, en su caso los SGdD, y el PoP del proveedor del servicio de comunicaciones, localizado en las instalaciones principales del Operador del Sistema. Los mecanismos de conmutación entre canales redundantes dispondrán de sistemas de bloqueo que impidan conmutaciones repetidas e intempestivas.

c) En cada momento el EMCC, en su caso los SGdD, podrá comunicar únicamente con el SG-SCECI situado en la instalación principal o redundante del Operador del Sistema.

d) Permitirá en cualquier momento, a iniciativa del SG-SCECI, establecer la comunicación con el EMCC, en su caso los SGdD, desde la instalación principal o de respaldo del Operador del Sistema.

e) Garantizará la integridad y confidencialidad de los datos transmitidos.

f) La comunicación se establecerá mediante protocolos de Internet.

g) Permitirá la asignación de una IP fija a cada EMCC, y en su caso a los SGdD. El esquema de direccionamiento IP será definido por el Operador del Sistema, que también asignará una dirección IP a cada EMCC.

h) Garantizará un ancho de banda mínimo de 1 Mbps, para las comunicaciones desde el EMCC, y en su caso los SGdD, hacia el SG-SCECI, y desde este último hacia el EMCC y en su caso los SGdD.

4.3 Características particulares.

El sistema de comunicaciones de podrá establecer mediante cualquiera de las tecnologías siguientes:

a) Punto a Punto.

Conexión de cada equipo EMCC, y en su caso los SGdD, con el PoP, localizado en la instalación principal del Operador del Sistema, mediante dos líneas de comunicación dedicadas.

Conexión de cada equipo EMCC, y en su caso los SGdD, con el PoP, localizado en la instalación redundante del Operador del Sistema, mediante una línea de comunicación dedicada.

Los canales de comunicación establecidos entre el EMCC, y en su caso los SGdD, con el PoP deberán soportar unicast, multicast y protocolos de routing IPv4 (RFC 1812).

El punto de conexión del sistema de comunicaciones con los equipos del Operador del Sistema localizados en el PoP serán las líneas de comunicación finalizadas en el siguiente interfaz: UIT-T G.703 conector RJ48c.

b) Red Privada Virtual (IP-VPN MPLS).

Conexión de uno o varios equipos EMCC, y en su caso los SGdD, con los PoP mediante el establecimiento de una red privada virtual sobre una infraestructura MPLS, sin conexión a Internet, gestionada por un proveedor de servicios de comunicaciones. La red tendrá seguridad inherente sin necesidad de túneles ni cifrado.

Topología del servicio en estrella, concentrado el tráfico de los equipos EMCC, y en su caso los SGdD, conectados a la IP-VPN, en equipos terminales redundantes situados en el PoP de la instalación principal del Operador del Sistema y en un equipo terminal, no redundante, situado en el PoP de la instalación de respaldo del Operador del Sistema.

El punto de conexión del sistema de comunicaciones con los equipos del Operador del Sistema localizados en los PoP será una interfaz Ethernet IEEE 802.3v y 802.3x o superior con conector RJ45, de los equipos terminales de la red privada virtual situados en los PoP.

Los equipos EMCC tendrán un acceso redundante a la IP-VPN por cualquier tecnología disponible, siempre que garantice la confidencialidad e integridad de la información.

c) Red Privada Virtual (VPN-IPSec).

Conexión de cada equipo EMCC, y en su caso los SGdD, con los PoP situados en las instalaciones del Operador del Sistema, estableciendo una red privada virtual segura a través de Internet, mediante el conjunto de protocolos Internet Protocol Security (IPSec).

Se utilizará IPSec en modo túnel con encriptación. Los túneles IPSec serán iniciados desde el EMCC hacia el SG-SCECI.

Los equipos en ambos extremos del túnel IPSec, tendrán las siguientes características:

IPv4 RFC 791.

RFC 2784 – Generic Routing Encapsulation IP-47 (GRE).

Soporte NAT transversal (RFC 3947).

IPSec IKEv1 (RFC 2401).

Certificado digital (RFC 3280).

– PKI x509.

– IKE v1 RFC 2409.

– AES longitud 128 bits FIPS 197.

– Hash SHA-1 RFC 3174.

– Diffie Hellman grupo 2 mínimo (1024 bits) RFC 3526.

Soporte de protocolos de enrutamiento dinámico RIPv2 RFC 2453.

El Operador del Sistema podrá publicar, en el documento Protocolo de Comunicaciones, instrucciones de configuración complementarias para el establecimiento de los túneles IPSec.

El punto de conexión del sistema de comunicaciones con los equipos del Operador del Sistema localizados en los PoP, será la interfaz de estos equipos con los de los proveedores de servicio de Internet del Operador del Sistema.

La comunicación VPN-IPSec estará disponible únicamente en aquellas localizaciones del Operador del Sistema donde exista acceso redundante a Internet proporcionado por operadores diferentes.

d) Configuraciones especiales.

Se habilita a la Dirección General de Política Energética y Minas para la aprobación, en su caso, de un tipo de acceso específico por parte de un usuario del sistema de comunicación, ejecución y control del servicio de gestión de la demanda de interrumpibilidad (SCECI) a dicho sistema, cuando por causas debidamente justificadas el usuario del sistema no pueda acceder a los requerimientos técnicos especificados en la presente resolución.

4.4 Disponibilidad.

La disponibilidad de las comunicaciones a que hace referencia el artículo 9.7 de la Orden IET/2013/2013, de 31 de octubre, se verificará en los puntos de conexión del sistema de comunicaciones con los equipos del Operador del Sistema localizados en los PoP.

4.5 Responsabilidades.

Los proveedores del servicio de gestión de la demanda de interrumpibilidad serán los responsables de la instalación, supervisión y mantenimiento de los equipos localizados en el Punto de Presencia (PoP) en las instalaciones del Operador del Sistema, para lo que podrán designar a un proveedor del sistema de comunicaciones.

El Operador del Sistema será responsable de ceder espacio físico adecuado y alimentación eléctrica segura, a los equipos de los proveedores del servicio de comunicaciones en el PoP. El Operador del Sistema podrá denegar de forma razonada la instalación de equipamiento del proveedor del servicio en el PoP, solicitar su retirada o sustitución por modelos distintos, cuando las condiciones tecnológicas, de espacio o alimentación eléctrica así lo aconsejen. Las condiciones de cesión de espacio y suministro de energía, podrán ser objeto de un contrato de prestación de servicios entre el proveedor del servicio de comunicaciones y el Operador del Sistema.

Los proveedores del servicio de comunicaciones realizarán sus tareas en el PoP, previa autorización del Operador del Sistema, y de acuerdo con las instrucciones y normas dictadas por este.

4.6 Escalabilidad y seguridad.

El servicio de comunicaciones deberá permitir el aumento tanto del número de usuarios del sistema de comunicación, ejecución y control del servicio de gestión de la demanda de interrumpibilidad (SCECI) como del caudal de los accesos, y deberá garantizar en todo caso la integridad y confidencialidad de los datos transmitidos, debiendo tener establecidos los procedimientos, protocolos o estándares que se implementen en el servicio, para garantizar la seguridad.

4.7 Provisión del servicio de comunicaciones.

El servicio de comunicaciones para el sistema de comunicación, ejecución y control del servicio de gestión de la demanda de interrumpibilidad (SCECI) podrá ser prestado por aquellos proveedores de servicios de comunicaciones que, cumpliendo con las especificaciones que se recogen en la presente resolución, sean designados por los proveedores del servicio de gestión de la demanda de interrumpibilidad.

4.8 Certificación de la Calidad del Servicio.

Se establece la posibilidad de creación de un procedimiento de certificación de la calidad del servicio de comunicaciones que persiga garantizar la mejor prestación posible del servicio de comunicaciones a lo largo del tiempo, mediante la creación y adecuación de los correspondientes manuales de control de calidad que incluyan desde los aspectos técnicos hasta los contractuales relevantes, cuyo adecuado cumplimiento deberá ser auditado por personas o entidades de prestigio reconocido y ajenas tanto al proveedor del servicio de gestión de la demanda de interrumpibilidad como a las entidades contratadas para prestar el servicio de comunicaciones.

La participación en el esquema de certificación de calidad del servicio de comunicaciones así planteado será voluntaria para el proveedor del servicio de gestión de la demanda de interrumpibilidad.
