## ANEXO VIII

## Informe de resultados de otras pruebas diagnósticas

| Variable | Formato | Terminologías / Clasificaciones / Catálogos | Valores / Conjuntos de referencia | Comentarios | CM / R |
| --- | --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento. | TEXTO LIBRE. | CMDIC. | Tipos de informes listados en el anexo I de este real decreto. |  | CM |
| Fecha y hora de petición. | FECHA-HORA. |  |  |  | R |
| Fecha y hora de firma. | FECHA-HORA. |  |  |  | CM |
| Datos del (de los) profesional/es responsable/s. |  | Se consignarán tantos profesionales como sea necesario. Cardinalidad [1..n]. Podrán ir en el pie de página. Se atenderá a la normativa vigente en la denominación de categorías profesionales, servicios y unidades. | CM |
| ● Nombre responsable. | TEXTO LIBRE. |  |  |  | CM |
| ● Categoría profesional. | TEXTO LIBRE. |  |  |  | CM |
| ● Servicio responsable. | TEXTO LIBRE. |  |  |  | CM |
| ● Unidad asistencial responsable. | TEXTO LIBRE. |  |  |  | R |
| ● Área de gestión clínica. | TEXTO LIBRE. |  |  |  | R |
| DATOS DE LA INSTITUCIÓN EMISORA |  |
| Datos de la institución emisora. | Se consignará la información existente en el Registro General de centros, servicios y establecimientos sanitarios (REGCESS). | CM |
| Servicio de salud. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Logo del servicio de salud. | IMAGEN. |  |  |  | CM |
| Provisor de servicios. |  | R |
| Denominación del provisor de servicios. | TEXTO LIBRE. |  |  |  | R |
| Logo provisor de servicios. | IMAGEN. |  |  |  | R |
| Centro. |  | CM |
| Denominación del centro. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Datos de contacto del centro. | En caso de no poder proporcionarse la dirección en el formato estructurado propuesto, se admitirá el envío de un único campo de texto libre que contenga, como mínimo, la información de los campos marcados como obligatorios. | CM |
| Dirección del centro. |  |  | CM |
| ○ Tipo de vía. | TEXTO LIBRE. |  |  |  | CM |
| ○ Nombre de la vía. | TEXTO LIBRE. |  |  |  | CM |
| ○ Número de la vía. | NÚMERO. |  |  |  | CM |
| ○ Código postal. | TEXTO LIBRE. |  |  |  | CM |
| ○ Municipio. | TEXTO LIBRE. |  |  |  | CM |
| ○ Provincia. | TEXTO LIBRE. |  |  |  | CM |
| ○ País. | TEXTO CODIFICADO. | ISO 3166-1. |  |  | CM |
| Dirección web. | URL. |  |  |  | R |
| Correo electrónico. | TEXTO LIBRE. |  |  |  | R |
| Teléfono. | TEXTO LIBRE. |  |  |  | R |
| DATOS DEL PACIENTE |  |
| Datos del paciente. | Se consignará la información que figure en la base de datos de tarjeta sanitaria individual (TSI). | CM |
| Nombre. | TEXTO LIBRE. |  |  |  | CM |
| Primer apellido. | TEXTO LIBRE. |  |  |  | CM |
| Segundo apellido. | TEXTO LIBRE. |  |  |  | R |
| Fecha de nacimiento. | DATE. |  |  |  | CM |
| Sexo. | TEXTO LIBRE. |  |  |  | CM |
| Identificadores del paciente. | Se consignará la información que figure en la base de datos de tarjeta sanitaria individual (TSI). | CM |
| Tipo de documento de identificación. | TEXTO LIBRE. |  |  |  | CM |
| Número de documento. | TEXTO LIBRE. |  |  |  | CM |
| Número de afiliado a la Seguridad Social (NASS). | TEXTO LIBRE. |  |  |  | R |
| Código de Identificación Personal Autonómico (CIP-AUT). | TEXTO LIBRE. |  |  |  | CM |
| Código de Identificación Personal SNS (CIP-SNS). | TEXTO LIBRE. |  |  |  | CM |
| Código de Identificación Personal europeo (CIP europeo). | TEXTO LIBRE. |  |  |  | R |
| Número de historia clínica. | TEXTO LIBRE. |  |  |  | R |
| Datos de contacto del paciente. |  | CM |
| Domicilio. |  | En caso de no poder proporcionarse la dirección en el formato estructurado propuesto, se admitirá el envío de un único campo de texto libre que contenga, como mínimo, la información de los campos marcados como obligatorios. | CM |
| ○ Tipo de vía. | TEXTO LIBRE. |  |  |  | CM |
| ○ Nombre de la vía. | TEXTO LIBRE. |  |  |  | CM |
| ○ Número de la vía. | TEXTO LIBRE. |  |  |  | CM |
| ○ Portal. | TEXTO LIBRE. |  |  |  | R |
| ○ Piso. | TEXTO LIBRE. |  |  |  | R |
| ○ Letra. | TEXTO LIBRE. |  |  |  | R |
| ○ Código postal. | TEXTO LIBRE. |  |  |  | CM |
| ○ Municipio. | TEXTO LIBRE. |  |  |  | CM |
| ○ Provincia. | TEXTO LIBRE. |  |  |  | CM |
| ○ País. | TEXTO CODIFICADO. | ISO 3166-1. |  |  | CM |
| Teléfono móvil. | TEXTO LIBRE. |  |  |  | R |
| Otros teléfonos. | TEXTO LIBRE. |  |  |  | R |
| Correo electrónico. | TEXTO LIBRE. |  |  |  | R |
| Centro de atención primaria. |  |  | R |
| ○ Centro de atención primaria. | TEXTO CODIFICADO. | REGCESS. |  |  | R |
| ○ Teléfono. | TEXTO LIBRE. | REGCESS. |  |  | R |
| ○ Correo electrónico. | TEXTO LIBRE. | REGCESS. |  |  | R |
| DATOS DEL SOLICITANTE |
| Datos de la institución solicitante. | Aplicando el criterio de legibilidad del informe, no se duplicará información. Por ejemplo, en el caso de que la institución solicitante sea la misma que la emisora, podrá obviarse, aunque esté marcada como CM. | CM |
| Servicio de salud. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Logo del servicio de salud. | IMAGEN. |  |  |  | CM |
| Provisor de servicios. |  | R |
| Denominación del provisor de servicios. | TEXTO LIBRE. |  |  |  | R |
| Logo provisor de servicios. | IMAGEN. |  |  |  | R |
| Centro. |  | CM |
| Denominación del centro. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Datos del solicitante. |  | Se consignarán tantos profesionales como sea necesario. Cardinalidad [1..n]. Se atenderá a la normativa vigente en la denominación de categorías profesionales, servicios y unidades. | CM |
| ● Nombre del responsable. | TEXTO LIBRE. |  |  |  | CM |
| ● Categoría profesional. | TEXTO LIBRE. |  |  |  | CM |
| ● Servicio solicitante. | TEXTO LIBRE. |  |  |  | CM |
| ● Unidad solicitante. | TEXTO LIBRE. |  |  |  | R |
| ● Área de gestión sanitaria. | TEXTO LIBRE. |  |  |  |  |
| DATOS DEL PROCESO ASISTENCIAL |
| Información clínica de la solicitud. | TEXTO LIBRE. |  |  |  | CM |
| Procedimiento realizado. | TEXTO CODIFICADO. | SNOMED CT. CIE PCS. SERAM. SEMNIM. |  | La opción preferente es consignar información codificada, pero se aceptará excepcionalmente el uso de texto libre bajo circunstancias convenientemente justificadas. Se consignarán tantos procedimientos como sea necesario. En caso de haber más de uno, la etiqueta de la variable será «Procedimientos realizados». Cardinalidad [1..n]. | CM |
| Fecha y hora del procedimiento. | FECHA-HORA. |  |  |  | CM |
| Descripción del procedimiento. | TEXTO LIBRE. |  |  |  | R |
| Hallazgos. | TEXTO LIBRE. |  |  |  | CM |
| Diagnósticos. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  | La opción preferente es consignar información codificada, pero se aceptará excepcionalmente el uso de texto libre bajo circunstancias convenientemente justificadas. Se consignarán tantos diagnósticos como sea necesario. Cardinalidad [1..n]. | CM |
| Recomendaciones. | TEXTO LIBRE. |  |  |  | R |
| Informe complementario. | ARCHIVO. |  |  | Se incluirán documentos que por su naturaleza incluyan información relevante que no pueda incorporarse en las secciones previas. Se establecerán los mecanismos oportunos para que el acceso al mismo sea lo más sencillo posible. Estos mecanismos se valorarán en las auditorías realizadas por el Ministerio de Sanidad. | R |
| Imágenes relevantes. | IMAGEN. |  |  | Cardinalidad [0..n]. | R |

> Se sustituye por el art. único.13 del Real Decreto 572/2023, de 4 de julio. Ref. BOE-A-2023-15551
