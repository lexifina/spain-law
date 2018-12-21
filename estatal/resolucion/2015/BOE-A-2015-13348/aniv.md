## ANEXO IV

## Rango de precios y límite de cantidad permitidos

1. Rango de precios permitido.

De acuerdo a las reglas «Validación de ofertas» y «Datos de referencia del Agente», y con el fin de evitar errores indeseados en la introducción de valores de precios por parte del Agente en la Plataforma de Negociación, se establecerá un rango de precios permitido (definido por un límite inferior y uno superior) en el envío de ofertas, de tal modo que si el precio introducido por el Agente en la oferta (Pi) supera los límites establecidos, la oferta no será aceptada de forma inmediata dándose un doble aviso al Agente conforme a la Regla «Validación de ofertas».

Dichos límites, que podrán ser diferentes para cada tipo de producto, podrán ser introducidos por el Agente a través de la Plataforma de Registro y Consultas, y serán efectivos a partir de la Sesión de Negociación del día posterior al de su introducción y aceptación en la Plataforma de Negociación.

Para este fin, se establecen los siguientes parámetros:

a) El Agente podrá configurar un precio superior y un precio inferior (Psupi y Pinfi), para cada oferta y para cada producto i, teniendo en cuenta la máxima variación del precio fijada por el Operador del Mercado y los precios definidos para ello.

b) El Operador del Mercado fijará la máxima variación de precio (ΔPf), que tomará el valor de 5 €/MWh.

c) Los precios definidos (PD), para el producto i, sobre los que se aplicará la máxima variación indicada anteriormente, serán los siguientes:

1.º Precio de la última Transacción efectuada en la Sesión de Negociación para dicho producto.

2.º En caso de que no hubiera ninguna Transacción para dicha Sesión de Negociación, se utilizará el Precio Último Diario de la Sesión de Negociación anterior, según el tipo de producto:

i. Intradiario: el Precio Último Diario de la Sesión de Negociación del día anterior.

ii. Diario: el Precio Último Diario de la Sesión de Negociación del día anterior para el producto con mismo día de entrega. En caso de que no existiera, se utilizaría el Precio Último Diario del producto Diario con entrega en el día siguiente.

iii. Fin de Semana: el Precio Último Diario de la Sesión de Negociación del día anterior para el producto con los mismos días de entrega.

iv. Resto de Mes y Mes Siguiente: para cada tipo de producto, el Precio Último Diario de la Sesión de Negociación del día de negociación anterior, siempre que se mantenga el mismo mes de entrega.

3.º En caso de que no se cumpliese ninguna de las condiciones anteriores, no existiría precio definido para dicho producto y sesión.

En base a los anteriores valores, los límites de precio máximo y mínimo permitidos se calcularán, para cada producto i, Agente, y Sesión de Negociación, del modo siguiente:

max[0, max[(PDi – ΔPf), Pinfi]] < Pi < min[(PDi + ΔPf), Psupi]

Siendo:

Pi: Precio de la oferta introducida por el Agente para el producto i, en €/MWh.

PDi: Precio definido anteriormente indicados en el párrafo 2º para el producto i, en €/MWh.

ΔPf: Máxima variación de precio fijada por el Operador del Mercado, que tomará el valor de 5 €/MWh.

Pinfi: Precio inferior definido por el Agente para el producto i, en €/MWh.

Psupi: Precio superior definido por el Agente para el producto i, en €/MWh.

2. Límite de cantidad ofertable permitido.

De acuerdo a las Reglas «Validación de ofertas» y «Datos de referencia del Agente», y con el fin de evitar errores indeseados en la introducción de cantidades por parte del Agente en la Plataforma de Negociación, se establecerá un límite de cantidad máxima permitida en el envío de ofertas, de tal modo que si la cantidad introducida por el Agente en la oferta (Qi) supera el límite establecido, la oferta no será aceptada de forma inmediata dándose un doble aviso al Agente conforme a la Regla «Validación de ofertas».

Dicho límite, que podrá ser diferente para cada tipo de producto, podrá ser introducido a través de la Plataforma de Registro y Consultas, y será efectivo a partir de la Sesión de Negociación del día posterior al de su introducción y aceptación en la Plataforma de Negociación.

Para este fin, se establecen los siguientes parámetros:

• El Operador del Mercado fijará la Cantidad máxima (Qf), que tomará el valor de 20.000 unidades de negociación

• El Agente podrá configurar la Cantidad máxima (Qci) para el producto i.

En base a los anteriores valores, el límite de cantidad se calculará, para cada producto, Agente y Sesión de Negociación, del modo siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/294/13348_002.png)

Siendo:

Qi: Cantidad introducida en la oferta envida por el Agente para el producto i.

Qf: Cantidad máxima fijada por Operador del Mercado, que tomará el valor de 20.000 unidades de negociación.

Qci: Cantidad máxima configurable por el Agente para el producto i.

> Se modifica el apartado 1 por el apartado 3.16 de la Resolución de 5 de diciembre de 2018. Ref. BOE-A-2018-17574

> Esta modificación surtirá efectos en un plazo máximo de 3 meses a contar desde el 21 de diciembre de 2018, según establece el apartado 4 de la citada Resolución.
