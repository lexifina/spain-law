## ANEXO II

## Especificaciones de la tarjeta sanitaria individual en soporte virtual

1. Imagen de la tarjeta sanitaria virtual.

Esta se adaptará a los modelos referidos en el anexo I, punto 1, anverso.

2. Estructura de los datos del código QR.

La Tarjeta Sanitaria Virtual contendrá datos estructurados. Estos datos se representarán en un código bidimensional.

Los datos siempre comenzarán con una parte común y obligatoria. Después de los datos obligatorios, la administración sanitaria emisora tendrá un espacio libre para uso propio.

a) Datos obligatorios.

Los requisitos que deben asegurarse son los siguientes:

1.º Los datos de la tarjeta sanitaria virtual comenzarán con los siguientes 79 caracteres de la primera pista de la banda magnética:

| Posición | Número de caracteres | Contenido | Observaciones |
| --- | --- | --- | --- |
| 1 | 1 | CI | Centinela de comienzo: carácter ‘%’. |
| 2-17 | 16 | CIP-AUT | CIP asignado por la administración sanitaria emisora de la tarjeta. |
| 18 | 1 | CS | Campo Separador: carácter ‘^’. |
| 19-34 | 16 | CIP-SNS | CIP-SNS único asignado por el Sistema Nacional de Salud. |
| 35 | 1 | CS | Campo Separador: carácter ‘^’. |
| 36-37 | 2 | CITE | Código de identificación de la administración sanitaria emisora de la tarjeta (dos dígitos, el software de lectura convertirá este código al CITE). |
| 38 | 1 | CS | Campo Separador: carácter ‘^’. |
| 39-77 | 39 | Apellidos y nombre | Apellidos y Nombre del titular. En este campo se debe incluir el carácter ‘/’ como separador entre el Apellido Primero y el Apellido Segundo, y entre el Apellido Segundo y el Nombre. El formato sería: ApellidoPrimero/ApellidoSegundo/Nombre. ApellidoPrimero//Nombre (para ApellidoSegundo nulo). |
| 78 | 1 | CF | Centinela Final: carácter ‘?’. |
| 79 | 1 | LRC | Carácter de verificación de Redundancia Longitudinal: carácter ‘espacio’. |

2.º Los datos tendrán una longitud total de 79 caracteres. Será obligatorio respetar el número de caracteres de cada campo.

3.º En los apellidos y el nombre cuando aparece una “ñ” se sustituirá por el valor “$” y la “ç” por el valor “c”.

4.º Cuando apellidos y nombre superan la longitud admitida se le aplicará la función de truncado según las normas establecidas.

5.º Si los datos introducidos en el campo de apellidos y nombre tuvieran una longitud inferior a 39 caracteres, se deberá rellenar con espacios en blanco a la derecha para completar su longitud.

6.º Se indicará el separador “/” entre el primer apellido y el segundo apellido, y también para separar el segundo apellido y el nombre. Si el segundo apellido fuera nulo, no se introducirán caracteres convencionales sustitutivos del mismo y también se incluirá el separador “/”.

7.º El carácter de verificación de Redundancia Longitudinal (LRC) no se calculará. En su lugar siempre se pondrá el carácter “espacio”.

Se recomienda que todas las letras de los datos obligatorios sean mayúsculas.

Ejemplo:

%0000001234004321^BBBBBBBBZB123404^11^APELLIDO1/APELLIDO2/NOMBRE ?

| Número de caracteres | Contenido | Valor codificado |
| --- | --- | --- |
| 1 | CI | % |
| 16 | CIP-AUT | 0000001234004321 |
| 1 | CS | ^ |
| 16 | CIP-SNS | BBBBBBBBZB123404 |
| 1 | CS | ^ |
| 2 | Código de la administración sanitaria emisora | 11 |
| 1 | CS | ^ |
| 39 | Apellidos y Nombre | APELLIDO1/APELLIDO2/NOMBRE |
| 1 | CF | ? |
| 1 | LCR |  |

b) Datos adicionales.

Después de los 79 caracteres obligatorios, cada administración sanitaria emisora podrá introducir datos adicionales de uso libre.

Todas las administraciones sanitarias adaptarán sus rutinas de lectura para que no se produzca un error de lectura de las tarjetas sanitarias virtuales que contengan más de 79 caracteres. Es decir, aunque una administración sanitaria no utilice los datos adicionales, no se ha de producir un error al leer las tarjetas sanitarias virtuales de otras administraciones sanitarias que sí contengan datos adicionales.

Se recomienda que los datos adicionales sólo contengan los caracteres de la tabla del apartado d de este anexo. Si se utilizan caracteres que no figuran en la tabla, se recomienda codificar los datos adicionales en “base45”.

c) Características del código bidimensional.

La generación del código QR se ajustará a los siguientes requisitos:

1.º Se utilizará el formato QR definido en la norma ISO/IEC 18004:2015 para la generación de códigos de barras bidimensional.

2.º Los datos codificados en modo binario utilizarán el juego de caracteres ISO-8859-1 (Latin1).

3.º El código QR tendrá el tamaño (versión) necesario para la longitud de los datos, nivel de corrección de errores y tipo de codificación escogidos.

4.º Se respetará la “quiet zone”: región de 4 módulos de ancho rodeando el código QR por los cuatro lados que estará libre de todas las demás marcas. Su valor nominal de reflectancia será igual al de los módulos luminosos.

Adicionalmente a lo anterior, es recomendable generar el código QR siguiendo los siguientes parámetros:

5.º Se recomienda una tasa de corrección de errores “Q” (alrededor del 25 %).

6.º Se recomienda optimizar el tamaño del código QR usando distintos modos de codificación de caracteres (numérica, alfanumérica y binaria).

7.º Se recomienda que el código QR generado no supere el tamaño de la Versión 14 (73 × 73 módulos).

8.º Se recomienda que, si han de aparecer letras u otros símbolos en la misma pantalla que el código QR, éstos estén lo más alejados posible para no entorpecer la lectura del código.

d) Caracteres codificables para datos adicionales en un código QR en modo alfanumérico.

| Valor codificado | Carácter | Valor codificado | Carácter | Valor codificado | Carácter |
| --- | --- | --- | --- | --- | --- |
| 00 | 0 | 15 | F | 30 | U |
| 01 | 1 | 16 | G | 31 | V |
| 02 | 2 | 17 | H | 32 | W |
| 03 | 3 | 18 | I | 33 | X |
| 04 | 4 | 19 | J | 34 | Y |
| 05 | 5 | 20 | K | 35 | Z |
| 06 | 6 | 21 | L | 36 | Espacio |
| 07 | 7 | 22 | M | 37 | $ |
| 08 | 8 | 23 | N | 38 | % |
| 09 | 9 | 24 | O | 39 | * |
| 10 | A | 25 | P | 40 | + |
| 11 | B | 26 | Q | 41 | - |
| 12 | C | 27 | R | 42 | . |
| 13 | D | 28 | S | 43 | / |
| 14 | E | 29 | T | 44 | : |

> Se añade por el art. único.6 del Real Decreto 922/2024, de 17 de septiembre. Ref. BOE-A-2024-18620
