## ANEXO I

## Generación de un NRC (Número de Referencia Completo)

El NRC se generará a partir de los datos siguientes:

| Número de Referencia (Generado por la Entidad) | MMMBBBBNNNNNDC | (14) | Siendo: MMM = 901 (euros). BBBB = Código de Banco de España NNNNN= Número secuencia) correlativo. D = Dígito de control del justificante. C = Carácter de control complementario. |
| --- | --- | --- | --- |
| NIF del contribuyente | XXXXXXXXX | (9) |  |
| Fecha de vencimiento | MMAA | (4) | Siendo: MM = Mes AA = Año 0000 = Indefinido |
| Códigos de aval | X | (1) | «1»= Suspensión ejecución recurso de reposición. «2»= Suspensión ejecución reclamación económico-administrativa. «3»= Aplazamientos/Fraccionamientos. «4»= Devolución IVA. «5»= Garantía de deudas aduaneras y tributarias por operaciones aduaneras. «6»= Garantía con modelos previstos en el Reglamento de Ejecución (UE) 2015/2447. «7» = Adenda al modelo de aval tipo 5, 7 y 9 vigentes a la entrada en aplicación del Reglamento (UE) n.º 952/2013 del Parlamento Europeo y del Consejo, de 9 de octubre de 2013, por el que se establece el código aduanero de la Unión. «8» = Actas con acuerdo. «9» = Garantía por deudas tributarias por operaciones previstas en la normativa de Impuestos Especiales. |
| Importe | XXX | (12) | Siendo XXXXXXXXXXXX = Importe avalado de la liquidación recurrida (en los códigos «1» y «2») o el importe garantizado(en el resto de códigos). |
|  | LONGITUD TOTAL | (40) | DATO DE LA OPERACIÓN |

![imagen](https://www.boe.es/datos/imagenes/disp/2006/61/04511_10379497_image1.png)

El Número de Referencia Completo (NRC) de la presentación será:

![imagen](https://www.boe.es/datos/imagenes/disp/2006/61/04511_10379497_image2.png)

Detalle de los datos a incluir para generar el NRC:

Para generar el NRC es imprescindible que todos estos datos, a incluir en los procedimientos de cifrado, estén en EBCDIC.

MMM: Código de Modelo para Avales: 901 (euros)

BBBB: Cuatro primeros dígitos del Código del Banco de España.

NNNNN: Número secuencial correlativo, comenzando por 00000. Caso de llegar a 99999, se comenzaría por 00000.

D: Dígito de control del «MMMBBBBNNNNN», generado con el mismo algoritmo que el actual número de justificante de las autoliquidaciones.

C: Carácter de control complementario, generado aplicando un algoritmo que será facilitado a una de las personas designadas por la entidad avalista. Sólo se utilizará para el NRC.

MMMBBBBNNNNNDC: Conforman el Número de Referencia, que formará parte del NRC.

NIF: NIF del contribuyente. En el caso de que existan varios avalados, se consignará el correspondiente al primero que se haya señalado en el cuerpo del modelo.

Fecha de vencimiento: Mes y año de vencimiento del aval. Si se presta con carácter indefinido, se consignará 0000 (siempre en los avales con código 1, 2, 4, 5, 7, 8 y 9).

Códigos de aval:

(1) Suspensión ejecución recurso de reposición.

(2) Suspensión ejecución reclamación económico-administrativa.

(3) Aplazamientos/Fraccionamientos.

(4) Devolución IVA.

(5) Garantía de deudas aduaneras y tributarias por operaciones aduaneras.

(6) Garantía con modelos previstos en el Reglamento de Ejecución (UE) 2015/2447.

(7) Adenda al modelo de aval tipo 5, 7 y 9 vigentes a la entrada en aplicación del Reglamento (UE) n.º 952/2013 del Parlamento Europeo y del Consejo, de 9 de octubre de 2013, por el que se establece el código aduanero de la Unión.

(8) Actas con acuerdo.

(9) Garantía por deudas tributarias por operaciones previstas en la normativa de Impuestos Especiales.

Importe: Se indicará la cifra (un número entero), ajustada a la derecha y rellena con ceros a la izquierda, hasta completar las 12 posiciones. El importe avalado se expresará en céntimos de euro, para evitar el uso de decimales."

> Se modifica por el art. único.5 de la Resolución de 11 de febrero de 2019. Ref. BOE-A-2019-2288

> Se modifica por el art. único.3 de la Resolución de 15 de julio de 2014. Ref. BOE-A-2014-7793
