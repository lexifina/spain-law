## ANEXO SOBRE CARACTERÍSTICAS TÉCNICAS DE LA APLICACIÓN INFORMÁTICA DE LOS REGISTROS CIVILES

La aplicación informática INFOREG (versión 1.0) diseñada y aprobada para la informatización de los Registros Civiles a que se refiere la Orden adjunta responde a las siguientes características técnicas:

1.º Requisitos iniciales:

Independencia respecto al sistema operativo UNIX o NT.

Independencia respecto a cualquier B.D. Relacional. Conexión JDBC.

2.º Arquitectura de la aplicación.

La aplicación se basa en una arquitectura a tres niveles y se ha desarrollado con la herramienta Bolero, que genera código Java.

El diseño permite su utilización por uno o varios Registros Civiles.

En el servidor residen los siguientes elementos del aplicativo:

Clases Java incluidas en Bolero.

Clases Java de libre distribución.

Módulos de la aplicación de Registros Civiles compuestos de:

Servlets (objetos que se ejecutan en el entorno servidor).

Applets (objetos que se ejecutan en el entorno cliente).

Páginas HTML.

Documentos XML, donde se almacenan los formatos de las pantallas de captura de datos de los asientos.

B.D Relacional compuesta de:

Tablas de documentos. La aplicación contiene un generador de documentos dinámico, que define las pantallas de captura de los datos que dan forma a cada uno de los asientos que se practican (almacenadas en documentos XML), y la extensión de sus certificados en los libros registrales. Toda esta información se almacena en este conjunto de tablas.

Tablas de datos. En estas tablas se almacenan todos los datos de los asientos generados en cada Registro Civil.
