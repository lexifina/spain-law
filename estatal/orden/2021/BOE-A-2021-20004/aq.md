## Artículo quinto. Modificación de la Orden EHA/3290/2008, de 6 de noviembre, por la que se aprueba el modelo 216 «Impuesto sobre la Renta de no Residentes. Rentas obtenidas sin mediación de establecimiento permanente. Retenciones e ingresos a cuenta. Declaración-documento de ingreso» y el modelo 296 «Impuesto sobre la Renta de no Residentes. No residentes sin establecimiento permanente. Declaración anual de retenciones e ingresos a cuenta».

La Orden EHA/3290/2008, de 6 de noviembre, por la que se aprueban el modelo 216 y el modelo 296, queda modificada como sigue:

Uno. Se modifica el campo «SUBCLAVE», que ocupa las posiciones 102-103 del registro de tipo 2, registro de perceptor, de los diseños físicos y lógicos del modelo 296, contenidos en el anexo III, que tendrá la siguiente redacción:

> | «Posiciones | Naturaleza | Descripción de los campos |
> | --- | --- | --- |
> | 102-103 | Numérico. | Subclave |
> |  |  | Se consignará la que corresponda en función de las circunstancias tenidas en cuenta para el cálculo de la retención o ingreso a cuenta, según la relación siguiente: |
> |  |  | 01. Retención practicada a los tipos generales o escalas de tributación del artículo 25 de la Ley del Impuesto sobre la Renta de no Residentes. |
> |  |  | 02. Retención practicada aplicando límites de imposición de Convenios. |
> |  |  | 03. Exención interna (principalmente: artículo 14 de la Ley del Impuesto sobre la Renta de no Residentes) excepto los supuestos a que se refiere la subclave 12. |
> |  |  | 04. Exención por aplicación de un Convenio. |
> |  |  | 05. Sin retención por previo pago del Impuesto por el contribuyente o su representante. |
> |  |  | 06. El perceptor declarado es una entidad extranjera de gestión colectiva de derechos de la propiedad intelectual, habiéndose practicado retención aplicando el límite de imposición, o la exención, de un Convenio, conforme a lo previsto en el artículo 18 de esta Orden. |
> |  |  | 07. El perceptor es un contribuyente del Impuesto sobre la Renta de las Personas Físicas del régimen especial aplicable a los trabajadores desplazados a territorio español, a que se refiere el artículo 93 de la Ley del Impuesto sobre la Renta de las Personas Físicas excepto los supuestos a que se refiere la subclave 13. |
> |  |  | 08. El perceptor declarado es una entidad residente en el extranjero comercializadora de acciones o participaciones de instituciones de inversión colectiva españolas, habiéndose practicado retención aplicando un límite de imposición fijado en el Convenio inferior al previsto en el artículo 25 del texto refundido de la Ley del Impuesto sobre la Renta de no Residentes, conforme al procedimiento especial previsto en el artículo 19 de esta Orden. |
> |  |  | 09. El perceptor declarado es una entidad residente en el extranjero comercializadora de acciones o participaciones de instituciones de inversión colectiva españolas, habiéndose practicado retención aplicando el tipo de gravamen previsto en el artículo 25 del texto refundido de la Ley del Impuesto sobre la Renta de no Residentes, conforme el procedimiento especial previsto en el artículo 19 de esta Orden. |
> |  |  | 10. Ingreso a cuenta a que se refiere el artículo 36.2 del texto refundido de la Ley del Impuesto sobre la Renta de no Residentes, realizado por una entidad en régimen de atribución de rentas en relación con la renta atribuida a un miembro no residente. |
> |  |  | 11. El perceptor declarado es un contribuyente que ha acreditado al pagador haber hecho uso del procedimiento previsto en el artículo 32 del texto refundido de la Ley del Impuesto sobre la Renta de no Residentes. |
> |  |  | 12. Dietas y asignaciones para gastos de viaje exceptuados de gravamen (artículo 9 del Reglamento del Impuesto sobre la Renta de las Personas Físicas). |
> |  |  | 13. El perceptor es un contribuyente del Impuesto sobre la Renta de las Personas Físicas del régimen especial aplicable a los trabajadores desplazados a territorio español a que se refiere el artículo 93 de la Ley del Impuesto sobre la Renta de las Personas Físicas. Dietas y asignaciones para gastos de viaje exceptuados de gravamen (artículo 9 del Reglamento del Impuesto sobre la Renta de las Personas Físicas). |
> |  |  | En los supuestos a que se refieren las subclaves 06, 07, 08, 09, 10, 11 y 13 de la relación anterior, se consignarán siempre estas subclaves específicas sin tener en consideración el resto de subclaves.» |

Dos. Se añade un nuevo campo «INGRESOS A CUENTA REPERCUTIDOS», que ocupa las posiciones 389-401 del registro de tipo 2, registro de perceptor, de los diseños físicos y lógicos del modelo 296, contenidos en el anexo III, con el siguiente contenido:

> | «Posiciones | Naturaleza | Descripción de los campos |
> | --- | --- | --- |
> | 389-401 | Numérico. | Ingresos a cuenta repercutidos |
> |  |  | Campo numérico de 13 posiciones. |
> |  |  | Cuando en el campo “NATURALEZA” (posición 99 del registro de tipo 2) se haya consignado el valor E (Renta en especie) y tenga contenido el campo “RETENCIONES E INGRESOS A CUENTA” (posición 121-133 del registro de tipo 2), se consignará en este campo el importe de los ingresos a cuenta efectuados que, en su caso, el pagador de las retribuciones en especie hubiera repercutido al perceptor. |
> |  |  | Los importes deben consignarse en EUROS. |
> |  |  | Este campo se subdivide en dos: |
> |  |  | 389-399 Entero. Parte entera del importe de las retenciones e ingresos a cuenta (si no tiene contenido se consignará a ceros). |
> |  |  | 400-401 Decimal. Parte decimal del importe de las retenciones e ingresos a cuenta (si no tiene contenido se consignará a ceros).» |

Tres. El campo «BLANCOS», que ocupa las posiciones 389-432 del registro de tipo 2, registro de perceptor, de los diseños físicos y lógicos del modelo 296, contenidos en el anexo III pasa a ocupar las posiciones 402-432.
