## ANEXO I

## Características técnicas de la aplicación informática INFOREG (versión 4.0) de los registros civiles

1.º Requisitos iniciales:

Independencia respecto al sistema operativo UNIX, Linux o NT.

Base de Datos Relacional. Adaptación en la aplicación a algunas sentencias propias del gestor de Base de datos de Oracle, para su mejor rendimiento.

Acceso a datos vía JDBC.

2.º Arquitectura de la aplicación.

La aplicación se basa en una arquitectura MVC (Modelo Vista Controlador) con tecnología J2EE utilizando como framework de desarrollo el de la Subdirección General de Nuevas Tecnologías basado en Struts.

El diseño permite su utilización por uno o varios Registros Civiles. En el servidor residen los siguientes elementos del aplicativo:

Clases Java incluidas en la plataforma del framework desarrollado en la Subdirección General de Nuevas Tecnologías.

Clases Java de libre distribución.

Módulos de la aplicación de Registros Civiles compuestos de:

Acciones (objetos que se ejecutan en el entorno servidor).

Applets (objetos que se ejecutan en el entorno cliente).

JSP's y páginas HTML.

Documentos XML, donde se almacenan los formatos de las pantallas de captura de datos de los asientos.

Documentos PDF.

B.D Relacional compuesta de:

Tablas de textos matrices. La aplicación contiene un generador dinámico para la construcción de las pantallas de captura de los datos que dan forma a cada uno de los asientos que se practican y la extensión de sus certificados en los libros registrales. Toda esta información se almacena en este conjunto de tablas.

Tablas de datos. En estas tablas se almacenan todos los datos de los asientos generados en cada Registro Civil.
