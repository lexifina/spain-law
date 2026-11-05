## ANEXO

## Especificación del formato del código ITV

Cada nuevo modelo, variante o versión de un vehículo que sea distinguible por alguna característica técnica relevante, supondrá el alta de un nuevo código ITV. El fabricante o asociación de fabricantes deberá comunicar a la Dirección General de Tráfico las características técnicas asociadas a cada nuevo código ITV. La comunicación se realizará mediante el envío, a la dirección de correo electrónico que la Dirección General de Tráfico especifique, del fichero con las altas de códigos siguiendo el formato indicado en este anexo.

Composición del código ITV

La asignación de códigos se realiza por cupos, de manera que cada marca recibe un rango de códigos y se encarga de administrarlos. La composición del código consta de nueve posiciones alfanuméricas: tres posiciones para identificar a la marca (p.e. OPEL es OPE) según las siglas utilizadas por la Organización Internacional de Constructores de Automóviles (OICA), cinco posiciones para identificar la clase de vehículo que asigna el fabricante y por último un carácter de control.

El procedimiento de obtención del carácter de control es el siguiente:

1.º Asignación a cada carácter alfanumérico del valor que le corresponda según la tabla siguiente:

TABLA 1

| Car | Valor | Car | Valor | Car | Valor | Car | Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | A | l0 | K | 20 | U | 30 |
| 1 | 1 | B | 11 | L | 21 | V | 31 |
| 2 | 2 | C | 12 | M | 22 | W | 32 |
| 3 | 3 | D | 13 | N | 23 | X | 33 |
| 4 | 4 | E | 14 | O | 24 | Y | 34 |
| 5 | 5 | F | 15 | P | 25 | Z | 35 |
| 6 | 6 | G | 16 | Q | 26 |  |  |
| 7 | 7 | H | 17 | R | 27 |  |  |
| 8 | 8 | I | 18 | S | 28 |  |  |
| 9 | 9 | J | 19 | T | 29 |  |  |

Ejemplo: CÓDIGO OPE10001

| O | P | E | 1 | 0 | 0 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | 25 | 14 | 1 | 0 | 0 | 0 | 1 |

2.º Asignación a cada posición del factor de ponderación de la tabla

| 1.er dígito |  |  | 8 |
| --- | --- | --- | --- |
| 2.º |  |  | 7 |
| 3.º |  |  | 6 |
| 4.º |  |  | 5 |
| 5.º |  |  | 4 |
| 6.º |  |  | 3 |
| 7.º |  |  | 2 |
| 8.º |  |  | 1 |

Ejemplo: CÓDIGO OPE10001

| O | P | E | 1 | 0 | 0 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

3.º Suma de los productos de los valores numéricos por los factores de ponderación.

Ejemplo: CÓDIGO OPE10001

|  | O | P | E | 1 | 0 | 0 | 0 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Número asignado | 24 | 25 | 14 | 1 | 0 | 0 | 0 | 1 |
| × Ponderación | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| = N.º RESULTANTE | 192+ | 175+ | 84+ | 5+ | 0+ | 0+ | 0+ | 1 = 457 |

4.º División de la suma entre 36 y obtención del resto

457 : 36 = 10 RESTO = 25

5.º Asignación al resto de su valor alfanumérico según la tabla 1

En el ejemplo = P

CÓDIGO OPE10001 + CARÁCTER CONTROL P

CÓDIGO COMPLETO = OPE10001P

Datos asociados a cada código ITV

Por cada código ITV utilizado, el fabricante deberá remitir la información que se indica a continuación en un fichero de texto con campos de longitud fija codificado en ASCII (ISO latin 1). Los datos deben informarse en el orden y con el formato indicado en la siguiente tabla:

Los campos de tipo alfanumérico (CAR) se rellenarán con blancos por la derecha. Los campos de tipo (NUM) se rellenarán con «ceros» por la izquierda.

| Nombre | Longitud | Tipo de campo | Ejemplo | Observaciones | RD 750/2010 |
| --- | --- | --- | --- | --- | --- |
| CÓDIGO ITV | 9 | CAR | CIT016032 | Se añade un noveno dígito. Se reinicia la numeración «CIT00001B» | C.I. |
| BASTIDOR | 11 | CAR | VF7N0WJYB00 | Si no se rellenan los 11 caracteres dejar espacios en blanco a la derecha | E |
| FABRICANTE | 70 | CAR | AUTOMOVILES |  | A.1 |
| TIPO | 25 | CAR | 7***** |  | D.2 |
| VARIANTE | 25 | CAR | 7J9HXC |  | D.2 |
| VERSIÓN | 35 | CAR | H |  | D.2 |
| MARCA | 30 | CAR | CITROEN |  | D.1 |
| DENOMINACIÓN COMERCIAL | 30 | CAR | XSARA PICASSO 2.0 |  | D.3 |
| CAT. HOMOLOG | 4 | CAR | M1 |  | J |
| C02 | 6 | NUM | 101000 | En g/km. 3 enteros y 3 decimales EEEDDD. Vehículos M1 número entero. Cero en los decimales | V.7 |
| CONSUMO wh/km | 4 | NUM | 0025 | En wh /km. Número entero | P.3 |
| MASA (MOM) | 6 | NUM | 000980 | En Kg. Número entero | G |
| MMA | 6 | NUM | 001900 | En Kg. Número entero | F.2 |
| PLAZAS | 3 | NUM | 005 |  | S.1 |
| PROCEDENCIA | 3 | CAR | EEE | EEE= UE, IM = IMPORTADO, «en blanco»= NACIONAL | D.6 |
| DISTANCIA ENTRE EJES | 4 | NUM | 2345 | En mm. Número entero | M.1 |
| VÍA ANTERIOR | 4 | NUM | 1565 | En mm. Número entero | F.7 |
| VÍA POSTERIOR | 4 | NUM | 1575 | En mm. Número entero | F.7.1 |
| CILINDRADA | 5 | NUM | 01275 | En cm3. Número entero | P.1 |
| TIPO ALIMENTACIÓN | 1 | CAR | M | M= monocombustible. B= bicombustible F= flexicombustible. Según tabla de combustibles adjunta | P.3 |
| COMBUSTIBLE | 3 | CAR | G | Según la tabla de combustibles adjunta | P.3 |
| POTENCIA REAL | 5 | NUM | 06620 | En Kw Redondeado a la segunda cifra decimal. 3 enteros y 2 decimales EEEDD | P.2 |
| POTENCIA FISCAL | 5 | NUM | 01147 | En CVF. Redondeado a la segunda cifra decimal. 3 enteros y 2 decimales EEEDD | P.2.1 |
| CLASIFICACIÓN | 4 | NUM | 1000 | Según el Anexo II B) y C) del Real Decreto 2822/1998, de 22 de diciembre | CL |
| CONTRASEÑA HOMOLOGACIÓN | 40 | CAR | e2*98/14*0153*24 |  | K |
| NIVEL EMISIONES | 8 | CAR | Euro5 | Se consignará el nivel de emisiones del vehículo que aparece en la homologación de tipo |  |
| ECO INNOVACIÓN | 1 | CAR | S | S= SI, N= NO. A la espera de definir por UE, hasta entonces se deja en blanco | No existe |
| REDUCION ECO | 4 | NUM |  | A la espera de definir por UE, hasta entonces se deja en blanco | No existe |
| CÓDIGO ECO | 10 | CAR |  | A la espera de definir por UE, hasta entonces se deja en blanco | No existe |

La información referente al combustible, y al tipo de alimentación, se indicarán de la siguiente forma en el código ITV:

| Combustible | Combustible informado por el fabricante | Tipo alimentación | CO2 que debe informarse |
| --- | --- | --- | --- |
| Gasolina | G | M | Gasolina |
| Diesel | D | M | Diesel |
| GLP | GLP | M | GLP |
| Gas Natural | GNL o GNC según corresponda | M | GNL o GNC, según corresponda |
| Biometano | BM | M | Biometano |
| Hidrógeno | H | M | Hidrógeno |
| Eléctrico | E | M | Se indicará “0” |
| Gasolina-E85 | ET | F | Gasolina |
| Diesel-Biodiesel | BD | F | Diesel |
| GASOLINA-GLP | GLP | B | GLP |
| gasolina-GN | GNL o GNC según corresponda | B | GN |
| Gasolina-biometano | BM | B | Biometano |
| Gasolina- hidrógeno | H | B | Gasolina |
| Híbridos “enchufables” | E | B | Gasolina / Diesel o la combinación de combustible más beneficiosa en términos de CO2 |

En el caso de vehículos que pueden utilizar más de dos tipos de combustible (múltiples combustibles), se seleccionarán los dos combustibles que tengan un nivel inferior de emisiones de CO2. Se considerará que es B (bicombustible), aplicando lo dispuesto en la tabla para este tipo de alimentación. Por ejemplo, si es Gasolina/GLP/E85, se seleccionará Gasolina-GLP y se matriculará como GLP.
