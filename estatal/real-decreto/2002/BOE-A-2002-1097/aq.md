## APÉNDICE Q

## Formatos SNOWTAM, NOTAM y ASHTAM

## ADJUNTO 1

## Formato de SNOWTAM

![imagen](https://www.boe.es/datos/imagenes/disp/2002/17/01097_6245961_image3.png)

## Orientación para llenar el formato de SNOWTAM

1. Generalidades.

a) Cuando se notifican datos que se refieren a dos o tres pistas se transmiten de nuevo los datos indicados de C a P inclusive.

b) Deben omitirse completamente las casillas junto con su indicador cuando no haya información a incluirse.

c) Deben utilizarse unidades del sistema métrico decimal y no se notificará la unidad de medida.

d) La validez máxima de los SNOWTAM es de 24 horas. Deben publicarse nuevos SNOWTAM siempre que ocurra un cambio de importancia en las condiciones. Se consideran de importancia los cambios siguientes, relativos al estado de las pistas:

1) un cambio de alrededor de 0,05 en el coeficiente de rozamiento;

2) cambios en el espesor de los depósitos de órdenes mayores que los siguientes: 20 mm para nieve seca; 10 mm para nieve mojada; 3 mm para nieve fundente;

3) un cambio del 10%, o más, en la longitud o anchura disponible de una pista;

4) todo cambio del tipo de depósitos o extensión de cobertura que requiera reclasificación en las casillas F o T del SNOWTAM;

5) cuando existan bancos de nieve críticos en un lado de la pista, o en ambos lados, todo cambio de la altura o de la distancia a que se encuentren a partir del eje de pista;

6) todo cambio de la conspicuidad de la iluminación de pista provocado por un ocultamiento de las luces; y

7) toda otra condición considerada de importancia a base de la experiencia o de las circunstancias locales.

e) El encabezamiento abreviado «TTAAiiii CCCC MMYYGGgg (BBB)» se incluye para facilitar el tratamiento automático de los mensajes SNOWTAM en los bancos de datos por computadora. La explicación de los símbolos es la siguiente:

| TT | = | designador de datos SNOWTAM = SW; |
| --- | --- | --- |
| AA | = | designador geográfico de los Estados (por ejemplo, LF = Francia, EG = Reino Unido - (véase Indicadores de lugar (Doc 7910) Parte 2 - Indice de las letra de nacionalidad para los indicadores de lugar); |
| iiii | = | número de serie del SNOWTAM expresado por un grupo de cuatro cifras; |
| CCCC | = | indicador de lugar de cuatro letras correspondiente al aeródromo al que se refiere el SNOWTAM (véase Indicadores de lugar (Doc 7910); |
|  |
| MMYYGGgg | = | fecha/hora de la observación/medición, de manera que: |
|  | = | MM = mes, o sea enero = 01, diciembre = 12 |
|  | = | YY = día del mes |
|  | = | GGgg = horas (GG) y minutos (gg) UTC; |
| (BBB) | = | grupo facultativo para designar: |
|  | = | una corrección de un SNOWTAM difundido previamente con el mismo número de serie = COR. |
|  |
|  |  | Nota: Los paréntesis en (BBB) significan que se trata de un grupo facultativo. |

Ejemplo: Encabezamiento abreviado del SNOWTAM Núm. 149 de Zurich, medición/observación de 7 de noviembre a las 0620 UTC:

SWLS0149 LSZH 11070620

2. Casilla A: Indicador de lugar del aeródromo (indicador de lugar de cuatro letras).

3. Casilla B: Grupo fecha/hora de 8 cifras - indica la hora de observación en la secuencia mes, día, hora y minutos en UTC; esta casilla debe llenarse siempre.

4. Casilla C: Número más bajo designador de pista.

5. Casilla D: Longitud en metros de la pista limpia, si es inferior a la longitud publicada (véase la casilla T para notificar si parte de la pista no está limpia).

6. Casilla E: Anchura en metros de la pista, si es inferior a la anchura publicada; si está desplazada a la izquierda o a la derecha del eje, añádase «L» o «R» según se vea desde el umbral que tenga el número designador más bajo.

7. Casilla F: Depósitos sobre la longitud de la pista, según se explica en el formato de SNOWTAM. Pueden utilizarse combinaciones adecuadas de estos números para indicar condiciones variables sobre los distintos segmentos de la pista. Si hay más de un depósito en el mismo tramo de la pista, estos deberían notificarse en orden desde la parte superior hasta la parte inferior. Las acumulaciones causadas por el viento, los espesores de depósitos apreciablemente superiores a los valores medios u otras características importantes de los depósitos pueden notificarse en la casilla T en lenguaje claro.

Nota: Al final de este Apéndice figuran las definiciones de los diversos tipos de nieve.

8. Casilla G: Espesor medio en milímetros de depósito correspondiente a cada tercio de la longitud total de la pista, o «XX» si no es medible o no es importante desde el punto de vista operacional. La evaluación debe efectuarse con una precisión de 20 mm para nieve seca, 10 mm para nieve mojada y 3 mm para nieve fundente.

9. Casilla H: Medición del rozamiento correspondiente a cada tercio de pista y dispositivo de medición utilizado. Coeficiente medido o calculado (dos cifras) o, si no se dispone de éste, rozamiento en la superficie estimado (una cifra), en orden empezando por el umbral que tenga el número designador de pista más bajo. Insértese una clave 9 cuando el estado de la superficie o del dispositivo de medición del rozamiento disponible no permite efectuar una medición confiable del rozamiento en la superficie. Utilícense las siguientes abreviaturas para indicar el tipo de dispositivo de medición del rozamiento utilizado:

| BRD | Frenómetro-dinómetro. |
| --- | --- |
| GRT | Medidor del asimiento. |
| MUM | Medidor del Valor Mu |
| RFT | Medidor del rozamiento en la pista. |
| SFH | Medidor del rozamiento en la superficie (neumáticos de alta presión). |
| SFL | Medidor del rozamiento en la superficie (neumáticos de baja presión). |
| SKH | Deslizómetro (neumáticos de alta presión). |
| SKL | Deslizómetro (neumáticos de baja presión). |
| TAP | Medidor Tapley |

Si se utiliza otro equipo especifíquese en lenguaje claro.

10. Casilla J: Bancos de nieve críticos. Si los hay, insértese la altura en centímetros y la distancia con respecto al borde de la pista en metros, seguidas de izquierda («L») o derecha («R») o ambos lados («LR»), tal como se ven desde el umbral que tiene el número de designación de pista más abajo.

11. Casilla K: Si las luces de pista están ocultas, insértese «SI» seguido de «L», «R» o ambos «LR» tal como se ve desde el umbral que tenga en número de designación de pista más bajo.

12. Casilla L: Cuando se prevea realizar una nueva limpieza de la pista, anótese la longitud y anchura de la pista o «TOTAL» si la pista habrá de limpiarse en su totalidad.

13. Casilla M: Anótese la hora UTC prevista para la terminación de la limpieza.

14. Casilla N: Puede utilizarse la clave correspondiente a la casilla F para describir las condiciones de las calles de rodaje; anótese «NO» si no se dispone de las calles de rodaje que sirvan a la pista conexa.

15. Casilla P: Si es aplicable, anótese «SI» seguido por la distancia lateral en metros.

16. Casilla R: Puede utilizarse la clave correspondiente a la casilla F para describir las condiciones de la plataforma; anótese «NO» si la plataforma está inutilizable.

17. Casilla S: Anótese la hora UTC prevista de la próxima observación/medición.

18. Casilla T: Descríbase en lenguaje claro toda información de importancia operacional pero notifíquese siempre en longitud de pista no despejada (casilla D) y el grado de contaminación de la pista (casilla F) para cada tercio de la pista (si procediera) de conformidad con la escala siguiente:

contaminación de la pista ‒10% - si la contaminación es inferior al 10%

contaminación de la pista ‒25% - si la contaminación es de 11 a 25%

contaminación de la pista ‒50% - si la contaminación es de 26 a 50%

contaminación de la pista ‒100% - si la contaminación es de 51 a 100%

Ejemplo de formato SNOWTAM que ha sido llenado.

GG EHAMZQZX EDDFZQZX EKCHZQZX

070645 LSZHYNYX

SWLS0149 LSZH 11070620

SNOWTAM0149

A) LSZH B) 11070620 C) 02 D) P)

C) 09 D) P)

C) 12 D) P)

R) NO S) 11070920 T) DESCONGELAMIENTO.

Definiciones de los diversos tipos de nieve.

Nieve (en tierra).

a) Nieve seca: Nieve que, si está suelta, se desprende al soplar o, si se compacta a mano, se disgrega inmediatamente al soltarla. Densidad relativa: hasta 0,35 exclusive.

b) Nieve mojada: Nieve que, si se compacta a mano, se adhiere y muestra tendencia a formar bolas o se hace realmente una bola de nieve. Densidad relativa: de O,35 a 0,5 exclusive.

c) Nieve compactada: Nieve que se ha comprimido hasta formar una masa sólida que no admite más compresión y que mantiene su cohesión o se rompe a pedazos si se levanta. Densidad relativa: 0,5 o más.

d) Nieve fundente: Nieve saturada de agua que, cuando se le da un golpe contra el suelo con la suela del zapato, se proyecta en forma de salpicaduras. Densidad relativa: 0,5 a 0,8.

Nota: Las mezclas de hielo, de nieve y/o de agua estancada pueden, especialmente cuando hay precipitación de lluvia, de lluvia y nieve o de nieve, tener densidades relativas superiores a 0,8. Estas mezclas, por su gran contenido de agua o de hielo, tienen un aspecto transparente y no traslúcido, lo cual, cuando la mezcla tiene una densidad relativa bastante alta, las distingue fácilmente de la nieve fundente.

## ADJUNTO 2

## Formato de NOTAM

![imagen](https://www.boe.es/datos/imagenes/disp/2002/17/01097_6245961_image4.png)

## Instrucciones para llenar el formato NOTAM

1. Generalidades.

1.1. Debe transmitirse la línea de calificativos (Q) y todos los identificadores (A a G inclusive), cada uno seguido del signo de cierre de paréntesis como se indica en el formato, a no ser que no haya ninguna entrada respecto a determinado identificador.

1.2. Cada NOTAM tratará únicamente de un asunto y de una condición relativa al asunto.

2. Numeración de los NOTAM.

Debe indicarse la serie mediante una letra y un número que debe ser de cuatro cifras seguidas de una barra y de dos cifras para el año (A0023/91).

3. Calificativos (casilla Q).

Esta casilla se subdivide en ocho campos, separados por barras. Si no se incorpora ninguna entrada al campo, no es necesario transmitir espacios en blanco entre las barras. La definición de cada campo es la siguiente:

1) FIR.

Indicador de lugar de la OACI, FIR o indicador de país más «XX» si es aplicable a más de una FIR dentro de un Estado lo cual se indicará en la casilla A).

2) Codigo NOTAM.

Código de cinco letras de la OACI o una de las siguientes combinaciones según sea necesario:

a) Si el asunto del que trata el NOTAM (segunda y tercera letras del código NOTAM) no está en la lista de códigos NOTAM, deberían utilizarse con referencia a la categoría las siguiente letras:

| QAGXX = AGA | QRCXX = RAC |
| --- | --- |
| QCOXX = COM | QXXXX = Otros |

b) Si las condiciones correspondientes al asunto no están enumeradas en la lista de códigos NOTAM, insértese la condición «XX» como cuarta y quinta letra.

Ejemplo: QFAXX.

c) Las siguientes letras cuatro y cinco del código NOTAM deberían utilizarse para cancelar un NOTAM:

AK: Reanudada la operación normal.

AL: Funcionando (o de nuevo funcionando) a reserva de limitaciones/ condiciones anteriormente publicadas.

AO: Operacional.

CC: Completado.

XX: Lenguaje claro.

3) Tránsito.

I = IFR

V = VFR

IV= IFR/VFR si es de interés para ambas clases de vuelos.

4) Objetivo.

N = NOTAM seleccionado para los explotadores de aeronaves le presten inmediata atención.

B = NOTAM seleccionado para una entrada en el boletín de información previa al vuelo (PIB).

O = De importancia para las operaciones en el caso de vuelos IFR.

M = NOTAM sobre asuntos varios: no sujeto a aleccionamiento pero disponible a solicitud.

5) Alcance.

| Aeródromo | A |
| --- | --- |
| En ruta | E |
| Aviso Nav | W |

Nota: En algunas radioayudas para la navegación corresponderá tanto utilizar la letra «A» como la letra «E» puesto que prestan servicios dobles, por ejemplo, como ayudas en ruta y de área terminal; por consiguiente, el texto NOTAM se utilizará para determinar si el alcance debería indicarse como A, E o AE. Si un asunto tiene el calificatico AE, debe notificarse en la casilla A) el indicador de lugar del aeródromo.

6) y 7) Inferior/superior

Utilizados cuando se aplican a «FL000 = nivel MAR/TERRENO». Los valores por defecto son 000/999.

Nota: Si al asunto se refiere a la «organización del espacio aéreo» (p.ej. CTR, TMA, UIR,...) debe indicarse un límite apropiado inferior/superior en la línea -Q.

8) Coordenadas radio

La latitud y la longitud con una precisión de un minuto, así como un número de tres cifras para la distancia correspondiente al radio de influencia en NM (p. ej. 4700N 01140E043). Las coordenadas representan aproximadamente el centro de un círculo con un radio que abarca toda el área de influencia.

4. Casilla A).

Con respecto a la instalación, al espacio aéreo, o a las condiciones que son objeto de la notificación, anótese el indicador de lugar OACI del aeródromo, o de la FIR en los que están situados. Si corresponde, puede indicarse más de una FIR/UIR. Si no hubiera disponible ningún indicador de lugar OACI, utilícense las letras de nacionalidad de la OACI que figuran en el Doc 7910 de la OACI, Parte 2, más XX y seguida en la casilla E por el nombre en lenguaje claro.

5. Casilla B).

Para el grupo fecha-hora utilícese un grupo de diez cifras representando el año, mes, día, horas y minutos UTC. Esta entrada es la fecha-hora de entrada en vigor del NOTAM, N, R o C. En el caso de NOTAM R que sustituye a un NOTAM anterior y promulga nueva información, el campo B) debe dar el grupo de fecha-hora a la cual el nuevo NOTAM suple a aquél a que se hace referencia.

6. Casilla C).

Debe utilizarse un grupo de fecha-hora a no ser que la información sea PERM. Si la información relativa a la fecha-hora no es segura, debe indicarse la duración aproximada utilizando un grupo de fecha-hora seguido de EST. Debe cancelarse o sustituirse cualquier NOTAM en el que esté incluida una indicación EST.

7. Casilla D).

Si la situación de peligro, el estado de funcionamiento o condición de las instalaciones notificados continúan durante períodos determinados, inserte dicha información en la casilla D).

8. Casilla E).

Úsese el código NOTAM decodificado, completado cuando sea necesario por indicadores, identificadores, designadores, distintivos de llamada, frecuencias, cifras y lenguaje claro. Cuando corresponda, deberían utilizarse las abreviaturas de la OACI. Esta entrada debe ser clara y concisa para proporcionar una entrada conveniente al PIB. En el caso de NOTAM C, debe incluirse una referencia al asunto y un mensaje de estado para que pueda verificarse con precisión si la condición es plausible.

9. Casilla F) y G).

Estas casillas son normalmente aplicables a los avisos para la navegación o a las restricciones del espacio aéreo y habitualmente forman parte de la entrada del PIB. Insértense las alturas límite inferior o superior de la zona de actividades o restricciones, indicando claramente el nivel de la referencia y las unidades de medida.

Ejemplo:

Si se declara zona peligrosa EG-DXX, situada a 5510N00520W, con un radio de 50NM (y afectando a dos FIR) hasta 12 200 m (40 000ft) MSL los días 03,07,12,21,24 y 28 de abril de 1991, de 0730 a 1500 UTC y hasta 9 150 m (30 000ft) MSL los días 19 y 20 de abril de 1991, de 0730 a 1500 UTC, se requerirían dos NOTAM, a saber:

(A0623/91 NOTAMN

Q) EGXX/QRDCA/IV/NBO/W/000/400/5510N00520W050

A) EGTT/EGPX B) 9104030730 C) 9104281500

D) APR 03 07 12 21 24 Y 28 0730 A 1500

E) ZONA PELIGROSA DXX EN ACTIVIDAD

F) GND G) 12 200 M (40 000FT) MSL.)

(A0624/91 NOTAMN

Q) EGXX/QRDCA/IV/NBO/W/000/300/5510N00520W050

A) EGTT/EGPX B) 9104190730 C) 9104201500

D) APR 19 Y 20 0730 A 1500

E) ZONA PELIGROSA DXX EN ACTIVIDAD

F) GND G) 9150 M (30 000FT) MSL.)

## Adjunto 3

## Formato de ASHTAM

![imagen](https://www.boe.es/datos/imagenes/disp/2002/17/01097_6245961_image5.png)

## Orientación para llenar el formato de ASHTAM

1. Generalidades.

1.1. El ASHTAM proporciona información sobre la situación de la actividad de un volcán cuando un cambio en la actividad volcánica tiene o se prevé que tendrá importancia para las operaciones. La información en cuestión se suministra utilizando el nivel de código de colores de alerta para los volcanes que se indican en 3.5.

1.2. En caso de que se produzca una erupción volcánica con nube de cenizas de importancia para las operaciones, el ASHTAM también proporciona información sobre la ubicación, extensión y movimiento de la nube de cenizas y las rutas aéreas y niveles de vuelo afectados.

1.3. La expedición de un ASHTAM dando información sobre una erupción volcánica, de conformidad con la sección 3, no debería retrasarse hasta disponer de toda la información completa de A) a K) sino que debería expedirse inmediatamente después de recibir notificación de que ha ocurrido o se prevé que ocurra una erupción, o de que ha ocurrido o se prevé que ocurra un cambio de importancia para las operaciones por la situación de la actividad de un volcán, o de que se haya comunicado la existencia de una nube de cenizas. En caso de que se espere una erupción y por lo tanto no haya evidencia en ese momento de la existencia de nube de cenizas, deberían llenarse las casillas A) a E) e indicar respecto de las casillas F) a I) que «no se aplica». Análogamente, si se notifica una nube de cenizas volcánicas, por ejemplo, mediante aeronotifi- cación especial, pero no se sabe en ese momento cuál es el volcán originador, el ASHTAM debería expedirse en principio mencionando en las casillas A) a E) las palabras «se desconoce», y las casillas F) a K) deberían llenarse según corresponda basándose en la aeronotificación especial, hasta que se reciba nueva información. En otras circunstancias, en caso de no disponer de la información concreta para alguna de las casillas A) a K), indíquese «NIL».

1.4. El período máximo de validez de los ASHTAM es de 24 horas. Deben expedirse nuevos ASHTAM cuando cambie el nivel de la alerta.

2. Encabezamiento abreviado

2.1. Después del encabezamiento habitual de comunicaciones AFTN, se incluye el encabezamiento abreviado «TT AA iiii CCCC MMYYGGgg (BBB)» para facilitar el tratamiento automático de los mensajes ASHTAM en los bancos de datos computadorizados. La explicación de los símbolos es la siguiente:

TT = designador de datos ASHTAM = VA;

AA = designador geográfico de los Estados, p. ej., NZ Nueva Zelanda [véase Indicadores de lugar (Doc 7910 de OACI), Parte 2, índice de las letras de nacionalidad para los Indicadores de lugar];

iiii = Número de serie del ASHTAM expresado por un grupo de cuatro cifras;

CCCC = indicador de lugar de cuatro letras correspondiente a la región de información de vuelo en cuestión [véase Indicadores de lugar (Doc 7910 de OACI), Parte 5, direcciones de los centros a cargo de las FIR/UIR];

MMYYGGgg = fecha/hora del informe, donde:

MM = mes, p. ej., enero = 01, diciembre = 12

YY = día del mes

Gggg = horas (GG) y minutos (gg) UTC

(BBB) = Grupo facultativo para corregir un mensaje ASHTAM difundido previamente con el mismo número de serie = COR.

Nota: Los paréntesis en (BBB) significan que se trata de un grupo facultativo.

Ejemplo: Encabezamiento abreviado del ASHTAM correspondiente a la FIR Auckland Oceanic, informe del 7 de noviembre a las 0620 UTC:

VANZ0001 NZZO 11070620.

3. Contenido del ASHTAM.

3.1. Casilla A. Región de información de vuelo afectada, equivalente en lenguaje claro del indicador de lugar anotado en el encabezamiento abreviado, en este ejemplo «FIR Auckland Oceanic».

3.2. Casilla B. Fecha y hora (UTC) de la primera erupción.

3.3. Casilla C. Nombre del volcán y número del volcán según figuran en el Manual sobre cenizas volcánicas, materiales radiactivos y «nubes» de productos químicos tóxicos (título provisional), Apéndice H (Doc 9691*) de la OACI y en el Mapa mundial de los volcanes y de las principales características aeronáuticas.

* En preparación.

3.4. Casilla D. Latitud/longitud del volcán en grados enteros o radial y distancia desde el volcán hasta la ayuda para la navegación (según se reseña en el Manual sobre cenizas volcánicas, materiales radiactivos y «nubes» de productos químicos tóxicos, Apéndice H (Doc 9691*) de la OACI y en el Mapa mundial de los volcanes y de las principales características aeronáuticas).

* En preparación.

3.5. Casilla E. Código de colores para indicar el nivel de alerta de la actividad volcánica, incluidos los niveles previos de actividad, expresado así:

| Nivel de código de colores de alerta | Situación de la actividad del volcán |
| --- | --- |
| ROJO ALERTA | Erupción volcánica en actividad. Penacho/nube de cenizas notificado por encima de FL 250 o Volcán peligroso, erupción probable, previsión de penacho/nube de cenizas que ascenderá por encima de FL 250. |
| NARANJA ALERTA | Erupción volcánica en actividad pero el penacho/nube de cenizas no alcanza ni se prevé que alcance el FL 250 o Volcán peligroso, erupción probable pero no se espera que el penacho/nube de cenizas alcance el FL 250. |
| AMARILLO ALERTA | Volcán activo de tiempo en tiempo y recientemente incremento notable de la actividad volcánica, el volcán no se considera actualmente peligroso pero debería ejercerse cautela o (Después de una erupción, es decir, cambio de alerta de color rojo o naranja a color amarillo) - La actividad volcánica ha disminuido notablemente, el volcán no se considera actualmente peligroso pero debería ejercerse cautela. |
| VERDE ALERTA | La actividad volcánica se considera terminada y el volcán ha vuelto a su estado normal. |
| Nota: El código de colores para indicar el nivel de alerta respecto de la actividad del volcán y todo cambio con relación a la situación de actividad anterior debería ser información proporcionada al centro de control de área por el organismo vulcanológico correspondiente del Estado en cuestión, p. ej., «Alerta rojo después de amarillo» o «Alerta verde después de naranja . |

3.6. Casilla F. Si se notifica una nube de cenizas volcánicas de importancia para las operaciones, indíquese la extensión horizontal y la base/cima de la nube de cenizas utilizando la latitud/longitud (en grados enteros) y las altitudes en miles de metros (pies) o el radial y la distancia respecto al volcán originador. La información puede basarse inicialmente sólo en una aeronotificación especial pero la información subsiguiente puede ser más detallada en base al asesora- miento de la oficina de vigilancia meteorológica responsable o del centro de avisos de cenizas volcánicas.

3.7. Casilla G. Indíquese el sentido pronosticado de movimiento de la nube de cenizas a niveles seleccionados basándose en el asesoramiento de la oficina de vigilancia meteorológica responsable o del centro de avisos de cenizas volcánicas.

3.8. Casilla H. Indíquense las rutas aéreas y tramos de rutas y niveles de vuelo afectados, o que se prevé resultarán afectados.

3.9. Casilla I. Indíquense los espacios aéreos, rutas aéreas o tramos de rutas aéreas cerrados y rutas alternativas disponibles.

3.10. Casilla. Fuente de la información, p. ej., «aeronotificación especial» u «organismo vulcanológico», etc. la fuente de la información debería indicarse siempre, tanto si ocurrió de hecho la erupción o se notificó la nube de cenizas, como en caso contrario.

3.11. Casilla K. Inclúyase en lenguaje claro toda información de importancia para las operaciones además de lo antedicho.
