## ANEXO II

## Algoritmo de asignación de ofertas para la contratación de reserva de potencia adicional a subir

1. Características fundamentales del algoritmo de asignación

Las características principales que presenta este algoritmo de asignación de ofertas son las siguientes:

• Proceso de asignación iterativo en el que se realizan diferentes aplicaciones del algoritmo hasta alcanzar una solución válida.

• Se admiten bloques de oferta indivisibles y de tipo todo o nada.

• Mercado marginalista en el que la liquidación por la prestación del servicio en cada periodo de programación viene determinado por el precio de la última oferta asignada parcial o totalmente para cubrir los requerimientos en dicho periodo.

• Se admite un margen en la asignación de ofertas (± 10% de los requerimientos) de forma que se considera la asignación válida cuando se cubren los requerimientos publicados dentro del intervalo definido por este margen (90% <-> 110 % de los requerimientos publicados).

2. Descripción del funcionamiento del algoritmo

El procedimiento utilizado en el proceso de asignación de ofertas es el siguiente:

1. Para cada periodo de programación se ordenarán los bloques de oferta en orden creciente de precios.

2. A igualdad de precio, los bloques se ordenan según el siguiente criterio:

• Primero los bloques divisibles y a continuación los indivisibles o de tipo todo o nada.

• A igualdad de tipo (ambos divisibles o indivisibles o tipo de todo o nada), primero el bloque de menor potencia.

• A igualdad de todas las condiciones anteriores primero el bloque con menor número de orden en la oferta (que se haya recibido primero).

3. Para cada periodo de programación del horizonte diario se asignarán los bloques en el orden indicado en los puntos 1 y 2. anteriores, utilizando parcialmente los bloques divisibles si fuera necesario, hasta cubrir los requerimientos de potencia a subir de ese periodo con un margen de +/- 10%. En caso de no poder cumplirse la condición anterior con los bloques de un determinado precio se continuará con los bloques del precio siguiente, hasta completar la asignación.

4. Al asignar los bloques por unidad de programación y periodo se tendrán en cuenta:

• Las limitaciones de potencia máxima, asociadas a indisponibilidades comunicadas por el correspondiente sujeto del mercado, o su representante, con anterioridad al inicio del proceso de asignación.

·• Las limitaciones de programa establecidas por el OS por razones de seguridad del sistema.

• La condición de que la reserva de potencia adicional a subir ofertada no supere la diferencia entre la potencia máxima disponible del grupo y su programa PVP.

En el caso de que alguno de los bloques de oferta viole alguno de los límites anteriores se actuará de la siguiente forma:

• Bloque divisible: El bloque será truncado hasta el punto en que deje de violar el límite.

5. Bloque indivisible o de tipo todo o nada: El bloque no será asignado en los periodos de programación en los que se produzca dicha violación. Una vez procesados todos los periodos del horizonte de programación se verificará que los bloques de tipo todo o nada hayan sido asignados en todos los periodos horarios de programación en los que aplique dicha condición. En caso de incumplimiento de esta condición se desasignarán todos los bloques de tipo todo o nada que hubieran resultado asignados. Si una vez desasignados todos estos bloques se cubren los requerimientos de potencia a subir en todos los periodos de programación afectados con un margen de +/- 10%, se finalizará el proceso de asignación. En caso contrario se continuará con los bloques del precio siguiente, hasta completar la asignación. Este proceso se repetirá hasta que se alcance una solución, o un número máximo de (4) iteraciones. En este último caso se finalizará el proceso de asignación cubriendo menos del 90 % del requerimiento de potencia.
