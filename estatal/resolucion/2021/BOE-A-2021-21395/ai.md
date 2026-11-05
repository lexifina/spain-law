## ANEXO I

## Método de cálculo de los perfiles de consumo para los puntos de medida tipo 4 y tipo 5 de consumidores que no dispongan de registro horario de consumo

1. Objeto

El objeto de este procedimiento es establecer los perfiles de carga que serán utilizados para obtener las medidas horarias necesarias para la liquidación de la energía en el mercado de producción de energía eléctrica, a partir de los datos de consumo registrados por equipos de medida no horarios.

2. Ámbito de aplicación

Este procedimiento aplica a los puntos de medida tipo 4 y 5 de consumidores que no dispongan de registro de consumo horario en sus equipos de medida.

3. Definiciones

Perfil Inicial: perfil de carga publicado a efectos indicativos y que sirve de base para el cálculo de los perfiles de carga que se emplearán para obtener las medidas horarias de los consumidores.

Perfil Final: perfil de carga que se utilizará para obtener las medidas horarias de los consumidores a efectos de la liquidación de su energía en el mercado, a partir de registros de medida no horarios.

Demanda de Referencia: previsión de demanda del sistema peninsular que se utilizará para el cálculo de los Perfiles Finales a partir de los Perfiles Iniciales. La Demanda de Referencia tomará para 2022 los valores recogidos en el anexo III.

Demanda del Sistema: demanda del sistema eléctrico peninsular publicada por el operador del sistema a efectos de la determinación de los Perfiles Finales.

4. Clasificación de consumidores

Se establecen las siguientes categorías de consumidores que tendrán perfiles de carga diferenciados:

1.º Perfil tipo P2.0TD: de aplicación a la categoría de consumidores con peaje de transporte y distribución 2.0TD.

2.º Perfil tipo P3.0TD: de aplicación a la categoría de consumidores con peaje de transporte y distribución 3.0TD. Este perfil será de aplicación también a puntos de medida tipo 4 de consumidores conectados en alta tensión (a los que aplica el peaje 6.1TD).

3.º Perfil tipo P3.0TDVE: de aplicación a la categoría de consumidores con peaje de transporte y distribución 3.0TDVE. Este perfil será de aplicación también a puntos de recarga tipo 4 conectados en alta tensión (a los que aplica el peaje 6.1TDVE).

5. Peajes y periodos horarios

Para el conjunto de perfiles del anexo III, aplican los peajes de transporte y distribución del artículo 6 de la Circular 3/2020, de 15 de enero, de la Comisión Nacional de los Mercados y la Competencia, por la que se establece la metodología para el cálculo de los peajes de transporte y distribución de electricidad, y los periodos horarios del artículo 7 de la referida circular.

6. Perfiles Iniciales

Los Perfiles Iniciales para cada categoría de consumidores tomarán los valores recogidos en el anexo III de la presente resolución.

7. Cálculo de los Perfiles Finales

Los Perfiles Finales se obtendrán a partir de los Perfiles Iniciales modificando estos últimos en función de la evolución de la Demanda del Sistema en relación con la Demanda de Referencia, tratando de incorporar en los perfiles aquellos factores que afectan a las pautas de consumo y no son previsibles con antelación, como la temperatura, luminosidad, etc.

Sean:

Pi,0m,d,h = Perfil Inicial, de la categoría de consumidores «i», para el mes «m», día «d» y hora «h», que representa el peso relativo de la hora en el año.

Suma de los coeficientes del Perfil Inicial de la categoría de consumidores «i» en las 24 horas de un día.

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808747_1.png)

Hi,0m,d,h = Pi,0m,d,h / Ci,0m,d; Peso de la hora «h» del día «d» del mes «m», en el total del día «d» del mes «m».

; Peso del mes «m», en el año en el Perfil Inicial.

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808751_1.png)

Dm,d,h= Demanda del Sistema en la hora «h» del día »d» del mes «m».

DRm,d,h= Demanda de Referencia en la hora «h» del día »d» del mes «m».

αi, βi, γi = Coeficientes específicos para cada categoría de consumidores «i».

Pi,fm,d,h, Ci,fm,d, Hi,fm,d,h y Mi,fm, tienen el mismo significado que los anteriores pero referidos a los Perfiles Finales, en lugar de a los Perfiles Iniciales.

αi, βi, y γi tomarán en 2022 los valores recogidos en el anexo II de la presente Resolución.

El operador del sistema obtendrá los Perfiles Finales a partir de los Perfiles Iniciales realizando las siguientes operaciones:

Ajuste de energía en las horas respecto del día:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808789_1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808775_1.png)

Ajuste de energía en los días respecto del mes:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808776_1.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808777_1.png)

Ajuste de energía en el mes respecto del año:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808778_1.png)

Obteniendo los Perfiles Finales como:

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808795_1.png)

El operador del sistema pondrá a disposición de los sujetos de mercado, del Ministerio para la Transición Ecológica y el Reto Demográfico y de la Comisión Nacional de los Mercados y la Competencia, los Perfiles Finales y la Demanda del Sistema utilizada para su cálculo antes de transcurridos 5 días desde el final del mes de consumo a que se refieren.

8. Utilización de los Perfiles Finales

Los distribuidores, como encargados de lectura, serán los responsables de obtener las medidas horarias de los consumidores a partir de los datos registrados en sus equipos de medida.

El cálculo de la media horaria a efectos de liquidación de la energía en el mercado se realizará aplicando el Perfil Final, correspondiente a la categoría del consumidor, a la energía registrada por el equipo de medida en el período correspondiente. En aquellos casos en los que el equipo de medida registre la energía en más de un bloque horario, el Perfil Final se aplicará independientemente para las horas de cada bloque. En los casos en que no se registre la hora exacta de realización de la medida, se considerará que ésta se ha realizado a las 0 h del día en que se realizó la medida.

Sean:

MCcj,t,J,T,p = Medida incremental obtenida del contador del cliente «c», entre el día «t» del mes «j» y el día «T» del mes «J» correspondiente al bloque horario «p».

MCHc,im,d,h,p = Medida horaria calculada del cliente «c» con perfil «i», en la hora «h» del día «d» mes del «m» correspondiente al bloque horario «p» registrado por el equipo de medida.

Dm = número de días del mes «m»

![imagen](https://www.boe.es/datos/imagenes/disp/2021/310/21395_10808780_1.png)
