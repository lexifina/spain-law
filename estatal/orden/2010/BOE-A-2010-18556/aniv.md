## ANEXO IV

## Requisitos esenciales específicos para los cinemómetros destinados a medir la velocidad de circulación de los vehículos a motor desde aeronaves

1. Terminología

1.1 Torretas optrónicas.–Son plataformas aeronáuticas giroestabilizadas que sirven para determinar de forma precisa, la longitud y latitud de objetivos.

1.2 Línea de mira georreferenciada.–Es la dirección en el espacio terrestre que señalan las cámaras del sistema.

1.3 Sistema de medición inercial.–Es la combinación de un sistema de navegación inercial propio alojado en la torreta y un receptor GPS, que sirve para determinar con precisión la línea de mira.

1.4 Latitud.–Es la distancia angular, medida sobre un meridiano, entre una localización terrestre y el Ecuador. Se mide en grados.

1.5 Longitud.–Es la medida que expresa la distancia horizontal, paralela al Ecuador, entre el meridiano de Greenwich y un determinado punto de la Tierra. Se mide en grados.

1.6 Geolocalización.–Es la capacidad de conocer o localizar el objetivo mediante la línea de mira georreferenciada y su intersección con la superficie de la tierra, a través de su longitud y su latitud.

1.7 Geoseñalización.–Es la capacidad de definir la latitud y longitud de un punto en la superficie terrestre dentro de un sistema.

1.8 Geoseguimiento.–Es la capacidad de seguir un objetivo a través de la evolución de su latitud y longitud en el tiempo.

2. Composición y funcionamiento

2.1 Composición.–Estos instrumentos o sistemas van montados generalmente sobre plataformas o torretas aeronáuticas a bordo de aeronaves y son capaces de medir la velocidad de los vehículos a motor por identificación y seguimiento. Están formados por los siguientes dispositivos o subsistemas:

a) Plataforma giroestabilizada compuesta por los siguientes elementos:

i. Cámaras de video.

ii. Sistema de recepción de señales GPS.

iii. Sistema de seguimiento automático por video (autotracker).

iv. Sistema de seguimiento por coordenadas geográficas (geotraking).

v. Sistema de medición de distancias o telémetro láser.

vi. Sistema inercial de medidas (IMU).

b) Sistema de cálculo o unidad de proceso, que recoge la información de la cámara, la procesa y calcula la velocidad del vehículo identificado.

c) Otros dispositivos complementarios, que integran el sistema sobre la aeronave, monitores de visualización y sistemas de grabación y registro de datos.

d) Opcionalmente pueden incorporar otros dispositivos como un sistema de cartografía con modelo digital del terreno, para mayor facilidad para el seguimiento y operación del sistema.

2.2 Funcionamiento.–El modo de operación o funcionamiento sería el siguiente:

1. Localización del vehículo u objetivo.

2. Seguimiento del vehículo mediante Autotraker y Geotraking.

3. Determinación de la velocidad del vehículo en los siguientes pasos:

a) Determinación de la latitud y longitud (georreferencia) de un vehículo en movimiento en el tiempo t1.

b) Determinación de la latitud y longitud (georreferencia) del mismo vehículo en el tiempo t2.

c) Medida del tiempo transcurrido entre t1 y t2.

d) Diferencia entre las posiciones georreferenciadas (t1 – t2).

e) Cálculo de la velocidad a partir de las posiciones y tiempo transcurrido.

3. Requisitos específicos

a) El sistema debe estar concebido de tal manera que todos los elementos que lo componen puedan funcionar de manera autónoma y mostrar resultados a efectos de poder ser ensayados de manera independiente.

b) El sistema debe poder proporcionar y monitorizar de forma clara e independiente los siguientes datos a través de una o varias interfaces protegidas y adecuadas:

i. La posición del objetivo en distintos tiempos de observación.

ii. La distancia medida entre dos puntos observados.

iii. El tiempo transcurrido entre ambas observaciones.

c) Las torretas aeronáuticas tendrán capacidad de autoalineación independiente de la aeronave donde va instalada, pudiendo ser intercambiables entre distintas aeronaves

d) En caso de disminución del suministro de tensión hasta un valor inferior al límite mínimo de funcionamiento especificado por el fabricante, el sistema deberá interrumpir la medición existente y volver a iniciar la medición.

e) La correspondencia del vehículo cuya velocidad se mide por el cinemómetro y la del vehículo que aparece en la filmación debe quedar asegurada. El vehículo cuya velocidad se mide deberá identificarse sin ambigüedad en la filmación. La indicación por registro videofotográfico debe coincidir con lo indicado en la parte de operación e informará, al menos, sobre los siguientes aspectos:

i. La fecha y hora de la medida.

ii. La velocidad medida del vehículo infractor.

iii. Identificación del instrumento que realizó la medida.

f) Supervisión de la tensión operativa: No debe haber indicación de velocidad cuando la tensión de alimentación varíe fuera de los límites para los cuales pueden ser superados los errores admisibles.

4. Errores máximos permitidos

Los errores máximos permitidos (en adelante, EMP) son:

Para la posición y medida de distancias: ± 3 %.

Valor mínimo del EMP: 5 m.

Para el tiempo transcurrido: ± 0,1 %.

Valor mínimo del EMP: 0,2 s.

Para la medida de velocidad: ± 10 %.

5. Otros requisitos

Para la realización de los ensayos de simulación de velocidad se facilitará un conjunto de simulación adecuado a cada tipo de cinemómetro que deberá cumplir los siguientes requisitos:

a) El conjunto deberá ir provisto de salidas o tomas de información, tipo bus CAN, puertos RS 232 o similares, con posibilidad de transmisión vía radio de la información a un centro de control o verificación para su comparación.

b) Si las características de la aeronave son importantes para la corrección del sistema, éste contará con medios para garantizar la conexión del sistema a la aeronave en el que va instalado.

c) Para la realización de ensayos después de la instalación, el sistema tendrá la opción de poder comprobar por métodos auxiliares la precisión de las medidas de tiempo y distancia, de forma independiente, así como la exactitud del cálculo de la velocidad.

d) El sistema estará concebido para que pueda respetar los errores máximos permitidos sin ajustes durante un período de un año de uso normal.

e) El sistema estará equipado con un reloj de tiempo real para mantener la hora del día y la fecha. Se aplicarán al reloj de tiempo real los requisitos siguientes:

i. El registro horario tendrá una exactitud de 0.02 %.

ii. La posibilidad de corrección del reloj no será superior a dos minutos a la semana.

iii. La corrección del horario de verano y de invierno se efectuará automáticamente.

f) Los valores de la distancia recorrida y del tiempo transcurrido, cuando se exhiban o se impriman, se expresarán en las unidades siguientes:

i. Distancia recorrida: kilómetros o metros.

ii. Tiempo transcurrido: segundos, minutos u horas según corresponda teniendo en cuenta la resolución necesaria.

iii. Velocidad: kilómetros por hora (km/h).

6. Protección

6.1 Comunicaciones.

a) Si el sistema es capaz de comunicarse con otros dispositivos externos o internos a éste, los interfaces necesarios para estas comunicaciones deberán estar protegidos de tal manera que no interfieran en el funcionamiento normal del cinemómetro.

b) La transferencia de datos a un sistema de control central sólo será posible si el cinemómetro protege estos datos contra cualquier interferencia, ya sea accidental o deliberada, en la transmisión.

c) La transferencia de datos desde un sistema de control central, deberá cumplir los siguientes requisitos:

i. Todas los partes de este sistema de control central que tengan relevancia metrológica, estarán sometidas a esta orden.

ii. El cinemómetro debe comunicar al sistema central la evidencia de recepción de datos correctos. Esta evidencia será fácilmente comprobable en cualquier momento, tanto en el cinemómetro como en el sistema central.

6.2 Software.–El software del sistema que tenga relevancia metrológica, programas, parámetros o datos específicos que pertenezcan al sistema de medida, se identificarán con un número de versión que se irá adaptando o modificando ante cualquier cambio del software que pueda afectar a las funciones y precisión del cinemómetro.

Cuando el acceso a parámetros que intervienen en la determinación de los resultados de medida no pueda estar protegido por precintos u otros medios físicos de seguridad (hardware), para garantizar esta protección se deberá tener en cuenta lo siguiente:

a) El acceso sólo se permitirá a personal autorizado, por medio de códigos de acceso, claves o contraseñas que puedan ser configurables.

b) Se registraran o memorizaran al menos las cuatro últimas intervenciones realizadas por un operador. El registro incluirá, al menos, la fecha y un medio de identificación de la persona autorizada que realiza la intervención.

La documentación de software suministrada por el fabricante, debe incluir:

i. Una descripción del software relevante.

ii. Una descripción de la exactitud de los algoritmos de medición (por ejemplo, el algoritmo de redondeo al calcular la velocidad).

iii. Una descripción del interfaz de usuario, menús, diálogos.

iv. La identificación inequívoca del software.

v. Una descripción del sistema informático.

vi. Medios de asegurar el software.

vii. El manual de operación.

viii. Cualquier otra información relevante a las características de software.

7. Inscripciones y precintos

7.1 Inscripciones.

a) Inscripciones obligatorias: Los cinemómetros o cada unidad que lo forma, deben presentar las siguientes indicaciones indelebles y legibles:

i. Nombre o marca registrada del fabricante o su representante.

ii. Nombre del modelo, número de serie y año de fabricación.

iii. Espacio para el marcado oficial.

b) Inscripciones optativas: Los cinemómetros podrán llevar además inscripciones autorizadas por la Administración Pública competente siempre que dichas inscripciones no entorpezcan la lectura de las indicaciones suministradas por el instrumento.

7.2 Precintos.–Deben poder ser precintados aquellos elementos donde la manipulación puede conducir a errores de medida o a una reducción de la seguridad metrológica.

En la memoria técnica presentada para el examen de modelo se indicará el lugar de estos precintos así como su naturaleza.

> Redactado el apartado 2.2 conforme a la corrección de erratas publicada en BOE núm. 12, de 14 de enero de 2011. Ref. BOE-A-2011-695.
