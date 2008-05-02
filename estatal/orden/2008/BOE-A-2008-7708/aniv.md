## ANEXO IV

## Especificaciones de los protocolos de comunicación de información

La Plataforma de Contratación del Estado, en cumplimiento de la normativa aplicable, facilita una serie de servicios de publicación para los Órganos de Contratación de la Administración mediante un acceso Web al Portal de Contratación y mediante acceso sistémico de maquina a maquina denominado integración B2B.

Los servicios expuestos por la plataforma para la publicación sistema a sistema son los relativos a los siguientes casos de uso:

1. Solicitud de publicación de anuncios y pliegos:

a) Publicación del Anuncio Previo

b) Publicación del Anuncio del Licitación

c) Publicación del Documento de Pliego

d) Publicación del Anuncio de Adjudicación

2. Solicitud de estado de un Espacio Virtual de Licitación (EVL). El EVL es un concepto que maneja la Plataforma y que se equipara al conjunto de datos del expediente (interno al órgano de contratación) al que hay que dar publicidad.

3. Reenvío de las Ofertas recibidas en la Plataforma de contratación a los sistemas de los Órganos de Contratación.

Como mecanismo de comunicación sistema a sistema entre la Plataforma de Contratación del Estado y los Órganos de Contratación se utiliza tecnología Web Services con las siguientes características:

Uso de mensajería SOAP sobre un transporte síncrono petición/respuesta como http(s).

Definición de servicios mediante el lenguaje de definición de servicios Web WSDL.

Uso de canal cifrado mediante SSL/TLS (https) para preservar la confidencialidad de la información antes de su publicación.

La autenticación de los Órganos de Contratación en la plataforma se realizará mediante la utilización de WebService Security (WS-S). El órgano de contratación firmará las peticiones mediante un Certificado Digital de una Autorizada de Certificación (CA) reconocida, del cual debe facilitarse a la plataforma su parte pública (según se especifica en el anexo I).

La última versión de la especificación técnica de los protocolos de comunicación para el intercambio de contenidos sistema a sistema se puede encontrar en Portal de la Plataforma de Contratación del Estado http://contrataciondelestado.es y consta de los siguientes documentos:

1. Documento de Especificación de Integración de Servicios sistema a sistema (B2B).

2. Documento de Especificación de Reenvío de Oferta mediante mecanismos sistema a sistema (B2B).

Cualquier otro documento que deba utilizarse en nuevas implementaciones, o las modificaciones que puedan producirse en los existentes, será puesto a disposición de los interesados en el portal de la Plataforma de Contratación del estado en la dirección http://contrataciondelestado.es
