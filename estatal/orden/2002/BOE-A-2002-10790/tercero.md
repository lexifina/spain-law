## TERCERO. Estructura de los ficheros.

## Grupo 2

Todos los ficheros de este grupo tendrán formato de hoja de cálculo con tantos apartados como tipos de información contenga. Cada apartado con la siguiente estructura:

– Líneas de encabezamiento.

– Líneas de detalle.

En el caso de que en un envío no exista algún tipo de información a suministrar correspondiente a un fichero concreto, éste se compondrá exclusivamente de las líneas de encabezamiento.

a) Líneas de encabezamiento. Tantas como sean necesarias para identificar la información.

b) Líneas de detalle. Datos formateados de acuerdo con el contenido del apartado sexto de este Anexo I. «Formato de los registros/lÍneas de detalle».

## Grupo 3

Todos los ficheros con formato definido, correspondientes a este grupo, tendrán la siguiente estructura:

– Un único registro de cabecera.

– Ninguno, uno o varios registros de detalle.

– Un único registro de fin.

En el caso de que en un envío no existiera algún tipo de información a suministrar correspondiente a un fichero concreto, éste se compondrá exclusivamente de los registros de cabecera y fin.

Los ficheros contienen registros de longitud fija, que se corresponde con la del registro de mayor longitud.

a.–Registro de cabecera

El registro de cabecera, que será único en cada fichero, identifica a la Administración General del Estado como entidad que remite la información, tipo de información del fichero, ejercicio y período contable, fecha contable y fecha de envío, así como el indicador de moneda, de acuerdo con el siguiente formato:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Tipo de Registro. | Valor fijo «INI». | 1 | 3 | Alf |
| Ejercicio Económico. | Ejercicio Económico al que se refiere la información de la Cuenta Anual. | 4 | 4 | Num |
| Período contable. | Periodo contable de un ejercicio económico. Si sólo existe un periodo, este tendrá valor «0». | 8 | 1 | Num |
| Fecha contable. | Fecha contable a la que se refiere la información. Valor 31 de diciembre del ejercicio económico, codificada según el apartado «Características generales de campos». | 9 | 8 | Num |
| Fecha de envío. | Fecha en la que se obtiene la información, codificada según el apartado «Características generales de campos». | 17 | 8 | Num |
| Código de la Entidad Contable. | Código de la Administración General del Estado. | 25 | 5 | Num |
| Indicador de moneda. | «E»: euro; «P»: peseta. | 30 | 1 | Alf |
|  | Resto de posiciones sin contenido, hasta completar la longitud del registro de detalle. | 31 |  | Alf |

b.–Registros de detalle.

Los registros de detalle se ajustarán al siguiente formato:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Tipo de Registro. | Coincidirá con el Tipo de información que contiene, «A01» «A02» . «T12». | 1 | 3 | Alf |
| Código de la Entidad Contable. | Código de la Administración General del Estado. | 4 | 5 | Num |
|  | Datos del registro, formateado de acuerdo con el contenido del apartado sexto de este Anexo 1. «Formato de los registros/líneas de detalle. | 9 |  |  |

c.–Registro de fin.

El registro de fin de fichero, que será único en cada fichero, es un registro de control del contenido del fichero con el siguiente formato:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Tipo de Registro. | Valor fijo «FIN». | 1 | 3 | Alf |
| Contador. | Contador del número de registros existentes en el fichero, incluidos los registros de cabecera y fin. | 4 | 6 | Num |
|  | Resto de posiciones sin contenido hasta completar la longitud del registro. | 10 |  | AIf |
