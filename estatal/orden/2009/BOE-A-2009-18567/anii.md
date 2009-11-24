## ANEXO II

## DISEÑOS FÍSICOS Y LÓGICOS A LOS QUE DEBEN AJUSTARSE LOS SOPORTES DIRECTAMENTE LEGIBLES POR ORDENADOR DEL MODELO 190 Y LOS FICHEROS QUE CONTENGAN LA INFORMACIÓN QUE DEBE INCLUIRSE EN DICHO MODELO

A) CARACTERÍSTICAS DE LOS SOPORTES LEGIBLES POR ORDENADOR

Los soportes directamente legibles por ordenador para la presentación del resumen anual de retenciones e ingresos a cuenta del Impuesto sobre la Renta de las Personas Físicas sobre rendimientos del trabajo y de determinadas actividades económicas, premios y determinadas ganancias patrimoniales e imputaciones de renta (Modelo 190), habrán de cumplir las siguientes características:

— Tipo: DVD–R o DVD+R

— Capacidad: Hasta 4,7 GB

— Sistema de archivos UDF

— De una cara y una capa simple

Si las características del equipo de que dispone el declarante no le permiten ajustarse a las especificaciones técnicas exigidas, y está obligado a presentar el resumen anual de retenciones e ingresos a cuenta del Impuesto sobre la Renta de las Personas Físicas sobre rendimientos del trabajo y de actividades económicas, premios y determinadas ganancias patrimoniales e imputaciones de renta (modelo 190) en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (AEAT), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la AEAT.

B) DISEÑOS LÓGICOS

Diseños lógicos para la presentación del resumen anual de retenciones e ingresos a cuenta del Impuesto sobre la Renta de las Personas Físicas sobre rendimientos del trabajo y de determinadas actividades económicas, premios y determinadas ganancias patrimoniales e imputaciones de renta (Modelo 190).

DESCRIPCIÓN DE LOS REGISTROS

Se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

Tipo 1: Registro de declarante: Datos identificativos y resumen. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados.

Tipo 2: Registro de perceptor. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados.

El orden de presentación será ascendente por el campo tipo de registro, primero el de tipo 1 y a continuación los del tipo 2 que se declaren.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta forma la letra “Ñ” tendrá el valor ASCII 209 (Hex. D1) y la “Ç”(cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2009/282/18567_009.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2009/282/18567_010.png)

## MODELO 190

## A. TIPO DE REGISTRO 1: REGISTRO DE DECLARANTE (POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS)

| POSICIONES | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. |
|  |  | Constante número ‘1’. |
| 2-4 | Numérico | MODELO DECLARACIÓN. |
|  |  | Constante ‘190’. |
| 5-8 | Numérico | EJERCICIO. |
|  |  | Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico | NIF DEL DECLARANTE. |
|  |  | Se consignará el número de identificación fiscal (NIF) del declarante, de acuerdo con las reglas previstas en el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007, de 27 de julio («BOE» del 5 de septiembre). |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda. |
| 18-57 | Alfanumérico | APELLIDOS Y NOMBRE, DENOMINACIÓN O RAZÓN SOCIAL DEL DECLARANTE. |
|  |  | Si es una persona física se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo necesariamente en este orden. |
|  |  | Para personas jurídicas y entidades en régimen de atribución de Rentas, se consignará la razón social completa, sin anagrama. |
|  |  | En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético | TIPO DE SOPORTE. |
|  |  | Se cumplimentará una de las siguientes claves: |
|  |  | ‘C’: Si la información se presenta en soporte (DVD–R o DVD+R). |
|  |  | ‘T’: Transmisión telemática. |
| 59-107 | Alfanumérico | PERSONA CON QUIÉN RELACIONARSE. |
|  |  | Datos de la persona con quién relacionarse. Este campo se subdivide en dos: |
|  | 59-67 | TELÉFONO: Campo numérico de 9 posiciones. |
|  | 68-107 | APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN. |
|  |  | Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. |
| 121-122 | Alfabético | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. |
|  |  | En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarle obligatoriamente uno de los siguientes campos: |
|  |  | 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una «C» si la presentación de esta declaración tiene por objeto incluir percepciones que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidas en la misma. |
|  |  | La presentación de una declaración complementaria que tenga por objeto la modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente se realizará desde el servicio de consulta y modificación de declaraciones informativas en la Oficina Virtual de la Agencia Tributaria (www.agenciatributaria.es). |
|  |  | 122 DECLARACIÓN SUSTITUTIVA: Se consignará una «S» si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. |
|  |  | En caso de que se haya consignado una «C» en el campo «Declaración complementaria» (posición 121) o una «S» en el campo «Declaración sustitutiva» (posición 122), se consignará el número identificativo correspondiente a la declaración a la que complementa o la que se sustituye mediante la nueva. |
|  |  | Campo de contenido numérico de 13 posiciones. |
|  |  | En cualquier otro caso deberá rellenarse a CEROS. |
| 136-144 | Numérico | NÚMERO TOTAL DE PERCEPCIONES. |
|  |  | Se consignará el número total de percepciones declaradas para este retenedor, con independencia de las claves o subclaves de percepción a que correspondan. (Número de registros de tipo 2.) |
| 145-160 | Alfanumérico | IMPORTE TOTAL DE LAS PERCEPCIONES. |
|  |  | Este campo se subdivide en dos: |
|  |  | 145 SIGNO: campo alfabético que se cumplimentará cuando el resultado de la suma para obtener el importe de las percepciones satisfechas (posiciones 146 a 160 de este registro de tipo 1) sea menor de 0 (cero). En este caso se consignará una «N», en cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 146-160 IMPORTE: campo numérico en el que se consignará la suma de las cantidades, sin coma decimal, reflejadas en las percepciones íntegras satisfechas (posiciones 82 a 94 y 109 a 121, correspondientes a los registros de percepciones), con independencia de la clave de percepción a la que correspondan. En el supuesto de que en los registros de perceptores se hubiera consignado «N» en los campos SIGNO DE LA PERCEPCIÓN ÍNTEGRA o SIGNO DE LA PERCEPCIÓN EN ESPECIE (VALORACIÓN) (posiciones 81 y 108, respectivamente, del registro de tipo 2), por corresponder al reintegro de percepciones indebida o excesivamente satisfechas en ejercicios anteriores, dichas cantidades se computarán igualmente con signo menos al totalizar los importes que deben reflejarse en esta suma. |
|  |  | Los importes deben consignarse en EUROS. |
|  |  | Este campo se subdivide en dos: |
|  |  | 146-158 Parte entera del importe total de las percepciones. Si no tiene contenido se consignará a ceros. |
|  |  | 159-160 Parte decimal del importe total de las percepciones. Si no tiene contenido se consignará a ceros. |
| 161-175 | Numérico | IMPORTE TOTAL DE LAS RETENCIONES E INGRESOS A CUENTA. |
|  |  | Se consignará sin signo y sin coma decimal, la suma de las cantidades reflejadas en los campos «Retenciones practicadas» e «Ingresos a cuenta efectuados» (posiciones 95 a 107, 122 a 134 correspondientes a los registros de tipo 2), con independencia de las claves o subclaves de percepción a que correspondan. |
|  |  | Los importes deben consignarse en EUROS. |
|  |  | Este campo se subdivide en dos: |
|  |  | 161-173 Parte entera del importe total de las retenciones e ingresos a cuenta. Si no tiene contenido se consignará a ceros. |
|  |  | 174-175 Parte decimal del importe total de las retenciones e ingresos a cuenta. Si no tiene contenido se consignará a ceros. |
| 176-487 | – | BLANCOS. |
| 488-500 | Alfanumérico | SELLO ELECTRÓNICO. |
|  |  | Campo reservado para el sello electrónico, que será cumplimentado exclusivamente por los programas de la AEAT. En cualquier otro caso, se rellenará a blancos. |

* Todos los importes serán positivos.

* Los campos numéricos que no tengan contenido se rellenarán a ceros.

* Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

* Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda.

* Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.

![imagen](https://www.boe.es/datos/imagenes/disp/2009/282/18567_011.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2009/282/18567_012.png)

## MODELO 190

## B. TIPO DE REGISTRO 2: REGISTRO DE PERCEPTOR (POSICIONES, NATURALEZA Y DESCRIPCIÓN DE LOS CAMPOS)

| POSICIÓN | NATURALEZA | DESCRIPCIÓN DE LOS CAMPOS |
| --- | --- | --- |
| 1 | Numérico | TIPO DE REGISTRO. |
|  |  | Constante ‘2’. |
| 2-4 | Numérico | MODELO DECLARACIÓN. |
|  |  | Constante ‘190’. |
| 5-8 | Numérico | EJERCICIO. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico | NIF DEL DECLARANTE. |
|  |  | Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico | NIF DEL PERCEPTOR. |
|  |  | Si el perceptor es una persona física se consignará su número de identificación fiscal (NIF) de acuerdo con las reglas previstas en el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por el Real Decreto 1065/2007, de 27 de julio («BOE» del 5 de septiembre). |
|  |  | Si el perceptor es una entidad en régimen de atribución de rentas (comunidad de bienes, sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. |
|  |  | Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como el número de identificación fiscal de su representante legal. |
|  |  | En las percepciones correspondientes a la clave J se consignará en quien concurran las condiciones a que se refiere el artículo 92.1 de la Ley del Impuesto. |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
| 27-35 | Alfanumérico | NIF DEL REPRESENTANTE LEGAL. |
|  |  | Si el perceptor es menor de 14 años, se consignará en este campo el número de identificación fiscal de su representante legal (padre, madre o tutor). |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
|  |  | En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico | APELLIDOS Y NOMBRE O DENOMINACIÓN DEL PERCEPTOR. |
|  |  | a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este mismo orden. |
|  |  | b) Tratándose de entidades en régimen de atribución de rentas, se consignará la denominación completa de la entidad, sin anagramas. |
| 76-77 | Numérico | CÓDIGO PROVINCIA. |
|  |  | a) Con carácter general, se consignarán los dos dígitos numéricos que correspondan a la provincia o, en su caso, Ciudad con Estatuto de Autonomía, del domicilio del perceptor, según la siguiente relación: |
|  |  | ÁLAVA | 01 | LEÓN | 24 |
|  |  | ALBACETE | 02 | LLEIDA | 25 |
|  |  | ALICANTE | 03 | LUGO | 27 |
|  |  | ALMERÍA | 04 | MADRID | 28 |
|  |  | ASTURIAS | 33 | MÁLAGA | 29 |
|  |  | ÁVILA | 05 | MELILLA | 52 |
|  |  | BADAJOZ | 06 | MURCIA | 30 |
|  |  | BARCELONA | 08 | NAVARRA | 31 |
|  |  | BURGOS | 09 | OURENSE | 32 |
|  |  | CÁCERES | 10 | PALENCIA | 34 |
|  |  | CÁDIZ | 11 | PALMAS, LAS | 35 |
|  |  | CANTABRIA | 39 | PONTEVEDRA | 36 |
|  |  | CASTELLÓN | 12 | RIOJA, LA | 26 |
|  |  | CEUTA | 51 | SALAMANCA | 37 |
|  |  | CIUDAD REAL | 13 | S.C.TENERIFE | 38 |
|  |  | CÓRDOBA | 14 | SEGOVIA | 40 |
|  |  | CORUÑA, A | 15 | SEVILLA | 41 |
|  |  | CUENCA | 16 | SORIA | 42 |
|  |  | GIRONA | 17 | TARRAGONA | 43 |
|  |  | GRANADA | 18 | TERUEL | 44 |
|  |  | GUADALAJARA. | 19 | TOLEDO | 45 |
|  |  | GUIPÚZCOA | 20 | VALENCIA | 46 |
|  |  | HUELVA | 21 | VALLADOLID | 47 |
|  |  | HUESCA | 22 | VIZCAYA | 48 |
|  |  | ILLES BALEARS | 07 | ZAMORA | 49 |
|  |  | JAÉN | 23 | ZARAGOZA | 50 |
|  |  | b) Supuesto especial.–Tratándose de percepciones correspondientes a contribuyentes del Impuesto sobre la Renta de las Personas Físicas con residencia habitual en el extranjero, a los que se refieren los artículos 8.2 y 10 de la Ley del Impuesto (personas físicas de nacionalidad española que acrediten su nueva residencia fiscal en un país o territorio considerado como paraíso fiscal, miembros de misiones diplomáticas españolas, miembros de oficinas consulares españolas, ... etc.), se consignarán como código de provincia los dígitos 98. |
|  |  | En ningún caso se incluirán en el modelo 190 percepciones correspondientes a personas o entidades no residentes en territorio español que no sean contribuyentes del IRPF, sin perjuicio de la inclusión, en su caso, de la información correspondiente a dichas percepciones en el resumen anual de retenciones e ingresos a cuenta del Impuesto sobre la Renta de no Residentes (modelo 296) a que se refiere el artículo 15.2 del Reglamento de dicho Impuesto, aprobado por el Real Decreto 1776/2004, de 30 de julio («BOE» del 5 de agosto). |
| 78 | Alfabético | CLAVE DE PERCEPCIÓN. |
|  |  | Se consignará la clave alfabética que corresponda a las percepciones de que se trate, según la relación de claves siguientes: |
|  |  | A. Rendimientos del trabajo: Empleados por cuenta ajena en general. Se utilizará esta clave para relacionar todas aquellas percepciones, dinerarias o en especie, que hayan sido satisfechas por la persona o entidad declarante en concepto de rendimientos del trabajo, siempre que para determinar el importe de la retención hubiese resultado aplicable el procedimiento general establecido en el artículo 82 del Reglamento del Impuesto y que sean distintas de las que deban reflejarse específicamente en las claves B, C y D. Por consiguiente, también se incluirán en esta clave, entre otras, las percepciones correspondientes a los trabajadores manuales que perciban sus retribuciones por peonadas o jornales diarios como consecuencia de una relación esporádica y diaria con el empleador, así como las correspondientes a las relaciones laborales especiales de carácter dependiente y a los contratos o relaciones laborales de duración inferior al año. |
|  |  | Por excepción, no se incluirán en el modelo 190 las retribuciones del trabajo en especie respecto de las cuales no exista obligación de efectuar ingresos a cuenta conforme a lo previsto en el artículo 102.2 del Reglamento del Impuesto (contribuciones satisfechas por los promotores de Planes de Pensiones y de Mutualidades de Previsión Social y los Planes de Previsión Social Empresarial que reduzcan la base imponible), sin perjuicio de la obligación de declarar los datos relativos a dichos conceptos en el modelo 345. |
|  |  | B. Rendimientos del trabajo: Pensionistas y perceptores de haberes pasivos y demás prestaciones previstas en el articulo 17.2.a) de la Ley del Impuesto. Se identificarán con esta clave las percepciones no exentas del IRPF correspondientes a las pensiones y haberes pasivos de los regímenes públicos de la Seguridad Social y clases pasivas, así como las que correspondan a las demás, sean dinerarias o en especie, a que hace referencia el artículo 17.2, letra a), de la Ley del Impuesto. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | C. Rendimientos del trabajo: Prestaciones o subsidios por desempleo. Se identificarán con esta clave las percepciones correspondientes a las prestaciones o subsidios por desempleo, con excepción de las prestaciones satisfechas por este concepto en la modalidad de pago único. |
|  |  | D. Rendimientos del trabajo: Prestaciones por desempleo abonadas en la modalidad de pago único. Se identificarán con esta clave las prestaciones por desempleo abonadas con arreglo a la modalidad de pago único establecida en el Real Decreto 1044/1985, de 19 de junio, en la cuantía que, en su caso, exceda del límite exento del IRPF establecido en el artículo 7, letra n), de la Ley del Impuesto. La parte de dicho pago único que, por no exceder del mencionado límite, resulte exenta del impuesto, se incluirá entre las percepciones de la clave L, subclave 13. |
|  |  | En los supuestos en que, de no haber mediado el pago único, el perceptor hubiese tenido derecho a la prestación por desempleo durante un período de tiempo que comprenda más de un ejercicio, el importe del pago único que proceda relacionar en esta clave deberá desglosarse en varios apuntes o registros, de forma que cada uno de ellos refleje la parte de dicho importe imputable a cada uno de los ejercicios afectados, determinada en proporción a la cuantía de la prestación por desempleo que, de no haber mediado pago único, hubiera correspondido percibir en el ejercicio de que se trate. |
|  |  | E. Rendimientos del trabajo: Consejeros y administradores. Se identificarán con esta clave las retribuciones, dinerarias o en especie, satisfechas a personas físicas por su condición de administradores y miembros de los Consejos de administración o de las Juntas que hagan sus veces y demás miembros de otros órganos representativos. |
|  |  | F. Rendimientos del trabajo: Cursos, conferencias, seminarios y similares y elaboración de obras literarias, artísticas o científicas. Se identificarán con esta clave las percepciones, dinerarias o en especie, satisfechas por la persona o entidad declarante en concepto de rendimientos del trabajo, cuando deriven de impartir cursos, conferencias, coloquios, seminarios y similares, o bien de la elaboración de obras literarias, artísticas o científicas, siempre que se hubiera cedido el derecho a la explotación de las mismas. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | G. Rendimientos de actividades económicas: Actividades profesionales. Se identificarán con esta clave las percepciones, dinerarias o en especie, satisfechas por la persona o entidad declarante que sean contraprestación de las actividades económicas de naturaleza profesional a que se refieren los apartados 1 y 2 del artículo 95 del Reglamento del Impuesto. Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | H. Rendimientos de actividades económicas: actividades agrícolas, ganaderas y forestales y actividades en estimación objetiva a las que se refiere el artículo 95.6 del Reglamento del Impuesto. Se identificarán con esta clave las percepciones, dinerarias o en especie, satisfechas por la persona o entidad declarante que sean contraprestación de las siguientes actividades económicas: |
|  |  | a) Las actividades agrícolas, ganaderas o forestales a que se refieren los apartados 4 y 5 del artículo 95 del Reglamento del Impuesto. Respecto de estas actividades, no se incluirán las subvenciones corrientes o de capital ni las indemnizaciones, conceptos que, en su caso, deberán ser declarados en el modelo 346. |
|  |  | b) Las actividades económicas en estimación objetiva previstas en el apartado 6.2.º del artículo 95 del Reglamento del Impuesto. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | I. Rendimientos de actividades económicas: rendimientos a que se refiere el articulo 75.2, letra b), del Reglamento del Impuesto. Se identificarán con esta clave las percepciones, dinerarias o en especie, satisfechas por la persona o entidad declarante en concepto de rendimientos de la propiedad intelectual o industrial, de la prestación de asistencia técnica, del arrendamiento de bienes muebles, negocios o minas o del subarrendamiento de dichos bienes, así como los procedentes de la cesión del derecho a la explotación del derecho de imagen, cuando dichos rendimientos tengan para su perceptor la calificación fiscal de rendimientos de actividades económicas distintos de los procedentes de actividades profesionales que deban incluirse en la clave G. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | J. Imputación de rentas por la cesión de derechos de imagen: contraprestaciones a que se refiere el articulo 92.8 de la Ley del Impuesto. Se identificarán con esta clave las contraprestaciones, dinerarias o en especie, satisfechas por la persona o entidad declarante a personas o entidades no residentes en territorio español, que estén sujetas a la obligación de efectuar el ingreso a cuenta previsto en el artículo 92.8 de la Ley del Impuesto. |
|  |  | En las percepciones de esta clave se consignará como NIF del perceptor el correspondiente a la persona física residente que deba efectuar la imputación en la base imponible del IRPF de las rentas derivadas de la cesión del derecho de imagen, en aplicación del régimen especial establecido en el artículo 92 de la Ley del Impuesto. |
|  |  | K. Premios y ganancias patrimoniales de los vecinos derivadas de los aprovechamientos forestales en montes públicos. Se identificarán con esta clave las siguientes rentas sometidas a retención o ingreso a cuenta: |
|  |  | a) Los premios, dinerarios o en especie, a que se refiere el artículo 75.2, letra c), del Reglamento del Impuesto, que hayan sido entregados por la persona o entidad declarante como consecuencia de la participación de los perceptores en juegos, concursos, rifas o combinaciones aleatorias, incluyendo aquellos sobre los que no exista obligación de practicar retención o ingreso a cuenta por no superar la base de retención la cantidad de 300 euros. Se exceptúan los premios exentos del IRPF en virtud de lo dispuesto en el artículo 7, letra ñ), de la Ley del Impuesto, así como los premios que se entreguen como consecuencia de juegos organizados al amparo de lo previsto en el Real Decreto-ley 16/1977, de 25 de febrero, por el que se regulan los aspectos penales, administrativos y fiscales de los juegos de suerte, envite o azar y apuestas, y demás normativa estatal o autonómica sobre el juego. |
|  |  | b) Las ganancias patrimoniales a que se refiere el último inciso del artículo 75.1, letra d), del Reglamento del Impuesto, consistentes en percepciones obtenidas por los vecinos como consecuencia de aprovechamientos forestales en montes públicos. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
|  |  | L. Rentas exentas y dietas exceptuadas de gravamen. Se identificarán con esta clave las dietas y asignaciones para gastos de viaje, en las cuantías que resulten exceptuadas de gravamen con arreglo a lo dispuesto en el artículo 9 del Reglamento del Impuesto, así como las rentas exentas del IRPF que tengan la consideración de rendimientos del trabajo, con excepción de las anualidades por alimentos a que se refiere la letra k) del artículo 7 de la Ley del Impuesto, y aquellas otras que, teniendo la consideración de rendimientos de actividades económicas, estén exentas en virtud de lo dispuesto en el citado artículo 7 de la Ley del Impuesto. En el supuesto de las becas exentas a que se refiere la letra j) del artículo 7 de la Ley del Impuesto, únicamente deberán relacionarse en el modelo 190 aquellas cuya cuantía supere la cantidad de 3.000 euros. |
|  |  | Tratándose de dietas y asignaciones para gastos de viaje, así como cuando la exención esté sujeta a límites cuantitativos, si la persona o entidad declarante hubiera satisfecho cantidades superiores a los límites legal o reglamentariamente establecidos, el exceso deberá incluirse en la clave y, en su caso, subclave, que corresponda de las demás claves y subclaves que en estas instrucciones se indican. |
|  |  | Se consignará, obligatoriamente, la subclave que en cada caso proceda de las indicadas en el campo SUBCLAVE. |
| 79-80 | Numérico | SUBCLAVE. |
|  |  | Tratándose de percepciones correspondientes a las claves B, F, G, H, I, K y L, deberá consignarse, además, la subclave numérica de dos dígitos que corresponda a las percepciones de que se trate, según la relación de subclaves que para cada una de las mencionadas claves figura a continuación. |
|  |  | En percepciones correspondientes a claves distintas de las mencionadas, no se cumplimentará este campo. |
|  |  | Cuando deban consignarse en el modelo 190 percepciones satisfechas a un mismo perceptor que correspondan a diferentes claves o subclaves de percepción, deberán cumplimentarle tantos apuntes o registros de percepción como sea necesario, de forma que cada uno de ellos refleje exclusivamente los datos de percepciones correspondientes a una misma clave y, en su caso, subclave. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave B: |
|  |  | 01 Se consignará esta subclave cuando se trate de percepciones consistentes en pensiones y haberes pasivos de los regímenes de la Seguridad Social y Clases Pasivas, con excepción de las que deban relacionarse bajo la subclave 03. |
|  |  | 02 Se consignará esta subclave en todas las percepciones de la clave B distintas de las que deban relacionarse bajo las subclaves 01 y 03. |
|  |  | 03 Se consignará esta subclave en todas las percepciones de la clave B en las que el importe de las retenciones se haya determinado con arreglo al procedimiento especial previsto en el artículo 89.A del Reglamento del Impuesto. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave F: |
|  |  | 01 Se consignará esta subclave cuando las percepciones correspondan a alguno de los premios literarios, científicos o artísticos no exentos del Impuesto a que se refiere el artículo 11.1, letra g), del Reglamento del Impuesto. |
|  |  | 02 Se consignará esta subclave en todas las percepciones de la clave F distintas de las que deban relacionarse bajo la subclave 01. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave G: |
|  |  | 01 Se consignará esta subclave cuando se trate de percepciones a las que resulte aplicable el tipo de retención establecido con carácter general en el artículo 95.1 del Reglamento del Impuesto. |
|  |  | 02 Se consignará esta subclave cuando se trate de percepciones a las que resulte aplicable el tipo de retención específico establecido en el citado artículo del Reglamento del Impuesto para los rendimientos satisfechos a recaudadores municipales, mediadores de seguros que utilicen los servicios de auxiliares externos y delegados comerciales de la entidad pública empresarial «Loterías y Apuestas del Estado». |
|  |  | 03 Se consignará esta subclave cuando se trate de percepciones a las que resulte aplicable el tipo de retención reducido establecido en el artículo 95.1 del Reglamento del Impuesto para los rendimientos satisfechos a contribuyentes que inicien el ejercicio de actividades profesionales, tanto en el período impositivo en que se produzca dicho inicio como en los dos siguientes. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave H: |
|  |  | 01 Se consignará esta subclave cuando se trate de percepciones a las que resulte aplicable el tipo de retención establecido con carácter general en el artículo 95.4.2.º del Reglamento del Impuesto. |
|  |  | 02 Se consignará esta subclave cuando se trate de percepciones a las que resulte aplicable el tipo de retención específico establecido en el artículo 95.4.1.º del Reglamento del Impuesto para los rendimientos que sean contraprestación de actividades ganaderas de engorde de porcino y avicultura. |
|  |  | 03 Se consignará esta subclave cuando las percepciones satisfechas sean contraprestación de las actividades forestales a que se refiere el artículo 95.5 del Reglamento del Impuesto. |
|  |  | 04 Se consignará esta subclave cuando las percepciones satisfechas sean contraprestación de las actividades económicas en estimación objetiva recogidas en el artículo 95.6.2.º del Reglamento del Impuesto. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave I: |
|  |  | 01 Se consignará esta subclave cuando se trate de percepciones satisfechas por la persona o entidad declarante en concepto de rendimientos procedentes de la cesión del derecho a la explotación del derecho de imagen. |
|  |  | 02 Se consignará esta subclave cuando se trate de percepciones satisfechas por la persona o entidad declarante por cualquier otro de los conceptos a que se refiere el artículo 75.2, letra b) del Reglamento del Impuesto. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave K: |
|  |  | 01 Se consignará esta subclave cuando las percepciones correspondan a premios por la participación en juegos, concursos, rifas o combinaciones aleatorias. |
|  |  | 02 Se consignará esta subclave cuando las percepciones correspondan a ganancias patrimoniales obtenidas por los vecinos como consecuencia de aprovechamientos forestales en montes públicos. |
|  |  | Subclaves a utilizar en percepciones correspondientes a la clave L: |
|  |  | 01 Dietas y asignaciones para gastos de viaje exceptuadas de gravamen conforme a lo previsto en el artículo 9 del Reglamento del Impuesto. |
|  |  | 02 Prestaciones públicas extraordinarias por actos de terrorismo y pensiones derivadas de medallas y condecoraciones concedidas por actos de terrorismo que estén exentas en virtud de lo establecido en la letra a) del artículo 7 de la Ley del Impuesto. |
|  |  | 03 Ayudas percibidas por los afectados por el virus de la inmunodeficiencia humana a que se refiere la letra b) del artículo 7 de la Ley del Impuesto. |
|  |  | 04 Pensiones por lesiones o mutilaciones sufridas con ocasión o como consecuencia de la Guerra Civil 1936/1939 que estén exentas en virtud de lo establecido en la letra c) del artículo 7 de la Ley del Impuesto. |
|  |  | 05 Indemnizaciones por despido o cese del trabajador que estén exentas en virtud de lo establecido en la letra e) del artículo 7 de la Ley del Impuesto y en el artículo 1 del Reglamento. |
|  |  | 06 Prestaciones por incapacidad permanente absoluta o gran invalidez que estén exentas conforme a lo establecido en la letra f) del artículo 7 de la Ley del Impuesto. |
|  |  | 07 Pensiones por inutilidad o incapacidad permanente del régimen de clases pasivas a que se refiere la letra g) del artículo 7 de la Ley del Impuesto. |
|  |  | 08 Prestaciones, pensiones y haberes pasivos que estén exentos en virtud de lo establecido en la letra h) del artículo 7 de la Ley del Impuesto. |
|  |  | 09 Prestaciones económicas de instituciones públicas con motivo del acogimiento de personas con discapacidad, mayores de sesenta y cinco años o menores y ayudas económicas otorgadas por instituciones públicas a personas con discapacidad o mayores de sesenta y cinco años para financiar su estancia en residencias o centros de día, que estén exentas en virtud de lo establecido en la letra i) del artículo 7 de la Ley del Impuesto. |
|  |  | 10 Becas que estén exentas en virtud de lo establecido en la letra j) del artículo 7 de la Ley del Impuesto. |
|  |  | 11 Premios literarios, artísticos o científicos relevantes, así como los premios «Príncipe de Asturias», que estén exentos en virtud de lo establecido en la letra l) del artículo 7 de la Ley del Impuesto y en el artículo 3 del Reglamento. |
|  |  | 12 Ayudas económicas a los deportistas de alto nivel que estén exentas en virtud de lo establecido en la letra m) del artículo 7 de la Ley del Impuesto y en el artículo 4 del Reglamento. |
|  |  | 13 Prestaciones por desempleo abonadas en la modalidad de pago único que estén exentas en virtud de lo establecido en la letra n) del artículo 7 de la Ley del Impuesto. |
|  |  | 14 Gratificaciones extraordinarias satisfechas por el Estado español por la participación en misiones internacionales de paz o humanitarias que estén exentas en virtud de lo establecido en la letra o) del artículo 7 de la Ley del Impuesto y en el artículo 5 del Reglamento. |
|  |  | 15 Rendimientos del trabajo percibidos por trabajos realizados en el extranjero que estén exentos en virtud de lo establecido en la letra p) del artículo 7 de la Ley del Impuesto y en el artículo 6 del Reglamento. |
|  |  | 16 Prestaciones por entierro o sepelio que estén exentas en virtud de lo establecido en la letra r) del artículo 7 de la Ley del Impuesto. |
|  |  | 17 Ayudas a favor de las personas que hayan desarrollado la hepatitis C como consecuencia de haber recibido tratamiento en el ámbito del sistema sanitario público, que estén exentas en virtud de lo establecido en la letra s) del artículo 7 de la Ley del Impuesto. |
|  |  | 18 Prestaciones en forma de renta obtenidas por las personas con discapacidad correspondientes a aportaciones a sistemas de previsión social constituidos en favor de las mismas, que estén exentas en virtud de lo establecido en la letra w) del artículo 7 de la Ley del Impuesto. |
|  |  | 19 Prestaciones económicas públicas vinculadas al servicio para cuidados en el entorno familiar y de asistencia personalizada que se derivan de la Ley de promoción de la autonomía personal y atención a las personas en situación de dependencia, que estén exentas en virtud de lo establecido en la letra x) del artículo 7 de la Ley del Impuesto. |
|  |  | 20 Prestaciones y ayudas familiares públicas vinculadas al nacimiento, adopción, acogimiento o cuidado de hijos menores, que estén exentas en virtud de lo establecido en la letra z) del artículo 7 de la Ley del Impuesto. |
|  |  | 21 Otras rentas exentas. Se incluirán en esta subclave las rentas exentas del Impuesto sobre la Renta de las Personas Físicas que, debiendo relacionarse en el modelo 190, sean distintas de las específicamente señaladas en las subclaves anteriores. |
| 81-107 | Alfanumérico | PERCEPCIONES DINERARIAS. |
|  |  | Este campo se subdivide en tres: |
|  |  | 81 SIGNO DE LA PERCEPCIÓN ÍNTEGRA: Se cumplimentará este campo cuando las percepciones correspondan a cantidades reintegradas por el perceptor en el ejercicio, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores. En este caso se consignará una «N», en cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 82-94 PERCEPCIÓN ÍNTEGRA (Dineraria): Campo numérico de 13 posiciones. Se hará constar sin signo y sin coma decimal, el importe íntegro anual de las percepciones dinerarias efectivamente satisfechas a cada perceptor. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 82-92 Parte entera del importe de la percepción íntegra, si no tiene contenido se consignará a ceros. |
|  |  | 93-94 Parte decimal del importe de la percepción íntegra, si no tiene contenido se consignará a ceros. |
|  |  | 95-107 RETENCIONES PRACTICADAS: Campo numérico de 13 posiciones. Se consignará, sin signo y sin coma decimal el importe anual efectivamente retenido a cuenta del IRPF en relación con las percepciones dinerarias consignadas en el campo anterior. |
|  |  | Si algún perceptor no ha sufrido retención este campo se consignará relleno a ceros. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 95-105 Parte entera del importe de las retenciones practicadas, si no tiene contenido se consignará a ceros. |
|  |  | 106-107 Parte decimal del importe de las retenciones practicadas, si no tiene contenido se consignará a ceros. |
| 108-147 | Alfanumérico | PERCEPCIONES EN ESPECIE: |
|  |  | Este campo se subdivide en cuatro: |
|  |  | 108 SIGNO DE LA PERCEPCIÓN EN ESPECIE: Se cumplimentará este campo cuando el perceptor reintegre en este ejercicio percepciones en especie, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores. |
|  |  | En este caso se consignará una «N», en cualquier otro caso el contenido de este campo será un espacio. |
|  |  | 109-121 VALORACIÓN (De la percepción en especie): Campo numérico de 13 posiciones. Se hará constar sin signo y sin coma decimal, la suma de las valoraciones correspondientes a las percepciones en especie efectivamente satisfechas en el ejercicio al perceptor de que se trate, determinadas con arreglo a lo establecido en el artículo 43 de la Ley del Impuesto y sin incluir en ningún caso el importe del ingreso a cuenta. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 109-119 Parte entera del importe de la valoración, si no tiene contenido se consignará a ceros. |
|  |  | 120-121 Parte decimal del importe de la valoración, si no tiene contenido se consignará a ceros. |
|  |  | 122-134 INGRESOS A CUENTA EFECTUADOS: Campo numérico de 13 posiciones. Se consignará, sin signo y sin coma decimal el importe anual efectivamente ingresado a cuenta por el pagador en relación con las percepciones en especie consignadas en el campo anterior. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 122-132 Parte entera del importe de los ingresos a cuenta efectuados, si no tiene contenido se consignará a ceros. |
|  |  | 133-134 Parte decimal del importe de los ingresos a cuenta efectuados, si no tiene contenido se consignará a ceros. |
|  |  | 135-147 INGRESOS A CUENTA REPERCUTIDOS: Campo numérico de 13 posiciones. Se consignará, sin signo y sin coma decimal el importe anual de los ingresos a cuenta efectuados que, en su caso, el pagador de las retribuciones en especie hubiera repercutido al perceptor. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 135-145 Parte entera del importe de los ingresos a cuenta repercutidos, si no tiene contenido se consignará a ceros. |
|  |  | 146-147 Parte decimal del importe de los ingresos a cuenta repercutidos, si no tiene contenido se consignará a ceros. |
| 148-151 | Numérico | EJERCICIO DEVENGO. |
|  |  | Únicamente se cumplimentará este campo en los supuestos que a continuación se indican: |
|  |  | a) Cuando alguna de las percepciones relacionadas en el resumen anual se refiera a cantidades satisfechas en concepto de atrasos cuyo devengo o exigibilidad corresponda a ejercicios anteriores al que es objeto de declaración. En tal caso, además de cumplimentar los demás datos que procedan, se reflejarán en este campo las cuatro cifras del ejercicio de devengo. Cuando se hayan satisfecho a un mismo perceptor cantidades cuyo devengo corresponda a diferentes ejercicios, el importe de dichas percepciones, así como el de las retenciones practicadas o el de los ingresos a cuenta efectuados, deberá desglosarse en varios apuntes o registros, de forma que cada uno de ellos refleje exclusivamente percepciones y retenciones o ingresos a cuenta correspondientes a devengos de un mismo ejercicio. |
|  |  | b) Cuando se incluyan en el modelo 190 los datos relativos a cantidades reintegradas por sus perceptores en el ejercicio, como consecuencia de haber sido indebida o excesivamente percibidas en ejercicios anteriores. |
|  |  | En estos supuestos, cada reintegro se relacionará bajo la misma clave y, en su caso, subclave de percepción bajo la cual se incluyeron en su día las cantidades indebidas o excesivamente satisfechas, reflejando su importe en el campo «Percepción íntegra» o en el campo «Valoración», según proceda, cumplimentando el campo «Signo de la percepción íntegra» o el campo «Signo de la Valoración», respectivamente, con la letra «N»; consignando (0) en el campo «Retenciones practicadas» o «Ingresos a cuenta efectuados» y haciendo constar en el campo «Ejercicio devengo» el año en el que se hubieran devengado originariamente las percepciones reintegradas. Adicionalmente, si entre los datos de la percepción reintegrada reflejados en su día en el modelo 190 se hubiera incluido alguna cantidad en concepto de «Reducciones», en el campo «Reducciones aplicables» se hará constar, sin signo, el importe de las mismas que corresponda a la cuantía efectivamente reintegrada. |
|  |  | Cuando se hayan producido reintegros procedentes de una misma persona o entidad que correspondan a percepciones originariamente devengadas en varios ejercicios, su importe deberá desglosarse en varios apuntes o registros, de forma que cada uno de ellos refleje exclusivamente reintegros de percepciones correspondientes a un mismo ejercicio. |
|  |  | c) Cuando se trate de prestaciones correspondientes a la clave «D» en las que, de no haber mediado el pago único, el perceptor hubiese tenido derecho a la prestación por desempleo durante un período de tiempo que comprenda más de un ejercicio y que, por tal circunstancia, deban desglosarse en varios apuntes o registros, en el campo «Ejercicio devengo» se anotarán las cuatro cifras del ejercicio a que corresponda cada uno de los registros. |
|  |  | En cualquier otro caso este campo se rellenara a ceros (0). |
| 152 | Numérico | CEUTA O MELILLA. |
|  |  | Se consignará el número 1 en los supuestos en que, por tratarse de rentas obtenidas en Ceuta o Melilla con derecho a la deducción establecida en el artículo 68.4 de la Ley del Impuesto, el pagador hubiera determinado el tipo de retención de acuerdo con lo previsto en los artículos 80.2 y 95.1, último párrafo, del Reglamento del Impuesto. En otro caso se hará constar en este campo el número cero (0). |
| 153-254 |  | DATOS ADICIONALES (Sólo en las claves A, B.01, B.02, C y D). |
|  |  | Para cumplimentar estos datos se atenderá a los que hubieran sido comunicados por el perceptor a la persona o entidad pagadora con arreglo a lo dispuesto en el artículo 88 del Reglamento del Impuesto. |
|  |  | Cuando el tipo de retención hubiera sido objeto de regularización por aplicación de lo previsto en el artículo 87 del Reglamento del Impuesto, se harán constar los datos que hayan sido tenidos en cuenta a efectos de la misma. De haberse efectuado más de una regularización en el ejercicio, se harán constar los datos correspondientes a la última de ellas. |
| 153-156 | Numérico | AÑO DE NACIMIENTO. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Se consignarán las cuatro cifras del año de nacimiento del perceptor. |
| 157 | Numérico | SITUACIÓN FAMILIAR. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Se hará constar el dígito numérico indicativo de la situación familiar del perceptor, de acuerdo con la siguiente relación: |
|  |  | 1. Si el perceptor es soltero, viudo, divorciado o separado legalmente con hijos menores de 18 años o mayores incapacitados sujetos a patria potestad prorrogada o rehabilitada, que conviven exclusivamente con él, siempre que tenga, al menos, un hijo o descendiente con derecho a la aplicación del mínimo por descendientes a que se refiere el artículo 58 de la Ley del Impuesto. |
|  |  | 2. Si el perceptor está casado y no separado legalmente y su cónyuge no tiene rentas anuales superiores a la cuantía a la que se refiere la situación 2ª de las contempladas en el artículo 81.1 del Reglamento del Impuesto. |
|  |  | 3. Si la situación familiar del perceptor es distinta de las anteriores o no deseó manifestarla ante la persona o entidad retenedora. |
| 158-166 | Alfanumérico | NIF DEL CÓNYUGE. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Únicamente en el supuesto de que la «SITUACIÓN FAMILIAR» del perceptor sea la señalada con el número 2, se hará constar el número de identificación fiscal de su cónyuge. |
|  |  | Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. |
|  |  | En cualquier otro caso este campo se rellenara a espacios. |
| 167 | Numérico | DISCAPACIDAD. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02. C y D. |
|  |  | Si el perceptor es una persona con discapacidad que tiene acreditado un grado de minusvalía igualo superior al 33 por 100, se hará constar en este campo el código numérico indicativo de dicho grado. de acuerdo con la siguiente relación: |
|  |  | 0. Si el perceptor no padece ninguna discapacidad o si. padeciéndola, el grado de minusvalía es inferior al 33 por 100. |
|  |  | 1. Si el grado de minusvalía del perceptor es igual o superior al 33 por 100 e inferior al 65 por 100. |
|  |  | 2. Si el grado de minusvalía del perceptor es igual o superior al 33 por 100 e inferior al 65 por 100, siempre que, además, acredite necesitar ayuda de terceras personas o movilidad reducida. |
|  |  | 3. Si el grado de minusvalía del perceptor es igual o superior al 65 por 100. |
| 168 | Numérico | CONTRATO O RELACIÓN. |
|  |  | Sólo para percepciones correspondientes a la clave A. |
|  |  | Tratándose de empleados por cuenta ajena en activo, se hará constar el dígito numérico indicativo del tipo de contrato o relación existente entre el perceptor y la persona o entidad retenedora, de acuerdo con la siguiente relación: |
|  |  | 1. Contrato o relación de carácter general, que comprenderá todas las situaciones no contempladas en los códigos numéricos siguientes. |
|  |  | 2. Contrato o relación de duración inferior al año, con excepción de los supuestos contemplados en el código 4. |
|  |  | 3. Contrato o relación laboral especial de carácter dependiente, con excepción de los rendimientos obtenidos por los penados en las instituciones penitenciarias y de las relaciones laborales de carácter especial que afecten a discapacitados, que se considerarán comprendidos en el código 1. |
|  |  | 4. Relación esporádica propia de los trabajadores manuales que perciben sus retribuciones por peonadas o jornales diarios, a que se refiere la regla 2.ª del artículo 83.2 del Reglamento del Impuesto. |
|  |  | Cuando en un mismo ejercicio se hayan satisfecho al mismo perceptor cantidades que correspondan a diferentes tipos de contrato o relación, el importe de las percepciones, así como el de las retenciones practicadas o el de los ingresos a cuenta efectuados, deberá desglosarse en varios apuntes o registros, de forma que cada uno de ellos refleje exclusivamente percepciones y retenciones o ingresos a cuenta correspondientes a un mismo tipo de contrato o relación. |
|  |  | No obstante, cuando un contrato temporal de duración inferior al año se haya transformado durante el ejercicio en contrato indefinido, el importe total de las percepciones satisfechas, así como el de las retenciones practicadas o el de los ingresos a cuenta efectuados, se reflejará en un único apunte o registro en el cual se hará constar como tipo de contrato o relación el código 1. |
| 169 | Numérico | PROLONGACIÓN ACTIVIDAD LABORAL. |
|  |  | Sólo para percepciones correspondientes a la clave A. |
|  |  | Tratándose de empleados por cuenta ajena en activo (percepciones correspondientes a la clave «A») que tengan derecho en el ejercicio al incremento en la reducción por obtención de rendimientos del trabajo establecido en el artículo 20.2.a) de la Ley del Impuesto para los supuestos de prolongación de la actividad laboral una vez cumplidos los 65 años de edad, se hará constar en esta casilla el número 1. En otro caso, no se cumplimentará esta casilla En otro caso se hará constar en este campo el número cero (0). |
| 170 | Numérico | MOVILIDAD GEOGRÁFICA. |
|  |  | Sólo para percepciones correspondientes a la clave A. |
|  |  | Tratándose de empleados por cuenta ajena en activo (percepciones correspondientes a la clave «A») que tengan derecho en el ejercicio al incremento en la reducción por obtención de rendimientos del trabajo establecido en el artículo 20.2.b) de la Ley del Impuesto para los supuestos de movilidad geográfica previstos en el citado artículo y en el artículo 12.2 del Reglamento del Impuesto, se hará constar en esta casilla el número 1. En otro caso se hará constar en este campo el número cero (0). |
| 171-183 | Numérico | REDUCCIONES APLICABLES. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | De haberse incluido entre las percepciones satisfechas al perceptor de que se trate alguna a la que resulte aplicable cualquiera de las reducciones previstas en los apartados 2 y 3 del artículo 18 o en las disposiciones transitorias 11.ª y 12.ª de la Ley del Impuesto, se consignará en esta casilla el importe de dichas reducciones efectivamente considerado por la persona o entidad pagadora a efectos de determinar el tipo de retención. |
|  |  | Los importes deben consignarle en EUROS. |
|  |  | Este campo se subdivide en dos: |
|  |  | 171-181 Parte entera del importe de las reducciones, si no tiene contenido se consignará a ceros. |
|  |  | 182-18 Parte decimal del importe de las reducciones, si no tiene contenido se consignará a ceros. |
| 184-196 | Numérico | GASTOS DEDUCIBLES. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Se consignará, sin signo y sin coma decimal, el importe anual efectivamente considerado por la persona o entidad pagadora a efectos de determinar el tipo de retención, por los conceptos de gastos a que se refieren las letras a), b) y c) del artículo 19.2 de la Ley del Impuesto (cotizaciones a la Seguridad Social o a mutualidades generales obligatorias de funcionarios, detracciones por derechos pasivos y cotizaciones a Colegios de huérfanos o entidades similares). |
|  |  | Excepcionalmente, este campo también podrá tener contenido en aquellas percepciones correspondientes a las claves L. 05 y L. 10 de las que, pese a estar exentas del IRPF, se hayan detraído cantidades por los citados conceptos que tengan la consideración de gastos deducibles para el perceptor. |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 184-194 Parte entera del importe de los gastos, si no tiene contenido se consignará a ceros. |
|  |  | 195-196 Parte decimal del importe de los gastos, si no tiene contenido se consignará a ceros. |
| 197-209 | Numérico | PENSIONES COMPENSATORIAS. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Se consignará, sin signo y sin coma decimal, el importe anual de la pensión compensatoria que, en su caso, el perceptor estuviese obligado a satisfacer a su cónyuge por resolución judicial. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 197-207 Parte entera del importe de la pensión compensatoria al cónyuge, si no tiene contenido se consignará a ceros. |
|  |  | 208-209 Parte decimal del importe de la pensión compensatoria al cónyuge, si no tiene contenido se consignará a ceros. |
| 210-222 | Numérico | ANUALIDADES POR ALIMENTOS. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Se consignará, sin signo y sin coma decimal, el importe anual de las anualidades por alimentos que, en su caso, el perceptor estuviese obligado a satisfacer a favor de sus hijos por decisión judicial. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | Los importes deben consignarse en EUROS. Este campo se subdivide en dos: |
|  |  | 210-220 Parte entera del importe de las anualidades por alimentos a hijos, si no tiene contenido se consignará a ceros. |
|  |  | 221-222 Parte decimal del importe de las anualidades por alimentos a hijos, si no tiene contenido se consignará a ceros. |
| 223-228 | Numérico | HIJOS Y OTROS DESCENDIENTES. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Datos referidos a los hijos y demás descendientes del perceptor por los que éste tenga derecho a la aplicación del mínimo por descendientes previsto en el artículo 58 de la Ley del Impuesto. |
|  |  | Este campo se subdivide en cuatro: |
|  |  | 223 «< 3 años. N.º Total»: Número de descendientes del perceptor que, dando derecho a éste al mínimo por descendientes, sean menores de 3 años de edad el 31 de diciembre del ejercicio al que corresponda la declaración. Los hijos adoptados y los acogidos se computarán en este campo siempre que la adopción o el acogimiento haya tenido lugar en el ejercicio al que corresponda la declaración o en los dos ejercicios anteriores. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 224 «< 3 años. Por entero»: Se indicará, en su caso, el número de los descendientes menores de 3 años (posición 223) que han sido computados por entero a efectos de determinar el tipo de retención. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 225-226 «Resto. N.º Total»: Número de los demás descendientes del perceptor que, dando derecho a la aplicación del mínimo por descendientes, no estén incluidos en el campo «< 3 años». |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 227-228 «Resto. Por entero»: se indicará, en su caso, el número de los descendientes anteriores (posición 225-226) que han sido computados por entero a efectos de determinar el tipo de retención. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
| 229-240 | Numérico | HIJOS Y OTROS DESCENDIENTES CON DISCAPACIDAD. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Datos relativos a los descendientes del perceptor que, habiendo sido incluidos en alguno de los campos anteriores (posiciones 223-228) por dar derecho a éste a la aplicación del mínimo por descendientes previsto en el artículo 58 de la Ley del Impuesto, den también derecho al mínimo por discapacidad de descendientes contemplado en el artículo 60.2 de la citada Ley, por tratarse de personas con discapacidad que tienen acreditado un grado de minusvalía igual o superior al 33 por 100. |
|  |  | Este campo se subdivide en seis: |
|  |  | 229-230 «≥ 33% y < 65%. N.º Total»: Número de descendientes discapacitados cuyo grado de minusvalía sea igual o superior al 33 por 100 e inferior al 65 por 100. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 231-232 «≥ 33% y < 65%. Por entero»: se indicará, en su caso, el número de los descendientes anteriores (posiciones 229-230) que han sido computados por entero a efectos de determinar el tipo de retención. |
|  |  | En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 233-234 «Movilidad Reducida. N.º Total»: Número de descendientes discapacitados que, habiendo sido incluidos en el campo «≥ 33% Y < 65%» anterior (posiciones 229-230) por tener un grado de minusvalía igual o superior al 33 por 100 e inferior al 65 por 100, acrediten, además, necesitar ayuda de terceras personas o movilidad reducida. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 235-236 «Movilidad Reducida. Por entero»: Se indicará, en su caso, el número de los descendientes anteriores (posiciones 233-234) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 237-238 «≥ 65%. N.º Total»: Número de descendientes discapacitados cuyo grado de minusvalía sea igual o superior al 65 por 100. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 239-240 «≥ 65%. Por entero»: Se indicará, en su caso, el número de los descendientes anteriores (posiciones 237-238) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
| 241-244 | Numérico | ASCENDIENTES. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Datos referidos a los ascendientes del perceptor por los que éste tenga derecho a la aplicación de la reducción por edad prevista en el artículo 59 de la Ley del Impuesto. |
|  |  | Este campo se subdivide en cuatro: |
|  |  | 241 «< 75 años. N.º Total»: Número de ascendientes del perceptor que tengan menos de 75 años de edad el 31 de diciembre del ejercicio al que corresponda la declaración. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 242 «< 75 años. Por entero»: Se indicará, en su caso, el número de los ascendientes anteriores (posición 241) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 243 «≥ 75 años. N.º Total»: Número total de ascendientes del perceptor que tengan 75 o más años de edad el 31 de diciembre del ejercicio al que corresponda la declaración. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 244 «≥ 75 años. Por entero»: se indicará, en su caso, el número de los ascendientes anteriores (posición 243) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
| 245-250 | Numérico | ASCENDIENTES CON DISCAPACIDAD. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Datos relativos a los ascendientes del perceptor que, habiendo sido incluidos en alguna de las casillas anteriores por dar derecho a éste a la aplicación del mínimo por ascendientes previsto en el artículo 59 de la Ley del Impuesto, den también derecho al mínimo por discapacidad de ascendientes contemplado en el artículo 60.2 de la citada Ley, por tratarse de personas con discapacidad que tienen acreditado un grado de minusvalía igual o superior al 33 por 100. |
|  |  | Este campo se subdivide en seis: |
|  |  | 245 «≥ 33% y < 65%. N.º Total»: Número de ascendientes discapacitados cuyo grado de minusvalía sea igual o superior al 33 por 100 e inferior al 65 por 100. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 246 «≥ 33% y < 65%. Por entero»: se indicará, en su caso, el número de los ascendientes anteriores (posición 245) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 247 «Movilidad Reducida. N.º Total»: Número de ascendientes discapacitados que, habiendo sido incluidos en el campo «≥ 33% y < 65%» anterior (posición 245) por tener un grado de minusvalía igual o superior al 33 por 100 e inferior al 65 por 100, acrediten, además, necesitar ayuda de terceras personas o movilidad reducida. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 248 «Movilidad Reducida. Por entero»: Se indicará, en su caso, el número de los ascendientes anteriores (posición 247) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 249 «≥ 65%. N.º Total»: Número de ascendientes discapacitados cuyo grado de minusvalía sea igual o superior al 65 por 100. En cualquier otro caso este campo se rellenará a ceros (0). |
|  |  | 250 «≥ 65%. Por entero»: Se indicará, en su caso, el número de los ascendientes anteriores (posición 249) que han sido computados por entero a efectos de determinar el tipo de retención. En cualquier otro caso este campo se rellenará a ceros (0). |
| 251-253 | Numérico | CÓMPUTO DE LOS 3 PRIMEROS HIJOS. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | Datos referidos a la proporción en la que ha sido computado a efectos de determinar el tipo de retención cada uno de los tres primeros hijos o descendientes del perceptor, ordenados de mayor a menor según su edad, de los previamente incluidos en los campos «< 3 años. N.º Total» (posición 223) y «Resto. N.º Total» (posiciones 225-226). |
|  |  | Este campo se subdivide en tres: |
|  |  | 251 «Hijo 1.º»: Se indicará si el primer hijo ha sido computado por entero o por mitad a efectos de determinar el tipo de retención, de acuerdo a los siguientes valores: |
|  |  | 1: Computado por entero. |
|  |  | 2: Computado por mitad. |
|  |  | 252 «Hijo 2.º»: Se indicará si el segundo hijo ha sido computado por entero o por mitad a efectos de determinar el tipo de retención, de acuerdo a los siguientes valores: |
|  |  | 1: Computado por entero. |
|  |  | 2: Computado por mitad. |
|  |  | 253 «Hijo 3.º»: Se indicará si el tercer hijo ha sido computado por entero o por mitad a efectos de determinar el tipo de retención, de acuerdo a los siguientes valores: |
|  |  | 1: Computado por entero. |
|  |  | 2: Computado por mitad. |
|  |  | En cualquier otro caso estos campos se rellenaran a ceros (0). |
| 254 | Numérico | COMUNICACIÓN PRÉSTAMOS VIVIENDA HABITUAL. |
|  |  | Sólo para percepciones correspondientes a las claves A, B.01, B.02, C y D. |
|  |  | En función de si en algún momento del ejercicio ha resultado de aplicación la reducción del tipo de retención prevista en el artículo 86.1, último párrafo, del Reglamento del Impuesto, por haber comunicado el perceptor que está destinando cantidades a la adquisición o rehabilitación de su vivienda habitual por las que vaya a tener derecho a la deducción por vivienda habitual regulada en el artículo 68.1 de la Ley del Impuesto y por cumplirse los demás requisitos establecidos al efecto, se consignará en este campo la clave que en cada caso proceda de las dos siguientes: |
|  |  | 0: Si en ningún momento del ejercicio ha resultado de aplicación la reducción del tipo de retención. |
|  |  | 1: Si en algún momento del ejercicio ha resultado de aplicación la reducción del tipo de retención. |
| 255-500 | – | BLANCOS. |

* Todos los importes serán positivos.

* Los campos numéricos que no tengan contenido se rellenarán a ceros.

* Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

* Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda.

* Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.
