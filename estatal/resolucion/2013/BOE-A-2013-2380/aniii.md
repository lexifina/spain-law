## ANEXO III

## Metadatos de documentos y recursos de información del catálogo

A continuación se describen los distintos metadatos asociados con el catálogo y los documentos y recursos de información incluidos en él, además del término recomendado para su representación usando vocabularios estándar que se identifican por las abreviaturas de su espacio de nombres. Además de la denominación, descripción del metadato y el tipo de dato que se deberá usar para la representación, se especifica si es obligatorio – columna R (requerido)– y si admite más de un metadato de ese tipo –columna M (múltiple), como podría ser en el caso de las descripciones en distintos idiomas.

Para la descripción y exposición de los metadatos recogidos en este anexo se usarán los vocabularios y esquemas de valores propuestos, mediante tecnologías de la Web Semántica –al menos, la descripción de recursos en RDF en cualquiera de sus formatos de representación–, al objeto de facilitar la interoperabilidad a nivel semántico de los sistemas que compartan esta representación estándar.

Vocabularios:

| Vocabulario | URI |
| --- | --- |
| XML Schema | xsd: http://www.w3.org/2001/XMLSchema# |
| Simple Knowledge Organization System (SKOS) | skos: http://www.w3.org/2004/02/skos/core# |
| Dataset Catalog (dcat) | dcat: http://www.w3.org/ns/dcat# |
| Dublin Core Terms | dct: http://purl.org/dc/terms/ |
| Dublin Core Elements | dc: http://purl.org/dc/elements/1.1/ |
| W3C Time Ontology | time: http://www.w3.org/2006/time# |
| Friend Of A Friend (FOAF) | foaf: http://xmlns.com/foaf/0.1/ |

La representación semántica se basa en el vocabulario DCAT, desarrollado por la entidad World Wide Web Consortium (W3C) y que permite la estandarización en la definición de catálogos de documentos y recursos de información. Un catálogo de documentos y recursos de información se representa mediante instancias de tipo dcat:Catalog e incluye una colección de (dcat:Dataset). Estas instancias tienen propiedades que hacen referencia a otros recursos y conceptos semánticos identificados en los anexos del presente documento y que son representados gráficamente en el siguiente diagrama y detalladas a continuación. Las entidades o propiedades básicas que se detallan en este anexo podrán ser enriquecidas con metadatos adicionales que se estimen oportunos para la mejora de la calidad de la información.

Al menos, los recursos que representen al catálogo de datos y a sus conjuntos de datos deberán ser identificado mediante un URI específico que siga el esquema de definido en el anexo II.

![imagen](https://www.boe.es/datos/imagenes/disp/2013/54/02380_001.png)

| Catálogo (dominio dcat: Catalog) |
| --- |
| Metadato | Descripción | propiedad | R | M | Tipo y Esquema de valores |
| Nombre | Breve título o nombre dado al catálogo de datos. | dct:title | ✓ | ✓ | Literal. Cadena alfanumérica (se recomienda en varios idiomas). |
| Descripción | Resumen descriptivo del catálogo de datos. | dct:description | ✓ | ✓ | Literal. Cadena alfanumérica (se recomienda en varios idiomas). |
| Órgano publicador | Entidad que publica el catálogo. | dct:publisher | ✓ | – | foaf:Agent. Se especificará el URI correspondiente a un órgano público diferenciados por un código alfanumérico único para cada órgano/unidad/oficina, que será extraído del Directorio Común gestionado por el MINHAP según el esquema siguiente: http://datos.gob.es/recurso/sector‑ publico/org/Organismol(ID- MINHAP} |
| Tamaño del catálogo | Número total de documentos y recursos de información inventariados en el catálogo. | dct:extent | – | – | dct:SizeOrDuration. Se recomienda incluir el valor de un número entero y su representación textual equivalente. |
| Identificador | Referencia para identificar el catálogo. | dct:identifier | – | – | xsd:anyURl. URI que identifica la descripción actual del catálogo. |
| Fecha de creación | Fecha de publicación inicial del catálogo | dct:issued | ✓ | – | Literal. Fecha/Hora con formato ISO‑8601: YYYY-MM-DDThh:mm:ssTZD. |
| Fecha de actualización | Fecha en la que se modificó por última vez el catálogo (se añade, elimina o modifica un documento o recurso de información). | dct:modified | ✓ | – | Literal. Fecha/Hora con formato ISO‑8601: YYYY-MM-DDThh:mm:ssTZD. |
| Idioma(s) | Idioma(s) en el(los) que se proporciona la información del catálogo. | dc:language | ✓ | ✓ | Literal. Valores normalizados de etiquetas para identificar idiomas definidos en el RFC 5646 («es», «ga», «ca», «eu», «en», «fr»}. Se usará una etiqueta por cada propiedad. |
| Cobertura geográfica | Ámbito geográfico cubierto por el catálogo. | dct:spatial | – | ✓ | Recurso. Se aplicará preferentemente lo establecido al respecto en el anexo V. Un recurso por propiedad. |
| Temáticas | Totalidad de materias incluidas en el catálogo. | dcat:themeTaxo- nomy | ✓ | ✓ | skos:ConceptScheme. Se aplicará preferentemente la taxonomía definida en el anexo IV. Su valor es: http://datos.gob.es/kos/sector-publico/sector/ |
| Página web | Dirección web de acceso al catálogo de datos (acceso para el público). | foaf:homepage | ✓ | – | Recurso. URI que referencia a la portada del catálogo. |
| Términos de uso | Referencia a los términos de uso generales del catálogo. | dct:license | ✓ | – | Recurso. URI que referencia al recurso que describe los términos de uso. |
| Documento(s) y recurso(s) de información | Lista de cada uno de los documentos y recursos de información del catálogo. | dcat:dataset | ✓ | ✓ | dcat:Dataset. Tendrá tantas propiedades como entradas en el catálogo. (Ver metadatos de documentos y recursos de información). |
| Documento y recurso de información (dominio dcat: Dataset) |
| --- |
| Metadato | Descripción | propiedad | R | M | Tipo y Esquema de valores |
| Nombre | Nombre o título del documento o recurso de información. | dct: title | ✓ | ✓ | Literal. Cadena alfanumérica (se recomienda en varios idiomas). |
| Descripción | Descripción detallada del documento o recurso de información. | dct :description | ✓ | ✓ | Literal. Cadena alfanumérica (se recomienda en varios idiomas). |
| Temática(s) | Temática o materia primaria del documento o recurso de información. | dcat: theme | ✓ | ✓ | skos:Concept. Se recomienda hacer referencia a un tema asociado con el sector público, según la taxonomía definida en el anexo IV. |
| Etiqueta(s) | Etiqueta(s) textual(es) que permiten categorizar libremente el documento o recurso de información. | dcat:keyword | – | ✓ | Literal. Cadena alfanumérica compacta. Pueden incluirse varias propiedades (una por etiqueta). |
| Identificador | URI que identifica al documento o recurso de información. | det:identifie | – | – | xsd:anyURl. URI que identifica la ficha descriptiva del documento o recurso de información. |
| Fecha de creación | Fecha de creación del documento o recurso de información. | dct : issued | – | – | Literal. Fecha/Hora con formato ISO‑8601: YYYY-MM-DDThh:mm:ssTZD. |
| Fecha de última actualización | Última fecha conocida en la que se modificó o actualizó el contenido del documento o recurso de información. | det:modified | – | – | Literal. Fecha/Hora con formato ISO‑8601: YYYY-MM-DDThh:mm:ssTZD. |
| Frecuencia de actualización | Periodo de tiempo aproximado transcurrido entre actualizaciones del documento o recurso de información, si hubiera | dct : accrualPeriodicity | – | – | dct:Frequency. Se recomienda especificar periodos normalizados con formato ISO-8601 (PT), o similar. |
| Idioma(s) | Idioma(s) en el(los) que se encuentra la información del documento o recurso de información. | dc:language | – | ✓ | Literal. Valores normalizados de etiquetas para identificar idiomas definidos en el RFC 5646 («es», «ga», «ca», «eu», «en», «fr»}. Se usará una etiqueta por propiedad. |
| Organismo que expone y publica los datos | Organismo que publica el documento o recurso de información. | dct:publisher | ✓ | – | foaf:Agent. Se especificará el URI correspondiente a un organismo público diferenciados por un código alfanumérico único para cada órgano/unidad/oficina, que será extraído del Directorio Común gestionado por el MINHAP según el esquema siguiente: http:lldatos.gob.es/recu rso/sector‑ publico/org/Organismo){ID-MINHAP } |
| Condiciones de uso | Recurso que describe las condiciones de uso o licencia específica aplicable al propio documento o recurso de información. | dct : license | – | – | dct:LicenseDocument o similar. Se especificará un URI que referencia al recurso que define las condiciones de uso. Si no es una licencia-tipo, y si fuese necesario, en la descripción se podría indicar contraprestación económica utilizando valores del código de divisa normalizado por el estándar ISO-4217 (EUR, USD, GBP, etc.). |
| Cobertura geográfica | Ámbito geográfico cubierto por el documento o recurso de información. | dct:spatial | – | ✓ | Recurso. Puede tomar uno de los valores que representan las provincias españolas, según se expresan en el anexo V. |
| Cobertura temporal | Fecha de inicio, fin y la duración del periodo cubierto por el documento o recurso de información. | dct: temporal | – | ✓ | dct:PeriodOfTime. Periodo de tiempo que puede ser definido mediante la ontología de Tiempo del W3C (time:) |
| Vigencia del recurso | Fecha de validez de un documento o recurso de información o en la que se estima una modificación o actualización de su contenido. | dct:valid | – | – | Literal. Fecha/Hora con formato ISO‑8601: YYYY-MM-DDThh:mm:ssTZD. |
| Recurso(s) relacionado(s) | Enlaces a recursos relacionados con el documento o recurso de información (información sobre los propios datos, material audiovisual, etc.). | dct : references | – | ✓ | Recurso. URI que identifica al recurso relacionado. Se pueden incluir tantas propiedades como referencias se conozcan. |
| Normativa | Normativa relativa al documento o recurso de información. Es un enlace a un documento legal. | dct : conformsTo | – | ✓ | Recurso. URI que identifica al documento legal relacionado. Se pueden incluir tantas propiedades como documentos normativos se conozcan. |
| Distribución(es) | Referencia a los recursos que identifican los volcados del documento o recurso de información en sus posibles formatos. | dcat:distribution | ✓ | ✓ | dcat:Distribution. URI que identifica al recurso que describe una distribución del documento o recurso de información. Puede tener tantas propiedades como distribuciones se conozcan. |
| Distribución de documento o recurso de información (dominio dcat: Distribution) |
| --- |
| Metadato | Descripción | propiedad | R | M | Tipo y Esquema de valores |
| Identificador | URI que identifica a la distribución. | la dct:identifie | – | – | xsd:anyURl. URI que identifica la ficha descriptiva de la distribución. |
| Nombre | Breve título o nombre dado a la distribución. | dct:title | – | ✓ | Literal. Cadena alfanumérica (se recomienda en varios idiomas). |
| URL de acceso | URL que permite el acceso al volcado o consulta de los documentos o recursos de información. | dcat : accessURL | ✓ | – | Literal. URL con la dirección del documento, o servicio que permite la obtención de los datos. |
| Formato | Formato en que se encuentra representado el documento o recurso de información. | dcat:mediaType | ✓ | – | dct:MediaTypeOrExtent. Recurso que indica el tipo MIME del formato de los datos. Únicamente se especificará un formato por distribución. |
| Tamaño | Tamaño aproximado del documento o recurso de información. | dcat:byteSize | – | – | Literal. El tamaño será descrito en bytes. |
| Información adicional sobre formato | Enlace(s) relacionado(s) con el formato, el donde se indica el formato, el esquema utilizado para su representación u otra información técnica sobre cómo acceder a los documentos o recursos de información. | dct:relation | – | ✓ | Recurso. URI con una referencia a un recurso asociado con el formato. Se pueden incluir tantas propiedades como referencias a documentos adicionales se conozcan. |

> Redactado conforme a la corrección de errores publicada en BOE núm. 132, de 3 de junio de 2013. Ref. BOE-A-2013-5858.
