## ANEXO

## Propuesta de procedimiento para el envío y cálculo de la precisión de los programas de consumo de los consumidores electrointensivos

1. Objeto

El objeto de este documento es definir los intercambios de información entre los consumidores electrointensivos y el operador del sistema, así como el procedimiento para evaluar la precisión de los programas de consumo que dichos consumidores deben remitir a efectos de verificar que tienen un consumo predecible, de acuerdo al artículo 10 del Real Decreto 1106/2020, de 15 de diciembre, por el que se regula el Estatuto de los consumidores electrointensivos.

Se recoge también en este procedimiento el proceso para la obtención de los consumidores electrointensivos de la certificación de que disponen de los equipos y sistemas necesarios.

2. Ámbito de aplicación

Este procedimiento es de aplicación al operador del sistema y a los consumidores de energía eléctrica que tengan la categoría de electrointensivos conforme al Real Decreto 1106/2020, de 15 de diciembre.

3. Intercambios de información

3.1 Información a comunicar al operador del sistema por los consumidores electrointensivos. Los consumidores electrointensivos deberán comunicar su programa de consumo al operador del sistema, directamente o a través de su comercializadora, para al menos cada una de las horas del mes siguiente, antes de las 12:00 horas del día 15 (o día laborable inmediatamente anterior) de cada mes.

El programa de consumo comunicado incluirá la energía autoconsumida.

Los consumidores podrán actualizar su programa de consumo en cualquier instante, si bien no podrán actualizar el programa de consumo correspondiente a una hora ya comenzada.

La actualización del programa de consumo para una hora anulará cualquier programa anterior enviado para dicha hora, si bien, el operador del sistema mantendrá registro histórico de las actualizaciones de programa remitidas por el consumidor.

El operador del sistema confirmará a los consumidores electrointensivos, a través de los medios que determine y que publicará en su página web, la correcta recepción del programa de consumo enviado por el consumidor. El operador del sistema podrá habilitar otro tipo de mecanismos de intercambio para estos envíos.

3.2 Información a comunicar por el operador del sistema a los consumidores electrointensivos. El operador del sistema pondrá a disposición de los consumidores electrointensivos, en la forma y a través de los medios que determine y que publicará en su página web, la información de los programas de consumo de que dispone del consumidor.

El operador del sistema comunicará con carácter mensual a los consumidores electrointensivos la precisión de su programa de consumo evaluada por el operador del sistema.

3.3 Información a comunicar por el operador del sistema al MINCOTUR. El operador del sistema comunicará de forma mensual al MINCOTUR el seguimiento de la disponibilidad y la precisión de los programas de consumo de los consumidores electrointensivos. Dicha comunicación incluirá:

– Valor mensual de la precisión de consumo de cada consumidor electrointensivo.

– Número de meses del año en que la precisión del programa de consumo ha resultado inferior al 75 %.

– Un indicador en el caso del tercer mes en que la precisión del programa no llegue al valor del 75 %.

4. Equipos, sistemas y comunicaciones

Para evaluar la precisión de los programas de consumo se utilizará la información de medida horaria disponible en el concentrador principal de medidas, tal y como indica el Real Decreto 1106/2020, de 15 de diciembre.

Los consumidores deberán remitir, directamente o a través de su comercializadora, sus programas de consumo al concentrador principal, a través de la web del Sistema de Información de Medidas Eléctricas (SIMEL). A tales efectos, el operador del sistema publicará en su página web los requisitos necesarios para el acceso de los consumidores electrointensivos a dicha aplicación, así como los formatos en los que los consumidores deberán remitirla.

Los consumidores electrointensivos que presten el servicio de gestión de la demanda de interrumpibilidad en el periodo de entrega en curso, podrán realizar el envío de la previsión horaria de consumo conforme a lo establecido en la normativa que regule este servicio, siendo válida, a estos efectos, la certificación de los equipos, sistemas y comunicaciones emitida y vigente en el marco de la normativa de interrumpibilidad. Aquellos consumidores que opten por esta opción, deberán comunicarla al operador del sistema en los plazos y formato que este determine.

Una vez que el consumidor electrointensivo disponga del acceso indicado y se verifique que el mismo se encuentra operativo, el operador del sistema comunicará al Ministerio de Industria, Comercio y Turismo que el consumidor dispone de los equipos, sistemas y comunicaciones requeridos para cumplir lo establecido en el artículo 10.2 del Real Decreto 1106/2020, de 15 de diciembre, tal y como establece el artículo 6 de dicho real decreto.

5. Verificación de la precisión de los programas de consumo

La precisión del programa horario de consumo se evaluará mensualmente y deberá tener una precisión superior al 75 por ciento en media mensual, de acuerdo con lo establecido en el punto 1 del artículo 10 del Real Decreto 1106/2020, de 15 de diciembre.

La precisión mensual de los programas de consumo (PPC) se evaluará conforme a la siguiente fórmula y a partir de la información del concentrador principal de medidas:

PPC (%) = 100 – Error_previsión (%)

![imagen](https://www.boe.es/datos/imagenes/disp/2021/228/15436_5241.png)

– Si no se dispone de Progh o no se dispone de Ph para la hora h:

Error_horarioh = 1

– Si Progh> 0 kWh:

• Si Progh > 5 % de la potencia contratada máxima o Ph > 5 % de la potencia contratada máxima:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/228/15436_5322.png)

• Si Progh≤ 5 % de la potencia contratada máxima y Ph < 5 % de la potencia contratada máxima:

Error_horarioh = 0

– Si Progh = 0 kWh:

Si Ph = 0 kWh → Errorhorarioh = 0

Si Ph > 0 kWh → Errorhorarioh = 1

Donde:

– PPC: Precisión mensual de los programas de consumo (%).

– horas: Número total de horas en el mes de cálculo.

– Ph: Consumo horario de energía en la hora h (kWh) registrado en el concentrador principal, incluyendo la energía autoconsumida.

– Progh: Último programa de consumo horario para la hora h (kWh) recibido.

– Error_previsión: Desviación mensual del consumo respecto a los programas (%).

– Errorhorarioh: Desvío horario del consumo respecto a los programas en la hora h.

De forma general, el operador del sistema calculará la precisión de los programas de consumo a partir del día 15 de cada mes, para todos los meses del año en curso hasta el mes anterior al mes en que se realiza dicho cálculo.
