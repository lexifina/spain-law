## ANEXO II

## Sistema de telegestión

Constituye el objeto de este anexo establecer los requisitos relativos a la telegestión de los contadores eléctricos para la medida de energía eléctrica.

1. Definiciones de términos.

1.1 Sistema de telegestión.–Se denomina sistema de telegestión a un sistema de medida y comunicación bidireccional entre los contadores y las distribuidoras eléctricas, que, con las máximas garantías de integridad y seguridad, permite acceso remoto a los contadores de energía eléctrica, con disponibilidad de lectura, gestión de la energía, control de la potencia demandada y contratada y gestión de la conexión/desconexión de suministros y mecanismos antifraude avanzados, posibilitando el intercambio de información y actuaciones entre los sistemas de las empresas distribuidoras eléctricas y contadores.

1.2 Contadores estáticos de energía eléctrica con comunicaciones incorporadas.–Contador que, además de medir y registrar con fiabilidad y precisión la energía activa en clases A, B y C, hasta una potencia de 15 kW, y energía reactiva en clases 2 y 3, permite adicionalmente controlar la potencia demandada y ejecutar las órdenes que le son transmitidas confirmando su ejecución.

Deben disponer de una implementación software que ejecuta las funcionalidades necesarias. Se accede a él mediante un protocolo que debe contemplar mecanismos adicionales de seguridad y confiabilidad.

1.3 Concentrador CT.–Elemento intermedio entre el sistema informático de gestión y control y los equipos de medida, que permite la gestión de un número limitado de equipos de medida. Dispone de comunicaciones con el sistema informático y con los equipos de medida. Habitualmente pueden estar instalados en centros de transformación y actúan con funciones de telegestión entre los concentradores secundarios y los contadores, gestionando las comunicaciones entre ellos.

2. Estructura del sistema de telegestión.

2.1 Arquitectura del sistema.–El sistema puede estructurarse en una arquitectura jerárquica de varios niveles con los siguientes elementos:

Contadores: se comunicarán remotamente con los concentradores CT por la red de comunicaciones de distribución, fundamentalmente mediante PLC, y localmente mediante puerto óptico, según norma UNE EN 62056-21. Deberán cumplir con las especificaciones funcionales de telegestión y de discriminación horaria establecidas. Podrán existir contadores que comuniquen por otros canales de comunicación directamente con el concentrador secundario, en su caso, o con el concentrador principal.

Concentradores CT: se comunicarán remotamente con los concentradores secundarios por la red de acceso, utilizando distintos medios de comunicación; y con los contadores, fundamentalmente mediante PLC. Su ubicación topológica natural es el centro de transformación.

Concentradores secundarios: se comunicarán con el concentrador principal por la red troncal.

Concentrador principal.

2.2 Sincronización horaria del sistema.–Se establecerá un sistema de sincronización horaria, preferentemente basado en GPS en los niveles superiores y con una estructura jerarquizada de sincronización, desde los concentradores secundarios hacia los concentradores CT y contadores, mediante órdenes de supervisión y puesta en hora, para el cumplimiento de la norma UNE EN 62054-21. La cadena de sincronización garantizará la trazabilidad diaria de los relojes al patrón nacional de tiempo.

2.3 Integridad y seguridad.-El sistema de telegestión deberá contemplar mecanismos de control de acceso y de registro de eventos de accesos no autorizados; así como de confirmación de recepción de mensajes.

3. Requisitos técnicos y especificaciones funcionales del sistema.

Se establecen las siguientes especificaciones funcionales para el sistema de telegestión:

3.1 Lectura remota.–El sistema permitirá la lectura a través de comunicaciones, de, entre otros:

Medidas eléctricas: energía activa, reactiva y las potencias máximas según la discriminación horaria parametrizada (valores en curso) y las correspondientes a cierres de facturación.

Parametrización, activa y latente, de tarifas, calendarios y potencias contratadas.

Alarmas y eventos.

Datos de identificación del contador.

El concentrador CT realizará una interrogación cíclica, con periodicidad parametrizable a todos los contadores que comunican con él.

Junto con esta tarea automática de interrogación cíclica, el sistema podrá disponer de la funcionalidad de acceso puntual a un contador cualquiera con prioridad sobre la tarea automática.

3.2 Sincronización remota.–En cada ciclo de lectura se comprobará la fecha y hora de los contadores y se sincronizarán si fuera necesario.

3.3 Control remoto de la potencia. Corte y reconexión.–Desde niveles superiores se pueden enviar órdenes de corte y reposición a los contadores.

Una vez ejecutada la orden de corte por el contador, este no aceptará ninguna reconexión del interruptor, ni mediante orden remota de dispositivo externo doméstico si existe, ni permitirá el enclavamiento ante una actuación manual externa sobre el interruptor o el reenganche automático, si algunas de estas funciones están disponibles, hasta no recibir una nueva orden de reconexión del nivel superior.

La función de reconexión por orden remota deberá cumplir la normativa vigente aplicable en materia de protección y seguridad de bienes y personas. Adicionalmente a las órdenes remotas de conexión y desconexión, el elemento de corte actuará desde el punto de vista de control de la demanda, como interruptor de control de potencia programable que cumplirá los requisitos que sean de aplicación, establecidos en el Real Decreto 1955/2000, de 1 de diciembre y en las normas que se desarrollen en relación al control eléctrico de potencia.

La función de ICP programable deberá cumplir, del mismo modo, la normativa vigente aplicable en materia de protección y seguridad de bienes y personas.

3.4 Actualización dinámica de las tarifas (programación remota).–Desde niveles superiores se podrán enviar órdenes de modificación de parámetros a los contadores, entre otros, cambio de tarifas, potencias contratadas, tipo de contrato, cuando exista la base legal y contractual para ello.

3.5 Capacidad de gestión de cargas.–El sistema deberá disponer de funcionalidad que permita actuar sobre la demanda de los clientes, al objeto de poder actuar y realizar reducciones de carga en momentos críticos, cuando exista la base normativa, legal y contractual para ello.

El sistema permitirá la programación remota de la potencia contratada así como el control de la demandada por el cliente.

3.6 Control de accesos y registros de intervenciones.–El sistema debe garantizar la fiabilidad y seguridad de la información contenida y que circula por el mismo.

El acceso a cada equipo contador o concentrador estará controlado y asegurado por el sistema de direccionamiento al mismo y por clave de acceso definibles a nivel individual y en función de los permisos de acceso asociados.

Cada acceso a un equipo contador o concentrador podrá ser registrado con la identificación del equipo que inicia la comunicación, la fecha/hora y el perfil de la comunicación establecida.

El sistema contemplará la detección y registro de accesos no autorizados.

3.7 Registro de eventos.–El sistema almacenará una serie de incidencias con la fecha y hora en las que se han producido. El tipo de eventos almacenados deberán ser, al menos:

Versión de software y firmware con indicación del momento de su instalación o modificación.

Presencia y ausencia de tensión.

Indicación de modificación de parámetros en el contador o concentrador, particularmente todos aquellos relacionados con los epígrafes 3.2 y 3.3 inmediatamente anteriores, con identificador del tipo y cuantía de parámetro modificado.

Alarma crítica del equipo contador o concentrador.

Intentos de accesos no autorizados.

3.8 Verificación de las comunicaciones del sistema de telegestión.–A efectos de permitir su verificación, el sistema podrá elaborar estadísticas de comunicaciones entre concentradores y contadores.

3.9 Información de usuario.–El usuario, en función de la modalidad contractual que le aplique, podrá disponer de la siguiente información relevante a su consumo, entre otras:

Consumo eléctrico total y discriminado.

Período tarifario en curso.

Potencia máxima demandada.

Potencia contratada.

Fecha y hora.

Información de control de cargas, en su caso.

Con carácter general, el contador presentará:

Indicación del sentido de la energía.

Presencia y orden de las fases.

Estado de las comunicaciones.

3.10 Consideraciones para verificación del contador.–En el equipo se podrá verificar la medida tanto activa como reactiva mediante uno o varios led de pulsos con un peso de pulso no configurable. En caso de disponer de un led únicamente para activa y reactiva, éste por defecto emitirá pulsos en activa siendo posible la configuración para emitir pulsos en reactiva, bien por comunicaciones o por teclado.

3.11 Modificaciones de software y firmware.–El software y firmware instalado en el equipo forma parte integrante del mismo y deberá superar la evaluación de la conformidad a la que se refiere el artículo 5 de esta orden. Cualquier modificación o nueva versión de software deberá quedar documentada e identificada y tendrá que haber superado la evaluación de la conformidad.

En el caso de que el contador disponga de funciones de actualización de software o firmware de funcionamiento, tanto local como remoto, deberá garantizarse que dichas actualizaciones han superado la evaluación de la conformidad y que no modifican las características metrológicas del contador ni las medidas y resto de registros almacenados hasta el momento.

El responsable de la medida conservará la certificación del organismo de control metrológico a disposición de la Administración pública competente.
