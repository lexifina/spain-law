## ANEXO I

## Cálculo de las energías y potencias a efectos de facturación y liquidación para el autoconsumo colectivo o asociado a una instalación a través de la red

Las energías y potencias a efectos de facturación y de liquidación definidas en el artículo 3 del presente real decreto se calcularán de acuerdo con lo establecido a continuación:

1. Coeficientes y requisitos de los coeficientes de reparto.

La energía horaria neta generada individualizada de aquellos sujetos i que realicen autoconsumo colectivo o consumidores asociados a una instalación próxima a través de la red, ENGh,i será:

ENGh,i = βh,i · ENGh

Siendo:

ENGh energía neta horaria total producida por el generador o los generadores.

βh,i es el coeficiente de reparto horario en la hora h entre los consumidores que participan del autoconsumo colectivo de la energía generada en la hora h.

Para cada consumidor i participante del autoconsumo colectivo, este coeficiente tomará los valores que figuren en un acuerdo firmado por todos los consumidores participantes del autoconsumo colectivo y notificado a la empresa distribuidora como encargada de lectura de los consumos. El valor de estos coeficientes podrá determinarse en función de la potencia a facturar de cada uno de los consumidores asociados participantes, de la aportación económica de cada uno de los consumidores para la instalación de generación, o de cualquier otro criterio siempre que exista acuerdo firmado por todos los participantes y siempre que la suma de estos coeficientes βh,i de todos los consumidores que participan en el autoconsumo colectivo sea la unidad para cada hora del periodo de facturación. El coeficiente tomará el valor de 1 para cada hora del periodo de facturación en los casos en que sólo exista un consumidor asociado a una instalación próxima a través de la red.

El valor de estos coeficientes de reparto podrá ser distinto para cada hora del periodo de facturación, siempre que exista acuerdo firmado por todos los participantes y siempre que la suma de estos coeficientes βi de todos los consumidores que participan en el autoconsumo colectivo sea la unidad para cada hora del periodo de facturación.

Ficheros.

Si los participantes del autoconsumo optan por un reparto horario variable, la información de estos coeficientes de reparto deberá remitirse a la empresa distribuidora de acuerdo a las siguientes especificaciones:

i. Los consumidores, o en su caso los comercializadores que actúen como mandatarios de los mismos, deberán remitir un fichero texto plano de extensión “.txt” que contendrá el valor de los coeficientes de los consumidores que participan en el autoconsumo con el valor de todas las horas del año en curso con independencia de si las mismas han transcurrido o no. Este fichero tendrá las siguientes características:

a) El nombre del fichero será el del Código de Autoconsumo (CAU), seguido de un guion bajo, posteriormente se añadirá el correspondiente año expresado numéricamente con cuatro dígitos, seguido de la extensión “.txt”

b) El separador de campos será el punto y coma “;”

c) El carácter decimal será la coma “,”.

d) Los campos y orden que deberán contener serán los siguientes:

| Campo | Información y/o unidades | Long. | Tipo | Long. fija | Ejemplo |
| --- | --- | --- | --- | --- | --- |
| CUPS. | Código Universal de Punto de Suministro. | 22 | Cadena. | No |  |
| Hora. | Hora que tomará valores enteros desde 1 a 8760. | 4 | Entero. | No | 523 |
| Coeficiente. | Coeficiente que será un número. | 8 | Decimal. | No | 0,135464 |

ii. Adicionalmente, los consumidores, o en su caso los comercializadores que actúen como mandatarios de los mismos, podrán remitir el valor de los coeficientes además de para el año en curso, para los siguientes años en ficheros independientes hasta un máximo de 20 años incluido el año en curso. El nombre de cada uno de los ficheros será el del Código de Autoconsumo (CAU), seguido de un guion bajo, posteriormente se añadirá el del correspondiente año expresado numéricamente con cuatro dígitos, seguido de la extensión “.txt”.

iii. Si al inicio del año siguiente el distribuidor no dispusiera de los coeficientes para dicho año, este aplicará a cada hora el valor de los coeficientes del año anterior. El distribuidor pondrá este hecho en conocimiento de los comercializadores de los autoconsumidores, los cuales deberán informar a sus clientes de este hecho. Si ese año fuera bisiesto, los valores de cada una de las horas del día 29 de febrero serán los mismos que estén previstos para las horas del día 28 del mismo mes.

Si todos los participantes del autoconsumo optan por coeficientes constantes a lo largo de todo el año, los consumidores, o en su caso los comercializadores que actúen como mandatarios de los mismos, deberán remitir un fichero texto plano de extensión “.txt” que contendrá el valor de los coeficientes de los consumidores que participan en el autoconsumo con un solo valor para cada uno de ellos. Este fichero tendrá las siguientes características:

a) El nombre del fichero será el del Código de Autoconsumo (CAU), seguido de un guion bajo, posteriormente se añadirá el correspondiente año expresado numéricamente con cuatro dígitos, seguido de la extensión “.txt”.

b) El separador de campos será el punto y coma “;”

c) El carácter decimal será la coma “,”.

d) Los campos y orden que deberán contener serán los siguientes:

| Campo | Información y/o unidades | Long. | Tipo | Long. fija | Ejemplo |
| --- | --- | --- | --- | --- | --- |
| CUPS. | Código Universal de Punto de Suministro. | 22 | Cadena. | No |  |
| Coeficiente. | Coeficiente que será un número. | 8 | Decimal. | No | 0,135464 |

Aplicación de los coeficientes de reparto y plazos de activación y de modificación.

Se entenderá que la notificación de los consumidores, o en su caso a los comercializadores que actúen como mandatarios de los mismos a la empresa distribuidora de los coeficientes es correcta cuando todos los consumidores asociados que participan en un mismo autoconsumo colectivo aporten la siguiente información:

a) El mismo fichero de los coeficientes de reparto, el cual deberá cumplir los requisitos y criterios recogidos en el presente anexo.

b) El acuerdo firmado de reparto de cada uno de los consumidores asociados de un mismo autoconsumo colectivo.

En caso de que los ficheros se ajusten a los requisitos y criterios, y no contengan errores, la empresa distribuidora comunicará los consumidores, o en su caso a los comercializadores que actúen como mandatarios, la fecha de activación del autoconsumo o, en su caso, la fecha en que se aplicarán las modificaciones de los coeficientes del mismo.

La fecha de activación o utilización de los nuevos coeficientes será desde las 0 horas del primer día del mes siguiente a aquel en que la empresa distribuidora dispone de la información correcta y completa si este hecho sucede durante los primeros 10 días del mes en curso, o desde las 0 horas del primer día del segundo mes a aquel en que se dispone de esta información correcta y completa si se dispone de ésta a partir del día 11 del mes en curso.

La empresa distribuidora como encargada de lectura deberá aplicar los coeficientes de reparto βh,i que contenga el acuerdo firmado que le haya sido notificado. En ningún caso los coeficientes se aplicarán a energía generada con anterioridad a la fecha señalada en el párrafo anterior.

Si la información no estuviera completa o resultase incorrecta la empresa distribuidora deberá solicitar la pertinente subsanación a los consumidores, o en su caso los comercializadores que actúen como mandatarios de los mismos.

Sin perjuicio de lo previsto en el artículo 8.5 del Real Decreto 244/2019, de 5 de abril, en relación con la permanencia en la modalidad de autoconsumo elegida, el valor de los coeficientes de reparto podrá ser modificado con una periodicidad no inferior a cuatro meses, previa comunicación al encargado de la lectura correspondiente con la antelación suficiente.

2. La energía horaria autoconsumida individualizada de aquellos sujetos que realicen autoconsumo colectivo o consumidor asociado a una instalación próxima a través de la red, Eauth,i, de cada uno de los consumidores i se calculará como:

a) Si la energía horaria consumida individualizada del consumidor es superior en valor absoluto a la energía horaria neta generada individualizada, el autoconsumo horario individualizado será el valor de la energía horaria neta generada individualizada:

Eauth,i = ENGh,i

b) Si es inferior, el autoconsumo horario individualizado, Eauth,i, será el valor de la energía horaria consumida individualizada de cada consumidor.

3. En su caso, para las instalaciones de autoconsumo con excedentes, en los que existan varias instalaciones de producción con un solo equipo de medida de generación neta, el reparto de la energía horaria excedentaria de generación vertida entre cada una de las instalaciones de producción k que participen en dicho autoconsumo colectivo o instalaciones próximas a través de la red será:

Vh,k = αk * (ENGh,k – ∑iEauth,i)

Siendo:

Vh,k:Es el vertido neto horario de la instalación k.

ENGh,k:Es la energía neta horaria producida por la instalación k.

αk:Es el coeficiente de reparto de la energía horaria neta generada por la instalación k que se utilizará en ausencia de definición de coeficientes de reparto por acuerdo firmado por todos los sujetos participantes del autoconsumo colectivo y notificado al distribuidor como encargado de lectura de la generación siempre que la suma de estos coeficientes de todos los consumidores que participan en el autoconsumo colectivo sea la unidad.

Estos coeficientes se calcularán de acuerdo a la siguiente formulación:

![imagen](https://www.boe.es/datos/imagenes/disp/2019/83/05089_9547.png)

Siendo:

PIk: la potencia instalada de la instalación k.

∑jPIj:suma de las potencias instaladas de las instalaciones de generación.

4. En cualquier caso, la suma de la energía horaria excedentaria y la energía horaria autoconsumida de todos los consumidores asociados debe ser igual a la energía neta horaria total producida por el generador o los generadores.

> Se modifica el apartado 1 por el art. único de la Orden TED/1247/2021, de 15 de noviembre de 2021. Ref. BOE-A-2021-18706

> Téngase en cuenta, en la primera modificación del acuerdo de reparto para implementar los coeficientes de reparto variables, la disposición transitoria 2 de la citada Orden.
