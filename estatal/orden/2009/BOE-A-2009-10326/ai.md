## ANEXO III BIS

## Ficheros de órdenes de domiciliación de autoliquidaciones en cuentas abiertas en entidades no colaboradoras dentro de la Zona SEPA: especificaciones técnicas

Ficheros en formato XML con esquema XSD basado en el estándar ISO 20022 (Core customer-to-PSP direct debit ISO 20022 XML initiation message standards).

Bloque de cabecera

(Bloque único)

| NODO (formato xPATH) | Formato | Semántica | Ejemplo |
| --- | --- | --- | --- |
| /Document/CstmrDrctDbtInitn/GrpHdr/MsgId | Alfanumérico (35). | Identificación del mensaje. | AEATAUTOLIQ20221121123047 |
| /Document/CstmrDrctDbtInitn/GrpHdr/CreDtTm | Alfanumérico (19). YYYY-MM-DDThh:mm:ss.ms. | Fecha y hora de creación. | 2022-11-21T12:30:47.000Z |
| /Document/CstmrDrctDbtInitn/GrpHdr/NbOfTxs | Número entero (15). | Número de operaciones. | 348 |
| /Document/CstmrDrctDbtInitn/GrpHdr/CtrlSum | Número real (18). | Control de suma total de importes. | 7543.14 |
| /Document/CstmrDrctDbtInitn/GrpHdr/InitgPty/Nm | Alfanumérico (70). (Valor fijo). | Nombre de la parte iniciadora. | AGENCIA ESTATAL DE ADMINISTRACION TRIBUTARIA |
| /Document/CstmrDrctDbtInitn/GrpHdr/InitgPty/Id/OrgId/Othr/Id | Alfanumérico (35). (Valor fijo). | Identificación de la parte iniciadora. | ES37000Q2826000H |

Bloque información del pago

(Un bloque por cada fecha de cargo)

| NODO (formato xPATH) | Formato | Semántica | Ejemplo |
| --- | --- | --- | --- |
| /Document/CstmrDrctDbtInitn/PmtInf/PmtInfId | Alfanumérico (35). Cadena "AEAT" seguida de la fecha de cargo de la domiciliación en formato yyyyMMdd. | Identificación de la información de pago. | AEAT20221205 |
| /Document/CstmrDrctDbtInitn/PmtInf/PmtMtd | Alfanumérico (2). Valor fijo (DD, Direct Debit). | Método de pago. | DD |
| /Document/CstmrDrctDbtInitn/PmtInf/NbOfTxs | Número entero (15). | Número de operaciones individuales incluidas en el bloque "Información del pago". | 2 |
| /Document/CstmrDrctDbtInitn/PmtInf/CtrlSum | Número real (18). | Suma total de todos los importes individuales incluidos en el bloque "Información del pago". | 7543.14 |
| /Document/CstmrDrctDbtInitn/PmtInf/ReqdColltnDt | Alfanumérico (10). YYYY-MM-DD. | Fecha de vencimiento de la domiciliación. | 2022-12-05 |
| /Document/CstmrDrctDbtInitn/PmtInf/Cdtr/Nm | Alfanumérico (70). Valor fijo. | Nombre del acreedor. | AGENCIA ESTATAL DE ADMINISTRACION TRIBUTARIA |
| /Document/CstmrDrctDbtInitn/PmtInf/CdtrAcct/Id/IBAN | Alfanumérico (34). | IBAN de la cuenta intermedia de la Agencia Tributaria. | – |
| /Document/CstmrDrctDbtInitn/PmtInf/CdtrAcct/Ccy | Alfanumérico (3). Valor fijo. | Moneda. | EUR |
| /Document/CstmrDrctDbtInitn/PmtInf/CdtrAgt/FinInstnId/BIC | Alfanumérico (11). | Código BIC de la cuenta intermedia de la Agencia Tributaria. | – |
| /Document/CstmrDrctDbtInitn/PmtInf/CdtrSchmeId/Id/PrvtId/Othr/Id | Alfanumérico (35). Valor fijo. | Identificador del acreedor. | ES37000Q2826000H |
| /Document/CstmrDrctDbtInitn/PmtInf/CdtrSchmeId/Id/PrvtId/Othr/SchmeNm/Prtry | Alfanumérico (4). Valor fijo. | – | SEPA |

Subbloque de información de la operación de adeudo directo

(Un subbloque por cada autoliquidación)

| NODO (formato xPATH) | Formato | Semántica | Ejemplo |
| --- | --- | --- | --- |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/PmtId/InstrId | Alfanumérico (35). Se compone de: modelo-número de justificante. | Identificación de la instrucción. | 999-9992581426877 |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/PmtId/EndToEndId | Alfanumérico (35). | Identificación de extremo a extremo. Constituido por el NRC Online asociado al plazo. | 9992581426877RV7NF7Z99 |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/PmtTpInf/SvcLvl/Cd | Alfanumérico (4). Valor fijo. | Código de nivel de servicio. | SEPA |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/PmtTpInf/LclInstrm/Cd | Alfanumérico (35). Valor fijo. | Código de instrumento local. | CORE |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/PmtTpInf/LclInstrm/SeqTp | Alfanumérico (4). Valor fijo. | Secuencia del adeudo: OOFF-Adeudo con una operación con un único pago. | OOFF |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/InstdAmt | Número real (18). | Importe ordenado. Calculado como la suma del importe de la autoliquidación propiamente dicha más el importe que se repercute al obligado al pago en concepto de comisiones y demás gastos bancarios. | 6543.14 |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/DrctDbtTx/MndtRltdInf/MndtId | Alfanumérico (35). | Identificación del mandato. Se corresponde con el número de justificante de la autoliquidación. | 9992581426877 |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/DrctDbtTx/MndtRltdInf/DtOfSgntr | Alfanumérico (10). YYYY-MM-DD. | Fecha de firma del mandato. Se corresponde con la fecha de presentación de la autoliquidación. | 2022-07-20 |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/DrctDbtTx/MndtRltdInf/AmdmntInd | Alfanumérico (5). false. | Indicador de si se ha producido modificación de mandato, siempre tomará el valor false en las domiciliaciones de autoliquidaciones. | false |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/DbtrAgt/FinInstnId/Othr/Id | Alfanumérico (35). Valor fijo. | – | NOTPROVIDED |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/Dbtr/Nm | Alfanumérico (70). | Nombre / razón social del deudor. | DEUDOR PRUEBA UNO |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/Dbtr/PstlAdr/Ctry | Alfanumérico (2). ISO 3166-1 alfa-2. | País del deudor. Dato obligatorio únicamente cuando la entidad bancaria del deudor resida en un país de zona SEPA fuera del Espacio Económico Europeo. | DE |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/Dbtr/PstlAdr/AdrLine | Alfanumérico (70). | Dirección d.el deudor. Dato obligatorio únicamente cuando la entidad bancaria del deudor resida en un país de zona SEPA fuera del Espacio Económico Europeo. Podrá aportarse más de un nodo AdrLine. | DIRECCIÓN DEL DEUDOR |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/DbtrAcct/Id/IBAN | Alfanumérico (34). | IBAN de la cuenta del deudor. | – |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/Purp/Cd | Alfanumérico (4). Valor fijo. | – | OTHR |
| /Document/CstmrDrctDbtInitn/PmtInf/DrctDbtTxInf/RmtInf/Ustrd | Alfanumérico (140). | Concepto: Información que opcionalmente remite el acreedor al deudor para permitirle conciliar el pago con la información comercial del mismo. Conformado por el número de justificante de la autoliquidación. | 9992581426877 |

> Se modifica el "Subbloque de información de la operación de adeudo directo" por el art. 2.6 de la Orden HAC/241/2025, de 10 de marzo. Ref. BOE-A-2025-5048

> Se añade por el art. único.7 de la Orden HFP/387/2023, de 18 de abril de 2023. Ref. BOE-A-2023-9704
