## ANEXO

## Diseños de registro modelo 283

Diseños de registro a los que deben ajustarse los archivos que se generen para la presentación telemática de la Declaración informativa anual de ayudas recibidas en el marco del Régimen fiscal especial de las Illes Balears, modelo 283

A. Tipo de registro 1: registro de declarante.

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. Constante número '1'. |
| 2-4 | Numérico. | MODELO DECLARACIÓN. Constante '283'. |
| 5-8 | Numérico. | EJERCICIO. Las cuatro cifras del ejercicio fiscal al que corresponde la declaración. |
| 9-17 | Alfanumérico. | NIF DEL DECLARANTE. Se consignará el NIF del declarante. Este campo deberá estar ajustado a la derecha, siendo la última posición el carácter de control y rellenando con ceros las posiciones de la izquierda, de acuerdo con las reglas previstas en el Reglamento general de las actuaciones y los procedimientos de gestión e inspección tributaria y de desarrollo de las normas comunes de los procedimientos de aplicación de los tributos, aprobado por Real Decreto 1065/2007, de 27 de julio (BOE del 5 de septiembre). |
| 18-57 | Alfanumérico. | APELLIDOS Y NOMBRE O RAZÓN SOCIAL DEL DECLARANTE. Si es una persona física se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. Para personas jurídicas y entidades sin personalidad jurídica, se consignará la razón social completa o denominación, sin anagrama. En ningún caso podrá figurar en este campo un nombre comercial. |
| 58 | ‒ | BLANCOS. |
| 59-107 | Alfanumérico | PERSONA CON QUIÉN RELACIONARSE. Datos de la persona con quién relacionarse. Este campo se subdivide en dos: 59-67 TELÉFONO: Campo numérico de 9 posiciones. 68-107 APELLIDOS Y NOMBRE: Se consignará el primer apellido, un espacio, el segundo apellido, un espacio y el nombre completo, necesariamente en este orden. |
| 108-120 | Numérico | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN. Se consignará el número identificativo correspondiente a la declaración. Campo de contenido numérico de 13 posiciones. El número identificativo que habrá de figurar, será un número secuencial cuyos tres primeros dígitos se corresponderán con el código 283. |
| 121-122 | Alfabético. | DECLARACIÓN COMPLEMENTARIA O SUSTITUTIVA. En el caso excepcional de segunda o posterior presentación de declaraciones, deberá cumplimentarse obligatoriamente uno de los siguientes campos: 121 DECLARACIÓN COMPLEMENTARIA: Se consignará una «C» si la presentación de esta declaración tiene por objeto incluir operaciones que, debiendo haber figurado en otra declaración del mismo ejercicio y periodo presentada anteriormente, hubieran sido completamente omitidas en la misma. 122 DECLARACIÓN SUSTITUTIVA: Se consignará una «S» si la presentación tiene como objeto anular y sustituir completamente a otra declaración anterior, del mismo ejercicio y periodo. Una declaración sustitutiva sólo puede anular a una única declaración anterior. |
| 123-135 | Numérico. | NÚMERO IDENTIFICATIVO DE LA DECLARACIÓN ANTERIOR. Campo de contenido numérico de 13 posiciones. En el caso de que se haya consignado una «C» en el campo «Declaración complementaria» o que se haya consignado «S» en el campo «Declaración sustitutiva», se consignará el número identificativo correspondiente a la declaración a la que sustituye. En cualquier otro caso deberá rellenarse a CEROS. |
| 136-144 | Numérico. | NÚMERO TOTAL DE REGISTROS DE AYUDAS. Se consignará el número total de registros de tipo 2 declarados por este declarante. |
| 145 | Numérico. | IDENTIFICACIÓN DEL CONTRIBUYENTE. Se consignará el dígito numérico indicativo de la identificación del contribuyente, de acuerdo con la siguiente relación: 1. Impuesto sobre la Renta de las Personas Físicas. 2. Impuesto sobre Sociedades. 3. Impuesto sobre la Renta de no Residentes con Establecimiento permanente. 4. Impuesto sobre la Renta de no Residentes sin Establecimiento Permanente. |
| 146-500 | ‒ | BLANCOS. |
| * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

B. Tipo de registro 2: registro de ayudas.

| Posiciones | Naturaleza | Descripción de los campos |
| --- | --- | --- |
| 1 | Numérico. | TIPO DE REGISTRO. Constante '2'. |
| 2-4 | Numérico. | MODELO DECLARACIÓN. Constante '283'. |
| 5-8 | Numérico. | EJERCICIO. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 9-17 | Alfanumérico. | NIF DEL DECLARANTE. Consignar lo contenido en estas mismas posiciones del registro de tipo 1. |
| 18-75 | ‒ | BLANCOS. |
| 76-92 | Numérico. | VOLUMEN DE NEGOCIOS. Se consignará el volumen de negocios anual del beneficiario obtenido en las Illes Balears. 76-90 Parte entera del volumen de negocios. 91-92 Parte decimal del volumen de negocios. |
| 93-109 | Numérico. | AYUDA PERCIBIDA Y/O UTILIZADA EN CONCEPTO DE RESERVA PARA INVERSIONES EN LAS ILLES BALEARS. 93-107 Parte entera del importe. 108-109 Parte decimal del importe. |
| 110-126 | Numérico. | AYUDA PERCIBIDA Y/O UTILIZADA EN CONCEPTO DE RÉGIMEN ESPECIAL PARA EMPRESAS INDUSTRIALES, AGRÍCOLAS, GANADERAS Y PESQUERAS EN LAS ILLES BALEARS. 110-124 Parte entera del importe. 125-126 Parte decimal del importe. |
| 127-143 | Numérico. | OTRAS AYUDAS PERCIBIDAS Y/O UTILIZADAS. 127-141 Parte entera del importe. 142-143 Parte decimal del importe. |
| 144-500 | ‒ | BLANCOS. |
| * Los campos numéricos que no tengan contenido se rellenarán a ceros. * Los campos alfanuméricos/alfabéticos que no tengan contenido se rellenarán a blancos. * Todos los campos numéricos ajustados a la derecha y rellenos de ceros por la izquierda. * Todos los campos alfanuméricos/alfabéticos ajustados a la izquierda y rellenos de blancos por la derecha, en mayúsculas, sin caracteres especiales y sin vocales acentuadas, excepto que se especifique lo contrario en la descripción del campo. |

> Redactado conforme a la corrección de errores publicada en BOE núm. 244, de 9 de octubre de 2024. Ref. BOE-A-2024-20398
