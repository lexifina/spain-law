## ANEXO 1: CODIFICACIÓN

## Identificador del intercambio

A cada operación de intercambio se le asocia un identificador que permite designar la operación de forma única.

La codificación de este identificador se compone según el siguiente criterio:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_014.png)

La generación de este código se realiza antes de enviar el Mensaje de datos de intercambio, al sistema de gestión de intercambio.

## Mensaje de datos de intercambio y anexos

En el proceso de intercambio, el Mensaje de datos de intercambio y los anexos se nombran según lo siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_015.png)

Esta notación permite identificar de forma única a los ficheros dentro del espacio de intercambio registral.

## Mensajes de control y notificación

La entidad «de Mensaje» se trata como un fichero pero se utiliza una codificación diferente debido a que es necesario especificar el código de la Entidad Registral emisora del mensaje (con frecuencia, la «de destino» en el proceso de intercambio) en la denominación del fichero. La codificación para esta entidad es la siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2011/182/13174_016.png)

## Errores

Para realizar la codificación de los errores del sistema de intercambio, se utiliza un código de cuatro dígitos, estructurado en dos niveles:

i. Rango de error, que agrupa la definición de un tipo general de error. Se codifica con los dos primeros dígitos y establecen una secuencia:

0000

0100

0200

...

9900

ii. Código de error, pertenecientes a un rango. Utilizando los dos últimos dígitos, de la siguiente forma:

0000

0001

0002

...

0099

Por ejemplo, se puede definir un rango de error del tipo:

«0000» ➔ Errores en la validación del mensaje de datos de intercambio.

Y definir un error concreto como:

«0001» ➔ No se incorporan los anexos definidos en el mensaje de datos de intercambio.
