## ANEXO III

## Informe clínico de consultas externas

| Variable | Formato | Fuente | Valores | Comentarios | CM/R |
| --- | --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento. | TEXTO LIBRE. | CMDIC. | Tipos de informes listados en el anexo I de este real decreto. | Se distinguen tres subtipos de informe de consulta externa: primera consulta (P), evolución o seguimiento (S) y alta (A). Por defecto todos los campos obligatorios aplicarán a todos los subtipos. Se indicarán las excepciones que pudieran aplicar en los comentarios de cada uno. | CM |
| Fecha y hora de consulta. | FECHA-HORA. |  |  | Este campo no será necesario en el subtipo de alta. | (P y S) CM |
| Fecha y hora de alta. | FECHA-HORA. |  |  | Este campo no será necesario en los subtipos de primera consulta y seguimiento. | (A) CM |
| Fecha y hora de firma. | FECHA-HORA. |  |  |  | CM |
| Datos del (de los) profesional/es responsable/s. |  | Se consignarán tantos profesionales como sea necesario. Cardinalidad [1..n]. Se atenderá a la normativa vigente en la denominación de categorías profesionales, servicios y unidades. Podrán ir en el pie de página. | CM |
| ● Nombre responsable. | TEXTO LIBRE. |  |  |  | CM |
| ● Categoría profesional. | TEXTO LIBRE. |  |  |  | CM |
| ● Servicio responsable. | TEXTO LIBRE. |  |  |  | CM |
| ● Unidad asistencial responsable. | TEXTO LIBRE. |  |  |  | R |
| ● Área de gestión clínica. | TEXTO LIBRE. |  |  |  | R |
| DATOS DE LA INSTITUCIÓN EMISORA |
| Datos de la institución emisora. | Se consignará la información existente en el Registro General de centros, servicios y establecimientos sanitarios (REGCESS). | CM |
| Servicio de salud. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Logo del servicio de salud. | IMAGEN. |  |  |  | CM |
| Provisor de servicios. |  | R |
| Denominación del provisor de servicios. | TEXTO LIBRE. |  |  |  | R |
| Logo provisor de servicios. | IMAGEN. |  |  |  | R |
| Centro. |  | CM |
| Denominación del centro. | TEXTO LIBRE. | REGCESS. |  |  | CM |
| Datos de contacto del centro. |  | CM |
| Dirección del centro. |  | En caso de no poder proporcionarse la dirección en el formato estructurado propuesto, se admitirá el envío de un único campo de texto libre que contenga, como mínimo, la información de los campos marcados como obligatorios. | CM |
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
| DATOS DEL PACIENTE |
| Datos del paciente. | Se consignará la información que figure en la base de datos de tarjeta sanitaria individual (TSI). | CM |
| Nombre. | TEXTO LIBRE. |  |  |  | CM |
| Primer apellido. | TEXTO LIBRE. |  |  |  | CM |
| Segundo apellido. | TEXTO LIBRE. |  |  |  | R |
| Fecha de nacimiento. | FECHA. |  |  |  | CM |
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
| Datos sociales del paciente. |  | R |
| Cuidador principal. |  |  | R |
| ○ Nombre y apellidos. | TEXTO LIBRE. |  |  |  | R |
| ○ Teléfono. | TEXTO LIBRE. |  |  |  | R |
| ○ Relación con el paciente. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Tutor legal. |  |  | R |
| ○ Nombre y apellidos. | TEXTO LIBRE. |  |  |  | R |
| ○ Teléfono. | TEXTO LIBRE. |  |  |  | R |
| Contacto de emergencia. |  |  | R |
| ● Nombre y apellidos. | TEXTO LIBRE. |  |  |  | R |
| ● Teléfono. | TEXTO LIBRE. |  |  |  | R |
| ● Relación con el paciente. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| DATOS DEL PROCESO ASISTENCIAL |
| Datos del episodio. |  | CM |
| Motivo de consulta. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  | Este campo no es necesario en el subtipo de seguimiento. | (P y A) CM |
| Motivo de alta. | TEXTO CODIFICADO. | CMBD. |  | Este campo no será necesario en los subtipos de primera consulta y seguimiento. | (A) CM |
| Antecedentes personales. | Esta subsección no será necesaria en el subtipo de seguimiento. El orden de las diferentes subsecciones será flexible, primando siempre la lógica clínica y legibilidad del informe. | (P y A) CM |
| Enfermedades previas. |  | En los casos en los que la subsección sea obligatoria, de no contener información, deberá consignarse un valor nulo (NullFlavor). | (P y A) CM |
| ● Enfermedad. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  |  | (P y A) CM |
| ● Edad de inicio. | TEXTO LIBRE. |  |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Año de inicio. | TEXTO LIBRE. |  |  |  | R |
| Antecedentes neonatales. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  | Se consignarán tantos antecedentes como se considere oportuno. Cardinalidad [0..n]. | R |
| Antecedentes obstétricos. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  | Se consignarán tantos antecedentes como se considere oportuno. Cardinalidad [0..n]. | R |
| Antecedentes quirúrgicos. |  | En los casos en los que la subsección sea obligatoria, de no contener información, deberá consignarse un valor nulo (NullFlavor). | (P y A) CM |
| ● Procedimiento. | TEXTO CODIFICADO. | CIE PCS. SNOMED CT. |  |  | (P y A) CM |
| ● Edad en momento procedimiento. | TEXTO LIBRE. |  |  |  | R |
| ● Fecha del procedimiento. | FECHA. |  |  |  | R |
| ● Año del procedimiento. | TEXTO LIBRE. |  |  |  | R |
| Dispositivos médicos. |  | En los casos en los que la subsección sea obligatoria, de no contener información, deberá consignarse un valor nulo (NullFlavor). | (P y A) CM |
| ● Dispositivo médico. | TEXTO CODIFICADO. | EMDN. SNOMED CT. |  |  | (P y A) CM |
| ● Fecha implantación. | FECHA. |  |  |  | R |
| ● Fecha de retirada. | FECHA. |  |  |  | R |
| ● Identificador del dispositivo. | TEXTO LIBRE. |  |  |  | R |
| Vacunaciones e inmunizaciones. |  | En los casos en los que la subsección sea obligatoria, de no contener información, deberá consignarse un valor nulo (NullFlavor). | (P y A) CM |
| ● Vacuna/ Inmunización. | TEXTO CODIFICADO. | SNOMED CT. |  |  | (P y A) CM |
| ● Fecha administración. | FECHA. |  |  |  | (P y A) CM |
| ● Nombre comercial. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | R |
| ● Lote. | TEXTO LIBRE. |  |  |  | R |
| Alergias e intolerancias. |  | En los casos en los que la subsección sea obligatoria, de no contener información, deberá consignarse un valor nulo (NullFlavor). | (P y A) CM |
| ● Tipo de reacción. | TEXTO CODIFICADO. | eHDSI. | eHDSIAdverseEventType. |  | (P y A) CM |
| ● Agente causal. | TEXTO CODIFICADO. | SNOMED CT. |  |  | (P y A) CM |
| ● Manifestación clínica. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | R |
| ● Gravedad. | TEXTO CODIFICADO. | eHDSI. | eHDSISeverity. |  | R |
| ● Criticidad. | TEXTO CODIFICADO. | eHDSI. | eHDSICriticality. |  | R |
| ● Nivel de certeza. | TEXTO CODIFICADO. | eHDSI. | eHDSICertainty. |  | R |
| ● Estado. | TEXTO CODIFICADO. | eHDSI. | eHDSIStatusCode. |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Fecha de fin. | FECHA. |  |  |  | R |
| Hábitos tóxicos. |  |  | R |
| ● Sustancia. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ● Dosis. | TEXTO LIBRE. |  |  |  | R |
| ● Edad de inicio del consumo. | TEXTO LIBRE. |  |  |  | R |
| ● Año de inicio del consumo. | TEXTO LIBRE. |  |  |  | R |
| ● Edad de fin del consumo. | TEXTO LIBRE. |  |  |  | R |
| ● Año de fin del consumo. | TEXTO LIBRE. |  |  |  | R |
| ● Patrón del consumo. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Hábitos no saludables. |  |  | R |
| ● Hábito no saludable. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ● Edad de inicio. | TEXTO LIBRE. |  |  |  | R |
| ● Año de inicio. | TEXTO LIBRE. |  |  |  | R |
| ● Edad de fin. | TEXTO LIBRE. |  |  |  | R |
| ● Año de fin. | TEXTO LIBRE. |  |  |  | R |
| Situación funcional. |  |  | R |
| ● Escalas. |  |  | R |
| ● Escala. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ● Resultado. | TEXTO LIBRE. |  |  |  | R |
| ● Interpretación. | TEXTO LIBRE. |  |  |  | R |
| ● Situación funcional. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Antecedentes familiares. |  | Esta subsección no será necesaria en el subtipo de seguimiento. | (P y A) CM |
| ● Antecedente familiar. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | (P y A) CM |
| ● Grado de parentesco. | TEXTO CODIFICADO. | SNOMED CT. |  |  | (P y A) CM |
| ● Edad de inicio. | TEXTO LIBRE. |  |  |  | R |
| Antecedentes sociales. |  |  | R |
| ● Antecedente social. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Fecha de fin. | FECHA. |  |  |  | R |
| Antecedentes profesionales. |  |  | R |
| ● Antecedente profesional. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Fecha de fin. | FECHA. |  |  |  | R |
| Tratamiento previo. | Esta subsección no será necesaria en el subtipo de seguimiento. La información de esta sección procederá preferentemente de los sistemas de prescripción. | (P y A) CM |
| Medicamentos. |  |  | (P y A) CM |
| ● Fármaco. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  | Denominación del/los principio/s activo/s | (P y A) CM |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | (P y A) CM |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Dosis del medicamento. | TEXTO CODIFICADO. | EDQM, Nomenclátor. |  | El contenido de principio activo, expresado en cantidad por unidad de toma, por unidad de volumen o de peso en función de la presentación Ej: 500 mg (por comprimido); 1mg/ml; 10mg/g | (P y A) CM |
| ● Nombre comercial. | TEXTO CODÍFICADO. | Nomenclátor. |  |  | R |
| ● Posología. | TEXTO LIBRE. |  |  | Ej: 1 comprimido cada 8 horas durante 1 mes | (P y A) CM |
| Fórmulas magistrales. |  |  | R |
| ● Fórmula magistral. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | R |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | R |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | R |
| ● Dosis. | TEXTO LIBRE. |  |  |  | R |
| ● Frecuencia de las tomas. | TEXTO LIBRE. |  |  |  | R |
| Enfermedad actual. | Esta subsección no será necesaria en el subtipo de seguimiento. | (P y A) CM |
| Historia actual. | TEXTO LIBRE. |  |  | Esta subsección no será necesaria en el subtipo de seguimiento. | (P y A) CM |
| Exploración física. | TEXTO LIBRE. |  |  | Esta subsección no será necesaria en el subtipo de seguimiento. | (P y A) CM |
| Signos vitales. |  | Podrán añadirse los signos vitales que se estimen oportunos. | R |
| ○ Presión arterial sistólica. | TEXTO LIBRE. |  |  |  | R |
| ○ Presión arterial diastólica. | TEXTO LIBRE. |  |  |  | R |
| ○ Frecuencia cardiaca. | TEXTO LIBRE. |  |  |  | R |
| ○ Frecuencia respiratoria. | TEXTO LIBRE. |  |  |  | R |
| ○ Temperatura. | TEXTO LIBRE. |  |  |  | R |
| ○ Saturación O2. | TEXTO LIBRE. |  |  |  | R |
| Pruebas complementarias. |  |  | R |
| ○ Pruebas de laboratorio. | TEXTO LIBRE. |  |  |  | R |
| ○ Pruebas imagen. | TEXTO LIBRE. |  |  |  | R |
| ○ Otras pruebas. | TEXTO LIBRE. |  |  |  | R |
| Evolución y comentarios. | TEXTO LIBRE. |  |  |  | CM |
| Diagnóstico principal. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | CM |
| Otros diagnósticos. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | R |
| Procedimientos realizados. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | R |
| Tratamiento (al alta). | Esta subsección se llamará «Tratamiento al alta» en el subtipo de informe de alta. En el resto, se llamará «Tratamiento». La información de esta sección procederá preferentemente de los sistemas de prescripción. | CM |
| Tratamiento farmacológico. |  | CM |
| Medicamentos. |  |  | CM |
| ● Fármaco. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  | Denominación del/los principio/s activo/s | (P y A) CM |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | (P y A) CM |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Dosis del medicamento. | TEXTO CODIFICADO. | EDQM, Nomenclátor. |  | El contenido de principio activo, expresado en cantidad por unidad de toma, por unidad de volumen o de peso en función de la presentación Ej: 500 mg (por comprimido); 1mg/ml; 10mg/g | (P y A) CM |
| ● Nombre comercial. | TEXTO CODÍFICADO. | Nomenclátor. |  |  | R |
| ● Posología. | TEXTO LIBRE. |  |  | Ej: 1 comprimido cada 8 horas durante 1 mes | (P y A) CM |
| Fórmulas magistrales. |  |  | R |
| ● Fórmula magistral. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | CM |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | CM |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | R |
| ● Dosis. | TEXTO LIBRE. |  |  |  | CM |
| ● Frecuencia de las tomas. | TEXTO LIBRE. |  |  |  | CM |
| Vacunas individualizadas. |  | En este apartado se incluirán vacunas individualizadas antialérgicas | R |
| ● Vacunas individualizadas. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Tratamiento no farmacológico. | TEXTO LIBRE. |  |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| Plan de actuación. | TEXTO LIBRE. |  |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |

> Se sustituye por el art. único.8 del Real Decreto 572/2023, de 4 de julio. Ref. BOE-A-2023-15551
