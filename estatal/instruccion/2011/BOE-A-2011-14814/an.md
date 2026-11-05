## ANEXO A LA INSTRUCCIÓN 7/2011, DE 15 DE SEPTIEMBRE DE 2011, DE LA JUNTA ELECTORAL CENTRAL

I. Procedimiento para la certificación de firmas de candidaturas por muestreo

Se trata de determinar el tamaño de la muestra de las firmas que avalan a una candidatura de una circunscripción electoral, mediante la comprobación de la condición de electores de sus firmantes, con las suficientes garantías, sin necesidad de comprobarlas todas.

El modelo estadístico que se ajusta al problema planteado es el de una distribución hipergeométrica, para una población finita de tamaño N (el número de firmas presentadas) de las cuales una proporción P presenta una característica determinada (que son electores de la circunscripción).

El número de elementos que presenta la característica (el número de firmas realizadas por los electores) es NP y el de los que no N(1-P).

Este número se puede estimar mediante a partir de la proporción muestra obtenida con una muestra aleatoria de la población.

La confianza en el valor estimado se mide con el denominado intervalo de confianza, que determina los límites inferior y superior dentro de los cuales estarían los valores de las estimaciones que se obtendrían para el conjunto de todas las muestras posibles con un nivel de significación (expresado en tanto por ciento o en tanto por mil) predeterminado.

El problema a resolver consiste en calcular el tamaño de la muestra n necesario para estimar una característica que se presenta en la población en una proporción P con un nivel de precisión (CV) predeterminado, que para la distribución considerada es:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_001.png)

Esta distribución estadística se puede aproximar mediante una distribución normal de media p y de varianza p*(1-p)/n.

Finalmente, los límites obtenidos se refieren al total multiplicándolos por el tamaño de la población N.

Habida cuenta que ningún elector podrá prestar su firma a más de una candidatura las certificaciones se harían después de eliminar a los firmantes que resultaran duplicados, considerando que se distribuyen aleatoriamente en la misma proporción en la muestra que en el total de los firmantes.

Recomendación importante: Teniendo en cuenta que algunos de los avales presentados pueden resultar inválidos se aconseja recoger entre un 10 y un 20 % más de los avales necesarios.

A modo de ejemplo, se exponen distintos supuestos para poder certificar que se supera el número total de firmas realizadas por electores mediante una estimación muestral con un nivel de confianza.

Candidatura de agrupaciones de electores al Parlamento Europeo:

El número de avalistas necesario es de 15.000 electores (artículo 220.3).

| Número de firmas requeridas | Tamaño de la muestra | Tanto por mil de significación | Proporción muestral mínima |
| --- | --- | --- | --- |
| 15.000 | 600 | 999 | 0,80 |

Lo que se interpreta en la forma siguiente:

Supongamos que se presentaran 20 mil firmas. La proporción de las firmas que deben tener la condición de electores para superar los 15.000 debería ser mayor o igual a 0,75. Para una proporción mínima mayor, por ejemplo de 0,80, bastaría con una muestra de 600 (un 4%) de los firmantes, para garantizar que la proporción de los que tienen la condición de elector supera ese porcentaje en el 999 por mil de los casos.

Si se rebajara el nivel de confianza al 99% entonces bastaría con una muestra de 350 avalistas.

Dependiendo del número de certificaciones que de requieran se puede optar por establecer un nivel de confianza mayor o menor.

Candidatura de agrupaciones de electores al Congreso y al Senado:

El número de avalistas necesario es del 1% de los electores (artículo 169.3). Aplicando el procedimiento a las provincias con el mayor y menor número de electores (Madrid con 45 mil firmas requeridas y 55 mil presentadas y Soria con 750 requeridas y 1.000 presentadas), resulta:

| Número de firmas requeridas | Tamaño de la muestra | Tanto por mil de significación | Proporción muestral mínima |
| --- | --- | --- | --- |
| 45.000 | 700 | 99 | 0,85 |
| 750 | 100 | 99 | 0,85 |

Candidatura de candidaturas que no obtuvieron representación en el Congreso o al Senado:

El problema es el mismo que el de las agrupaciones de electores, descrito en el apartado anterior, con la única diferencia de que el número de avalistas necesario es del 0,1 % de los electores (artículo 169.3).

II. Especificaciones técnicas para la recogida de avales de candidaturas con firma electrónica

1 1. Índice.

1. Índice.

2. Especificación del fichero con el aval firmado.

2.1 Introducción.

2.2 Formato.

2.3 Firma.

2.4 Nombre de los ficheros xml.

2.5 Formato del fichero zip.

2 2. Especificación del fichero con el aval firmado.

2.1 Introducción.

Los avales para las candidaturas electorales deberán presentarse en formato XML y firmados electrónicamente por el avalista. En este documento se detalla el formato del fichero xml a firmar, el tipo de firma a incorporar y el formato del fichero zip a entregar en la Junta Electoral competente.

2.2 Formato.

El formato del fichero sin firmar es el siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_002.png)

La estructura y restricciones de contenido del fichero queda definido por el siguiente fichero xsd (XML Schema Definition).

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_003.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_004.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_005.png)

2.3 Firma.

El fichero a entregar deberá incorporar una firma XMLDsig. Esta firma se incorporará al propio fichero de aval, firmando los datos del nodo «avalcandidatura», esto es, una firma tipo «enveloped».

El fichero de aval firmado deberá verificar las especificaciones siguientes:

1. [XMLDSig] XML Signature Syntax and Processing.

2. [XADES] XML Advanced Electronic Signatures ETSI TS 101 903.

El fichero firmado deberá tener, por tanto, la estructura reflejada en el siguiente ejemplo:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_006.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2011/224/14814_007.png)

2.4 Nombre de los ficheros xml.

El fichero anterior deberá almacenarse con el nombre siguiente NNNNNNNNN.xml donde NNNNNNNNN es el NIF/NIE de la persona que avala la candidatura y que además firma el aval. Esto es, es el NIF/NIE del certificado usado para firmar y el NIF/NIE del campo <ID>.

2.5 Formato del fichero zip.

Para cada tipo de elecciones, circunscripción y candidatura se formará un fichero zip con todos los avales correspondientes, con el siguiente nombre:

EEEEEE.CCCCCC.PPPPPP.zip, donde cada campo tiene el siguiente significado:

| Campo | Descripción |
| --- | --- |
| EEEEEE | Nombre de elecciones. Sólo se admiten los valores especificados para la etiqueta <elecciones /> del xml de entrega. Éstos valores aparecen recogidos en el esquema. |
| CCCCCC | Nombre de la circunscripción. Sólo se admiten los valores especificados para la etiqueta <circunscripción /> del xml de entrega. Éstos valores aparecen recogidos en el esquema. |
| PPPPPP | Nombre de la candidatura. Debe coincidir con lo recogido en la etiqueta nombre. No hay limitación, únicamente la limitación de tamaño recogida en el esquema, 100 caracteres. |

Así por ejemplo, para una candidatura de nombre Candidatura1, que presenta avales al Congreso y al Senado por la circunscripción de Almería, el nombre del fichero sería:

CONGRESO Y SENADO.Almería.Candidatura1.zip, y todos los ficheros xml del fichero zip deberán tener esos valores en las etiquetas correspondientes.

En el supuesto de candidaturas al Congreso y al Senado (elecciones=CONGRESO y SENADO) en las provincias insulares, dado que las circunscripciones de ambas elecciones son distintas, se deberán aportar dos ficheros zip, uno con los avales al Congreso para la circunscripción provincial y otro con los avales al Senado para la circunscripción de la isla o agrupación de islas por la que se pretenda la candidatura.
