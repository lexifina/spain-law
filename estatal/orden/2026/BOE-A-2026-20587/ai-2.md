## ANEXO II

## Contenido y estructura de los campos del mensaje relativo a los estados de pago, rechazo, cobro o impago de las facturas conforme al modelo UBL

La información del pago, rechazo, cobro o impago de las facturas que, en cumplimiento de lo dispuesto en la presente orden, sean transmitidas a la Agencia Estatal de Administración Tributaria deberán contener, en los términos establecidos en el artículo 12 del Real Decreto 238/2026, de 25 de marzo, por el que se desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y por el que se modifica el Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, la información que se muestra a continuación.

I. Campos de registro y especificaciones funcionales de la información de los estados de pago, rechazo o cobro de las facturas electrónicas a la solución pública de facturación electrónica

Cada elemento de información o grupo de elementos de información que constituye el modelo semántico de datos de los elementos principales de la comunicación de los estados de pago, cobro o impago, se define en las filas de la siguiente tabla, incluyendo cada columna la siguiente información:

– Nivel: indica el nivel en el que el elemento de información interviene en el modelo:

+: primer nivel del modelo;

++: segundo nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el primer nivel del modelo;

+++: tercer nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el segundo nivel del modelo;

++++: cuarto nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el tercer nivel del modelo.

– Cardinalidad: se utiliza para indicar si un elemento o grupo de elementos de información es obligatorio o no (condicional), y si se puede repetir. Pueden darse las siguientes cardinalidades:

1..1: elemento obligatorio y no repetitivo.

0..1: elemento condicional y no repetitivo.

– Término de negocio: el nombre del elemento o grupo de elementos de información utilizado en el modelo de estado de pago o cobro.

– Descripción: descripción del significado semántico del elemento de información.

– Tipo semántico de dato: formato de dato que se aplica al elemento de información.

– Ruta UBL: expresión que identifica un elemento o atributo dentro de la estructura XML del documento de «Application Response» de UBL, en su última versión aprobada.

1. Información sobre el pago de la factura electrónica

Se recoge a continuación el contenido y estructura de los campos de los mensajes de alta y baja de pago efectivo completo de la factura electrónica a la solución pública de facturación electrónica, por parte del destinatario de la misma.

| COMUNICACIÓN DE PAGOS POR EL DESTINATARIO - Mensaje de alta | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: PAYMENT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Fecha de efecto | Fecha de expedición del pago o situación del pago. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveDate |
| + | 1..1 | Fecha de vencimiento del plazo de pago | Fecha de vencimiento del plazo de pago, calculada de acuerdo con lo dispuesto en el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales o en la normativa específica que resulte de aplicación. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=DueDate |
| + | 0..1 | Fecha de recepción de las mercancías o de los servicios prestados | Campos opcionales, a informar si, de acuerdo con el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales, esta información resulta relevante. Si no se informan, de acuerdo con lo dispuesto en la D.A. 7.ª del Real Decreto 238/2026, de 25 de marzo, por el que se desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y por el que se modifica el Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, se entenderá como fecha de inicio del plazo de pago la fecha de expedición de la factura. | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse cac:Response//cac:Status/cac:Condition/cbc:AttributeID=ShipmentDate |
| + | 0..1 | Fecha de recepción de la factura | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=ReceptionDate |
| + | 0..1 | Factura rectificada | Factura que ha sido previamente rectificada (y la confirmación no necesariamente será por el importe de la factura original) | Indicador | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:StatusReason=CorrectedInvoice |
| + | 0..1 | Factura rectificativa | Factura sin pago asociado (factura rectificativa negativa) | Indicador | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:StatusReason=NegativeAmountInvoice |
| + | 1..1 | FACTURA INFORMADA | Datos de la factura sobre la que se informa el pago |  |  |
| ++ | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| ++ | 1..1 | Fecha de expedición de la factura. | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| ++ | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |
| COMUNICACIÓN DE PAGOS POR EL DESTINATARIO - Mensaje de baja | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: CANCELPAYMENT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| + | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| + | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |

2. Información sobre el rechazo de la factura electrónica

Se recoge a continuación el contenido y estructura de los campos de los mensajes de alta y baja de rechazo de la factura electrónica a la solución pública de facturación electrónica, por parte del destinatario de la misma.

| COMUNICACIÓN DE RECHAZO POR EL DESTINATARIO- Mensaje de alta | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: REJECTION |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Fecha de rechazo | Fecha de rechazo por el destinatario. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveDate |
| + | 1..1 | Motivo de rechazo | Motivo por el que se rechaza la factura. Admite dos valores posibles: - Rechazo comercial. - Rechazo por ser un consumo particular o no estar afectado a la actividad. | Código (L1) | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:ConditionCode |
| + | 1..1 | FACTURA INFORMADA | Datos de la factura sobre la que se informa el rechazo |  |  |
| ++ | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| ++ | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| ++ | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |
| COMUNICACIÓN DE RECHAZO POR EL DESTINATARIO - Mensaje de baja | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: CANCELREJECTION |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| + | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| + | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |

3. Información sobre el cobro de la factura electrónica

Se recoge a continuación el contenido y estructura de los campos de los mensajes de alta y baja de cobro de la factura electrónica a la solución pública de facturación electrónica, por parte del emisor de la misma.

| COMUNICACIÓN DE COBRO POR EL EMISOR - Mensaje de alta | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: SETTLEMENT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Fecha del cobro | Fecha de cobro por el emisor. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveDate |
| + | 0..1 | Fecha de vencimiento del pago | Fecha de vencimiento del pago, calculada de acuerdo con lo dispuesto en el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales o en la normativa específica que resulte de aplicación. | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=DueDate |
| + | 0..1 | Mecanismo de financiación | Indicador de si el cobro se ha producido a través de un mecanismo de financiación concertado por el emisor. | Indicador | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cac:Condition/cbc:AttributeID=FinancingArrangement |
| + | 0..1 | Fecha de recepción de las mercancías o de los servicios prestados | Campos opcionales, a informar si, de acuerdo con el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales, esta información resulta relevante. Si no se informan, de acuerdo con lo dispuesto en la D.A. 7.ª del Real Decreto 238/2026, de 25 de marzo, por el que se desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y por el que se modifica el Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, se entenderá como fecha de inicio del plazo de pago la fecha de expedición de la factura. | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=ShipmentDate |
| + | 0..1 | Fecha de recepción de la factura | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=ReceptionDate |
| + | 1..1 | FACTURA INFORMADA | Datos de la factura sobre la que se informa el pago |  |  |
| ++ | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| ++ | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| ++ | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |
| COMUNICACIÓN DE COBRO POR EL EMISOR - Mensaje de baja | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: CANCELSETTLEMENT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| + | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| + | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |

4. Información sobre el impago de la factura electrónica

Se recoge a continuación el contenido y estructura de los campos de los mensajes de alta y baja de impago de la factura electrónica a la solución pública de facturación electrónica, por parte del emisor de la misma.

| COMUNICACIÓN DE IMPAGO POR EL EMISOR - Mensaje de alta | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: DEFAULT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Fecha de vencimiento del pago | Fecha de vencimiento del pago, calculada de acuerdo con lo dispuesto en el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales o en la normativa específica que resulte de aplicación. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveDate |
| + | 0..1 | Fecha de recepción de las mercancías o de los servicios prestados | Campos opcionales, a informar si, de acuerdo con el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales, esta información resulta relevante. Si no se informan, de acuerdo con lo dispuesto en la D.A. 7.ª del Real Decreto 238/2026, de 25 de marzo, por el que se desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y por el que se modifica el Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, se entenderá como fecha de inicio del plazo de pago la fecha de expedición de la factura. | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=ShipmentDate |
| + | 0..1 | Fecha de recepción de la factura | Fecha | ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cbc:ReferenceDate ApplicationResponse/cac:DocumentResponse/ cac:Response/cac:Status/cac:Condition/cbc:AttributeID=ReceptionDate |
| + | 1..1 | FACTURA INFORMADA | Datos de la factura sobre la que se informa el pago |  |  |
| ++ | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| ++ | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| ++ | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |
| COMUNICACIÓN DE IMPAGO POR EL EMISOR - Mensaje de baja | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: CANCELDEFAULT |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Número de factura (ID) | Serie y número que identifican la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID |
| + | 1..1 | Fecha de emisión factura | Fecha de expedición de la factura informada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:IssueDate |
| + | 1..1 | NIF emisor | Número de identificación fiscal (NIF) del vendedor en la factura informada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| ++ | 1..1 | Nombre / Razón social emisor | Nombre o razón social del vendedor en la factura informada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationName |

II. Claves y valores permitidos en campos de tipo código

Se definen a continuación los valores permitidos en los campos con tipo semántico de dato de tipo código en los que se ha indicado expresamente que se definirán los valores en una lista (L). En los restantes campos de tipo código, en la columna descripción, se indica la forma de definición de los valores admitidos.

L1 – Motivos de rechazo

| Valores | Descripción |
| --- | --- |
| 01 | Rechazo comercial |
| 02 | Rechazo por ser un consumo particular o no estar afectado a la actividad. |
