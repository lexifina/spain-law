## ANEXO IV

## Ficheros de entrada

El Sistema cuenta con los siguientes ficheros de entrada:

Fichero de Vuelos

El fichero de vuelos contendrá los cupones volados {cupones de vuelo y cupones de «cargo por emisión»} en el mes que indica el nombre del propio fichero y, en su caso, aquellos cupones volados en meses anteriores que no hayan podido ser incluidos en ficheros de meses pasados (máximo doce meses). Será de texto ASCII y contará con una línea de texto por cada cupón facturado. Cada línea (cupón) irá separada por un final de línea tipo DOS: CR y LF (ASCII 13 y ASCII 10 respectivamente). Cada línea tendrá 20 campos separados por el carácter «|» (ASCII 124) y un total de 198 caracteres/cupón (incluidos caracteres separadores y terminadores de línea). Los campos tendrán el contenido y formato dados por la siguiente tabla:

| N.º de orden | Denominación del campo | Contenido del campo |
| --- | --- | --- |
| 1 | Año facturación. | El año de facturación con cuatro dígitos. Caracteres permitidos: 0 a 9. |
| 2 | Mes facturación. | El número de orden anual del mes de facturación con dos dígitos, correspondiendo el 01 a enero y, consecutivamente, hasta el 12 que corresponde a diciembre. En caso de que el número del mes sea inferior a diez se añadirá un cero a la izquierda. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 3 | Código compañía. | Código alfanumérico de tres caracteres, que identifica a la compañía responsable de la facturación, que será asignado al acreditarse la compañía como entidad emisora de facturas de cupones de vuelo con derecho a subvención. Si la compañía dispone de código numérico IATA podrá proponer éste como código de compañía. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 4 | Número billete. | El número de billete con doce dígitos. En caso de que el número de dígitos significativos sea menor de 12 se deberá rellenar con ceros a la izquierda hasta completar las doce posiciones. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 5 | Número cupón. | El número del cupón de vuelo con dos dígitos. En caso de que el número sea de un único dígito se deberá añadir un cero a la izquierda. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). '00' para cupón de «cargos por emisión» |
| 6 | Compañía utilización. | Código alfanumérico de tres caracteres, que identifica a la compañía que realiza el vuelo, que será asignado al acreditarse la compañía como entidad emisora de facturas de cupones de vuelo con derecho a subvención. Si la compañía dispone de código numérico IATA podrá proponer éste como código de compañía. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). En el caso de cupones de «cargo por emisión» el valor de este campo debe coincidir con el campo n.º orden 3 «código compañía» |
| 7 | Tipo subvención. | Un valor numérico que se corresponde con la tabla siguiente: Canarias-Resto del Territorio Nacional 01 Baleares-Resto del Territorio Nacional 02 Interinsular Canarias 03 Interinsular Balear 05 Melilla 06 Ceuta 07 Obligaciones de Servicio Público 08 Caracteres permitidos: 0-9. No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 8 | Denominación tarifa. | Secuencia alfanumérica compuesta por el código de la tarifa registrada y aplicada seguido por los códigos de los descuentos, si hubiere. Las dos últimas posiciones contendrán lo siguiente, según la razón de la subvención: Residente Canarias RC Residente Baleares RB Insular Canarias IC Insular Balear IB Residente Melilla RM Residente Ceuta RE El campo deberá estar justificado a la izquierda, rellenándose con espacios (ASCII 32 decimal) hasta completar la longitud del campo. Caracteres permitidos: A-Z, 0-9. |
| 9 | Tarifa cobrada. | Importe en céntimos de euro de la tarifa aplicada o «cargo por emisión» registrado, tras realizar los descuentos comerciales, si los hubiere, (en ningún caso el de residente y el de familia numerosa si coincidiesen ambas circunstancias), redondeado al céntimo de euro. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 10 | Importe subvención. | Importe en céntimos de euro de la subvención facturada, resultante de aplicar el descuento legalmente establecido a la tarifa cobrada o al «cargo por emisión», redondeado igualmente al céntimo de euro. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 11 | Fecha emisión billete. | Fecha de emisión del billete en el formato DD/MM/AAAA en la que: DD es el número de día del mes. Si es inferior a 10 se añadirá un cero a la izquierda. MM es el número del mes. Si es inferior a 10 se añadirá un cero a la izquierda. AAAA es el año con cuatro dígitos. Caracteres permitidos: 0-9 y '/' (ASCII 47 decimal). Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 12 | Fecha utilización. | Fecha y hora de utilización del cupón en el formato DD/MM/AAA HH:MM en la que DD, MM, AAAA se conformarán a lo establecido para el campo 11 y: HH es la hora de comienzo del vuelo en formato 24 h. Si es inferior a 10 se añadirá un cero a la izquierda. MM es el minuto de comienzo del vuelo. Si es inferior a 10 se añadirá un cero a la izquierda. El grupo fecha estará separado del grupo hora mediante un único espacio (ASCII 32 decimal). Caracteres permitidos: 0-9, '/' (ASCII 47 decimal) y ':' (ASCII 58 decimal). En los «cupones de cargo» debe figurar el contenido de «fecha emisión billete» al que se le añade la cadena ' 00:00' |
| 13 | Origen. | El Código de Identificación de Localidad IATA de tres letras correspondiente al aeropuerto de origen del cupón. En los casos en que existan códigos múltiples para un cierto aeropuerto se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. |
| 14 | Destino. | El Código de Identificación de Localidad IATA de tres letras correspondiente al aeropuerto de destino del cupón. En los casos en que existan códigos múltiples para un cierto aeropuerto se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. |
| 15 | Identificación compañía. | Código de identificación del billete para la compañía. Caracteres permitidos: desde ASCII 32 decimal, inclusive, hasta ASCII 127, exclusive. Cuando se trate de «cargo por emisión» en las últimas 13 posiciones debe figurar el numero de billete de primera emisión, con 12 dígitos incluyendo los ceros no significativos, precedido de un espacio. El espacio puede omitirse en el caso de que sea la única información que aparezca en el campo. |
| 16 | Tipo de acreditación de residencia. | Tipo de documento de acreditación, con dos dígitos, siendo el situado más a la izquierda un cero (ASCII 48 decimal) presentado según la siguiente tabla: 01 DNI. 02 Tarjeta de Residente. 03 Certificado de Residencia del Ayuntamiento. 04 Españoles menores 14 años sin DNI. 05 Senador o Diputado. Caracteres permitidos: 0-4. No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 17 | Núm. documento. | El número de DNI o Tarjeta de Residente, incluyendo letra de validación. En caso de que el número de dígitos significativos sea menor de 9 se deberá rellenar con ceros a la izquierda hasta completar las doce posiciones. Caracteres permitidos: 0-9, A-Z. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). Cuando el documento sea de tipo 04, la fecha nacimiento en el formato DDMMAAAA0. |
| 18 | Código municipio. | Código del municipio de residencia (según Anexo II), o de la circunscripción en el caso de Senador o Diputado. Constará de seis caracteres numéricos, incluyendo los ceros no significativos. Caracteres permitidos: 0-9. No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 19 | Tipo emisión. | Caracteres permitidos: A-Z, 0-9 El tipo de emisión del cupón puede adoptar los valores: Manual: 0 (ASCII 48 decimal). Automático: distinto de cero. En el caso de «cupón de cargo» el índice que corresponda en la tabla de Índices de cupones de cargo, registrado por la compañía aérea. |
| 20 | Código numérico IATA de agencia. | El código numérico de la lista de agentes y localizaciones IATA, con siete dígitos más el dígito de control. Este campo es optativo y cuando no se cumplimente deberán rellenarse las ocho posiciones con ceros. Caracteres permitidos: No se aceptará el carácter «espacio» (ASCII 32 decimal). |

El campo «IDENTIFICACIÓN COMPAÑÍA», es de utilidad a la propia compañía para identificar o localizar los cupones mediante un código interno. Este dato será incluido en todos los listados de billetes remitidos a la compañía (facilitando a ésta la identificación del cupón referido). Por tanto se rellenará con espacios en blanco cuando no se utilice. La cumplimentación de los demás campos es obligatoria.

Los campos numéricos irán ajustados a la derecha y rellenos con ceros. Los campos alfanuméricos (son únicamente validos los caracteres ASCII 32 a 255) irán ajustados a la izquierda.

Con objeto de poder realizar las distintas verificaciones en un trayecto directo subvencionado, se facturarán todos los cupones del mismo, una vez haya sido volado en su totalidad y se incluirán en el fichero de vuelos que corresponda, reflejando en cada caso la subvención aplicada.

Resumen del formato de la tabla de cupones de vuelo

| Nº | Campo | Posición | Longitud | Caracteres permitidos | Justificado |
| --- | --- | --- | --- | --- | --- |
| 0-9 | A-Z | Otros | Espacio |
| 1 | Año facturación. | 1 - 4 | 4 | Si | No | No | No | Total |
| 2 | Mes facturacion. | 6 - 7 | 2 | Si | No | No | No | Total |
| 3 | Codigo compañía. | 09-Nov | 3 | Si | Si | No | No | Total |
| 4 | Número billete. | 13 - 24 | 12 | Si | No | No | No | Relleno 0s |
| 5 | Número cupón. | 26 - 27 | 2 | Si | No | No | No | Relleno 0s |
| 6 | Compañía utilización. | 29 - 31 | 3 | Si | Si | No | No | Total |
| 7 | Tipo subvención. | 33 - 34 | 2 | 01-Ago | No | No | No | Total |
| 8 | Denominación tarifa. | 36 - 51 | 16 | Si | Si | No | Si | Izquierda |
| 9 | Tarifa cobrada. | 53 - 58 | 6 | Si | No | No | No | Relleno 0s |
| 10 | Importe subvención. | 60 - 65 | 6 | Si | No | No | No | Relleno 0s |
| 11 | Fecha emisión billete. | 67 - 76 | 10 | Si | No | '/' | No | Total |
| 12 | Fecha utilización. | 78 - 93 | 16 | Si | No | '/' y ':' | No | Total |
| 13 | Origen. | 95 - 97 | 3 | Si | Si | No | No | Total |
| 14 | Destino. | 99 - 101 | 3 | Si | Si | No | No | Total |
| 15 | Identificación compañía. | 103 - 166 | 64 | Si | Si | >= 32 y < 127 | Si | Izquierda |
| 16 | Tipo de acreditación de identidad. | 168- 169 | 2 | 01-May | No | No | No | Relleno 0s |
| 17 | Numero documento. | 171 - 179 | 9 | Si | Si | No | No | Relleno 0s |
| 18 | Código municipio. | 181 - 186 | 6 | Si | No | No | No | Relleno 0s |
| 19 | Tipo emisión. | 188 - 189 | 2 | Si | Si | No | Si | No |
| 20 | Código numérico IATA agencias. | 191 - 198 | 8 | Si | No | No | No | Total |

Fichero de Tarifas Básicas

El fichero de tarifas básicas contendrá aquellas necesarias para la comprobación de los topes máximos de subvención aplicable a cada cupón facturado en el mes correspondiente. Se incluirán las tarifas básicas solo en ida y en ambos sentidos, relativas a los cupones volados por la compañía emisora y las de los trayectos de cupones de vuelo realizados por otras compañías e incluidos en el fichero de vuelos del mes facturado. No se necesitará proporcionar aquellas tarifas básicas que ya fueron notificadas con anterioridad. Sólo será necesario incluir las tarifas de compañías distintas de la de facturación cuando éstas no hayan sido ya notificadas por la compañía de utilización.

Las compañías aéreas que en sus estructuras tarifarias no tengan tarifas básicas, incluirán en este fichero las tarifas más altas de cada una de sus rutas, en las mismas condiciones indicadas anteriormente.

En las tarifas «punto a punto» que tengan dos vías intermedias, se indicará en el campo «VIA» el código del primer aeropuerto de tránsito y en el campo «VIA(2)» el del segundo aeropuerto.

El fichero será de texto ASCII y contará con una línea de texto por cada tarifa básica indicada. Cada línea irá separada por un final de línea tipo DOS: CR y LF (ASCII 13 y ASCII 10 respectivamente). Cada línea tendrá 10 campos separados por el carácter «|» (ASCII 124) y un total de 63 caracteres/tarifa (incluidos caracteres separadores y terminadores de línea). Los campos tendrán el contenido y formato dados por la siguiente tabla:

| N.º de orden | Denominación del campo | Contenido del campo |
| --- | --- | --- |
| 1 | Código compañía emisión | Código alfanumérico de tres caracteres que identifica a la compañía que emite el billete susceptible de subvención. Si la compañía dispone de código numérico IATA podrá proponer éste como código de compañía. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 2 | Código compañía utilación | Código alfanumérico de tres caracteres que identifica a la compañía que realiza el vuelo. Si la compañía dispone de código numérico IATA podrá proponer éste como código de compañía. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 3 | Origen | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de origen del trayecto. En los casos en que existan códigos múltiples para un cierto aeropuerto se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 4 | Destino | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de destino del trayecto. En los casos en que existan códigos múltiples para un cierto aeropuerto se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 5 | Vía | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de tránsito en el trayecto. Caracteres permitidos: A-Z, 0-9. Nota: Puede emplearse el carácter 'espacio' (ASCII 32 decimal) para rellenar las posiciones no ocupadas hasta completar la longitud del campo, en el caso que este campo no fuera de aplicación. |
| 6 | Vía (2) | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de tránsito en el trayecto. Caracteres permitidos: A-Z, 0-9. Nota: Puede emplearse el carácter 'espacio' (ASCII 32 decimal) para rellenar las posiciones no ocupadas hasta completar la longitud del campo, en el caso que este campo no fuera de aplicación. |
| 7 | Código tarifa básica | El código de la tarifa básica utilizado por la compañía que realiza el vuelo. Caracteres permitidos: A-Z, 0-9. Nota: Puede emplearse el carácter 'espacio' (ASCII 32 decimal) para rellenar las posiciones no ocupadas hasta completar la longitud del campo. |
| 8 | Tarifa básica | Importe de la tarifa básica expresado en céntimos de euros, sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 9 | Fecha de efectividad desde | Fecha en que se comienza la oferta de la tarifa en el formato DD/MM/AAAA en la que: DD es el número de día del mes. Si es inferior a 10 se añadirá un cero a la izquierda. MM es el número del mes. Si es inferior a 10 se añadirá un cero a la izquierda. AAAA es el año con cuatro dígitos. Caracteres permitidos: 0-9 y '/' (ASCII 47 decimal). Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). |
| 10 | Fecha de efectividad hasta | Último día en que se oferta la tarifa en el formato DD/MM/AAAA en la que DD, MM, AAAA se conformarán a lo establecido para el campo 8 del fichero de tarifas. |

Las fechas de efectividad, es el intervalo en el que se puede emitir billetes con está tarifa básica.

La cumplimentación de todos los campos es obligatoria. En el caso de tarifas directas los campos «VIA» o «VIA (2)» se rellenarán con espacios en blanco.

Los campos numéricos irán ajustados a la derecha y rellenos con ceros. Los campos alfanuméricos (son únicamente validos los caracteres ASCII 32 a 127) irán ajustados a la izquierda.

Deberá figurar un registro para el trayecto de ida y otro para el de vuelta en el caso de que se oferten ambos trayectos.

Resumen del formato de la tabla de tarifas

| N.º | Campo | Posición | Longitud | Caracteres permitidos |
| --- | --- | --- | --- | --- |
| 0-9 | A-Z | Otros | Espacio | Justificado |
| 1 | Código compañía emisión | 1-3 | 3 | Sí | Sí | No | No | Total. |
| 2 | Código compañía utilización | 5-7 | 3 | Sí | Sí | No | No | Total. |
| 3 | Origen | 9-11 | 3 | Sí | Sí | No | No | Total. |
| 4 | Destino | 13-15 | 3 | Sí | Sí | No | Sí | Total. |
| 5 | Vía | 17-19 | 3 | Sí | Sí | No | Sí | Total. |
| 6 | Vía (2) | 21-23 | 3 | Sí | Sí | No | No | Total. |
| 7 | Código tarifa básica | 25-32 | 8 | Sí | Sí | No | Sí | Izquierda. |
| 8 | Tarifa básica | 34-39 | 6 | Sí | No | No | No | Relleno 0s. |
| 9 | Fecha de efectividad desde | 41-50 | 10 | Sí | No | '/' | No | Total. |
| 10 | Fecha de efectividad hasta | 52-61 | 10 | Sí | No | '/' | No | Total. |

Fichero de índices de «cargos por emisión»

El contenido del fichero de índices de cargos por emisión, deberá coincidir con los registrados y aplicables únicamente a emisión de billetes nacionales. El número de índice no variará si la descripción de dicho cargo no varía.

| Número | Nombre | Contenido |
| --- | --- | --- |
| 1 | Compañía. | Código alfanumérico de compañía (igual que el campo 1 de la tabla de cupones de vuelo). |
| 2 | Índice. | Dos caracteres entre 01 y ZZ con un cero a la izquierda cuando se requiera para completar las dos posiciones. Es el código asignado a la modalidad de emisión registrada con un precio dado. |
| 3 | Precio. | Valor en céntimos de € de la modalidad de emisión, sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter 'espacio' (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 4 | Descripción. | Descripción de la modalidad de emisión que pueda relacionarse con los cargos por emisión registrados. |
| 5 | Fecha. | Fecha de entrada en vigor del cargo, en el formato DD/MM/AAAA. |

Formato de tabla de índices de cargos

| Número | Campo | Posición | Longitud | Caracteres permitidos | Justificado |
| --- | --- | --- | --- | --- | --- |
| 0-9 | A-Z | Otros | Espacio |
| 1 | Compañía | 1-3 | 3 | Sí | Sí |  | No | Total. |
| 2 | Índice | 5-6 | 2 | Sí | No |  | No | Total. |
| 3 | Precio | 8-13 | 6 | Sí | No |  | No | Total. |
| 4 | Descripción | 15-78 | 64 | Sí | Sí |  | Sí | Izquierda. |
| 5 | Fecha | 80-90 | 10 | Sí | No | / | No | Total. |

## Denominación de los ficheros

Los ficheros se denominarán con la siguiente descripción, mas la extensión .txt:

| Posición* | Contenido |
| --- | --- |
| 1-3 | El código alfanumérico IATA de la compañía, o bien un código acordado con la D.G.A.C., con tres posiciones. |
| 4-5 | Año del mes de facturación con dos posiciones. |
| 6-7 | Mes de facturación del 01 al 12. |
| 8/9 | Identificación del fichero según lo siguiente: Una 'C' para los ficheros de cupones de vuelos. Una 'T' para los ficheros de tarifas básicas. En el caso de los ficheros de «índices de cargo» en las posiciones 8-9 deberán figurar los caracteres 'SF'. |

> Se modifica por el art. único.4 y anexo IV del Real Decreto 1340/2007, de 11 de octubre. Ref. BOE-A-2007-18085.

> Redactado conforme a la corrección de errores y erratas publicada en BOE núm. 28, de 1 de febrero de 2002. Ref. BOE-A-2002-1994.
