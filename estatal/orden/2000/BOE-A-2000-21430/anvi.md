## ANEXO VI

## DISEÑOS FÍSICOS Y LÓGICOS A LOS QUE DEBEN AJUSTARSE LOS ARCHIVOS QUE SE GENEREN PARA LA PRESENTACIÓN TELEMÁTICA Y LOS SOPORTES DIRECTAMENTE LEGIBLES POR ORDENADOR DEL MODELO 180

A) Características de los soportes magnéticos.

Los soportes directamente legibles por ordenador para la presentación del resumen anual de retenciones e ingresos a cuenta sobre determinadas rentas o rendimientos procedentes del arrendamiento o subarrendamiento de inmuebles urbanos del Impuesto sobre la Renta de las Personas Físicas, del Impuesto sobre Sociedades y del Impuesto sobre la Renta de no Residentes, correspondiente a establecimientos permanentes (Modelo 180) habrán de cumplir las siguientes características:

– Tipo: DVD-R o DVD+R.

– Capacidad: Hasta 4,7 GB.

– Sistema de archivos UDF.

– De una cara y una capa simple.

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y pretende presentar el resumen anual de retenciones e ingresos a cuenta sobre determinadas rentas o rendimientos procedentes del arrendamiento o subarrendamiento de inmuebles urbanos del Impuesto sobre la Renta de las Personas Físicas, del Impuesto sobre Sociedades y del Impuesto sobre la Renta de no Residentes, correspondiente a establecimientos permanentes (Modelo 180) en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (A.E.A.T.), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la A.E.A.T.

B) Diseños lógicos.

Descripción de los registros.

Para cada declarante se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

Tipo 1: Registro del declarante: Datos identificativos y resumen de la declaración. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

Tipo 2: Registro de perceptor. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros del tipo 2 como perceptores tenga la declaración.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta forma la letra «Ñ» tendrá el valor ASCII 209 (Hex. D1) y la «Ç» (cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

El primer registro del fichero (tipo 1), contendrá un campo de 13 caracteres, en las posiciones 488 a 500, reservado para el sello electrónico, que será cumplimentado exclusivamente por los programas oficiales de la A.E.A.T. En cualquier otro caso se rellenará a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2014/234/09740_13858697_image1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2014/234/09740_13858697_image2.png)

## MODELO 180

TIPO DE REGISTRO 1: REGISTRO DE DECLARANTE

(Posiciones, naturaleza y descripción de los campos)

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. |
|  |  | Constante «1». |
| 2-4 | Numérico. | MODELO DECLARACIÓN. |
|  |  | Constante «180». |
| 5-8 | Numérico. | EJERCICIO. |
|  |  | Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico. | N.I.F. DEL DECLARANTE. |
|  |  | Se consignará el NIF del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007 de 27 de Julio (BOE del 5 de septiembre). |
| 18-57 | Alfanumérico. | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL DECLARANTE. |
|  |  | Si es una persona física se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. Para personas jurídicas y entidades sin personalidad jurídica, se consignará la razón social completa o denominación, sin anagrama. En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético. | TIPO DE SOPORTE. |
|  |  | Se cumplimentará una de las siguientes claves: «C»: Si la información se presenta en cinta magnética. «T»: Transmisión telemática |
| 59-107 | Alfanumérico. | PERSONA CON QUIÉN RELACIONARSE. |
|  |  | Datos de la persona con quién relacionarse. Este campo se subdivide en dos: 59-67 TELÉFONO: Campo numérico de 9 posiciones. 68-107 APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico. | NÚMERO DE IDENTIFICATIVO DE LA DECLARACIÓN. |
|  |  | Se consignará el número identificativo correspondiente a la declaración. El número identificativo de la declaración que habrá de figurar en el modelo 180 en euros, será un número secuencial cuyos tres primeros dígitos se corresponderán con el código 180. |
| 121-122 | Alfabético. | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. |
|  |  | En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarse obligatoriamente uno de los siguientes campos: 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una «C» si la presentación de esta declaración tiene por objeto incluir nuevos registros de tipo 2 que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidas en la misma. La modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente, se realizará desde el servicio de consulta y modificación de declaraciones informativas en la Oficina Virtual de la Agencia Tributaria (www.agenciatributaria.gob.es). 122 DECLARACIÓN SUSTITUTIVA: Se consignará una «S» si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico. | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. |
|  |  | Únicamente en el caso de que se haya consignado «S» en el campo «Declaración sustitutiva», se consignará el número identificativo correspondiente a la declaración a la que sustituye. Campo de contenido numérico de 13 posiciones. En cualquier otro caso deberá rellenarse a CEROS. |
| 136-144 | Numérico. | NÚMERO TOTAL DE PERCEPTORES. |
|  |  | Se consignará el número total de perceptores declarados en el soporte para este declarante. Si un mismo perceptor figura en varios registros, se computará tantas veces como figure relacionado. (Número de registros de tipo 2). |
| 145-160 | Alfanumérico. | BASE RETENCIONES E INGRESOS A CUENTA. |
|  |  | Se consignará la suma total de las cantidades reflejadas en el campo «BASE DE RETENCIONES E INGRESOS A CUENTA» (posiciones 80 a 92) correspondientes a los registros de tipo 2. Este campo se subdivide en dos: 145 SIGNO: campo alfabético, que se cumplimentará cuando el resultado de la suma para obtener el importe de las bases de retenciones e ingresos a cuenta (posiciones 146 a 160 de este registro de tipo 1) sea menor de 0 (cero). En este caso se consignará una «N», en cualquier otro caso el contenido de este campo será un espacio. 146-160 IMPORTE: campo numérico en el que se consignará la suma de las cantidades reflejadas en el campo «BASE DE RETENCIONES E INGRESOS A CUENTA» (posición 80 a 92, correspondientes a los registros de percepciones), con independencia de la clave de modalidad a la que correspondan. En el supuesto de que en los registros de perceptores se hubiera consignado «N» en el campo «SIGNO DE LA BASE DE RETENCIONES E INGRESOS A CUENTA», (posición 79 del registro de tipo 2), por corresponder al reintegro de percepciones indebida o excesivamente satisfechas en ejercicios anteriores, dichas cantidades se computarán igualmente con signo menos al totalizar los importes que deben reflejarse en esta suma. 146-159 Parte entera del importe total de las bases de retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. 159-160 Parte decimal del importe total de las bases de retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. Los importes deben consignarse en EUROS. |
| 161-175 | Numérico. | RETENCIONES E INGRESOS A CUENTA. |
|  |  | Se consignará sin signo la suma de las cantidades reflejadas en el campo «RETENCIONES E INGRESOS A CUENTA» (posición 97 a 109) correspondientes a los registros de percepciones, con independencia de la modalidad de percepción a que correspondan. 161-173 Parte entera del importe total de las retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. 174-175 Parte decimal del importe total de las retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. Los importes deben consignarse en EUROS. |
| 176-237 | ------------ | BLANCOS. |
| 238-500 | Alfanumérico. | SELLO ELECTRÓNICO. |
|  |  | Campo reservado para el sello electrónico en presentaciones individuales, que será cumplimentado exclusivamente por los programas de la A.E.A.T. En cualquier otro caso, y en presentaciones colectivas se rellenará a blancos. |
| * Todos los importes serán positivos. * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

![imagen](https://www.boe.es/datos/imagenes/disp/2014/234/09740_13858697_image3.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2014/234/09740_13858697_image4.png)

## MODELO 180

TIPO DE REGISTRO 2: REGISTRO DE PERCEPTOR

(Posiciones, naturaleza y descripción de los campos)

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. |
|  |  | Constante «2». |
| 2-4 | Numérico. | MODELO DECLARACIÓN. |
|  |  | Constante «180». |
| 5-8 | Numérico. | EJERCICIO. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico. | N.I.F. DEL DECLARANTE. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico. | N.I.F. DEL PERCEPTOR. |
|  |  | Si el declarado dispone de NIF asignado en España, se consignará: Si es una persona física se consignará el NIF del declarado de acuerdo con las reglas previstas en el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007, de 27 de julio (BOE del 5 de septiembre). Si el declarado es una persona jurídica o una entidad sin personalidad jurídica (Comunidad de bienes, Sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. Sólo se cumplimentará con los NIF asignados en España. |
| 27-35 | Alfanumérico. | N.I.F. DEL REPRESENTANTE LEGAL. |
|  |  | Si el declarado es menor de 14 años se consignará en este campo el número de identificación fiscal de su representante legal (padre, madre o tutor). Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico. | APELLIDOS Y NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN DEL PERCEPTOR. |
|  |  | a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este mismo orden. Si el declarado es menor de 14 años, se consignarán en este campo los apellidos y nombre del menor de edad. b) Tratándose de personas jurídicas y entidades sin personalidad jurídica, se consignará la razón social o la denominación completa de la entidad, sin anagramas. |
| 76-77 | Numérico. | CÓDIGO PROVINCIA. |
|  |  | Se consignarán los dos dígitos numéricos que correspondan a la provincia o, en su caso, ciudad autónoma, del domicilio del perceptor, según la siguiente relación: ÁLAVA. 01 LEÓN. 24 ALBACETE. 02 LLEIDA. 25 ALICANTE. 03 LUGO. 27 ALMERÍA. 04 MADRID. 28 ASTURIAS. 33 MÁLAGA. 29 ÁVILA. 05 MELILLA. 52 BADAJOZ. 06 MURCIA. 30 BARCELONA. 08 NAVARRA. 31 BURGOS. 09 OURENSE. 32 CÁCERES. 10 PALENCIA. 34 CÁDIZ. 11 PALMAS, LAS. 35 CANTABRIA. 39 PONTEVEDRA. 36 CASTELLÓN. 12 RIOJA, LA. 26 CEUTA. 51 SALAMANCA. 37 CIUDAD REAL. 13 S.C. TENERIFE. 38 CÓRDOBA. 14 SEGOVIA. 40 CORUÑA, A. 15 SEVILLA. 41 CUENCA. 16 SORIA. 42 GIRONA. 17 TARRAGONA. 43 GRANADA. 18 TERUEL. 44 GUADALAJARA. 19 TOLEDO. 45 GUIPÚZCOA. 20 VALENCIA. 46 HUELVA. 21 VALLADOLID. 47 HUESCA. 22 VIZCAYA. 48 ILLES BALEARS. 07 ZAMORA. 49 JAÉN. 23 ZARAGOZA. 50 |
| 78 | Numérico. | MODALIDAD. |
|  |  | Se consignará la modalidad de renta o rendimiento satisfecho a cada perceptor de acuerdo a las siguientes claves: «1» Si la renta o rendimiento satisfecho es de tipo dinerario. «2» Si la renta o rendimiento satisfecho es en especie. |
| 79-92 | Alfanumérico. | BASE RETENCIONES E INGRESOS A CUENTA. |
|  |  | Se consignará el importe que a continuación se indica: – Si el perceptor es un contribuyente por el Impuesto sobre la Renta de las Personas Físicas se consignará la suma de los importes de los rendimientos que por todos los conceptos se satisfagan al arrendador, excluido el Impuesto sobre el Valor Añadido. – Si el perceptor es un sujeto pasivo del Impuesto sobre Sociedades o un contribuyente por el Impuesto sobre la Renta de no Residentes (establecimientos permanentes) se consignará la contraprestación íntegra satisfecha en concepto de alquiler, excluido el Impuesto sobre el Valor Añadido. Este campo se subdivide en: 79 SIGNO: Alfabético. Se cumplimentará este campo cuando las percepciones correspondan a cantidades reintegradas por el perceptor en el ejercicio, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores. En este caso se consignará una «N», en cualquier otro caso el contenido de este campo será un espacio. 80-92 IMPORTE: Campo numérico de 13 posiciones. Se hará constar sin signo y sin decimales, el importe íntegro anual de las percepciones, efectivamente satisfechas a cada perceptor. 80-90 Parte entera del importe de la base de retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. 91-92 Parte decimal del importe de la base de retenciones e ingresos a cuenta, si no tiene contenido se consignará a ceros. Los importes deben consignarse en EUROS. |
| 93-96 | Numérico. | % RETENCIÓN. |
|  |  | Este campo se subdivide en otros dos: 93-94 ENTERO Numérico Parte entera: Se consignará la parte entera del porcentaje (si no tiene, consignar CEROS). 95-96 DECIMAL Numérico Parte decimal: Se consignará la parte decimal del porcentaje (si no tiene, consignar CEROS). De haberse utilizado a lo largo del año más de un porcentaje se indicará exclusivamente el último de ellos. |
| 97-109 | Numérico. | RETENCIONES E INGRESOS A CUENTA. |
|  |  | Campo numérico de 13 posiciones. Se consignará el importe total de las retenciones e ingresos a cuenta que correspondan al campo «BASE RETENCIONES E INGRESOS A CUENTA» del perceptor. Los importes deben consignarse en EUROS. |
| 110-113 | Numérico. | EJERCICIO DEVENGO. |
|  |  | Únicamente se cumplimentará este campo en los supuestos que a continuación se indican, en caso contrario se rellanará a ceros: a) Cuando alguna de las rentas o rendimientos relacionados en el resumen anual se refiera a cantidades satisfechas cuyo devengo o exigibilidad corresponda a ejercicios anteriores al que es objeto de declaración; en estos casos, además de cumplimentar los demás datos que procedan, se reflejarán en este campo las cuatro cifras del ejercicio de devengo. Cuando se hayan satisfecho a un mismo perceptor cantidades cuyo devengo corresponda a diferentes ejercicios, la cumplimentación de los correspondientes datos deberá desglosarse en varios registros, de forma que cada uno de ellos refleje exclusivamente los datos correspondientes a devengos de un mismo ejercicio. b) Asimismo, se cumplimentará este campo cuando se incluyan en el modelo 180 los datos relativos a cantidades reintegradas por sus perceptores en el ejercicio, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores. En estos supuestos, cada reintegro se relacionará bajo la misma modalidad de percepción bajo la cual se incluyeron en su día las cantidades indebida o excesivamente satisfechas, reflejando su importe en el campo «Base de Retención», cumplimentando el campo «Signo de la Base de Retención» con la letra «N» y haciendo constar en el campo «Ejercicio devengo» el año en el que se hubieran devengado originariamente las percepciones reintegradas. Cuando se hayan producido reintegros procedentes de una misma persona o entidad que correspondan a percepciones originariamente devengadas en varios ejercicios, su importe deberá desglosarse en varios apuntes (registros), de forma que cada uno de ellos refleje exclusivamente reintegros de percepciones correspondientes a un mismo ejercicio. |
| 114 | Numérico. | SITUACIÓN DEL INMUEBLE. |
|  |  | Se consignará de entre las siguientes claves la que corresponda a la situación del inmueble arrendado: 1. Inmueble con referencia catastral situado en cualquier punto del territorio español, excepto País Vasco y Navarra. 2. Inmueble con referencia catastral situado en la Comunidad Autónoma del País Vasco o en la Comunidad Foral de Navarra. 3. Inmueble sin referencia catastral. |
| 115-134 | Alfanumérico. | REFERENCIA CATASTRAL. |
|  |  | Se consignará la referencia catastral correspondiente al inmueble arrendado. |
| 135-327 | Alfanumérico. | DIRECCIÓN DEL INMUEBLE. |
|  |  | Se consignará la dirección correspondiente al inmueble arrendado. Este campo se subdivide en: 135-139 TIPO DE VÍA. Se consignará el código alfabético de tipo de vía, normalizado según Instituto Nacional de Estadística (INE). 140-189 NOMBRE VÍA PÚBLICA. Se consignará el nombre largo de la vía pública, si no cupiese completo el nombre, no se harán constar los artículos, preposiciones ni conjunciones y se pondrán en abreviatura los títulos (vgr, cd = Conde). Los demás casos se abreviarán utilizando las siglas de uso general. 190-192 TIPO DE NUMERACIÓN. Se consignará el tipo de numeración (Valores: NÚM; KM.; S/N; etc.). 193-197 NÚMERO DE CASA. Se consignará el número de casa o punto kilométrico. 198-200 CALIFICADOR DEL NÚMERO. Se consignará el calificador del número (valores BIS; DUP; MOD; ANT; etc. / metros si Tipo Numer = KM.). 201-203 BLOQUE. Se consignará el bloque (número o letras). 204-206 PORTAL. Se consignará el portal (número o letras). 207-209 ESCALERA. Se consignará la escalera (número o letras). 210-212 PLANTA O PISO. Se consignará la planta o el piso (número o letras). 213-215 PUERTA. Se consignará la puerta (número o letras). 216-255 COMPLEMENTO. Datos complementarios del domicilio. Valores: Literal libre. (Ejemplos: «Urbanización ..........»; «Centro Comercial ........, local ..........»; «Mercado de .......... puesto n.º ........»; «Edificio .........»; etc.). 256-285 LOCALIDAD O POBLACIÓN. Se consignará el nombre de la localidad, de la población, etc., si es distinta al Municipio. 286-315 MUNICIPIO. Se consignará el nombre de municipio. Se consignará el correspondiente al inmueble arrendado. 316-320 CÓDIGO DE MUNICIPIO. Se consignará el CÓDIGO de municipio normalizado según Instituto Nacional de Estadística (INE). 321-322 CÓDIGO PROVINCIA. Se consignará el código de la provincia. Se consignarán los dos dígitos numéricos que correspondan a la provincia o, en su caso, ciudad autónoma, que corresponda al inmueble arrendado, según la siguiente relación: ARABA/ÁLAVA. 01 LEÓN. 24 ALBACETE. 02 LLEIDA. 25 ALICANTE/Alacant. 03 LUGO. 27 ALMERÍA. 04 MADRID. 28 ASTURIAS. 33 MÁLAGA. 29 ÁVILA. 05 MELILLA. 52 BADAJOZ. 06 MURCIA. 30 BARCELONA. 08 NAVARRA. 31 BURGOS. 09 OURENSE. 32 CÁCERES. 10 PALENCIA. 34 CÁDIZ. 11 PALMAS, LAS. 35 CANTABRIA. 39 PONTEVEDRA. 36 CASTELLÓN/Castelló. 12 RIOJA, LA. 26 CEUTA. 51 SALAMANCA. 37 CIUDAD REAL. 13 S.C. TENERIFE. 38 CÓRDOBA. 14 SEGOVIA. 40 CORUÑA, A. 15 SEVILLA. 41 CUENCA. 16 SORIA. 42 GIRONA. 17 TARRAGONA. 43 GRANADA. 18 TERUEL. 44 GUADALAJARA. 19 TOLEDO. 45 GIPÚZKOA. 20 VALENCIA/Valéncia. 46 HUELVA. 21 VALLADOLID. 47 HUESCA. 22 BIZKAIA. 48 ILLES BALEARS. 07 ZAMORA. 49 JAÉN. 23 ZARAGOZA. 50 323-327 CÓDIGO POSTAL. Se consignará el código postal correspondiente a la dirección del inmueble arrendado. |
| 328-500 | ------------ | BLANCOS. |
| * Todos los importes serán positivos. * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

> Se sustituye por el art. 2 y el anexo III de la Orden HAP/1732/2014, de 24 de septiembre. Ref. BOE-A-2014-9740.
