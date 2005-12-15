## ANEXO II

## Especificaciones del fichero que contenga la información y los datos de los documentos contables

Los ficheros de envío tendrán un nombre y una extensión. El nombre será de 8 caracteres obligatoriamente y empezará por DOC, SIG o SIC dependiendo del sistema que los genere: DOC para los sistemas de los Servicios gestores, SIG para el sistema SIGNO de las Intervenciones delegadas y SIC para el sistema de información contable. Los ficheros de envío tendrán extensión. tcn e internamente serán ficheros de texto.

El contenido del fichero estará dividido en dos partes, la primera parte contendrá los datos de cabecera y serán los datos generales del envío. La segunda parte del fichero contendrá los datos de detalle de los documentos incluidos en el envío. Los documentos incluidos en un envío tendrán que estar ordenados por el número de identificación del documento (N.I.D.).

a. Datos de cabecera.–La primera parte del fichero está formada por las 8 primeras líneas que contienen los datos generales del envío. El formato y la información de cada línea es la siguiente:

Número de versión TELCON: Alfanumérico de 3 caracteres, reservado para identificar la versión TELCON con la que se genera el envío. Codificación de acuerdo con lo dispuesto al respecto en las especificaciones del procedimiento TELCON indicado en el punto 3 del apartado Segundo.

Código de centro origen del envío: Alfanumérico de 7 caracteres. Es un número único que identifica a cada unidad administrativa origen de la información a transmitir.

Tipo de relación: Alfanumérico de 1 carácter. Codificación de acuerdo con el tipo de envío, según las especificaciones del procedimiento TELCON indicado en el punto 3 del apartado Segundo.

Número de relación: Alfanumérico de 9 caracteres que identifica el envío con el siguiente formato:

4 posiciones para el ejercicio contable de los documentos incluidos en el envío, es decir, en un envío sólo se podrán incluir documentos pertenecientes al mismo ejercicio contable.

«/» como carácter de separación.

4 posiciones para un secuencial de envíos realizados por una instalación en un ejercicio contable independientemente del tipo de relación.

Fecha de generación: Alfanumérico de 10 caracteres con formato DD/MM/AAAA. Fecha en la que se genera el envío.

Número de documentos contables: Alfanumérico. Indica el número de documentos contables incluidos en el envío.

Número de documentos de proyectos de gasto: Alfanumérico. Indica el número de documentos del subsistema de proyectos incluidos en el envío.

Número de documentos de terceros: Alfanumérico. Indica el número de documentos de terceros incluidos en el envío.

Ejemplo de los datos de cabecera de un envío.

1.0

1920100

P

2002/0032

07/08/2002

1

0

0

b. Datos de detalle.‒Justo después de la última línea de cabecera comienzan los datos de detalle de los documentos incluidos en el envío. La Orden del Ministerio de Economía y Hacienda de 1 de febrero de 1996, por la que se aprueban los documentos contables a utilizar por la Administración General del Estado, regula los diferentes modelos de documentos contables así como los datos a incluir en los mismos.

Se ha elaborado un inventario completo de los diferentes datos susceptibles de ser capturados en cada documento y por lo tanto de ser incluidos en un envío. A cada uno de los datos del inventario se le ha asignado un código de cuatro dígitos denominado código IGAE.

Por cada dato de un documento se creará un registro.

Cada registro de detalle constará de la siguiente información:

Código de centro origen del envío: Alfanumérico de 7 caracteres. Número de instalación del Servicio gestor que capturó el documento.

N.I.D.: Alfanumérico con un máximo de 13 posiciones que identifica el documento de forma única.

Código campo IGAE: Alfanumérico de 4 posiciones.

Número relativo de campo IGAE: Alfanumérico de 3 posiciones. Indica el número de secuencia del campo IGAE cuando se tengan múltiples ocurrencias de un mismo código en el mismo documento. La primera ocurrencia llevará el valor 001, la segunda llevará el valor 002, y así sucesivamente. Ej: Un documento multiaplicación.

Si el código IGAE no fuera un dato múltiple estas tres posiciones se rellenarán con blancos.

Valor del campo IGAE: Alfanumérico de longitud variable cuyo valor es el del dato en cuestión y que contendrá como secuencia final la cadena de caracteres #$

Conviene hacer algunas precisiones en relación a los datos de detalle:

Dentro de un envío los registros deberán estar agrupados por documento, es decir, deberán aparecer todos los registros de un documento antes de pasar al siguiente.

Los documentos deberán estar ordenados ascendentemente por el N.I.D., de forma que aparezcan en primer lugar los documentos que primero se han creado.

Dado que el N.I.D. de un documento puede estar formado por una cadena alfanumérica de hasta 13 caracteres conviene recordar que la ordenación numérica no tiene por qué coincidir con la alfanumérica. Si tenemos dos documento DOC1 y DOC10, en una ordenación numérica DOC1 está antes que DOC10, mientras que en una ordenación alfanumérica DOC10 está antes que DOC1. Para que ambas ordenaciones coincidan, ambas cadenas deben tener el mismo número de caracteres, es decir, si los documentos se hubieran llamado DOC01 y DOC10 ambas ordenaciones coincidirían.

Para cada documento el primer registro que tiene que aparecer en el envío es el 0000 código de operación.

Aunque en la mayoría de las ocasiones un registro sólo ocupa una línea, esto no tiene por que ser así. El conjunto de caracteres que marca el final del registro correspondiente a un determinado dato es #$.

Los importes se deberán grabar siempre con dos dígitos decimales, separando por una coma la parte entera de la parte decimal.

Ejemplo de los registros de detalle de un documento en un fichero generado:

192010000000000000110000 2.00.100.0#$

192010000000000000110008 2#$

192010000000000000110105 29/01/2002#$

192010000000000000110011 2002#$

192010000000000000110053 2002#$

192010000000000000110012 19#$

192010000000000000110001 19201#$

192010000000000000110002 100#$

192010000000000000110004 0#$

192010000000000000110014001323A #$

19201000000000000011001500110000 #$

1920100000000000001100160011,00#$

192010000000000000110014002323A #$

19201000000000000011001500210001 #$

1920100000000000001100160021,00#$

192010000000000000110019 19,00#$

192010000000000000110800 01#$

192010000000000000110801 00#$

Cada registro contiene el valor de un campo en concreto del documento, siendo el campo código IGAE (en negrita) el que indica de qué campo se trata.
