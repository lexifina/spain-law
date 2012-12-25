## ANEXO I

## Metodología para la estimación del Crecimiento Potencial y del Output gap

El crecimiento potencial y el output gap de una economía son conceptos de gran utilidad para el análisis económico y, en particular, para la toma de decisiones de política económica. Constituyen la referencia básica para valorar la posición cíclica de la economía y efectuar el diagnóstico sobre la orientación de las políticas macroeconómicas.

Se define el producto potencial como el nivel de producción en términos reales que una economía es capaz de generar utilizando los factores productivos disponibles y la tecnología existente, sin generar presiones inflacionistas. Es importante resaltar, sin embargo, que no es una variable observable por lo que requiere ser estimada. Por su parte, el output gap o brecha de producción, se define como la diferencia entre el cociente entre el nivel de PIB observado o previsto, también en términos reales, y el nivel estimado para el PIB potencial y uno. Es decir, en tanto por uno la brecha de producción (OG) viene dada por:

OG= (PIB observado/PIB potencial)-1

La estimación del producto potencial está sujeta a un elevado grado de incertidumbre, razón por la que la literatura existente recomienda efectuar el diagnóstico de la evolución de la brecha de producción a partir de una horquilla de estimaciones obtenidas a partir de diferentes metodologías. Entre ellas destaca la basada en la estimación de una función de producción, aplicada por los principales organismos económicos internacionales (FMI, OCDE y Comisión Europea).

La estimación del PIB potencial basada en la función de producción presenta la ventaja tener un fundamento teórico sólido, del que carecen otros métodos puramente estadísticos (por ejemplo, aplicación del filtro de suavizado Hodrick-Prescott al PIB real observado), lo que permite un análisis económico de las fuentes del crecimiento del producto potencial. Como principal inconveniente hay que mencionar, sin embargo, los elevados requerimientos de información para su cálculo. En concreto, esta metodología exige, por un lado, la estimación de la productividad total de los factores (PTF) y, por otro, la evaluación de los factores productivos (empleo y capital) en su nivel potencial.

El Ministerio de Economía y Competitividad elabora estimaciones de PIB potencial y output gap anual para la economía española aplicando la metodología de la función de producción utilizada por la Comisión Europea y acordada en el seno del Grupo de Trabajo del Output Gap («Calculating potential growth rates and output gaps. A revised production function approach». Denis C., Grenouilleau D., Mc Morrow K. and Róger W. European Commission. Economic papers number 247. March 2006). Sus principales características se detallan a continuación:

Se utiliza una función de producción Cobb-Douglas del tipo:

PIB = PTF ∙ L1-α ∙ Kα [1]

Donde PIB es el PIB real, PTF la productividad total de los factores, K el stock de capital y L el factor trabajo. A las elasticidades del producto respecto de los factores capital (a) y trabajo (1-a) se les han asignado los valores 0,35 y 0,65, respectivamente, valores fijados en la metodología de la Comisión Europea para todos los Estados Miembros. Al estimarse al PIB potencial anual, las series que se utilizan para esta estimación son también anuales.

Para estimar el producto potencial es preciso evaluar cada uno de los componentes de la función de producción en su valor potencial y sustituirlos en la función de producción.

En relación con la determinación de los factores determinantes del PIB potencial, el empleo potencial se corresponde con el total de horas trabajadas al año por los ocupados de la economía con el supuesto de plena utilización de los recursos disponibles y sin presiones inflacionistas, obteniéndose a partir de la siguiente expresión:

Lpot = POB ∙ PARTpot ∙ (1– NAWRU) ∙ Hpot [2]

POB es la población en edad de trabajar (15-64 años), PARTpot la tasa de actividad potencial, Hpot el número de horas potenciales trabajadas al año por ocupado y NAWRU la tasa de desempleo no aceleradora de los salarios.

A su vez, la tasa de participación y el número de horas potenciales se obtienen aplicando un filtro de Hodrick-Prescott (HP) a la tasa de actividad y al número de horas trabajadas al año por trabajador, respectivamente, mientras que la NAWRU se estima como componente no observable en una curva de Phillips que incluye como regresores la aceleración de la participación de los salarios en el PIB, la productividad del factor trabajo y los términos de comercio definidos como la diferencia entre las tasas de crecimiento de los deflactores del PIB y del consumo privado.

Por su parte, el stock de capital potencial se supone que coincide con el capital observado, evaluándose mediante la aplicación del método de inventario permanente a través de la ecuación dinámica de acumulación del capital.

Kt = Kt-1 ∙ (1 – δ) + It [3]

Siendo I la inversión real y δ la tasa de depreciación del capital.

De este modo, el capital de un período será igual a la inversión bruta efectuada más el capital del período anterior corregido de depreciación.

Por último, la productividad total de los factores potencial se determina extrayendo cada año la productividad total de los factores observada a partir de los valores del PIB, stock de capital y trabajo, y se estima su tendencia utilizando, de entre todos los métodos disponibles, el que se considere se adapta mejor a la realidad cíclica de la economía española. La PTF (o Residuo de Solow) se obtiene a partir de la expresión.

![imagen](https://www.boe.es/datos/imagenes/disp/2012/308/15499_001.png)

Una vez obtenidos los diferentes componentes de la función de producción, en términos potenciales, esto es, el empleo potencial, el stock de capital y la PTF potencial, se está en disposición de calcular el PIB potencial aplicando la expresión:

![imagen](https://www.boe.es/datos/imagenes/disp/2012/308/15499_002.png)

El periodo muestral analizado se extiende desde el año 1980 hasta 6 años más allá del año en curso (año t). Entre 1980 y t-1 se utilizan datos tomados de las series de la Contabilidad Nacional, de la Encuesta de Población Activa y de las estimaciones intercensales de población; entre t y t+3 se utilizan las previsiones incluidas en el escenario macroeconómico del Ministerio de Economía y Competitividad, y entre t+4 y t+6 se lleva a cabo una extensión de las series de horas por trabajador, tasa de participación y PTF mediante la aplicación de modelos ARIMA. Dicha extrapolación tiene por objetivo limitar la sensibilidad del filtro de Hodrick-Prescott a la información disponible en los extremos del periodo muestral (problema del «punto final»).

El Ministerio de Economía y Competitividad en sus estimaciones de crecimiento potencial y output gap y, con el fin de obtener estimaciones más precisas y consistentes con la situación cíclica de la economía española utiliza las proyecciones de población de corto plazo publicadas por el Instituto Nacional de Estadística, al ser una fuente de datos más actualizada que la publicada por Eurostat.

En línea con la práctica de la Comisión Europea, el parámetro de alisado del filtro de Hodrick Prescott utilizado para estimar la tasa de actividad potencial y las horas potenciales por trabajador en la expresión [2] toma el valor 10 para tener mejor en cuenta los cambios que se han producido en las horas por trabajador.
