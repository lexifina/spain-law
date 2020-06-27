## ANEXO H

## Requisitos del registrador jurídico

(La información recogida en este anexo es a título informativo, a excepción del apartado H.3.3 que es normativo)

H.1 Objeto. El objeto de este anexo es establecer los requisitos generales, técnicos y funcionales que deberá reunir y cumplir una unidad de grabación embarcada.

Una unidad de grabación es un sistema embarcado destinado a registrar información relevante sobre la circulación del tren, compuesto por un hardware, un software e interfaces de E/S de datos, y que deberá soportar unas severas solicitaciones físicas y ambientales.

Por lo tanto, y de acuerdo a esta definición, los temas genéricos que deberán estudiarse para establecer los requisitos para la unidad de grabación son:

– Especificaciones funcionales del sistema.

– Especificaciones técnicas del sistema.

– Parámetros a registrar.

– Descarga de los registros.

– Proceso de validación.

Consecuentemente, este documento abarca y define los puntos anteriores, estableciendo en todos los casos los mínimos requerimientos que se recomienda que reúna un sistema de grabación de datos jurídicos para ser apto y adecuado al uso. A excepción, de los requerimientos indicados en el apartado H.3.3, los cuales son de obligado cumplimiento siempre y cuando el vehículo a validar disponga de sistema ASFA.

H.2 Especificaciones funcionales y técnicas del sistema. En el presente apartado se incluyen las especificaciones funcionales y técnicas que deberán cumplir los equipos de registro de datos embarcados en el vehículo.

Los requisitos mínimos que se consideran son los siguientes:

H.2.1 Especificaciones funcionales.

H.2.1.1 Funciones genéricas de la unidad de grabación. La información deberá tratar los siguientes elementos:

– Magnitudes cinemáticas de la circulación.

– Sucesos operacionales (funciones de ERTMS, ASFA, LZB, etc.).

– Acciones del maquinista y el comportamiento consecuente de la unidad de tracción.

– El funcionamiento de la infraestructura de vía (información intercambiada entre vía y vehículo).

– Operaciones de los equipos embarcados seleccionados y sus cambios de estado asociados, que afecten la operación segura del vehículo.

– Información diagnóstica como posible elección nacional (por ejemplo, estado de los equipos, códigos por defecto, etc.).

H.2.1.2 Requisitos de la unidad de grabación. Para el material rodante nuevo que tenga más de una cabina con unidad de grabación, toda la información se recogerá en la unidad de grabación de la cabina que esté habilitada en ese momento. Este requisito es recomendable para el material reacondicionado.

La unidad de grabación se compondrá de un sistema embarcado que incluirá una memoria ignífuga que será recuperable cumpliendo los requisitos post-accidente especificados en el apartado H.2.2.6.

Si el material rodante incorpora un registrador de voz instalado a bordo, este cumplirá los siguientes requisitos:

– Calidad: El dispositivo deberá registrar con una calidad tal que permita evaluar las conversaciones mantenidas en la cabina, así como las señales de advertencia en la cabina, en las peores condiciones de ruido proveniente del exterior (tren a velocidad máxima).

– Capacidad: La capacidad de almacenamiento del dispositivo, en condiciones normales de servicio del tren, no será inferior a 30 minutos de funcionamiento en memoria CPM.

– Activación/desactivación: El dispositivo permanecerá activado si la velocidad es superior a 0 km/h y la cabina de conducción está activa.

En cuanto a los requisitos técnicos, el registrador de voz deberá cumplir lo establecido para el registrador jurídico o unidad de grabación en el apartado H.2.2 de este Anexo. Existirá además una sincronización entre la grabación de voz y los datos del registrador jurídico que permita el análisis conjunto.

H.2.1.3 Compatibilidad. La extracción de los datos deberá ser lo más estándar posible para asegurar, con el paso del tiempo, el acceso a los mismos independientemente del software empleado.

H.2.1.4 Color. La unidad de grabación deberá ser de color RAL2003 y debe estar claramente identificada.

H.2.1.5 Activación y auto-diagnosis. La unidad de grabación deberá activarse automáticamente cuando el maquinista active la consola de conducción de la unidad tractora. A continuación, el equipo deberá iniciar su proceso de auto-diagnosis para establecer si está en condiciones de operar correctamente.

La duración de la auto-diagnosis no excederá los 20 segundos ni requerirá la interacción del maquinista. El resultado se indicará al maquinista, y se registrará en la unidad de grabación.

H.2.1.6 Interfaz con el maquinista. El maquinista dispondrá de una indicación visual en la cabina de conducción que indique si la unidad de grabación no puede desempeñar las funciones requeridas o si el resultado de la auto-diagnosis resulta negativo.

H.2.1.7 Exigencias de operatividad. La unidad de grabación será operativa, como mínimo, desde 0 km/h hasta la velocidad máxima del vehículo aumentada en un 10%.

La velocidad, y cualquier otra información, deberán ser registradas con una precisión que permita reconstruir fielmente los hechos relevantes acontecidos durante la conducción.

La resolución de registro de la señal de velocidad será como mínimo de 5 km/h. La resolución de presentación será ésta misma.

H.2.1.8 Entradas y salidas de señales. El equipo dispondrá de las suficientes entradas y salidas como para procesar, al menos, todos los parámetros a registrar indicados en el apartado H.3, independientemente del vehículo de que se trate.

La precisión en la medida de señales analógicas, incluido cálculos de ajuste de escala, será de al menos un 2%.

El sistema estará equipado con las entradas suficientes para recibir la señal de los tacogeneradores.

El sistema estará equipado, como mínimo, con 8 salidas que preferentemente serán contactos de relé.

H.2.1.9 Período de retención de los datos. Representa el mínimo período de tiempo durante el cual la integridad de los datos almacenados en el soporte de memoria debe ser garantizada cuando éste ha sido extraído del vehículo (fuera de línea) o cuando el sistema de a bordo esté desconectado.

En el caso de estar desconectada de la alimentación, la memoria del registro mantendrá la información registrada durante al menos dos años en condiciones nominales de almacenamiento.

H.2.2 Especificaciones técnicas.

H.2.2.1 Condiciones de funcionamiento, diseño, construcción y ensayos. En lo que se refiere a los requisitos sobre las condiciones de funcionamiento, diseño, construcción y ensayos, serán de aplicación la especificación técnica indicada en el anexo C, cuadro C.2, índice [39].

Todos los ensayos se realizarán conforme a las especificaciones indicadas en la especificación técnica indicada en el anexo C, cuadro C.2, índice [40].

– Condiciones ambientales:

• Temperatura: Se aplicará la categoría T3 establecida en la especificación técnica indicada en el anexo C, cuadro C.2, índice [41].

• Grado de Humedad: Las partes mecánicas, cajas, tapas, etc., llevarán un tratamiento anticorrosión adecuado para operación en ambientes salinos cercanos a la costa. En las superficies enfriadas puede haber un 100 % de humedad relativa que dé lugar a condensación sobre algunas partes de los equipos; esto no deberá dar lugar a un mal funcionamiento de los mismos. El equipo deberá soportar una humedad relativa del 95% durante al menos 30 días seguidos.

• Altitud: La elección de componentes tendrá en cuenta que deberán poder operar a altitudes en nivel del mar y 1500 metros sobre éste.

– Vibraciones, choques y sacudidas: En lo que se refiere al ensayo de vibraciones, choques y sacudidas, el equipo deberá soportar los límites indicados en la especificación técnica indicada en el anexo C, cuadro C.2, índice [42]. Estos límites son:

• Vibraciones: El equipo deberá soportar los ensayos válidos para un equipo de categoría 1B (tablas 1 y 2 de los apartados 8 y 9 de la citada norma).

• Choques y sacudidas: Deberá garantizarse que los equipos, de categoría 1B, soportan los siguientes niveles de aceleración:

Cuadro H.2.2.1 Niveles de aceleración en choques y sacudidas

|  | Vertical | Transversal | Longitudinal |
| --- | --- | --- | --- |
| Nivel de aceleración (g). | 30 m/s2 durante 30 ms | 30 m/s2 durante 30 ms | 50 m/s2 durante 30 ms |

Adicionalmente, deberá funcionar correctamente ante solicitaciones introducidas por el funcionamiento normal del vehículo. En particular deberá soportar aceleraciones longitudinales de hasta 7 m/s2, con duraciones superiores a 50 ms, introducidas por la tracción o el frenado del vehículo.

– Componentes: Los componentes electrónicos a usar tendrán al menos rango industrial.

La elección de componentes tendrá en cuenta segundas fuentes de suministro y continuidad de éste, para garantizar el mantenimiento de los equipos por 20 años.

La elección de componentes tendrá en cuenta que se usarán en vehículos que prestarán servicio en túneles.

H.2.2.2 Condiciones eléctricas.

– Unidad de alimentación: La unidad de alimentación se surtirá de la línea de batería, y proporcionará la alimentación necesaria para el funcionamiento de todo el equipo.

Se adaptará, como mínimo, a una de las siguientes tensiones normalizadas: 24 V, 48 V, 72 V, 110 V; para cada una de ellas, estará preparada para trabajar dentro del rango de tensiones situado entre -30% / +25%. Si se pudiera adaptar automáticamente a más de una de estas tensiones, el rango de trabajo sería Umin – 30% - Umax + 25%.

La unidad de alimentación se adaptará a las especificaciones indicadas en la especificación técnica indicada en el anexo C, cuadro C.2, índice [43].

– Requisitos de compatibilidad electromagnética: Se cumplirá con lo establecido en la especificación técnica indicada en el anexo C, cuadro C.2, índice [44].

Se cumplirá con los requisitos EMC y con las condiciones eléctricas de servicio especificadas en la especificación técnica indicada en el anexo C, cuadro C.2, índice [45] y de acuerdo a los ensayos referidos dicha especificación.

– Seguridad eléctrica: Respecto a la seguridad de las personas relativa a riesgos eléctricos, será de aplicación la especificación técnica indicada en el anexo C, cuadro C.2, índice [46].

Así, como protección contra el contacto indirecto, el equipo contará con una toma de tierra que garantice la seguridad de las personas en caso de derivación eléctrica, y las partes mecánicas, cajas, tapas, etc., deberán disponer del correspondiente contacto directo con tierra.

Para la protección contra el contacto directo, se contemplarán los requisitos citados en la anterior norma (acceso a zonas activas y grados de protección).

– Instalación: La instalación del equipo electrónico deberá disponerse de forma que se reduzcan, lo máximo posible, los efectos de las interferencias externas.

H.2.2.3 Fiabilidad del equipo. El parámetro utilizado para el estudio de fiabilidad será el MTBF (tiempo medio entre fallos).

Los tipos de fallos se describirán y clasificarán, excluyendo los de propagación radioeléctrica, proporcionando una descripción de cada fallo, características, causas, probabilidad de aparición y posibles consecuencias en el Sistema.

Se especificarán los valores esperados para los índices de fiabilidad de cada uno de los subsistemas principales.

Deberá entregarse la documentación necesaria para garantizar la seguridad global del sistema. Para ello, deberá elaborarse un estudio FDMS (fiabilidad, disponibilidad, mantenibilidad y seguridad) de acuerdo con la especificación técnica indicada en el anexo C, cuadro C.2, índice [47].

H.2.2.4 Vida útil. La vida útil del equipo se fija en 30 años. Se entiende por vida útil el periodo de tiempo durante el cual el equipo debe mantenerse dentro de unos niveles de fiabilidad aceptables o aquel dentro del cual no se produce un fallo irreparable.

Cuando el fabricante utilice componentes con una vida conocida menor que la vida útil del equipo electrónico, deberá garantizar su reposición para conseguir la vida útil exigida. No obstante, si por obsolescencia tecnológica no fuese posible su reposición, se sustituirán por otros componentes similares de manera que se mantenga el conjunto total de funcionalidades del equipo conforme a la especificación técnica indicada en el anexo C, cuadro C.2, índice [48].

H.2.2.5 Mantenimiento del equipo.

– Se tendrán en cuenta los siguientes factores para asegurar el mantenimiento del equipo:

• Mantenibilidad. El equipo tiene que ser mantenible, para ello se contemplarán las siguientes premisas que influyen en la mantenibilidad:

No deberá ser necesario un mantenimiento regular.

Se podrá comprobar la operatividad de las tarjetas módulos que componen el sistema individualmente.

La instalación del equipo no debe impedir el correcto acceso a otros sistemas instalados en el vehículo.

Todas las tarjetas estarán polarizadas mecánicamente para evitar errores de conexión de las mismas.

Las tarjetas estarán protegidas contra las posibles descargas electrostáticas provocadas por su manipulación manual. La protección se realizará por medios que aislarán del contacto, tanto con componentes, como con soldaduras.

Será de aplicación la especificación técnica indicada en el anexo C, cuadro C.2, índice [49], que constituirá una base de diseño en esta materia.

• Sistemas de autodiagnosis integrados. El equipo dispondrá de sistemas de autotest (checksum, watchdog, hardware, etc.), que verificarán la operatividad del sistema. Sería conveniente que se generase un registro de incidencias que incluyera los siguientes datos:

Contador de incidencias almacenadas.

Fecha y hora en que ocurre la incidencia.

Código de error.

Estos datos se podrán visualizar en la consola del equipo. Si ésta no está operativa se podrá acceder a estos datos a través de una línea de control.

– Condiciones de inflamabilidad. Se tendrán en cuenta las siguientes prescripciones generales:

• Minimizar el riesgo de auto-ignición de un fuego que comience en un componente de un equipo debido a fenómenos eléctricos anormales, tales como sobrecarga, cortocircuito, contactos defectuosos, envejecimiento térmico prematuro, etc.

• Resistir al fallo cuando se encuentre expuesto a fuegos inducidos, mediante el empleo de cableados y recubrimientos adecuados de los mismos.

• Minimizar el humo y los gases nocivos emitidos en el caso de que el equipo se incendie.

H.2.2.6 Requisitos post-accidente. La memoria protegida de la unidad de grabación será capaz de soportar los siguientes efectos tras un accidente, sin que se pierda ni altere la información almacenada y permitiendo su extracción:

– Se cumplirán los criterios de compatibilidad electromagnética de la especificación técnica indicada en el anexo C, cuadro C.2, índice [50].

– Fluidos y sus componentes, tales como: alcohol, anticongelante, carburante diésel, fluidos hidráulicos, aceites lubricantes, ácido de batería, etc.

– Agua y polvo: Se garantizará un nivel de protección mínimo IP 67.

– El sistema de almacenamiento dispondrá de conexión serie tipo Dsub9 (RS-232 hembra) para el acceso a la información registrada en caso de accidente, estando de acuerdo con lo indicado en la norma SUBSET-027 para la descarga de datos del sistema ETCS. Se aceptarán también conexiones tipo RJ-45 estándar (Ethernet), USB 2.0 o superior (pasivo).

El sistema no deberá emitir ninguna polución nociva en el caso de que le suceda cualquier incidente.

H.3 Parámetros a registrar. En este apartado se incluye un listado de parámetros que deben registrar los equipos.

Se ha organizado de forma que primero se muestran las señales de cabecera, donde se recogen aquellas señales que deben estar almacenadas en el equipo al inicio de cualquier trayecto. Éstas pueden ser introducidas bien por el maquinista, bien porque alguno de los parámetros fundamentales haya cambiado o bien porque algún fallo de la alimentación haya provocado su pérdida.

A continuación se incluyen las señales a registrar como datos de cabecera, generales y en función del sistema que lleve activo el vehículo. Sólo se consideran las señales adicionales a las ya especificadas por el apartado 4.2.3.5 de la ETI de explotación y gestión del tráfico.

H.3.1 Datos de cabecera.

– Velocidad máxima del vehículo.

– Porcentaje de freno del tren.

– Diámetro de rueda.

Los datos de fecha y hora del registrador provendrán de un reloj propio, que sea fiable, seguro y no manipulable externamente, excepto mediante sistemas de actualización permanente de la hora (por ejemplo, GPS) o en operaciones de mantenimiento en taller homologado, en cuyo caso quedará registrado este evento.

Los datos del LZB se registrarán en el equipo cuando no exista STM LZB. En caso contrario, formarán parte del registro ETCS. Se procederá de la misma forma con cualquier otro sistema que en el futuro se decida implementar como STM.

H.3.2 Generales.

– Estado de la unidad de grabación (on/off/error).

– Recorrido actual (m).

– Velocidad registrada por el velocímetro.

– Velocidad prefijada conectada.

– Sentido de la marcha/posición del inversor.

– Puertas del vehículo autopropulsado cerradas.

– Puertas izquierdas desbloqueadas.

– Puertas derechas desbloqueadas.

– Operaciones del tren terminadas (si está implementado).

– Dispositivo de vigilancia (HM) en servicio.

– Dispositivo de vigilancia (HM) anulado.

– Freno de emergencia por dispositivo de vigilancia (HM).

– Freno de emergencia por accionamiento manual (seta, freno neumático máximo).

– Presión de la tubería de freno automático OK.

– Freno directo activado.

– Elevada temperatura de las cajas de grasa.

– Alarma de viajeros activada.

– Señales luminosas por cabeza y cola activas (en unidades autopropulsadas).

H.3.3 ASFA.

– 7 canales digitales para el registro de las informaciones del ASFA conforme al documento de la especificación técnica indicada en el anexo C, cuadro C.2, índice [51].

– Registro de velocidad ASFA

Si la unidad de grabación embarcada dispone de puerto de entrada RS-485, el registro de las informaciones del ASFA podrá realizarse mediante éste en vez de a través de los 7 canales digitales.

H.3.4 LZB.

– Transmisión LZB.

– Prueba funcional.

– Rebase de punto de parada.

– Freno automático.

– Freno emergencia.

– autorización.

– Posiciones de los conmutadores LZB de aislamiento y de defecto.

– Rebasar.

– Liberar.

– Alertar, si procede.

– Cambio de sentido del recorrido.

– Presión adecuada en TFA.

– Error telegrama LZB (deseable).

– Tipo de freno (TF).

– Porcentaje de freno (PFT).

– Velocidad máxima del tren (VMT).

– Longitud del tren.

– Diámetro rueda 1.

– Diámetro rueda 2.

– Vcons.

– Vreal.

– Magnitudes V-meta y D-meta apagadas.

– Deceleración de frenado.

– Bloqueo parcial.

H.3.5 ETCS. La unidad de grabación debe ser capaz de registrar y de producir un output de la información almacenada para permitir su análisis mediante sistemas externos, de acuerdo con el listado de parámetros prescrito en el documento SUBSET-027.

H.4 Metodología de ensayo a componente. El proceso de validación como componente del registrador jurídico o unidad de grabación embarcada, y del registrador de voz si lo incorpora el material rodante, comprenderá las siguientes fases de evaluación:

– Fase de análisis de diseño y ensayo de tipo. Se comprobará el cumplimiento de todos los requisitos mencionados en este anexo mediante certificado del fabricante y mediante las pruebas que se establezcan en el protocolo.

– Fase de ensayo de serie. Se comprobará que todas las interfaces previstas funcionan correctamente.
