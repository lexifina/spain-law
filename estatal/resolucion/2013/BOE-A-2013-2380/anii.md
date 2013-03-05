## ANEXO II

## Esquema de URI

El esquema de identificadores de recursos uniformes o URI establece un mecanismo de identificación común para los datos que se exponen públicamente, de forma que se pueda hacer referencia a estos de forma única, fiable y persistente en el tiempo, requisito clave para facilitar su posterior reutilización.

Características básicas del esquema a implementar

Los requisitos genéricos para diseñar el esquema de URI son los siguientes:

a) Utilizar el protocolo HTTP, de forma que se garantiza la resolución de cualquier URI en la web.

b) Usar una estructura de composición de URI consistente, extensible y persistente. Las normas de construcción de los URI seguirán unos patrones determinados que ofrezcan coherencia en la uniformidad, los cuales podrán ser ampliados o adaptados en caso de necesidad.

c) Los URI seguirán una estructura de composición comprensible y relevante. Esto significa que el propio identificador debe ofrecer información semántica autocontenida, lo que permitirá a cualquier agente reutilizador disponer de información sobre el propio recurso, así como su procedencia.

d) No se debe exponer información sobre la implementación técnica de los recursos que representan los URI. En la medida de lo posible se omitirá información específica sobre la tecnología subyacente del recurso representado; por ejemplo, no se incluirán las extensiones correspondientes a tecnologías con las que se generan los recursos web como.php,.jsp, etc.

e) Los URI deben cumplir el principio de persistencia, lo que significa que los que ya han sido creados previamente nunca deberían variar, y que el contenido al que hacen referencia, debería ser accesible. En el caso de que sea necesario cambiar o eliminar el recurso al que apunta un identificador, se deberá establecer un mecanismo de información sobre el estado del recurso usando los códigos de estado de HTTP. En el caso de poder ofrecer una redirección a la nueva ubicación del recurso, se utilizarán los códigos de estado HTTP 3XX, mientras que para indicar que un recurso ha desaparecido permanentemente se utilizará el código de estado HTTP 410.

Estructura básica de los URI

Todos los URI tendrán una estructura uniforme que ofrecerá coherencia al sistema de representación de los recursos, cubrirá los principios básicos de construcción de las mismas y contendrá información intuitiva sobre la procedencia y el tipo de información que identifica.

La base de los URI incluirá información básica sobre la procedencia de los datos, que representará un espacio dedicado por parte de la entidad para albergar su plataforma de reutilización; para indicar la situación de la información relativa a la iniciativa de datos abiertos –portal web, catálogo, u otra información sobre el proyecto– se utilizará preferentemente www.sede.gob.es/datosabiertos o bien http://organismo.gob.es/datosabiertos cuando los recursos no se ubiquen en una sede electrónica. El resto de los recursos semánticos podrán seguir un patrón dependiente únicamente del dominio (http://organismo.gob.es).

Para el caso de los URI de la documentación en los portales web de los organismos, cabe en su caso determinar primero el idioma, según la norma internacional correspondiente ISO 639-1, y después el canal, según el modelo http://organismo.gob.es/idioma/datosabiertos, por ejemplo http://organismo.gob.es/es-ES/datosabiertos. Esto dependerá de las políticas y de las características tecnológicas de cada organismo. Esto no será necesario en la gestión de recursos semánticos, ya que su propia descripción admite varios idiomas para el mismo recurso con un URI único.

Los elementos que componen la ruta de un URI son: sector, carácter de la información, tipo de representación, dominio o temática y los conceptos específicos. Dentro de la composición de una URI se especifican por el siguiente orden:

http://{base}/{carácter}[/{sector}][/{dominio}][/{concepto}][.{ext}]

O, alternativamente, utilizando los identificadores de fragmento mediante la marca «#» al final de la dirección:

http://{base}/{carácter}[/{sector}][/{dominio}][.{ext}][#{concepto}]

Esta estructura general de un URI puede variar dependiendo de las necesidades o preferencias de una organización, siendo obligatorio mantener invariables los elementos base y carácter. La parte final del URI, podría identificar la temática general o específica del recurso, el concepto concreto que representa y/o el formato de representación mediante una extensión. Estos dos últimos componentes son opcionales dependiendo del tipo de información que represente.

Carácter:

| Valor | Información que representa |
| --- | --- |
| Catálogo. | Documento o recurso de información incluido en el catálogo, con una lista de recursos o entidades de un mismo dominio. Habitualmente estos documentos y recursos de información contendrían datos comunes como condiciones de uso, origen, vocabularios utilizados, etc. También identifica al catálogo en sí. |
| Def. | Vocabulario u ontología utilizada como modelo semántico. Habitualmente esquemas RDF-S u ontologías representadas mediante OWL. |
| Kos. | Sistema de organización del conocimiento sobre un dominio concreto. Habitualmente taxonomías, diccionarios o tesauros, representados mediante SKOS. |
| Recurso. | Identificación abstracta única y unívoca de un recurso u objeto físico o conceptual. Estos recursos son las representaciones atómicas de los documentos y recursos de información y suelen ser instancias de los conceptos que se definen en los vocabularios. Si se especifica extensión (o formato) en el URI indica que es la representación del recurso. Pueden existir dos tipos de representaciones de un recurso básicas: un documento legible para humanos –normalmente HTML– o para las máquinas, en cualquiera de los formatos de representación de RDF. El tipo concreto del documento será especificado mediante extensiones del propio documento. |

Sector:

La selección de un sector adecuado, acompañado del dominio específico del origen, le dará a cualquier usuario la confianza de conocer el tipo de información que está manejando y la fuente de la misma. Se seleccionará un identificador del sector (primario), según lo especificado en el anexo IV. Cada documento o recurso de información, vocabulario o esquema de conceptos debe pertenecer a un único sector. Si pertenece a más de uno, se utilizará el más representativo o alguno que se pueda considerar común.

Dominio o temática de la información:

Para identificar los elementos específicos dentro de un sector –recursos de información, vocabularios, esquemas de conceptos, etc.–, se creará una referencia adecuada que represente al dominio o temática de la información tratada.

Conceptos específicos:

Los últimos elementos de ciertos URI –tras el carácter, sector y nombre del dominio de la información– incluyen a los conceptos e instancias específicas de recursos. Los conceptos son representaciones abstractas que se corresponden con las clases o propiedades de los vocabularios u ontologías utilizados para representar semánticamente los recursos. Además del concepto, se podrá representar una referencia unívoca a instancias concretas. También se podrán representar esquemas de conceptos abstractos, dentro de sistemas de gestión del conocimiento (taxonomías, tesauros, etc.).

Formato:

Dado que los documentos que representan recursos pueden ser de diversos tipos, éstos se identificarán a través de la extensión del propio fichero, como, por ejemplo, «doc.html», «doc.rdf» o «doc.n3». Para la identificación de los recursos de forma abstracta se omitirá la extensión.

A continuación, se especifican los tipos de URI específicos para recursos semánticos de una iniciativa basada en Linked Data.

URI para identificar catálogos y conjuntos de datos

Si la iniciativa de reutilización sólo dispone de un catálogo, se podría representar a través del URI: http://{base}/catalogo

En el caso de que el organismo disponga de más de un catálogo se definirá una referencia descriptiva para cada catálogo que haga referencia al tema o dominio del mismo. Para ello se utilizará el URI: http://{base}/catalogo/{sector}

Los conjuntos de datos incluidos en cada catálogo se identifican mediante un URI con un identificador único para cada conjunto de datos: http://{base}/catalogo/{dataset}

O, en su defecto, utilizando la nomenclatura de identificadores de fragmentos (#): http://{base}/catalogo#{dataset}

URI para identificar vocabularios

Cualquier vocabulario u ontología seguirá el esquema: http://{base}/def/{sector}/{dominio}

Donde sector indicará el tema del vocabulario y dominio corresponderá a la referencia asignada al vocabulario, una representación textual breve pero descriptiva.

Las clases y propiedades del vocabulario tendrán como base el URI correspondiente al vocabulario donde se definen, compuesto con los identificadores de las clases o propiedades según el esquema: http://{base}/def/{sector}/{dominio}/{propiedad|Clase}

O, en su defecto, utilizando la nomenclatura de identificadores de fragmentos (#): http://{base}/def/{sector}/{dominio}#{propiedad|Clase}

URI para identificar esquemas de conceptos

Cualquier sistema de organización del conocimiento –taxonomías, diccionarios, tesauros, etc.– sobre un dominio concreto será identificado mediante un esquema de URI basado en la estructura: http://{base}/kos/{sector}/{dominio}

Donde sector indicará el tema del esquema de conceptos y dominio corresponderá a la referencia asignada a dicho esquema de clasificación. Ésta referencia del dominio será una breve representación textual pero descriptiva.

Los conceptos incluidos en el esquema tendrán como base el URI correspondiente al esquema donde se definen y tendrán la forma: http://{base}/kos/{sector}/{dominio}/{Concepto}

O, en su defecto, utilizando la nomenclatura de identificadores de fragmentos (#): http://{base}/kos/{sector}/{dominio}#{Concepto}

URI para identificar a cualquier instancia física o conceptual

Estos recursos son las representaciones atómicas de los documentos y recursos de información. A su vez suelen ser instancias de las clases que se definen en los vocabularios. Estos recursos se identifican mediante el esquema: http://{base}/recurso/{sector}[/{dominio}]/{clase}/{ID}

O, en su defecto, utilizando la nomenclatura de identificadores de fragmentos (#): http://{base}/recurso/{sector}[/{dominio}]/{clase}#{ID}

Donde sector indicará el tema relacionado con el recurso y clase corresponderá al tipo de concepto que describe al recurso. Habitualmente coincide con el identificador de una de las clases que caracteriza al recurso. El ID es un identificador que permite distinguir al recurso entre el resto de las instancias del mismo tipo, dentro del sistema. El dominio, relativo al recurso, podría corresponder al especificado en el propio vocabulario que define las clases de la instancia, es opcional.

Normalización de los componentes de los URI

Para garantizar la coherencia y el mantenimiento posterior del esquema de URI se aplicarán las siguientes reglas para normalizar las distintas partes que componen los URI:

a) Seleccionar identificadores alfanuméricos cortos únicos, que sean representativos, intuitivos y semánticos.

b) Usar siempre minúsculas, salvo en los casos en los que se utilice el nombre de la clase o concepto. Habitualmente, los nombres de las clases se representan con el primer carácter de cada palabra en mayúsculas.

c) Eliminar todos los acentos, diéresis y símbolos de puntuación. Como excepción puede usarse el guión (–).

d) Eliminar conjunciones y artículos en los casos de que el concepto a representar contenga más de una palabra.

e) Puede usarse el guión (–) como separador entre palabras.

f) Evitar en la medida de lo posible la abreviatura de palabras, salvo que la abreviatura sea intuitiva.

Los términos que componen los URI deberán ser legibles e interpretables por el mayor número de personas posible, por lo que se utilizará el castellano o cualquiera de las lenguas oficiales.

Prácticas relativas a la gestión de recursos semánticos a través de URI

Se aplicarán las prácticas siguientes para la gestión de recursos semánticos descritos en RDF:

a) Siempre que sea posible, y existan versiones del recurso en formato legible para personas HTML o similar y RDF, el servidor que gestiona los URI realizará negociación del contenido en función de la cabecera del agente que realiza la petición. En el caso de que el cliente acepte un formato de representación RDF en cualquiera de sus notaciones (p.e., especificando en su cabecera que acepta el tipo MIME application/rdf+xml) se servirá el documento RDF a través del mecanismo de redirecciones alternativas mediante los códigos de estado HTTP 3XX. De la misma forma, si es posible, se servirá la representación en cualquier otro formato preferido por el cliente.

b) En el caso de que no se realice una negociación del contenido desde el servidor y, para favorecer el descubrimiento de contenido RDF desde los documentos HTML relacionados con las descripciones de los recursos, se incluirán enlaces a la representación alternativa en cualquiera de las representaciones en RDF desde los propios documentos HTML de la forma <link rel=«alternate» type=«application/rdf+xml» href=«documento.rdf»> o similar. En esa sentencia se incluye el tipo de formato MIME del documento (application/rdf+xml, text/n3, etc.).

c) Cuando se establezcan enlaces entre distintos recursos de información, se procurará la generación de enlaces que conecten los recursos bidireccionales para facilitar la navegación sobre los recursos de información en ambos sentidos.
