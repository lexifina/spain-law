## ANEXO I

## Metadatos mínimos obligatorios del documento electrónico

| Metadato | Descripción/Condiciones de uso | ¿Repetible?1 | Tipo | Esquema de valores |
| --- | --- | --- | --- | --- |
| Versión N11 | Identificador normalizado de la versión de la Norma Técnica de Interoperabilidad de Documento electrónico conforme a la cual se estructura el documento electrónico. | 1 | URI | http://administracionelectronica.gob.es/ENI/XSD/v1.0/documento-e |
| Identificador | Identificador normalizado del documento. | 1 | Cadena de caracteres | ES_ <Órgano>_<AAAA>_<ID específico>2 Ejemplo: ES E00010207 2010 MPR000000000000000000000010207 |
| Órgano | Identificador normalizado de la administración generadora del documento o que realiza la captura del mismo. | 1:N | Cadena de caracteres | Código alfanumérico único para cada órgano/unidad/oficina extraído del Directorio Común gestionado por el Ministerio de Política Territorial y Administración Pública. |
| Fecha de captura | Fecha de alta del documento en el sistema de gestión documental. | 1 | Fecha/hora | Formato: AAAAMMDD T HH:MM:SS <ISO 8601> |
| Origen | Indica si el contenido del documento fue creado por un ciudadano o por una administración. | 1 | Lógico | ‘0’ = Ciudadano ‘1’ = Administración |
| Estado de elaboración | Indica la naturaleza del documento. Si es copia, este metadato indica también si se ha realizado una digitalización o conversión de formato en el proceso de generación. | 1 | Cadena de caracteres | – Original (Ley 11/2007 Ad. 30). – Copia electrónica auténtica con cambio de formato (Ley 11/2007Art.30.1). – Copia electrónica auténtica de documento papel (Ley 11/2007 Art.30.2 y 30.3). – Copia electrónica parcial auténtica. Otros. |
| Nombre de formato | Formato lógico del fichero de contenido del documento electrónico. | 1 | Cadena de caracteres | Valor extraído de la lista de formatos admitidos para ficheros definidos en la Norma Técnica de Interoperabilidad de Catálogo de estándares. |
|  |  |  |  | Documentos de decisión: |
|  |  |  |  | – Resolución. |
|  |  |  |  | – Acuerdo. |
|  |  |  |  | – Contrato. |
|  |  |  |  | – Convenio. |
|  |  |  |  | – Declaración. |
|  |  |  |  | Documentos de transmisión: |
|  |  |  |  | – Comunicación. |
|  |  |  |  | – Notificación. |
|  |  |  |  | – Publicación. |
|  |  |  |  | – Acuse de recibo. |
| Tipo documental | Descripción del tipo documental del documento. | 1 | Cadena de caracteres | Documentos de constancia: |
| – Acta. |
| – Certificado. |
|  |  |  |  | – Diligencia. |
|  |  |  |  | Documentos de juicio: |
|  |  |  |  | – Informe. |
|  |  |  |  | Documentos de ciudadano: |
|  |  |  |  | – Solicitud. |
|  |  |  |  | – Denuncia. |
|  |  |  |  | – Alegación. |
|  |  |  |  | – Recursos. |
|  |  |  |  | – Comunicación ciudadano. |
|  |  |  |  | – Factura. |
|  |  |  |  | – Otros incautados. |
|  |  |  |  | Otros. |
| Tipo de firma | Indica el tipo de firma que avala el documento. En caso de firma con certificado, indica el formato de la firma. | 1:N | Cadena de caracteres | – CSV – Formatos de firma electrónica de documentos electrónicos definidos en la Norma Técnica de Interoperabilidad de Política de firma y certificados de la Administración. |
| Si «Tipo de firma» = CSV |
| Valor CSV | Valor del CSV. | 1:N | Cadena de caracteres | NIA |
| Definición generación CSV | Referencia a la Orden, Resolución o documento que define la creación del CSV correspondiente. | 1:N | Cadena de caracteres | Si AGE: Referencia BOE:BOE A YYYY-XXXXX En otro caso, referencia correspondiente. |
| Si «Estado de elaboración» = |
| – Copia electrónica auténtica con cambio de formato (Ley 11/2007Art.30.1). |
| – Copia electrónica parcial auténtica. |
| Identificador de documento origen | Identificador normalizado del documento origen al que corresponde la copia. | 1 | Cadena de caracteres | Si el documento origen es un documento electrónico: ES_<Órgano>_<AAAA>_<ID específico> Ejemplo: ES–E00010207–2010 MPR000000000000000000000010207 |

1 Nótese que la repetibilidad indicada en la tabla sólo se refiere a los metadatos que acompañan al documento electrónico en un intercambio, sin perjuicio de la posibilidad de asignación de otros metadatos gestionados a nivel interno de cada administración cuyas consideraciones atenderán a la Norma Técnica de Interoperabilidad de Política de gestión de documentos electrónicos.

2 Codificación del Identificador del documento:

<Órgano>: Véase codificación del metadato «Órgano». En caso de más un órgano los nueve caracteres correspondientes serán acordados entre las partes con el fin de asegurarla unicidad del identificador que es su único fin.

<AAAA>: Año de la fecha de captura del documento. (Longitud: 4 caracteres).

<ID específico>: Código alfanumérico que identifica de forma única al documento dentro de los generados por la administración responsable. Cada administración puede diseñar el proceso de generación según sus necesidades, asegurando en cualquier caso su unicidad. Por lo tanto, este ID puede generarse de forma secuencia) o bien, ser una réplica del ID utilizado a nivel interno de la administración. (Longitud: 30 caracteres).
