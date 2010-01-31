## ANEXO II

## Diseños físicos y lógicos a los que deben ajustarse los archivos que se generen para la presentación telemática y los soportes directamente legibles por ordenador del Modelo 170

A) CARACTERÍSTICAS DE LOS SOPORTES MAGNÉTICOS

Los soportes directamente legibles por ordenador para la presentación de la declaración informativa anual de las operaciones realizadas por los empresarios o profesionales adheridos al sistema de gestión de cobros a través de tarjetas de crédito o de débito (modelo 170) habrán de cumplir las siguientes características:

• Tipo: DVD-R o DVD+R.

• Capacidad: Hasta 4,7 GB.

• Sistema de archivos UDF.

• De una cara y una capa simple.

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y está obligado a presentar declaración informativa anual de las operaciones realizadas por los empresarios o profesionales adheridos al sistema de gestión de cobros a través de tarjetas de crédito o de débito (modelo 170), en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (AEAT), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la AEAT.

B) DISEÑOS LÓGICOS

DESCRIPCIÓN DE LOS REGISTROS

Para cada declarante se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

• Tipo 1: Registro del declarante: Datos identificativos y hoja resumen de la declaración. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

• Tipo 2: Registro de declarado. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros del tipo 2 como declarados tenga la declaración.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta forma la letra “Ñ” tendrá el valor ASCII 209 (Hex. D1) y la “Ç” (cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image8.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image9.png)

## MODELO 170

A. TIPO DE REGISTRO 1: REGISTRO DEL DECLARANTE.

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Constante número '1'. |
| 2-4 | Numérico | MODELO DECLARACIÓN. Constante 170. |
| 5-8 | Numérico | EJERCICIO. Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico | N.I.F. DEL DECLARANTE. Se consignará el N.I.F. del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, (B.O.E del 5 de septiembre). |
| 18-57 | Alfanumérico | RAZÓN SOCIAL DEL DECLARANTE. Se consignará la razón social completa, sin anagrama. En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético | TIPO DE SOPORTE. Se cumplimentará una de las siguientes claves: 'C': Si la información se presenta en DVD. 'T': Transmisión telemática. |
| 59-107 | Alfanumérico | PERSONA CON QUIÉN RELACIONARSE. Datos de la persona con quién relacionarse. Este campo se subdivide en dos: 59-67 TELÉFONO: Campo numérico de 9 posiciones. 68-107 APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN. Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. El número identificativo que habrá de figurar, será un número secuencial cuyos tres primeros dígitos se corresponderán con el código 170. |
| 121-122 | Alfabético | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarse obligatoriamente uno de los siguientes campos: 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una “C” si la presentación de esta declaración tiene por objeto incluir registros que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidos en la misma. La presentación de una declaración complementaria que tenga por objeto la modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente se realizará desde el servicio de consulta y modificación de declaraciones informativas en la sede electrónica de la Agencia Tributaria, dirección electrónica www.agenciatributaria.gob.es). 122 DECLARACIÓN SUSTITUTIVA: Se consignará una “S” si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. En el caso de que se haya consignado una “C” en el campo “Declaración complementaria” o en caso de que se haya consignado “S” en el campo “Declaración sustitutiva”, se consignará el número identificativo correspondiente a la declaración a la que complementa o sustituye. En cualquier otro caso deberá rellenarse a CEROS. |
| 136-140 | Numérico | NÚMERO TOTAL DE IDENTIFICADORES DE COMERCIO. Se consignará el número total de registros de declarados, registros de detalle de tipo 2 en los que el campo “Tipo de Hoja” (posición 76) tome el valor “C”. |
| 141-149 | Numérico | NÚMERO TOTAL DE OPERACIONES DECLARADAS. Se consignará el número total de registros de declarados, registros de detalle de tipo 2 en los que el campo “Tipo de Hoja” (posición 76) tome el valor “I”. |
| 150-166 | Numérico | IMPORTE TOTAL DE LAS OPERACIONES DECLARADAS. Campo numérico de 17 posiciones. Se consignará la suma total de las cantidades reflejadas en el campo “IMPORTE TOTAL NETO ANUAL DE LA FACTURACIÓN DEL EMPRESARIO O PROFESIONAL” (posiciones 102 a 116) correspondientes a los registros de declarado en los que el tipo de hoja (posición 76) toma el valor “I”. Los importes deben consignarse en EUROS. El importe no irá precedido de signo alguno (+/-), ni incluirá coma decimal. Este campo se subdivide en dos: 150-164 Parte entera del importe, si no tiene contenido se consignará a ceros. 165-166 Parte decimal del importe, si no tiene contenido se consignará a ceros. |
| 167-500 | -------------- | BLANCOS. |
| * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image13.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image14.png)

B. TIPO DE REGISTRO 2: REGISTRO DE OPERACIÓN.

Se incluirán tantos registros del tipo 2 de operación como códigos de cuenta cliente correspondan a cada declarado (aunque el importe neto total anual sea el mismo).

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Constante '2'. |
| 2-4 | Numérico | MODELO DECLARACIÓN. Constante 170. |
| 5-8 | Numérico | EJERCICIO. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico | N.I.F. DEL DECLARANTE. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico | N.I.F. DEL EMPRESARIO O PROFESIONAL. Si el declarado dispone de NIF asignado en España, se consignará: Se consignará el N.I.F. del declarado de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, (B.O.E del 5 de septiembre). Si el declarado es una persona jurídica o una entidad en régimen de atribución de rentas (Comunidad de bienes, Sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. Para la identificación de los menores de edad o incapacitados habrán de figurar tanto los datos de la persona menor de edad o incapacitada, incluyéndose su número de identificación fiscal, así como el de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. Sólo se cumplimentará con los NIF asignados en España. |
| 27-35 | Alfanumérico | N.I.F. DEL REPRESENTANTE LEGAL. Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico | APELLIDOS Y NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN DEL EMPRESARIO O PROFESIONAL. a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este mismo orden. Si el declarado es menor de edad o incapacitado, se consignarán en este campo los apellidos y nombre del menor de edad o incapacitado. b) Tratándose de personas jurídicas y entidades en régimen de atribución de rentas, se consignará la razón social o denominación completa de la entidad, sin anagramas. |
| 76 | Alfabético | TIPO DE HOJA. Constante “I”. |
| 77 | Alfabético | CLAVE TIPO DE CÓDIGO. En función de la identificación de la cuenta se consignará una de las siguientes claves: Clave Descripción: C Identificación de la cuenta con el Código Cuenta Cliente (C.C.C.), la cual será obligatoria cuando los declarantes sean entidades que se encuentren inscritas en el Registro de Entidades del Banco de España. O Otra identificación. |
| 78-81 | Alfanumérico | PREFIJO CÓDIGO IBAN. Cuando el campo Clave Tipo de Código tome el valor “C” se consignará en este campo el código IBAN (Código Internacional de Cuenta Bancaria). Este campo se subdivide en dos: 78-79 CÓDIGO PAÍS ISO: campo alfabético. 80-81 DÍGITO DE CONTROL. En los supuestos en que el declarante no tiene asignado el código de entidad por el Banco Emisor y en consecuencia no se tenga el IBAN, se rellenarán a blancos. |
| 82-101 | Numérico | CÓDIGO CUENTA CLIENTE (CCC). Se consignará la identificación de la cuenta donde se han efectuado cobros de las operaciones a lo largo del ejercicio. 1. Para Identificación de la cuenta con el Código Cuenta Cliente (CCC). Su estructura se descompone de la siguiente forma: Posiciones Descripción 82-85 Código de Entidad 86-89 Código de sucursal 90-91 Dígitos de control 92-101 Número de cuenta 2. Si el declarante no tiene asignado el código de entidad por el Banco Emisor, se consignara la identificación definida internamente por la entidad. |
| 102-116 | Numérico | IMPORTE TOTAL NETO ANUAL DE LA FACTURACIÓN DEL EMPRESARIO O PROFESIONAL. Campo numérico de 15 posiciones. Se consignará el importe de la operación. Los importes deben consignarse en EUROS. Cuando la operación estuviera denominada en moneda distinta del euro, a efectos de determinar si su cuantía excede o no de 3.000 euros, el contravalor en euros deberá determinarse en función del tipo de cambio oficial del euro publicado por el Banco Central Europeo y comunicado al Banco de España. Este campo se subdivide en dos: 102-114 Parte entera del importe de la operación, si no tiene contenido se consignará a ceros. 115-116 Parte decimal del importe de la operación, si no tiene contenido se consignará a ceros. |
| 117-500 | -------------- | BLANCOS. |
| * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image18.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/26/01392_5834184_image19.png)

B. TIPO DE REGISTRO 2: REGISTRO DE COMERCIO.

Se incluirán tantos registros de tipo 2 de comercio como números de comercio tenga asignados el empresario o profesional.

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Constante '2'. |
| 2-4 | Numérico | MODELO DECLARACIÓN. Constante 170. |
| 5-8 | Numérico | EJERCICIO. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico | N.I.F. DEL DECLARANTE. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico | N.I.F. DEL EMPRESARIO O PROFESIONAL. Si el declarado dispone de NIF asignado en España, se consignará: Se consignará el N.I.F. del declarado de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, (B.O.E del 5 de septiembre). Si el declarado es una persona jurídica o una entidad en régimen de atribución de rentas (Comunidad de bienes, Sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. Para la identificación de los menores de edad o incapacitados habrán de figurar tanto los datos de la persona menor de edad o incapacitada, incluyéndose su número de identificación fiscal, así como el de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. Sólo se cumplimentará con los NIF asignados en España. |
| 27-35 | Alfanumérico | N.I.F. DEL REPRESENTANTE LEGAL. Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico | APELLIDOS Y NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN DEL EMPRESARIO O PROFESIONAL. a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este mismo orden. Si el declarado es menor de edad o incapacitado, se consignarán en este campo los apellidos y nombre del menor de edad o incapacitado. b) Tratándose de personas jurídicas y entidades en régimen de atribución de rentas, se consignará la razón social o denominación completa de la entidad, sin anagramas. |
| 76 | Alfabético | TIPO DE HOJA. Constante “C”. |
| 77-116 | -------------- | BLANCOS. |
| 117-126 | Numérico | NÚMERO DE COMERCIO DE VENTA. Se consignará el número de comercio de venta con el que el empresario o profesional opera en el sistema. |
| 127-500 | -------------- | BLANCOS. |
