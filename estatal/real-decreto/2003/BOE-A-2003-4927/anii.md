## ANEXO II

## Especificaciones del fichero de intercambio

El fichero de intercambio se compone de un registro de cabecera, seguido por los registros de datos del centro.

Estructura del registro de cabecera

| Posición | Campo | Tipo de datos | Tabla de Códigos/Descripción |
| --- | --- | --- | --- |
| 0001-0001 | Identificador de registro de cabecera | a(1) | Valor: «0» |
| 0002-0007 | Envío | aaaaaa(6) | aa ➔ Código de la comunidad autónoma (TABLA 14) aa ➔ Año aa ➔ Número de envío |
| 0008-0015 | Fecha del envío | aaaammdd(8) | aaaa ➔ Año mm ➔ Mes dd ➔ Día |
| 0016-0020 | Número de registros de datos enviados | nnnnn(5) |  |
| 0021-0025 | Número de centros que figuran en el envío | nnnnn(5) |  |
| 0026-2420 | Observaciones | a(2395) |  |

Estru=ctura del registro de datos del centro

| Posición | Campo | Tipo de datos | Tabla de Códigos/Descripción |
| --- | --- | --- | --- |
| 0001-0001 | Identificador de registro de datos | a(1) | Valor: «1» |
| 0002-0007 | Número de envío | aaaaaa(6) | aa ➔ Código de la comunidad autónoma (TABLA 14) aa ➔ Año aa ➔ Número de envío |
| 0008-0012 | Número de orden dentro del envío | nnnnn(5) | Número correlativo |
| 0013-0013 | Tipo de registro enviado | a(1) | TABLA 1 |
| 0014-0015 | Tipo de disposición, si existe. En caso contrario: «II» | aa(2) | TABLA 2 |
| 0016-0031 | Código de la disposición, si existe. En caso contrario: «0000000000000000» | a(16) | Leyes, reales decretos, decretos u órdenes ministeriales que contienen la disposición |
| 0032-0036 | Tipo de publicación en la que aparece la disposición, si existe. En caso contrario: «COM» + «Código de la comunidad autónoma» | aaaaa(5) | TABLA 3 |
| 0037-0044 | Fecha de publicación, si existe. En caso contrario: «fecha de envío» | aaaammdd(8) | aaaa ➔ Año mm ➔ Mes dd ➔ Día |
| 0045-0049 | Número dentro de la publicación, si existe. En caso contrario: «00000» | aaaaa(5) |  |
| 0050-0057 | Fecha de firma, si existe. En caso contrario: «fecha de publicación» | aaaammdd(8) |  |
| 0058-0065 | Fecha de efectividad del registro enviado. Si no existe: «fecha de publicación» | aaaammdd(8) | Solo debe utilizarse cuando tenga que constar en el registro, o bien una situación anterior a la última registrada, o bien una situación cuya efectividad queda postergada a una fecha posterior a la de publicación |
| 0066-0067 | Número de secuencia | nn(2) | Indica la secuencia de registros para un mismo centro y fecha de efectividad Por defecto: 50 |
| 0068-0075 | Código del centro | ppnnnnnd(8) | pp ➔ Cód. Provincia nnnnn ➔ N.º correlativo d ➔ Dígito de control |
| 0076-0375 | Denominación específica. Si no existe: «Blancos» | a(300) |  |
| 0376-0455 | Domicilio | a(80) |  |
| 0456-0460 | Código postal | aaaaa(5) | Código postal que aparece en la guía editada por Correos y Telégrafos |
| 0461-0469 | Código de localidad | aaaaaaaaa(9) | Código de la entidad singular correspondiente, que figura en el Nomenclátor del INE con el formato: ppmmmccss: pp ➔ Provincia mmm ➔ Municipio cc ➔ Entidad colectiva ss ➔ Entidad singular |
| 0470-0472 | Código de la denominación genérica1 | aaa(3) | TABLA 4 |
| 0473-0476 | Código del tipo de centro1 | aaaa(4) | TABLA 5 |
| 0477-0477 | Naturaleza | a(1) | TABLA 6 |
| 0478-0478 | Ámbito | a(1) | TABLA 7 |
| 0479-0928 | Localidades del ámbito, si existen. En caso contrario: «BLANCOS» | a(9)*50=a(450) | Podrán recogerse hasta 50 códigos, en los centros que disponga de ámbito |
| 1-9 | Código INE de localidad | a(9) | Código de la entidad singular correspondiente, que figura en el Nomenclátor del INE con el formato ppmmmccss: pp ➔ Provincia mmm ➔ Municipio cc ➔ Entidad colectiva ss ➔ Entidad singular |
| 0929-0929 | Activo/No-activo | a(1) | TABLA 8 |
| 0930-0937 | Código del centro de dependencia, si existe. En caso contrario: «BLANCOS» | a(8) | pp ➔ Código de la provincia nnnnn ➔ N.º correlativo d ➔ Dígito de control |
| 0938-0938 | Organismo que crea/autoriza el funcionamiento y modalidad del centro | a(1) | TABLA 9 |
| 0939-1520 | Titulares del centro | a(97)*6=a(582) | Hasta 6 titulares. Al menos debe figurar uno. |
| 01-02 | Tipo de titular | a(2) | TABLA 10 |
| 03-17 | NIF/CIF del titular | a(15) |  |
| 18-97 | Nombre del titular | a(80) |  |
| 1521-2420 | Enseñanzas autorizadas | a(18)*50=a(900) | Hasta 50 enseñanzas |
| 01-08 | C ódigo de la enseñanza | a(8) | TABLA 11 |
| 09-09 | Modalidad | a(1) | TABLA 12 |
| 10-10 | Concierto/Convenio. Valor por defecto: «NO» | a(1) | TABLA 13 |
| 11-12 | N.º de unidades autorizadas. Si no se proporciona: «BLANCOS» | nn(2) | Dato no-registral. Se utiliza únicamente en casos convenidos. |
| 13-16 | N.º de puestos escolares. Si no se proporciona: «BLANCOS» | nn(4) | Dato no-registral. Se utiliza únicamente en casos convenidos. |

1 La codificación de estos dos campos es alternativa: si se proporciona la codificación Denominación genérica, el Tipo de centro es deducible (Denominación genérica es un refinamiento de Tipo de centro). Se puede dar solo el Tipo de centro cuando se desconozca o no se utilice la Denominación genérica.

Observaciones:

El registro de cabecera permite el control de los envíos que se producen entre las comunidades autónomas y el Registro estatal de centros docentes no universitarios.

El registro de datos de los centros refleja la situación de un centro, en sus atributos registrales, después de cada disposición o acción administrativa que la correspondiente comunidad autónoma considere que lo ha modificado, dentro del periodo entre dos envíos.

Un centro puede aparecer varias veces en un mismo envío, siempre que cada una de ellas indique una situación distinta.

El orden en que aparezcan los registros de un mismo centro determina la secuencia de las situaciones.

Los datos serán todos de tipo carácter alfanumérico (codificación ASCII): las letras utilizadas en la columna «Tipo de datos» (a, n, p, m...) hacen referencia únicamente al contenido.

Los datos de tipo numérico deberán ir alineados a la derecha. El resto, a la izquierda.

Las tablas que contienen listas de valores y a las que se hace referencia en estas especificaciones técnicas se encuentran en el área de intercambio del registro y podrán ser alteradas alterarse cuando la comisión técnica lo considere oportuno para satisfacer las necesidades que se generen de la propia evolución del sistema educativo, de acuerdo con lo establecido en el presente real decreto.

En consecuencia de lo anterior, el propio registro de intercambio podrá ser alterado a propuesta de la citada comisión.
