## ANEXO II

## DISEÑOS FÍSICOS Y LÓGICOS A LOS QUE DEBEN AJUSTARSE LOS ARCHIVOS QUE SE GENEREN PARA LA PRESENTACIÓN TELEMÁTICA Y LOS SOPORTES DIRECTAMENTE LEGIBLES POR ORDENADOR DEL MODELO 349

A) CARACTERÍSTICAS DE LOS SOPORTES MAGNÉTICOS

Los soportes directamente legibles por ordenador para la presentación de la declaración recapitulativa de operaciones intracomunitarias (modelo 349) habrán de cumplir las siguientes características:

• Tipo: DVD-R o DVD+R

• Capacidad: Hasta 4,7 GB

• Sistema de archivos UDF

• De una cara y una capa simple

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y está obligado a presentar declaración recapitulativa de operaciones intracomunitarias, en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (AEAT), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la AEAT.

B) DISEÑOS LÓGICOS

DESCRIPCIÓN DE LOS REGISTROS

Para cada declarante se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

• Tipo 1: Registro del declarante: Datos identificativos y hoja resumen de la declaración. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados y Anexo de la presente orden.

• Tipo 2: Registro de operador intracomunitario y Registro de rectificaciones. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados y Anexo de la presente orden.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros del tipo 2 como operadores intracomunitarios y rectificaciones tenga la declaración, siendo diferentes los de operadores intracomunitarios y los de rectificaciones.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta formala letra "Ñ" tendrá el valor ASCII 209 (Hex. D1) y la "Ç" (cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II-1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II-2.png)

## MODELO 349

A. TIPO DE REGISTRO 1: REGISTRO DE DECLARANTE.

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Constante número '1'. |
| 2-4 | Numérico | MODELO DECLARACIÓN. Constante '349'. |
| 5-8 | Numérico | EJERCICIO. Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico | NIF DEL DECLARANTE. Se consignará el NIF del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007 de 27 de Julio (BOE del 5 de septiembre). |
| 18-57 | Alfanumérico | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL DECLARANTE. Si es una persona física se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. Para personas jurídicas y entidades en régimen de atribución de rentas, se consignará la razón social completa, sin anagrama. En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético | TIPO DE SOPORTE. Se cumplimentará una de las siguientes claves: "C': la información se presenta en soporte. 'T': Transmisión telemática. |
| 59-107 | Alfanumérico | PERSONACON QUIÉN RELACIONARSE. Datos de la persona con quién relacionarse. Este campo se subdivide en dos: 59-67 TELÉFONO: Campo numérico de 9 posiciones. 68-107 APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico | NUMERO IDENTIFICATIVO DE LA DECLARACIÓN. Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. El número identificativo que habrá de figurar, será un número secuencial cuyos tres primeros dígitos se corresponderán con el código 349. |
| 121-122 | Alfabético | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarse obligatoriamente uno de los siguientes campos: 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una "C" si la presentación de esta declaración tiene por objeto incluir registros que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidas en la misma. La presentación de una declaración complementaria que tenga por objeto la modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente se realizará desde el servicio de consulta y modificación de declaraciones informativas en la sede electrónica de la Agencia Tributaria (https://www.agenciatributaria.gob.es). 122 DECLARACIÓN SUSTITUTIVA: Se consignará una "S" si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico | NUMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. En el caso de que se haya consignado una "C" en el campo "Declaración complementaria" o en el caso de que se haya consignado "S" en el campo "Declaración sustitutiva", se consignará el número identificativo correspondiente a la declaración a la que sustituye. Campo de contenido numérico de 13 posiciones En cualquier otro caso deberá rellenarse a CEROS. |
| 136-137 | Alfanumérico | PERÍODO. Se hará constar el periodo al que corresponda la declaración. Se consignará el que corresponda según la siguiente relación de claves: "01" - Enero "02" - Febrero "03" - Marzo "04" - Abril "05" - Mayo "06" - Junio "07" - Julio "08" - Agosto "09" - Septiembre "10" - Octubre "11" - Noviembre "12" - Diciembre "1T" - Primer trimestre "2T" - Segundo trimestre "3T" - Tercer trimestre "4T" - Cuarto trimestre "0A" - Periodicidad anual |
| 138-146 | Numérico | NÚMERO TOTAL DE OPERADORES INTRACOMUNITARIOS. Deberá consignar el número total de sujetos pasivos a los que se hayan efectuado entregas intracomunitarias exentas, entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, adquisiciones intracomunitarias sujetas, prestaciones intracomunitarias de servicios o adquisiciones intracomunitarias de servicios declarados en el soporte para este declarante que figuren en el registro de operador intracomunitario (registro de tipo 2). (Número de registros de operador intracomunitario (registro de tipo 2) con clave de operación, posición 133, igual a "E", "M, "H", "A, "T", "S" o "I"). |
| 147-161 | Numérico | IMPORTE DE LAS OPERACIONES INTRACOMUNITARIAS. Numérico de 15 posiciones. Deberá consignar la suma total de las bases imponibles que correspondan a entregas intracomunitarias exentas, entregas en otros Estados miembros, subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, adquisiciones intracomunitarias sujetas, prestaciones intracomunitarias de servicios o adquisiciones intracomunitarias de servicios, efectuadas por la totalidad de sujetos pasivos mencionados en el apartado anterior. (Suma de Bases Imponibles, posiciones 134-146, de los registros de operador intracomunitario (registro de tipo 2) y clave de operación, posición 133, igual a "E", "M, "H", "A, "T", "S" o "I". Los importes deben consignarse en EUROS. Este campo se subdivide en dos: 147-159 Parte entera del importe de las operaciones intracomunitarias, si no tiene contenido se consignará a ceros. 160-161 Parte decimal del importe de las operaciones intracomunitarias, si no tiene contenido se consignará a ceros. |
| 162-170 | Numérico | NÚMERO TOTAL DE OPERADORES INTRACOMUNITARIOS CON RECTIFICACIONES. Deberá consignar el número total de registros de rectificaciones de entregas intracomunitarias exentas, de entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, de adquisiciones intracomunitarias sujetas, prestaciones intracomunitarias de servicios o adquisiciones intracomunitarias de servicios declarados en el soporte para este declarante que figuren en el registro de rectificaciones (registro de tipo 2). (Número de registros de rectificaciones (registro de tipo 2) con clave de operación, posición 133, igual a "E", "M, "H", "A, "T", "S" o "I". |
| 171-185 | Numérico | IMPORTE DE LAS RECTIFICACIONES. Deberá consignar la suma total de las bases imponibles rectificadas que correspondan a las entregas intracomunitarias exentas, entregas en otros Estados miembros, subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, a adquisiciones intracomunitarias sujetas, a prestaciones intracomunitarias de servicios o a adquisiciones intracomunitarias de servicios efectuadas por la totalidad de sujetos pasivos mencionados en el apartado anterior. (Suma de Bases Imponibles Rectificadas, posiciones 153-165, de los registros de rectificaciones (registro de tipo 2) y clave de operación, posición 133, igual a "E", "M, "H", "A, "T", "S" o "I". Los importes deben consignarse en EUROS. Este campo se subdivide en dos: 171-183 Parte entera del importe de las bases imponibles rectificadas, si no tiene contenido se consignará a ceros. 184-185 Parte decimal del importe de las bases imponibles rectificadas, si no tiene contenido se consignará a ceros. |
| 186 | Alfabético | INDICADOR CAMBIO PERIODICIDAD EN LA OBLIGACIÓN DE DECLARAR. En caso de que el importe total de las entregas de bienes y prestaciones de servicio superen los 50.000 euros (en los ejercicios 2010 y 2011 este límite será de 100.000€) en el segundo mes de cada trimestre (Febrero, Mayo, Agosto, Noviembre) deberá presentarse una declaración mensual por ese período en la que se incluirán las operaciones correspondientes a ese mes (segundo mes del trimestre) y al anterior (primer mes del trimestre). Se consignará el valor que corresponda según la siguiente relación: X:. Si se corresponde con una declaración mensual con operaciones correspondientes a los dos primeros meses del trimestre. Blanco: En cualquier otro caso. |
| 187-390 | -------------- | BLANCOS. |
| 391-399 | Alfanumérico | NIFDEL REPRESENTANTE LEGAL. Si el declarante es menor de 14 años se consignará en este campo el número de identificación fiscal de su representante legal (padre, madre o tutor). Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 400-487 | -------------- | BLANCOS. |
| 488-500 | Alfanumérico | SELLO ELECTRONICO. Campo reservado para el sello electrónico, que será cumplimentado exclusivamente por los programas de la A.E.A.T. En cualquier otro caso se rellenará a blancos. |
| * Todos los importes serán positivos. * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II_2-1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II_2-2.png)

## MODELO 349

TIPO DE REGISTRO 2: REGISTRO DE OPERADOR INTRACOMUNITARIO.

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSIC. | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Numérico de una posición. Constante "2" (Dos). |
| 2-4 | Numérico | MODELO DECLARACIÓN. Numérico de 3 posiciones. Constante "349". |
| 5-8 | Numérico | EJERCICIO. Numérico de 4 posiciones. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico | NIF DEL DECLARANTE. Alfanumérico de 9 posiciones. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-75 | Alfanumérico | BLANCOS. |
| 76-92 | Alfanumérico | NIF OPERADOR INTRACOMUNITARIO. Alfanumérico de 17 posiciones. Se compone de los subcampos: 76-77 Código país Alfabético de 2 posiciones Se compone de las dos primeras letras identificativas del Estado miembro de la UE. 78-92 Número Alfanumérico de 15 posiciones. Campo alfanumérico, que se ajustará a la izquierda y se rellenará con blancos a la derecha en los casos en que dicho número tenga menos de 15 posiciones. Composición del NIF comunitario de los distintos Estados miembros: A partir del 1 de mayo de 2004, con la incorporación de nuevos países a la Unión Europea, debe tenerse en cuenta la composición del NIF aplicable en cada uno de dichos países, a efectos de la declaración recapitulativa de operaciones intracomunitarias, modelo 349. |
|  | País Código país Número Alemania DE 9 caracteres numéricos Austria AT 9 caracteres alfanuméricos Bélgica BE 10 caracteres numéricos Bulgaria BG 9 o 10 caracteres numéricos Chipre CY 9 caracteres alfanuméricos Dinamarca DK 8 caracteres numéricos Eslovenia SI 8 caracteres numéricos Estonia EE 9 caracteres numéricos Finlandia FI 8 caracteres numéricos Francia FR 11 caracteres alfanuméricos Grecia EL 9 caracteres numéricos Gran Bretaña GB 5, 9 o 12 caracteres alfanuméricos Holanda NL 12 caracteres alfanuméricos Hungría HU 8 caracteres numéricos Italia IT 11 caracteres numéricos Irlanda IE 8 caracteres alfanuméricos Letonia LV 11 caracteres numéricos Lituania LT 9 o 12 caracteres numéricos Luxemburgo LU 8 caracteres numéricos Malta MT 8 caracteres numéricos Polonia PL 10 caracteres numéricos Portugal PT 9 caracteres numéricos República Checa CZ 8, 9 o 10 caracteres numéricos República Eslovaca SK 10 caracteres numéricos Rumanía RO de 2 a 10 caracteres numéricos Suecia SE 12 caracteres numéricos |
| 93-132 | Alfanumérico | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL OPERADOR INTRACOMUNITARIO. Alfanumérico de 40 posiciones. Se cumplimentará con el mismo criterio que el especificado para el declarante en el registro de tipo 1. |
| 133 | Alfabético | CLAVE DE OPERACIÓN. Alfabético de una posición. Se consignará la que corresponda según la siguiente relación: E: Entregas intracomunitarias exentas, excepto las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, que se consignará “T”, y las entregas intracomunitarias de bienes posteriores a una importación exenta, que se consignarán con las claves “M” o “H” según corresponda. M: Entregas intracomunitarias de bienes posteriores a una importación exenta, de acuerdo con el artículo 27.12.º de la Ley del Impuesto sobre el Valor Añadido. H: Entregas intracomunitarias de bienes posteriores a una importación exenta, de acuerdo con el artículo 27.12.º de la Ley del Impuesto sobre el Valor Añadido, efectuadas por el representante fiscal según lo previsto en el artículo 86.Tres de la Ley del Impuesto. A: Adquisiciones intracomunitarias sujetas. T: Entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares. Cuando se realice alguna entrega de bienes de las mencionadas en el artículo 79, apartado 5º del Reglamento del IVA. Estas operaciones, cuando sean efectuadas para un destinatario para el cual se hayan realizado entregas intracomunitarias, se consignarán en un registro independiente de aquél en que se hayan consignado estas últimas operaciones. S: Prestaciones intracomunitarias de servicios realizadas por el declarante. I: Adquisiciones intracomunitarias de servicios localizadas en el territorio de aplicación del Impuesto, prestadas por empresarios o profesionales establecidos en otros Estados miembros cuyo destinatario es el declarante. |
| 134-146 | Numérico | BASE IMPONIBLE. Numérico de 13 posiciones Se hará constar el importe total de la Base Imponible del conjunto de las entregas intracomunitarias exentas, si se ha consignado clave de operación E, del conjunto de las adquisiciones intracomunitarias sujetas, si se ha consignado clave de operación A, del conjunto de las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, si se ha consignado clave de operación T, del conjunto de prestaciones intracomunitarias de servicios realizadas si se ha consignado clave de operación S, o del conjunto de adquisiciones intracomunitarias de servicios si se ha consignado clave de operación I para cada operador intracomunitario. Por lo tanto, si en un mismo periodo se han realizado varias operaciones con un operador intracomunitario, éstas deberán acumularse por clave de operación con el fin de consignar un único registro por cada clave de operación y periodo. En cuanto a las operaciones triangulares, también deberán acumularse por operador intracomunitario y periodo, no obstante se consignarán en un registro independiente de aquellas operaciones distintas de éstas. Se consignarán las operaciones mencionadas en los artículos 79 y 80 del Reglamento del IVA. Los importes deben consignarse en EUROS. Este campo se subdivide en dos: 134-144 Parte entera del importe de las entregas, si no tiene contenido se consignará a ceros. 145-146 Parte decimal del importe de las entregas, si no tiene contenido se consignará a ceros. |
| 147-500 | -------------- | BLANCOS. |
| * Todos los importes serán positivos. * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda, sin signos, sin empaquetar y sin decimales. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, excepto que se especifique lo contrario en la descripción del campo. |

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II_3-1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2010/76/05098_anexo_II_3-2.png)

TIPO DE REGISTRO 2: REGISTRO DE RECTIFICACIONES.

(POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS).

| POSIC. | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. Numérico de una posición. Constante "2" (Dos). |
| 2-4 | Numérico | MODELO DECLARACIÓN. Numérico de 3 posiciones. Constante "349". |
| 5-8 | Numérico | EJERCICIO. Numérico de 4 posiciones. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico | NIF DEL DECLARANTE. Alfanumérico de 9 posiciones. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-75 | Alfanumérico | BLANCOS. |
| 76-92 | Alfanumérico | NIF OPERADOR INTRACOMUNITARIO. Alfanumérico de 17 posiciones. Se compone de los subcampos: 76-77 Código país: Alfabético de 2 posiciones. Se compone de las dos primeras letras identificativas del Estado miembro de la UE. 78-92 Número: Alfanumérico de 15 posiciones. Campo alfanumérico, que se ajustará a la izquierda y se rellenará con blancos a la derecha en los casos en que dicho número tenga menos de 15 posiciones. Composición del NIF comunitario de los distintos Estados miembros: A partir del 1 de mayo de 2004, con la incorporación de nuevos países a la Unión Europea, debe tenerse en cuenta la composición del NIF aplicable en cada uno de dichos países, a efectos de la declaración recapitulativa de operaciones intracomunitarias, modelo 349. |
|  | País Código país Número Alemania DE 9 caracteres numéricos Austria AT 9 caracteres alfanuméricos Bélgica BE 10 caracteres numéricos Bulgaria BG 9 o 10 caracteres numéricos Chipre CY 9 caracteres alfanuméricos Dinamarca DK 8 caracteres numéricos Eslovenia SI 8 caracteres numéricos Estonia EE 9 caracteres numéricos Finlandia FI 8 caracteres numéricos Francia FR 11 caracteres alfanuméricos Grecia EL 9 caracteres numéricos Gran Bretaña GB 5, 9 o 12 caracteres alfanuméricos Holanda NL 12 caracteres alfanuméricos Hungría HU 8 caracteres numéricos Italia IT 11 caracteres numéricos Irlanda IE 8 caracteres alfanuméricos Letonia LV 11 caracteres numéricos Lituania LT 9 o 12 caracteres numéricos Luxemburgo LU 8 caracteres numéricos Malta MT 8 caracteres numéricos Polonia PL 10 caracteres numéricos Portugal PT 9 caracteres numéricos República Checa CZ 8, 9 o 10 caracteres numéricos República Eslovaca SK 10 caracteres numéricos Rumanía RO de 2 a 10 caracteres numéricos Suecia SE 12 caracteres numéricos |
| 93-132 | Alfanumérico | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL OPERADOR INTRACOMUNITARIO. Alfanumérico de 40 posiciones. Se cumplimentará con el mismo criterio que el especificado para el declarante en el registro de tipo 1. |
| 133 | Alfabético | CLAVE DE OPERACIÓN. Alfabético de una posición. Se consignará la que corresponda según la siguiente relación: E: Rectificaciones de las entregas intracomunitarias exentas, excepto las que deban consignarse, según corresponda, con las claves “T”, “M” o “H”. M: Rectificaciones de las entregas intracomunitarias de bienes posteriores a una importación exenta, de acuerdo con el artículo 27.12.º de la Ley del Impuesto sobre el Valor Añadido. H: Rectificaciones de las entregas intracomunitarias de bienes posteriores a una importación exenta efectuadas por el representante fiscal, de acuerdo con el artículo 27.12.º de la Ley del Impuesto sobre el Valor Añadido, efectuadas por el representante fiscal según lo previsto en el artículo 86.Tres de la Ley del Impuesto. A: Rectificaciones a las adquisiciones intracomunitarias sujetas. T: Rectificaciones a las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares. Cuando se realice alguna entrega de bienes de las mencionadas en el artículo 79, apartado 5.º del Reglamento del IVA. Estas operaciones, cuando sean efectuadas para un destinatario para el cual se hayan realizado entregas intracomunitarias, se consignarán en un registro independiente de aquél en que se hayan consignado estas últimas operaciones. S: Rectificaciones a las prestaciones intracomunitarias de servicios realizadas por el declarante. I: Rectificaciones a las adquisiciones intracomunitarias de servicios localizadas en el territorio de aplicación del Impuesto prestadas por empresarios o profesionales establecidos en otros Estados miembros cuyo destinatario es el declarante. |
| 134-146 | -------------- | BLANCOS. |
| 147-178 | Alfanumérico | RECTIFICACIONES. Estos campos se cumplimentarán cuando se hayan producido circunstancias que supongan errores o rectificaciones de las bases consignadas en declaraciones anteriores. La rectificación se incluirá en el periodo en que se hubiera notificado tal modificación al destinatario de los bienes. Por tanto este campo se rellenará únicamente si la operación que se consigna es una rectificación a una entrega, adquisición intracomunitaria, operación triangular, prestación intracomunitaria de servicios o adquisición intracomunitaria de servicios. Se compone de los siguientes subcampos: 147-150 Ejercicio: Numérico de 4 posiciones. Las cuatro cifras del ejercicio fiscal al que corresponde la declaración que se corrige. 151-152 Periodo: Alfanumérico de 2 posiciones. Periodo al que corresponde la declaración que se corrige, codificado con las siguientes claves: "01" - Enero "02" - Febrero "03" - Marzo "04" - Abril "05" - Mayo "06" - Junio "07" - Julio "08" - Agosto "09" - Septiembre "10" - Octubre "11" - Noviembre "12" - Diciembre "1T" - Primer trimestre "2T" - Segundo trimestre "3T" - Tercer trimestre "4T" - Cuarto trimestre "0A" - Periodicidad anual 153-165 Numérico Base Imponible Rectificada: Numérico de 13 posiciones. Se consignará el nuevo importe total de la Base Imponible de las entregas intracomunitarias exentas, si se ha consignado clave de operación E, de las adquisiciones intracomunitarias sujetas, si se ha consignado clave de operación A, de las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, si se ha consignado clave de operación T, de las prestaciones intracomunitarias de servicios realizadas si se ha consignado clave de operación S, y del conjunto de adquisiciones intracomunitarias de servicios si se ha consignado clave de operación I que corresponda al operador intracomunitario y al periodo indicado, una vez modificado el importe de la Base imponible de la operación que se desea rectificar. Por lo tanto, si en un mismo periodo se han realizado varias operaciones con un operador intracomunitario y en una o varias de ellas se quiere rectificar la base imponible que se declaró, se acumularán en un único registro, por clave de operación y periodo, el total de bases imponibles de todas las operaciones una vez rectificadas las bases imponibles que correspondan. Los importes deben consignarse en EUROS. Este campo se subdivide en dos: 153-163 Parte entera del importe de la base imponible rectificada, si no tiene contenido se consignará a ceros. 164-165 Parte decimal del importe de la base imponible rectificada, si no tiene contenido se consignará a ceros. 166-178 Numérico Base imponible declarada anteriormente: Numérico de 13 posiciones. Importe de la Base imponible de la operación que se consignó en la declaración que se corrige. Los importes deben consignarse en EUROS. Este campo se subdivide en dos: 166-176 Parte entera del importe de la base imponible declarada anteriormente, si no tiene contenido se consignará a ceros. 177-178 Parte decimal del importe de la base imponible declarada anteriormente, si no tiene contenido se consignará a ceros. |
| 179-500 | -------------- | BLANCOS. |
| * Todos los importes serán positivos. * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, excepto que se especifique lo contrario en la descripción del campo. |

## CUMPLIMENTACIÓN DEL REGISTRO DE RECTIFICACIONES

El registro de rectificaciones tiene como finalidad que el contribuyente pueda corregir operaciones declaradas en una declaración anterior, cuando se haya incurrido en errores o se hayan producido alteraciones derivadas de las circunstancias a que se refiere el artículo 80 de la Ley del Impuesto sobre el Valor Añadido.

La manera en que se cumplimentará el registro de rectificaciones será diferente dependiendo del error o alteración que se quiera corregir.

A) Cuando únicamente se quiera rectificar el importe de la base imponible debido a que la misma se declaró por un importe erróneo o se ha producido una alteración derivada de las circunstancias a que se refiere el artículo 80 de la Ley del Impuesto sobre el Valor Añadido, se cumplimentará un único registro. El registro de rectificación se cumplimentará respecto a los campos ‘NIF OPERADOR COMUNITARIO’ (posición 76-92), ‘APELLIDOS Y NOMBRE O RAZON SOCIAL DEL OPERADOR INTRACOMUNITARIO’ (posición 93-132) y ‘CLAVE DE OPERACIÓN’ (posición 133) con los mismos datos que los que se consignaron en el registro que ahora se quiere rectificar. Respecto al campo ‘RECTIFICACIONES’ (posiciones 147-178) se consignarán en los subcampos ‘Ejercicio’ (posición 147-150) y ‘Periodo’ (posición 151-152) el ejercicio fiscal y periodo a los que corresponde la declaración que se corrige, respecto al subcampo ‘Base imponible rectificada’ (posición 153-165) se consignará el nuevo importe total de la Base Imponible de las entregas, si se ha consignado clave de operación E, de las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, si se ha consignado clave de operación T, de las adquisiciones, si se ha consignado clave de operación A, de las prestaciones intracomunitarias de servicios realizadas si se ha consignado clave de operación S, y del conjunto de adquisiciones intracomunitarias de servicios si se ha consignado clave de operación I que corresponda al operador intracomunitario y al período indicado, una vez modificado el importe de la Base imponible de la operación que se desea rectificar, y en cuanto al campo ‘Base imponible declarada anteriormente’ (posición 166-178) se consignará el importe que se declaró en la declaración que se corrige. Por lo tanto, si en un mismo período se han realizado varias operaciones con un operador intracomunitario y en una o varias de ellas se quiere rectificar la base imponible que se declaró, se acumularán en un único registro, por clave de operación y período, el total de bases imponibles de todas las operaciones una vez rectificadas las bases imponibles que correspondan.

Ejemplo:

El contribuyente español con NIF: B22222222 consigna en su declaración del ejercicio 2009 y periodo 4T la siguiente operación:

## REGISTRO DE OPERADOR INTRACOMUNITARIO

| Nombre campo | Posiciones | Dato consignado |
| --- | --- | --- |
| TIPO DE REGISTRO | 1 | 2 |
| MODELO EJERCICIO NIF DECLARANTE | 2-4 5-8 9-17 | 349 2009 B22222222 |
| N.I.F. OPERADOR COMUNITARIO | 76-92 | PT123456789 |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL ‘OPERADOR INTRACOMUNITARIO | 93-132 | OPERADOR PORTUGUÉS |
| CLAVE DE OPERACIÓN | 133 | A |
| BASE IMPONIBLE | 134-146 | 0000000123456 |

En enero del 2010 se rescinde una de las adquisiciones que se habían realizado durante el cuarto trimestre del año 2009 con el operador portugués (PT123456789), siendo la nueva base imponible de la totalidad de las adquisiciones realizadas durante dicho periodo de 1000,00 euros. En su declaración del 1T del ejercicio 2010 se consignará el registro de la siguiente manera:

## REGISTRO DE RECTIFICACIONES

| Nombre campo | Posiciones | Dato consignado |
| --- | --- | --- |
| TIPO DE REGISTRO | 1 | 2 |
| MODELO EJERCICIO NIF DECLARANTE | 2-4 5-8 9-17 | 349 2010 B22222222 |
| N.I.F. OPERADOR COMUNITARIO | 76-92 | PT123456789 |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL ‘OPERADOR INTRACOMUNITARIO | 93-132 | OPERADOR PORTUGUÉS |
| CLAVE DE OPERACIÓN | 133 | A |
| EJERCICIO PERIODO BASE IMPONIBLE RECTIFICADA BASE IMPONIBLE DECLARADA ANTERIORMENTE | 147-150 151-152 153-165 166-178 | 2009 4T 0000000100000 0000000123456 |

B) Cuando el campo que desea corregir es el ‘NIF OPERADOR COMUNITARIO’ (posición 76-92), ‘APELLIDOS Y NOMBRE O RAZON SOCIAL DEL OPERADOR INTRACOMUNITARIO’ (posición 93-132) o ‘CLAVE DE OPERACIÓN’ (posición 133), será necesario cumplimentar dos registros de rectificaciones.

El primer registro de rectificación se cumplimentará, respecto a los campos anteriormente mencionados, con los mismos datos que los que se consignaron en el registro que ahora se quiere rectificar. El campo ‘RECTIFICACIONES’ (posiciones 147-178) se cumplimentará de la siguiente manera: en los subcampos ‘Ejercicio’ (posición 147-150) y ‘Periodo’ (posición 151-152) el ejercicio fiscal y periodo a los que corresponde la declaración que se corrige, respecto al subcampo ‘Base imponible rectificada’ (posición 153-165) se rellenará a ceros y en cuanto al subcampo ‘Base imponible declarada anteriormente’ se consignará el importe que se declaró en la declaración que se corrige.

El segundo registro de rectificación se cumplimentará respecto a los campos ‘NIF OPERADOR COMUNITARIO’ (posición 76-92), ‘APELLIDOS Y NOMBRE O RAZON SOCIAL DEL OPERADOR INTRACOMUNITARIO’ (posición 93-132) y ‘CLAVE DE OPERACIÓN’ (posición 133) con los datos corregidos de los errores o alteraciones que se quieren comunicar. Respecto al campo ‘RECTIFICACIONES’ (posiciones 147-178) se consignarán en los subcampos ‘Ejercicio’ (posición 147-150) y ‘Periodo’ (posición 151-152) el ejercicio fiscal y periodo a los que corresponde la declaración que se corrige, respecto al subcampo ‘Base imponible rectificada’ (posición 153-165) se consignará el importe total de la Base Imponible de las entregas, si se ha consignado clave de operación E, de las entregas en otros Estados miembros subsiguientes a adquisiciones intracomunitarias exentas en el marco de operaciones triangulares, si se ha consignado clave de operación T, de las adquisiciones, si se ha consignado clave de operación A, de las prestaciones intracomunitarias de servicios realizadas si se ha consignado clave de operación S, y del conjunto de adquisiciones intracomunitarias de servicios si se ha consignado clave de operación I, que corresponda al operador intracomunitario y al período indicado, y en cuanto a la ‘Base imponible declarada anteriormente’ (posición 166-178) se consignará cero al ser un nuevo registro.

Ejemplo:

El contribuyente español con NIF: B22222222 consigna en su declaración del ejercicio 2009 y periodo 4T la siguiente operación:

## REGISTRO DE OPERADOR INTRACOMUNITARIO

| Nombre campo | Posiciones | Dato consignado |
| --- | --- | --- |
| TIPO DE REGISTRO | 1 | 2 |
| MODELO EJERCICIO NIF DECLARANTE | 2-4 5-8 9-17 | 349 2009 B22222222 |
| N.I.F. OPERADOR COMUNITARIO | 76-92 | PT123456789 |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL ‘OPERADOR INTRACOMUNITARIO | 93-132 | OPERADOR PORTUGUÉS |
| CLAVE DE OPERACIÓN | 133 | A |
| BASE IMPONIBLE | 135-147 | 0000000123456 |

En marzo del 2010 el operador portugués le comunica que su NIF comunitario no es ‘PT123456789’ sino ‘PT987654321’. En su declaración del 1T del ejercicio 2010 será necesario declarar dos registros de rectificaciones. El primero de ellos se consignará de la siguiente manera:

## REGISTRO DE RECTIFICACIONES

| Nombre campo | Posiciones | Dato consignado |
| --- | --- | --- |
| TIPO DE REGISTRO | 1 | 2 |
| MODELO EJERCICIO NIF DECLARANTE | 2-4 5-8 9-17 | 349 2010 B22222222 |
| N.I.F. OPERADOR COMUNITARIO | 76-92 | PT123456789 |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL ‘OPERADOR INTRACOMUNITARIO | 93-132 | OPERADOR PORTUGUÉS |
| CLAVE DE OPERACIÓN | 133 | A |
| EJERCICIO PERIODO BASE IMPONIBLE RECTIFICADA BASE IMPONIBLE DECLARADA ANTERIORMENTE | 147-150 151-152 153-165 166-178 | 2009 4T 0000000000000 00000002000,00 |

El segundo registro se consignará:

## REGISTRO DE RECTIFICACIONES

| Nombre campo | Posiciones | Dato consignado |
| --- | --- | --- |
| TIPO DE REGISTRO | 1 | 2 |
| MODELO EJERCICIO NIF DECLARANTE | 2-4 5-8 9-17 | 349 2010 B22222222 |
| N.I.F. OPERADOR COMUNITARIO | 76-92 | PT987654321 |
| APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL ‘OPERADOR INTRACOMUNITARIO | 93-132 | OPERADOR PORTUGUÉS |
| CLAVE DE OPERACIÓN | 133 | A |
| EJERCICIO PERIODO BASE IMPONIBLE RECTIFICADA BASE IMPONIBLE DECLARADA ANTERIORMENTE | 147-150 151-152 153-165 166-178 | 2009 4T 0000000123456 0000000000000 |

> Se modifica por la disposición final 1 de la Orden EHA/1721/2011, de 16 de junio. Ref. BOE-A-2011-10827

> Téngase en cuenta que esta modificación se aplicará a las declaraciones correspondientes a periodos iniciados a partir del día 1 de julio de 2011, según establece la disposición final 2 de la citada Orden.
