## Disposición adicional segunda. Incremento de los límites máximos de inversión en la red de distribución para el periodo 2027-2030.

1. En virtud de lo previsto en el artículo 7.5 de este real decreto, se establece, para el periodo 2027-2030, un incremento del límite máximo de inversión en la red de distribución que podrá ser retribuido con cargo al sistema de 10.200 millones de euros que se dividen de la siguiente manera, 1.020 millones de euros para el año 2027, 2.550 millones de euros para el año 2028, 3.060 millones de euros para el año 2029 y 3.570 millones de euros para el año 2030.

Este incremento, cuyo reparto entre las empresas distribuidoras se realizará conforme a lo establecido en el artículo 7.6 de este real decreto, deberá destinarse exclusivamente a:

a) Inversiones cuyo objeto sea, al menos, uno de los siguientes:

1.º Control de tensión.

2.º Incorporación de telemando y telecontrol en instalaciones que el gestor de la red de distribución considere esenciales dentro de los procedimientos de reposición del servicio o para garantizar la continuidad del suministro dentro de los niveles exigibles.

3.º Mejora de la observabilidad de las instalaciones y/o de la medida y/o de la transparencia de datos.

4.º Ciberseguridad.

En ningún caso estas inversiones podrán suponer más de un 20 por ciento del incremento anual establecido en esta disposición adicional.

b) Inversiones anticipatorias. A los efectos previstos en esta disposición se considerará inversión anticipatoria aquella que cumpla todas y cada una de las siguientes condiciones:

1.º Su demanda en los cinco años siguientes no esté asegurada.

2.º Permita conectar demanda en zonas donde la carencia o insuficiencia de la red existente impida el crecimiento de esta.

3.º Tenga un efecto dinamizador en las demandas de la zona en los siguientes cinco años.

Las inversiones anticipatorias, según la anterior definición, tendrán la consideración de «Extensión natural de las redes de distribución» a las que se refiere el artículo 21.1.a) del Real Decreto 1048/2013, de 27 de diciembre, por el que se establece la metodología para el cálculo de la retribución de la actividad de distribución de energía eléctrica.

En ningún caso estas inversiones podrán suponer más de un 20 por ciento del incremento anual establecido en esta disposición adicional.

De igual modo, a las empresas distribuidoras con menos de 100.000 puntos de suministro a las que no se les haya asignado incremento en el límite de inversión, por no haber cumplido con las condiciones recogidas en el artículo 7 de este real decreto, se les permitirá invertir para este fin hasta un 20 por ciento del incremento en el límite de inversión que les hubiera correspondido en ese ejercicio en las actuaciones contempladas en este apartado b).

c) Inversiones necesarias para el suministro de demandas con origen en consumos industriales o residenciales. A estos efectos, tendrán consideración de consumidores industriales aquellos cuyo código en la Clasificación Nacional de Actividades Económicas (CNAE-2025) pertenezca a las secciones B o C.

d) Inversiones necesarias para la descarbonización del transporte.

e) Inversiones para la adaptación de las líneas existentes a la normativa estatal de avifauna.

En ningún caso estas inversiones podrán suponer más de un 10 por ciento del incremento anual establecido en esta disposición adicional.

A las empresas distribuidoras con menos de 100.000 puntos de suministro a las que no se les haya asignado incremento en el límite de inversión, por no haber cumplido con las condiciones recogidas en el artículo 7 de este real decreto, se les permitirá invertir para este fin hasta un 10 por ciento del incremento en el límite de inversión que les hubiera correspondido en ese ejercicio en las actuaciones contempladas en este apartado e).

f) Inversiones para mejorar la resiliencia climática y frente a fenómenos naturales adversos.

En ningún caso estas inversiones podrán suponer más de un 10 por ciento del incremento anual establecido en esta disposición adicional.

De igual modo, a las empresas distribuidoras con menos de 100.000 puntos de suministro a las que no se les haya asignado incremento en el límite de inversión, por no haber cumplido con las condiciones recogidas en el artículo 7 de este real decreto, se les permitirá invertir para este fin hasta un 10 por ciento del incremento en el límite de inversión que les hubiera correspondido en ese ejercicio en las actuaciones contempladas en este apartado f).

2. El incremento establecido en el apartado anterior podrá ser modificado mediante orden de la persona titular del Ministerio para la Transición Ecológica y el Reto Demográfico, previo acuerdo de la Comisión Delegada del Gobierno para Asuntos Económicos.

3. Para poder acceder al incremento de su límite de inversión correspondiente al año n, que resulte de tener en cuenta lo previsto en esta disposición adicional, las empresas distribuidoras deberán identificar en su plan de inversión de ese año aquellas instalaciones, de entre todas las incluidas en el mismo, que se acogerán a los supuestos previstos en las letras a), b), c), d), e) y f) respectivamente, del apartado 1. Con este fin, deberán incluir como parte del plan de inversiones de ese año un archivo txt con el nombre PI_INCREMENTO_R1-XXX.txt que incluya un registro por cada una de las instalaciones, de entre todas las incluidas en el plan, que se ejecutarán con dicho incremento, con la siguiente información:

| Campo | Descripción | Longitud | Tipo | Long. fija | Ejemplo |
| --- | --- | --- | --- | --- | --- |
| COD_PROYECTO. | Código Único con el que se identifica en el plan de inversión el proyecto al que pertenece la instalación. | 22 | Cadena. | No | I25fsf329387432 |
| IDENTIFICADOR_PY. | Identificador Único con el que se identifica la Instalación en el plan de inversión. | 22 | Cadena. | No | I25fsf329387432 |
| FINALIDAD. | Finalidad a la que se destina la instalación: CT: inversiones destinadas al control de tensión. TT: inversiones destinadas a telemando y telecontrol de instalaciones esenciales. OB: inversiones destinadas a mejora de la observabilidad, medida y/o transparencia de datos. IA: Inversiones anticipatorias. DE: Suministro de demanda Industrial y/o residencial. DT: Descarbonización del transporte. AV: Avifauna. RS: Resiliencia Climática. | 2 | Cadena. | Si | DT |
| INC_CAPACIDAD. | Incremento de capacidad estimado que permitirá satisfacer la instalación, en MW. | 6 | Decimal. | No | 55,10 |

El formato y el alcance de la información necesaria para identificar las inversiones, a los que se refiere este apartado, podrán ser modificados mediante orden de la persona titular del Ministerio para la Transición Ecológica y el Reto Demográfico.

4. En el caso de que una empresa distribuidora destine su incremento del límite de inversión del año n a inversiones que respondan a alguno de los supuestos c) o d) del apartado 1 de esta disposición adicional, deberá presentar la documentación justificativa que permita demostrar que, como consecuencia de dichas inversiones, se han logrado otorgar permisos de acceso por, al menos, un 50 % del incremento de capacidad recogido en el archivo PI_INCREMENTO_R1-XXX.txt. La empresa distribuidora deberá presentar esta documentación junto con el informe que, de acuerdo con lo previsto en el artículo 9 de este real decreto, habrá de presentar en relación con el cumplimiento de su plan de inversión del año n.

Si dicho informe no incluyese la justificación señalada, si no se lograse acreditar dicho incremento de capacidad de acceso otorgada o, si el porcentaje señalado en el párrafo anterior no respondiese a alguno de los supuestos a los que se refieren las letras c) o d) del apartado 1, el límite de inversión del año siguiente al que se tenga conocimiento de la incapacidad para demostrarlo se verá minorado en una cantidad igual a la invertida, actualizada utilizando el factor de retardo retributivo a la inversión calculado conforme a lo previsto en el artículo 6 de este real decreto.
