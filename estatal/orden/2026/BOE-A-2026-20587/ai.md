## ANEXO I

## Contenido y estructura de los campos de la factura electrónica conforme al modelo UBL y la EN 16931

Las facturas electrónicas y copias fieles que, en cumplimiento de lo dispuesto en la presente orden, sean transmitidas a la Agencia Estatal de Administración Tributaria deberán contener como mínimo, en los términos establecidos en los artículos 7.1 y 11.2 y 11.3 del Real Decreto 238/2026, de 25 de marzo, por el que se desarrolla el sistema de facturación electrónica obligatoria entre empresarios y profesionales y por el que se modifica el Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre, la información que se muestra a continuación.

Campos de registro y especificaciones funcionales de la factura electrónica y las copias fieles remitidas a la solución pública de facturación electrónica

Cada elemento de información o grupo de elementos de información que constituye el modelo semántico de datos de los elementos principales de una factura electrónica, se define en las filas de la siguiente tabla, incluyendo cada columna la siguiente información:

– ID: identificador del elemento de información (BT-Término de negocio, por sus siglas en inglés), y grupo de elementos de información (BG- Grupo de términos de negocio, por sus siglas en inglés), tal y como se definen en la EN 16931. En el caso de campos no definidos expresamente en la EN 16931, se identifican con los códigos BT-ES y BG-ES, respectivamente.

– Nivel: indica el nivel en el que el elemento de información interviene en el modelo:

+: primer nivel del modelo;

++: segundo nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el primer nivel del modelo;

+++: tercer nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el segundo nivel del modelo;

++++: cuarto nivel del modelo. El elemento o grupo de elementos de información es parte de un grupo de elementos de información que se definen en el tercer nivel del modelo.

– Cardinalidad: se utiliza para indicar si un elemento o grupo de elementos de información es obligatorio o no (condicional), y si se puede repetir. Pueden darse las siguientes cardinalidades:

1..1: elemento obligatorio y no repetitivo.

1..n: elemento obligatorio y repetitivo.

0..1: elemento condicional y no repetitivo.

0..n: elemento condicional y repetitivo.

– Término de negocio: el nombre del elemento o grupo de elementos de información utilizado en el modelo de factura electrónica.

– Descripción: descripción del significado semántico del elemento de información.

– Tipo semántico de dato: formato de dato que se aplica al elemento de información.

– Ruta UBL: expresión que identifica un elemento o atributo dentro de la estructura XML del documento de factura electrónica UBL, en su última versión aprobada. Aparecerá especificado en aquellos campos que no tienen término de negocio definido en la EN 16931, así como en aquellos campos cuyo uso implica informar con un valor determinado campos sin término de negocio definido en la EN 16931 y que no están expresamente incluidos en el anexo I.

| FACTURA ELECTRÓNICA O COPIA FIEL - Mensaje de alta | /Invoice/ |
| --- | --- |
| ID | Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- | --- |
| BT-1 | + | 1..1 | Serie y número de la factura | Serie y número que identifican la factura emitida. | Identificador |  |
| BT-ES-1 | + | 0..1 | Indicador de copia | Adoptará alguno de los siguientes valores: True: copia. False (o sin informar): original. | Indicador | /in:Invoice/cbc:CopyIndicator |
| BT-2 | + | 1..1 | Fecha de expedición de la factura | Fecha en la que se ha expedido la factura. | Fecha |  |
| BT-166 | + | 0..1 | Hora de expedición de la factura | Hora en la que se ha expedido la factura. | Hora |  |
| BT-3 | + | 1..1 | Código de tipo de factura | Las facturas comerciales se definen de acuerdo con los códigos definidos en UNTDID 1001. Sólo podrán adoptarse los valores definidos en la lista L1. Las facturas emitidas con valores 384 y 471 incorporarán el grupo de términos de negocio de tipo de factura rectificativa (BG-24), el grupo de términos de negocio de modalidad de factura rectificativa (BG-24) y, en su caso, hasta tres grupos de términos de negocio de importes rectificados (BG-24). | Código (L1) |  |
| BT-5 | + | 1..1 | Código de moneda de la factura | Moneda en la que se expresan todos los importes de la factura, excepto aquellos campos en los que se indica expresamente que deben expresarse en euros. Los códigos se definen en la Norma ISO-4217 «códigos para la representación de monedas y fondos». | Código |  |
| BT-6 | + | 0..1 | Código de moneda de contabilización del IVA | En aquellos casos en los que la moneda de la factura no sea el euro, se consignará obligatoriamente como moneda de contabilización del IVA el euro. Valor obligatorio: usar «EUR». | Código |  |
| BT-167 | + | 0..1 | Tipo de cambio de contabilización del IVA | Tipo de cambio aplicado para contabilizar el IVA, en aquellos casos en los que la moneda de la factura no sea el euro. | Importe |  |
| BT-7 | + | 0..1 | Fecha de realización de las operaciones | Fecha en la que se realiza la operación siempre que sea diferente a la fecha de expedición. | Fecha |  |
| BT-9 | + | 0..1 | Fecha de vencimiento del pago | Fecha de vencimiento del pago, calculada de acuerdo con lo dispuesto en el artículo 4 de la Ley 3/2004, de 29 de diciembre, por la que se establecen medidas de lucha contra la morosidad en las operaciones comerciales o en la normativa específica que resulte de aplicación. | Fecha |  |
| BT-ES-2 | + | 0..1 | Fecha efectiva de pago | En aquellos casos en los que la factura ha sido pagada con anterioridad a la fecha de expedición de la factura o en dicha fecha, el emisor podrá consignar la fecha efectiva de pago de la misma. Esta fecha deberá ser necesariamente coincidente o posterior a la fecha de realización de las operaciones. | Fecha | /in:Invoice/cac:PrepaidPayment/ cbc:PaidDate |
| BT-10 | + | 0..n | Referencia del comprador | Un identificador asignado por el comprador para especificar rutas internas de la factura. | Texto |  |
| BG-1 | + | 0..n | NOTA DE FACTURA | Grupo de términos de negocio que contienen notas de texto que son relevantes para la factura. En este grupo podrán incluirse menciones obligatorias en factura de acuerdo con normativa específica, o bien de carácter adicional que el emisor considere conveniente incluir. |  |  |
| BT-21 | ++ | 0..1 | Código de la nota de factura | Código que identifica la tipología de la nota de la factura. Se utilizarán los valores definidos en la UNTDID 4451. En el caso de menciones obligatorias en factura de acuerdo con normativa específica, se debe usar el valor «REG». | Código |  |
| BT-22 | ++ | 1..1 | Nota de factura | Descripción de la nota o mención en factura. | Texto |  |
| BG-2 | + | 1..1 | CONTROL DE PROCESO | Un conjunto de términos de negocio que aportan información sobre el proceso de negocio y reglas aplicables al documento Factura. |  |  |
| BT-23 | ++ | 1..1 | Tipo de proceso de negocio | Adoptará el valor: urn:aeat:names:specification:ubl:schema:profile:B2B | Texto |  |
| BT-24 | ++ | 1..1 | Identificador de especificación | Adoptará el valor: urn:cen.eu:en16931:2026#conformant#urn:aeat.es:spfe:1.0.0:extended | Identificador |  |
| BG-3 | + | 0..n | REFERENCIA DE UNA FACTURA ANTERIOR | Información relativa a una factura o facturas previamente emitidas, con relación con la factura que se expide. |  |  |
| BT-25 | ++ | 1..1 | Serie y número de la factura referenciada | Serie y número que identifican la factura emitida referenciada o sustituida. | Referencia de documento |  |
| BT-26 | ++ | 1..1 | Fecha de expedición de la factura referenciada | Fecha de expedición de la factura referenciada o sustituida. | Fecha |  |
| BG-4 | + | 1..1 | DATOS DEL VENDEDOR | Grupo de términos de negocio que proporcionan información sobre el vendedor. |  |  |
| BT-27 | ++ | 1..1 | Nombre o razón social del vendedor | Nombre y apellidos o razón social del vendedor. | Texto |  |
| BT-31 | ++ | 0..1 | Número de identificación fiscal a efectos de IVA del vendedor | Número de identificación fiscal a efectos de IVA del vendedor, con el prefijo correspondiente a España, según los códigos ISO 3166-1. Será obligatorio consignar un NIF-IVA válido en el caso de que el campo BT-32 no tenga contenido. | Identificador | En este caso /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «VAT» |
| BT-32 | ++ | 0..1 | Identificador fiscal del vendedor | Número de identificación fiscal (NIF) del vendedor. Será obligatorio consignar un NIF válido en el caso de que el campo BT-31 no tenga contenido. | Identificador | En este caso /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «LOC» y el atributo /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID@schemeID tomará el valor «FC» |
| BT-30 | ++ | 0..1 | Identificador de inscripción legal del vendedor | Número de identificación fiscal (NIF) del vendedor. Será obligatorio en los casos en los que venga informado el campo BT-32. | Identificador |  |
| BT-33 | ++ | 0..1 | Información jurídica adicional del vendedor | Información jurídica relevante adicional del vendedor. | Texto |  |
| BG-5 | ++ | 1..1 | DIRECCIÓN POSTAL DEL VENDEDOR | Grupo de términos de negocio que proporciona información de la dirección del vendedor. |  |  |
| BT-35 | +++ | 1..1 | Dirección del vendedor | Se consignará la dirección correspondiente al vendedor, incluyendo tipo de vía, nombre largo de la vía pública, tipo de numeración de la vía pública y número de la dirección o punto kilométrico. | Texto |  |
| BT-37 | +++ | 0..1 | Municipio del vendedor | Se consignará el nombre del municipio. Este campo será obligatorio cuando la dirección postal del vendedor esté en España. | Texto |  |
| BT-38 | +++ | 0..1 | Código de dirección postal del vendedor | Se consignará el código postal correspondiente a la dirección del domicilio. Este campo será obligatorio cuando la dirección postal del vendedor esté en España. | Texto |  |
| BT-39 | +++ | 0..1 | Provincia del vendedor | Se consignará la provincia. Este campo será obligatorio cuando la dirección postal del vendedor esté en España. | Texto |  |
| BT-40 | +++ | 1..1 | Código de país del vendedor | El listado con países válidos se encuentra en la Norma EN ISO 3166-1 «Códigos para la representación de los nombres de los países y sus subdivisiones». | Código |  |
| BG-6 | ++ | 0..1 | CONTACTO DEL VENDEDOR | Un grupo de términos de negocio que ofrecen información de contacto del vendedor. |  |  |
| BT-42 | +++ | 0..1 | Número de teléfono de contacto del Vendedor | Número de teléfono de contacto del vendedor. | Texto |  |
| BT-43 | +++ | 0..1 | Dirección de correo electrónico del vendedor | Dirección de correo electrónico de contacto del vendedor. | Texto |  |
| BG-7 | + | 1..1 | DATOS DEL COMPRADOR | Un conjunto de términos de negocio que ofrecen información sobre el comprador. |  |  |
| BT-44 | ++ | 1..1 | Nombre del comprador | Nombre y apellidos o razón social del comprador. | Texto |  |
| BT-47 | ++ | 0..1 | Identificador fiscal del comprador | Número de identificación fiscal (NIF) del comprador. Será obligatorio consignar un NIF válido en el caso de que el campo BT-48 no tenga contenido. |  | En este caso /in:Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «LOC» y el atributo /in:Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID@schemeID tomará el valor «FC» |
| BT-48 | ++ | 0..1 | Número de identificación fiscal a efectos de IVA del comprador | Número de identificación fiscal a efectos de IVA del vendedor, con el prefijo correspondiente a España, según los códigos ISO 3166-1. Será obligatorio consignar un NIF-IVA válido en el caso de que el campo BT-47 no tenga contenido. | Identificador | En este caso /in:Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «VAT» |
| BG-8 | ++ | 1..1 | DIRECCIÓN POSTAL DEL COMPRADOR | Un grupo de términos de negocio que ofrecen información sobre la dirección postal del comprador. |  |  |
| BT-50 | +++ | 1..1 | Dirección del comprador | Se consignará la dirección correspondiente al comprador, incluyendo tipo de vía, nombre largo de la vía pública, tipo de numeración de la vía pública y número de la dirección o punto kilométrico. | Texto |  |
| BT-52 | +++ | 0..1 | Municipio del comprador | Se consignará el nombre del municipio. Este campo será obligatorio cuando la dirección postal del comprador esté en España. | Texto |  |
| BT-53 | +++ | 0..1 | Código de dirección postal del comprador | Se consignará el código postal correspondiente a la dirección del domicilio. Este campo será obligatorio cuando la dirección postal del comprador esté en España. | Texto |  |
| BT-54 | +++ | 0..1 | Provincia del comprador | Se consignará la provincia. Este campo será obligatorio cuando la dirección postal del comprador esté en España. | Texto |  |
| BT-55 | +++ | 1..1 | Código de país del comprador | El listado con países válidos se encuentra en la Norma EN ISO 3166-1 «Códigos para la representación de los nombres de los países y sus subdivisiones». | Código |  |
| BG-9 | ++ | 0..1 | CONTACTO DEL COMPRADOR | Un grupo de términos de negocio que ofrecen información de contacto relevante del comprador. |  |  |
| BT-57 | +++ | 0..1 | Teléfono de contacto del comprador | Número de teléfono de contacto del comprador. | Texto |  |
| BT-58 | +++ | 0..1 | Dirección de correo electrónico del comprador | Dirección de correo electrónico de contacto del comprador. | Texto |  |
| BG-ES-1 | + | 0..n | DATOS DEL TERCERO | Información relativa a un tercero. Este grupo de términos de negocio será obligatorio en el caso del tercero que expide materialmente la factura en lugar del obligado a expedirla, de acuerdo con el artículo 5 del Reglamento por el que se regulan las obligaciones de facturación, aprobado por Real Decreto 1619/2012, de 30 de noviembre. |  | /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty |
| BT-ES-3 | ++ | 1..1 | Nombre o razón social del tercero | Nombre completo o razón social del tercero informado. | Texto | /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName |
| BT-ES-4 | ++ | 1..1 | NIF del tercero | Número de identificación fiscal (NIF) del tercero informado. | Identificador | /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID En caso de NIF además: /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «LOC» y el atributo /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID@schemeID tomará el valor «FC» En caso contrario /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID tomará el valor «VAT» |
| BT-ES-5 | ++ | 1..1 | Tipología de tercero | Código que define el tipo de tercero informado. En el caso de un tercero que expide materialmente la factura en lugar del vendedor, se debe usar obligatoriamente el código «FacturaciónPorTercero». | Código | /in:Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cbc:ServiceTypeCode |
| BG-14 | + | 0..1 | PERIODO DE LA FACTURA RECAPITULATIVA | Grupo de términos de negocio que sirven para indicar la fecha de inicio y fin del periodo abarcado por la factura expedida, en el caso de que se trate de una factura recapitulativa. |  |  |
| BT-73 | ++ | 0..1 | Fecha de inicio del período de facturación | Fecha inicial del plazo de la factura recapitulativa. | Fecha |  |
| BT-74 | ++ | 0..1 | Fecha de fin del período de facturación | Fecha final del plazo de la factura recapitulativa. | Fecha |  |
| BG-20 | + | 0..n | MINORACIONES A NIVEL DE DOCUMENTO | Un grupo de términos de negocio que ofrecen información sobre minoraciones aplicables a la factura en su totalidad. |  | Su uso implica que todos los elementos /in:Invoice/cac:AllowanceCharge/cbc:ChargeIndicator del grupo deben tener el valor «false» |
| BT-92 | ++ | 1..1 | Importe de la minoración a nivel de documento | Importe de las minoraciones aplicables a la factura, IVA excluido. | Importe |  |
| BT-95 | ++ | 1..1 | Código de categoría de IVA de la minoración a nivel de documento | Identificación codificada de la categoría de IVA aplicable a la minoración definida a nivel de documento. Se utilizarán los valores definidos en la UNTDID 5305, incluidos en la lista L4. | Código (L4) | Implica que /in:Invoice/cac:AllowanceCharge/cac:TaxCategory/cac:TaxScheme/cbc:ID tome el valor «VAT» |
| BT-96 | ++ | 0..1 | Tipo de IVA de la minoración a nivel de documento | Tipo de IVA representado como porcentaje que es aplicable a la minoración definida a nivel de documento. | Porcentaje |  |
| BT-97 | ++ | 1..1 | Razón de la minoración a nivel de documento | La razón de la minoración definida a nivel de documento, expresada como texto. | Texto |  |
| BG-21 | + | 0..n | CARGOS A NIVEL DE DOCUMENTO | Grupo de términos de negocio que proporcionan información sobre cargos e impuestos distintos al IVA que se aplican a la factura en su conjunto. |  | Su uso implica que todos los elementos /in:Invoice/cac:AllowanceCharge/cbc:ChargeIndicator del grupo deben tener el valor «true» |
| BT-99 | ++ | 1..1 | Importe del cargo a nivel de documento | Importe del cargo aplicable a la factura, sin IVA. | Importe |  |
| BT-102 | ++ | 1..1 | Código de categoría de IVA del cargo a nivel de documento | Identificación codificada de la categoría de IVA aplicable al cargo definido a nivel de factura. Se utilizarán los valores definidos en la UNTDID 5305, incluidos en la lista L4. | Código (L4) | Implica que /in:Invoice/cac:AllowanceCharge/cac:TaxCategory/cac:TaxScheme/cbc:ID tome el valor «VAT» |
| BT-103 | ++ | 0..1 | Tipo de IVA del cargo a nivel de documento | Tipo de IVA representado como porcentaje que es aplicable al cargo definido a nivel de factura. | Porcentaje |  |
| BT-104 | ++ | 1..1 | Razón de cargo a nivel de documento | La razón del cargo definido a nivel de factura, expresado como texto. | Texto |  |
| BG-ES-2 | ++ | 0..n | DETALLE DEL IMPUESTO O TASA A NIVEL DE DOCUMENTO | Grupo de términos de negocio que proporcionan información sobre tasas o impuestos distintos al IVA que aplican a la factura en su conjunto. |  |  |
| BT-ES-6 | +++ | 0..1 | Base del impuesto o tasa | Base imponible del impuesto o tasa correspondiente. | Importe | /in:Invoice/cac:Invoice/cac:AllowanceCharge/cac:TaxTotal/ cac:TaxSubTotal/cbc:TaxableAmount |
| BT-ES-7 | +++ | 0..1 | Tipo del impuesto o tasa | Tipo del impuesto o tasa representado como porcentaje, que es aplicable a la base del impuesto o tasa correspondiente. | Porcentaje | /in:Invoice/cac:Invoice/cac:AllowanceCharge/cac:TaxTotal/cac:TaxSubTotal/cac:TaxCategory/cbc:Percent |
| BT-ES-8 | +++ | 1..1 | Cuota del impuesto o tasa | Resultado de aplicar a la base del impuesto o tasa el tipo correspondiente. | Importe | El mismo importe debe consignarse en dos rutas distintas: /in:Invoice/cac:Invoice/cac:AllowanceCharge/cac:TaxTotal/ /cbc:TaxAmount Y también en: /in:Invoice/cac:Invoice/cac:AllowanceCharge/cac:TaxTotal/ cac:TaxSubTotal/cbc:TaxAmount |
| BT-ES-9 | +++ | 1..1 | Código del tipo de impuesto incluido como cargo a nivel de documento | Tipo de impuesto (no IVA) incluido como cargo a nivel de documento, expresado como código. | Código (L9) | /in:Invoice/cac:Invoice/cac:AllowanceCharge/ cac:TaxTotal/ cac:TaxSubTotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode |
| BG-22 | + | 1..1 | TOTALES A NIVEL DE DOCUMENTO | Grupo de términos de negocio que proporcionan los totales monetarios de la factura. |  |  |
| BT-106 | ++ | 1..1 | Suma del importe neto de las líneas de factura | Suma de todos los importes netos de las líneas de la factura. | Importe |  |
| BT-107 | ++ | 0..1 | Suma de minoraciones a nivel de documento | Suma de todas las minoraciones definidas a nivel de documento de la factura. | Importe |  |
| BT-108 | ++ | 0..1 | Suma de cargos a nivel de documento | Suma de todos los cargos definidos a nivel de documento de la factura. | Importe |  |
| BT-109 | ++ | 1..1 | Importe total de la factura sin IVA | Importe total de la factura antes de aplicar el IVA. | Importe |  |
| BT-110 | ++ | 1..1 | Cuota total del IVA de la factura | Cuota total del IVA para la factura. | Importe |  |
| BT-111 | ++ | 0..1 | Cuota total del IVA de la factura en la moneda contable | Cuando la moneda de la factura no sea el euro, la cuota total del IVA de la factura deberá expresarse adicionalmente en euros. En el caso de que en la misma factura se repercutan cantidades en concepto de recargo de equivalencia, se adicionarán las cuotas del recargo en euros. | Importe |  |
| BT-112 | ++ | 1..1 | Importe total de la factura con IVA | Importe total de la factura después de aplicar el IVA. | Importe |  |
| BT-113 | ++ | 0..1 | Importe pagado | La suma de los importes que han sido pagados por adelantado. Este campo no debe ser utilizado en el caso de pagos anticipados que hayan supuesto el devengo del IVA previsto en el artículo 75.Dos de la Ley 37/1992, de 28 de diciembre. | Importe |  |
| BT-114 | ++ | 0..1 | Importe de redondeo | El importe a añadir o restar al total de la factura para redondear el importe a pagar. | Importe |  |
| BT-115 | ++ | 1..1 | Total a pagar | Este importe es igual al importe total de la factura con IVA menos los importes que han sido pagados por adelantado, junto con los importes correspondientes a los conceptos BT-179 y los importes redondeados, BT-114. El importe es cero en el caso de una factura pagada en su totalidad. El importe puede ser negativo; en ese caso, el vendedor debe dicho importe al comprador. | Importe |  |
| BG-34 | ++ | 0..n | CARGOS EN NOMBRE DE UN TERCERO | Importes a favor de un tercero distinto del vendedor, a pagar por el comprador. |  |  |
| BT-179 | +++ | 1..1 | Importe del cargo cobrado en nombre de un tercero | Se consignarán suplidos y/o cantidades repercutidas o exigidas en nombre de un tercero, sin reflejo en la base imponible de la operación. | Importe |  |
| BT-180 | +++ | 1..1 | Descripción del cargo en nombre de un tercero | Descripción del motivo del cargo en nombre de un tercero. | Texto |  |
| BT-ES-10 | +++ | 1..1 | Identificación del cargo en nombre de un tercero | Código de identificación del cargo en nombre de un tercero. Código obligatorio, usar «SUPL». | Código (L7) | /in:Invoice/cac:CollectionInvoiceLine/cbc:ID |
| BG-34 | ++ | 0..n | IMPUESTOS Y TASAS | En caso de que se incluyan cargos en nombre de un tercero correspondientes a impuestos y tasas, en este grupo de términos de negocio se incluirá la información relativa a su cálculo que resulte obligatoria. |  |  |
| BT-179 | +++ | 1..1 | Suma de las cuotas de los impuestos o tasas | Suma de las cuotas de los impuestos y tasas incluidos como cargos en nombre de un tercero. | Importe |  |
| BT-180 | +++ | 1..1 | Denominación del impuesto o tasa | Denominación del Impuesto o tasa. | Texto |  |
| BT-ES-11 | +++ | 1..1 | Identificación del impuesto o tasa | Código de identificación del impuesto o tasa. Código obligatorio, usar «IEDMT» en el caso del Impuesto Especial sobre Determinados medios de transporte. En el resto de casos, se consignará «OTROS». | Código (L7) | /in:Invoice/cac:CollectionInvoiceLine/cbc:ID |
| BG-ES- 3 | +++ | 0..n | DESGLOSE IMPUESTOS Y TASAS | Grupo de términos de negocio que se emplean para detallar el cálculo de los impuestos y tasas incluidos como cargos en nombre de un tercero. |  | Su uso implica que la ruta /in:Invoice/cac:CollectionInvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID tomará el valor «VAT», y la ruta /in:Invoice/cac:CollectionInvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID adoptará el valor «S» |
| BT-ES-12 | ++++ | 0..1 | Base del impuesto o tasa | Importe correspondiente a la base de cálculo del impuesto o tasa incluido como cargo en nombre de un tercero. | Importe | /in:Invoice/cac:CollectionInvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount |
| BT-ES-13 | ++++ | 0..1 | Tipo del impuesto o tasa | Tipo aplicable para el cálculo del impuesto o tasa incluido como cargo en nombre de un tercero. | Porcentaje | /in:Invoice/cac:CollectionInvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent |
| BT-ES-14 | ++++ | 1..1 | Cuota total del impuesto o tasa | Cuota resultante de aplicar a la base del impuesto o tasa el tipo correspondiente. | Importe | /in:Invoice/cac:CollectionInvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount |
| BG-34 | ++ | 0..n | MINORACIONES EN NOMBRE DE UN TERCERO | Minoraciones, no parte de la factura, que deben minorar el total a pagar, como la devolución de un suplido. |  |  |
| BT-179 | +++ | 1..1 | Importe de la minoración en nombre de un tercero | Se consignarán minoraciones de las cantidades exigidas en nombre de un tercero, sin reflejo en la base imponible de la operación. | Importe |  |
| BT-180 | +++ | 1..1 | Descripción de la minoración en nombre de un tercero | Descripción del motivo de la minoración en nombre de un tercero. | Texto |  |
| BT-ES-15 | +++ | 1..1 | Identificación de la minoración en nombre de un tercero | Código de identificación de la minoración en nombre de un tercero. Código obligatorio, usar «MINO». | Código (L7) | /in:Invoice/cac:CollectionInvoiceLine/cbc:ID |
| BG-34 | ++ | 0..1 | RETENCIONES | Grupo de términos de negocio que proporcionan información relativa a las retenciones practicadas en la factura. |  |  |
| BT-179 | +++ | 1..1 | Suma de retenciones | Sumatorio de todas las retenciones practicadas en factura. | Importe |  |
| BT-180 | +++ | 1..1 | Descripción de la retención | Descripción del motivo de la retención. | Texto |  |
| BT-ES-16 | +++ | 1..1 | Identificación de retención | Código de identificación de la retención en factura. Código obligatorio, usar «RETE». | Código (L7) | /in:Invoice/cac:CollectionInvoiceLine/cbc:ID |
| BT-ES-17 | +++ | 1..1 | Suma de retenciones | Sumatorio de todas las retenciones practicadas en factura. | Importe | /in:Invoice/cac:WithholdingTaxTotal/ cbc:TaxAmount |
| BG-ES-4 | +++ | 0..n | RETENCIÓN APLICADA | Grupo de términos de negocio que proporcionan información relativa a una retención practicada en la factura. |  | Su uso implica que la ruta /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID tome el valor «S», y la ruta /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID adopte el valor «WTH» |
| BT-ES-18 | ++++ | 1..1 | Base imponible retención | Base de cálculo sobre la que se aplicará el porcentaje de retención para calcular la retención correspondiente. | Importe | /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cbc:TaxableAmount |
| BT-ES-19 | ++++ | 1..1 | Total retención | Resultado de aplicar a la Base imponible de la retención, el porcentaje de retención correspondiente. | Importe | /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cbc:TaxAmount |
| BT-ES-20 | ++++ | 1..1 | Porcentaje | Porcentaje de retención aplicable. | Porcentaje | /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent |
| BT-ES-21 | ++++ | 1..1 | Concepto | Información relativa a la retención practicada. Se usarán las claves contenidas en la tabla L5. | Código (L5) | /in:Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode |
| BG-25 | + | 1..n | LÍNEA DE FACTURA | Un grupo de términos de negocio que proporcionan información a nivel de líneas individuales de la factura. |  |  |
| BT-126 | ++ | 1..1 | Identificador de línea de factura | Un identificador único de una línea individual de la factura. | Identificador |  |
| BT-129 | ++ | 1..1 | Cantidad facturada | La cantidad de artículos (bienes o servicios) que se cargan en la línea de factura. | Cantidad |  |
| BT-130 | ++ | 1..1 | Código de la unidad de medida de la cantidad facturada | La unidad de medida aplicable a la cantidad facturada. La unidad de medida debe elegirse de las listas de la Recomendación UN/ECE N.º 20 «Códigos de Unidades de Medida utilizados en el comercio internacional» y la Recomendación UN/ECE N.º 21 «Tipos de Pasajeros, tipos de carga, embalajes y materiales de embalaje (con códigos complementarios para los nombres de embalajes)». | Código |  |
| BT-131 | ++ | 1..1 | Importe neto a nivel de línea de factura | El importe total a nivel de la línea de factura. En las operaciones acogidas al régimen especial de grupo de entidades, nivel avanzado, se informará del importe total de la contraprestación. | Importe |  |
| BG-27 | ++ | 0..n | MINORACIONES DE LÍNEA DE FACTURA | Grupo de elementos de negocio que proporciona información sobre minoraciones aplicables a una línea de factura individual. |  | Su uso implica que todos los elementos /in:Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:ChargeIndicator del grupo deben tener el valor «false» |
| BT-136 | +++ | 1..1 | Importe de la minoración de línea de factura | Importe de la minoración, sin IVA. | Importe |  |
| BT-139 | +++ | 1..1 | Razón de la minoración de línea de factura | La razón de la minoración de línea de factura, expresada como texto. | Texto |  |
| BG-28 | ++ | 0..n | CARGOS DE LÍNEA DE FACTURA | Grupo de elementos de negocio que proporciona información sobre cargos, tasas e impuestos distintos del IVA aplicables a una línea individual de la factura. |  | Su uso implica que todos los elementos /in:Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:ChargeIndicator del grupo deben tener el valor «true» |
| BT-141 | +++ | 1..1 | Importe del cargo de línea de factura | Importe del cargo, sin IVA. | Importe |  |
| BT-142 | +++ | 0..1 | Base del importe de cargo de línea de factura | El importe base que puede utilizarse, junto con el porcentaje de cargo, tasa o impuesto de la línea de factura, para calcular el importe del cargo o del impuesto correspondiente a dicha línea de factura. | Importe |  |
| BT-143 | +++ | 0..1 | Tipo aplicable a la base del cargo de línea de factura | Porcentaje que puede utilizarse, junto con la base del importe, para calcular el importe del cargo, tasa o del impuesto correspondiente a dicha línea de factura. | Porcentaje |  |
| BT-ES-22 | +++ | 1..1 | Código del tipo de impuesto incluido como cargo de línea de factura | Tipo de impuesto (no IVA) o tasa incluido como cargo, expresado como código. | Código (L9) | /in:Invoice/cac:InvoiceLine/cac:AllowanceCharge/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode |
| BT-144 | +++ | 1..1 | Razón del cargo de línea de factura | La razón del cargo de línea de factura, expresada como texto. | Texto |  |
| BG-29 | ++ | 1..1 | DETALLES DEL PRECIO | Grupo de términos de negocio que proporcionan información sobre el precio aplicado a los bienes y servicios facturados en la línea de factura. |  |  |
| BT-146 | +++ | 1..1 | Precio neto del artículo | Precio de un artículo, excluido el IVA, una vez minorado por el descuento sobre el precio del artículo. | Importe de precio unitario |  |
| BT-149 | ++ | 0..1 | Cantidad del precio base por artículo | Número de unidades de artículos a las que se aplica el precio. | Cantidad |  |
| BG-30 | ++ | 1..1 | INFORMACIÓN DEL IVA A NIVEL DE LÍNEA | Un grupo de términos de negocio que ofrecen información sobre el IVA aplicable a los bienes y servicios a nivel de línea de la factura. |  | Su uso implica que la ruta /in:Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:ID tomará el valor «VAT» |
| BT-151 | +++ | 1..1 | Código de categoría de IVA del artículo facturado | Identificación codificada de la categoría de IVA correspondiente al artículo facturado. Se utilizarán los valores definidos en la UNTDID 5305, incluidos en la lista L4. | Código (L4) |  |
| BT-152 | +++ | 0..1 | Tipo impositivo de IVA del artículo facturado | El tipo impositivo, representado como un porcentaje aplicable al artículo facturado. | Porcentaje |  |
| BT-195 | +++ | 0..1 | Código de razón de exención | Lista de códigos creada y mantenida por el Mecanismo «Conectar Europa» (CEF, Connecting Europe Facility). Lista CEF-VATEX. Solo podrán adoptar valores VATEX-EU o VATEX-ES. | Código |  |
| BG-31 | ++ | 1..1 | INFORMACIÓN DE ARTÍCULO | Un grupo de términos de negocio que ofrecen información sobre los bienes y servicios facturados. |  |  |
| BT-153 | +++ | 1..1 | Nombre de artículo | Nombre del artículo. | Texto |  |
| BT-154 | +++ | 0..1 | Descripción de artículo | Permite la descripción del artículo y sus prestaciones en mayor detalle que el campo nombre de artículo. | Texto |  |
| BG-32 | +++ | 0..n | INFORMACIÓN ADICIONAL A NIVEL DE LÍNEA | Un grupo de términos de negocio que ofrece información adicional de inclusión obligatoria en factura de acuerdo con normativa específica, así como información adicional que el emisor considere conveniente introducir. |  |  |
| BT-160 | +++ | 1..1 | Código de la propiedad - Información adicional a nivel de línea | Código de identificación de la información adicional a nivel de línea. Adoptará el valor fijo «INFO». | Código (L8) |  |
| BT-161 | +++ | 1..1 | Información adicional a nivel de línea | Descripción de la información adicional a nivel de línea. | Texto |  |
| BG-32 | +++ | 0..1 | REFERENCIA CATASTRAL | Un grupo de términos de negocio que ofrece información relativa al inmueble sobre el que recae la operación facturada. |  |  |
| BT-160 | ++++ | 1..1 | Código de la propiedad - Referencia catastral | Código de identificación de la referencia catastral. Adoptará el valor fijo «RCAT». | Código (L8) |  |
| BT-161 | +++ | 1..1 | Referencia catastral | Referencia catastral del inmueble. | Texto |  |
| BT-ES-23 | +++ | 1..1 | Situación del inmueble | Identificador que especifica la situación del inmueble. | Código (L6) | /in:invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty/cbc:ValueQualifier |
| BG-32 | +++ | 1..2 | CLAVE DE RÉGIMEN | Un grupo de términos de negocio que ofrece información relativa al régimen aplicable a la operación facturada. |  |  |
| BT-160 | ++++ | 1..1 | Código de la propiedad - Régimen | Código de identificación de la clave de régimen. Adoptará el valor fijo «REGI». | Código (L8) |  |
| BT-161 | ++++ | 1..1 | Código de clave de régimen | Se consignará la clave de régimen correspondiente a la operación, según las listas L3A, L3B y L3C. | Código (L3A/L3B/L3C) |  |
| BT-ES-24 | ++++ | 1..1 | Tipo de impuesto nacional | Identificador de la sujeción de la operación al IVA, IGIC y al IPSI. | Código-Calificador (L3A/L3B/L3C) | /in:invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty/cbc:ValueQualifier |
| BG-23 | + | 1..n | DESGLOSE DEL IVA | Grupo de términos de negocio que proporcionan información sobre el desglose del IVA en diferentes categorías, tipos y razones de exención. También proporcionará información sobre el desglose del recargo de equivalencia, en su caso. |  | Su uso implica que la ruta /in:Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID tomará el valor «VAT» |
| BT-116 | ++ | 1..1 | Base imponible por categoría de IVA | Suma de todas las bases imponibles a las que son de aplicación un mismo código de categoría de IVA. En las operaciones acogidas al régimen especial de grupo de entidades, nivel avanzado, se informará de la base imponible a coste. | Importe |  |
| BT-117 | ++ | 1..1 | Cuota tributaria por categoría de IVA | La cuota de IVA por categoría. En el caso del recargo de equivalencia, se informará de la cuota de dicho recargo. | Importe |  |
| BT-118 | ++ | 1..1 | Código de cuota tributaria por categoría de IVA | Identificación codificada de la categoría de IVA correspondiente a la cuota tributaria. Se utilizarán los valores definidos en la UNTDID 5305, incluidos en la lista L4. | Código (L4) |  |
| BT-119 | ++ | 1..1 | Tipo de IVA por categoría | Tipo de IVA, representado en forma de porcentaje, aplicable a la categoría de IVA que corresponde. En el caso del recargo de equivalencia, se informará del tipo del recargo de equivalencia aplicable. | Porcentaje |  |
| BT-120 | ++ | 0..1 | Razón de exención | Enunciado que explica la razón por la que un importe está exento de IVA o por qué el IVA no se aplica. | Texto |  |
| BT-121 | ++ | 0..1 | Código de razón de exención | Lista de códigos creada y mantenida por el Mecanismo «Conectar Europa» (CEF, Connecting Europe Facility). Lista CEF-VATEX. Solo podrán adoptar valores VATEX-EU o VATEX-ES. | Código |  |
| BG-33 | + | 0..n | Condiciones de pago | Este grupo recoge los datos relativos a las condiciones de pago a aplicar a la cantidad a pagar. |  |  |
| BT-20 | ++ | 0..1 | Descripción de las condiciones de pago | Descripción de las condiciones de pago a aplicar a la cantidad a pagar. | Texto |  |
| BG-16 | + | 0..1 | INSTRUCCIONES DE PAGO | Un grupo de términos de negocio que ofrecen información acerca del pago. |  |  |
| BT-81 | ++ | 1..1 | Código de tipo de medios de pago | Los medios, expresados como un código, a través de los que el pago va a liquidarse o se ha liquidado. Deben utilizarse obligatoriamente los códigos de la lista UNTDID 4461. | Código |  |
| BG-17 | ++ | 0..n | TRANSFERENCIA BANCARIA | Un grupo de términos de negocio utilizados para especificar pagos por transferencia. |  |  |
| BT-84 | +++ | 1..1 | Identificador de la cuenta de pago | Identificador único de la cuenta financiera de pago, puesta a disposición por un proveedor de servicios de pago, a la que debería efectuarse el pago. Con carácter general, se tratará de un código IBAN. | Identificador |  |
| BG-24 | + | 0..1 | QR FISCAL | Grupo de términos de negocio que proporcionan información obligatoria relativa al código QR previsto en el artículo 6.5 del Real Decreto 1619/2012, de 30 de noviembre, o en la normativa foral que resulte de aplicación. |  |  |
| BT-122 | ++ | 1..1 | Referencia de documento justificativo - ID | Valor obligatorio: usar «QR». | Código (L10) |  |
| BT-123 | ++ | 0..1 | Descripción de documento justificativo - Tipo de QR | Valor obligatorio: usar «VERIFACTU» o «TICKETBAI», según corresponda conforme normativa aplicable. | Texto |  |
| BT-ES-25 | ++ | 1..1 | Localización de documento externo - Descripción | Se debe consignar la URL correspondiente al QR VERI*FACTU o TICKETBAI, según corresponda conforme normativa aplicable. | Texto | /in:Invoice/cac:AdditionalDocumentReference/cbc:UUID |
| BG-24 | + | 0..n | AUTORIZACIÓN DE FACTURACIÓN | Grupo de términos de negocio que proporcionan información sobre la autorización concedida al obligado a expedir factura, de acuerdo con lo dispuesto en el Real Decreto 1619/2012, de 30 de noviembre, o con el Real Decreto 1624/1992, de 29 de diciembre, por el Departamento de Gestión Tributaria de la Agencia Tributaria o por la Administración Tributaria Canaria; o, en su caso, por la Diputación Foral correspondiente, según la normativa foral que resulte de aplicación. |  |  |
| BT-122 | ++ | 1..1 | Referencia de documento justificativo - ID | Valor obligatorio: usar «AUT». | Código (L10) |  |
| BT-123 | ++ | 0..1 | Descripción de documento justificativo - Descripción autorización | Texto descriptivo de la autorización concedida. | Texto |  |
| BT-ES-26 | ++ | 1..1 | Referencia de documento justificativo - N.º referencia autorización | Número de referencia de la autorización concedida. | Texto | /in:Invoice/cac:AdditionalDocumentReference/cbc:UUID |
| BG-24 | + | 0..1 | TIPO DE FACTURA RECTIFICATIVA | Este grupo recoge los datos relativos al tipo de factura rectificativa expedida. |  |  |
| BT-122 | ++ | 1..1 | Referencia de documento justificativo - ID | Valor fijo que permite identificar el tipo de factura rectificativa: usar «RECT:TIPO». | Código (L10) |  |
| BT-123 | ++ | 0..1 | Descripción del tipo de factura rectificativa | Se especificará el tipo de factura rectificativa. | Texto |  |
| BT-ES-27 | ++ | 1..1 | Código de tipo de factura rectificativa | Las facturas rectificativas (código de tipo de factura 384 y 471) adoptarán los valores definidos en la lista L2.A. | Código (L2.A) | /in:Invoice/cac:AdditionalDocumentReference/cbc:DocumentTypeCode |
| BG-24 | + | 0..1 | MODALIDAD DE FACTURA RECTIFICATIVA | Este grupo recoge los datos relativos a la modalidad de rectificación utilizada. |  |  |
| BT-122 | ++ | 1..1 | Referencia de documento justificativo - ID | Valor fijo que permite identificar la modalidad de factura rectificativa: usar «RECT:MODALIDAD». | Código (L10) |  |
| BT-123 | ++ | 0..1 | Descripción de la modalidad de factura rectificativa | Descripción que especifica la modalidad de la rectificación empleada. | Texto |  |
| BT-ES-28 | ++ | 1..1 | Código de modalidad de factura rectificativa | Código que especifica la modalidad de rectificación empleada. Adoptarán los valores definidos en la lista L2.B. | Código (L2.B) | /in:Invoice/cac:AdditionalDocumentReference/cbc:DocumentTypeCode |
| BG-24 | + | 0..5 | IMPORTES RECTIFICADOS | Este grupo recoge los importes rectificados respecto de la factura original, en los casos en los que se proceda a la rectificación por sustitución de la factura original, y se opte por la emisión de una única factura con los importes correctos, incluyendo aquí información sobre los importes rectificados. |  |  |
| BT-122 | ++ | 1..1 | Referencia de documento justificativo - ID | Valor fijo que permite identificar los importes rectificados: usar «RECT:IMPORTES». | Código (L10) |  |
| BT-123 | ++ | 1..1 | Importe rectificado | Importe de la factura rectificada. En función del código que se informe, se referirá a la base imponible, a la cuota de IVA o a la cuota del recargo de equivalencia. | Texto |  |
| BT-ES-29 | ++ | 1..1 | Código de los importes rectificados | Código que especifica el importe rectificado. Adoptarán los valores definidos en la lista L2.C. | Código (L2.C) | /in:Invoice/cac:AdditionalDocumentReference/cbc:DocumentTypeCode |
| FACTURA ELECTRÓNICA O COPIA FIEL– Mensaje de anulación | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode: CANCELINVOICE |
| --- | --- |
| Nivel | Cardinalidad | Término de negocio (BT) | Descripción | Tipo semántico de dato | Ruta UBL |
| --- | --- | --- | --- | --- | --- |
| + | 1..1 | Fecha de la anulación. | Fecha en la que se produce la anulación de la factura. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveDate |
| + | 1..n | FACTURA ANULADA | Datos de la factura que se anula. |  | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference |
| ++ | 1..1 | Número de factura (ID) | Serie y número de la factura anulada. | Texto | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference/cbc:ID |
| ++ | 1..1 | Fecha de expedición de la factura | Fecha de expedición de la factura anulada. | Fecha | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference/cbc:IssueDate |
| ++ | 1..1 | DATOS DEL VENDEDOR | Grupo de términos de negocio que proporcionan información sobre el vendedor identificado en la factura. |  | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference/cac:IssuerParty |
| +++ | 1..1 | NIF del vendedor | Número de identificación fiscal (NIF) del vendedor en la factura anulada. | Identificador | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID |
| +++ | 1..1 | Nombre o razón social del vendedor | Nombre y apellidos o razón social del vendedor. | Texto | ApplicationResponse/cac:DocumentResponse/cac:Response/cac:DocumentReference/cac:IssuerParty/cac:PartyTaxScheme/cac:PartyLegalEntity/cbc:RegistrationName |

Claves y valores permitidos en campos de tipo código:

Se definen a continuación los valores permitidos en los campos con tipo semántico de dato de tipo código en los que se ha indicado expresamente que se definirán los valores en una lista (L). En los restantes campos de tipo código, en la columna descripción, se indica la forma de definición de los valores admitidos.

L1 – Tipo de factura

| Valores | Descripción |
| --- | --- |
| 380 | Factura (artículo 6, 7.2 y 7.3 del RD 1619/2012). |
| 384 | Factura rectificativa. |
| 388 | Factura emitida en sustitución de facturas simplificadas. |
| 389 | Factura emitida por el destinatario. |
| 471 | Factura rectificativa emitida por el destinatario. |

L2.A – Tipo de factura rectificativa

| Valores | Descripción |
| --- | --- |
| R1 | Factura Rectificativa (Error fundado en derecho y artículo 80 Uno Dos y Seis LIVA). |
| R2 | Factura Rectificativa (artículo 80.3). |
| R3 | Factura Rectificativa (artículo 80.4). |
| R4 | Factura Rectificativa (Resto). |

L2.B – Modalidad de factura rectificativa

| Valores | Descripción |
| --- | --- |
| I | Rectificativa por diferencias. |
| S | Rectificativa por sustitución. |

L2.C – Importes rectificados

| Valores | Descripción |
| --- | --- |
| Base | Base imponible de la factura rectificada. |
| Cuota | Cuota repercutida de la factura rectificada. |
| CuotaRecargo | Cuota recargo de equivalencia de la factura rectificada. |

L3A – Clave de régimen-IVA

| CALIFICADOR | IVA |
| --- | --- |
| Valores | Descripción de la clave de régimen para desgloses donde el impuesto de aplicación es el IVA |
| --- | --- |
| 01 | Operación en régimen general y no incluidas en otras claves. |
| 02 | Exportación. |
| 03 | Operaciones a las que se aplique el régimen especial de bienes usados, objetos de arte, antigüedades y objetos de colección. |
| 04 | Régimen especial del oro de inversión. |
| 05 | Régimen especial de las agencias de viajes. |
| 06 | Régimen especial grupo de entidades en IVA (Nivel Avanzado). |
| 07 | Régimen especial del criterio de caja. |
| 08 | Operaciones sujetas al IPSI / IGIC (Impuesto sobre la Producción, los Servicios y la Importación / Impuesto General Indirecto Canario). |
| 09 | Facturación de las prestaciones de servicios de agencias de viaje que actúan como mediadoras en nombre y por cuenta ajena (D.A.4.ª RD1619/2012). |
| 11 | Operaciones de arrendamiento de local de negocio. |
| 14 | Factura con IVA pendiente de devengo en certificaciones de obra cuyo destinatario sea una Administración Pública. |
| 15 | Factura con IVA pendiente de devengo en operaciones de tracto sucesivo. |

L3B – Clave de régimen-IGIC

| CALIFICADOR | IGIC |
| --- | --- |
| Valores | Descripción de la clave de régimen para desgloses donde el impuesto de aplicación es el IGIC |
| --- | --- |
| 01 | Operación en régimen general y no incluidas en otras claves. |
| 02 | Exportación. |
| 03 | Operaciones a las que se aplique el régimen especial de bienes usados, objetos de arte, antigüedades y objetos de colección. |
| 04 | Régimen especial del oro de inversión. |
| 05 | Régimen especial de las agencias de viajes. |
| 06 | Régimen especial grupo de entidades en IGIC (Nivel Avanzado). |
| 07 | Régimen especial del criterio de caja. |
| 08 | Operaciones sujetas al IPSI / IVA (Impuesto sobre la Producción, los Servicios y la Importación / Impuesto sobre el Valor Añadido). |
| 09 | Facturación de las prestaciones de servicios de agencias de viaje que actúan como mediadoras en nombre y por cuenta ajena (D.A.4.ª RD1619/2012). |
| 11 | Operaciones de arrendamiento de local de negocio. |
| 14 | Factura con IGIC pendiente de devengo en certificaciones de obra cuyo destinatario sea una Administración Pública. |
| 15 | Factura con IGIC pendiente de devengo en operaciones de tracto sucesivo. |
| 17 | Régimen especial de comerciante minorista. |
| 18 | Régimen especial del pequeño empresario o profesional. |
| 19 | Operaciones interiores exentas por aplicación artículo 25 Ley 19/1994. |

L3C – Clave de régimen-IPSI

| CALIFICADOR | IPSI |
| --- | --- |
| Valores | Descripción de la clave de régimen para desgloses donde el impuesto de aplicación es el IPSI |
| --- | --- |
| 01 | Operación en régimen general y no incluidas en otras claves. |
| 08 | Operaciones sujetas al IGIC / IVA (Impuesto sobre la Producción, los Servicios y la Importación / Impuesto sobre el Valor Añadido). |
| 11 | Operaciones de arrendamiento de local de negocio. |
| 19 | Operaciones interiores exentas. |
| 20 | Régimen simplificado. |

L4 – Código de tipo de operación

| Valores | Descripción |
| --- | --- |
| S | Operaciones en régimen general. |
| Z | Bienes con tipo impositivo 0 %. |
| E | Exento de IVA. |
| AE | Inversión del sujeto pasivo. |
| O | Operación no sujeta a IVA. |
| G | Exportación. |
| L | Operación sujeta al IGIC. |
| M | Operación sujeta al IPSI. |
| N | Regímenes nacionales de IVA (régimen especial de grupo de entidades, nivel avanzado, y régimen especial del recargo de equivalencia). |
| D | Régimen especial de agencias de viajes. |
| F | Régimen especial de bienes usados, objetos de arte antigüedades, y objetos de colección. |

L5 – Tipo de retención

| Valores | Descripción |
| --- | --- |
| 01 | Artículo 75.1.c) Inciso primero RIRPF – Rendimiento de actividades profesionales. |
| 02 | Artículo 75.1.c) Inciso segundo RIRPF – Rendimiento de actividades agrícolas y ganaderas. |
| 03 | Artículo 75.1.c) Inciso tercero RIRPF – Rendimiento de actividades forestales. |
| 04 | Artículo 75.1.c) Inciso cuarto RIRPF – Rendimientos de actividades empresariales del artículo 95.6.2.º RIRPF. |
| 05 | Artículo 75.1. d) Inciso segundo RIRPF – Ganancias patrimoniales de los aprovechamientos forestales de los vecinos en montes públicos. |
| 06 | Artículo 75.2.a) RIRPF – Rendimientos de arrendamientos o subarrendamientos de locales urbanos. |
| 07 | Artículo 75.2.b) RIRPF - Rendimientos procedentes de la propiedad intelectual, industrial, de la prestación de asistencia técnica, del arrendamiento de bienes muebles, negocios o minas, del subarrendamiento sobre los bienes anteriores y los procedentes de la cesión del derecho a la explotación del derecho de imagen. |
| 08 | Artículo 60.1.c) RIS - Las contraprestaciones obtenidas como consecuencia de la atribución de cargos de administrador o consejero en otras sociedades. |
| 09 | Artículo 60.1.d) RIS - Las rentas procedentes de la cesión del derecho a la explotación de la imagen o del consentimiento o autorización para su utilización, aun cuando constituyan ingresos derivados de explotaciones económicas. |
| 10 | Artículo 60.1.e) RIS - Las rentas procedentes del arrendamiento o subarrendamiento de inmuebles urbanos, aun cuando constituyan ingresos derivados de explotaciones económicas. |
| 11 | Otros. |

L6 – Situación del inmueble

| Valores | Descripción |
| --- | --- |
| 01 | Inmueble con referencia catastral situado en cualquier punto del territorio español, excepto País Vasco y Navarra. |
| 02 | Inmueble situado en la Comunidad Autónoma del País Vasco o en la Comunidad Foral de Navarra. |
| 03 | Inmueble en cualquiera de las situaciones anteriores pero sin referencia catastral. |
| 04 | Inmueble situado en el extranjero. |

L7 – Tipo de cargo o minoración

| CALIFICADOR | urn:aeat:names:specification:schema:add: |
| --- | --- |
| Valores | Descripción |
| --- | --- |
| SUPL | Cargo en nombre de un tercero. |
| MINO | Minoración en nombre de un tercero. |
| RETE | Retención. |
| IEDMT | Impuesto especial sobre determinados medios de transporte. |
| OTROS | Otros supuestos de tasas o impuestos no incluidos en el resto de claves. |

L8 – Tipo de propiedad

| CALIFICADOR | urn:aeat:names:specification:schema:lin: |
| --- | --- |
| Valores | Descripción |
| --- | --- |
| RCAT | Referencia catastral. |
| REGI | Clave de régimen. |
| INFO | Regulación aplicable a la línea de la factura. |

L9 – Impuestos y cargos a nivel de línea o documento

| Valores | Descripción |
| --- | --- |
| IEH | Impuesto especial sobre los hidrocarburos. |
| IECE | Impuesto especial sobre la cerveza. |
| IEPI | Impuesto especial sobre productos intermedios. |
| IEA | Impuesto especial sobre el alcohol y bebidas derivadas. |
| IET | Impuesto especial sobre las labores del tabaco. |
| IELC | Impuesto sobre los líquidos para cigarrillos electrónicos y otros productos relacionados con el tabaco. |
| IEE | Impuesto especial sobre la electricidad. |
| IEC | Impuesto especial sobre el carbón. |
| IEP | Impuesto especial sobre los envases de plástico no reutilizables (artículo 82.9.a) Ley 7/2022, de 8 de abril). |
| IEDE | Impuesto sobre el depósito de residuos en vertederos, la incineración y la coincineración de residuos. |
| IMPTAS | Otros impuestos y tasas. |
| RESTO | Otros cargos a nivel de línea o documento. |

L10 – Documentos justificativos adicionales

| CALIFICADOR | urn:aeat:names:specification:schema: |
| --- | --- |
| Valores | Descripción |
| --- | --- |
| QR | QR fiscal. |
| AUT | Autorización de facturación. |
| RECT:TIPO | Tipo de factura rectificativa. |
| RECT:MODALIDAD | Modalidad de factura rectificativa. |
| RECT:IMPORTES | Importes rectificados. |
