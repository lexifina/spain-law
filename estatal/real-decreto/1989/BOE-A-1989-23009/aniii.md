## ANEXO III

## NORMA TÉCNICA PARA LA DIFUSIÓN DEL SERVICIO DE VALOR AÑADIDO DE TELETEXTO

1. OBJETO.

La presente norma tiene por objeto determinar las características para la difusión del servicio de valor añadido de teletexto adoptado por el Estado español.

2. DEFINICIONES.

2.1 Servicio de valor añadido de teletexto:

Servicio de difusión de datos digitales que puede transmitirse dentro de la estructura de una señal analógica de televisión, o utilizando una modulación digital.

Está destinado primordialmente a la visualización de textos o material gráfico en forma bidimensional, reconstruidos a partir de datos codificados en la pantalla de receptores de televisión adecuadamente equipados.

2.2 Línea de datos:

Una línea de datos es una línea de televisión cuya parte activa se asigna a datos digitales. El contenido de los datos se subdivide en una secuencia de sincronización de los bits seguida de una unidad de datos.

2.3 Unidad de datos:

Una unidad de datos es una unidad lógica de datos, subdividida en una secuencia de sincronización de bytes (octetos) y un paquete de datos.

2.4 Paquete de datos:

Un paquete de datos es un conjunto identificable de información que comprende:

– un prefijo que permite funciones como las de direccionamiento, indicación del tamaño del paquete, indicación de continuidad del paquete y designación del tipo de paquete;

– un bloque de datos que contiene señales de control o información del usuario;

– en algunos sistemas un sufijo para efectuar la función de detección o corrección de errores en el nivel de paquetes.

2.5 Grupo de datos:

Un grupo de datos es un grupo identificable de bloques de datos que contienen información de una misma fuente.

2.6 Codificación alfanumérica:

Estos códigos se utilizan para visualizar textos. Los elementos gráficos alfanuméricos comprenden letras del alfabeto, caracteres silábicos Y caracteres ideográficos con o sin signos diacríticos, figuras, signos de puntuación y signos especiales.

2.7 Codificación mosaica:

Estos códigos se utilizan para construir dibujos mediante caracteres mosaicos por bloques, mosaicos suavizados y para trazado de líneas. Cada elemento define parte de un diagrama y ocupa una posición de carácter. Se definen dos formas de presentación:

– separada: cada elemento está rodeado por un borde del color de fondo;

– contigua: los elementos lindan unos con otros.

3. ESPECIFICACIONES DEL SERVICIO DE TELETEXTO.

3.1 Se utilizará para el Servicio de teletexto en España un sistema de formato fijo, con un cuadro de 128 caracteres alfanuméricos, de empleo simultáneo dentro de una misma página de información.

Esta característica es absolutamente necesaria a fin de que sea posible la escritura de textos en todas las lenguas oficiales españolas, bien por separado o combinados varios de dichos caracteres en una misma página.

3.1.1 Se utilizarán para la transmisión de las señales Teletexto, las líneas libres existentes en el borrado vertical de cada trama, es decir, las líneas comprendidas entre la 7 y 22 en la primera trama, y la 320 y 335 en la segunda trama, teniendo en cuenta las líneas actualmente ocupadas con señales de prueba internacionalmente adoptada.

3.1.2 Cuando las señales Teletexto no se multiplexen con la señal de imagen de Televisión, se podrán usar cualesquiera líneas de cada trama, excepto las ocupadas por el sincronismo de trama y los impulsos de igualación.

3.2 Identificación de datos:

Se hará por medio de la señal de sincronización de bits y el código de sincronización de objetos, según figura 1.

3.3 El método de señalización será por impulsos binarios NRZ (sin retorno a cero).

3.4 Niveles de las señales:

Los niveles de los impulsos, en el sistema de modulación negativa de uso en España, serán de: Nivel de negro ± 2% para el nivel 0 lógico y del 66 (± 6) % de la diferencia entre el nivel de negro y de blanco de la señal de TV para el nivel 1 lógico.

3.5 La velocidad binaria de transmisión será 444 × fH (6,9375 Mbits/s ± 25 ppm) (fH = frecuencia nominal de línea).

3.6 El punto de referencia para le temporización de los datos será el nivel máximo del penúltimo «1» de la señal de sincronismo de bits.

3.7 Espectro de los impulsos de datos:

Existirá simetría oblicua en torno e 0’5 × velocidad binaria, esencialmente cero para 5 MHz.

3.8 El contenido de una línea de datos será de 360 bits, formando estos 45 octetos.

Este contenido de datos representará un renglón de escritura de texto sobre la pantalla.

3.9 El sincronismo de las distintas señales empleadas se muestra en la figura 1.

3.9.1 Según dicha figura 1 la sincronización de bits se hará por medio de los octetos 1 y 2, que comienzan 10101010 ... Paridad par.

3.9.2 La sincronización de octetos se hará por medio del octeto 3, de forma 11100100, paridad Par.

3.10 El direccionamiento de gaceta y paquete queda expresado en las figuras 1 y 2.

3.10.1 Formato de numeración de piquetes para cualquier línea de datos.

Este formato será X/Y, siendo X el número de gaceta e Y el de renglón.

Vendrán dado por los octetos 4 y 5 con protección Hamming, empleando 3 bits para el número de gaceta X y 5 bits para el número de renglón Y.

3.10.2 Lineas de datos de encabezamiento de página. Formados por paquetes con numeración X/O. Ver apéndice 2.

3.10.2.1 El número de página vendrá dado por los octetos 6 y 7 con protección Hemming.

3.10.2.2 El subcódigo de página vendrá dado por los octetos 8, 9, 10 y 11 con protección Hamming.

El bit 8 del octeto 9 será el bit de control Cd, y los bits 6 y 8 del octeto 11 serán, respectivamente, los bits de control C5 y C6. Ver apartado siguiente.

3.11 El decodificador en el Teletexto español responderá:

a) Paquetes con numeración X/C e X/24. X/27 y E/3C.

b) Página 00 a 99 codificada DCS (decimal codificado en binario).

c) Subcódigos de página. Los cuatro dígitos del subcódigo podrán tomar los valores 0 a 3; D a 9; 0 a 7 y 0 a 9, respectivamente.

d) Paquetes con numeración X/26 para extensión del repertorio de caracteres.

3.11.1 Los bits de control en el encabezamiento de página serán C4 a C14, activos cuando están puestos a 1. Los octetos 12 y 13 contendrán los bits C7 a C14 con protección Hamming. Para los bits C0 a C6 ver apartado 3.10.2.2.

3.11.1.1 El bit C6 será el de borrado de página, seguido siempre de un intervalo de 20 mseg. antes de la transmisión de nuevos datos. Ver apéndice 2.

3.11.1.2 Bit C5 corresponderá a noticias urgentes. Toda información de este género deberá enmarcarse.

3.11.1.3 Bit C6, correspondiente a página de subtítulos. También deberá enmarcarse toda información de subtítulo.

3.11.1.4 Bit C7, correspondiente a la supresión del encabezamiento. Podrá suprimirse éste a voluntad, visualizándose opcionalmente la hora.

3.11.1.5 Bit C8, indicador de actualización. Los datos que le sigan podrán Incluir únicamente la parte actualizada de la página.

3.11.1.6 Bit C9, de secuencia interrumpida. La página asociada no seguirá el orden numérico de las páginas.

3.11.1.7 Bit C10, de inhibición de visualización. Los datos no serán visualizados.

3.11.1.8 Bit C11, para transmisión de gacetas en serie. Éstas se transmitirán una a una, por orden.

3.11.1.9 Bits C12, C13 y C14, de selección del juego básico de caracteres.

En el caso del Sistema de Teletexto a emplear en España, estos tres bits tendrán, respectivamente, los valores 1, 0, 1,

3.11.2 Una página visualizada sobre la pantalla se compondría de 25 renglones.

3.11.2.1 Las renglones visualizados corresponderán a paquetes de datos con numeración X/0 a X/24, que harán posible la visualización de los renglones 0 a 24 de una página de la gaceta X.

La visualización del paquete 24 sólo se permitirá cuando el paquete X/27 se trasmita a su vez con el bit 4 del octeto 43 puesto a 1.

El paquete 24 podrá contener indicadores coloreados para facilitar al usuario el acceso a páginas encadenadas, mediante teclas de su mando a distancia asociadas a dichos colores (ver apartado 3.12.1.3.2.1).

3.11.2.2 Casillas de carácter en los renglones 1 a 24.

Serán 40, transmitidas de izquierda a derecha.

3.11.2.3 Casillas de carácter de encabezamiento de página, renglón 0.

Serán 32, transmitidas de izquierda a derecha.

3.11.3 Octeto de carácter.

Compuesto por 7 bits de paridad impar, definirán un carácter visualizable de control, que ocupará una casilla.

3.11.4 Juegos de caracteres para visualización, transmitidos en los paquetes X/0 a X/24.

a) 94 caracteres alfanuméricos más ESPACIO Y SUPRESION (ver cuadro 60 con opción para el idioma español: figuras 3 y 3 A).

b) 63 caracteres gráficos mosaicos contiguos más ESPACIO y 32 caracteres alfanuméricos.

c) 63 caracteres gráficos mosaicos separados más ESPACIO y 32 caracteres alfanuméricos (ver juego de caracteres mosaicos de la figura 4).

La selección entre a, b y c se efectuará mediante caracteres de control según apartado 3.11.5.

3.11.5 Juegos de caracteres de control.

Constarán de 29 caracteres de control que definirán características de visualización. Al comienzo de cada renglón, el receptor adoptará los atributos por defecto (ver figura 5). Algunos caracteres de control producirán su efecto inmediatamente y otros en la casilla siguientes.

3.11.5.1 Color de primer plano.

Podrá ser uno de los siguientes: blanco, amarillo, cyan, verde, violeta, rojo, azul y negro. Designados al seleccionar el modo de visualización alfanumérico o mosaico (ver figura 5).

3.11.5.2 Color de fondo de una casilla.

Podrá ser uno de los calores de primer plano del apartado anterior.

3.11.5.2.1 Fondo negro.

Será designado por un carácter de control «fondo negro».

3.11.5.2.2 Nuevo fondo.

Este carácter de control hará que el color de primer plano se adopte como color de fondo.

3.11.5.3 Caracteres gráficos mosaicos contiguos.

Los bloques mosaicos irán uno al lado del otro, sin separación entre ellos.

3.11.5.4 Caracteres gráficos mosaicos separados.

Cada bloque mosaico estará rodeado de un borde del color de fondo.

3.11.5.5 Retención de mosaico.

Se visualizará un carácter de modelo, retenido en lugar del carácter ESPACIO correspondiente a un carácter de control. El carácter retenido estará definido únicamente durante el modo mosaico. Será el carácter más reciente con el bit 6 igual a 1 en su código, siempre y cuando no se produzcan un cambio en los modos alfanumérico/mosaico o altura normal/doble. Se visualizará en el modo original, ya sea contiguo o separado.

3.11.5.6 Ocultación.

Los caracteres que le sigan habrán de visualizarse como ESPACIO hasta que sean «revelados» por una operación del decodificador o del usuario.

3.11.5.7 Intermitencia.

Los caracteres que le sigan habrán de presentarse de forma normal y como ESPACIO alternadamente, bajo el control de un dispositivo de temporización incorporado en el receptor.

3.11.5.8 Enmarcado.

Parte de una página que habrá de insertarse en la imagen normal de televisión. La protección contra una falsa operación se obtendrá mediante la transmisión repetida del carácter de control.

3.11.5.9 Altura doble.

Las caracteres se extenderán verticalmente para ocupar la casilla correspondiente en el renglón inferior; éste presentará el mismo color de fondo que el anterior.

3.12.

Datos auxiliares relacionados con el texto, que se detallan en los apartados siguientes: apartado 3.12.1 y siguientes.

3.12.1.

Páginas encadenadas relacionadas con una página determinada y destinados a ser almacenadas automáticamente en la memoria del decodificador.

Responderán a los datos contenidos en el paquete X/27 (ver figura 2).

3.12.1.1 Secuencia de sincronización de bits, código de sincronismo de octeto y dirección de paquete.

Formados por los octetos 1 a 5 inclusive. Ver apartados 3.9 y 3.10.

3.12.1.2 Código de designación,

Formado por el octeto 6, con cuatro bits de datos más 4 bits de protección Hamming. El código 0000 designará la función de página encadenada (ver figura 2).

3.12.1.3 Direcciones de páginas encadenadas.

Loa octetos 7 a 42 se organizarán como 6 grupos de 6 octetos. Cada grupo de 6 octetos definirá le dirección de una página encadenada. Estos grupos se numerarán del 0 al 5 en orden de transmisión.

El bit 4 del octeto 43 puesto a 1, definirá las páginas encadenadas codificadas por colores, y se les asignará el significado siguiente: Los grupos 0 a 3 corresponderán a páginas encadenadas roja, verde, amarilla y cyan, respectivamente. El grupo 5 corresponderá al índice de encadenamiento que deberá estar siempre presente.

3.12.1.3.1 Formato de grupos de datos para definir una página encadenada.

Constará de 6 octetos que contendrán.

| Número de gaceta relativa | 3 bits |
| --- | --- |
| Número de página | 8 bits |
| Subcódigo de página | 13 hits |
| Código Hamming | 24 bits |

Para la secuencia de bits véase la figura 2.

Cuando no haya de especificarse un subcódigo de página, se transmitirá la dirección de subcódigo de página 3F y 7F (hexadecimal).

Cuando se transmita el código FF 3F y 7F no se especificará página.

3.12.1.3.2 Control encadenado.

Formado por el octeto 43, con 4 bits de datos más 4 bits de protección Namming.

3.12.1.3.2.1 Cuando el bit 4 está puesto a 1, implicará que las páginas encadenadas quedan asociadas a los indicadores coloreados del paquete X/24. La tecla roja estará siempre habilitada, las teclas verde, amarilla y cyan lo estarán también si los respectivos bits de datos 1, 2 y 3 se ponen a 1. La tecla de índice estará siempre habilitada.

Cuando el bit 4 esté puesto a 0 no habrá páginas encadenadas asociadas a los indicadores coloreados, y no se visualizará ningún paquete X/24.

3.12.1.4 Palabra de verificación de la página básica.

Los octetos 44 y 45 contendrán la palabra de verificación por redundancia cíclica de los datos de los paquetes X/0 a X/25. Para la generación de esta palabra ver figura 7.

3.13 Paquetes de datos de servicio de radiodifusión.

Será el paquete 8/30. Que se transmitirá aproximadamente una vez por segundo (figura 2).

3.13.1 Secuencia de sincronismo de bits, código de sincronismo de octetos y dirección de paquete.

Serán las octetos 1 a 5 inclusive, según los apartados 3.9 y 3.10.

3.13.2 Código de designación.

Será el octeto 6, con 4 bits de datos más 4 bits de protección Hamming. El primer bit de datos puesto a 0 significará función multiplexada, como en el apartado 3.1.1. El primer bit de datos puesto a 1 significa función no multiplexada, como en el articulo 3.1.2. Los bits de datos 2, 3 y 4 puestos a 0, designarán las funcionas relacionadas en los apartados 3.13.3 a 3.13.9. Sin respuesta a otros códigos.

3.13.3 Página inicial de Teletexto para almacenamiento en el decodificador sin operación del usuario.

Los octetos 7 a 12 contendrán la dirección de la página inicial:

| Número de gaceta relativo | 3 bits |
| --- | --- |
| Número de página | 8 bits |
| Subcódigo de página | 13 hits |
| Protección Hamming | 24 bits |

Para la secuencia de bits, véase le figura 2.

Cuando no se especifique un subcódlgo de página, se transmitirá la dirección de subcódigo de página 3F y 7F (hexadecimal). Cuando se transmite el código FF 3F 7F no se especificará la página.

3.13.4 Identificación de emisora.

Los octetos 13 y 14 contendrán un código asignado que identifique de forma única a la emisora.

3.13.5 Código de diferencia horaria.

El octeto 15 definirá la diferencia «en unidades de media hora» entre la hora local y el tiempo universal coordinado (UTC). Las diferencias negativas corresponderán al oeste de Greenwich. Ver figura 8.

3.13.6 Fecha del calendario Juliano (MJD).

Corresponderá a los octetos 16 a 18. Será un número de 5 dígitos que definirá la fecha del calendario Juliano (MJD).

Será aumentada diariamente a media noche UTC, con punto de referencia en 31-1-1982, en que MJD a 45.000. Ver figura 8.

3.13.7 Tiempo universal coordinado (UTC).

Corresponderá a los octetos 19 a 21. Será un número de 6 dígitos que definirá la UTC. La transmisión se referirá al segundo próximo inmediato. Ver figura 8.

3.13.8 Etiqueta del programa de TV.

Corresponderá a los octetos 22 a 25, reservados para propósitos relacionados con el programa de TV que acompaña.

3.13.9 Visualización de «Status».

Corresponderá desde el octeto 26 hasta el final del paquete. Este grupo estará codificado con caracteres de paridad impar a partir de los códigos de la figura 8.

3.14 Ampliación del repertorio de caracteres.

Se utilizarán paquetes con Y = 26 para sobreescribir cualquier casilla. Los paquetes X/1 a X/24 habrán de contener en esas posiciones los datos con paridad par. El orden de transmisión recomendado para los paquetes con Y = 26 se encuentra en el apéndice 1.

3.14.1.

Secuencia de sincronismo de bits, código de sincronismo de octetos y de direccionamiento de paquetes.

Formados por los octetos 1 a 5 inclusive, como en los apartados 3.9 y 3.10.

3.14.2 Código de designación.

Formado por el octeto 6, con 4 bits de datos más 4 bits de protección Hamming. Los códigos 0000 a 1110 inclusive, serán etiquetas de secuencia para un máximo de 15 paquetes con Y = 25.

Sin respuesta al código 1111.

3.14.3 Grupos de datos.

Formados por los octetos 7 a 45 inclusive, como 13 grupos de 3 octetos cada uno.

3.14.3.1 Atribución de bits de grupo de datos.

Será: 6 bits para direccionamiento de casilla.

5 bits para descripción de modo.

6 bits para protección Hamming.

7 bits de datos.

Para visualizar en una casilla direccionada como en el apartado 3.14.4, los bits de descripción de modo, en el rango de valores desde 10000 hasta 11111, respectivamente, definirán los acentos de la columna 4 de la tabla de la figura 6 A en orden numérico ascendente.

El carácter asociado, a partir del juego básico de la figura 3, estará definido por los 7 bits de datos. Si se necesitase un acento nulo se usará el modo 10000.

3.14.5.2 Caracteres del juego suplementario.

Para visualizar una casilla se direccionará como en el apartado 3.14.4. Los bits de descripción de modo tomarán el valor 01111. Los 7 bits de datos definirán un carácter del juego de caracteres suplementario de la figura 6 A, columnas 2, 3, 5, 6 y 7.

3.14.5.3 Caracteres de líneas para dibujo.

Se visualizará una casilla direccionando como en el apartado 3.14.4. Los bits de descripción de modo tomarán el valor 00010. Los 7 bits de datos definirán un carácter del juego de líneas para dibujo de la figura 6 E.

3.14.6 Identificador de final.

Como se podrá necesitar más de un paquete X/26 para una página dada, se preverá un identificador de paquete final.

Esto se realizará poniendo a 1 todos los bits de direccionamiento de renglón y de descripción de modo, de un grupo de datos que ocupe los octetos 40, 41 y 42 en el último paquete X/25. Sin respuesta a los datos del octeto 42.

Los grupos de datos sin usar entre los grupos activos de datos y el grupo identificador de final, estarán rellenos con repetición del grupo identificador final.

3.14.7 Palabra de verificación del paquete X/26.

Los dos octetos que sigan inmediatamente al grupo de datos que lleve el identificador final, contendrán un chequeo de redundancia cíclica (CRC) opcional, de los datos de los paquetes X/26. Este se generará de la misma forma que el CRC del paquete X/27, usando los datos de los paquetes X/26. Cualquier dato que falte se sustituirá por el carácter ESPACIO (2/0).

APÉNDICE 1

Orden de transmisión recomendada para los paquete Y = 26 e Y = 27

Para permitir la operación lo más eficaz posible del decodificador, se recomienda que, a continuación de la transmisión de una cabecera de página con Y = 0, se transmitan los paquetes con Y = 27 e Y = 26, en este orden.

Si se transmite otro paquete de cabecera con Y = 0, a continuación de la transmisión de los paquetes con Y = 27 e Y = 26, estos dos paquetes deben ser transmitidos de nuevo.

APÉNDICE 2

Memoria del decodificador

Aunque esta especificación no introduce explícitamente limitaciones en cuanto al tamaño o velocidad de la memoria del decodificador, ésta deberá permitir que:

1) Puedan requerirse hasta 20 milisegundos para borrar la memoria del decodificador después de la recepción de un paquete de cabecera de página con Y = 0.

2) Pueda ser necesario el transcurso de este período de tiempo, después de la transmisión del paquete de cabecera de una determinada página, antes de que se transmitan más datos relacionados con dicha página.

APÉNDICE 3

Datos protegidos por Hamming

Ciertos octetos de datos están protegidos usando códigos Hamming y pueden usarse de dos formas:

1) Octetos con 4 bits de información y 4 bits de protección.

2) Grupos de 3 octetos con 15 bits de información y 5 bits de protección.

En la primera forma, los bits b1, b3, b5 y b7 son los bits de protección.

Los bits b2, b4, b6 y b8 son los de información.

Las comprobaciones de paridad son:

P1 = b8 + b6 + b2 + b1.

P2 = b8 + b4 + b3 + b2.

P3 = b5 + b5 + b4 + b2

P4 = b8 + b7 + b6 + b5 + b4 + b3 + b2 + b1.

En la segunda forma, los bits b1, b2, b4, b8, b16 y b24 son bits de protección.

Los bits b3, b5, b6, b7, b9, b10, b11, b12, b13, b14, b15, b17, b18, b19, b20, b21, b22 y b23 son de información.

Las comprobaciones de paridad son:

P1 = Suma de todos los bits de orden impar desde b1 a b23, inclusive.

P2 = b2 + b3 + b6 + b7 + b10 + b11 + b14 + b15 + b18 + b19 + b22 + b23.

P3 = b4 + b5 + b6 + b7 + b12 + b13 + b14 + b15 + b20 + b21 b22 + b22 + b23.

P4 = Suma de bits numerados b8 a b15, inclusive.

P5 = Suma de los bits numerados b15 a b23, inclusive.

P5 = Suma de los bits numerados b1 a b24, inclusive.

Las secuencia de bits se muestran en las figuras 1 y 2.

Nota: «+» significa «O» inclusiva.

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_015.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_016.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_017.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_018.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_019.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_020.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_021.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_022.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_023.png)

Según el ejemplo arriba indicado, un registro de desplazamiento de 16 bits tiene como entrada la suma de módulo 2 de una entrada externa y de los contenidos de las posiciones 7, 9, 12 y 16 del registro.

Inicialmente todas las posiciones del registro se ponen a 0.

Durante una secuencia de 8.192 impulsos de reloj, la entrada está formada por los primeros 24 octetos de carácter (192 bits) del paquete de cabecera de página, y por los siguientes octetos de carácter de los paquetes con valores de Y hasta 25, en el orden de transmisión convencional. Cualquier paquete ausente, se considera como si estuviera presente y compuesto por octetos pertenecientes al carácter ESPACIO (2/0).

En cada octeto, el orden de los bits es b8 a b1 inclusive. Este orden, que es el inverso del empleado en la secuencia de transmisión, facilita el funcionamiento del decodificador cuando los datos empleados son los almacenados en la memoria de página. Al final del proceso de generación, el contenido del registro es la palabra de verificación de la página básica y se transmite comenzando con el bits contenido en la primera posición.

El orden de transmisión del grupo de dos octetos que resulta de la verificación cíclica redundante de 16 bits de la página es: primero los bits 9 a 16, seguidos de los bits 1 a 8 inclusive.

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_024.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_025.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_026.png)
