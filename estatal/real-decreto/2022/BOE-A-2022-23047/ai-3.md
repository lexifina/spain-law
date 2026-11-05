## ANEXO III

## Características técnicas del Sistema de Información Geográfica de Parcelas Agrícolas

A. Características de la base de datos

1. Información gráfica.

La información gráfica básica del SIGPAC se compone de la delimitación geográfica de cada parcela del terreno, que contendrá uno o varios recintos clasificados con alguno de los usos citados en el anexo IV, superpuesta a una base cartográfica formada por mapas y ortofotografías aéreas, proporcionando una visión continua de terreno de todo el territorio nacional.

Por ello la información gráfica del SIGPAC contiene:

1.1 Cartografías en formato vectorial, que cumplan las normas exigibles para la escala 1:5.000, de:

a) Parcelas, coincidentes con las parcelas catastrales.

b) Recintos, uno o varios por cada parcela, clasificados con alguno de los usos citados en el anexo IV.

c) Árboles de frutos secos, cuando la autoridad competente así lo determine.

d) Particularidades topográficas o elementos del paisaje, según se definen en el anexo II, apartado 4, apartado 2 del Real Decreto 1049/2022de 27 de diciembre.

e) Franjas de protección de los cauces, según se definen para la BCAM4, en el anexo II apartado 2 del Real Decreto 1049/2022, de 27 de diciembre.

f) Humedales y turberas.

g) Pastos permanentes, así como las zonas cubiertas por pastos permanentes designadas medioambientalmente sensibles.

h) Superficie agrícola autorizada para el cultivo del algodón.

i) Zonas de cultivo tradicional del arroz.

j) Superficie de olivar con dificultades específicas y alto valor medioambiental.

k) Superficies abancaladas.

1.2 Otras cartografías de referencia.

1.3 Ortofotografías e Imágenes Sentinel2.

2. Información alfanumérica.

La base de datos alfanumérica contiene la siguiente información mínima de cada uno de los recintos: códigos de identificación, superficie, coeficiente de subvencionabilidad en pastos, perímetro, código de uso asignado, incidencias detectadas en la subdivisión, coeficiente de regadío, pendiente media, número de árboles de frutos de cáscara por especies y región del Régimen de ayuda básica a la renta para la sostenibilidad (según se definen en el artículo 8 del Real Decreto 1045/2022, de 27 de diciembre, así como otra información que se determine en la mesa del sistema de gestión y control. Cuando la autoridad competente así lo determine, la base de datos alfanumérica también incluirá el número de árboles de frutos de cáscara por especies (almendro, algarrobo, avellano, nogal, pistacho, castaño y otras especies).

Para cada parcela SIGPAC, se recogerá la referencia catastral correspondiente.

3. Sistema de referencia.

El SIGPAC funciona sobre la base de dos sistemas de referencia de coordenadas. Por un lado, en el ámbito de la Península Ibérica y el Archipiélago Balear el sistema geodésico de referencia oficial es el sistema ETR89 (European Terrestial Reference System 1989); en el caso de Canarias se adopta el sistema REGCAN95.

B. Características del sistema informático

El modelo funcional del SIGPAC responde a una arquitectura de datos centralizada o distribuida cuya actualización se realiza desde terminales o sistemas locales ubicados en las comunidades autónomas o en el Ministerio de Agricultura, Pesca y Alimentación, así como a través de los servicios web desarrollados de acuerdo con unos mismos requisitos técnicos y de seguridad.

El sistema informático gestiona toda la información gráfica y alfanumérica indicada en el apartado A.

1. Funciones básicas que permite el sistema informático:

a) Consulta de la información por todos los agentes del sector –agricultores, entidades colaboradoras y Administraciones Públicas–, a través de los sistemas informáticos dispuestos al efecto. Esta consulta se podrá realizar a través de copias locales, de los servicios de consultas y salidas gráficas, de los servicios INSPIRE (WMS y descarga ATOM) y del Visor SIGPAC.

b) Actualización de la base de datos, ya sea por edición directa o por substitución de la información desde los sistemas instalados en las comunidades autónomas, previo sometimiento a los requisitos de seguridad necesarios.

c) Exportación de información desde la base de datos, de una zona concreta del territorio, en formatos OpenGIS, produciendo ficheros que se transmiten a través del sistema de comunicaciones, con los correspondientes requisitos de seguridad.

2. Sistema de seguridad:

a) Consta de un sistema de seguridad basado en el par usuario-contraseña, para funciones que impliquen actualización de datos.

b) Dispone de mecanismos de control de accesos para permitir asignar a cada usuario sus posibilidades de actuación.

c) El Ministerio de Agricultura, Pesca y Alimentación y las comunidades autónomas garantizarán la seguridad e integridad de la información y el régimen de autorización y acceso al sistema. En todo caso, se deberá conocer la identidad del autor de cualquier modificación y la fecha en la que ésta fue realizada, además de disponer en todo momento del acceso a la información a una fecha determinada.

3. Sistema de comunicaciones:

El modelo de comunicaciones está basado en el uso de la Red Sara o internet en función del tipo de usuario y de las funciones atribuidas.

Los requisitos de seguridad del sistema de comunicaciones serán elevados. Dichos requisitos estarán definidos por el Ministerio de Agricultura, Pesca y Alimentación.

a) Red Sara: Red basada en circuitos privados, y/o redes privadas virtuales sobre circuitos públicos, que permiten mantener la base de datos única, interconectando los diferentes sistemas de información que constituyen el SIGPAC. Permite la transferencia de datos relativos a procesos de consulta y actualización, de forma ágil y segura.

b) Internet: Red utilizada para la realización de consultas a la base de datos por los usuarios finales.
