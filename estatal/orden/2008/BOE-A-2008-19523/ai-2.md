## ANEXO II

## Diseños físicos y lógicos para la presentación del modelo 189 en soporte directamente legible por ordenador

Los soportes directamente legibles por ordenador para la presentación de la Declaración Informativa Anual de Valores, Seguros y Rentas (Modelo 189), habrán de cumplir las siguientes características:

A) Características de los soportes magnéticos.

– Tipo: CD-R (Compact Dic Recordable) de 12 cm.

– Capacidad: hasta 700 MB.

– Formato ISO/IEC DIS 9660:1999, con extensión o sin extensión Joliet.

– No multisesión.

B) Diseños lógicos.

Descripción de los registros.

Para cada declarante se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

Tipo 1: Registro del declarante: Datos identificativos y resumen de la declaración. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

Tipo 2: Registro de declarado. Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros del tipo 2 como declarados tenga la declaración.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación ISO-8859-1. De esta forma la letra «Ñ» tendrá el valor ASCII 209 (Hex. D1) y la «Ç» (cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y está obligado a presentar declaración en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (A.E.A.T.), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la A.E.A.T.

## Modelo 189. Registro de Tipo 1: Registro de declarante

![imagen](https://www.boe.es/datos/imagenes/disp/2008/292/19523_7759372_image5.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/292/19523_7759372_image6.png)

## Modelo 189

A. Tipo de registro 1: Registro de declarante

(Posiciones, naturaleza y descripción de los campos)

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | Tipo de registro. Constante número «1». |
| 2-4 | Numérico. | Modelo declaración. Constante «189». |
| 5-8 | Numérico. | Ejercicio. Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico. | NIF del declarante. Se consignará el NIF del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento general de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, (BOE del 5 de septiembre). |
| 18-57 | Alfanumérico. | Razón social del declarante. Se consignará la razón social completa, sin anagrama. En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | Alfabético. | Tipo de soporte. Se cumplimentará una de las siguientes claves: «C»: Si la información se presenta en CD-R. «T»: Transmisión telemática. |
| 59-107 | Alfanumérico. | Persona con quién relacionarse. Datos de la persona con quién relacionarse. Este campo se subdivide en dos: 59-67 Teléfono: Campo numérico de 9 posiciones. 68-107 Apellidos y nombre: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico. | Número identificativo de la declaración. Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. El número identificativo que habrá de figurar, será un número secuencial cuyos tres primeros dígitos se corresponderán con el código 180. |
| 121-122 | Alfabético. | Declaración complementaria o sustitutiva. En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarse obligatoriamente uno de los siguientes campos: 121 Declaración complementaria: Se consignará una «C» si la presentación de esta declaración tiene por objeto incluir datos que, debiendo haber figurado en otra declaración del mismo ejercicio presentada anteriormente, hubieran sido completamente omitidas en la misma. La modificación del contenido de datos declarados en otra declaración del mismo ejercicio presentada anteriormente se realizará desde el servicio de consulta y modificación de declaraciones informativas en la Oficina Virtual de la Agencia Tributaria (www.agenciatributaria.es). 122 Declaración sustitutiva: Se consignará una «S» si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico. | Número identificativo de la declaración anterior. En el caso de que se haya consignado una «C» en el campo «Declaración complementaria» o que se haya consignado «S» en el campo «Declaración sustitutiva», se consignará el número identificativo correspondiente a la declaración a la que sustituye. En cualquier otro caso deberá rellenarse a ceros. |
| 136-144 | Numérico. | Número total de declarados. Se consignará el número total de declarados en el registro de detalle de tipo 2 por la entidad declarante. Si un mismo declarado figura en varios registros, se computará tantas veces como figure relacionado. (Número de registros de tipo 2). |
| 145–167 | Alfanumérico. | Valoración. Campo alfanumérico de 23 posiciones. Se consignará la suma total de las cantidades reflejadas en el campo Valoración (posición 108 a 123) correspondientes al total de los registros de declarados. En el supuesto de que, en estos registros de declarados, se hubiera consignado «N» en el campo «Signo de la valoración» (posición 108 del registro de tipo 2), las cantidades se computarán con signo menos a efectos de esta suma. Este campo se subdivide en dos: 145 Signo: campo alfabético que se cumplimentará cuando el resultado de la suma a que se acaba de hacer referencia sea menor que 0 (cero); en este caso se consignará una «N». En cualquier otro caso el contenido del campo será un espacio. 146-167 Importe: Campo numérico de 22 posiciones. Se consignará la valoración resultante de la suma a que se ha hecho referencia más arriba. Los importes deben consignarse en euros. La valoración no irá precedida de signo alguno (+/-), ni incluirá coma decimal. Este campo se subdivide en dos: 146-165 Parte entera de la valoración, si no tiene contenido se consignará a ceros. 166-167 Parte decimal de la valoración, si no tiene contenido se consignará a ceros. |
| 168-500 | ‒ | Blancos. |

*Los campos numéricos que no tengan contenido se rellenarán a ceros.

*Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

*Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda.

*Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.

## Modelo 189. Registro de Tipo 2: Registro de declarado

![imagen](https://www.boe.es/datos/imagenes/disp/2008/292/19523_7759372_image7.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2008/292/19523_7759372_image8.png)

B. Tipo de registro 2: Registro de declarado

(Posiciones, naturaleza y descripción de los campos)

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | Tipo de registro. Constante «2». |
| 2-4 | Numérico. | Modelo declaración. Constante «189». |
| 5-8 | Numérico. | Ejercicio. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico. | NIF del declarante. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-26 | Alfanumérico. | NIF del declarado. Si el declarado dispone de NIF asignado en España, se consignará: Si es una persona física se consignará el NIF del declarado de acuerdo con las reglas previstas en el Real Decreto 1065/2007, de 27 de julio, por el que se aprueba el Reglamento General de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, (BOE del 5 de septiembre). Si el declarado es una persona jurídica o una entidad en régimen de atribución de rentas (Comunidad de bienes, Sociedad civil, herencia yacente, etc.), se consignará el número de identificación fiscal correspondiente a la misma. Para la identificación de los menores de 14 años en sus relaciones de naturaleza o con trascendencia tributaria habrán de figurar tanto los datos de la persona menor de 14 años, incluido su número de identificación fiscal, como los de su representante legal. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. Sólo se cumplimentará con los NIF asignados en España. |
| 27-35 | Alfanumérico. | NIF del representante legal. Si el declarado es menor de 14 años se consignará en este campo el número de identificación fiscal de su representante legal (padre, madre o tutor). Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones a la izquierda. En cualquier otro caso el contenido de este campo se rellenará a espacios. |
| 36-75 | Alfanumérico. | Apellidos y nombre, razón social o denominación del declarado. a) Para personas físicas se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este mismo orden. Si el declarado es menor de 14 años, se consignarán en este campo los apellidos y nombre del menor de 14 años. b) Tratándose de personas jurídicas y entidades en régimen de atribución de rentas, se consignará la razón social o denominación completa de la entidad, sin anagramas. |
| 76-77 | Numérico. | Código provincia. En el caso de residentes o de no residentes que operen en territorio español mediante establecimiento permanente, se consignarán los dos dígitos numéricos que correspondan a la provincia o, en su caso, ciudad autónoma, del domicilio fiscal del declarado según la relación siguiente: Álava 01 León 24 Albacete 02 Lleida 25 Alicante 03 Lugo 27 Almería 04 Madrid 28 Asturias 33 Málaga 29 Ávila 05 Melilla 52 Badajoz 06 Murcia 30 Barcelona 08 Navarra 31 Burgos 09 Ourense 32 Cáceres 10 Palencia 34 Cádiz 11 Palmas, Las 35 Cantabria 39 Pontevedra 36 Castellón 12 Rioja, La 26 Ceuta 51 Salamanca 37 Ciudad Real 13 S. C. Tenerife 38 Córdoba 14 Segovia 40 Coruña, A 15 Sevilla 41 Cuenca 16 Soria 42 Girona 17 Tarragona 43 Granada 18 Teruel 44 Guadalajara 19 Toledo 45 Guipúzcoa 20 Valencia 46 Huelva 21 Valladolid 47 Huesca 22 Vizcaya 48 Illes Balears 07 Zamora 49 Jaén 23 Zaragoza 50 En el caso de no residentes que no operen en territorio español mediante establecimiento permanente, se consignará 99. |
| 78-79 | Alfabético. | Código país. En el caso de no residentes que operen en territorio español sin establecimiento permanente se consignarán el código que corresponda al país o territorio de residencia del declarado, de acuerdo con los códigos alfabéticos de países y territorios que figuran en la Orden EHA/3202/2008, de 31 de octubre, en su Anexo IV (BOE 10 de noviembre de 2008). En el caso de residentes o de no residentes que operen en territorio español mediante establecimiento permanente, las posiciones 78 a 79 se consignarán a blancos. |
| 80 | Alfabético. | Clave de mercado. Se consignará una de las claves siguientes: Clave descripción: A Mercado secundario oficial de valores español. B Mercado secundario oficial de valores extranjeros. C Otros mercados nacionales. D Otros mercados extranjeros. |
| 81 | Alfabético. | Clave de valor. Se consignará una de las claves siguientes: Clave descripción: A Acciones o participaciones en el capital o en los fondos propios de entidades jurídicas negociados en un mercado organizado. B Valores representativos de la cesión a terceros de capitales propios negociados en mercados organizados. C Acciones o participaciones en el capital social o fondo patrimonial de una institución de inversión colectiva. D Seguros de Vida (limitados a los que tengan valor de rescate). Cuando las rentas temporales o vitalicias derivadas de seguros de vida o invalidez tengan valor de rescate a 31 de diciembre éste se hará constar en la Clave D. E Renta temporal o vitalicia. Únicamente se hará constar el valor de capitalización a 31 de diciembre, calculado de acuerdo con lo dispuesto en el artículo 17 de la Ley 19/1991, del Impuesto sobre el Patrimonio, de las rentas temporales o vitalicias que no deriven de seguros de vida o invalidez (rentas temporales o vitalicias que tengan por causa la imposición de capitales a las que se refiere el artículo 25.3, letra b) de la Ley del IRPF). No deberá suministrarse información relativa a los seguros de vida que cubran exclusivamente el riesgo de muerte (sin perjuicio de que puedan cubrir riesgos complementarios comprendidos en otros ramos distintos al de vida) y que no tengan valor de rescate. No deberá suministrarse información respecto de los planes de previsión asegurados, planes de previsión social empresarial, contratos de seguro colectivo que instrumenten compromisos por pensiones ni de los seguros privados de dependencia. |
| 82 | Numérico. | Clave de identificación. Se consignará una de las claves siguientes: Clave descripción: 1 Identificación por código ISIN (código de 12 posiciones). 2 Valores extranjeros sin código ISIN. 3 Identificación por NIF. Sólo se informará este campo cuando en el campo «Clave de Valor» (posición 81) se haya consignado «A», «B» o «C» |
| 83-94 | Alfanumérico. | Identificación de los valores. Se hará constar: 1. El código ISIN, configurado de acuerdo a la Norma Técnica 1/1998, de 16 de diciembre, de la Comisión Nacional del Mercado de Valores y la Circular 6/1998, de 16 de Diciembre, de la Comisión Nacional del mercado de Valores (supuesto de Campo «Clave de identificación», posición 82, configurado con valor 1). 2. Para valores extranjeros que tengan asignado ISIN se hará constar éste en todo caso. En los demás casos, se reflejará la clave «ZXX», siendo «XX» el código del país emisor de acuerdo con los códigos alfabéticos de países y territorios que figuran en la Orden EHA/3202/2008, de 31 de octubre, en su Anexo IV (BOE de 10 de noviembre de 2008), en el supuesto de campo «Clave de identificación», posición 82, configurado con valor 2. 3. En defecto de código ISIN, se consignará el Número de Identificación Fiscal, otorgado por la Agencia Estatal de Administración Tributaria (supuesto de campo «Clave de identificación», posición 82, configurado con valor 3). Únicamente se informará este campo si en el campo «Clave de valor», posición 81, se ha consignado «A», «B» o «C». |
| 95 | Alfabético. | Clave de representación. Se consignará una de las claves siguientes: Clave descripción: A Valores representados mediante anotaciones en cuenta. B Valores no representados mediante anotaciones en cuenta. |
| 96-107 | Numérico. | Número de valores. Se consignará el número de acciones o participaciones en el capital o en los fondos propios de entidades jurídicas negociados en un mercado organizado, de valores representativos de la cesión a terceros de capitales propios negociados en mercados organizados o de acciones o participaciones en el capital social o fondo patrimonial de una institución de inversión colectiva. Solo se informará este campo cuando en el campo «Clave de valor», posición 81, se haya consignado «A», «B» o «C». Se subdivide en dos campos: 96-105 Parte entera de los valores. 106-107 Parte decimal de los valores (si no tiene, se configurará a ceros). Asimismo, cuando existen múltiples declarados, se consignará, en cada uno, el número de valores imputados a cada uno de ellos en función del porcentaje de su participación. |
| 108-123 | Alfanumérico. | Valoración. Se hará constar el valor de los activos declarados en euros o su contravalor en los casos de operaciones en divisa, asimismo cuando existan múltiples partícipes asociados a la operación se consignará en cada uno, el valor imputable a cada uno de ellos en función del porcentaje de participación. En los supuestos en que se haya consignado una «A» o «B» en el campo «Clave de valor», posición 81, el valor de las acciones, participaciones o valores representativos de la cesión a terceros de capitales propios, se calculará conforme a lo dispuesto en el artículo 15 de la Ley 19/1991, de 6 de junio, del Impuesto sobre el Patrimonio. En los supuestos en que se haya consignado una «C» en el campo «Clave de valor», el valor liquidativo a 31 de Diciembre se calculará de acuerdo a lo dispuesto en la Ley 35/2003, de 4 de Noviembre, de Instituciones de Inversión Colectiva y en su normativa de desarrollo. En los supuestos en que se haya consignado una «D» en el campo «Clave de valor», se hará constar el valor de rescate a 31 de diciembre. En los supuestos en que se haya consignado una «E» en el campo «Clave de valor», el valor de capitalización a 31 de diciembre, se calculará de acuerdo con lo dispuesto en el artículo 17 de la Ley 19/1991, de 6 de junio, del Impuesto sobre el Patrimonio. Este campo se subdivide en dos: 108 Signo: Campo alfabético que se cumplimentará cuando el resultado de la valoración a que se acaba de hacer referencia sea menor que 0 (cero); en este caso se consignará una «N». En cualquier otro caso el contenido del campo será un espacio. 109-123 Importe: Campo numérico de 15 posiciones. Se consignará el importe resultante de la valoración a que se ha hecho referencia más arriba. Los importes deben consignarse en euros. El importe no irá precedido de signo alguno (+/-), ni incluirá coma decimal. Este campo se subdivide en dos: 109-121 Parte entera del importe, si no tiene contenido se consignará a ceros. 122-123 Parte decimal del importe, si no tiene contenido se consignará a ceros. Asimismo, cuando existen múltiples declarados, se consignará, en cada uno, la valoración de cada uno de ellos en función del porcentaje de su participación. |
| 124-128 | Numérico. | Porcentaje de participación. Se consignará el porcentaje de titularidad de los valores, seguros o rentas. Se subdivide en dos campos: 124-126 Parte entera del porcentaje; si no tiene contenido, se consignará a ceros. 127-128 Parte decimal del porcentaje; Figurará la parte decimal del porcentaje; si no tiene contenido se consignará a ceros. |
| 129-500 | ‒ | Blancos. |

*Los campos numéricos que no tengan contenido se rellenarán a ceros.

*Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos.

*Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda.

*Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo.
