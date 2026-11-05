## ANEXO I

## Requisitos técnicos del sistema REM para la obtención de ayudas para la adquisición e instalación de sistemas de seguimiento electrónico remoto (REM) conforme al artículo 1.1 a)

De forma común para todas las pesquerías, los sistemas de observación deben ser capaces de monitorizar todas y cada una de las operaciones de pesca. Éstas deben estar geo-referenciadas e incluir hora y fecha de comienzo y final de todas las actividades registradas.

El sistema de observación electrónica debería estar compuesto, por instrumentos con marcado CE y al menos, por los siguientes componentes:

Unidad central con las siguientes características:

– Los requisitos técnicos mínimos que debe cumplir la unidad central son los siguientes:

• Capacidad para controlar todos los componentes embarcados:

• Capacidad para grabar toda la información relevante de interés capturada por el sistema de observación electrónica

• Capacidad para encriptar los datos almacenados.

– Disponer de capacidad de almacenamiento suficiente para todos los datos necesarios durante el período de operación del buque que se va a monitorizar:

• Almacenamiento en discos duros extraíbles compatibles con los sistemas de gestión de datos

• Contar con almacenamiento de respaldo, para prevenir pérdidas de datos.

– Estar adaptada para ser instalada a bordo de un barco y contar con:

• Alimentación mediante tensión adaptada a la instalación del buque.

• Un sistema de fijación apropiado.

– Soportar un interfaz de usuario a bordo

– Disponer de capacidad para conectividad.

Interfaz de usuario.

– Dotado de una pantalla de visualización conectada a la unidad central para permitir visualizar la imagen de las cámaras y los indicadores de estado del equipo.

– Puede incluir un dispositivo que permita la entrada de datos a los usuarios: pantalla táctil o teclado y ratón.

Cámaras que permitan visualizar todas las operaciones de pesca objeto de monitorización.

Las cámaras utilizadas por el sistema de observación electrónica deben cumplir los siguientes requisitos mínimos:

– Tener conexión de tipo IP.

– Contar con un grado de protección IP66 o superior.

– Conectividad mediante cable Ethernet de categoría CAT5E o superior.

– Estar dotadas de una óptica ajustable (comprendiendo al menos, enfoque y apertura)

– Garantizar la caracterización de su óptica para la calibración de áreas de medición sobre la imagen.

– Garantizar el enmascaramiento de áreas de la imagen para aquellas zonas que no sea necesario grabar.

– Garantizar las condiciones de resolución de las imágenes que permitan la posterior gestión de datos.

Formato de información registrada.

– Al objeto de garantizar que la información gráfica registrada posibilite su análisis, el formato de dicha información debe cumplir los siguientes requisitos mínimos:

• Soportar encriptación simétrica (cifrado AES-256 o superior) o asimétrica (algoritmo criptográfico de curva elíptica o similar).

• Tener la capacidad de asegurar la integridad de los datos.

– Imagen:

Soportar una resolución de 1080p (1920x1080) para imágenes fijas.

Disponer de tasa de captura de imágenes configurable según la actividad a monitorizar.

– Video:

Soportar una resolución de al menos 720p (1280x720) para vídeo.

Disponer una tasa de fps configurable no siendo menor de 10 fps.

Soportar algoritmos de compresión de vídeo H.264 o H.265.

Sistema de geolocalización.

Debe permitir geolocalizar la embarcación para registrar la ubicación del buque junto con la fecha y la hora en la que se realiza la captura de datos.

Sistema de alimentación ininterrumpida.

Una unidad de alimentación ininterrumpida que proporcione al menos 15 minutos de autonomía sin alimentación del barco.

Sistemas de comunicaciones.

El sistema de observación electrónica debe soportar, al menos, uno de los siguientes interfaces de comunicación:

– Comunicaciones móviles 3G, 4G o 5G.

– Wi-Fi 802.11n.

– Comunicaciones por satélite.

– Puerto Ethernet, u otro sistema de comunicación, que permita la transmisión de datos y el acceso remoto al sistema a través de la conexión a Internet existente a bordo, en su caso.

Sensores.

El sistema de observación electrónica debe ser capaz de registrar lecturas de sensores tanto analógicos como digitales.

Para los supuestos de contar con sensores instalados, estos deben ser capaces de dar información sobre los parámetros siguientes, que aplicarán en función del tipo de buque y arte de pesca:

– Rotación de maquinillas (con contador para detección de velocidad de rotación).

– Presión hidráulica.

– Corriente eléctrica.

– Apertura y cierre de puertas (para embarque de pescado, cubas de congelación, etc.)

– Temperatura de tanques de refrigeración.

– Activación de cintas transportadoras.

– Apertura o cierre de válvulas.

– Funcionamiento de haladores.

– sobre cualquier otro componente de interés relevante

Herramientas de diagnóstico del sistema.

El sistema de observación electrónica debe ser capaz de aportar información sobre su estado de funcionamiento y posibilitar la realización de los procesos de comprobación descritos en los siguientes apartados:

Comprobaciones iniciales sobre el sistema.

El sistema debe permitir la realización de comprobaciones previas que garanticen su correcto funcionamiento con anterioridad al inicio de las operaciones pesqueras que se van a monitorizar.

Eventos y alarma del sistema.

El sistema de observación electrónica debe permitir registrar los principales eventos que puedan afectar a la toma de datos, tales como:

– Corte de alimentación.

– Apagado del equipo.

– Fallo o pérdida de conexión de las cámaras.

– Cambio de configuración del equipo.

– Pérdida de cobertura.

– Inicio y fin de grabación de imágenes de cada cámara.

– Activación y desactivación de disparadores de grabación.

– Alarma de llenado de discos.

Estación de análisis en tierra.

La estación de análisis en tierra estará formada por:

Programa de análisis de datos (Software).

El software de análisis debe tener, al menos, las siguientes funcionalidades:

– Capacidad de desencriptación de la información recogida por el sistema de observación electrónica.

– Visualización de traza del buque sobre mapa.

– Visualización de rumbo y velocidad del buque.

– Visualización de las imágenes o vídeos registrados por todas las cámaras.

– Visualización de información de validación de origen de la información (nombre del buque, fecha, hora y posición del momento de la captura de la imagen).

– Visualización de información de sensores.

– Posibilidad de calibración de dimensiones de área sobre la imagen para la realización de medidas.

– Edición de anotaciones.

– Capacidad para interacción con bases de datos para almacenamiento de la información.

– Capacidad de extracción de la información almacenada en la base de datos en los formatos solicitados.

– Capacidad para exportación de evidencias de que la información procesada es precisa y que permita garantizar la trazabilidad de los datos almacenados.

– Opcionalmente, podrá incorporar herramientas de ayuda a los observadores basados en machine learning.

Las zonas objeto de observación electrónica más relevantes en función de la pesquería se desglosan a continuación:

– Arrastre (Fondo y pelágico).

C.1 Palangre de superficie.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Zona de largada (popa). | Largada del aparejo. | Descripción del aparejo. | Número de secciones, cestas y anzuelos utilizados. |
| Información de la carnada. | Tipo de cebo. |
| Uso de dispositivos y/o métodos de mitigación. | Identificación de dispositivos y/o métodos de mitigación (líneas tori, lanzadera, trabajo nocturno, etc.). |
| Zona de virada. | Virada del aparejo. | Captura de especies objetivo. | Identificación especies, número total por lance, talla y devenir. |
| Captura de especies accesorias. | Identificación de especies, número y devenir, y posición del anzuelo. |
| Interacciones con especies ETP. | Identificación de especies, número y devenir y posición del anzuelo. |
| Depredación. | Número total de especímenes depredados por lance. |
| Pantano1. | Estimación talla- peso. | Captura de especie objetivo. | Identificación de especies retenidas, talla y número total por especie y lance. |
| Posición del anzuelo. |
| Parque de pesca1. |
| 1 De aplicación según la estructura de las embarcaciones. |

C.2 Palangre de fondo.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Zona de largada. | Largada del aparejo. | Geolocalización caceas. | Inicio y fin de caceas. |
| Zona de virada. | Virada del aparejo. | Captura de especies objetivo. | Identificación especies, número total por lance, talla y devenir. |
| Estimación del descarte. | Identificación de especies y número/peso. |
| Captura de especies accesorias. | Identificación de especies, número y devenir. |
| Interacción con especies ETP. | Identificación de especies, número y devenir. |
| Parque de pesca. | Procesado. | Captura de especie objetivo. | Identificación de especies retenidas, talla y número total por especie y lance. |

C.3 Cerco congelador.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Cubierta de trabajo. | Salabardeo. | Captura total por lance. | Número de salabardos y porcentaje llenado de cada salabardo. |
| Composición por especies de la captura. | Peso, talla y especies retenidas de túnidos. |
| Descarte túnidos. | Descarte total de túnidos por lance. | Peso, talla y especies descartadas de túnidos. |
| Gestión de especies accesorias. | Estimación de especies accesorias. | Identificación de especies y número de individuos o peso según modo de manipulación. |
| Liberación especies accesorias. | Total de especies accesorias por lance. | Número de individuos e identificación por especie. |
| Área de saco en el agua. | Salabardeo. | Total de captura por lance. | Número de salabardos y porcentaje de llenado de cada salabardo. |
| Gestión especies accesorias grandes (tiburón ballena, mantas, etc.). | Interacción con especies ETP. | Modo de manipulación e identificación de especie. |
| Área de red en el agua (cerco). | Lance del arte. | Identificación del lance. | Hora y posición de inicio y fin del lance. Identificación del tipo de lance y maniobras con DCPs. |
| Proa, centro o cubierta provista de grúa 1. | Actividad con DCP/FADs (plantado, sustitución, reparación, etc.). | Número total de actividades con DCP/FADs por marea. | Actividad, diseño y materiales del DCP/FADs. |
| Cubierta parque de pesca y cinta transportadora. | Triado de la captura. | Composición por especies de la captura. | Proporción de especies retenidas de túnidos y tallas. |
| Descarte túnidos. | Descarte total de túnidos por lance. | Peso, talla y especies descartadas de túnidos. |
| Gestión de especies accesorias. | Estimación de especies accesorias por lance. | Identificación de especies y número de individuos o peso según modo de manipulación. |
| 1 De aplicación en buques auxiliares para atuneros. |

C.4 Cerco de pequeños pelágicos.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Cubierta de trabajo. | Salabardeo y estiba de la captura. | Captura total por lance. | Estimación de captura total dividida por especie. |
| Composición por especies de la captura. |
| Descarte de pequeños pelágicos desde cubierta. | Descarte total por lance. | Estimación peso total descartado. |
| Área de la red en el agua. | Lance. | Identificación del lance. | Hora y posición de inicio y fin del lance. |
| Volteo del saco o «Slipping». | Estimar cantidad de captura liberada desde el saco. | Estimación de peso total. |
| Gestión de especies accesorias grandes (cetáceos, etc.). | Interacción con especies ETP. | Modo de manipulación e identificación de especie. |

C.5 Cebo vivo.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Cubierta de trabajo. | Lance | Identificación del lance | Hora y posición de inicio y fin de la parada |
| Captura mediante caña y sedal1 | Captura total de especies objetivo por lance | Estimación de captura total por especie, talla |
| Captura de especies accesorias | Identificación de especie, número y devenir |
| Interacción con especies ETP | Identificación de especie, número y devenir |
| 1 Cobertura de todas las cañas y de las cajoneras donde se dejan las capturas de cada lance para posteriormente introducirlas en las bodegas o en su caso, de la cinta transportadora que traslada la captura a bodega. |

C.6 Cacea.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Ambas bandas y popa. | Captura mediante carrete y sedal1. | Captura total de especies objetivo. | Estimación de captura total por especie y talla. |
| Captura de especies accesorias. | Identificación de especie, número y devenir. |
| Interacción con especies ETP. | Identificación de especie, número y devenir. |
| 1 Cobertura de todos los carreteles (babor y estribor) y de la zona del barco donde se dejan las capturas de cada lance para posteriormente introducirlas en bodega. |

C.7 Arrastre (fondo y pelágico).

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Cubierta de trabajo y rampa de popa. | Embarque del arte. | Interacción con especies ETP. | Identificación de especie, número y devenir. |
| Vaciado del copo. | Captura total del lance. | Estima de la captura total. |
| Parque de pesca. | Triado de la captura. | Captura total del lance y de especies objetivo por lance. | Estimación de captura total por especie y talla. |
| Interacción con especies ETP. | Identificación de especie, número y devenir. |
| Trancanil. | Descarte de especies no objetivo. | Estimación del descarte. | Identificación de especie, peso total y talla. |

C.8 Volanta.

| Área del buque a cubrir | Acción de pesca a cubrir | Objetivo | Requisitos básicos de observación |
| --- | --- | --- | --- |
| Zona de largada. | Largada del aparejo. | Geolocalización aparejo. | Localización de baliza de inicio y fin. |
| Zona de virada. | Virada del aparejo. | Captura de especies objetivo. | Identificación especies, número total por lance, talla y devenir. |
| Estimación del descarte. | Identificación de especies y número/peso. |
| Captura de especies accesorias. | Identificación de especies, número y devenir. |
| Interacción con especies ETP. | Identificación de especies, número y devenir. |
| Parque de pesca o cubierta de trabajo. | Procesado. | Captura de especie objetivo. | Identificación de especies retenidas, talla y número total por especie y lance. |
