## ANEXO I

## Generación de un NRC (Número de Referencia Completo)

El NRC se generará a partir de los datos siguientes:

| Número de Referencia (Generado por la Entidad) | MMMBBBBNNNNNDC | (14) | Siendo: MMM = 901 (euros). BBBB = Código de Banco de España NNNNN= Número secuencia) correlativo. D = Dígito de control del justificante. C = Carácter de control complementario. |
| --- | --- | --- | --- |
| NIF del contribuyente | XXXXXXXXX | (9) |  |
| Fecha de vencimiento | MMAA | (4) | Siendo: MM = Mes AA = Año 0000 = Indefinido |
| Códigos de aval | X | (1) | «1»= Suspensión ejecución recurso de reposición. «2»= Suspensión ejecución reclamación económico-administrativa. «3»= Aplazamientos/Fraccionamientos. «4»= Devolución IVA. «5»= Deuda aduanera IVA e Impuestos Especiales. «6»= Régimen de tránsito comunitario. «7» = Deudas aduaneras y fiscales en representación directa. «8» = Actas con acuerdo. |
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

Fecha de Vencimiento: Mes y Año de vencimiento del aval. Si se presta con carácter indefinido, se consignará 0000 (siempre en los avales con código 1, 2, 4, 5, 7 y 8).

Códigos de aval:

(1) Suspensión ejecución recurso de reposición.

(2) Suspensión ejecución reclamación económico-administrativa.

(3) Aplazamientos/Fraccionamientos.

(4) Devolución IVA.

(5) Deuda aduanera, I.V.A. e Impuestos Especiales.

(6) Régimen de tránsito comunitario.

(7) Deudas aduaneras y fiscales en representación directa.

(8) Actas con acuerdo.

Importe: Se indicará la cifra (un número entero), ajustada a la derecha y rellena con ceros a la izquierda, hasta completar las 12 posiciones. El importe avalado se expresará en céntimos de euro, para evitar el uso de decimales."
