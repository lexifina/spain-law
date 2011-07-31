## ANEXO I

## Metadatos mínimos obligatorios de expedientes electrónicos

| Metadato | Descripción/Condiciones de uso | ¿Repetible?1 F1 | Tipo | Esquema de valores |
| --- | --- | --- | --- | --- |
| Versión NTI | Identificador normalizado de la versión de la Norma Técnica de Interoperabilidad de Expediente electrónico conforme a la cual se estructura el expediente. | 1 | URI | http://administracionelectronica.gob.es/ENI/XSD/v1.0/expediente-e |
| Identificador | Identificador normalizado del expediente. | 1 | Cadena de caracteres | ES <órganoUU><AAAA> EXP <ID especifico>2F2 Ejemplo: ES_E00010207_2010_EXP_ MPR000000000000000000000010207 |
| Órgano | Identificador normalizado de la administración responsable de la tramitación del procedimiento | 1:N | Cadena de caracteres | Código alfanumérico único para cada órgano/unidad/oficina extraído del Directorio Común gestionado por el Ministerio de Política Territorial y Administración Pública. UEjemploU: E00003901 |
| Fecha Apertura Expediente | Fecha de apertura del expediente | 1 | Fecha/hora | Formato: AAAAMMDD T HH:MM:SS <ISO 8601> |
| Clasificación | Procedimiento administrativo con el que se relaciona el expediente | 1 | Cadena de caracteres | Esquema de valores normalizado según el Sistema de Información Administrativa (SIA). Si el procedimiento no se encuentra en SIA: <órgano >_PRO_<ID_PRO_especifico>3F3 |
| Estado | Estado del expediente en el momento de intercambio. | 1 | Cadena de caracteres | – Abierto – Cerrado – Índice para remisión cerrado. |
| Interesado | Identificador del interesado. | 0:N | Cadena de caracteres | a) Si ciudadano o persona jurídica: DNI, NIE, NIF o similar. b) Si administración: <ÓrganoUU> |
| Tipo de firma | Indica el tipo de firma del índice del expediente | 1:N | Cadena de caracteres | – CSV’ – Formatos de firma electrónica de documentos electrónicos definidos en la Norma Técnica de Interoperabilidad de Política de firma y certificados de la Administración. |
| Si “Tipo de firma” = CSV |
| Valor CSV | Valor del CSV. | 1:N | Cadena de caracteres | N/A |
| Definición generación CSV | Referencia a la Orden, Resolución o documento que define la creación del CSV correspondiente. | 1:N | Cadena de caracteres | Si AGE: Referencia BOE:BOE-A-YYYY-XXXXX En otro caso, referencia correspondiente. |

1 Nótese que la repetibilidad indicada en la tabla sólo se refiere a los metadatos que acompañan al expediente electrónico en un intercambio, sin perjuicio de la posibilidad de asignación de otros metadatos gestionados a nivel interno de cada administración cuyas consideraciones atenderán a la Norma Técnica de Interoperabilidad de Política de gestión de documentos electrónicos.

2 Codificación del Identificador del expediente:

<Órgano>: Véase codificación del metadato “Órgano”. En caso de más de un órgano los nueve caracteres correspondientes serán acordados entre las partes con el fin de asegurar la unicidad del identificador que es su único fin.

<AAAA>: Año de la fecha de creación del expediente. (Longitud: 4 caracteres).

<ID_específico>: Código alfanumérico que identifica de forma única al expediente dentro de los generados por la administración responsable. Cada administración puede diseñar el proceso de generación según sus necesidades, asegurando en cualquier caso su unicidad. Por lo tanto, este ID puede generarse de forma secuencial o bien, ser una réplica del ID utilizado a nivel interno de la administración. (Longitud: 30 caracteres).

3 Codificación del metadato Calificación si el procedimiento no existe en SIA:

<Órgano>: Véase codificación del metadato “Órgano”.

<ID_PRO_específico>: Código alfanumérico que identifica de forma única al procedimiento dentro de los propios de la administración. Cada administración puede diseñar el proceso de generación según susnecesidades, asegurando en cualquier caso su unicidad. Por lo tanto, este ID puede generarse de forma secuencial o bien, ser una réplica del ID utilizado a nivel interno de la administración. (Longitud: 30 caracteres).
