## ANEXO

## Determinación del cálculo de la liquidación de la retribución del servicio y de la liquidación de los incumplimientos

A. CÁLCULO DE LA LIQUIDACIÓN DE LA RETRIBUCIÓN DEL SERVICIO.

1. Derecho de cobro fijo por disponibilidad de potencia:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6290.png)

Donde:

p= producto subastado (5MW o 90MW).

s= identificador de la subasta (1,2,…n)

PSs,p= potencia asignada en la subasta s del bloque de producto p (MW)

PRs,p= precio de adjudicación en la subasta s del bloque de producto p (€/MW)

DCFm = derecho de cobro fijo asociado a disponibilidad del recurso del mes m obtenido en el conjunto de las subastas.

m = mes de liquidación correspondiente del Periodo de Entrega.

2. Derecho de cobro variable por ejecución efectiva de la opción de reducción de potencia:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6416.png)

Donde:

PSs,p = potencia asignada al proveedor en la subasta s del bloque de producto p (MW)

i = Identificador de la ejecución de la opción de reducción de potencia (1,2,…j)

ti = periodo de ejecución de la opción i (horas)

Pri = precio de referencia de la ejecución de la opción i para el proveedor

DCVm = derecho de cobro variable asociado al mes m resultado de la ejecución de las órdenes de reducción de potencia que se hubiesen ejecutado durante ese mes.

B. CÁLCULO DE LA LIQUIDACIÓN DE LOS INCUMPLIMIENTOS.

1. Incumplimiento de la ejecución de una opción de reducción de potencia:

Primer incumplimiento. En el caso de un primer incumplimiento de ejecución de una opción de reducción de potencia durante el periodo de entrega, el Operador del Sistema calculará y anotará una obligación de pago, calculada conforme a la fórmula del artículo 11.2.a) de la Orden IET/2013/2013, de 31 de octubre.

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6459.png)

Los parámetros Pd, Pmax, Pa, N y Nt son los definidos en el artículo 11.2.a) de la Orden IET/2013/2013, de 31 de octubre.

El derecho de cobro DCFm es el derecho de cobro fijo por disponibilidad de potencia definido en el artículo 5 de este procedimiento de operación y calculado según lo dispuesto en el apartado A del presente anexo.

Segundo incumplimiento. En el caso de un segundo incumplimiento de ejecución de una opción de reducción de potencia durante el periodo de entrega, el Operador del Sistema calculará y anotará una obligación de pago, calculada conforme a lo dispuesto en el artículo 11.2.b) de la Orden IET/2013/2013, de 31 de octubre:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6500.png)

Donde:

– DCFm y DCVm son los derechos de cobro definidos en el artículo 5 de este Procedimiento de Operación y calculados según lo dispuesto en el apartado 1.A del presente anexo.

– M2 es el mes en el que se produce el segundo incumplimiento.

– OPIEO1 es la obligación de pago anotada como consecuencia del primer incumplimiento de ejecución de una opción de reducción de potencia.

– OPIEO2 es la obligación de pago anotada como consecuencia del segundo incumplimiento de ejecución de una opción de reducción de potencia.

2. Incumplimiento por insuficiente disponibilidad del recurso:

Primer incumplimiento disponibilidad para producto 90MW. El primer mes en el que el consumo horario menos el valor de la potencia residual de referencia (Pmax) no sea superior al recurso asignado durante el 91% de las horas del mes, como está descrito en el artículo 11.3.a) de la Orden IET 2013/2013, de 31 de octubre, el proveedor perderá el derecho de cobro asociado a la disponibilidad del mes del incumplimiento descrito en el artículo 5 de este Procedimiento de Operación, de forma que:

DCFm=M1 = 0

Donde M1 es el mes del primer incumplimiento.

Segundo incumplimiento disponibilidad para producto 90MW. En caso de incumplirse este requisito durante dos meses del mismo periodo de entrega, el proveedor perderá los derechos de cobro descritos en el artículo 5 de este Procedimiento de Operación, desde el mes del segundo incumplimiento, incluido, hasta el final del periodo de entrega, de forma que

DCFm = 0, para M2 ≤ m ≤12.

DCVm = 0, para M2 ≤ m ≤12.

Donde M2 es el mes del segundo incumplimiento.

Si además, el proveedor fuera adjudicatario del producto 5MW, tal y como establece el artículo 11.3.c de la Orden IET 2013/2013, de 31 de octubre, será de aplicación lo establecido en el artículo 11.3.b de la misma, de forma que (i) se generará una obligación de pago por las cantidades percibidas por el producto 5MW, hasta el mes previo al del segundo incumplimiento, y (ii) se perderán los derechos de cobro fijos y variables del resto del periodo de entrega de dicho producto, de forma que:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6545.png)

DCFm = 0, para M2 ≤ m ≤12.

DCVm = 0, para M2 ≤ m ≤12.

Donde M2 es el mes del segundo incumplimiento.

Incumplimiento de disponibilidad para producto 5MW. Si el consumo medio horario durante el periodo de entrega menos el valor de la potencia residual de referencia (Pmax) no es superior al recurso asignado, se aplicará lo establecido en el artículo 11.3.b de la Orden IET 2013/2013, de 31 de octubre, generándose una obligación de pago de importe igual a los derechos de cobro durante el periodo de entrega:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6657.png)

Si además, el proveedor fuera adjudicatario del producto 90MW y, durante el periodo de entrega, todos los meses se hubieran cumplido los requisitos del producto de 90MW, tal y como establece el artículo 11.3.c) de la Orden IET 2013/2013, de 31 de octubre, será de aplicación lo establecido en el artículo 11.3.b) de la orden, por lo que la obligación de pago de este punto sólo se calculará mediante la suma de los derechos de cobro obtenidos durante el periodo de entrega por su condición de proveedor del producto de 5MW.

3. Incumplimiento por actuación incorrecta del relé de deslastre:

Primera actuación incorrecta del relé de deslastre. Cuando se produzca el incumplimiento derivado de la primera actuación incorrecta del relé de deslastre durante el periodo de entrega, se aplicará lo dispuesto en el artículo 11.4.a) de la Orden IET/2013/2013, de 31 de octubre, por lo que el Operador del Sistema anotará una obligación de pago calculada conforme a la fórmula:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6700.png)

Donde:

DCFm es el derecho de cobro definido en el artículo 5 de este procedimiento de operación y calculado según el apartado 1.A del presente anexo.

4. Incumplimiento por insuficiente consumo en periodo 6:

Primer incumplimiento consumo en periodo 6 para producto 90MW. El primer mes en el que el consumo en periodo 6 no alcance el requisito establecido en el artículo 9.1.a) de la Orden IET/2013/2013, de 31 de octubre, el proveedor perderá el derecho de cobro fijo asociado a la disponibilidad del mes del incumplimiento según el artículo 5 de este Procedimiento de Operación, y se aplicará lo establecido en el artículo 11.5.a) de la orden, de forma que:

DCFM1 = 0

Donde M1 es el mes del primer incumplimiento.

Segundo incumplimiento consumo en periodo 6 para producto 90MW. En el caso de un segundo incumplimiento del requisito establecido en el artículo 9.1.a) de la Orden IET 2013/2013, de 31 de octubre, el proveedor perderá los derechos de cobro fijos y variables desde el mes del segundo incumplimiento hasta el final del periodo de entrega definidos en el artículo 5 de este Procedimiento de Operación, y se aplicará lo establecido en el artículo 11.5.a) de la orden, de forma que:

DCFm = 0, para M2 ≤ m ≤12.

DCVm = 0, para M2 ≤ m ≤12.

Donde M2 es el mes del segundo incumplimiento.

Incumplimiento consumo en periodo 6 para producto 5MW. Si el consumo en el periodo 6 no alcanza el requisito establecido en el artículo 9.1.b de la Orden IET 2013/2013, de 31 de octubre, el proveedor tendrá una obligación de pago de importe igual a los derechos de cobro fijos y variables del periodo de entrega definidos en el artículo 5 de este Procedimiento de Operación, y se aplicará lo establecido en el artículo 11.5.a) de la orden, de forma que:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6742.png)

5. Incumplimiento por insuficiente disponibilidad de comunicaciones:

Cuando el proveedor no alcance un índice mensual de disponibilidad de comunicaciones superior al 90%, perderá la retribución fija asociada a la disponibilidad del recurso del mes, tal y como establece el artículo 11.5.b) de la Orden IET 2013/2013, de 31 de octubre, de forma que:

DCFM = 0

Donde M es el mes del incumplimiento.

Cuando el proveedor no alcance un índice anual de disponibilidad de comunicaciones superior al 95%, el proveedor tendrá una obligación de pago de importe igual a la retribución fija asociada a la disponibilidad del recurso del periodo de entrega, tal y como establece el artículo 11.5.b) de la Orden IET 2013/2013, de 31 de octubre, de forma que:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/192/08571_6786.png)

6. Incumplimiento por insuficiente disponibilidad de programa de consumo:

Cuando el proveedor tenga un índice de disponibilidad de los programas de consumo horarios inferior al 95% de las horas del mes, perderá la retribución fija asociada a la disponibilidad del recurso del mes, tal y como establece el artículo 11.5.c) de la Orden IET 2013/2013, de 31 de octubre, de forma que:

DCFM = 0

Donde M es el mes del incumplimiento.

7. Incumplimiento por insuficiente precisión del programa de consumo:

Cuando el proveedor tenga un índice de precisión de los programas de consumo horarios inferior al 75% en un mes, perderá la retribución fija asociada a la disponibilidad del recurso del mes, tal y como establece el artículo 11.5.d) de la Orden IET 2013/2013, de 31 de octubre, de forma que:

DCFM = 0

Donde M es el mes del incumplimiento.

8. Incumplimiento por insuficiente información por parte del proveedor:

Cuando el proveedor incumpla reiteradamente sus obligaciones de información, será de aplicación lo establecido en el artículo 11.5.e de la Orden IET/2013/2013, de 31 de octubre, de forma que se generará una obligación de pago igual a los derechos de cobros fijos y variables reconocidos durante el periodo de entrega, y perderá los derechos de cobro fijos y variables del resto del periodo de entrega.
