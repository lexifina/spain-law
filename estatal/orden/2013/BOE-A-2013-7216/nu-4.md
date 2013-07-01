## IV. Instrucciones para la cumplimentación del mensaje de notificación de recepción

Los receptores de productos objeto de los impuestos especiales de fabricación que hayan circulado con origen y destino en el ámbito territorial interno al amparo de un documento administrativo electrónico estarán obligados a presentar, ante la Agencia Estatal de Administración Tributaria, una notificación de recepción tan pronto como se reciban los productos y, en todo caso, dentro de los cinco días hábiles siguientes a la terminación de la circulación. Este plazo podrá ampliarse exclusivamente en los casos en que, previamente justificados, sean autorizados por la oficina gestora.

La Agencia Estatal de Administración Tributaria verificará por vía electrónica los datos en ella incluidos y, si dichos datos no son válidos, informará de ello sin demora al destinatario. Si dichos datos son válidos, confirmará al destinatario el registro de la notificación de recepción presentada y la pondrá a disposición del expedidor.

En los supuestos de envío de productos por los que se haya aplicado una exención o un tipo impositivo reducido a destinatarios no inscritos en el registro territorial de la oficina gestora, el destinatario deberá devolver al expedidor uno de los ejemplares impresos del documento administrativo electrónico, de acuerdo con lo previsto en el artículo 31.B)3. del Reglamento de los Impuestos Especiales.

En los supuestos de exportación, la Aduana de salida cumplimentará la salida en el Sistema Electrónico de Control de Exportación (ECS-Export Control System) y, a través de este sistema, se volcará en el EMCS.

El mensaje de notificación de recepción se presentará con cumplimiento de las siguientes instrucciones:

1. Atributo

Este grupo de datos no se cumplimentará y serán facilitados por la AEAT tras la aceptación del mensaje de notificación de recepción.

1a. Fecha de validación.

1b. Hora de validación.

1c. Código Seguro de Verificación (CSV).

2. Destinatario

Grupo de datos obligatorio.

2a. Destinatario NIF

Obligatorio.

Se indicará el NIF.

2b. Destinatario nombre.

Obligatorio.

Deberá consignarse el nombre y apellidos o razón social del destinatario.

2c. Destinatario CAE.

Obligatorio.

Deberá consignarse el CAE declarado en el e-DA para el que se está realizando la notificación de recepción.

3. Documento

Grupo de datos obligatorio.

3a. ARC.

Obligatorio.

Se indicará el ARC del e-DA.

3b. Número de secuencia.

Obligatorio.

Se indicará el número de secuencia del e-DA.

4. Recepción

Grupo de datos obligatorio.

4a. Fecha de recepción.

Cumplimentación obligatoria.

Se indicará la fecha en la que el destinatario haya recibido los productos sujetos a impuestos especiales.

4b. Resultado de la recepción.

Cumplimentación obligatoria.

Se indicará alguno de los siguientes valores:

| Códigos | Descripción |
| --- | --- |
| 1 | Recepción aceptada y satisfactoria de todos las partidas de orden del e-DA. |
| 2 | Recepción aceptada aunque insatisfactoria. |
| 3 | Recepción rechazada. |
| 4 | Recepción rechazada parcialmente. |

Si se consigna cualquiera de los códigos 2 ó 4, deberá cumplimentarse adicionalmente el bloque de datos 5, a nivel de partida.

4c. Información complementaria.

Cumplimentación opcional.

Facilitará cualquier información relativa a la recepción de los productos sujetos a impuestos especiales.

4d. Autoridad fiscal en destino.

Cumplimentación obligatoria.

Se indicará el código de seis caracteres correspondiente a la oficina gestora responsable del control de los impuestos especiales en el lugar de recepción o exportación, de acuerdo con los siguientes códigos:

| Código | Oficina |
| --- | --- |
| D01200 | Áraba/Álava. |
| D02200 | Albacete. |
| D03200 | Alicante. |
| D04200 | Almería. |
| D05200 | Ávila. |
| D06200 | Badajoz. |
| D07200 | Illes Balears. |
| D08200 | Barcelona. |
| D09200 | Burgos. |
| D10200 | Cáceres. |
| D11200 | Cádiz. |
| D12200 | Castellón. |
| D13200 | Ciudad Real. |
| D14200 | Córdoba. |
| D15200 | A Coruña. |
| D16200 | Cuenca. |
| D17200 | Girona. |
| D18200 | Granada. |
| D19200 | Guadalajara. |
| D20200 | Guipúzkoa. |
| D21200 | Huelva. |
| D22200 | Huesca. |
| D23200 | Jaén. |
| D24200 | León. |
| D25200 | Lleida. |
| D26200 | La Rioja. |
| D27200 | Lugo. |
| D28200 | Madrid. |
| D29200 | Málaga. |
| D30200 | Murcia. |
| D31200 | Navarra. |
| D32200 | Ourense. |
| D33200 | Oviedo. |
| D34200 | Palencia. |
| D35200 | Las Palmas. |
| D36200 | Pontevedra. |
| D37200 | Salamanca. |
| D38200 | S.C. Tenerife. |
| D39200 | Santander. |
| D40200 | Segovia. |
| D41200 | Sevilla. |
| D42200 | Soria. |
| D43200 | Tarragona. |
| D44200 | Teruel. |
| D45200 | Toledo. |
| D46200 | Valencia. |
| D47200 | Valladolid. |
| D48200 | Bizkaia. |
| D49200 | Zamora. |
| D50200 | Zaragoza. |
| D51200 | Cartagena. |
| D52200 | Gijón. |
| D53200 | Jerez F. |
| D54200 | Vigo. |

5. Cantidades recepción

Este grupo de datos se cumplimentará, a nivel de partida, en los casos de resultado de la recepción (4b) «aceptada aunque insatisfactoria» (2) o «recepción rechazada parcialmente» (4). Puede repetirse hasta 99 veces.

5a. Número de partida original.

Obligatorio.

Se indicará la partida de orden (casilla 12a del documento administrativo electrónico) cuya recepción no ha sido aceptada y satisfactoria.

5b. Indicador de cantidad en exceso o en defecto.

Obligatoria cuando se hayan detectado a la recepción cantidades en exceso o en defecto.

Se indicará alguno de los siguientes códigos:

| Código | Descripción |
| --- | --- |
| S | Cuando se haya detectado defecto. |
| E | Cuando se haya detectado exceso. |

5c. Cantidad en exceso o defecto observada.

Obligatoria cuando se haya cumplimentado la casilla 5b anterior.

Se indicará la cantidad, con dos decimales, expresada en la unidad de medida asociada al código del producto, de acuerdo con la tabla del anexo 3.

5d. Epígrafe.

Se indicará el código aplicable al producto sujeto a impuestos especiales, de acuerdo con los códigos del anexo 3.

5e. Cantidad rechazada.

Obligatoria si se ha consignado el código 4 (recepción rechazada parcialmente) en la casilla 4b anterior. Se indicará la cantidad, con dos decimales, en la medida asociada al código de producto, de acuerdo con la tabla del anexo 3.

5f. Motivo de la insatisfacción.

Obligatoria para cada una de las partidas cuya recepción no haya sido «1. Aceptada y satisfactoria» Se indicará uno de los siguientes valores:

| Valores | Descripción |
| --- | --- |
| 0 | Otro. |
| 1 | Exceso. |
| 2 | Defecto. |
| 3 | Productos dañados. |
| 4 | Precinto roto. |
| 6 | Una o varias partidas con valores incorrectos. |
