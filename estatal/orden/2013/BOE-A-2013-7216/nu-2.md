## II. Instrucciones para la cumplimentación del mensaje de anulación

El procedimiento de circulación al amparo de un e-DA prevé que el documento administrativo electrónico pueda anularse pero siempre que no haya comenzado la circulación. La anulación del e-DA se ha de realizar a través de un mensaje que contiene los siguientes datos:

1. Atributo

Este grupo de datos no se cumplimentará y serán facilitados por la AEAT tras la aceptación del mensaje de anulación.

1a. Fecha de validación.

1b. Hora de validación.

1c. Código Seguro de Verificación (CSV).

2. Documento

Grupo de datos obligatorio.

2a. ARC.

Obligatorio.

Se indicará el ARC del documento administrativo electrónico (e-DA) para el que se solicita la anulación.

3. Anulación

Grupo de datos obligatorio.

3a. Razón de la Anulación.

Obligatorio.

Se indicará uno de los siguientes valores:

| Valores | Descripción |
| --- | --- |
| 0 | Otro. |
| 1 | Error tipográfico. |
| 2 | Operación comercial interrumpida. |
| 3 | e-DA duplicado. |
| 4 | La circulación no se ha iniciado en la fecha de expedición. |

3b. Información complementaria.

Opcional.

Se consignará cualquier información adicional relativa a la razón de la anulación.
