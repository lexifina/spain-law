## ANEXO I

## Documentos clínicos que forman parte del conjunto mínimo de datos del Sistema Nacional de Salud y aspectos generales para su elaboración

Los documentos clínicos que forman parte del conjunto mínimo de datos de los informes clínicos (CMDIC) en el Sistema Nacional de Salud son:

1. Informe clínico de alta.

2. Informe clínico de consulta externa.

3. Informe clínico de urgencias.

4. Informe clínico de atención primaria.

5. Informe de laboratorio.

6. Informe de resultados de pruebas de imagen.

7. Informe de resultados de otras pruebas diagnósticas.

8. Informe de cuidados de enfermería.

9. Historia clínica resumida.

En la elaboración de los informes clínicos mencionados, se tendrán en consideración los aspectos que se indican a continuación:

I. Legibilidad clínica. La legibilidad clínica para profesionales y la ciudadanía, así como la interoperabilidad semántica a nivel de sistemas de información, será tenida en cuenta en la creación de los informes recogidos en los anexos de este real decreto. Su observación por parte de los destinatarios de este real decreto, será objeto de auditoría por el Ministerio de Sanidad.

En aquellos campos marcados como TEXTO CODIFICADO, si las circunstancias técnicas no permiten su envío en este formato, se podrá considerar como opcional y excepcional el envío de TEXTO LIBRE.

El Ministerio de Sanidad podrá aceptar otras terminologías o clasificaciones de referencia no recogidas en estos anexos cuando exista una justificación clínica para ello.

II. Servicios terminológicos del Sistema Nacional de Salud. Se priorizará el uso de los servicios terminológicos del Sistema Nacional de Salud. Para el uso de SNOMED CT, se tendrán en cuenta los recursos desarrollados por el Centro Nacional de Referencia (CNR). Los conjuntos de referencias para este real decreto irán identificados con la partícula «CMDIC» y podrán consultarse en el Navegador SNOMED CT del Sistema Nacional de Salud.

III. Fusión de los informes clínicos de alta hospitalaria y de cuidados de enfermería. Para aquellas comunidades autónomas que lo precisen, se aceptará la fusión de los informes clínicos de alta (ICA) y de cuidados de enfermería (ICE), contando ambos en el listado de informes disponibles que publica el Ministerio de Sanidad.

IV. Formato de la tabla.

| Variable | Formato | Fuente | Valores | Comentarios | CM / R |
| --- | --- | --- | --- | --- | --- |
| SECCIÓN DEL DOCUMENTO |
| Subsección del documento |  |  |
| Agrupación de campos |  |  |  |
| ○ Campo agrupado |  |  |  |  |  |
| ○ Campo agrupado |  |  |  |  |  |
| Campo normal |  |  |  |  |  |
| Clúster de campos |  |  |  |
| ● Campo clúster |  |  |  |  |  |
| ● Campo clúster |  |  |  |  |  |
| Clúster de campos |  |  |  |
| ● Campo clúster |  |  |  |  |  |
| ● Campo clúster |  |  |  |  |  |
| Campo normal |  |  |  |  |  |

• Clúster de campos: Se trata de un conjunto de campos que pueden repetirse en grupo. Están identificados por una celda con fondo gris y los campos incluidos en el mismo por un punto negro. Se recomienda el formato tabla para este tipo de agrupaciones de campos.

• Agrupación de campos: Se trata de un conjunto de campos que deben estar agrupados, pero que no se repiten (en contraposición a los clústeres). Están identificados por texto subrayado en cursiva y los campos incluidos en el mismo por un punto blanco.

• Uso de la sangría: mediante la sangría se expresa el anidamiento y dependencia de unos campos, o agrupaciones, respecto a otros.

• Formato: se explicarán con detalle en el apartado III.

• Fuente: hace referencia a la fuente de los valores que se pueden consignar en el campo en cuestión. En el apartado VI se explicarán las diferentes fuentes incluidas en el real decreto.

• Valores: hace referencia a conjuntos de valores identificables que pueden ser utilizados en el campo en cuestión.

o Valores nulos (NullFlavor): cuando un campo sea obligatorio, pero no pueda consignarse información, se utilizará un valor nulo (NullFlavor) que podrá explicar el motivo de la no existencia de información. Por ejemplo: sin información (NI), desconocido (UNK), preguntado pero desconocido (ASKU), etc.

• Comentarios: detalla información de interés o excepciones que se pueden aplicar a un campo concreto. Por ejemplo, excepciones a la obligatoriedad de algunos campos según circunstancias.

○ Cardinalidad: se indica de la siguiente manera [x..y], donde x es el número mínimo de valores que acepta un campo (0 = opcional; 1 = obligatorio) e y es el número máximo de valores que acepta un campo (n = tantos como sean necesarios).

• CM / R: indica si un campo es obligatorio (CM – conjunto mínimo) u opcional (R – recomendado).

V. Tipos de variables.

| Variable | Detalle |
| --- | --- |
| ARCHIVO. | Pondrá a disposición del profesional un documento adicional de soporte. Las comunidades autónomas establecerán los mecanismos necesarios para facilitar la consulta del mismo. |
| BOOLEANO. | Valor lógico que consigna las opciones SI/NO o VERDADERO/FALSO. |
| FECHA . | Formato dd/mm/aaaa (día/mes/año). |
| FECHA-HORA . | Formato dd/mm/aaaa HH:MM:SS (día/mes/año hora:minutos:segundos). |
| IMAGEN. | Pondrá a disposición del profesional un documento gráfico adicional de soporte. Las comunidades autónomas establecerán los mecanismos necesarios para facilitar la consulta del mismo. También se podrán incrustar las imágenes directamente en el documento. |
| TEXTO LIBRE. | Una cadena de texto simple sin restricciones especiales. |
| TEXTO CODIFICADO. | Está compuesto por 3 campos: ● Identificador único de la fuente: mediante un código OID que permitirá identificar claramente la versión de la fuente que se está utilizando (por ejemplo: Clasificación Internacional de Enfermedades – 9.ª Revisión - Modificación Clínica (edición española). CIE-9-MC. 8.ª edición). ● Código: que es el dato que permitirá la interoperabilidad entre sistemas. ● Término: el descriptor que facilita la lectura a las personas. |
| URL. | Una dirección web. |

VI. Fuentes de información.

| Fuente | Detalle |
| --- | --- |
| CIAP. | La Clasificación Internacional de Atención Primaria (CIAP) permite clasificar los componentes de la consulta: motivo de la consulta, problema de salud atendido y proceso de atención. |
| CIE. | Clasificación Internacional de Enfermedades (CIE), se corresponde a la versión en español de la versión en inglés ICD. |
| CIE PCS. | Sistema de Codificación de Procedimientos de la Clasificación Internacional de Enfermedades (CIE PCS) |
| CMBD. | Conjunto Mínimo Básico de Datos (CMBD). |
| CMDIC. | Conjunto Mínimo de Datos de Informes Clínicos (CMDIC). |
| EDQM. | European Directorate For the Quality of Medicines & Healthcare (EDQM) es uno de los catálogos incluidos en el MVC de eHDSI. En concreto, incluye información sobre la dosis y la forma farmacéutica de los medicamentos. |
| eHDSI. | Son los valores clínicos definidos en el sistema europeo eHealth Digital Service Infraestructure (eHDSI) o Infraestructura de Servicios de Sanidad electrónica. Estos se encuentran definidos en el Master Value Sets Catalogue (MVC) o Catálogo Maestro de Valores, que se trata de una colección de términos basados en sistemas de códigos estandarizados como CIE-10, SNOMED CT, ATC, EDQM, etc. empleados para los sistemas de intercambio transfronterizo de la Unión Europea. Se usará siempre la versión más actualizada del MVC. En informes nacionales se utilizarán los términos en castellano. |
| EMDN. | La Nomenclatura Europea de Dispositivos Médicos (European Medical Device Nomenclature - EMDN) tiene como objetivo apoyar el funcionamiento de la base de datos europea sobre productos sanitarios (EUDAMED). Entre sus diversos usos, será utilizada por los fabricantes para el registro de dispositivos médicos en EUDAMED, donde estará asociada a cada Identificador Único de Dispositivos - Identificador de Dispositivos (UDI-DI). |
| HL7. | Health Level Seven (HL7) es un conjunto de estándares para facilitar el intercambio electrónico de información clínica. |
| ISO 3166-1. | El Estándar Internacional de Normalización ISO 3166-1, publicado por la Organización Internacional de Normalización (ISO), define códigos para la representación de nombres de países y sus subdivisiones |
| LOINC. | Logical Observation Identifiers Names and Codes (LOINC) es un estándar internacional para la identificación de resultados de pruebas de laboratorio. |
| NANDA. | North American Nursing Diagnosis Association (NANDA) es una terminología que refleja los juicios clínicos (diagnósticos) de las enfermeras. |
| NIC. | Clasificación de Intervenciones de Enfermería (NIC). |
| NOC. | Clasificación de Resultados de Enfermería (NOC). |
| Nomenclátor. | Catálogos maestros de medicamentos mantenidos y actualizados diariamente por la Agencia Española de Medicamentos y Productos Sanitarios (AEMPS). |
| REGCESS. | Registro General de centros, servicios y establecimientos sanitarios (REGCESS). |
| SEFM. | Sociedad Española de Física Médica |
| SEMNIM. | Sociedad Española de Medicina Nuclear e Imagen Molecular (SEMNIM). |
| SERAM. | Sociedad Española de Radiología Médica (SERAM). |
| SNOMED CT. | Systematized Nomenclature of Medicine – Clinical Terms (SNOMED CT) es la terminología clínica integral, multilingüe y codificada de mayor amplitud, precisión e importancia desarrollada en el mundo. Las extensiones del Sistema Nacional de Salud pueden consultarse en el Navegador de SNOMED CT del Sistema Nacional de Salud. |
| TSI. | Tarjeta sanitaria individual (TSI). |
| UCUM. | Unified Code for Units of Measure (UCUM) es un sistema de códigos destinado a incluir todas las unidades de medida que se utilizan. |

> Se sustituye por el art. único.6 del Real Decreto 572/2023, de 4 de julio. Ref. BOE-A-2023-15551
