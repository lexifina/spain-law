## Tercero. Equipos de medida, control y comunicaciones (EMCC).

3.1 Los proveedores del servicio deberán disponer de equipos de medida, control y comunicaciones (EMCC) para comunicar con los SG-SCECI instalados en los centros de control principal y de respaldo mediante el Protocolo de Comunicaciones, realizar todas las funciones necesarias para recibir del SG-SCECI y ejecutar las órdenes de reducción de potencia, su cambio y anulación, y captar y enviar al SG-SCECI la información necesaria para la supervisión de las órdenes de reducción de potencia y resto de información precisa para la verificación de la prestación del servicio. Todo ello de acuerdo con los requisitos de los artículos 9 y 10, según corresponda, de la Orden IET/2013/2013, de 31 de octubre.

3.2 El EMCC incluye los contadores, excepto cuando estos sean compartidos con el Sistema de Medidas Eléctricas SIMEL, los convertidores necesarios para la captación de las medidas de potencia instantánea y el relé de deslastre por subfrecuencia. En su caso, también los equipos auxiliares de conversión y transformación de las medidas, así como la comunicación de estos equipos auxiliares con el equipo principal.

3.3 El EMCC y, en su caso, los equipos auxiliares del mismo, deberán estar conectados a un sistema de alimentación que, en caso de ausencia del suministro principal de energía, garantice su correcto funcionamiento durante al menos 4 horas.

3.4 El EMCC y, en su caso, los equipos auxiliares del mismo, deberán estar construidos e instalados de manera que sean precintables. El Operador del Sistema será responsable de la realización del precintado.

3.5 El EMCC y sus equipos auxiliares, así como su instalación, deberán ser certificados antes de su puesta en servicio y con periodicidad bianual, por el Operador del Sistema, que verificará si reúnen los requisitos que se establecen en la presente resolución y, en su caso, emitirá la certificación correspondiente a efectos de lo dispuesto en la Orden IET/2013/2013, de 31 de octubre. El proceso de verificación y certificación será publicado en el sitio Web del Operador del Sistema.

3.6 El EMCC deberá estar dotado de los elementos necesarios para la captación de la información procedente de contadores de energía activa, y convertidores de potencia instantánea activa y reactiva.

3.7 El EMCC deberá estar dotado de los elementos necesarios para la captación de la actuación del relé de deslastre por subfrecuencia, su procesamiento y notificación al SG-SCECI.

3.8 El EMCC deberá recibir del SG-SCECI la autorización de reconexión del relé de deslastre por subfrecuencia, procesar dicha autorización y notificarla al proveedor del servicio.

3.9 El EMCC dispondrá de elementos de vigilancia de fallos en el funcionamiento del equipo y en su interfaz con el sistema de comunicaciones, así como de la funcionalidad necesaria para notificar al SG-SCECI cambios en los mismos, tan pronto como el EMCC recupere la situación de funcionamiento normal.

3.10 Especificaciones técnicas.

El EMCC deberá contar al menos con los siguientes elementos:

a) Una unidad de comunicación, que intercambie información con el resto de unidades del EMCC, implemente el Protocolo de Comunicación y actúe como interfaz con el Sistema de Comunicaciones. Cada EMCC se identificará en el Sistema de Comunicaciones con una IP única asignada por el Operador del Sistema.

b) Una unidad de tratamiento de órdenes de interrupción de potencia, que procese las órdenes de interrupción de potencia y la señal de autorización de reconexión del relé de deslastre por subfrecuencia recibidas de la unidad de comunicación, y las ponga a disposición del proveedor del servicio, para su utilización posterior.

c) Una unidad de tratamiento de la información de contadores de energía y medidas de potencia instantánea activa y reactiva, con los siguientes elementos:

1.º Maxímetro integrador de energía demandada con período de integración de quince minutos, que calculará y registrará de modo continuo la potencia activa media en cada uno de los periodos. El inicio de cada periodo de integración estará sincronizado con el de cada cuarto de hora del reloj local del EMCC.

2.º Maxímetro integrador de energía demandada con período de integración de cinco minutos, que calculará y registrará la potencia activa media en cada uno de los periodos. Este maxímetro se activará únicamente durante la ejecución de las órdenes de reducción de potencia. El inicio del primer periodo de integración se sincronizará con el instante de inicio de la orden de reducción de potencia. El último periodo de integración finalizará con el instante de finalización de la orden de reducción de potencia y por lo tanto su duración podrá ser inferior a cinco minutos.

3.º Procesador de medidas instantáneas de potencia activa y reactiva, que calculara y registrará su valor medio, en periodos de 4 segundos. Envío a la unidad de comunicaciones de la información al finalizar cada periodo.

d) Reloj interno con fecha y hora, en horario oficial, que se utilizará para etiquetar todos los eventos del EMCC y sincronizar los registros de los maxímetros de la letra c) anterior. Este reloj estará sincronizado con el reloj del SG-SCECI de acuerdo con el procedimiento descrito en la norma EN 60870-5-104 que se deberá implementar en el Protocolo de Comunicación. El proceso de sincronización se realizará de forma continua, salvo durante los periodos correspondientes a una orden de reducción de potencia, con la periodicidad que se indique en el Protocolo de Comunicación.

e) Sistema de impresión en soporte cinta de papel que registrará, al menos, parada y arranque del EMCC, fallo del EMCC, valores en cada periodo de los maxímetros que se indican en la letra c) anterior, recepción, ejecución, modificación y anulación de las órdenes de reducción de potencia, activación del relé de deslastre de subfrecuencia, recepción de la señal de autorización de la reconexión del relé de deslastre de subfrecuencia y estado de la comunicación entre el EMCC y el SG-SCECI.

Los registros en cinta de papel llevarán impresa la hora, minuto, segundo y fecha en que se producen así como el Código Universal de Punto de Suministro (CUPS) que identifique al proveedor del servicio.

El sistema de impresión podrá ser complementado o reemplazado por una tarjeta de memoria no volátil removible (Compact Flash). El procedimiento de grabación de los registros deberá garantizar la integridad y no repudio de la información, y deberá ser aprobado por el Operador del sistema.

El cambio de papel y el de la tarjeta de memoria deberán poder realizarse sin necesidad de desprecintar el EMCC.

f) Panel o indicadores de salida luminosos claramente visible e identificables, con la siguiente información:

1.º Indicador de la opción de ejecución. Esta indicación estará activada permanentemente.

2.º Indicador de cambio de orden de reducción de potencia. Esta indicación se activará al recibir el cambio de orden de reducción y permanecerá activada cinco minutos.

3.º Indicador de anulación de orden de reducción de potencia. Esta indicación se activará al recibir la anulación de la orden de reducción y permanecerá activada cinco minutos.

4.º Indicador del periodo tarifario, P1 a P6, de entre los definidos en el apartado 3.3 del anexo II de la Orden ITC/2794/2007, de 27 de septiembre, por la que se revisan las tarifas eléctricas a partir del 1 de octubre de 2007, que corresponda a hora y día en curso.

5.º Indicador de mal funcionamiento o error del EMCC.

6.º Indicador de pérdida de comunicación entre el EMCC y el SG-SCECI.

7.º Indicador de activación de los contactos de salida para uso externo del apartado g) siguiente.

8.º Cuatro últimos valores del maxímetro integrador de energía demandada con periodo de integración de quince minutos.

9.º Medida de potencia activa instantánea demandada y, en su caso, generada.

g) Contactos se salida, libres de potencial, claramente identificados, para uso externo al EMCC:

1.º Un contacto de salida de relé normalmente abierto (N/A), por cada una de las opciones de ejecución de potencia definidas en la Orden Ministerial IET/2013/2013, de 31 de octubre. Este contacto deberá permanecer cerrado desde el instante de recepción de una orden de reducción de potencia, hasta su finalización, modificación o anulación.

2.º Un contacto de salida de relé normalmente abierto (N/A), que deberá permanecer cerrado mientras dure la ejecución de una orden de reducción de potencia.

3.º Un contacto de salida de relé normalmente abierto (N/A), por cada Identificador de la Potencia residual que aplique, Pmax, según lo previsto en el apartado 10.3.b) de la Orden IET/2013/2013, de 31 de octubre.

Este contacto deberá permanecer cerrado durante el periodo o periodos de la orden de reducción de potencia para los cuales aplique la Potencia Residual correspondiente a dicho Identificador.

4.º Un contacto de salida de relé normalmente abierto (N/A), que deberá cerrarse, y permanecer cerrado durante cinco minutos, al recibir la señal de autorización de la reconexión del relé de deslastre por subfrecuencia.

5.º Un contacto de salida de relé normalmente cerrado (N/C), que deberá permanecer abierto cuando el equipo EMCC del proveedor del servicio no tenga conexión con el SG-SCECI.

6.º Un contacto de salida de relé normalmente cerrado (N/C), que deberá permanecer abierto cuando el equipo EMCC tenga algún fallo que imposibilite su correcto funcionamiento.

7.º Un mínimo de 5 contactos de salida de reserva.

h) Entradas digitales al equipo EMCC.

El EMCC dispondrá, al menos, de las siguientes entradas accesibles externamente con aislamiento de potencial, para captar la siguiente información:

1.º Activación del relé de deslastre por subfrecuencia.

2.º Cinco entradas de reserva.

i) Bus de comunicaciones.

El EMCC dispondrá de un bus de comunicaciones accesible a través de una interfaz Ethernet con conector RJ45 o puerto serie RS232/RS485, que utilizará alguno de los siguientes protocolos de comunicación: MODBUS RTU, MODBUS TCP, EN 60870-5-102, para la adquisición de la siguiente información:

1.º Contadores de energía activa demandada por la instalación del consumidor.

2.º Medida de potencia instantánea demandada activa y reactiva de la instalación del consumidor.

3.º Medida de potencia activa instantánea generada. Esta información solo se captará en aquellos proveedores del servicio que dispongan de una instalación de generación asociada al proceso productivo cuya demanda está adscrita al servicio de interrumpibilidad.

Opcionalmente, para la conexión de las señales digitales indicadas en los apartados f) y g) anteriores con los sistemas del proveedor del servicio, se podrá utilizar la conexión a través de puerto serie o Ethernet y alguno de los siguientes protocolos de comunicación: MODBUS RTU, MODBUS TCP, EN 60870-5-101, EN 60870-5-104.

El Operador del Sistema podrá publicar una implementación de los protocolos de comunicación anteriores, que deberán soportar los equipos EMCC.

j) El EMCC deberá disponer de una interfaz de usuario, que podrá ser accesible de forma local, sin necesidad de desprecintar el equipo, o remota, para realizar, al menos, las siguientes operaciones:

1.º Volcado en el registro que se describe en el apartado tercero. 3.10 e) de los datos de demanda de la última orden de reducción de potencia, registrados cada cinco minutos y, al menos, las 3 últimas autorizaciones de reconexión del relé del deslastre por subfrecuencia.

2.º Recuperación del archivo de orden de reducción de potencia, en el formato que se describa por el Operador del Sistema en el documento del Protocolo de Comunicación.

3.º Introducción de las magnitudes siguientes:

i) Periodos tarifarios recogidos en el apartado 3.3 del anexo II de la Orden ITC/2794/2007, de 27 de septiembre.

ii) Pmax (Potencia residual de referenciaprevista en el artículo 10.3 b) de la Orden IET/2013/2013, de 31 de octubre).

iii) Psub (Potencia asignada en la subasta, de acuerdo a lo dispuesto en la Orden IET/2013/2013, de 31 de octubre).

iv) Tiempo de Espera (definido en el apartado Sexto. 6.6).

v) Número Máximo de Reintentos (definido en el apartado Sexto. 6.6).

4.º Realización de las siguientes operaciones:

i) Activación de una orden de interrupción de potencia.

ii) Acceso al registro del EMCC que se describe en el apartado Tercero. 3.10 e) del presente procedimiento.

iii) Carga en el EMCC del programa de consumo horario previsto de la instalación del consumidor.

iv) Carga en el EMCC de los periodos de indisponibilidad de la instalación del consumidor.

Todas las actividades realizadas a través de la interfaz de usuario deberán quedar registradas en el sistema que se describe en el apartado Tercero. 3.10 e) del presente procedimiento.

k) El EMCC deberá mantener un registro histórico en soporte informático con los siguientes datos relativos a cada solicitud de orden de reducción de potencia:

– Pi: Valor de cada uno de los i registros cincominutales durante la ejecución de una orden de reducción de potencia.

– Pd: Máxima potencia demandada durante la ejecución de una orden de reducción de potencia.

– Hora de recepción de señal de preaviso, activación, cambio y anulación de la orden de reducción de potencia.

– Opción de ejecución de las recogidas en el artículo 5 de la Orden IET/2013/2013, de 31 de octubre.

– Cualquier otro dato que, a criterio del proveedor del servicio, se juzgue necesario para contrastar el cumplimiento de la orden de reducción de potencia.

Este registro deberá conservarse en soporte informático, accesible por el proveedor del servicio y, previa solicitud, por el Operador del Sistema, durante al menos cinco años.

3.11 Información estructural.

Los proveedores del servicio suministrarán al Operador del Sistema, la siguiente información estructural:

– Fabricante y modelo del EMCC, y equipos auxiliares del mismo cuando los hubiera, incluyendo, cuando sea preciso para la correcta caracterización del equipo, la versión o versiones del software.

– Relación de transformación y clase de precisión de los transformadores de medida de tensión e intensidad.

– Fabricante, modelo, potencia nominal, clase de precisión y características técnicas eléctricas y mecánicas de la interfaz con el EMCC de los contadores de energía activa y equipos de medida de potencia activa y reactiva.

– Unifilar, en formato electrónico, de la instalación del proveedor del servicio con indicación del conexionado de los equipos de medida, EMCC y equipos auxiliares de este cuando los hubiera. Cuando sea relevante para el funcionamiento de los equipos, se indicará la distancia entre los mismos.

– Direcciones de correo electrónico de contacto, hasta un máximo de tres, para la comunicación de incidencias relativas al EMCC y su instalación. Los proveedores del servicio notificarán esta información en el formato indicado por el Operador del Sistema, y comunicarán cualquier modificación en el momento en que se produzca.

– Direcciones de correo electrónico, hasta un máximo de tres, y número de fax para uso con carácter excepcional cuando no se encuentre disponible la comunicación entre el SG-SCECI y el EMCC. Los proveedores del servicio enviarán esta información en el formato indicado por el Operador del Sistema, y comunicarán cualquier modificación en el momento en que se produzca, todo ello sin perjuicio de las autorizaciones que en su caso puedan requerir dichas modificaciones.
