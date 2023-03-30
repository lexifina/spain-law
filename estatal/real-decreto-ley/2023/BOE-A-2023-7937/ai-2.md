## ANEXO II

## Documentación para acreditar el registro de los instrumentos de cobertura en una cámara de contrapartida central o la comunicación de los mismos de acuerdo con REMIT o EMIR

La documentación concreta que tendrá validez para la acreditación del registro de los instrumentos de cobertura en cámaras de contrapartida central o la comunicación de los mismos bajo normativa REMIT/EMIR, será la siguiente:

1. Instrumentos de cobertura registrados en cámaras de contrapartida central (CCP):

Deberá remitirse un certificado expedido por la cámara de contrapartida central con la posición neta compradora del agente, asociada a instrumentos de cobertura a plazo registrados en dicha cámara de contrapartida central antes del 7 de marzo de 2023, con periodo de entrega o de liquidación entre junio y diciembre de 2023.

2. Instrumentos de cobertura comunicados bajo la normativa REMIT:

Para cada transacción realizada antes del 7 de marzo de 2023 que haya sido comunicada a ACER, de instrumentos de cobertura a plazo con periodo entrega o de liquidación entre junio y diciembre de 2023, deberán remitirse los siguientes dos archivos xml:

a) En caso de comunicación de datos bajo Table 1:

– <REMITTable1 xmlns=http://www.acer.europa.eu/REMIT/REMITTable1_V2.xsd>

– <REMITReceipt

xmlns=http://www.acer.europa.eu/REMIT/REMITReceiptSchema_V1.xsd>

b) En caso de comunicación de datos bajo Table 2:

– <ns0:REMITTable2 xml:ns0ns=http://www.acer.europa.eu/REMIT/REMITTable2_V1.xsd>

– <REMITReceipt

xmlns=http://www.acer.europa.eu/REMIT/REMITReceiptSchema_V1.xsd>

3. Instrumentos de cobertura comunicados bajo la normativa EMIR:

Para cada transacción realizada antes del 7 de marzo de 2023 y que haya sido comunicada bajo EMIR, de instrumentos de cobertura a plazo con periodo entrega o de liquidación entre junio y diciembre de 2023, deberá remitirse el documento xml con el detalle del reporte de datos de la transacción bajo EMIR, así como el xml por el que el trade repository valida la comunicación de datos de la transacción.

A modo de ejemplo, en el caso de comunicación de datos al trade repository REGIS-TR, se remitirán los informes D431 y W440.
