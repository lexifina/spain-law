## ANEXO V

## Normas técnicas de generación del NRC

1) Declaraciones-Liquidaciones o Autoliquidaciones. Las normas técnicas de generación del NRC para declaraciones-liquidaciones o autoliquidaciones se encuentran recogidas en la disposición adicional primera y en el anexo I de la Orden de 20 de enero de 1999 por la que se establecen las condiciones generales y el procedimiento para la presentación telemática de las declaraciones-liquidaciones mensuales de grandes empresas correspondientes a los códigos 111, 320 y 332 (BOE de 22 de enero) y en la disposición adicional cuarta de la Orden 22 de febrero de 1999, por la que se aprueban los modelos 117, en pesetas y en euros, de declaración-documento de ingreso de retenciones e ingresos a cuenta y del pago a cuenta del Impuesto sobre la Renta de las Personas Físicas, del Impuesto sobre Sociedades y del Impuesto sobre la Renta de no Residentes correspondiente a establecimientos permanentes, en relación con las rentas o ganancias patrimoniales obtenidas como consecuencia de las transmisiones o reembolsos de acciones y participaciones representativas del capital o del patrimonio de las instituciones de inversión colectiva, y se establecen las condiciones generales y el procedimiento para su presentación telemática (BOE de 24 de febrero).

2) Documentos de ingreso expedidos por la Administración. Las normas técnicas de generación del NRC para los documentos de ingreso modelos 790, 791, 990 y 991 expedidos por la Administración son las anteriores con la peculiaridad de que la estructura del NRC para los mismos se genera a partir de los siguientes datos:

![imagen](https://www.boe.es/datos/imagenes/disp/2003/79/06588_001.png)

Para generar el NRC es imprescindible que todos estos datos, a incluir en los procedimientos de cifrado, estén en EBCDIC y que se sigan las normas genéricas expresadas en las Órdenes más arriba mencionadas con respecto al NIF, al importe ingresado y al carácter 14 del justificante.

Detalle de los datos a incluir para generar el NRC:

D: Carácter de control generado con el mismo algoritmo que el actual para documentos de ingreso modelos 790, 791, 990 y 991.

C: Carácter de control complementario generado aplicando el algoritmo facilitado a las Entidades colaboradoras junto con la clave privada de cifrado.
