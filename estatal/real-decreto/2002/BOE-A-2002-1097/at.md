## APÉNDICE T

## Mensajes de los servicios de tránsito aéreo

1. Contenido y formato de los mensajes y presentación convencional de los datos.

Para facilitar la descripción del contenido y formato de los mensajes de los servicios de tránsito aéreo, destinados tanto al intercambio entre dependencias que no dispongan de equipo para el tratamiento automático de datos como para los intercambios entre computadoras del control de tránsito aéreo, los elementos de datos que han de incluirse en los mensajes se agrupan por «campos». Cada campo contiene un solo elemento o un grupo de elementos relacionados entre sí.

1.1. Tipos normalizados de mensajes.

1.1.1. Los tipos normalizados de mensajes, establecidos para el intercambio de datos ATS, junto con los correspondientes designadores de tipo de mensaje, son los siguientes:

| Categoría de mensaje | Tipo de mensaje | Designador del tipo de mensaje |
| --- | --- | --- |
| Emergencia | Alerta | ALR |
| Fallo de radiocomunicaciones | RCF |
| Plan de vuelo presentado y actualizado correspondiente | Plan de vuelo presentado | FPL |
| Modificación | CHG |
| Cancelación | CNL |
| Demora | DLA |
| Salida | DEP |
| Llegada | ARR |
| Coordinación | Plan de vuelo actualizado | CPL |
| Estimación | EST |
| Coordinación | CDN |
| Aceptación | ACP |
| Acuse de recibo lógico | LAM |
| Suplementarios | Solicitud de plan de vuelo Solicitud de plan de vuelo | RQP |
| Solicitud de plan de vuelo suplementario | RQS |
| Plan de vuelo suplementario | SPL |

1.2. Tipos normalizados de campo.

1.2.1. Los datos que pueden figurar en un campo de mensajes ATS son los indicados en la tabla siguiente. Los números de la columna 1 corresponden con los indicados en la Figura T-1.

| Tipo de campo | Datos |
| --- | --- |
| 3 | Tipo, número y datos de referencia del mensaje |
| 5 | Descripción de la emergencia |
| 7 | Identificación de la aeronave y modo y clave SSR |
| 8 | Reglas de vuelo y tipo de vuelo |
| 9 | Número y tipo de aeronave y categoría de estela turbulenta |
| 10 | Equipo |
| 13 | Aeródromo de salida y hora |
| 14 | Datos estimados |
| 15 | Ruta |
| 16 | Aeródromo de destino y duración total prevista, aeródromo(s) de alternativa |
| 17 | Aeródromo de llegada y hora |
| 18 | Otros datos |
| 19 | Información suplementaria |
| 20 | Información de alerta referente a búsqueda y salvamento |
| 21 | Información referente al fallo de las comunicaciones |
| 22 | Enmienda |

1.3. Composición de los tipos normalizados de mensaje.

1.3.1. La composición de cada tipo normalizado de mensaje, expresado por una sucesión normalizada de campos de datos se ajustará a lo prescrito en la tabla de referencia de la Figura T-1. Los mensajes deberán contener todos los campos prescritos.

1.4. Composición de los tipos normalizados de campo.

1.4.1. La composición de los tipos normalizados de campo expresada por una sucesión normalizada de elementos de datos o en algunos casos por un simple elemento, se ajustará a lo prescrito en las tablas de campos de OACI.

1.4.1.1. Cada tipo de campo contendrá obligatoriamente por lo menos un elemento que, excepto en el tipo de campo 9, será el primero o el único elemento del campo. Las normas para la inclusión u omisión de los elementos condicionales se indican en las tablas de campos.

1.5. Estructura y puntuación.

1.5.1. El principio de los datos ATS se indicará en las copias de página mediante un paréntesis «(», que constituirá la señal del comienzo de los datos ATS. Esta señal se utilizará solamente como el carácter impreso, que precede inmediatamente al designador del tipo del mensaje.

1.5.2. El principio de cada campo, salvo el primero, se indicará mediante un guion, «-», que representa la señal de principio de campo. Dicha señal se utilizará únicamente como carácter impreso que precede al primer elemento de los datos ATS de cada campo.

1.5.3. Los elementos que constituyen un campo se separarán mediante una barra oblicua «/», o un espacio (esp.) únicamente cuando así lo prescriban las tablas de campos de OACI.

1.5.4. El fin de los datos ATS se indicará mediante un paréntesis cerrado «)», que constituirá la «señal de fin de datos ATS». Esta señal se utilizará únicamente como el carácter impreso que sigue inmediatamente al último campo del mensaje.

1.5.5. Cuando los mensajes ATS normalizados se preparen en la forma propia del teletipo, se insertará una función de alineación (dos retornos del carro seguidos de una alimentación de línea):

a) antes de cada uno de los campos indicados en la Figura T-1;

b) en los tipos de campo 5 (descripción de la emergencia), 15 (ruta), 18 (otros datos), 19 (información suplementaria), 20 (información de alerta referente a búsqueda y salvamento), 21 (información referente a fallo de las comunicaciones) y 22 (enmienda), siempre que sea necesario empezar una nueva línea de la copia de la página impresa (1). En dichos casos, la función de alineación se insertará entre dos elementos de datos, sin dividir los elementos.

(1) Las líneas de las copias de teletipo no contendrán más de 69 caracteres.

1.6. Representación convencional de los datos.

1.6.1. La representación convencional que debe utilizarse para indicar la mayor parte de los datos de los mensajes ATS se prescribe en las tablas de campos de OACI, pero la representación correspondiente a los datos de nivel, posición y ruta se indican a continuación para simplificar las tablas de campos.

1.6.2. Expresión de los datos correspondientes al nivel.

1.6.2.1. Para expresar los datos correspondientes al nivel se pueden utilizar las cuatro representaciones siguientes:

a) «F» seguida de 3 cifras: indica el número del nivel de vuelo, es decir, el nivel de vuelo 330 se expresa por «F330»;

b) «S» seguida de 4 cifras: indica el nivel normalizado en decenas de metros, es decir, que el nivel métrico normalizado de 11.300 m (nivel de vuelo 370) se expresa por «S1130»;

c) «A» seguida de 3 cifras: indica la altitud en centenas de pies, es decir, una altitud de 4.500 pies se expresa por «A045 »;

d) «M» seguida de 4 cifras: indica la altitud en decenas de metros, es decir, una altitud de 8.400 metros se expresa por «M0840».

1.6.3. La expresión de la posición o de la ruta.

1.6.3.1. Al expresar la posición o ruta se pueden utilizar las siguientes representaciones convencionales:

a) de 2 a 7 caracteres, correspondientes al designador cifrado asignado o la ruta ATS que debe recorrerse;

b) de 2 a 5 caracteres, correspondientes al designador cifrado designado como punto de la ruta;

c) 4 cifras indicadoras de la latitud en grados y en decenas y unidades de minuto, seguidas de «N» (para indicar el Norte) o «S» (Sur), seguidas de 5 cifras indicadoras de la longitud en centenas, decenas y unidades de grado y en decenas y unidades de minuto, seguidas de «E» (Este) o «W» (Oeste). Para completar la cantidad de cifras necesaria pueden utilizarse ceros, como, «4620N07805W»;

d) 2 cifras correspondientes a la latitud en grados, seguida de «N» (Norte) o «S» (Sur), y de 3 cifras correspondientes a la longitud en grados, seguida de «E» (Este) o «W» (Oeste). También en este caso, la cantidad necesaria de números puede completarse mediante ceros, como, «46N078W»;

e) 2 ó 3 caracteres correspondientes a la identificación de una ayuda para la navegación (normalmente un VOR), seguidos de 3 cifras indicadoras de la marcación del punto en grados magnéticos, seguidas de tres cifras indicadoras de la distancia al punto en millas marinas. En caso necesario puede completarse la cantidad de cifras mediante ceros; así pues, un punto situado a 180 grados magnéticos y a una distancia de 40 millas marinas del VOR «FOJ», se expresaría por «FOJ180040».

1.7. Detalle de los campos.

1.7.1. Los elementos de datos prescritos o autorizados para cada tipo de campo, junto con las condiciones impuestas o las variaciones permitidas, se indican en los Procedimientos para los Servicios de Navegación Aérea de OACI.

1.8. Exactitud en la preparación de los mensajes ATS.

1.8.1. Cuando se transmitan mensajes ATS normalizados por los canales de teletipo en regiones en las que se sabe que se utilizan computadoras ATC, el formato y la representación convencional de los datos prescritos en las tablas de campo de los Procedimientos para los Servicios de Navegación Aérea de OACI deberán observarse rigurosamente.

2. Mensajes normalizados ATS y su composición.

![imagen](https://www.boe.es/datos/imagenes/disp/2002/17/01097_6245961_image7.png)
