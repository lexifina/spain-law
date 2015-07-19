## APÉNDICE INFORMATIVO

5AN1.AP1.1. Arquitectura del sistema.

Debido a la naturaleza de las funciones requeridas para su funcionamiento, el sistema ETCS se encuentra instalado parte en vía y en parte a bordo de los trenes definiendo así dos subsistemas: el subsistema vía, y el subsistema embarcado.

1. Subsistema vía.

Dependiendo del nivel de la aplicación con el que se equipe la vía, el subsistema vía puede estar compuesto por los siguientes componentes:

Eurobaliza: Es un dispositivo de transmisión puntual de información que envía telegramas al sistema ETCS embarcado. Pueden transmitir telegramas fijos (predeterminados) o, conmutables, esto es, variables en función de la señalización.

Las eurobalizas están organizadas en Grupos de Balizas (BG) dentro de los cuales cada baliza transmitirá un telegrama al equipo ETCS embarcado, que circule sobre ellas.

Unidad Electrónica de Línea (LEU): Son dispositivos electrónicos que conectan el enclavamiento con las eurobalizas conmutables. Su función es la de transmitir a las eurobalizas los telegramas variables en función de las condiciones de la señalización.

Centro de Bloqueo por Radio (RBC): Es un sistema informático que elabora los mensajes a enviar, vía radio, al equipo ETCS embarcado en función de las condiciones de la señalización y de la información intercambiada con dicho subsistema embarcado. El principal objeto de estos mensajes es proporcionar autorizaciones de movimiento que permitan a los trenes circular con seguridad por la zona de infraestructura bajo la responsabilidad del RBC.

Puesto de control ETCS (PCE): Puesto que gestiona las aplicaciones de control de ETCS de forma centralizada. El PCE permite al operador establecer y anular «limitaciones temporales de velocidad máxima».

Euroradio (GSM-R): Es un sistema de comunicaciones vía radio que se utiliza para el intercambio de mensajes en ambos sentidos entre los subsistemas ETCS embarcados y los RBC.

Eurolazo o unidad de información previa vía radio: Son dispositivos opcionales para líneas equipadas con Nivel 1. Proporcionan información con antelación al equipo ETCS embarcado, relativa a la próxima señal principal en el sentido de marcha del tren. De momento no son operativos.

2. Subsistema embarcado.

Dependiendo del nivel de aplicación con el que se equipe el subsistema ETCS embarcado, este puede estar compuesto por los siguientes componentes:

Equipo ETCS «básico» embarcado: Es un sistema informático que supervisa y controla el movimiento del tren sobre la base de la información intercambiada con el subsistema de vía. Es suficiente para operar en nivel 1 con eurobalizas.

Sistema de radiocomunicación embarcado (GSM-R): Se utiliza para el intercambio de mensajes entre el equipo ETCS embarcado y los RBC. Necesario para el nivel 2.

Módulos de transmisión específicos para los sistemas nacionales (STM): Hacen las funciones de «traductor» entre los sistemas nacionales implementados en vía y en los trenes, y el equipo ETCS «básico».

5AN1.AP1.2. Niveles de aplicación del sistema.

1. Se denomina Nivel de aplicación del sistema, abreviadamente Nivel, al tipo de integración del equipo embarcado y la infraestructura, que depende fundamentalmente del medio de transmisión y del equipo de vía. Se relacionan ordenados de mayor a menor prioridad.

a) ETCS Nivel 2:

Sistema ETCS operando en una línea controlada por un RBC y equipada con eurobalizas fijas y Euroradio.

b) ETCS Nivel 1:

Sistema ETCS operando en una línea equipada con eurobalizas, fijas y conmutables.

c) ETCS Nivel STM:

Sistema ETCS operando en una línea con un sistema de señalización «nacional». El equipo embarcado incorpora un módulo STM para comunicar con el sistema instalado en la vía. La parada de los trenes y la supervisión de la velocidad se realizan por equipos ajenos al ETCS.

d) ETCS Nivel 0+ASFA:

Sistema ETCS operando en una línea no equipada con ERTMS, pero equipada con ASFA (sistema nacional).

e) ETCS Nivel 0:

Sistema ETCS operando en una línea no equipada con ETCS en servicio.

2. Compatibilidades. Los Niveles 1, 2 y 3 son compatibles de mayor a menor. Esto es, un tren equipado para operar en Nivel 3 puede operar también en Niveles 2 y 1.

Un tren equipado para operar en Nivel 2, puede también operar en Nivel 1.

El sistema ETCS, por medio del STM, puede integrar LZB, EBICAB o ASFA, por tanto mantiene la compatibilidad con la información existente en la vía, correspondiente a dichos sistemas.

El Maquinista, seleccionará en cada momento el Nivel que corresponda a la circulación de su tren y en función del equipamiento de las infraestructuras.

5AN1.AP1.3. Principios del sistema ETCS.

El subsistema embarcado ETCS realiza la supervisión y el control de velocidad y distancia en base a la información que recibe desde el subsistema de vía.

La información más relevante en base a la cual el equipo embarcado realiza estos controles es:

1. Autorización de movimiento (MA)

Es el permiso que recibe el tren, en términos de distancia, cuando se encuentra totalmente supervisado, para circular hasta un punto determinado. Tal distancia es enviada al tren vía RBC o vía balizas.

Las siguientes características forman parte de la MA:

a) El final de autorización es el punto hasta el cual se autoriza al tren para circular.

Cuando la Velocidad meta (velocidad permitida en aquel punto) es cero se llama Fin de Autorización (EOA). Cuando no es cero, se llama Límite de la Autorización (LOA).

b) La velocidad de liberación es la velocidad del tren a la cual se supervisa la aproximación al EOA. El maquinista de forma manual debe regular la velocidad del tren para no sobrepasar el EOA. Si el tren dispone de automatismo de tracción/freno conectado al sistema y está operativo, se encarga en combinación con el ETCS de no sobrepasar el EOA.

c) El Punto de Peligro (DP) es una localización más allá del EOA hasta la que podría llegar la cabeza del tren, sin el riesgo de una situación real de peligro.

d) Una MA puede ser dividida en varias secciones, a cada una de las cuales se le puede asignar un valor límite de tiempo para recorrerla. Cuando expire el tiempo asignado y no se haya recorrido la sección, se podría aplicar una reacción de frenado por parte del equipo embarcado.

La MA puede ser ampliada, recortada o revocada, los nuevos valores recibidos por el equipo embarcado reemplazarán siempre a los anteriores. En el caso de ser revocada, se pierde la MA.

2. Restricciones de velocidad.

La velocidad máxima a la que se permite que un tren circule, está limitada por diversas clases de restricciones de velocidad, llamadas restricciones estáticas de velocidad y además teniendo en cuenta los valores de EOA/LOA de la correspondiente MA.

Estas restricciones estáticas de velocidad son tratadas de la misma forma independientemente del nivel de aplicación de ETCS.

Las Restricciones Estáticas de Velocidad son limitaciones de velocidad impuestas por la infraestructura de la vía, las características del tren, y el modo en que se encuentra el equipo de a bordo.

Las categorías de Restricción Estática de la Velocidad son independientes unas de otras, es decir, una categoría de restricción de velocidad no afecta, ni será afectada, por ninguna otra categoría de Restricciones Estáticas de Velocidad.

Dependiendo del tipo de Restricción Estática de Velocidad, normalmente será necesario utilizar la longitud del tren para asegurar que todo él haya pasado por una Restricción Estática de Velocidad, antes de que pueda tomarse en consideración un aumento de la velocidad. El equipo embarcado se encargará de la compensación por longitud del tren cuando ello sea necesario.

Las categorías de Restricciones Estáticas de Velocidad son:

a) Perfil Estático de Velocidad (SSP).

El Perfil Estático de Velocidad (SSP) es el determinado por las restricciones fijas de velocidad de un determinado tramo de vía. Las restricciones pueden estar en relación, por ejemplo, con la velocidad máxima de la línea, curvas, túneles, puentes.

El Perfil Estático de Velocidad se basa en factores que dependen principalmente de la vía, pero también del tren; como es el caso del tipo de tren, Normal, A, B, etc. La relación entre las características de la vía y del tren determina el Perfil Estático de Velocidad para cada tren.

Si un aumento de la velocidad en un punto del SSP, debe ser retrasado o no en función de la longitud del tren, viene determinado por la información del SSP enviada al equipo de a bordo.

b) Perfil de Velocidad por Carga por Eje.

Se trata de un Perfil de Velocidad no continuo y definido en función de la carga por eje, de forma que para cada sección a la que este tipo de restricción le es aplicable, se especifican los diferentes límites de velocidad y para qué cargas por eje esos diferentes límites serán aplicados.

Es posible que para una misma sección sean aplicadas distintas restricciones de velocidad, dependiendo de la carga por eje.

Los trenes cuya carga por eje sea igual o superior al valor mínimo definido, se ven afectados por la restricción de velocidad dada para tal valor; no así los trenes con una carga por eje inferior.

c) Limitaciones temporales de velocidad máxima (LTV))

La velocidad limitada es una limitación de velocidad transitoria por causa de la infraestructura; por ejemplo para ser utilizada en zonas de obras, etc.

Cuando se superponen parcialmente dos o más LTVs el tren utiliza la limitación de velocidad más restrictiva en la zona en que se superpongan.

Cada LTV tiene un identificador, lo que hace posible su revocación utilizando tal identificador. La LTV será cancelada inmediatamente cuando se reciba la revocación desde el equipo fijo de línea, sin tener en cuenta la longitud del tren. Esta revocación solo puede ser dada por el subsistema vía.

d) Restricción de velocidad relacionada con el tren.

El sistema ETCS tiene en cuenta la velocidad máxima del tren de acuerdo con su velocidad máxima autorizada, o con los datos introducidos en el equipo embarcado, en el caso de que estos puedan ser modificados.

e) Restricciones de velocidad relacionadas con el modo.

El valor de la restricción de velocidad relacionada con el modo será determinado por el valor nacional correspondiente o por los valores correspondientes por defecto si no son aplicables los valores nacionales. Excepción: Para algunos modos de funcionamiento (On Sight y Shunting), el límite de velocidad puede ser dado también por el subsistema vía. El límite de velocidad dado por este subsistema predomina sobre el valor nacional y el valor por defecto.

Con la información de todas las restricciones estáticas de velocidad, el equipo embarcado elabora y supervisa el Perfil de Velocidad Más Restrictivo (MRSP) que debe respetar el tren. El Perfil de Velocidad Más Restrictivo será calculado de nuevo, cuando cambie cualquiera de los elementos sobre los que esté construido.

Selección de perfil de velocidad más restrictivo:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/171/08042_231.png)

3. Otras informaciones de la vía.

Los datos relativos a la infraestructura de vía normalmente van siendo almacenados por el equipo de a bordo de forma que constituyen un mapa especial de los tramos de la ruta que el tren ha de recorrer.

A continuación se incluye una síntesis de estos datos.

a) Condiciones de la Vía.

La función de Condición de la Vía se utiliza para informar al maquinista y al tren, cuando corresponda, de una condición existente por delante del tren.

Las Condiciones de la Vía se envían como datos de perfil (por ejemplo, área donde no está permitida la parada), es decir, se especifica el comienzo y el final donde los datos son aplicables, o datos de localización (por ejemplo, de cambio de alimentación de tracción) es decir, dando el punto de comienzo, dependiendo del tipo de condición de la vía.

Los tipos de condiciones de la vía que son cubiertos por esta función son:

– Sección sin alimentación, bajar pantógrafos o desconectar el interruptor principal / abrir el disyuntor;

– Cierre de trampillas de presurización;

– Túnel, parada no permitida / inhibición del sistema de aparatos de alarma para los viajeros;

– Cambio de alimentación de tracción, accionar el conmutador de a bordo de alimentación de tracción;

– Puente, parada no permitida / inhibición del sistema de aparatos de alarma para los viajeros;

– Grandes masas metálicas;

– Zona de Sombra de Radio, cortar la supervisión de la pérdida de enlace radio;

– Desconexión del freno de recuperación;

– Desconexión del freno de corrientes de Foucault;

– Desconexión del freno magnético sobre los carriles;

b) Mensajes de Texto.

El Sistema ETCS hace posible transmitir información que se muestra al Maquinista en forma de mensajes de texto. Los mensajes de texto están siempre complementados por condiciones respecto a cuándo y dónde deben ser mostrados, y si es necesaria confirmación por parte del maquinista.

Si deben mostrarse simultáneamente más mensajes del mismo tipo que los que puede contener la pantalla DMI disponible, los mensajes más nuevos tendrán precedencia sobre los antiguos que quedarán ocultos pero permanecen almacenados y reaparecen si los mensajes más nuevos son borrados. El maquinista puede también seleccionar los diferentes mensajes ocultos para mostrarlos en pantalla.

En el caso de mensajes que precisan confirmación por parte del maquinista, no se ocultan detrás de los mensajes más nuevos de la misma clase que no requieran confirmación. Si un mensaje que debe ser confirmado queda oculto detrás de otro mensaje que también ha de ser confirmado, reaparece cuando este último se confirma.

c) Perfil de Modo.

Es posible enviar al tren una indicación de Perfil de Modo para pasar a modo On Sight (OS) o modo Shunting (SH). Para el modo OS el perfil de modo define la entrada y la longitud de la zona de marcha a la vista. Para el modo SH el perfil de modo solo definirá la entrada a la zona de maniobras.

Si el equipo de a bordo recibe una nueva MA sin Perfil de Modo, el Perfil de Modo que se estaba utilizando se elimina.

4. Supervisión dinámica y gradientes.

El control de la velocidad es la supervisión de la velocidad del tren en relación con su posición, con el fin de hacer que el tren respete el «Perfil Más Restrictivo de Velocidad» (MRSP) y el Límite o final de la autorización de movimiento (LOA/EOA).

El equipo ETCS embarcado emite órdenes de frenado y las revoca (salvo la orden de freno de emergencia); también puede recibir información de estado: si se aplican o aflojan los frenos. Sin embargo, no supervisa los circuitos de control de frenos; ya que son ajenos al equipo ETCS.

El control de la velocidad comprende:

– La vigilancia de la velocidad máxima, supervisando las curvas de velocidad constante determinada en base al valor actual del Perfil Más Restrictivo de Velocidad (MRSP).

– La vigilancia de la velocidad meta, supervisando el proceso de frenado a una velocidad meta más baja, o al EOA / LOA.

– El control de la velocidad de liberación.

– La función de detención del tren, al rebasar una EOA / LOA. La función de detención del tren (Train Trip) será iniciada si el equipo de a bordo detecta que la cabeza del tren ha rebasado el EOA/LOA.

La función de detención del tren emitirá una orden de frenado de emergencia que no será revocada hasta que el tren se encuentre detenido y el maquinista confirme la detención.

El gradiente es la medida de la inclinación que presenta la vía. Tendrá un valor positivo cuando se trate de una rampa (ascendente) o negativo cuando se trate de una pendiente (descendente). Esta información se envía desde vía al equipo embarcado, que la utiliza en los cálculos de distancia de frenado.

5. Límites de Supervisión.

El principio de la supervisión de velocidad reside en la comparación en tiempo real de la velocidad del tren con la velocidad permitida, calculada por la Eurocabina, y en el accionamiento del freno del tren (de servicio o de emergencia, según el caso), cuando la velocidad del tren sobrepasa dicha velocidad.

Este funcionamiento está basado en el conocimiento por el equipo del tren de su localización con respecto a los puntos de información ETCS representados por las eurobalizas.

Todos los cálculos efectuados por el equipo embarcado tienen en cuenta que las deceleraciones consideradas están garantizadas, pero son diferentes dependiendo de los escalones de velocidad y los tipos de tren, y que estas deceleraciones deben ser corregidas teniendo en cuenta las pendientes y rampas incluidas en la MA (Autorización de Movimiento).

El tren ETCS calcula puntos meta intermedios (distancia meta y velocidad meta) y un punto meta que no deberá sobrepasar (distancia meta con velocidad cero, EOA).

A partir de estos puntos meta, el tren elabora las curvas de control de velocidad:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/171/08042_232.png)

a) Curva de velocidad permitida (V. Límite): es la velocidad que puede alcanzar el Maquinista de forma segura, y la que se le muestra en el DMI.

b) Curva de aviso: situada por encima de la curva de velocidad permitida de tal forma que, si la velocidad real del tren sobrepasa la velocidad prescrita para esa curva, se envía una indicación (sonora y visual) al Maquinista para que disminuya la velocidad con el fin de evitar la aplicación del freno de servicio.

c) Curva de intervención (supervisión) del freno de servicio: cuando esta operativo este freno en funcionamiento ETCS, se sitúa por encima de la curva de aviso tal que, si la velocidad real del tren sobrepasa la velocidad prescrita por esta curva, se activa el freno de servicio, liberándose cuando se llega a la velocidad permitida. La actuación del freno de servicio se indica en el DMI.

d) Curva de emergencia: situada por encima de la curva de activación del freno de servicio, tal que, si la velocidad real del tren sobrepasa la velocidad prescrita por esta curva, se aplica el freno de emergencia, liberándose únicamente a tren parado. La activación del freno de emergencia se indica en el DMI.

e) Velocidad de liberación: Si la velocidad del tren excede la Velocidad de Liberación, se activará una orden para aplicar el freno de emergencia.

La transición al control de la velocidad de liberación se ejecutará automáticamente cuando el valor de la Velocidad de Liberación sea igual al límite de la intervención del freno de servicio. Los límites de las curvas de intervención y emergencia, dejarán de ser supervisados.

Se establece un límite de aviso que activa una alerta que permanece mostrada mientras la velocidad del tren exceda del mismo. Este límite de advertencia es más bajo que la Velocidad de Liberación. La transición se ejecuta cuando el límite de aviso del control de la velocidad meta sea igual al límite de aviso del control de la Velocidad de Liberación.

Se indica en el DMI que la Velocidad de Liberación es supervisada, y el valor de dicha Velocidad de Liberación.

La indicación del límite de Velocidad Permitida del control de la velocidad meta sigue mostrándose hasta llegar al valor cero.

6. Protección contra movimientos indeseados de los trenes.

a) Protección ante movimientos indebidos.

La Protección contra Movimientos Indebidos (RAP) impedirá que el tren se desplace en sentido contrario a la posición del inversor en la cabina activa. Si el inversor se encuentra en posición neutra, la RAP impide que el tren se mueva hacia adelante o hacia atrás.

Cuando el sistema reconozca un movimiento que exceda del valor nacional para distancia de escape permitida, se aplican los frenos.

Cuando el tren se detenga se revocará la orden de frenado para permitir que el maquinista afloje los frenos.

Tras la revocación de la orden de frenado, la RAP se iniciara de nuevo, utilizando la posición actual del tren como la nueva localización de referencia.

b) Protección contra el Movimiento de Retroceso.

La Protección contra el Movimiento de Retroceso (RMP) impide que el tren se desplace en sentido opuesto al permitido. El sentido de movimiento permitido de un tren es el de la MA activa, si se halla disponible a bordo. Cuando se detecte un movimiento de retroceso, se da la orden de aplicar los frenos al cabo de una distancia especificada por un valor nacional.

Cuando el tren quede detenido se revoca la orden de frenado para permitir que el maquinista afloje los frenos.

Tras la revocación de la orden de frenado, el RMP es inicializado de nuevo, utilizando la posición actual del tren como nueva localización de referencia.

c) Supervisión de inmovilización.

Esta función impide que el tren se desplace más que una distancia dependiente del tren.

Si se excede de la distancia supervisada, se emitirá una orden de frenado.

Si una cabina se encuentra activada, la orden de frenado es revocada en cuanto el tren quede parado, para permitir al maquinista que afloje los frenos.

Tras la revocación de la orden de frenado, la supervisión de la inmovilización es nuevamente inicializada, usando la posición actual del tren como nueva referencia de localización.

NOTA: En ciertas series de trenes existen en el propio tren supervisiones iguales a similares a estas. Ejecutándose la supervisión del valor más restrictivo de ambas.

5AN1.AP1.4. Modos. Definición.

1. Se entiende por modo técnico de operación, abreviadamente «modo», al estado de operación del equipo embarcado en relación con la supervisión que puede ofrecer en función de la información recibida de la infraestructura, en cada uno de sus niveles.

2. Los modos técnicos de ETCS son:

No operativos; aplicables a todos los niveles (0, 1, 2 y STM):

IS (Isolation; asilamiento). El equipo se encuentra asilado; no interviene en ningún equipo del tren, ni incluso en los frenos.

NP (No power; sin alimentación). El equipo se encuentra sin alimentación y por lo tanto hay orden de freno de emergencia.

SF (System failure; fallo del sistema). Se produce por un fallo del EOB que afecte a la seguridad del equipo. Se da la orden de freno de emergencia.

SB (Stand By; en espera). Modo utilizado para el inicio del equipo, para su autocomprobación y la de los dispositivos periféricos. Es el modo en el que hay que introducir los datos del tren al inicio de la misión. El tren permanece parado por la acción de los frenos.

Operativos:

SR (Staff Responsible; responsabilidad maquinista); aplicable a niveles 1 y 2. Modo de conducción bajo la responsabilidad del maquinista; cuando sea preciso bajo las indicaciones del responsable de circulación. Se utiliza cuando no hay información de ruta, por ejemplo, en el inicio de una misión, tras un rebase, o después de un fallo del equipo de vía. En este modo eI equipo embarcado supervisa la velocidad máxima; valor nacional establecido para este caso. El Maquinista debe respetar la señalización lateral de acuerdo al RCF.

FS (Full Supervision; supervisión total); aplicable a niveles 1 y 2. El equipo supervisa los movimientos del tren con respecto a un perfil dinámico de velocidad calculado sobre la base del perfil estático de velocidad, limitaciones temporales de velocidad máxima, datos de gradiente de la vía, datos del tren y MA. Este modo no puede ser seleccionado por el Maquinista. El DMI mostrará al Maquinista la velocidad del tren, la velocidad permitida, y la distancia meta y la velocidad meta cuando sea precisada.

OS (On Sight; marcha a la vista); aplicable a niveles 1 y 2. Modo de circulación asociado a la entrada a vía ocupada. El equipo embarcado supervisa la velocidad definida para este modo (valor nacional) y las limitaciones de velocidad por debajo de ese valor nacional; el maquinista procederá como establece el RCF con el límite de esa velocidad máxima establecida. Este modo no puede ser seleccionado por el Maquinista, es enviado desde la vía por orden del responsable de circulación.

SH (Shunting; maniobras); aplicable a niveles 0, 1 y 2. Modo para la realización de movimientos de maniobras. El equipo supervisa los movimientos del tren respecto a una velocidad máxima y una distancia máxima delimitada por una orden de parada. El modo SH puede ser seleccionado por el Maquinista, u ordenado por la vía, lo que requiere el reconocimiento deI maquinista. La entrada del equipo en el modo SH se considera un final de misión.

SN (STM nacional); aplicable a nivel STM. Se utiIiza cuando se circula por una línea equipada con un sistema de señalización nacional. El módulo STM mantiene la funcionalidad del sistema nacional e interacciona con el equipo fijo de vía. En este modo, el Maquinista debe respetar los procedimientos establecidos para el sistema nacional.

UN (Unfitted; vía no equipada); aplicable a nivel 0. Modo de circulación en Nivel 0, utilizado en zonas no equipadas con ETCS. El equipo supervisa la velocidad determinada para este modo (valor nacional) El Maquinista debe respetar la señalización lateral existente y los procedimientos establecidos en el RCF.

Operativos particulares:

TR (Trip; Rebase indebido); aplicable a niveles 1 y 2. Modo asociado a la detención automática del tren, que conlleva la aplicación deI freno de emergencia. El equipo transita a este modo como reacción ante un evento no seguro (por ejemplo, el rebase de un EOA). Cuando el tren se encuentre detenido se solicitará el reconocimiento del Maquinista para salir de este modo.

PT (Post Trip; después de rebase); aplicable a niveles 1 y 2. Modo al que transita el equipo una vez reconocido eI TR. En este modo se produce la liberación del freno de emergencia; solamente permite el movimiento hacia atrás y a una distancia determinada como valor nacional. Para continuarla marcha únicamente se podrá realizar el procedimiento de rebase o, si el equipo no lo permitiese, seleccionar el comienzo de misión.

NL (Non Leading; sin mando); aplicable a todos los niveles. Este modo se define para gestionar eI equipo de una cabina que no circula en primer lugar y que no es controlada desde la de cabeza, ya que tiene su propio Maquinista (tracción múltiple).

SL (Sleeping; durmiente); aplicable a todos los niveles. Este modo es aplicable a una cabina que no circula en cabeza y que es controlada a distancia; por lo tanto no tiene maquinista (mando múltiple).

RV (Reversing; retroceso); aplicable a niveles 1 y 2 (no usada en la RFIG). Este modo se utiIiza para cambiar eI sentido de la marcha del tren y conducir desde la misma cabina. Esto solo es posible en un área de retroceso previamente anunciada por el equipo fijo de vía. El equipo embarcado mostrará la velocidad del tren, la velocidad permitida y la distancia restante por recorrer.

5AN1.AP1.5. Formas de realizar las transiciones.

Se consideran dos formas de realizar las transiciones de nivel.

1. Transiciones nominales: son las que se producen en las fronteras de la línea (o dentro de ella tras un inicio de misión) como consecuencia del cambio de nivel ETCS o sistema de señalización en la vía.

Se realizan de forma automática cuando se recibe la orden de cambio de nivel transmitida mediante balizas o RBC que contienen la siguiente información:

a) Distancia al cambio de nivel.

b) Punto, antes de llegar al cambio de nivel, a partir del cual el Maquinista puede realizar el reconocimiento. Este debe realizarse antes de que pasen 5 segundos tras el cambio de nivel.

c) MA (Autorización de movimiento) hasta el punto de conmutación. La velocidad en dicho punto será la adecuada al nuevo nivel.

2. Transiciones degradadas: son las que se realizan a tren parado dentro de la línea como consecuencia de un fallo en el sistema de señalización que protege al tren.

En los puntos de transición entre sistemas o a distintos Niveles de ETCS en los que aparezcan valores de la velocidad límite inferiores a las velocidades máximas permitidas, obedecen a las reglas de ingeniería aplicadas al equipo de vía.
