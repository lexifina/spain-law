## ANEXO II

## Análisis de riesgos a nivel nacional

1. Metodología empleada

Un análisis de riesgos tiene como objetivo identificar y categorizar las principales amenazas sobre las redes y servicios 5G, con la finalidad de determinar medidas correctivas que puedan disminuir sus consecuencias o incluso evitarlas.

Conociendo esta finalidad, el paso siguiente lógico es establecer los medios para lograr dicho objetivo. Un análisis de riesgos ha de realizarse con una metodología estandarizada, holística y un orden consecuente y lógico, pormenorizando cada uno de los aspectos de manera cualitativa y cuantitativa. En caso contrario, el nivel de riesgo calculado podría desvirtuarse y con él, los criterios y prioridades en las medidas de protección y/o acciones clave a llevar a cabo.

Se muestra a continuación las fases seguidas para el análisis efectuado, así como las fuentes de información utilizadas para la metodología utilizada.

a) Identificación y descripción de la arquitectura 5G, los entornos de red existentes en la misma y los activos que la componen, todo ello sujeto a la evolución tecnológica (ver anexo I).

b) Identificación de criticidad para los activos dentro de cada una de las partes o elementos de una red 5G, sean partes o elementos críticos o no de la red 5G en los términos indicados en el artículo 6, apartados 2 y 3, del Real Decreto-ley 7/2022, de 29 de marzo, artículos 5 y 6 y anexo I de este esquema: para poder identificar el impacto de una amenaza en la red, es necesario primeramente determinar la criticidad de cada uno de los activos, basándonos en las cinco dimensiones de seguridad (Confidencialidad, Integridad, Trazabilidad, Autenticidad y Disponibilidad).

c) Identificación de los riesgos de la tecnología 5G y su impacto en los activos identificados: determinar las potenciales amenazas presentes en este entorno específico, clasificándolas por activo e identificando su nivel de riesgo.

d) Identificación de las medidas de seguridad técnicas, organizativas y estratégicas, para paliar o reducir el nivel de riesgo de las amenazas identificadas para cada entorno de red. Su efectividad será directamente proporcional al grado de disminución del nivel de riesgo para una determinada amenaza y activo.

e) Gestión de los riesgos y riesgos remanentes, en aquellas amenazas cuyo nivel sea considerable y no pueda ser disminuido por ninguna medida adicional desde el diseño (ver anexo III).

2. Dimensiones de seguridad que afectan a la criticidad de un activo

De manera estandarizada y ampliamente reconocida, se consideran cinco dimensiones de seguridad a la hora de evaluar la criticidad de los activos dentro de cada una de las partes o elementos de una red 5G, sean partes o elementos críticos o no de la red 5G en los términos indicados en el artículo 6, apartados 2 y 3, del Real Decreto-ley 7/2022, de 29 de marzo, artículos 5 y 6 y anexo I de este esquema, cuando de evaluar la seguridad de una solución es lo que aplica.

Las cinco dimensiones de seguridad son Confidencialidad, Integridad, Trazabilidad, Autenticidad y Disponibilidad.

a) Confidencialidad: La confidencialidad en un activo o una red valora la capacidad de evitar que la información que está contenida en el activo, o en tránsito en la red, sea expuesta a usuarios no autorizados, los cuales no deben tener acceso a ésta y la información ni se pone a disposición, ni se revela a individuos, entidades o procesos no autorizados.

Las medidas de seguridad para garantizar la confidencialidad son diversas, desde la segmentación y el control de acceso, hasta el cifrado robusto de la información. El principal factor a la hora de valorar importancia de la confidencialidad en un activo es la sensibilidad de la información que almacena o transita por el mismo. Es importante tener en cuenta cuando se atiende a este factor, el impacto que puede tener para el resto de la red el hecho de que se comprometa ese activo.

Ejemplos de riesgos que puedan comprometer la confidencialidad son los siguientes: Espiar/interceptar el tráfico/datos de usuario en la red (Man in the Middle/, Eavesdropping), u obtener las credenciales de los operadores, ya sea debido a una errónea configuración de la red, a la ausencia de políticas de segmentación y control de acceso a los activos, o, por ejemplo, a la ausencia de cifrado en interfaces expuestas.

b) Integridad: La integridad es la capacidad de garantizar que los datos de un activo/usuario/red durante su ciclo de vida, ya sea en tránsito o almacenados, son modificados sólo por los agentes autorizados a ello, evitando que fuentes no deseadas puedan cambiar o manipular dichos datos, es decir, que no ha sido alterado de manera no autorizada. Algunas medidas para garantizar la integridad pueden ser la segmentación y el control de acceso, la comprobación del hash en los paquetes, la verificación de integridad de las versiones a instalar o almacenadas, etc.

Ejemplos de riesgos que comprometan la integridad son: Manipulación del tráfico/datos (en tránsito o almacenado) en interfaces expuestas de la red 5G.

c) Trazabilidad: propiedad o característica consistente en que las actuaciones de una entidad (activo/usuario/red/persona/proceso) pueden ser trazadas de forma indiscutible hasta dicha entidad.

Ejemplos de riesgos que puedan comprometer la trazabilidad son los siguientes: pérdida de control de la cadena de generación de información y/o datos o la manipulación y/o borrado de los registros y logs.

d) Autenticidad: propiedad o característica consistente en que una entidad (activo/usuario/red/persona/proceso) es quien dice ser o bien que garantiza la fuente de la que proceden los datos.

Ejemplos de riesgos que puedan comprometer la autenticidad son los siguientes: falsificación de información y/o de paquetes de datos.

e) Disponibilidad: La disponibilidad se basa en el principio de garantizar que los usuarios legítimos tengan acceso ininterrumpido a los servicios y datos dentro del entorno para su correcto funcionamiento y las entidades o procesos autorizados tienen acceso a los mismos cuando lo requieren. Este concepto pretende juzgar la importancia del activo y su solución en la continuidad de negocio de un determinado servicio, recurso o infraestructura. El nivel de riesgo de afectación a la disponibilidad se suele unir al número y al tipo de usuarios afectados que supondría la caída del servicio.

Para garantizar la disponibilidad se pueden tomar diversas medidas entre las que están la creación de soluciones de backup, la redundancia/resiliencia de los activos, la capacidad de mitigación frente a ataques DDoS, o los procedimientos eficaces de restauración del servicio tras la caída.

Dentro del entorno, algunos riesgos que puedan comprometer la disponibilidad son los siguientes: Ataques como denegación de servicio a la función de red, a la infraestructura de virtualización, o la infraestructura física, o catástrofes naturales, terrorismo, etc.

3. Determinación de la criticidad de los activos

Se procede, en este apartado, a identificar la criticidad de los activos de una red 5G-SA, teniendo en cuenta las cinco dimensiones de seguridad descritas en el apartado anterior.

1. Se definen tres categorías de criticidad de los activos: BÁSICA, MEDIA y ALTA.

a) Un activo será de categoría ALTA si alguna de sus dimensiones de seguridad alcanza el nivel de seguridad ALTO.

b) Un activo será de categoría MEDIA si alguna de sus dimensiones de seguridad alcanza el nivel de seguridad MEDIO, y ninguna alcanza un nivel de seguridad superior.

c) Un activo será de categoría BÁSICA si alguna de sus dimensiones de seguridad alcanza el nivel BAJO, y ninguna alcanza un nivel superior.

a) Red de acceso.

– gNB: Criticidad media.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_5.png)

Los nodos de acceso radio se encuentran ubicados, en su gran mayoría, en emplazamientos en lugares públicos no seguros. Esto hace que su exposición a ataques in situ aumente. La afectación de una celda puede suponer la interrupción de servicio en un área reducida, afectando a una cantidad de usuarios pequeña, además de poder ser soportado su tráfico por alguna otra estación base cercana, por lo que se considera que la criticidad es baja en cuanto a disponibilidad.

Estos nodos no almacenan datos de usuario. A pesar de ello, si se produce un ataque Man in the Middle (MitM), podría verse comprometido el tráfico no cifrado (afectando sólo a los pocos usuarios conectados a ese nodo), además de poder manipular los paquetes en curso si no existe verificación de integridad. Debido a la dificultad de realizar este ataque en el escenario descrito, a la confidencialidad, integridad y autenticidad se le otorga una criticidad media.

b) Núcleo de red.

– AUSF, UDM y UDR: Criticidad alta.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_6.png)

Un atentado contra la confidencialidad/integridad en estos activos puede suponer la exposición de información crítica del usuario en la red (claves de autenticación, integridad y cifrado, datos de provisión de los usuarios y sus identidades, etc.).

La obtención de esta información tendría un impacto muy alto debido a que es información asociada directamente a la tarjeta SIM de los clientes, y su exfiltración puede conllevar no sólo a una exposición de las comunicaciones de los usuarios, sino también a la pérdida de imagen del operador de redes y servicios 5G, y puede implicar la sustitución de las tarjetas SIM comprometidas. Por dichos motivos, la criticidad del activo en lo que a confidencialidad e integridad se refiere es alta.

Además, al ser un elemento centralizado que recibe las peticiones de autenticación de todos los usuarios de la red, en caso de no desplegarse con una solución correcta que garantice su resiliencia y continuidad de negocio, una disrupción en el mismo puede provocar la caída completa de la red. Por tanto, en cuanto a disponibilidad, también tiene una criticidad alta.

En el caso de la autenticidad y trazabilidad se le otorga una criticidad alta.

– AMF, NRF y NEF: Criticidad alta.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_7.png)

• NRF: Criticidad alta.

Este elemento dispone de un mapa de toda la red, nodos y servicios. Un acceso no autorizado puede dar el detalle del despliegue de la red, los enrutamientos, DNS, slices, servicios, etc. Además, la alteración de su configuración puede provocar errores de comunicaciones internas en la red. Dadas estas razones, la confidencialidad e integridad del NRF se consideran de criticidad alta.

Sin embargo, dado que en casos de caída de NRF, el AMF guarda en caché los destinos de forma indefinida, hace que su criticidad en cuanto a disponibilidad sea baja.

En el caso de la autenticidad y trazabilidad se le otorga una criticidad alta.

• AMF: Criticidad alta.

Al ser el encargado de gestionar la movilidad de los usuarios, un ataque o acceso no autorizado puede permitir obtener o exfiltrar información delicada (identidades del usuario, localización a nivel de Tracking Area, e incluso el identificador del nodo donde se encuentra el cliente cuando el terminal está en modo conectado).

Por este motivo, riesgos de exfiltración más que de alteración de información, se considera alta la criticidad en cuanto a confidencialidad, y media en cuanto a integridad.

Por otra parte, dado que únicamente atiende a una parte de los usuarios de la red, se considera que la criticidad en cuanto a disponibilidad es media.

En el caso de la autenticidad y trazabilidad se le otorga una criticidad media.

• NEF: Criticidad media.

Este elemento es el responsable de garantizar la autenticación, confidencialidad e integridad de las comunicaciones de entidades externas al Núcleo de red, contra alguna de las funciones internas del Núcleo de red (interfaz SBI). Un acceso no autorizado, puede permitir la modificación de alguna política de seguridad entre las funciones externas al Núcleo de red y las internas. Sin embargo, esta función de red no se utiliza para la prestación de servicio generalista a los usuarios 5G. Por ese motivo, la confidencialidad e integridad tienen una valoración media.

Si atendemos a la disponibilidad, la caída de este equipo, en caso de no tener redundancia, sólo afectaría a aquellos servicios que necesiten comunicación externa con los elementos del Núcleo de red, lo que no tendría una afectación considerable y por eso se considera baja.

En el caso de la autenticidad y trazabilidad se le otorga una criticidad media.

– SMF/UPF y PCF: Criticidad baja.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_8.png)

En esta categoría se agrupan los siguientes elementos, en los que, en general, una afectación a los mismos no tiene un impacto notable en la prestación del servicio 5G, por lo que su valoración de criticidad es baja.

• SMF/UPF: Criticidad baja.

El SMF se encarga del establecimiento de las sesiones, y el UPF se encarga de la gestión del plano de usuario: desencapsula el tráfico del usuario que llega del acceso radio y lo encamina a otras redes de datos. Un acceso no autorizado puede desactivar la sesión de un usuario, pero se establecería en otro SMF/UPF. Además, el uso del SecGW entre la Red de acceso y el Núcleo de red imposibilita un MiTM, lo que hace que su criticidad atendiendo a la confidencialidad, integridad, autenticidad y trazabilidad sea baja.

Por otra parte, atendiendo a la disponibilidad, su criticidad se considera baja igualmente, debido a que un usuario no puede estar más que en un AMF, pero sus sesiones sí pueden estar en diversos SMF/UPF.

• PCF: Criticidad baja.

Este elemento no es especialmente crítico para los servicios de datos, siempre y cuando, además, los terminales sean de tipo data-centric. Aunque dispone de las políticas relacionadas con los servicios y la tarificación, los AMF/SMF siempre son configurados para poder dar servicio sin este elemento. Un efecto normal de caída de PCF en servicio de datos es no poder tarificar online a los clientes. La eventual afectación sobre el servicio de voz puede mitigarse mediante servicio de voz por 2G/3G. Por dichos motivos, su criticidad atendiendo a los diferentes criterios sería baja.

c) Transporte-Backhaul.

– SecGW: Criticidad alta.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_9.png)

La red de transporte conecta los elementos del Núcleo con los de la Red de acceso. Un posible corte de esta en uno de sus tramos hace que solamente la zona de nodos de acceso radio en la que se produce dicho corte se vea afectada y, de forma temporal, se puede forzar a que el tráfico no pase por este elemento en dicha zona, con lo que la disponibilidad tiene una criticidad media.

Por otro lado, comprometer un sitio o interceptar el tráfico conlleva a una fuga de información importante, dado que es el elemento encargado de cifrar la información en tránsito que llega desde una gran cantidad de nodos. Por ello, atendiendo a la confidencialidad se le asigna una criticidad alta. Estando cifrada esta comunicación, alterarla es complicado, por lo que la criticidad en cuanto a integridad, autenticidad y trazabilidad se considera media.

d) Interconexión Roaming.

– SEPP: Criticidad alta.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_10.png)

Este elemento permite el intercambio de señalización con otras redes en escenarios de itinerancia. Pese a ser un elemento expuesto a otras redes, únicamente transporta tráfico de usuarios de roaming, y no el de los usuarios nacionales. Este hecho hace que la criticidad en cuanto a disponibilidad, autenticidad y trazabilidad sea media.

Por otra parte, la confidencialidad de las comunicaciones y su integridad sí son aspectos importantes (sobre todo la primera), pues es un entorno en el que, en caso de carecer de las protecciones adecuadas, se puede obtener o exfiltrar información sensible de los usuarios, incluso de aquellos que no están en roaming. Esto hace que la criticidad en cuanto a confidencialidad sea alta.

Es un entorno que la industria y los organismos de estandarización se ha tomado muy en serio, donde, de manera nativa, los fabricantes van a incluir capacidades de configuración de cifrado e integridad, lo que permite que, si el tráfico va cifrado, atentar contra la integridad sea más complicado, otorgándose una criticidad media.

e) Sistemas de control y gestión y servicios de soporte.

– GER: Criticidad alta.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_11.png)

Estos elementos permiten una correcta operación de los elementos que conforman el entorno de red 5G. Pueden gestionar todo un entorno de red, intercambiando mensajes de configuración que pueden dar órdenes fraudulentas a los equipos, o incluso transportar credenciales.

Por tanto, se considera que la integridad, confidencialidad, autenticidad y trazabilidad de este elemento es alta.

Sin embargo, una interrupción o falta de comunicación con la red por parte de los Sistemas de gestión no ocasiona una caída de esta, considerando que la disponibilidad es de criticidad baja.

f) Infraestructura de virtualización /orquestación.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_12.png)

– Infraestructura de virtualización: Criticidad alta.

Todos los elementos del Núcleo de red 5G se encuentran desplegados sobre una Infraestructura virtualizada. Esto implica que cualquier ataque que consiga una disrupción de su funcionamiento, poder controlar los nodos de esta, interceptar el tráfico, modificar el funcionamiento, etc., puede tener graves consecuencias en la prestación del servicio, llegando a incluso su interrupción total. Por los motivos descritos, la criticidad en cuanto a confidencialidad, integridad, disponibilidad, autenticidad y trazabilidad es alta, considerándose este un activo crítico dentro de la red.

– Gestión/orquestación de la virtualización: Criticidad alta.

De forma análoga a los Sistemas de gestión/operación y servicios de soporte, lo más crítico en este activo son la confidencialidad e integridad de las comunicaciones y accesos, calificadas de criticidad alta, pues desde los Orquestadores de la virtualización se controlan todos los elementos de la plataforma de virtualización, que podrían ser vulnerados o atentados (por ejemplo, eliminación de CNF, apagado de hardware, etc.). Así mismo se otorga a autenticidad y trazabilidad una criticidad alta.

Sin embargo, una interrupción o falta de comunicación con la red por parte del Orquestador no ocasiona una caída de las plataformas de virtualización, considerando así que la criticidad en cuanto a disponibilidad es baja.

g) Infraestructura física.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_13.png)

– Infraestructura física: Criticidad alta.

La infraestructura física es especialmente vulnerable a los ataques que provocan daños físicos en el equipamiento, robo, cortes de energía, etc. La disponibilidad de esta es fundamental para el funcionamiento de las redes y los servicios, ya que se va a utilizar de base para ubicar muchas funciones de red y sistemas de gestión de toda la red, por lo que el valor de criticidad, en cuanto a disponibilidad, es alto.

La confidencialidad, integridad, autenticidad y trazabilidad de este activo se consideran bajas, dado que no representa un riesgo para la información o las comunicaciones en sí misma, dependiendo fundamentalmente de los protocolos y mecanismos de control lógicos implementados en las capas superiores (infraestructura de virtualización, aplicaciones, etc.), con objeto de evitar la obtención de información si alguien se hace con un activo.

Cuadro resumen: tabla de criticidad de activos

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_14.png)

4. Clasificación de activos en función de la criticidad

En base a los análisis anteriores y a las aportaciones realizadas por los operadores de redes y servicios 5G, se ha identificado un conjunto de elementos calificándolos con importancia crítica para la operación de las redes 5G, para su configuración o gestión, o de los servicios prestados por las mismas.

Tal y como se ha recogido en el apartado anterior, todos los activos de criticidad alta del entorno primario de red pertenecen al Núcleo de red. No obstante, desde el punto de vista de la criticidad, no es posible considerar el Núcleo de red como un bloque homogéneo. Por ello, se considera aplicable un tratamiento diferenciado en relación a las medidas conducentes a garantizar la disponibilidad de los servicios que ofrecen.

Así pues, el Núcleo de red está compuesto de diversas funciones de red (o Network Functions, NF) que se despliegan en Infraestructuras virtualizadas independientes de la propia función de red. La clasificación considera cuáles de estas entidades son más críticas no sólo desde el punto de vista de redundancia, sino también del posible impacto de accesos no autorizados o ataques desde otras redes.

Además, se tiene en cuenta los posibles accesos no autorizados a la Infraestructura virtualizada sobre la que se despliegan estas funciones de red, y se establece una importancia relativa entre las distintas entidades, recalcando que, para obtener un servicio completo, todas ellas son necesarias.

a) Criticidad alta.

El riesgo que más comprometería el servicio 5G sería un acceso no autorizado al entorno AUSF/UDM/UDR. En el AUSF están las claves de autenticación que permiten el acceso a cualquier comunicación radio cifrada, y en el UDM/UDR se encuentran todos los datos de provisión de los usuarios y sus identidades, y precisamente el 3GPP ha incluido el uso del SUCI (identidad IMSI cifrada) para evitar que esa identidad viaje por el interfaz radio, ya que disponer del SUPI de un usuario es el primer paso para cualquier otro ataque. Se considera sin duda que estas son las funciones de red más críticas dado que el impacto de obtener las claves y las entidades es duradero (al estar asociado a las claves de la SIM de los clientes). La pérdida de imagen de un operador de redes y servicios 5G ante una intrusión en estas funciones de red sería enorme y podría implicar la sustitución de las SIMs comprometidas. No obstante, el diseño de red permite proveer servicio sin ningún impacto ante fallo doble de instancias de cualquiera de estos nodos.

Además de los anteriores, se consideran de criticidad alta, entre otras, las siguientes funciones:

i. NRF: este elemento dispone de un mapa de toda la red, nodos y servicios. Con la información del NRF se dispone de todo el detalle del despliegue de la red, enrutamientos, DNNs, slices, servicios, etc. Además, un acceso no autorizado permitiría paralizar el servicio 5G ya que todas las funciones de red consultan a esta entidad para conocer las funciones de red destino que dispone del servicio requerido. No obstante, las funciones de red tienen cacheada la información de NRF, lo que permitiría mitigar temporalmente el ataque. A mayores, el diseño de red permite proveer el servicio sin ningún impacto ante fallo doble de instancias de este nodo.

ii. SEPP: permite el intercambio de señalización con otras redes para escenarios de itinerancia en la red propia, o en la de otras redes de terceros. Es un elemento expuesto, aunque los suministradores 5G han desarrollado un número elevado de funcionalidades para garantizar su seguridad e integridad. Adicionalmente, ha de garantizarse el aislamiento entre los dominios internos y externos.

iii. AMF: es el encargado de la gestión de la movilidad. Un ataque o acceso no autorizado al mismo, permitiría obtener información muy delicada (identidad del usuario, localización a nivel Tracking Area, e incluso gNB-id donde se encuentra el cliente cuando su terminal está en modo connected), con posibilidad de rastrear el movimiento de usuarios, y sus procedimientos de señalización relacionados con la movilidad y gestión de sesiones. Estos elementos se despliegan en modo pool y se dimensionan para soportar de forma simultánea fallo de un nodo de cada pool.

b) Criticidad media.

En esta categoría de criticidad media se incluye la función NEF.

c) Criticidad baja.

En esta categoría, nuevamente, de mayor a menor criticidad, se indica:

i. SMF/UPF: SMF se encarga de la gestión de las sesiones (establecimiento, modificación y liberación), la gestión y asignación de IP a los terminales de los usuarios, etc. También es responsable de interactuar con el plano de usuario creando, actualizando o borrando sesiones PDU, así como de administrar el contexto de la sesión con el UPF, mientras que el UPF gestiona el plano de usuario. Estos elementos están mucho más redundados que los AMFs anteriormente descritos, y un acceso no autorizado podría desactivar la sesión de un usuario, aunque esta se establecería en otro SMF/UPF. El plano de usuario o tráfico real de clientes se encamina, en general a otras redes (internet/intranet) que son de seguridad más baja, por lo que un atacante de plano de usuario tiene más fácil comprometer el servicio atacando el servidor destino o incluso el terminal.

ii. PCF: no es especialmente crítico, ya que los AMF/SMF se configuran para poder dar servicio sin este elemento, afectando, eventualmente, a la tarificación online de los clientes.

d) No críticos.

Los elementos CHF, NWADF y 5G-EIR no se consideran críticos para prestación del servicio 5G debido a que, en caso de caída o indisponibilidad parcial o total de cualquiera de ellos, los clientes no deberían verse afectados en el servicio.

5. Identificación de amenazas y riegos en la tecnología 5G

En el artículo 9 del Real Decreto-ley 7/2022, de 29 de marzo, se especifica la necesidad de identificar los factores de riesgo a analizar en función de la evolución tecnológica, la incorporación de nuevos avances, funcionalidades y estándares tecnológicos, la situación del mercado de comunicaciones electrónicas y del de suministros y de la aparición de nuevas amenazas y vulnerabilidades.

Los siguientes apartados recogen las tareas realizadas.

5.1 Criterio de identificación del riesgo de un ataque.

Para calcular el nivel de riesgo de seguridad que introduce una amenaza, utilizamos tres factores atendiendo a las siguientes fórmulas:

Nivel de riesgo = (Probabilidad de ocurrencia) × (Impacto en la red)

donde, a su vez,

(Impacto en la red) = (Criticidad del activo) × (Factor de escalado)

Se define, seguidamente, los conceptos empleados:

a) Probabilidad de ocurrencia: Se realiza una valoración en base a los siguientes parámetros:

i. Grado de exposición del activo a la vulnerabilidad: da una medida de lo expuesto que se encuentra el elemento analizado a nivel físico o lógico, y el nivel de accesibilidad/facilidad que pueda tener el atacante de cara a ejecutar la amenaza.

ii. Complejidad o conocimientos para desarrollar el ataque: la probabilidad de ocurrencia aumenta en el caso de que el ataque se pueda realizar sin muchos conocimientos técnicos y el entorno de ataque sea sencillo de implementar o se usen herramientas automatizadas.

iii. Conocimiento público de la vulnerabilidad: un ataque es más probable cuanto más conocido es a nivel de comunidad. En el caso de que la vulnerabilidad esté poco difundida o se maneje solamente en ciertos círculos (como por ejemplo suministradores 5G u operadores de redes y servicios 5G), su explotación será menos probable.

iv. Rastro que deja el ataque: en caso de que el ataque se realice por fuerza bruta o dejando trazabilidad en las redes, será menor la probabilidad de que existan atacantes dispuestos a aprovechar la vulnerabilidad. Se trata de casos en los cuales no pueda realizarse suplantación de identidad.

v. Beneficio obtenido con el éxito del ataque: valor económico, reconocimiento, relevancia, etc., de la consecución del ataque.

Los posibles valores de la probabilidad de ocurrencia son Muy Alto, Alto, Medio, Bajo.

b) Impacto en la red: de forma similar a la probabilidad de ocurrencia, se utiliza una valoración cualitativa para medir el impacto que podría tener el ataque en la red.

Para evaluar el servicio y dar una valoración del impacto se utilizan los siguientes parámetros:

i. Criticidad del activo: concepto mencionado anteriormente, que engloba la confidencialidad, la integridad, la disponibilidad, la autenticidad y la trazabilidad.

ii. Factor de escalado: identifica la importancia y/o alcance del ataque a nivel de afectación de la red. Toma en consideración tanto el alcance (número de usuarios que pueden ser impactados), como el tipo de impacto del ataque (fuga de credenciales, disminución de disponibilidad, etc.).

Los posibles valores del Impacto en red del ataque son: Muy Alto, Alto, Medio, Bajo, teniendo en cuenta los criterios anteriores.

c) Nivel de riesgo: Es el resultado de las dos variables anteriores siguiendo la fórmula descrita arriba.

Los posibles valores del nivel de riesgo son: Crítico, Alto, Medio, Bajo.

5.2 Matriz de riesgos.

Atendiendo a las consideraciones del apartado anterior, se presenta la matriz genérica que caracteriza los niveles de riesgo que se analizan posteriormente en este documento.

![imagen](https://www.boe.es/datos/imagenes/disp/2024/106/8715_14352171_15.png)

6. Amenazas o riesgos en una red 5G SA

Una vez identificados los activos y caracterizada su criticidad, el siguiente paso en el análisis de riesgos es evaluar las amenazas o posibles ataques a las que están expuestos cada uno de estos activos de red 5G SA.

Es importante destacar que una misma amenaza puede tener distinto nivel de riesgo en función del activo o entorno sobre el que se evalúe, de cara a establecer las prioridades correctas de acciones mitigadoras que permitan incrementar, en una misma línea temporal, la seguridad de la solución de la manera más eficiente posible.

A continuación, se detallan las amenazas o riesgos en una red 5G SA:

a) Actividades maliciosas debidas a accesos indebidos o maliciosos a la gestión, extracción de información sensible o modificación no autorizada de parametrización que provoque la indisponibilidad del elemento.

Se trata de aquellas acciones llevadas a cabo por atacantes internos o externos que van dirigidas a los elementos o funciones de red e infraestructura con la intención de robar información, alterarla o destruir, mediante configuración, un objetivo específico.

En este bloque se engloban, entre otras, las siguientes amenazas:

i. Intrusiones en la red con el objetivo de obtener información, a través de accesos maliciosos, movimientos laterales, escalado de privilegios, por falta de políticas de seguridad robustas (ausencia de control de acceso, autenticación, autorización, segmentación, hardening, etc). Destaca, entre otros la obtención de credenciales de usuarios operadores, información sensible de clientes (datos, identificadores de usuario, claves de autenticación, cifrado e integridad), o información útil de configuración de red (puertos, versiones, etc.), que sirva como vector de información adicional para realizar ataques de mayor impacto.

ii. Modificación malintencionada y no autorizada de parametrización o configuración de red que pueda provocar indisponibilidad parcial o total del servicio en el activo o la red, así como favorecer la exfiltración de tráfico comentada en el punto anterior.

A. Manipulación de configuración o parametrización que afecte al funcionamiento del equipo (políticas de enrutamiento de tráfico, configuración de DNS, sesiones de usuario, imágenes de funciones de red virtuales, etc.)

B. Manipulación de configuración de seguridad del equipo (políticas de seguridad, servicios ofrecidos en el aplicativo y sistema operativo, algoritmos criptográficos, reglas de acceso) y creación de puertas traseras.

C. Ejecución de forma intencionada o inconsciente de software/código malicioso (SQL, XSS injection, rootkits, malware/ransomware, etc.)

iii. Explotación de vulnerabilidades en hardware o software, que permitan un acceso simple y eficaz para poder ejecutar las amenazas comentadas en los dos puntos anteriores (vulnerabilidades conocidas/CVEs, nuevas vulnerabilidades y de zero-day).

b) Compromiso de las comunicaciones o datos de usuario a través de la captura, interceptación, secuestro de tráfico de servicio o su modificación:

Esta categoría recoge las acciones realizadas para espiar, interrumpir o alterar las comunicaciones o datos de usuario en el plano de servicio, sin su consentimiento.

Las principales amenazas dentro de esta categoría serían:

i. Espionaje de comunicaciones de un determinado usuario en entornos con alto nivel de exposición como es el caso del acceso radio o la interconexión de Roaming.

ii. Obtención de información sensible de los usuarios (identificadores de usuario, localización, servicios, etc) en interfaces expuestos que puedan ser utilizados como vectores de información para realizar ataques de mayor impacto.

iii. Manipulación de las comunicaciones en interfaces expuestos a través de actividades Man in The Middle (MiTM) y/o de los datos de usuario, siendo posible provocar acciones ilegales tales como fraude, suplantación de identidad, etc.

c) Denegación de Servicio (DoS).

Esta categoría recoge aquellas acciones, actividades o incidencias malintencionadas o no que puedan provocar una disrupción total o parcial en el equipo, causando una afectación a los usuarios de la red. Las principales amenazas dentro de esta categoría serían:

i. Ataques volumétricos de denegación de servicio (DoS/DDoS): Inundación de tráfico a las interfaces expuestas de los activos (dispositivos de usuario, interconexiones, etc.) buscando la sobrecarga de las capacidades de los elementos, con el objetivo de provocar un malfuncionamiento/disrupción en la red.

ii. Ataques dirigidos a usuarios específicos con el objetivo de provocar su indisponibilidad en la red (por ejemplo, ataques de interferencia o desregistro de la red).

iii. Daños no intencionados por los operadores por errores de configuración: Recoge las acciones no intencionadas por parte de un operador con acceso a la gestión de un activo que puedan resultar en un fallo o la reducción de funcionalidad de este, como, por ejemplo, la configuración pobre/errónea de los activos de red y sus capacidades de seguridad (aislamiento, bastionado, segmentación, etc.) o error en su gestión o manipulación por desconocimiento o falta de formación o diligencia.

iv. Mal funcionamiento del elemento: Engloba el malfuncionamiento «nativo» (por causas ajenas a la configuración del activo) que pueda provocar una disrupción total o parcial de su servicio.

d) Amenazas físicas.

Está dirigido a destruir, inutilizar, alterar o robar activos físicos de la infraestructura física que alberga la funciones/elementos de red.

Entre las amenazas principales destacan el sabotaje o terrorismo contra los elementos críticos de equipamiento de red, las catástrofes naturales, el malfuncionamiento de la red de energía y la posible sustracción de equipamiento de red para la extracción de información sensible y su posterior explotación.

e) Escasa formación y concienciación de los empleados en materia de ciberseguridad, así como mala praxis en la gestión de la evolución de los riesgos identificados.

Por un lado, el hecho de que los empleados no estén concienciados en materia de seguridad aumenta la probabilidad de ocurrencia de incidentes tales como ataques ransomware y otro tipo de malware. La falta de formación en materia de seguridad y operación aumenta la probabilidad de errores de configuración por desconocimiento que expongan los activos a riesgos innecesarios.

Además de todo esto, si no se lleva a cabo un buen procedimiento de gestión de riesgos, controlando su evolución en la red, será imposible plantear un plan de prioridades y ejecutar las medidas de seguridad de manera eficiente.
