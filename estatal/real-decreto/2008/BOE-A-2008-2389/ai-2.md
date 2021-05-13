## ANEXO II

## Formato XML para el envío de los documentos que deban insertarse en el Suplemento del Tablón Edictal Judicial Único

El contenido del envío se realizará en formato XML con la información estructurada de la siguiente forma:

<envio> <version> <remitente> <fechaPub>? <controlPub> <url> <email> </controlPub> <edictos> <edicto>+ <emisor> <metadatos>? <id>? <sede>? </metadatos> <organo> <identificacion> <direccion> <localidad> <cp> <provincia> <telefono>? <email>? </organo> <contenido>+ <procedimiento> <tipo> <numero> <nig> </procedimiento> <resolucion>+ <tipo> <fecha> <objeto>+ <tipo> <plazo>?<p></plazo> </objeto> </resolucion> <destinatarios>? <determinados> <nombre> </determinados> <indeterminados> <p>+ </indeterminados> </destinatarios> <observaciones>? <p>+ </observaciones> </contenido> <firma> <lugar> <fecha> <cargo> <firmante> </firma> </edicto> </edictos> </envio>

+ significa una o más ocurrencias.

? significa cero o una ocurrencia.

* significa cero o más ocurrencias.

A continuación se describen de forma pormenorizada cada uno de los elementos.

| Esquema | Nombre | Descripción | Valores | Obl. | Tipo |
| --- | --- | --- | --- | --- | --- |
|  | envio | Nodo raíz del envío. |  | [1..1] |  |
| 1 | version | Código que indica la versión utilizada. Existirá compatibilidad de versiones. | [1.0.0] | [1..1] | string |
| 2 | remitente | Código del órgano judicial remitente del edicto, que puede ser el mismo que el emisor o el de un servicio común que actúe como remitente de edictos emitidos por otros órganos judiciales. |  | [1..1] | string |
| 3 | fechaPub | Fecha de publicación solicitada en formato ISO 8601:2004 (aaaa-mm-dd). |  | [0..1] | string |
| 4 | controlPub | Información de control de publicación o devolución. |  | [1..1] | complexType |
| 4.1 | url | Dirección del servicio web a la que se informará de la fecha de publicación de los edictos o de su devolución. |  | [0..1] | anyUri |
| 4.2 | email | Dirección de correo electrónico a la que se informará la fecha de publicación de los edictos o de su devolución. |  | [1..1] | string |
| 5 | edictos | Lista de edictos que componen el envío. |  | [1..1] | complexType |
| 5.1 | edicto | Información relativa a un edicto. |  | [1..*] | complexType |
| 5.1.1 | emisor | Código del órgano judicial que emite el edicto Nota: El emisor y el remitente será el mismo órgano judicial, salvo en el caso de los servicios comunes que actúen como remitentes de edictos emitidos por otros órganos judiciales. |  | [1..1] | string |
| 5.1.2 | metadatos | Información que facilita la identificación de los edictos en los sistemas de información y su localización en la sede electrónica correspondiente. |  | [0..1] | complexType |
| 5.1.2.1 | id | Identificador único del edicto en los sistemas de información del órgano emisor o remitente. Este campo es opcional, aunque se recomienda que esté informado porque permite identificar posibles envíos de edictos duplicados. |  | [0..1] | string |
| 5.1.2.2 | sede | URL de la sede electrónica donde se encuentra disponible el edicto. |  | [0..1] | anyUri |
| 5.1.3 | organo | Datos del órgano emisor. |  | [1..1] | complexType |
| 5.1.3.1 | identificacion | Descripción textual (nombre) del órgano judicial. |  | [1..1] | string |
| 5.1.3.2 | direccion | Domicilio del órgano judicial. |  | [1..1] | string |
| 5.1.3.3 | localidad | Localidad del órgano judicial. |  | [1..1] | string |
| 5.1.3.4 | provincia | Código de provincia del órgano judicial. La tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. |  | [1..1] | string |
| 5.1.3.5 | telefono | Teléfono del órgano judicial. |  | [0..1] | string |
| 5.1.3.6 | email | Dirección de correo electrónico del órgano judicial. |  | [0..*] | string |
| 5.1.4 | contenido | Contenido del edicto. Incluye el atributo idioma con el identificador del idioma en el que está escrito el edicto. La tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. Pueden incluirse dos elementos de este tipo si el edicto se publica en lengua cooficial, además del castellano. En ese caso, ambos elementos tendrán los mismos valores, salvo para los campos «plazo» y «observaciones», que deberán ser redactados en la lengua correspondiente. |  | [1..2] | complexType |
| 5.1.4.1 | procedimiento | Datos del procedimiento. |  | [1..1] | complexType |
| 5.1.4.1.1 | tipo | Código del tipo de procedimiento. La tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. |  | [1..1] | string |
| 5.1.4.1.2 | numero | Número de procedimiento, compuesto por el año (expresado con 4 dígitos) y el número secuencial dentro del año. |  | [1..1] | string |
| 5.1.4.1.3 | nig | Número de identificación general. |  | [0..1] | string |
| 5.1.4.2 | resolucion | Datos de la resolución. |  | [1..*] | complexType |
| 5.1.4.2.1 | tipo | Código del tipo de resolución. La tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. |  | [1..1] | string |
| 5.1.4.2.2 | fecha | Fecha de la resolución en formato ISO 8601:2004 (aaaa-mm-dd). |  | [1..1] | string |
| 5.1.4.2.3 | objeto | Objeto del edicto. |  | [1..*] | complexType |
| 5.1.4.2.3.1 | tipo | Tipo de objeto, cuya tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. |  | [1..1] | string |
| 5.1.4.2.3.2 | plazo | Indicaciones relativas al plazo para atender el tipo de objeto. |  | [0..1] | string |
| 5.1.4.2.3.2.1 | p | Párrafo de texto en el que se incluye las indicaciones relativas al plazo. |  | [1..1] | string |
| 5.1.4.3 | destinatarios | Identificación de los destinatarios del edicto. Si existe este elemento, tiene que incluir o bien el elemento «determinados» o bien el elemento «indeterminados». |  | [0..*] | complexType |
| 5.1.4.3.1 | determinados | Identificación de los destinatarios determinados del edicto, si existen. |  | [1..1] | complexType |
| 5.1.4.3.1.1 | nombre | Nombre del destinatario. Incluye tres atributos para determinar la identificación: 1. tipoId: Tipo de identificador del destinatario, cuya tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE 2. id: Número de identificador 3. truncado: Permite que el órgano judicial indique si el número de identificador debe publicarse de forma íntegra o parcial. |  | [1..*] | string |
| 5.1.4.3.2 | indeterminados | Descripción de los destinatarios indeterminados del edicto. |  | [1..1] | complexType |
| 5.1.4.3.2.1 | p | Párrafo de texto con la descripción de los destinatarios indeterminados. |  | [1..*] | string |
| 5.1.4.4 | observaciones | Observaciones del emisor. |  | [0..1] | complexType |
| 5.1.4.4.1 | p | Párrafo de texto para que el órgano judicial incorpore la información complementaria que debe aparecer en el edicto. |  | [1..*] | string |
| 5.1.5 | firma | Pie de firma del anuncio. |  | [1..1] | complexType |
| 5.1.5.1 | lugar | Población en que tiene lugar la firma. |  | [1..1] | string |
| 5.1.5.2 | fecha | Fecha de la firma en formato ISO 8601:2004 (aaaa-mm-dd). |  | [1..1] | string |
| 5.1.5.3 | cargo | Código del cargo del firmante. La tabla de valores estará disponible en la sede electrónica de la Agencia Estatal BOE. |  | [1..1] | string |
| 5.1.5.4 | firmante | Nombre y dos apellidos del firmante. |  | [1..1] | string |

> Se añade por el art. único.15 del Real Decreto 327/2021, de 11 de mayo. Ref. BOE-A-2021-7843
