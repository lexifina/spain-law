## ANEXO III

## Especificaciones de contenidos y formatos correspondientes a la arquitectura de información CODICE

CODICE es una librería de componentes y documentos electrónicos estándar para el desarrollo de aplicaciones de contratación pública electrónica de conformidad con los procedimientos y prescripciones de la Directiva 2004/18 y de la Ley 30/2007, de 30 de octubre de 2007, de Contratos del Sector Público, así como con los estándares y recomendaciones internacionales aplicables a la identificación, denominación, definición y construcción de dichos componentes.

La arquitectura desarrollada proporciona la biblioteca de componentes estándar, reutilizables, y extensibles o adaptables a diversos contextos o necesidades de contratos públicos específicos, para satisfacer las necesidades de información de los documentos y mensajes intercambiados a lo largo del ciclo completo de los procedimientos electrónicos de contratación contemplados en la citada Directiva.

Dichos componentes deberían ser además suficientes para la construcción a partir de ellos de cualquier documento o mensaje estructurado (o estructurable) intercambiado entre los participantes de un proceso de contratación pública susceptible de conversión a formato electrónico funcionalmente equivalente.

CODICE proporciona una biblioteca con los documentos electrónicos estandarizados básicos o comunes utilizados en dichos procedimientos, construidos a partir de la librería de los componentes.

La última versión de la especificación técnica de los documentos electrónicos CODICE se puede encontrar en el Portal de la Plataforma de Contratación del Estado http://contrataciondelestado.es y contempla los siguientes documentos:

1. Anuncio de licitación (ContractNotice): Documento que utiliza un órgano de contratación para anunciar el proyecto de adquisición de bienes, servicios u obras. El anuncio de licitación se publicará en el perfil del contratante y si se supera el umbral legal deberá ser publicado en otras publicaciones como el Diario Oficial de la Unión Europea.

2. Anuncio Previo (PriorInformationNotice): Documento que utiliza un órgano de contratación para declarar la intención de comprar bienes, servicios o trabajos durante un período de tiempo determinado. Se trata de un documento no vinculante que puede ser usado para declarar la voluntad de adquirir durante un período, y tiene el efecto de permitir que el órgano de contratación pueda reducir los plazos en el proceso de licitación.

3. Anuncio de Adjudicación (ContractAwardNotice): Documento publicado por un órgano de contratación para anunciar la adjudicación de un contrato.

4. Pliegos (ContractDocuments): Documento que un órgano de contratación publica o envía a un empresario para ofrecerle información acerca de un contrato en licitación. Este es el principal documento para la licitación, en él, los órganos de contratación especifican el objeto del contrato, el proceso de licitación y sus condiciones.

5. Oferta (Tender): Documento mediante el cual un licitador ofrece sus productos, servicios o proyectos como respuesta a una licitación.

6. Declaración (Declaration): Documento que utiliza el operador económico para realizar declaraciones sobre su propia condición. Se utiliza para permitir al órgano de contratación evaluar la capacidad del operador económico de participar en el proceso de licitación.

7. Garantía (Guarantee): Documento para notificar el depósito de una garantía.

8. Notificación de adjudicación (AwardNotification): Documento que se utiliza para comunicar la adjudicación del contrato al adjudicatario.

9. Notificación de no adjudicación (UnawardedNotification): Documento que se utiliza para comunicar la adjudicación del contrato a otro licitador.

10. Notificación de admisión/exclusión (QualificationResultNotification): Documento que el órgano de contratación envía a un operador económico a fin de notificarle su admisión o exclusión al proceso de licitación.

11. Notificación de recurso (AppealNotification): Documento que el órgano de contratación envía a todos los licitadores en un proceso de licitación ante la eventual presentación de un recurso por parte de uno de los licitadores.

12. Notificación de recepción de oferta (TenderReceptionNotification): Documento enviado por el órgano de contratación a un operador económico para notificar de la recepción de la oferta de licitación. Está firmado por el órgano de contratación para que el licitador obtenga una prueba de presentación.

13. Invitación a licitar (InvitationToTender): Documento enviado por el órgano de contratación a un operador económico invitándolo a presentar oferta a un proceso de licitación.

14. Solicitud de pliegos (ContractDocumentsRequest): Documento enviado por el operador económico solicitando la documentación del contrato. En algunos procesos de licitación, los pliegos no son de acceso público, por lo que los licitadores deben solicitarlo mediante este documento

15. Solicitud de subsanación (ClarifyingRequest): Documento enviado por el órgano de contratación a un operador económico solicitando aclaraciones o nueva documentación para poder evaluarle como candidato válido para un proceso de licitación.

Toda la documentación completa necesaria para la implementación de CODICE, así como las modificaciones que pudiera producirse, de uso libre y gratuito, estará a disposición pública en el Portal de la Plataforma de Contratación del Estado (http://contrataciondelestado.es), con el contenido que se detalla a continuación:

1. Memoria CODICE:

Análisis de procedimientos de contratación: estudio de los distintos procedimientos de contratación previstos en la Directiva Europea 2004/18/CE y en la Ley de Contratos del Sector Público española

Normalización UMM de procesos de negocio: representación de los procesos de negocio y de las transacciones implicadas en la contratación electrónica.

2. Mapa ontológico: Contiene todos los componentes CODICE, más los reutilizados de UBL en un único diagrama de clases. Ensamblando estos componentes se han construido los documentos CODICE. Estos mismos componentes podrán utilizarse para crear nuevos documentos.

3. Documentos ensamblados: creados a partir de componentes, con varias representaciones de dichos documentos:

Diagramas de clases. Modelos UML de los documentos CODICE.

Modelo de datos en hoja de calculo.

Esquemas XSD v1.04. Contiene la definición de la estructura XML que deben cumplir los documentos CODICE. Se utilizan para validar los documentos CODICE.

XML de ejemplo.

Guías de implementación. Explicación de cómo implementar cada uno de los documentos CODICE.

4. Listas de códigos: Listas de valores para aquellos elementos de datos que requieren codificación.
