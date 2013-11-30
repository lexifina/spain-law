## ANEXO II

DISEÑOS FÍSICOS Y LÓGICOS A LOS QUE DEBEN AJUSTARSE LOS ARCHIVOS QUE SE GENEREN PARA LA PRESENTACIÓN TELEMÁTICA Y LOS SOPORTES DIRECTAMENTE LEGIBLES POR ORDENADOR DEL MODELO 340

DISEÑOS LÓGICOS A LOS QUE DEBEN AJUSTARSE LOS ARCHIVOS QUE SE GENEREN PARA LA PRESENTACIÓN TELEMÁTICA DEL MODELO 340

A) CARACTERÍSTICAS DE LOS SOPORTES DIRECTAMENTE LEGIBLES POR ORDENADOR.

Los soportes directamente legibles por ordenador para la presentación de la declaración de los Libros Registro regulada en el artículo 36 del Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, habrán de cumplir las siguientes características:

Los soportes directamente legibles por ordenador para la presentación de la información a que se refiere la presente norma habrán de ser:

Tipo: DVD-R o DVD+R.

Capacidad: Hasta 4,7 GB.

Sistema de archivos UDF.

De una cara y una capa simple.

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y pretende presentar declaración de los Libros Registro regulada en el artículo 36 del Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (A.E.A.T.), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la A.E.A.T.

B) DISEÑOS LÓGICOS.

Diseños lógicos para la presentación de la declaración de los Libros Registro regulada en el artículo 36 del Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos.

DESCRIPCIÓN DE LOS REGISTROS

Se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

Tipo 1: Registro de la entidad declarante: Datos identificativos y resumen. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados.

Tipo 2: Registro de detalle. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros de detalle tipo 2 se declaren.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta forma la letra «Ñ» tendrá el valor ASCII 209 (Hex. D1) y la «Ç» (cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_005.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_006.png)

## MODELO 340

## TIPO DE REGISTRO 1: REGISTRO DE LA ENTIDAD DECLARANTE (POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS)

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. |
|  |  | Constante número ‘1’. |
| 2-4 | Numérico. | MODELO. |
|  |  | Constante ‘340’. |
| 5-8 | Numérico. | EJERCICIO. |
|  |  | Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico. | N.I.F. DEL DECLARANTE. |
|  |  | Se consignará el N.I.F. del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos («BOE» de 5 de septiembre). |
| 18-57 | Alfanumérico. | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL DECLARANTE. |
|  |  | Se consignará los apellidos y nombre o razón social del declarante que presenta los Libros Registro de facturas expedidas, recibidas, de bienes de inversión y de determinadas operaciones intracomunitarias. |
|  |  | Si es una persona física, se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo necesariamente en este orden. |
|  |  | Para personas jurídicas y entidades en régimen de atribución de Rentas, se consignará la razón social completa, sin anagrama. |
|  |  | En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético. | TIPO DE SOPORTE. |
|  |  | Se cumplimentará la siguiente clave: |
|  |  | ‘C’: Si la información se presenta en DVD. |
|  |  | ‘T’: Transmisión telemática. |
| 59-107 | Alfanumérico. | PERSONA CON QUIÉN RELACIONARSE. |
|  |  | Datos de la persona con quién relacionarse. Este campo se subdivide en dos: |
|  |  | 59-67 NÚMERO TELÉFONO: Campo numérico de 9 posiciones, el cual se corresponde con el número de teléfono de la persona con quién relacionarse. |
|  |  | 68-107 APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio, y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico. | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN. |
|  |  | Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. Este campo deberá generarse ajustándose al siguiente formato: 340EEEEPPSSSS, donde: |
|  |  | • EEEE: Ejercicio fiscal (Ej.: 2009). |
|  |  | • PP: Se hará constar dos dígitos en función del período al que corresponda la declaración. Se consignará el que corresponda, según la siguiente relación de claves: |
|  |  | «01»: ENERO. |
|  |  | «02»: FEBRERO. |
|  |  | «03»: MARZO y el primer trimestre. |
|  |  | «04»: ABRIL. |
|  |  | «05»: MAYO. |
|  |  | «06»: JUNIO y el segundo trimestre. |
|  |  | «07»: JULIO. |
|  |  | «08»: AGOSTO. |
|  |  | «09»: SEPTIEMBRE y el tercer trimestre. |
|  |  | «10»: OCTUBRE. |
|  |  | «11»: NOVIEMBRE. |
|  |  | «12»: DICIEMBRE y el cuarto trimestre. |
|  |  | • SSSS: Número secuencial consecutivo para cada presentación, comenzando por el 0001. |
| 121-122 | Alfabético. | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. |
|  |  | En el caso excepcional de segunda o posterior presentación de declaraciones deberá cumplimentarle obligatoriamente uno de los siguientes campos: |
|  |  | 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una «C» si la presentación de esta declaración tiene por objeto incluir percepciones que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidas en la misma. |
|  |  | La presentación de una declaración complementaria que tenga por objeto la modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente se realizará desde el servicio de consulta y modificación de declaraciones informativas en la Oficina Virtual de la Agencia Tributaria (www.agenciatributaria.es). |
|  |  | 122 DECLARACIÓN SUSTITUTIVA: Se consignará una «S» si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva solo puede anular a una única declaración anterior. |
| 123-135 | Numérico. | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. |
|  |  | En el caso de que se haya consignado una «C» en el campo «Declaración complementaria» o que se haya consignado «S» en el campo «Declaración sustitutiva», se consignará el número identificativo correspondiente a la declaración a la que sustituye o complementa. |
|  |  | En cualquier otro caso deberá rellenarse a CEROS. |
| 136-137 | Numérico. | PERIODO. |
|  |  | Numérico de dos posiciones. Se hará constar el periodo al que corresponda la declaración. Se consignará el que corresponda según la siguiente relación de claves: |
|  |  | «01»: ENERO. |
|  |  | «02»: FEBRERO. |
|  |  | «03»: MARZO. |
|  |  | «04»: ABRIL. |
|  |  | «05»: MAYO. |
|  |  | «06»: JUNIO. |
|  |  | «07»: JULIO. |
|  |  | «08»: AGOSTO. |
|  |  | «09»: SEPTIEMBRE. |
|  |  | «10»: OCTUBRE. |
|  |  | «11»: NOVIEMBRE. |
|  |  | «12»: DICIEMBRE. |
| 138-146 | Numérico. | NÚMERO TOTAL DE REGISTROS. |
|  |  | Se consignará el número total de registros de detalle del tipo 2 incluidos por la de la entidad declarante que presenta los Libros Registro de facturas expedidas, recibidas, de bienes de inversión y de determinadas operaciones intracomunitarias. |
| 147-164 | Alfanumérico. | IMPORTE TOTAL DE LA BASE IMPONIBLE. |
|  |  | Este campo se subdivide en: |
|  |  | 147 SIGNO: Alfabético. Se cumplimentará cuando el resultado de la suma para obtener el Importe de la Base Imponible (posiciones 148 a 164 de este registro tipo 1) sea menor de 0 (cero). En este caso se consignará una «N». En cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 148-164 IMPORTE: Campo numérico de 17 posiciones. Se consignará la suma de las cantidades (sin coma decimal ni puntuación de miles) reflejadas en los campos BASE IMPONIBLE (posiciones 122-135 correspondientes al registro de tipo 2). En el supuesto de que en los registros de declarados se hubiera consignado «N» en el campo SIGNO DE LA BASE IMPONIBLE (posición 122 del registro de tipo 2), dichas cantidades se computarán con signo menos al totalizar los importes que deben reflejarse en esta suma. Este campo se subdivide en dos: |
|  |  | 148-162 Parte entera del IMPORTE TOTAL DE LAS BASES IMPONIBLES DEL IVA Y DEL IGIC. |
|  |  | 163-164 Parte decimal del IMPORTE TOTAL DE LAS BASES IMPONIBLES IVA Y DEL IGIC. |
| 165-182 | Alfanumérico. | IMPORTE TOTAL DE LA CUOTA DEL IMPUESTO. |
|  |  | Este campo se subdivide en: |
|  |  | 165 SIGNO: Alfabético. |
|  |  | Se cumplimentará cuando el resultado de la suma para obtener el importe TOTAL DE LA CUOTA (posiciones 166 a 182 de este registro tipo 1) sea menor de 0 (cero). En este caso se consignará una «N»; en cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 166-182 IMPORTE. Campo numérico de 17 posiciones. |
|  |  | Se consignará la suma de las cantidades (sin coma decimal ni puntuación de miles) reflejadas en los campos CUOTA DEL IMPUESTO (posiciones 136 a 149 correspondientes al registro de tipo 2). En el supuesto de que en los registros de declarados se hubiera consignado «N» en el campo SIGNO DE LA CUOTA DEL IMPUESTO (posición 136 del registro de tipo 2), dichas cantidades se computarán con signo menos al totalizar los importes que deben reflejarse en esta suma. Este campo se subdivide en dos: |
|  |  | 166-180 Parte entera del IMPORTE TOTAL DE LAS CUOTAS DEL IVA Y DEL IGIC. 181-182 Parte decimal del IMPORTE TOTAL DE LAS CUOTAS DEL IVA Y DEL IGIC. |
| 183-200 | Alfanumérico. | IMPORTE TOTAL DE LAS FACTURAS. |
|  |  | Este campo se subdivide en: |
|  |  | 183 SIGNO: Alfabético. |
|  |  | Se cumplimentará cuando el resultado de la suma para obtener el IMPORTE TOTAL DE LAS FACTURAS (posiciones 184 a 200 de este registro tipo 1) sea menor de 0 (cero). En este caso se consignará una «N»; en cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 184-200 IMPORTE: Campo numérico de 17 posiciones. Se consignará la suma de las cantidades (sin coma decimal ni puntuación de miles) reflejadas en los campos IMPORTE TOTAL DE LA FACTURA (posiciones 150 a 163 correspondientes al registro de tipo 2). En el supuesto de que en los registros de declarados se hubiera consignado «N» en el campo SIGNO DEL IMPORTE TOTAL DE LA FACTURA (posición 150 del registro de tipo 2), dichas cantidades se computarán con signo menos al totalizar los importes que deben reflejarse en esta suma. |
|  |  | Este campo se subdivide en dos: |
|  |  | 184-198 Parte entera del IMPORTE TOTAL DE LAS FACTURAS. |
|  |  | 199-200 Parte decimal del IMPORTE TOTAL DE LAS FACTURAS. |
| 201-390 | – | BLANCOS. |
| 391-399 | Alfanumérico. | N.I.F. DEL REPRESENTANTE LEGAL DEL DECLARANTE. |
|  |  | Para los declarantes menores de 14 años, la identificación de los mismos en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
|  |  | En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 400-415 | Alfanumérico. | CÓDICO ELECTRÓNICO AUTOLIQUIDACIÓN IVA. |
|  |  | Campo reservado para el Código electrónico formado por 16 caracteres alfanuméricos generado por la AEAT en función de los datos incluidos por el declarante en su autoliquidación por vía telemática y que da validez a la autenticidad de la presentación para la declaración del IVA a la que corresponden estos datos de los Libros de Registro de IVA. |
|  |  | El código electrónico se define en la Orden de 20 de enero de 1999 («BOE» de 22 de enero). |
| 416-500 |  | BLANCO. |

* Todos los importes serán positivos.

* Los campos numéricos que no tengan contenido se rellenarán a ceros.

* Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

* Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda.

* Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_007.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_008.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_009.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_010.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_011.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_012.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_013.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/314/20954_014.png)

## MODELO 340

TIPO DE REGISTRO 2: REGISTRO DE DETALLE (POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS)

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. |
|  |  | Constante ‘2’. |
| 2-4 | Numérico. | MODELO. |
|  |  | Constante ‘340’. |
| 5-8 | Numérico. | EJERCICIO. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico. | N.I.F. DE LA ENTIDAD DECLARANTE. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico. | N.I.F. DEL DECLARADO. |
|  |  | Si el destinatario, remitente u obligado a la expedición, en adelante el declarado, dispone de N.I.F. asignado en España, se consignará: |
|  |  | Si es una persona física se consignará el N.I.F. del declarado de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento general de actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos («BOE» de 5 de septiembre). |
|  |  | Si el declarado es una persona jurídica o una entidad en régimen de atribución de rentas (comunidad de bienes, sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. |
|  |  | Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
|  |  | Este campo es incompatible (excluyente) con el campo número de identificación fiscal del declarado asignado en el país o territorio de residencia. |
|  |  | Sólo se cumplimentará con los N.I.F. asignados en España. |
| 27-35 | Alfanumérico. | N.I.F. DEL REPRESENTANTE LEGAL. |
|  |  | Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
|  |  | En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico. | APELLIDOS Y NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN DEL DECLARADO. |
|  |  | a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio, y el nombre completo, necesariamente en este mismo orden. Si el declarado es menor de edad, se consignarán en este campo los apellidos y nombre del menor de edad. En el caso de personas físicas que tengan un solo apellido, se consignará el apellido, un espacio y el nombre, en este orden. |
|  |  | b) Tratándose de personas jurídicas y entidades en régimen de atribución de rentas, se consignará la razón social o denominación completa de la entidad, sin anagramas. |
| 76-77 | Alfabético. | CÓDIGO PAÍS. |
|  |  | Se consignará el código del país o territorio al que corresponde la dirección del declarado, de acuerdo con las claves de países que figuran en la Orden EHA/3202/2008, de 31 de octubre, en su anexo IV («BOE» de 10/11/2008). |
| 78 | Numérico. | CLAVE NÚMERO DE IDENTIFICACIÓN EN EL PAÍS DE RESIDENCIA. |
|  |  | Identifica el contenido del campo «número de identificación fiscal del cliente o proveedor asignado en el país o territorio de residencia». Puede tomar los valores siguientes: |
|  |  | 1. Corresponde a un NIF. |
|  |  | 2. Se consigna el NIF/IVA (NIF OPERADOR INTRACOMUNITARIO). |
|  |  | 3. Pasaporte. |
|  |  | 4. Documento oficial de identificación expedido por el país o territorio de residencia. |
|  |  | 5. Certificado de residencia fiscal. |
|  |  | 6. Otro documento probatorio. |
| 79-98 | Alfanumérico. | NÚMERO DE IDENTIFICACIÓN FISCAL EN EL PAÍS DE RESIDENCIA. |
|  |  | Se consignará el número de identificación fiscal del cliente o proveedor asignado en el país o territorio de residencia. |
|  |  | Este campo es incompatible (excluyente) con el campo NIF del declarado. |
|  |  | En los supuestos de adquisición intracomunitaria de bienes, se consignará el NIF/IVA (NIF OPERADOR INTRACOMUNITARIO). Se compone de los subcampos: |
|  |  | 70-80 Código país: Alfabético de 2 posiciones. Se compone de las dos primeras letras identificativas del Estado miembro de la UE. |
|  |  | 81-95 Número: Alfanumérico de 15 posiciones. Campo alfanumérico, que se ajustará a la izquierda y se rellenará con blancos a la derecha en los casos en que dicho número tenga menos de 15 posiciones. |
|  |  | 96-98 Blancos. |
|  |  | Composición del N.I.F. comunitario de los distintos Estados miembros: |
|  |  | País | Cód. país | Número. |
|  |  | Alemania. | DE | 9 caracteres numéricos. |
|  |  | Austria. | AT | 9 caracteres alfanuméricos. |
|  |  | Bélgica. | BE | 9 o 10 caracteres numéricos. |
|  |  | Bulgaria. | BG | 9 o 10 caracteres numéricos. |
|  |  | Croacia | HR | 11 caracteres numéricos. |
|  |  | Chipre. | CY | 9 caracteres numéricos. |
|  |  | Chequia. | CZ | 8, 9 o 10 caracteres numéricos. |
|  |  | Dinamarca. | DK | 8 caracteres numéricos. |
|  |  | Estonia. | EE | 9 caracteres numéricos. |
|  |  | Finlandia. | FI | 8 caracteres numéricos. |
|  |  | Francia | FR | 11 caracteres alfanuméricos. |
|  |  | Grecia. | EL | 9 caracteres numéricos. |
|  |  | Gran Bretaña. | GB | 5, 9 o 12 caracteres alfanuméricos. |
|  |  | Holanda. | NL | 12 caracteres alfanuméricos. |
|  |  | Hungría. | HU | 8 caracteres numéricos. |
|  |  | Italia. | IT | 11 caracteres numéricos. |
|  |  | Irlanda. | IE | 8 ó 9 caracteres alfanuméricos. |
|  |  | Lituania. | LT | 9 o 12 caracteres numéricos. |
|  |  | Luxemburgo. | LU | 8 caracteres numéricos. |
|  |  | Letonia. | LV | 11 caracteres numéricos. |
|  |  | Malta. | MT | 8 caracteres numéricos. |
|  |  | Polonia. | PL | 10 caracteres numéricos. |
|  |  | Portugal. | PT | 9 caracteres numéricos. |
|  |  | Rumanía. | RO | 2, 3, 4, 5, 6, 7, 8, 9 o 10 caracteres numéricos. |
|  |  | Suecia. | SE | 12 caracteres numéricos. |
|  |  | Eslovenia. | SI | 8 caracteres numéricos. |
|  |  | Eslovaquia. | SK | 10 caracteres numéricos. |
| 99 | Alfabético. | CLAVE TIPO DE LIBRO. |
|  |  | E Libro registro de facturas expedidas. |
|  |  | I Libro registro de bienes de invención. |
|  |  | R Libro registro de facturas recibidas. |
|  |  | U Libro registro de determinadas operaciones intracomunitarias. |
|  |  | F Libro registro de facturas expedidas IGIC. |
|  |  | J. Libro de registro de bienes de inversión IGIC. |
|  |  | S. Libro de registro de facturas recibidas IGIC. |
| 100 | Alfanumérico | CLAVE DE OPERACIÓN. |
|  |  | La clave que corresponda: |
|  |  | A Asiento resumen de facturas. |
|  |  | B Asiento resumen de tique. |
|  |  | C Factura con varios asientos (varios tipos impositivos). |
|  |  | D Factura rectificativa. |
|  |  | F Adquisiciones realizadas por las agencias de viajes directamente en interés del viajero (Régimen especial de agencias de viajes). |
|  |  | G Régimen especial de grupo de entidades en IVA o IGIC (incorpora la contraprestación real a coste). |
|  |  | H Régimen especial de oro de inversión. |
|  |  | I Inversión del sujeto pasivo (ISP). |
|  |  | J Tiques. |
|  |  | K Rectificación de errores registrales. |
|  |  | L Adquisiciones a comerciantes minoristas del IGIC. |
|  |  | Ninguna de las anteriores. |
|  |  | Si este campo viene a blanco se considerará que corresponde con «Ninguna de las anteriores». |
|  |  | La anotación individualizada de las facturas o documentos sustitutivos se podrá sustituir por la de asientos resúmenes en los que se harán constar la fecha o periodo en que se hayan expedido, base imponible global, el tipo impositivo, la cuota global de facturas o documentos sustitutivos numerados correlativamente y expedidos en la misma fecha, y los números inicial y final de los documentos anotados, siempre que se cumplan simultáneamente los requisitos establecidos en el apartado 4 del artículo 63 Reglamento del IVA o en el artículo 31.4 del Decreto 182/1992 del IGIC. |
|  |  | Podrá hacerse un asiento resumen global de las facturas recibidas en una misma fecha, en el que se harán constar los números inicial y final de las facturas recibidas asignados por el destinatario, siempre que procedan de un único proveedor, la suma global de la base imponible y la cuota impositiva global, siempre que el importe total conjunto de las operaciones, Impuesto sobre el Valor Añadido o Impuesto General Indirecto Canario no incluido, no exceda de 6.000 euros, y que el importe de las operaciones documentadas en cada una de ellas no supere 500 euros, Impuesto sobre el Valor Añadido no incluido. |
|  |  | Igualmente será válida la anotación de una misma factura en varios asientos correlativos cuando incluya operaciones que tributen a distintos tipos impositivos. |
|  |  | Con carácter voluntario, se podrán consignar, asimismo, las claves siguientes: |
|  |  | E IVA/IGIC devengado pendiente de emitir factura. |
|  |  | M IVA/IGIC facturado pendiente de devengar (emitida factura). |
|  |  | N Facturación de las prestaciones de servicios de agencias de viaje que actúan como mediadoras en nombre y por cuenta ajena (disposición adicional 4.ª RD 1496/2003). Deberá consignarse de forma obligatoria cuando se realicen operaciones que se correspondan con la misma. |
|  |  | O Factura emitida en sustitución de tiques facturados y declarados. |
|  |  | P Adquisiciones intracomunitarias de bienes. |
|  |  | Q Operaciones a las que se aplique el Régimen especial de bienes usados, objetos de arte, antigüedades y objetos de colección según los artículos del 135 al 139 de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido. |
|  |  | R–Operación de arrendamiento de local de negocio. |
|  |  | S–Subvenciones, auxilios o ayudas satisfechas o recibidas, tanto por parte de Administraciones públicas como de entidades privadas. |
|  |  | T–Cobros por cuenta de terceros de honorarios profesionales o de derechos derivados de la propiedad intelectual, industrial, de autor u otros por cuenta de sus socios, asociados o colegiados efectuados por sociedades, asociaciones, colegios profesionales u otras entidades que, entre sus funciones, realicen las de cobro. |
|  |  | U–Operación de seguros. |
|  |  | V–Compras de agencias viajes: operaciones de prestación de servicios de mediación en nombre y por cuenta ajena relativos a los servicios de transporte de viajeros y de sus equipajes que las agencias de viajes presten al destinatario de dichos servicios de transporte, de acuerdo con lo dispuesto en el apartado 3 de la disposición adicional cuarta del Reglamento por el que se regulan las obligaciones de facturación. |
|  |  | W–Operaciones sujetas al Impuesto sobre la Producción, los Servicios y la Importación en las Ciudades de Ceuta y Melilla. |
|  |  | X–Operaciones por las que los empresarios o profesionales que satisfagan compensaciones agrícolas, ganaderas y/o pesqueras hayan expedido el recibo correspondiente. |
|  |  | Z: Régimen especial del criterio de caja. |
|  |  | Claves numéricas de carácter voluntario: |
|  |  | 1: IVA criterio de caja. Asiento resumen de facturas. |
|  |  | 2: IVA criterio de caja. Factura con varios asientos (varios tipos impositivos). |
|  |  | 3: IVA criterio de caja. Factura rectificativa. |
|  |  | 4: IVA criterio de caja. Adquisiciones realizadas por las agencias de viajes directamente en interés del viajero (Régimen especial de agencia de viajes). |
|  |  | 5: IVA criterio de caja. Factura simplificada. |
|  |  | 6: IVA criterio de caja. Rectificación de errores registrales. |
|  |  | 7: IVA criterio de caja. Facturación de las prestaciones de servicios de agencias de viaje que actúan como mediadoras en nombre y por cuenta ajena. (Disposición adicional 4.ª RD 1496/2003). |
|  |  | 8: IVA criterio de caja. Operación de arrendamiento de local de negocio. |
| 101-108 | Numérico. | FECHA DE LA EXPEDICIÓN. |
|  |  | Se consignará la fecha de la expedición de la factura, indicando los cuatro dígitos del año, los dos del mes (de 01 a 12) y los dos del día (de 01 a 31) con el formato AAAAMMDD. |
| 109-116 | Numérico. | FECHA DE LA OPERACIÓN. |
|  |  | En función del tipo de libro registro se consignará la fecha de la realización de la operación (facturas expedidas y facturas recibidas), la de comienzo de uso del bien (bienes de inversión), indicando los cuatro dígitos del año, los dos del mes (de 01 a 12) y los dos del día (de 01 a 31) con el formato AAAAMMDD. |
| 117-121 | Numérico. | TIPO IMPOSITIVO. |
|  |  | Se consignará el tipo de gravamen aplicable. Este campo se subdivide en otros dos: |
|  |  | 117-119 ENTERO Numérico. Parte entera: Se consignará la parte entera del tipo de gravamen (si no tiene, consignar CEROS). |
|  |  | 120-121 DECIMAL Numérico. Parte decimal: Se consignará la parte decimal del tipo de gravamen (si no tiene, consignar CEROS). |
| 122-135 | Alfanumérico. | BASE IMPONIBLE. |
|  |  | Se consignará la Base Imponible del Impuesto en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. En las de operaciones de la clave A o B (asiento resumen) se consignará la Base Imponible Global. Asimismo, en los supuestos de operaciones de Rectificación (facturas rectificativas), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 122 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 123-135 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: 123-133 Parte entera de la Base Imponible del Impuesto. 134-135 Parte decimal de la Base Imponible del Impuesto. |
| 136-149 | Alfanumérico. | CUOTA DEL IMPUESTO. |
|  |  | Se consignará la Cuota del Impuesto repercutida o soportada en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimos. En las de operaciones de la clave A o B (asiento resumen) se consignará la Cuota Global. Asimismo, en los supuestos de operaciones de rectificación (facturas rectificativas), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 136 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una N. En cualquier otro caso se rellenará a blancos. |
|  |  | 137-149 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 137-147 Parte entera de la cuota del Impuesto. 148-149 Parte decimal de la Cuota del Impuesto. |
| 150-163 | Alfanumérico. | IMPORTE TOTAL DE LA FACTURA. |
|  |  | Se consignará el importe total de la factura, resultado de la suma de Base imponible y de la Cuota del Impuesto en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. En las de operaciones de la clave A o B (asiento resumen) se consignara Importe Global de la facturación. Asimismo, en los supuestos de operaciones de rectificación(facturas rectificativas, devolución de mercancías y rapels), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 150 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 151-163 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 151-161 Parte entera del importe total de la factura. 162-163 Parte decimal del importe total de la factura. |
| 164-177 | Alfanumérico. | BASE IMPONIBLE A COSTE. |
|  |  | El importe a consignar estará constituido por el coste de los bienes y servicios utilizados directa o indirectamente, total o parcialmente, en su realización y por los cuales se haya soportado o satisfecho efectivamente el Impuesto en los supuestos de clave de operación G «Régimen especial de grupo de entidades en IVA o IGIC», posición 100, en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992 de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimos, En las de operaciones de la clave A o B (asiento resumen) se consignará la Base Imponible Global. Asimismo, en los supuestos de operaciones de rectificación (facturas rectificativas), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 164 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 165-167 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. |
|  |  | Este campo se subdivide en dos: |
|  |  | 165-175 Parte entera de la Base Imponible a Coste. |
|  |  | 176-177 Parte decimal de la Base Imponible a Coste. |
| 178-217 | Alfanumérico. | IDENTIFICACIÓN DE LA FACTURA. |
|  |  | Se consignará la identificación de las facturas o documentos sustitutivos expedidos, incluyendo la serie en su caso. |
| 218-235 | Alfanumérico. | NÚMERO DE REGISTRO. |
|  |  | Se consignará el número correlativo que corresponda al asiento en el correspondiente libro registro de IVA o IGIC. |

LIBRO REGISTRO DE FACTURAS EXPEDIDAS

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 236-243 | Numérico. | NÚMERO DE FACTURAS. |
|  |  | Número de facturas o tiques acumulados que corresponden al registro. La acumulación se realizará por cada intervalo continuo de emisión de los mismos (correlativos), y en los supuestos de operaciones distintas a las de la clave A o B (asiento resumen), se consignará uno. |
| 244-245 | Numérico. | NÚMERO DE REGISTROS (DESGLOSE). |
|  |  | En los supuestos de la clave de operación C «Factura con varios asientos (varios tipos impositivos)», se consignará el número de registros en los cuales se declara. En los supuestos de operaciones distintas a la clave C (Factura con varios asientos, distintos tipos impositivos) se consignará uno. |
| 246-325 | Alfanumérico. | INTERVALO DE IDENTIFICACIÓN DE LA ACUMULACIÓN. |
|  |  | Se consignará para los supuestos de acumulación de facturas o tiques en un solo registro, y dado que dicha numeración ha de ser correlativa (intervalo continuo de emisión), se anotará el número primero y último de dicha relación correlativa. Este campo se subdivide en dos: |
|  |  | 246-285 PRIMER NÚMERO: Se consignará el primer número de la correlación del día objeto de declaración (si no tiene, consignar BLANCOS). |
|  |  | 286-325 ÚLTIMO NÚMERO: Se consignará el último número de la correlación del día objeto de declaración (si no tiene, consignar BLANCOS). |
| 326-365 | Alfanumérico. | IDENTIFICACIÓN DE LA FACTURA RECTIFICADA. |
|  |  | Se consignarán la identificación de la factura o documentos sustituidos como consecuencia de la rectificación. |
| 366-370 | Numérico. | TIPO EL RECARGO DE EQUIVALENCIA. |
|  |  | Se consignará el tipo de recargo de equivalencia aplicable. Este campo se subdivide en otros dos: |
|  |  | 366-368 ENTERO Numérico. Parte entera: Se consignará la parte entera del tipo de recargo de equivalencia (si no tiene, consignar CEROS). |
|  |  | 369-370 DECIMAL Numérico. Parte decimal: Se consignará la parte decimal del tipo de recargo de equivalencia (si no tiene, consignar CEROS). |
| 371-384 | Alfanumérico. | CUOTA DEL RECARGO DE EQUIVALENCIA. |
|  |  | Se consignará la Cuota del recargo de equivalencia en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. Asimismo, en los supuestos de operaciones de rectificación (facturas rectificativas), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 371 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una N. En cualquier otro caso se rellenará a blancos. |
|  |  | 372-384 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 372-382 Parte entera de la Cuota del recargo de equivalencia. |
|  |  | 383-384 Parte decimal de la Cuota del recargo de equivalencia. |
| 385 | Numérico | Situación del inmueble. |
|  |  | Cuando se consigne la clave de operación ''R'' se consignará de entre las siguientes claves la que corresponda a la situación del local de negocio arrendado: 1. Inmueble con referencia catastral situado en cualquier punto del territorio español, excepto País Vasco y Navarra. 2. Inmueble situado en la Comunidad Autónoma del País Vasco o en la Comunidad Foral de Navarra. 3. Inmueble en cualquiera de las situaciones anteriores pero sin referencia catastral. 4. Inmueble situado en el extranjero. |
| 386-410 | Alfanumérico | Referencia catastral. |
|  |  | Cuando se consigne la clave ''R'' se consignará la referencia catastral correspondiente al local de negocio arrendado. |
| 411-425 | Numérico | Importe percibido en metálico. |
|  |  | Se consignarán sin signo y sin coma decimal los importes superiores a 6.000 euros que se hubieran percibido en metálico (moneda o billetes de curso legal) de la misma persona o entidad por las operaciones realizadas durante el año natural. Estos importes se reflejarán en las declaraciones mensuales a partir de las cuales se haya superado el citado límite. Cuando las cantidades percibidas en metálico previstas no puedan incluirse en las declaraciones mensuales del año natural en el que se realizan las operaciones por percibirse con posterioridad a su presentación o por no haber alcanzado en ese momento un importe superior a 6.000 euros, los obligados tributarios deberán incluirlas separadamente en la declaración correspondiente al período del año natural posterior en el que se hubiese efectuado el cobro o se hubiese alcanzado el importe señalado anteriormente. Los importes deben consignarse en euros. Este campo se subdivide en dos: |
|  |  | 411-423 Parte entera del importe percibido en metálico, si no tiene contenido se consignará a ceros. |
|  |  | 424-425 Parte decimal del importe percibido en metálico, si no tiene contenido se consignará a ceros. |
| 426-429 | Numérico | Ejercicio. |
|  |  | Se consignarán las cuatro cifras del ejercicio en el que se hubieran declarado las operaciones que dan origen al cobro en metálico por importe superior a 6.000 euros. |
| 430-444 | Numérico | Importe percibido por transmisiones de inmuebles sujetas a IVA. |
|  |  | Se consignará, sin signo y sin coma decimal, separadamente de otras operaciones, las cantidades que se perciban en contraprestación por transmisiones de inmuebles, efectuadas o que se deban efectuar, que constituyan entregas sujetas en el Impuesto sobre el Valor añadido (IVA incluido). Los importes deben consignarse en euros. Este campo se subdivide en dos: |
|  |  | 430-442 Parte entera del importe percibido por transmisiones de inmuebles sujetas a IVA, si no tiene contenido se consignará a ceros. |
|  |  | 443-444 Parte decimal del importe percibido por transmisiones de inmuebles sujetas a IVA, si no tiene contenido se consignará a ceros. |
| 445-452 | Numérico. | FECHA DE COBRO. |
|  |  | Cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar la fecha en la que se hubiera producido el devengo conforme al criterio de devengo del Régimen especial del criterio de caja. Este campo se subdivide en otros tres: |
|  |  | 445-448 Numérico AÑO |
|  |  | 449-450 Numérico MES |
|  |  | 451-452 Numérico DÍA |
| 453-465 | Numérico. | IMPORTES COBRADOS. |
|  |  | Se consignarán sin coma decimal los importes devengados correspondientes a facturas expedidas cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2. Los importes deben consignarse en euros. Este campo se subdivide en dos: |
|  |  | 453-463 Numérico. Parte entera del importe cobrado, si no tiene contenido se consignará a ceros. |
|  |  | 464-465 Numérico. Parte decimal del importe cobrado, si no tiene contenido se consignará a ceros. |
| 466 | Alfabético. | MEDIO DE COBRO UTILIZADO. |
|  |  | Cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar en este campo una de las siguientes claves identificativas del medio de cobro utilizado: "Cˮ – Cuenta bancaria. "Tˮ – Cheque. "Oˮ – Otros medios de cobro. Este campo no se cumplimentará cuando no se hubiera producido ningún cobro. |
| 467-500 | Alfanumérico. | CUENTA BANCARIA O MEDIO DE COBRO UTILIZADO. |
|  |  | Cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar en este campo el medio de cobro parcial o total de la operación, ya bien sea el número de cuenta bancaria o el número de cheque a través del cual se hubiera realizado el cobro si se consignó la clave "Cˮ o la clave "Tˮ respectivamente en el campo "MEDIO DE COBRO UTILIZADOˮ (posición 466). Del mismo modo se cumplimentará la descripción o identificación de cualquier otro medio utilizado que pueda acreditar el cobro si se consignó la clave "Oˮ del campo anterior. Este campo no se cumplimentará cuando no se hubiera producido ningún cobro. |

LIBRO REGISTRO DE FACTURAS RECIBIDAS

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 236-253 | Numérico. | NÚMERO DE FACTURAS. |
|  |  | Número de facturas o tiques acumulados que corresponden al registro. La acumulación se realizará por cada intervalo continuo de emisión de los mismos (correlativos), y en los supuestos de operaciones distintas a las de la clave A o B (asiento resumen), se consignará uno. |
| 254-255 | Numérico. | NÚMERO DE REGISTROS (DESGLOSE). |
|  |  | En los supuestos de la clave de operación C «con varios asientos (varios tipos impositivos)», se consignará el número de registros en los cuales se declara. En los supuestos de operaciones distintas a la clave C (Factura con varios asientos, distintos tipos impositivos) se consignará uno. |
| 256-335 | Alfanumérico. | INTERVALO DE IDENTIFICACIÓN DE LA ACUMULACIÓN. |
|  |  | Se consignará para los supuestos de acumulación de facturas o tiques en un solo registro, y dado que dicha numeración ha de ser correlativa (intervalo continuo de emisión), se anotará el número primero y ultimo de dicha relación correlativa. Este campo se subdivide en otros dos: |
|  |  | 256-295 PRIMER NÚMERO: Se consignará el primer número de la correlación del día objeto de declaración (si no tiene, consignar BLANCOS). |
|  |  | 296-335 ÚLTIMO NÚMERO: Se consignará el ultimo número de la correlación del día objeto de declaración (si no tiene, consignar BLANCOS). |
| 336-349 | Alfanumérico. | CUOTA DEDUCIBLE. |
|  |  | Campo de configuración voluntaria, en el cual se incluirá el importe de la cuota deducible según la normativa del impuesto. Coincidirá con la cuota del impuesto soportada en los supuestos en que la cuota sea deducible en su totalidad. |
|  |  | Se consignará la Cuota Deducible en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. Asimismo, en los supuestos de operaciones de rectificación (facturas rectificativas), se consignará el signo que corresponda en función de la corrección a efectuar. |
|  |  | 336 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 337-349 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 337-347 Parte entera de la Cuota Soportada del Impuesto. |
|  |  | 348-349 Parte decimal de la Cuota Soportada del Impuesto. |
| 350-357 | Numérico. | FECHA DE PAGO. |
|  |  | Cuando se consigne la clave "Z" o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar la fecha en la que se hubiera producido el devengo conforme al criterio de devengo del Régimen especial del criterio de caja. Este campo se subdivide en otros tres: |
|  |  | 350-353 Numérico AÑO |
|  |  | 354-355 Numérico MES |
|  |  | 356-357 Numérico DÍA |
| 358-370 | Numérico. | IMPORTES PAGADOS. |
|  |  | Se consignarán sin coma decimal los importes devengados correspondientes a facturas recibidas cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2. Los importes deben consignarse en euros. Este campo se subdivide en dos: |
|  |  | 358-368 Numérico. Parte entera del importe pagado, si no tiene contenido se consignará a ceros. |
|  |  | 369-370 Numérico. Parte decimal del importe pagado, si no tiene contenido se consignará a ceros. |
| 371 | Alfabético. | MEDIO DE PAGO UTILIZADO. |
|  |  | Cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar en este campo una de las siguientes claves identificativas del medio de pago utilizado: "Cˮ – Cuenta bancaria. "Tˮ – Cheque. "Oˮ – Otros medios de pago. Este campo no se cumplimentará cuando no se hubiera producido ningún pago. |
| 372-405 | Alfanumérico. | CUENTA BANCARIA O MEDIO DE PAGO UTILIZADO. |
|  |  | Cuando se consigne la clave "Zˮ o cualquiera de las claves numéricas del campo "CLAVE DE OPERACIÓNˮ, posición 100 de los diseños lógicos del tipo de registro 2, se hará constar en este campo el medio de pago parcial o total de la operación, ya bien sea el número de cuenta bancaria o el número de cheque a través del cual se hubiera realizado el cobro si se consignó la clave "Cˮ o la clave "Tˮ respectivamente en el campo "MEDIO DE PAGO UTILIZADO" (posición 371). Del mismo modo se cumplimentará la descripción o identificación de cualquier otro medio utilizado que pueda acreditar el pago si se consignó la clave "Oˮ del campo anterior. Este campo no se cumplimentará cuando no se hubiera producido ningún pago. |

LIBRO REGISTRO DE BIENES DE INVERSIÓN

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 236-238 | Numérico. | PRORRATA ANUAL DEFINITIVA. |
|  |  | Se consignará la prorrata anual definitiva aplicable. |
| 239-252 | Alfanumérico. | REGULARIZACIÓN ANUAL DE LA DEDUCCIÓN. |
|  |  | Se consignará la regularización anual de la deducción en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. |
|  |  | 239 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 240-252 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 240-250 Parte entera de la regularización anual de la deducción. |
|  |  | 251-252 Parte decimal de la regularización anual de la deducción. |
| 253-292 | Alfanumérico. | IDENTIFICACIÓN DE LA ENTREGA. |
|  |  | Se consignarán la identificación de la factura que corresponde en el LIBRO REGISTRO DE FACTURAS EXPEDIDAS que recoge la entrega. |
| 293-306 | Alfanumérico. | REGULARIZACIÓN DE LA DEDUCCIÓN EFECTUADA (TRANSMISIONES). |
|  |  | Se consignará la regularización de la deducción efectuada con motivo de la transmisión del bien en euros o su contravalor, en los casos de operaciones en divisas, según el artículo 79.once de la Ley 37/1992, de 28 de diciembre, del Impuesto sobre el Valor Añadido, y el artículo 23.8 de la Ley 20/1991, de 7 de junio, de modificación de los aspectos fiscales del Régimen Económico Fiscal de Canarias, sin signo y sin céntimo. |
|  |  | 293 SIGNO: Alfabético. Si el importe descrito anteriormente es negativo, se consignará una «N». En cualquier otro caso se rellenará a blancos. |
|  |  | 294-306 IMPORTE: Campo numérico de 13 posiciones. Se consignará (sin coma decimal ni puntuación de miles) el importe descrito anteriormente. Este campo se subdivide en dos: |
|  |  | 294-304 Parte entera de la regularización de la deducción efectuada con motivo de la transmisión del bien. |
|  |  | 305-306 Parte decimal de la regularización de la deducción efectuada con motivo de la transmisión del bien. |
| 307-314 | Numérico. | FECHA DE INICIO DE LA UTILIZACIÓN. |
|  |  | Se consignará la fecha del inicio del uso del bien, indicando los cuatro dígitos del año, los dos del mes (de 01 a 12) y los dos del día (de 01 a 31) con el formato AAAAMMDD. |
| 315-331 | Alfanumérico. | IDENTIFICACIÓN DEL BIEN. |
|  |  | Se consignará la descripción del bien objeto de este libro registro de IVA o IGIC. |
| 332-500 |  | BLANCO. |

LIBRO REGISTRO DE DETERMINADAS OPERACIONES INTRACOMUNITARIAS

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 236 | Alfabético. | TIPO DE OPERACIÓN INTRACOMUNITARIA. |
|  |  | Se consignará el tipo de operación intracomunitaria que corresponda: |
|  |  | A. El envío o recepción de bienes para la realización de los informes periciales o trabajos mencionados en el artículo 70, apartado uno, número 7.º, de la Ley del Impuesto (Ley 37/1992). |
|  |  | B. Las transferencias de bienes y las adquisiciones intracomunitarias de bienes comprendidas en los artículos 9, apartado 3.º, y 16, apartado 2.º, de la Ley del Impuesto (Ley 37/1992). |
| 237 | Alfabético. | CLAVE DE DECLARADO. |
|  |  | En función de la condición del declarado, se consignará una de las siguientes claves: |
|  |  | D Destinatario. |
|  |  | R Remitente. |
| 238-239 | Alfabético. | CÓDIGO DEL ESTADO MIEMBRO. |
|  |  | En los supuestos de los registros correspondientes al Libro registro de determinadas operaciones intracomunitarias, se cumplimentará el código del Estado miembro de la UE origen o destino de los bienes, de acuerdo con las claves de países que figuran en la Orden EHA/3202/2008, de 31 de octubre, en su Anexo IV («BOE» de 10/11/2008). |
| 240-242 | Numérico. | PLAZO DE LA OPERACIÓN. |
|  |  | En los supuestos de los registros correspondientes al Libro registro de determinadas operaciones intracomunitarias, se cumplimentará el plazo en días para la realización de las operaciones. |
| 243-277 | Alfanumérico | DESCRIPCIÓN DE LOS BIENES. |
|  |  | En los supuestos de los registros correspondientes al Libro registro de determinadas operaciones intracomunitarias, se consignara la descripción de los bienes objeto de la operación con referencia a la correspondiente factura. |
| 278-349 | Alfanumérico | DIRECCIÓN DEL OPERADOR INTRACOMUNITARIO. |
|  |  | Se consignará la dirección del operador intracomunitario contrapartida del residente en España. |
|  |  | Este campo se subdivide en: |
|  |  | 278-317 DOMICILIO. Se consignará el domicilio (calle, número, etc.). |
|  |  | 318-339 POBLACIÓN. Se consignará el nombre de Población/Ciudad. |
|  |  | 340-349 CÓDIGO POSTAL. Se consignará el Código Postal (ZIP code). |
| 350-484 | Alfanumérico | OTRAS FACTURAS O DOCUMENTACIÓN. |
|  |  | En los supuestos de los registros correspondientes al Libro Registro de determinadas operaciones intracomunitarias se consignarán los datos de «Otras facturas o documentación relativas a las operaciones de que se trate» (art 66.2.3.º RIVA). |
| 485-500 |  | BLANCOS. |

* Todos los importes será positivos.

* Los campos numéricos que no tengan contenido se rellenarán a ceros.

* Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

* Todos los campos numéricos ajustados a la derecha y rellenos a ceros por la izquierda

* Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.

> Se modifica por el art. 3.2 y 3 de la Orden HAP/2215/2013, de 26 de noviembre. Ref. BOE-A-2013-12489.

> Se modifica por el art. 2.2 a 4 de la Orden EHA/3378/2011, de 1 de diciembre. Ref. BOE-A-2011-19397.
