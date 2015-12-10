## ANEXO IV

## Rango de precios y límite de cantidad permitidos

1. Rango de precios permitido.

De acuerdo a las Reglas «Validación de ofertas» y «Datos de referencia del Agente», y con el fin de evitar errores indeseados en la introducción de valores de precios por parte del Agente en la Plataforma de Negociación, se establecerá un rango de precios permitido (definido por un límite inferior y uno superior) en el envío de ofertas, de tal modo que si el precio introducido por el Agente en la oferta (Pi) supera los límites establecidos, la oferta no será aceptada de forma inmediata dándose un doble aviso al Agente conforme a la Regla «Validación de ofertas».

Dichos límites, que podrán ser diferentes para cada tipo de producto, podrán ser introducidos por el Agente a través de la Plataforma de Registro y Consultas, y serán efectivos a partir de la Sesión de Negociación del día posterior al de su introducción y aceptación en la Plataforma de Negociación.

Para este fin, se establecen los siguientes parámetros:

• El Operador del Mercado fijará la máxima variación de precio (ΔPf), que tomará el valor de 10 unidades de precio.

• El Agente podrá configurar el máximo incremento y decremento de precio (IPci y DPci) para el producto i.

• Precios definidos (PD) sobre los que se aplicarán las máximas variaciones indicadas anteriormente:

– Producto cuya negociación esté abierta en modo de Mercado Continuo: Precio de la última Transacción efectuada en la Sesión de Negociación para dicho producto.

– Producto que sólo haya sido negociado en Subasta de apertura: Precio de Cierre de Subasta.

– Producto negociado en una Sesión de Negociación anterior: Precio último de la Sesión de Negociación del producto disponible.

– Producto recién listado, que todavía no ha sido negociado: Precio último de la Sesión de Negociación del producto de su mismo tipo cuyo periodo de entrega sea el más próximo.

En base a los anteriores valores, los límites de precio máximo y mínimo permitidos se calcularán, para cada producto, Agente, y Sesión de Negociación, del modo siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2015/294/13348_001.png)

Siendo:

Pi: Precio de la oferta introducida por el Agente para el producto i.

PDi: Precio definido anteriormente según cada caso para el producto i.

ΔPf: Máxima variación de precio fijada por el Operador del Mercado, que tomará el valor de 10 unidades de precio.

DPci: Máximo decremento de precio configurable por el Agente para el producto i, en unidades enteras de precio.

IPci: Máximo incremento de precio configurable por el Agente para el producto i, en unidades enteras de precio.

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
