## ANEXO IV

## Ficheros de entrada

El sistema cuenta con los siguientes ficheros de entrada:

Fichero de vuelos

El fichero de vuelos contendrá los cupones volados (cupones de vuelo) en el mes que indica el nombre del propio fichero y, en su caso, aquellos cupones volados en meses anteriores que no hayan podido ser incluidos en ficheros de meses pasados. Todos los cupones que compongan un trayecto directo, de ida o vuelta, deberán estar incluidos en un mismo fichero. Será de texto ASCII y contará con una línea de texto por cada cupón facturado. Cada línea (cupón) irá separada por un final de línea tipo DOS: CR y LF (ASCII 13 y ASCII 10, respectivamente). Cada línea (cupón) tendrá 21 campos separados por el carácter «I» (ASCII 124) y un total de 200 caracteres/cupón (incluidos caracteres separadores y terminadores de línea). Los campos tendrán el contenido y formato dados por la siguiente tabla:

| Número de orden | Denominación del campo | Contenido del campo |
| --- | --- | --- |
| 1 | Año facturación. | El año de facturación con cuatro dígitos. Caracteres permitidos: 0 a 9. |
| 2 | Mes facturación. | El número de orden anual del mes de facturación con dos dígitos, correspondiendo el 01 a enero y, consecutivamente, hasta el 12, que corresponde a diciembre. En caso de que el número del mes sea inferior a diez, se añadirá un cero a la izquierda. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 3 | Código compañía. | Código alfanumérico de tres caracteres, que identifica a la compañía responsable de la facturación, que será asignado al acreditarse la compañía como entidad emisora de facturas de cupones de vuelo con derecho a subvención. Si la compañía dispone de código numérico IATA, podrá proponer éste como código de compañía. En caso de que posea más de uno, deberá especificar cuál se desea utilizar. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 4 | Número billete. | El número de billete con doce dígitos. En caso de que el número de dígitos significativos sea menor de 12, se deberá rellenar con ceros a la izquierda hasta completar las doce posiciones. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 5 | Número cupón. | El número del cupón de vuelo con dos dígitos. En caso de que el número sea de un único dígito, se deberá añadir un cero a la izquierda. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 6 | Compañía utilización. | Código alfanumérico de tres caracteres, que identifica a la compañía que realiza el vuelo, que será asignado al acreditarse la compañía como entidad emisora de facturas de cupones de vuelo con derecho a subvención. Si la compañía dispone de código numérico IATA, podrá proponer éste como código de compañía. En caso de que posea más de uno, deberá especificar cuál se desea utilizar. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 7 | Tipo subvención. | Un valor numérico que se corresponde con la tabla siguiente: |
| Canarias-resto del territorio nacional: 1. |
| Baleares-resto del territorio nacional: 2. |
| Interinsular Canarias: 3. |
| Interinsular Balear: 5. |
| Melilla: 6. |
| Ceuta: 7. |
| Obligaciones de servicio público: 8. |
| Caracteres permitidos: 1-8. No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| Esta tabla es susceptible de variación en el futuro. |
| 8 | Denominación tarifa. | Secuencia alfanumérica compuesta por el código de la tarifa registrada y aplicada, seguido por las claves de los descuentos si hubiere. Las dos últimas posiciones contendrán lo siguiente, según la razón de la subvención: |
| Residente Canarias: RC. |
| Residente Baleares: RB. |
| Insular Canarias: IC. |
| Insular Balear: IB. |
| Residente Melilla: RM. |
| Residente Ceuta: RE. |
| El campo deberá estar justificado a la izquierda, rellenándose con espacios (ASCII 32 decimal) hasta completar la longitud del campo. Caracteres permitidos: A-Z, 0-9. |
| 9 | Tarifa cobrada. | Importe de la tarifa cobrada tras aplicar los descuentos correspondientes (excepto el de residente y el de familia numerosa en su caso). Sobre este importe se calculará la subvención y habrá de figurar en pesetas o euros, según sea la moneda en la que se facturó el cupón al pasajero. Las pesetas se redondearán por exceso a la unidad y los euros al céntimo, de acuerdo a la norma establecida. En este último caso el valor aparecerá sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 10 | Importe subvención. | Importe de la subvención facturada. Deberá figurar en la misma moneda que la tarifa cobrada. Las pesetas se redondearán por exceso a la unidad y los euros al céntimo, de acuerdo a la norma establecida. En este último caso el valor aparecerá sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 11 | Fecha emisión billete. | 1. Fecha de emisión del billete en el formato DD/MM/AAAA, en la que: |
| DD es el número de día del mes. Si es inferior a 10, se añadirá un cero a la izquierda. |
| MM es el número del mes. Si es inferior a 10, se añadirá un cero a la izquierda. |
| AAAA es el año con cuatro dígitos. |
| Caracteres permitidos: 0-9 y ’’/’’ (ASCII 47 decimal). |
| Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 12 | Fecha utilización. | 2. Fecha y hora de utilización del cupón en el formato DD/MM/AAAA HH:MM, en la que DD, MM, AAAA se conformarán a lo establecido para el campo 11 y: |
| HH es la hora de comienzo del vuelo en formato 24h. Si es inferior a 10, se añadirá un cero a la izquierda. |
| MM es el minuto de comienzo del vuelo. Si es inferior a 10, se añadirá un cero a la izquierda. |
| El grupo fecha estará separado del grupo hora mediante un único espacio (ASCII 32 decimal). Caracteres permitidos: 0-9, "/’’ (ASCII 47 decimal) y ″/’’ (ASCII 58 decimal). |
| 13 | Origen. | El Código de Identificación de Localidad IATA de tres letras correspondiente al aeropuerto de origen del cupón. En los casos en que existan códigos múltiples para un cierto aeropuerto, se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. |
| 14 | Destino. | El Código de Identificación de Localidad IATA de tres letras correspondiente al aeropuerto de destino del cupón. En los casos en que existan códigos múltiples para un cierto aeropuerto, se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. |
| 15 | Identificación compañía. | Código de identificación del billete para la compañía. Caracteres permitidos: desde ASCII 32 decimal, inclusive, hasta ASCII 127, exclusive. |
| 16 | Tipo de acreditación de residencia. | Tipo de documento de acreditación, con dos dígitos, siendo el situado más a la izquierda un cero (ASCII 48 decimal) presentado según la siguiente tabla: |
| 01 DNI. |
| 02 Tarjeta de Residente. |
| 03 Certificado de Residencia del Ayuntamiento. |
| 04 Certificado de Residencia del Ayuntamiento para menores sin DNI. |
| 05 Senador o Diputado. |
| 06 Certificado de Acuartelamiento Militar. |
| Caracteres permitidos: 0-6. No se aceptará el carácter ″espacio" (ASCII 32 decimal). |
| 17 | Número documento. | El número de DNI o Tarjeta de Residente, incluyendo carácter de comprobación. En caso de que el número de dígitos significativos sea menor de 9, se deberá rellenar con ceros a la izquierda hasta completar las doce posiciones. Caracteres permitidos: 0-9, A-Z. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 18 | Código municipio. | Código del municipio de residencia (según anexo II), o de la circunscripción en el caso de Senador o Diputado, o de la provincia de destino militar activo. |
| Constará de seis caracteres numéricos, incluyendo los ceros no significativos. Caracteres permitidos: 0-9. No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 19 | Tipo moneda. | Moneda utilizada en los campos «Tarifa cobrada» e «Importe subvención». Los valores serán: |
| Peseta: 1. |
| Euro: 2. |
| Caracteres permitidos: 1 ó 2. |
| 20 | Tipo emisión. | El tipo de emisión del cupón puede adoptar los valores: |
| Manual: 0 (ASCII 48 decimal). |
| Automático: Distinto de cero. |
| Caracteres permitidos: 0-9, A-Z, a-z. |
| 21 | Código numérico IATA de agencia. | El código numérico de la lista de Agentes y Localizaciones IATA, con siete dígitos más el dígito de control. |
| Este campo es optativo y cuando no se cumplimente deberán rellenarse las ocho posiciones con ceros. |
| Caracteres permitidos: 0-9. No se aceptará el carácter «espacio» (ASCII 32 decimal). |

El campo «Identificación compañía» es de utilidad a la propia compañía para identificar (o localizar) los billetes o cupones mediante un código interno. Este dato será incluido en todos los listados de billetes remitidos a la compañía (facilitando a ésta la identificación del cupón referido). Por tanto, se rellenará con espacios en blanco cuando no se utilice. La cumplimentación de los demás campos es obligatoria. Cuando el tipo de acreditación corresponda a «Certificado de residencia del Ayuntamiento para menores sin DNI» (tipo codificado 04), el campo número 17, «Número documento», se completará con ceros en las nueve posiciones.

Los campos numéricos irán ajustados a la derecha y rellenos con ceros. Los campos alfanuméricos (son únicamente validos los caracteres ASCII 32 a 255) irán ajustados a la izquierda.

Con objeto de poder realizar las distintas verificaciones en un vuelo subvencionado se facturarán todos los cupones del mismo una vez haya sido volado en su totalidad, reflejando en cada caso la subvención aplicada.

Se informará de cualquier cambio en el formato o contenido de las tablas.

Resumen del formato de la tabla de cupones de vuelo

| Número | Campo | Posición | Longitud | Caracteres permitidos | Justificado |
| --- | --- | --- | --- | --- | --- |
| 0-9 | A-Z | Otros | Espacio |
| 1 | Año facturación | 1-4 | 4 | Sí | No | No | No | Total |
| 2 | Mes facturación | 6-7 | 2 | Sí | No | No | No | Total |
| 3 | Código compañía | 9-11 | 3 | Sí | Sí | No | No | Total |
| 4 | Número billete | 13-24 | 12 | Sí | No | No | No | Relleno 0s |
| 5 | Número cupón | 26-27 | 2 | Sí | No | No | No | Relleno 0s |
| 6 | Compañía utilización | 29-31 | 3 | Sí | Sí | No | No | Total |
| 7 | Tipo subvención | 33 | 1 | 1-8 | No | No | No | Total |
| 8 | Denominación tarifa | 35-50 | 16 | Sí | Sí | No | Sí | Izquierda |
| 9 | Tarifa cobrada | 52-57 | 6 | Sí | No | No | No | Relleno 0s |
| 10 | Importe subvención | 59-64 | 6 | Sí | No | No | No | Relleno 0s |
| 11 | Fecha emisión billete | 66-75 | 10 | Sí | No | ’’/’’ | No | Total |
| 12 | Fecha utilización | 77-92 | 16 | Sí | No | ’’/’’ y ’’:’’ | Sí | Total |
| 13 | Origen | 94-96 | 3 | Sí | Sí | No | No | Total |
| 14 | Destino | 98-100 | 3 | Sí | Sí | No | No | Total |
| 15 | Identificación compañía | 102-165 | 64 | Sí | Sí | >= 32 y <127 | Sí | Izquierda |
| 16 | Tipo de acreditación de identidad | 167-168 | 2 | 0-6 | No | No | No | Relleno 0s |
| 17 | Número documento | 170-178 | 9 | Sí | Sí | No | No | Relleno 0s |
| 18 | Código municipio | 180-185 | 6 | Sí | No | No | No | Relleno 0s |
| 19 | Tipo moneda | 187 | 1 | 1-2 | No | No | No | Total |
| 20 | Tipo emisión | 189 | 1 | Sí | Sí | a-z | Sí | Total |
| 21 | Código numérico IATA de agencia | 191 | 8 | Sí | No | No | No | Relleno 0s |

Fichero de tarifas básicas

El fichero de tarifas básicas contendrá aquellas necesarias para la comprobación de los topes máximos de subvención aplicable a cada cupón facturado en el mes correspondiente. Se incluirán las tarifas básicas relativas a los cupones volados por la compañía emisora y las de los trayectos de cupones de vuelo realizados por otras compañías e incluidos en el fichero de vuelos del mes facturado. No se necesitará proporcionar aquellas tarifas básicas que ya fueron notificadas con anterioridad. Sólo será necesario incluir las tarifas de compañías distintas de la de facturación cuando éstas no hayan sido ya notificadas por la compañía de utilización.

El fichero será de texto ASCII y contará con una línea de texto por cada tarifa básica indicada. Cada línea irá separada por un final de línea tipo DOS: CR y LF (ASCII 13 y ASCII 10 respectivamente). Cada línea tendrá 10 campos separados por el carácter «|» (ASCII 124) y un total de 61 caracteres/tarifa (incluidos caracteres separadores y terminadores de línea). Los campos tendrán el contenido y formato dados por la siguiente tabla:

| Número de orden | Denominación del campo | Contenido del campo |
| --- | --- | --- |
| 1 | Código compañía emisión. | Código alfanumérico de tres caracteres que identifica a la compañía que emite el billete susceptible de subvención. Si la compañía dispone de código numérico IATA, podrá proponer éste como código de compañía. En caso de que posea más de uno, deberá especificar cuál se desea utilizar. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 2 | Código compañía utilización. | Código alfanumérico de tres caracteres que identifica a la compañía que realiza el vuelo. Si la compañía dispone de código numérico IATA, podrá proponer éste como código de compañía. En caso de que posea más de uno, deberá especificar cuál se desea utilizar. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 3 | Origen. | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de origen del trayecto. En los casos en que existan códigos múltiples para un cierto aeropuerto, se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 4 | Destino. | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de destino del trayecto. En los casos en que existan códigos múltiples para un cierto aeropuerto, se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 5 | Vía. | El Código de Identificación de Localidad IATA de tres letras correspondiente a la localidad de tránsito en el trayecto. En los casos en que existan códigos múltiples para un cierto aeropuerto, se indicará cuál es el que deberá figurar en la tabla. Caracteres permitidos: A-Z, 0-9. Nota: Puede emplearse el carácter «espacio» (ASCII 32 decimal) para rellenar las posiciones no ocupadas hasta completar la longitud del campo, en el caso que este campo no fuera de aplicación. |
| 6 | Código tarifa básica. | El código de la tarifa básica utilizado por la compañía que realiza el vuelo. Caracteres permitidos: A-Z, 0-9. Nota: Puede emplearse el carácter «espacio» (ASCII 32 decimal) para rellenar las posiciones no ocupadas hasta completar la longitud del campo. |
| 7 | Tarifa básica. | Importe de la tarifa básica. Deberá figurar en la misma moneda en que se realiza la oferta. Las pesetas se redondearán por exceso a la unidad y los euros al céntimo, de acuerdo a la norma establecida. En este último caso el valor aparecerá sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 8 | Tipo moneda. | Moneda utilizada en el campo «Tarifa básica». Los valores serán: |
| Peseta: 1. |
| Euro: 2. |
| Caracteres permitidos: 1 ó 2. |
| 9 | Fecha de efectividad desde: | Fecha en que se comienza la oferta de la tarifa en el formato DD/MM/AAAA, en la que: |
| DD es el número de día del mes. Si es inferior a 10, se añadirá un cero a la izquierda. |
| MM es el número del mes. Si es inferior a 10, se añadirá un cero a la izquierda. |
| AAAA es el año con cuatro dígitos. |
| Caracteres permitidos: 0-9 y ’’/’’ (ASCII 47 decimal). Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 10 | Fecha de efectividad hasta: | Último día en que se oferta la tarifa en el formato DD/MM/AAAA, en la que DD, MM, AAAA se conformarán a lo establecido para el campo 8 del fichero de tarifas. |

Las fechas de efectividad, es el intervalo en el que se puede emitir billetes con está tarifa básica.

La cumplimentación de todos los campos, salvo «VIA», es obligatoria.

Los campos numéricos irán ajustados a la derecha y rellenos con ceros. Los campos alfanuméricos (son únicamente validos los caracteres ASCII 32 a 127) irán ajustados a la izquierda.

Deberá figurar un registro para el trayecto de ida y otro para el de vuelta en el caso que se oferten ambos trayectos. También deberá figurar un registro independiente por cada tarifa ofertada bien en pesetas, bien en euros, para un mismo trayecto.

Resumen del formato de la tabla de tarifas

| Número | Campo | Posición | Longitud | Caracteres permitidos | Justificado |
| --- | --- | --- | --- | --- | --- |
| 0-9 | A-Z | Otros | Espacio |
| 1 | Código compañía emisión | 1-3 | 3 | Sí | Sí | No | No | Total |
| 2 | Código compañía utilización | 5-7 | 3 | Sí | Sí | No | No | Total |
| 3 | Origen | 9-11 | 3 | Sí | Sí | No | No | Total |
| 4 | Destino | 13-15 | 3 | Sí | Sí | No | No | Total |
| 5 | Vía | 17-19 | 3 | Sí | Sí | No | Sí | Total |
| 6 | Código tarifa básica | 21-28 | 8 | Sí | Sí | No | Sí | Izquierda |
| 7 | Tarifa básica | 30-35 | 6 | Sí | No | No | No | Relleno 0s |
| 8 | Tipo moneda | 37 | 1 | 1-2 | No | No | No | Total |
| 9 | Fecha de efectividad desde: | 39-48 | 10 | Sí | No | ’’/’’ | No | Total |
| 10 | Fecha de efectividad hasta: | 50-59 | 10 | Sí | No | ’’/’’ | No | Total |

## Denominación de los ficheros

Los ficheros se denominarán con la siguiente convención: El nombre estará compuesto de ocho caracteres seguidos de la extensión «.txt». Las posiciones se rellenarán según la tabla siguiente:

| Posición * | Contenido |
| --- | --- |
| 1-3 | El código alfanumérico IATA de la compañía, o bien un código acordado con la DGAC, con tres posiciones. |
| 4-5 | Año del mes de facturación con dos posiciones. |
| 6-7 | Mes de facturación del 01 al 12. |
| 8 | Identificación del fichero según lo siguiente: |
| Una «C» para los ficheros de cupones de vuelos. |
| Una «T» para los ficheros de tarifas básicas. |

* Se justificarán los valores a la derecha de las posiciones, rellenando con ceros a la izquierda de manera que la longitud total del nombre sea siempre de ocho caracteres más la extensión.

> Redactado conforme a la corrección de errores y erratas publicada en BOE núm. 28, de 1 de febrero de 2002. Ref. BOE-A-2002-1994.
