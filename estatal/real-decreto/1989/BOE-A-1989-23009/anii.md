## ANEXO II

## NORMA TÉCNICA PARA LA DIFUSIÓN DE SONIDO DUAL/ESTEREOFÓNICO POR EL SERVICIO DE DIFUSIÓN DE TELEVISIÓN

1. Objeto.

La presente norma técnica tiene por objeto determinar las características del sistema adoptado por el Estado español para la transmisión de dos canales de sonido digital dual/estereofónico en los sistemas de difusión de televisión definidos en el Anexo I del presente Reglamento Técnico.

2. Especificación del multiplex datos/sonido y método de codificación del sonido.

2.1 Formato en banda base.

2.1.1 Estructura de trama.

El flujo de datos se transmitirá en serie y estará dividido en tramas de 728 bits, que serán transmitidas de forma continua sin separación entre ellas. Cada milisegundo se transmitirá una trama, con lo que el número total de bits será de 728 Kb/s según la siguiente estructura:

6 bits/Palabra de alineación de trama: 8 Kb/s (sección 2.2.1).

5 bits/Información de control: 5 Kb/s (sección 2.2.2).

11 bits/Datos adicionales: 11 Kb/s (sección 2.2.3).

704 bits/Sonido, paridad o datos: 704 Kb/s (sección 2.2.4/5).

Total: 726 Kb/s.

Los diagramas de la estructura de trama para enviar señales de sonido estereofónico y monofónico, se muestran en la Fig. 1. Los 720 bits siguientes a la palabra de alineación de trama, forman una estructura de bloques de señal de sonido comprimido del tipo de sistemas MAC-PAQUETES con protección de primer nivel. Los primeros 15 bits del bloque, se usarán para indicar la información de control (sección 2.2.2) y como bits de datos adicionales (sección 2.2.3).

2.1.2 Transposición de bits.

Los 704 bits del bloque que sigue a la palabra de alineación de trama, los bits de control y los bits adicionales, se transpondrán para minimizar el efecto de errores multiplex. Los bits de cada trama se transmitirán en el siguiente orden:

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_007.png)

La transposición anterior coloca los bits de datos que son adyacentes en la estructura de trama de la Fig. 1 en posiciones separadas como mínimo 16 ciclos de reloj en la cadena de bits transmitidos (como mínimo hay 15 bits intercalados entre dos bits adyacentes en la Fig. 1).

2.1.3 Aleatorización para la dispersión de energía.

Los datos transmitidos se aleatorizarán para conformar el espectro. La aleatorización se realizará de manera síncrona con la trama del multiplex.

La palabra de alineación de trama no se aleatorizará y se utilizará para sincronizar el generador de secuencia seudo-aleatoria usado en el receptor para la desaleatorización. Los demás parámetros serán:

(I) El primer bit después de la palabra de alineación de trama será el primer bit aleatorizado, y se sumará binariamente (sin acarreo) al primer bit de la secuencia seudo-aleatoria.

(II) El bit inmediato anterior a la palabra de alineación de trama será el último bit aleatorizado.

(III) La aleatorización se realizará después de la transposición (y la desaleatorización antes de la reposición en el receptor).

(IV) La secuencia seudo-aleatoria se define mediante el generador polinomial y la palabra de inicialización:

Generador Polinomial: x E9 + x E4 + 1.

Palabra de inicialización: 1 1 1 1 1 1 1 1 1.

2.2 Codificación de la información.

2.2.1 Palabra de alineación de trama.

La palabra de alineación de trama será 01001110 y se transmitirá de izquierda a derecha.

2.2.2 Información de control.

La información de control se enviará mediante un bit de señalización de trama, C0, tres bits de control de aplicación, C1, C2, C3 y un bit de reserva de conmutación de audio Ca (ver Fig. 1).

2.2.2.1 Bit de señalización de trama.

El bit de señalización de trama, C0, será «1» para 5 tramas sucesivas y «0» para las 8 siguientes; de forma que defina una secuencia de 15 tramas. Las tramas se numeran así: la primera trama (trama 1) de la secuencia como la primera de las 5 tramas en que C0 = 1; de forma que la última trama (trama 16) de la secuencia, sea la última de las 8 tramas en que C0 =0. Esta secuencia de trama se utilizará para sincronizar los cambios en el tipo de información transmitida por el canal.

2.2.2.2 Bit de control de aplicación.

Los últimos 704 bits de cada trama se utilizarán para enviar muestras de sonido o datos. La aplicación del uso de esos bits se definirá mediante los tres bits de control de aplicación: C1, C2 y C3, como se indica en la Tabla 1.

Para cambiar a una nueva aplicación, los bits de control cambian en la trama 1 de la última secuencia de 16 tramas de la presente aplicación. Los 704 bits de sonido/datos cambiarán el nuevo modo de trabajo en la trama 1 de la siguiente secuencia de 16 tramas.

## TABLA 1

## Aplicaciones de los bloques de 704 bits de sonido/datos

| Bits de control de aplicación | Contenido del bloque sonido/datos de 704 bits |
| --- | --- |
| C1 | C2 | C3* |
| 0 | 0 | 0 | Señal estéreo, compuesta de muestras alternadas de canales A y B. |
| 0 | 1 | 0 | Dos señales monofónicas independientes transmitidas en tramas alternas (designadas como M1 y M2). |
| 1 | 0 | 0 | Una señal monofónica y un canal transparente de datos de 352 Kb/s transmitidos en tramas alternas. |
| 1 | 1 | 0 | Un canal transparente de datos de 704 Kb/s. |

(*) C3 = 1 puede indicar otras opciones de codificación de datos o sonido. Cuando sea C3 = 1 los decodificadores no equipados para estas opciones adicionales, no deberán proporcionar salida de sonido.

2.2.2.3 Indicativo de conmutación a sonido de reserva.

Los decodificadores de sonido digital deberán estar preparados para conmutar la salida al demodulador de sonido convencional, para sustituir al sonido digital cuando este falle. La conmutación al demodulador de FM es únicamente aceptable si la portador de FM está siendo modulada con el mismo programa de sonido que la señal digital. El criterio para inhibir esta conmutación estará incorporado en la información de control.

El quinto bit de control, C4, se pondrá a «1» cuando la señal de FM lleve la misma información que la señal estereofónica digital, o la señal monofónico-digital (sólo la señal mono M1 en el caso de que se transmitan dos señales monofónicas digitales). Cuando la señal de FM no lleve la misma información de programa que la señal digital el bit de conmutación se pondrá a «0». en este caso se usará para impedir la conmutación al sonido de FM.

2.2.3 Datos adicionales.

Para futuras aplicaciones se reservan 11 bits de datos ADC a AD1C (Fig. 1).

2.2.4 Bloque de sonido/datos.

Los últimos 704 bits de cualquier trama forman un bloque de información de datos o sonido. Los dos tipos de información no se mezclan dentro de una trama. Se transmiten 64 muestras de sonido (D1 a D64). La Fig. 1 (a) muestra una trama de sonido estereofónico, y la Fig. 1 (b) una trama monofónica.

Cuando se transmita una señal estereofónica (C1=C2=C3=0), las muestras impares (D1, D3, D5, ..., D64) para enviar el canal B (sección 2.2.5.1). De este modo se transmiten 323 muestras de cada canal en cada trama.

Cuando se transmiten dos señales monofónicas independientes (C1=0, C2=1, C3=0), M1 se transmitirá en las tramas impares, y M2 en las pares (sección 2.2.2.1).

De este modo, para señales monofónicas, cada trama de información de sonido contendrá 64 muestras consecutivas, que se separarán en dos bloques completos comprimidos, representados como bloques n y n+1 en la Fig. 1 (b).

2.2.5 Señales de sonido.

2.2.5.1 Compresión-expansión casi instantánea.

Las señales de sonido se muestrean a 32 Khz y se codifican inicialmente con una resolución de 14 bits por muestra. Para la transmisión, el número de bits por muestra se reduce a 10 utilizando una compresión casi instantánea, añadiéndose un bit de paridad a cada muestra de 10 bits para detección de errores e indicación del factor de escala.

En el proceso de compresión casi-instantánea se conforman las muestras digitales de 14 bits en bloques de 32. Todas las muestras en cada bloque de 1 ms. se codifican utilizando un código de 10 bits en complemento a 2, con una precisión determinada por la magnitud de la muestra más alta en el bloque, y formándose un factor de escala para enviar al receptor el grado de compresión. En la Fig. 3 se ilustra la codificación para la compresión expansión de las señales de sonido.

Mediante la utilización de redes analógicas o de filtros digitales, se somete a las señales de sonido, antes de la compresión, a un proceso de pre-énfasis. (Rec. J.17 del C.C.I.T.T.).

Para la transmisión estereofónica las señales derecha e izquierda se muestrean simultaneamente; las muestras A llevan la señal de sonido que reproducirá el altavoz izquierdo y las muestras B la del derecho.

## TABLA 2

## Características de codificación de sonido

| Frecuencia de muestreo: | 32 KHz. |
| --- | --- |
| Resolución inicial: | 14 bits/muestra. |
| Características de compresión-expansión: | Casi-instantánea con compresión a 10 bits por muestra en bloques de 32 muestras (1 ms). |
| Codificación de las muestras comprimidas: | Complemento a 2 (Fig. 2). |
| Pre-énfasis: | Recomendación J. 17 del CCITT (6,5 dB de atenuación a 800 Hz). |
| Nivel de saturación de audio: | +12 dBm0 medidos a la frecuencia de ganancia unidad de la red de pre-énfasis (2 kHz). |

2.2.5.2 Protección de errores en las señales de sonido.

Para detectar errores en los seis bits más significativos, se añade un bit de paridad a cada muestra de 10 bits. El grupo de paridad así formado es par (la suma binaria sin acarreo del bit de paridad y los seis bits protegidos es siempre igual a cero). Posteriormente, los bits de paridad se modifican para indicar la palabra de tres bits de factor de escala asociada a cada bloque de señal de sonido (ver sección 2.2.5.3).

La tabla 3 muestra los rangos de codificación y los rangos de protección asociados a cada palabra de tres bits de factor de escala. Los cinco rangos de codificación indican el grado de comprensión al que han sido sometidas las muestras en el proceso de compresión-expansión casi instantánea.

Además de indicar el rango de codificación, el factor de escala indica siete rangos de protección. Esta información se usará en el receptor para proporcionar una protección adicional a los bits más significativos de cada muestra.

TABLA 3

| Rango codificación | Rango protección | Factor Escala |
| --- | --- | --- |
| R2 | R1 | R0 |
| Primer rango | Primer rango | 1 | 1 | 1 |
| Segundo rango | Segundo rango | 1 | 1 | 0 |
| Tercer rango | Tercer rango | 1 | 0 | 1 |
| Cuarto rango | Cuarto rango | 0 | 1 | 1 |
| Quinto rango | Quinto rango | 1 | 0 | 0 |
| Quinto rango | Sexto rango | 0 | 1 | 0 |
| Quinto rango | Séptimo rango | 0 | 0 | 1 |
| Quinto rango | Séptimo rango* | 0 | 0 | 0 |

(*) El código del último factor de escala indica «Séptimo rango de protección» (no octavo) para mantener la máxima similitud con el sistema MAC-PAQUETES especificado en el Anexo B de este mismo Reglamento.

2.2.5.3 Indicación del factor escala de las señales de sonido en la paridad.

Los tres bits de factor de escala R2, R1, R0 (ver Tabla 3) asociados a cada señal de sonido se envían mediante la modificación de los bits de paridad, en las muestras usadas para enviar esa señal de sonido.

Cuando se transmita una señal estereofónica, FE1 es la palabra de factor de escala R2A, R1A, R0A, asociada con las muestras A, y FE2 es la palabra de factor de escala R2B, R1B, R0B, asociada con las muestras B. «Pi» es el bit de paridad de la muestra «i» y se cambiará por «P’i» mediante la suma binaria sin acarreo con uno de los bits de las palabras de factor de escala según la siguiente norma:

P’i = Pi xor R2A. Para i = 1,7,13,19,25,31,37,43,49.

P’i = Pi xor R1A. Para i = 3,9,15,21,27,33,39,45,51.

P’i = Pi xor R0A. Para i = 5,11,17,23,29,35,41,47,53.

P’i = Pi xor R2B. Para i = 2,8,14,20,25,32,38,44,50.

P’i = Pi xor R1B. Para i = 4,10,16,22,28,34,40,46,52.

P’i = Pi xor R0B. Para i = 6,12,18,24,30,35,42,48,54.

Cuando se transmita una señal monofónica, FE1 es la palabra de factor R2n, R1n, R0n asociada al primer bloque de 32 muestras de la trama, y Fe2 es la palabra de factor de escala R2n + 1, R1n +1, y R0n + 1 asociada al segundo bloque de 32 muestras de la trama. Al igual que en el caso de transmisión estereofónica, el bit de paridad de la muestra «i» (Pi) se cambia a (P’i) mediante la suma binaria, sin acarreo, con uno de los bits de las palabras de factor de escala. La modificación de los bits de paridad en el caso monofónico se relacionará con la estructura del bloque de señal monofónica como se indica:

P’i = Pi xor R2n. Para i = 1,4,7,10,13,16,19,22,25.

P’i = Pi xor R1n. Para i = 2,5,8,11,14,17,20,23,26.

P’i = Pi xor R0n. Para i = 3,6,9,12,15,18,21,24,27.

P’i = Pi xor R2n+1. Para i = 28,31,34,37,40,43,46,49,52.

P’i = Pi xor R1n+1. Para i = 29,32,35,38,41,44,47,50,53.

P’i = Pi xor R0n+1. Para i = 30,33,35,39,42,45,48,51,54.

Parte de la información del factor de escala del segundo bloque de muestras es enviada en el código de paridad de las muestras 28 a 32, que pertenecen al primer bloque.

La información del rango de factor de escala y del rango de protección se extraen del decodificador con prioridad lógica. Posteriormente se restaura la paridad original para la cancelación de errores.

La relación de paridad correspondiente podrá ser par o impar.

3. Especificación de los parámetros de modulación.

3.1 Señales analógicas.

3.1.1 Portadora de imagen: De acuerdo con el anexo I de este Reglamento.

3.1.2 Portadora de sonido analógico: De acuerdo con el Anexo I de este Reglamento, en la relación de potencias indicadas posteriormente.

3.1.3 Relación de potencias entre el pico de portadora de imagen y la portadora de sonido analógico: Aprox. 20 a 1.

3.2 Señal digital.

3.2.1 Tipo de modulación: En cuadratura por desplazamiento de fase (DPSK) codificada diferencialmente (Ver 3.3).

3.2.2 Velocidad de transmisión: 728 Kb/s ± 1x10-6.

3.2.3 Frecuencia portadora: 5,85 MHz por encima de la portadora de imagen. (Sin relación con la velocidad de transmisión). Ver Fig. 3.

3.2.4 Nivel de señal: Relación aproximada de potencias entre el pico de portadora de imagen y la portadora digital modulada: 100 a 1.

3.2.5 Conformación del espectro: Los pulsos a la frecuencia de 354 KHz se filtran, antes de ser modulados en cuadratura, por un filtro paso bajo cuya respuesta se indica a continuación (ver Fig. 4a). El retardo de grupo del filtro es constante.

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_008.png)

Cuando en recepción se usa el mismo filtro se obtiene una respuesta global en coseno al 40%. (Ver Fig. 4b).

3.3 Especificaciones de la portadora modulada digitalmente.

3.3.1 Tipo de modulación.

La modulación será en cuadratura por desplazamiento de fase (DPSK) codificada diferencialmente, es decir, modulación de fase en cuatro estados, en la cual cada cambio de estado indica dos bits de datos a partir de fase 0º.

3.3.2 Codificación diferencial.

El flujo de datos a la entrada del modulador se codifica de forma diferencial de la siguiente manera:

I) Conversión serie a dos bits en paralelo.

El flujo de datos de entrada se agrupa en pares de bits mediante un conversor serie-paralelo.

II) Codificación de los cambios de fase transmitidos.

Las magnitudes de los cambios de fase de portadora que corresponden a los cuatro posibles valores de los pares de bits de entrada (An, Bn) son:

| Par de bits de entrada | Valor del cambio de fase de la portadora (En grados) |
| --- | --- |
| An | Bn |  |
| 0 | 0 | 0º (no cambia) |
| 0 | 1 | –90º |
| 1 | 0 | –270º |
| 1 | 1 | –180º |

en donde, como se indica en la Fig. 5, An es el bit a la entrada en un momento cualquiera, y Bn es el bit presente un ciclo de reloj después.

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_009.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_010.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_011.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_012.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_013.png)

![imagen](https://www.boe.es/datos/imagenes/disp/1989/233/23009_014.png)
