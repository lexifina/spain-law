## ANEXO X

## Historia clínica resumida

| Variable | Formato | Fuente | Valores | Comentarios | CM/R |
| --- | --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento. | TEXTO LIBRE. | CMDIC. | Tipos de informes listados en el anexo I de este real decreto. |  | CM |
| Fecha y hora del informe. | FECHA-HORA. |  |  |  | CM |
| Fecha y hora de actualización. | FECHA-HORA. |  |  |  | CM |
| DATOS DE LA INSTITUCIÓN EMISORA. |
| Servicio de salud. | TEXTO LIBRE. | REGCESS. |  | Se consignará la información existente en el Registro General de centros, servicios y establecimientos sanitarios (REGCESS). | CM |
| Denominación del provisor de servicios. | TEXTO LIBRE. |  |  |  | R |
| Logo del servicio de salud. | IMAGEN. |  |  |  | CM |
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
| Datos del contacto del paciente. |  | CM |
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
| Centro de atención primaria. |  |  |  |
| ○ Centro de atención primaria. | TEXTO CODIFICADO. | REGCESS. |  |  | R |
| ○ Teléfono. | TEXTO LIBRE. |  |  |  | R |
| ○ Correo electrónico. | TEXTO LIBRE. |  |  |  | R |
| Datos sociales del paciente. |  | R |
| Cuidador principal. |  | R |
| ○ Nombre y apellidos. | TEXTO LIBRE. |  |  |  | CM |
| ○ Teléfono. | TEXTO LIBRE. |  |  |  | R |
| ○ Relación con el paciente. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Tutor legal. |  | R |
| ○ Nombre y apellidos. | TEXTO LIBRE. |  |  |  | CM |
| ○ Teléfono. | TEXTO LIBRE. |  |  |  | R |
| Contacto de emergencia. |  | R |
| ● Nombre y apellidos. | TEXTO LIBRE. |  |  |  | CM |
| ● Teléfono. | TEXTO LIBRE. |  |  |  | R |
| ● Relación con el paciente. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| DATOS CLÍNICOS DEL PACIENTE |
| DATOS CLÍNICOS GENERALES |
| ¿Está incluido en protocolo de investigación clínica?. | BOOLEANO. |  |  |  | CM |
| ¿Existe documento de instrucciones previas?. | BOOLEANO. |  |  |  | CM |
| Alertas. | TEXTO CODIFICADO. | CIE. SNOMED CT. CIAP. |  | Una alerta es una llamada especial de atención o señal de alarma sobre un problema de salud u otra circunstancia del paciente que, de no ser tenida en cuenta, puede provocarle consecuencias negativas importantes(1). El campo es obligatorio. En caso de no contener información, se deberá consignar un valor nulo (NullFlavor). | CM |
| Antecedentes personales. | El orden de las diferentes subsecciones será flexible, primando siempre la lógica clínica y legibilidad del informe. | CM |
| Enfermedades previas. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Enfermedad. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  |  | CM |
| ● Edad de inicio. | TEXTO LIBRE. |  |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Año de inicio. | TEXTO LIBRE. |  |  |  | R |
| Antecedentes neonatales. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  | Se consignarán tantos antecedentes como se considere oportuno. Cardinalidad [0..n]. | R |
| Antecedentes obstétricos. | TEXTO CODIFICADO. | CIE. SNOMED CT. |  | Se consignarán tantos antecedentes como se considere oportuno. Cardinalidad [0..n]. | R |
| Antecedentes quirúrgicos. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Procedimiento. | TEXTO CODIFICADO. | CIE PCS. SNOMED CT. |  |  | CM |
| ● Edad en momento procedimiento. | TEXTO LIBRE. |  |  |  | R |
| ● Fecha del procedimiento. | FECHA. |  |  |  | R |
| ● Año del procedimiento. | TEXTO LIBRE. |  |  |  | R |
| Dispositivos médicos. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Dispositivo médico. | TEXTO CODIFICADO. | EMDN. SNOMED CT. |  |  | CM |
| ● Fecha implantación. | FECHA. |  |  |  | R |
| ● Fecha de retirada. | FECHA. |  |  |  | R |
| ● Identificador del dispositivo. | TEXTO LIBRE. |  |  |  | R |
| Vacunaciones e inmunizaciones. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Vacuna/Inmunización. | TEXTO CODIFICADO. | SNOMED CT. |  |  | CM |
| ● Fecha administración. | FECHA. |  |  |  | CM |
| ● Nombre comercial. | TEXTO CODIFICADO. | Nomenclátor. SNOMED CT. |  |  | R |
| ● Lote. | TEXTO LIBRE. |  |  |  | R |
| Alergias e intolerancias. |  |  | CM |
| ● Tipo de reacción. | TEXTO CODIFICADO. | eHDSI. | eHDSIAdverseEventTyp. |  | CM |
| ● Agente causal. | TEXTO CODIFICADO. | SNOMED CT. |  |  | CM |
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
| ○ Escala. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ○ Resultado. | TEXTO LIBRE. |  |  |  | R |
| ○ Interpretación. | TEXTO LIBRE. |  |  |  | R |
| ● Situación funcional. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| Antecedentes familiares. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Antecedente familiar. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | CM |
| ● Grado de parentesco. | TEXTO CODIFICADO. | SNOMED CT. |  |  | CM |
| ● Edad de inicio. | TEXTO LIBRE. |  |  |  | R |
| Antecedentes sociales. |  |  | R |
| ● Antecedente social. | TEXTO CODIFICADO. | SNOMED CT. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Fecha de fin. | FECHA. |  |  |  | R |
| Antecedentes profesionales. |  |  | R |
| ● Antecedente profesional. | TEXTO CODIFICADO. | SNOMED CT. CIE. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| ● Fecha de fin. | FECHA. |  |  |  | R |
| Problemas de salud activos. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Problema de salud activo. | TEXTO CODIFICADO. | SNOMED CT. CIE. CIAP. |  |  | CM |
| ● Fecha de inicio. | FECHA. |  |  |  | CM |
| Cuidados. |  | CM |
| Diagnósticos de Enfermería activos. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| ● Diagnóstico de Enfermería activo. | TEXTO CODIFICADO. | NANDA. SNOMED CT. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| Resultados de Enfermería. |  |  | R |
| ● Resultado de enfermería. | TEXTO CODIFICADO. | NOC. SNOMED CT. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| Intervenciones de Enfermería. |  |  | R |
| ● Intervención de Enfermería. | TEXTO CODIFICADO. | NIC. SNOMED CT. |  |  | R |
| ● Fecha de inicio. | FECHA. |  |  |  | R |
| Intervenciones de Enfermería no vinculadas a diagnóstico. | TEXTO CODIFICADO. | NIC. SNOMED CT. |  |  | R |
| Recomendaciones de cuidados enfermeros. | TEXTO LIBRE. |  |  |  | R |
| Tratamiento y recomendaciones. |  | CM |
| Tratamiento farmacológico. |  | CM |
| Medicamentos. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). La información de esta sección procederá preferentemente de los sistemas de prescripción. | CM |
| ● Fármaco. | TEXTO CODIFICADO. | Nomenclátor. |  | Denominación del/los principio/s activo/s . | CM |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | CM |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Dosis del medicamento. | TEXTO CODIFICADO. | EDQM Nomenclátor. |  | El contenido de principio activo, expresado en cantidad por unidad de toma, por unidad de volumen o de peso en función de la presentación Ej: 500 mg (por comprimido); 1mg/ml; 10mg/g . | CM |
| ● Nombre comercial. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Posología. | TEXTO LIBRE. |  |  | Ej: 1 comprimido cada 8 horas durante 1 mes. | CM |
| Fórmulas magistrales. |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). La información de esta sección procederá preferentemente de los sistemas de prescripción. | R |
| ● Fórmula magistral. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Fecha inicio tratamiento. | FECHA. |  |  |  | R |
| ● Fecha fin de tratamiento. | FECHA. |  |  |  | R |
| ● Vía de administración. | TEXTO CODIFICADO. | Nomenclátor. |  |  | R |
| ● Dosis. | TEXTO LIBRE. |  |  |  | R |
| ● Frecuencia de las tomas. | TEXTO LIBRE. |  |  |  | R |
| Tratamiento no farmacológico. | TEXTO LIBRE. |  |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| Recomendaciones. | TEXTO LIBRE. |  |  | La subsección es obligatoria. En caso de no contener información, deberá consignarse un valor nulo (NullFlavor). | CM |
| (1) Historia clínica digital. Conceptos comunes y definiciones. Enfoque desde la Atención Primaria. Disponible en https://www.sanidad.gob.es/en/estadEstudios/estadisticas/docs/siap/HCE.ConceptosyDefiniciones.pdf» |

> Se añade por el art. único.15 del Real Decreto 572/2023, de 4 de julio. Ref. BOE-A-2023-15551
