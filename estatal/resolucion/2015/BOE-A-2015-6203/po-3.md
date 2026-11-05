## P.O. 10.6. Agregaciones de puntos de medida

1. Objeto.

El objeto de este documento es definir el procedimiento de cálculo de las agregaciones de puntos de medida y la información a intercambiar de las mismas.

2. Ámbito de aplicación.

Este documento aplica a los puntos frontera de clientes tipo 3, 4 y 5 y a los puntos frontera de generación de los que el distribuidor es encargado de lectura.

3. Responsabilidades.

Los distribuidores son los responsables del cálculo de las agregaciones de los puntos frontera de clientes tipo 3, 4 y 5 y de los puntos frontera de generación de los que son encargados de lectura, de acuerdo a lo indicado en este documento.

4. Calculo de agregaciones.

4.1 Definición de medidas agregadas.

4.1.1 Medidas agregadas de fronteras de clientes.

Una medida agregada de medidas horarias de puntos frontera de clientes es el resultado de calcular el sumatorio de la energía activa consumida para cada periodo de integración horario de los distintos puntos frontera de clientes agrupados por distribuidor, comercializador, nivel de tensión, peaje de acceso, discriminación horaria, tipo de punto de medida, sistema eléctrico aislado (para los sistemas eléctricos de los territorios no peninsulares) o provincia (para el sistema peninsular).

Hasta que no se disponga de medida horaria en todos los puntos frontera de clientes tipo 5, las medidas agregadas de dichas fronteras se obtendrán a partir de:

• Medidas de curvas de carga horaria CCH reales o estimadas de suministros que dispongan de equipos de medida con capacidad para telemedida y telegestión efectivamente integrados en los correspondientes sistemas.

• Medidas horarias de suministros que no dispongan de equipos de medida con capacidad para telemedida y telegestión efectivamente integrados en los correspondientes sistemas y deban ser previamente perfilados a partir de las medidas utilizadas para la facturación del peaje de acceso de terceros a la red (saldos de ATR) de acuerdo con lo establecido en el procedimiento de Operación 10.5.

4.1.2 Medidas agregadas de fronteras de instalaciones de generación de las que el distribuidor es encargado de lectura.

Una medida agregada de fronteras de instalaciones de generación de las que el distribuidor es encargado de lectura es el resultado de calcular el sumatorio de energía activa generada horariamente de los distintos puntos frontera de dichas instalaciones agrupados por distribuidor, unidad de programación o entidad de liquidación del representante o titular sin representante, tipo de punto de medida, sistema eléctrico aislado para los sistemas eléctricos no peninsulares o provincia para el sistema peninsular.

4.2 Requisitos de los concentradores secundarios que calculan e intercambian datos de agregaciones.

Los concentradores secundarios dentro del alcance de este documento deberán cumplir los requisitos indicados en los procedimientos de operación. 10.4 y 10.11.

4.3 Procedimiento de cálculo de medidas agregadas.

Los encargados de la lectura deberán calcular las distintas agregaciones de las que son participes de acuerdo a lo indicado en este procedimiento.

4.3.1 Identificación y alta de las agregaciones.

Cada encargado de la lectura deberá identificar y notificar al comercializador/consumidor directo a mercado/representante/generador sin representante y al operador del sistema las agregaciones que tiene responsabilidad de calcular utilizando el protocolo, plazos y formatos descritos en los procedimientos de operación 10.4, 10.5 y 10.11.

4.3.2 Baja de agregaciones.

Cada encargado de la lectura deberá identificar y notificar al comercializador/consumidor/representante/generador sin representante y al operador del sistema las agregaciones de las que deja de tener responsabilidad de cálculo por dejar de ser partícipe de las mismas utilizando el protocolo, plazos y formatos descritos en los procedimientos de operación 10.4, 10.5 y 10.11.

4.3.3 Cálculo de medidas agregadas.

Cada encargado de la lectura deberá calcular las distintas agregaciones de las que es responsable atendiendo a la definición descrita en el apartado 4.1 de este documento.

a. Las medidas individuales (desagregadas) de cada punto frontera de cliente tipo 3 y 4 o de instalaciones de generación de las que el distribuidor es encargado de lectura deberán haber sido calculadas y perfiladas, en su caso, previamente de acuerdo a lo establecido en el P.O. 10.5. «Cálculo del Mejor Valor de Energía en los Puntos Frontera y Cierres de Energía del Sistema de Información de Medidas Eléctricas».

Cada medida agregada de clientes tipo 3 y 4 y de instalaciones de generación de las que el distribuidor es encargado de lectura que no dispongan de equipo de medida horario en un periodo de integración y magnitud tiene asociada adicionalmente la siguiente información:

• Número total de puntos frontera que participan en el cálculo de dicha agregación en el periodo de integración indicado.

• Energía calculada (agregada) utilizando únicamente medidas procedentes de registrador con las características indicadas en el Reglamento unificado de puntos de medida (esto es, excluyendo las estimadas).

• Número de puntos frontera que han servido como base para el cálculo anterior (las procedentes de registrador que cumplan el Reglamento unificado de puntos de medida).

En el Anexo 1 de este documento se detalla el procedimiento de tratamiento de decimales de las medidas agregadas.

b. Las medidas individuales (desagregadas) de cada punto frontera de cliente tipo 5 deberán haber sido calculadas previamente de acuerdo a lo establecido en el procedimiento de operación 10.5.

Cada medida agregada de clientes tipo 5 en un periodo de integración horario deberá tener asociada la siguiente información:

• Sumatorio de la medida horaria de energía de todos los suministros que forman parte de la agregación para el periodo horario (en kWh).

• Número total de suministros que forman parte de la agregación para el periodo horario.

• Sumatorio de las medidas horarias de energía procedentes de curva real de suministros que dispongan de equipos de medida con capacidad de telemedida y telegestión efectivamente integrados en los correspondientes sistemas que forman parte de la agregación para el periodo horario (en kWh).

• Número de suministros con medida procedente de curva real.

• Sumatorio de las medidas horarias de energía procedentes de medida estimada de suministros que dispongan de equipos de medida con capacidad de telemedida y telegestión efectivamente integrados en los correspondientes sistemas que forman parte de la agregación para el periodo horario (en kWh).

• Número de suministros con medida estimada.

El detalle de la obtención de cada uno de los datos agregados de clientes tipo 5, se describe en el Anexo 2 de este documento.

4.4 Intercambio de información.

4.4.1 Publicaciones de los concentradores secundarios al concentrador principal.

El intercambio de información de medidas agregadas atenderá a lo indicado en el P.O. 10.4 «Concentradores de medidas eléctricas y sistemas de comunicaciones» para agregaciones de puntos frontera generación de los que el distribuidor es encargado de lectura y el P.O. 10.11 «Tratamiento e intercambio de Información entre Operador del Sistema, encargados de la lectura, comercializadores y resto de agentes» para agregaciones de puntos frontera clientes junto con las consideraciones de este procedimiento.

Las medidas agregadas que deberá calcular y enviar cada concentrador secundario quedan identificadas por la siguiente información:

• Concentrador que envía la medida.

• Magnitud (será activa consumida para agregaciones de clientes y activa generada para agregaciones de generación de las que el distribuidor es encargado de lectura).

• Periodo de integración.

• Medida (kWh, valores incrementales).

• Número total de puntos frontera y sumatorio de las medidas horarias de energía de la agregación según se describe en el apartado 4.3.3 de este procedimiento.

• Agregación calculada: identificada por los distintos parámetros que la definen descritas en los apartados 4.1.1 y 4.1.2 de este procedimiento. Esto es, cada concentrador secundario, enviará para cada periodo y magnitud las distintas agregaciones vigentes de las que disponga de medidas.

4.4.2 Publicaciones del concentrador principal a los concentradores secundarios.

La publicación por parte del operador del sistema de las medidas agregadas se realizará utilizando el protocolo de comunicaciones entre concentradores y formatos descritos en el P.O. 10.4.
