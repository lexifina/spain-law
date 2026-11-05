## P.O. 10.12. Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión

1. Ámbito de aplicación.

Este procedimiento regula la captación, validación, tratamiento y estimación de los datos de medida procedentes de los equipos de medida instalados en puntos frontera de clientes tipo 5, efectivamente integrados en el sistema de telegestión y utilizados, en su caso, en su facturación.

2. Definiciones.

En coherencia con lo establecido en el Reglamento unificado de puntos de medida del sistema eléctrico, a continuación se incluyen las definiciones de aplicación al presente procedimiento:

• Punto de medida de clientes tipo 5: puntos situados en las fronteras de consumidores cuya potencia contratada en cualquier periodo sea igual o inferior a 15 kW.

• Encargado de la lectura (Encargado de la lectura): entidad responsable de realizar la lectura (ya sea en modo remoto, local o visual), poner la información a disposición del operador del sistema y del resto de participantes en la medida, así como otras funciones asociadas. La empresa distribuidora es el encargado de la lectura en los puntos frontera de clientes.

• Lectura remota: captación de datos de medida de un registrador mediante la intervención de algún sistema o canal de comunicación.

• Lectura local: captación de datos de medida sin intervención del sistema de comunicaciones de los datos de medida de un registrador realizada mediante el acoplamiento al mismo de un terminal portátil de lectura (TPL). A los efectos del presente procedimiento, se entenderá que la lectura local absoluta se ha realizado a las 00:00:00 h del día d+1, siendo d el día de la lectura.

• Lectura visual por parte del Encargado de la lectura: captación manual por parte del Encargado de la lectura de datos de medida de un registrador anotando las medidas que refleja el visor del equipo de medida. A los efectos del presente procedimiento, se entenderá que la lectura visual absoluta se ha realizado a las 00:00:00 h del día d+1, siendo d el día de la lectura.

• Lectura comunicada o autolectura: Registros de las lecturas absolutas puestas a disposición del Encargado de la lectura por el consumidor, según lo establecido en el apartado 1 del artículo 2 del Real Decreto 1718/2012, de 28 de diciembre. A los efectos del presente procedimiento, se entenderá que la autolectura se ha realizado a las 00:00:00 h del día d+1, siendo d el día de la lectura. La medida proporcionada por el consumidor se referirá, en cualquier caso, a las energías absolutas correspondientes a cada periodo tarifario del periodo de facturación, y no a la curva de carga horaria.

• Validación: proceso mediante el cual se determina la adecuación de las medidas eléctricas registradas a los criterios de calidad establecidos.

• Estimación: proceso de tratamiento de las medidas mediante el cual se infiere la energía correspondiente a un determinado periodo y punto de medida, mediante un procedimiento de cálculo basado en otra información de medidas diferente de la real registrada según lo establecido en el presente procedimiento.

• Sistema de telegestión: sistema de medida y comunicación bidireccional entre los contadores y las distribuidoras eléctricas que, con las máximas garantías de integridad y seguridad, permite el acceso remoto a los contadores de energía eléctrica, con disponibilidad de lectura horaria, gestión de la energía, control de la potencia demandada y contratada, gestión de la conexión/desconexión de suministros y otras funcionalidades, posibilitando el intercambio de información y actuaciones entre los sistemas de las empresas y los contadores eléctricos.

Por otro lado, se definen determinados conceptos relacionados con la obtención y tratamiento de la Curva de Carga Horaria (en adelante, CCH):

• Lectura o medida real: las lecturas remotas, locales y visuales validadas por el encargado de la lectura. En los equipos situados en puntos frontera de clientes tipo 5 y efectivamente integrados en el sistema de telegestión la lectura visual o local se realizará excepcionalmente y por causas justificadas.

• Lectura absoluta: medida de energía acumulada total por periodo tarifario registrada por el equipo de medida desde 0 kWh.

• Resumen diario: registro almacenado en el equipo de medida del valor a las 00:00 h de cada día de los totalizadores absolutos (valores totales y por periodos tarifarios) de las 6 magnitudes de energía (activa de entrada o consumida, activa de salida o generada y reactivas de los cuatro cuadrantes).

• Saldo ATR: la energía consumida, en cada período tarifario, utilizada para facturar el término de energía de los peajes de acceso. Se obtendrá como la diferencia en kWh, en cada periodo tarifario, entre las lecturas absolutas del día inicial y final del periodo de facturación. Dichas lecturas serán tomadas a las 00:00 horas, excluyendo el día inicial e incluyendo el día final del periodo de facturación.

• CCH_BRUTA: CCH bruta. Es la CCH tal y como queda registrada en el equipo de medida y obtenida por el encargado de la lectura, bien de forma remota, local o visualmente, sin haber sido sometida a ningún proceso de validación ni estimación.

• CCH_VAL: CCH validada. Es la CCH resultante después de someter a la CCH_BRUTA al proceso de validación definido en el presente procedimiento.

• CCH_FACT: CCH a efectos de facturación al consumidor, en los casos que corresponda. Es la CCH después de ser validada, tratadas sus anomalías y, en su caso, estimados los huecos horarios de la misma de acuerdo al presente procedimiento.

3. Aspectos relativos la medida.

3.1 Prelación de la medida.

Las magnitudes necesarias para la facturación tanto de los peajes de acceso como de las CCH, podrán ser obtenidas de los diferentes modos y con el siguiente orden de prelación:

1. Remoto.

2. Local.

3. Visual por parte del Encargado de la lectura.

4. Comunicada por el cliente o autolectura.

Además de lo anterior, el saldo ATR tendrá prelación sobre la CCH a efectos de determinar las magnitudes que sirven de base para la facturación de los peajes de acceso y la obtención de la CCH.

3.2 Unidades de la medida.

Las unidades de medida empleadas en los diferentes registros de energía son, de acuerdo con lo establecido en la Orden ITC/3022/2007, de 10 de octubre, por la que se regula el control metrológico del Estado sobre los contadores de energía eléctrica, estáticos combinados, activa, clases a, b y c y reactiva, clases 2 y 3, a instalar en suministros de energía eléctrica hasta una potencia de 15 kW de activa que incorporan dispositivos de discriminación horaria y telegestión, en las fases de evaluación de la conformidad, verificación después de reparación o modificación y de verificación periódica, las siguientes:

• Curvas de carga en Wh.

• Medidas de los resúmenes diarios, cierres y medidas absolutas en kWh.

El tratamiento de los decimales que puedan surgir en el proceso del cálculo del saldo ATR y de la CCH_FACT será el establecido en el procedimiento de Operación 10.5.

4. Criterios para la validación de la medida.

Las medidas obtenidas por el Encargado de la lectura tanto de la CCH_BRUTA como las absolutas necesarias para el cálculo de los saldos de ATR, así como dichos saldos deberán ser previamente validadas por los encargados de la lectura para poder ser utilizadas en los procesos de facturación.

El encargado de la lectura establecerá uno de los siguientes estados de validación para cada medida o saldo ATR:

• Medida o saldo ATR válido:

Medida o saldo ATR que cumple todas las validaciones establecidas. Una medida o saldo ATR válido puede dejar de serlo como consecuencia del tratamiento de incidencias, por disponer de nueva información sobre dicha medida o por comprobaciones o validaciones posteriores realizadas por el encargado de la lectura.

• Medida o saldo ATR inválido:

Medida o saldo ATR que no cumple alguna de las validaciones establecidas. Una medida o saldo ATR inválido puede dejar de serlo como consecuencia de análisis posteriores de su encargado de la lectura.

4.1 Validación de la curva de carga horaria.

Los encargados de la lectura deberán realizar las siguientes validaciones de las medidas horarias de las curvas de carga horarias CCH obtenidas de forma remota por los sistemas de telegestión (CCH_BRUTA) y excepcionalmente a través de TPL:

a) Validación de bit de calidad:

Se considerarán medidas válidas las que tengan el bit de calidad correcto. Este bit de calidad será el detallado en el protocolo correspondiente a cada modelo de contador. En cualquier caso, deberá existir un bit de calidad relacionado con la falta de sincronización de los equipos.

b) Validación de eventos:

Se considerarán medidas inválidas las que considere el encargado de lectura como consecuencia del análisis de los eventos aportados por el contador (opcional).

c) Validación de integridad:

Se considerarán medidas inválidas las que no cumplan con las comprobaciones de integridad que aseguren que el origen inequívoco de las medidas.

d) Validaciones de fecha:

Se considerarán medidas inválidas aquellas con hora distinta de XX:00:00, fuera de rango del periodo a facturar, fechas futuras, fechas inexistentes o incoherentes para los periodos de cambio horario, fechas anteriores al inicio de contrato y similar.

e) Validación de consumo excesivo:

Se considerarán medidas inválidas aquellas cuyo valor de energía activa sea superior a 55 kWh.

f) Validaciones de comprobación de coherencia con otros orígenes de medida:

Se considerarán medidas inválidas las que no cumplan con comprobaciones que identifiquen incoherencias en la medida con otros orígenes de la medida (opcional).

g) Otras validaciones:

Se considerarán medidas inválidas las que no cumplan con otras comprobaciones realizadas por el encargado de la lectura que identifiquen incoherencias en los datos de la curva de carga horaria (opcional).

4.2 Validación de los resúmenes diarios o lecturas absolutas.

Los encargados de la lectura deberán realizar las siguientes validaciones de los resúmenes diarios o lecturas absolutas obtenidas de forma remota por los sistemas de telegestión que vayan a ser utilizados para calcular el saldo ATR:

a) Validación de bit de calidad:

Se considerarán válidas para el cálculo de un saldo ATR las lecturas absolutas que tengan el bit de calidad correcto. Este bit de calidad será el detallado en el protocolo correspondiente a cada modelo de contador.

b) Validación de eventos:

Se considerarán lecturas absolutas inválidas para el cálculo de un saldo ATR las que considere el encargado de lectura como consecuencia del análisis de los eventos aportados por el contador (opcional).

c) Validación de integridad:

Se considerarán lecturas absolutas inválidas para el cálculo de un saldo ATR las que no cumpla con las comprobaciones de integridad que aseguren el origen inequívoco de las medidas.

d) Validaciones de fecha:

Se considerarán inválidas para el cálculo de un saldo ATR las lecturas absolutas con hora distinta de 00:00, fechas futuras, fechas inexistentes o incoherentes para los periodos de cambio horario, fechas anteriores al inicio de contrato y similar.

Se considerará inválida la lectura absoluta inicial distinta a la última fecha validada o a la fecha de inicio del contrato.

Se considerará inválida la lectura absoluta final posterior a la fecha de fin de contrato.

4.3 Validaciones de las lecturas locales y visuales por el Encargado de la lectura.

Los encargados de la lectura deberán validar las lecturas locales o visuales que vayan a ser utilizados, en su caso, para calcular el saldo ATR, usando los criterios de validación de los resúmenes diarios o lecturas absolutas establecidos en el apartado anterior, que apliquen.

4.4 Validaciones a las lecturas comunicadas por clientes (autolecturas).

Los encargados de la lectura deberán validar las autolecturas que vayan a ser utilizadas, en su caso, para calcular el saldo ATR, comprobando que:

• No faltan ni sobran periodos con lectura aportada respecto a los periodos de la tarifa contratada.

• El número de dígitos de la lectura no supera al registrado en el sistema.

• La lectura es mayor o igual que la última lectura real empleada para facturar el suministro.

• La fecha de la lectura es mayor que la fecha de la última lectura facturada para el suministro.

4.5 Validación de saldo ATR.

Los encargados de la lectura deberán realizar las siguientes validaciones del saldo ATR:

Se considerará inválido el saldo ATR en el que la lectura absoluta final sea inferior a la lectura absoluta inicial. Esta validación tendrá en cuenta los posibles pasos por cero del contador. En el caso de no cumplirse la comprobación anterior se invalidará el saldo total y, para suministros con varios periodos tarifarios o discriminación horaria, se invalidará cada uno de los saldos.

Asimismo para suministros con varios periodos tarifarios o discriminación horaria, el consumo totalizado debe ser igual a la suma de consumos por periodo tarifario. El número de periodos tarifarios programados debe coincidir con el número de periodos tarifarios para los que existe medida. Caso de no coincidir, se considerarán no validos todos los saldos por periodo del equipo.

4.6 Validación de coherencia de la CCH_VAL con el saldo ATR.

En los casos en los que se disponga de saldo ATR válido y de CCH válida completa, los encargados de la lectura deberán comprobar que la diferencia por periodo tarifario entre el saldo ATR y la suma de todas las medidas válidas de la CCH correspondientes a cada periodo tarifario, para el periodo de facturación, sea menor que 1 kWh en términos absolutos. En caso contrario, se invalidarán las medidas de la curva de carga horaria y se procederá según el apartado 6.4. En estos casos, el encargado de lectura dará de alta una incidencia.

En el caso de saldos de ATR obtenidos con una lectura absoluta en una hora distinta de las 00:00, la comparación con la CCH se realizará teniendo en cuenta la hora real de la lectura absoluta. En caso de que el minutaje de dicha lectura absoluta sea distinto de cero, se considerará que está tomado en la hora anterior o posterior más cercana.

4.7 Invalidación sistemática de medidas de un punto de medida.

Cuando un encargado de la lectura identifique que las medidas procedentes de un punto de medida son invalidadas sistemáticamente se procederá de acuerdo a lo establecido en el PO10.5.

4.8 Plazos.

Los plazos para las validaciones de las medidas de las curvas de carga horarias de clientes tipo 5 serán los siguientes:

Medidas de la CCH: Las validaciones de bit de calidad y consumo excesivo se realizarán al día siguiente de la recepción de la CCH. Las validaciones de la CCH_BRUTA establecidas en el apartado 4.1 se realizarán semanalmente.

Lecturas absolutas para el cálculo de facturación de ATR: Mensualmente hasta el 5.º día hábil posterior a la fecha final del periodo de facturación según el procedimiento recogido en la normativa vigente en cada momento.

Validaciones de coherencia entre la medida de la CCH y saldos de ATR: Mensualmente hasta el 5.º día hábil posterior a la fecha final del periodo de facturación.

Las validaciones de las lecturas visuales o locales del encargado de la lectura y de las autolecturas se llevarán a cabo exclusivamente cuando se requieran de acuerdo a lo establecido en el apartado 6.

5. Incidencias en las medidas.

La medida de un suministro puede tener asociada una incidencia cuando se detecte algún tipo de situación que afecte al registro de energía por avería, verificación con inyección externa, desbordamiento, sustitución del equipo de medida, anomalías en la medida, gestión de inventario o contrato u otras causas debidamente justificadas.

Las incidencias en la medida serán tratadas de acuerdo a lo establecido en el apartado 3.4 Incidencias en puntos de medida del PO 10.5.

El plazo de emisión de incidencias y su resolución por parte del encargado de lectura será el establecido en el apartado 8 del PO 10.5.

6. Proceso de tratamiento y estimación de la CCH.

Captación de medidas.

Para la facturación del peaje de acceso, los plazos de registro del consumo no serán superiores a los tres días anteriores o posteriores a la finalización del mes a contar desde el último registro del consumo realizado, tal y como se establece en el apartado 2 del artículo 5 del Real Decreto 1164/2001, de 26 de octubre, por el que se establecen tarifas de acceso a las redes de transporte y distribución de energía eléctrica.

La captación de la CCH deberá realizarse, como mínimo, con una periodicidad semanal.

La captación de la CCH se prolongará, salvo que se obtenga una CCH completa y sin huecos, hasta el tercer día posterior a la finalización del mes a contar desde el último registro del consumo realizado, tratando de recuperar al menos diariamente los huecos existentes en la CCH correspondiente a los registros horarios de consumo del periodo de facturación. No obstante lo anterior, la recuperación de los huecos podrá extenderse durante un periodo superior siempre que la puesta a disposición de la CCH_FACT a las comercializadoras no se demore más que el plazo establecido en el apartado 3.3.3 del P.O. 10.13 «procedimiento por el que los distribuidores intercambian información con los comercializadores de energía eléctrica, y ponen a disposición de los comercializadores y los consumidores los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión».

Los encargados de la lectura realizarán las validaciones de la curva de carga horaria, de los resúmenes diarios o lecturas absolutas, del saldo ATR y de la coherencia de la CCH_VAL con el saldo ATR en los términos y los plazos establecidos en el apartado 4.

Una vez superados los plazos señalados para la recuperación de los huecos y validación de las medidas, podrán presentarse las situaciones contempladas en la siguiente tabla, debiéndose aplicar el proceso de tratamiento y/o estimación indicado:

| Situación tras fase de validación | Situación tras fase de tratamiento y estimación |
| --- | --- |
| Saldo ATR | CCH | Apartado del procedimiento | Tipo de saldo ATR | Tipo de medidas horarias de la CCH | Tipo de lectura en factura del consumidor |
| Válido | Válida y completa | 6.1 | Real | Real | Real |
| Inválido o no disponible | Válida y completa | 6.2 | Calculado | Real | Real |
| Inválido | Válida e incompleta o inválida o no disponible | 6.3.1 | Real por lectura local o visual del EdL válida | Real/Perfil | Real |
| Inválido | Válida e incompleta o inválida o no disponible | 6.3.2.a) | Estimado por autolectura válida | Real/Perfil | Estimada |
| Inválido o no disponible | Válida e incompleta o inválida o no disponible | 6.3.2.b) | Estimado | Real/Perfil | Estimada |
| Válido | Válida e incompleta | 6.4.a) | Real | Real/Perfil | Real |
| Válido | Inválida o no disponible | 6.4.b) | Real | Perfil | Real |
| Válido | Válida y completa diferencia con saldo ATR > 1kWh | 6.4.c) | Real | Ajustada | Real |
| Válido | Válida diferencia saldo ATR y CCH <-1 kWh | 6.4.d) | Real | Ajustada | Real |

6.1 Curvas válidas, sin huecos y coincidentes con los saldos de ATR.

En caso de que, tras haber superado los procesos de validación, se disponga de una CCH_VAL completa, sin huecos y coincidente con el saldo de ATR válido (con el margen de 1 kWh en términos absolutos establecido en este procedimiento), tanto el saldo ATR como la curva de carga horaria serán considerados reales a efectos de facturación y la curva CCH_VAL se convertirá en CCH_FACT y será puesta a disposición del comercializador.

6.2 Curvas válidas y sin huecos pero saldo ATR inválido o no disponible.

Para los casos en que el saldo ATR sea inválido o no se disponga del mismo, y se disponga de una curva horaria válida y sin huecos, el encargado de lectura deberá calcular el saldo ATR para cada periodo tarifario como la suma de las medidas válidas correspondientes a dicho periodo tarifario de la curva de carga horaria del periodo de facturación.

6.3 Proceso de estimación en caso de inexistencia de saldo de ATR y CCH no disponible o incompleta.

6.3.1 En caso de que no se disponga de saldo ATR obtenido a través del sistema de telegestión, ni de CCH_VAL completa se procederá a obtener el saldo ATR a partir otras medidas válidas de acuerdo con la prelación establecida en el apartado 3.1, esto es, a partir de la lectura absoluta local del Encargado de la lectura, de la lectura absoluta visual del Encargado de la lectura. Las medidas utilizadas para el cálculo del saldo ATR habrán sido previamente validadas de acuerdo a lo establecido en el apartado 4.

Si la falta de lectura real se debe a incidencia en el equipo de medida se procederá a la estimación del saldo ATR de acuerdo a lo indicado en el apartado b. El encargado de la lectura dispondrá de tres meses como máximo para resolver dicha incidencia.

6.3.2 En los casos en que, una vez superados los plazos de recuperación de huecos y validación, el encargado de la lectura no disponga de una lectura real válida de los equipos de medida necesaria para realizar la facturación del peaje de acceso se procederá a la estimación del saldo ATR, según el siguiente orden de prelación:

a) Autolectura del consumidor válida, de acuerdo con lo establecido en el apartado 4.4.

b) Estimación del saldo ATR de acuerdo con lo establecido en la Resolución de 14 de mayo de 2009, de la Dirección General de Política Energética y Minas, por la que se establece el procedimiento de facturación con estimación del consumo de energía eléctrica y su regularización con lecturas reales, con la siguiente prelación:

• Estimación en función de históricos del año anterior:

• Estimación según un factor de utilización de la potencia contratada:

Una vez obtenida la estimación de saldo ATR con el procedimiento correspondiente, se procederá a obtener la CCH de acuerdo con el procedimiento establecido en el apartado 6.4.

6.4 Proceso de estimación de la CCH.

En caso de que, tras haber superado los procesos de validación no se disponga de una CCH completa o ésta no sea coherente con el saldo ATR (con un margen de error de 1 kWh en términos absolutos), el encargado de la lectura procederá de la siguiente manera, para calcular la CCH_FACT:

a) Cuando exista una CCH_VAL válida pero con huecos, para obtener la CCH_FACT el encargado de la lectura mantendrá los valores horarios reales válidos disponibles en la CCH y estimará dichos huecos de acuerdo a lo establecido en el anexo 7 del PO 10.5. En caso de suministros con discriminación horaria, el proceso se realizará por periodos tarifarios.

El cálculo de la estimación de medidas de la CCH a partir del perfil de facturación correspondiente a la categoría del consumidor, se efectuará para cada ciclo de facturación que lo requiera a partir del saldo de ATR, de la suma de medidas horarias válidas disponibles y de los coeficientes del perfil ajustado a efectos de facturación calculados y publicados a estos efectos por el operador del sistema.

Para calcular las medidas horarias de la CCH no disponibles, la diferencia positiva entre el saldo de ATR y la suma de medidas horarias válidas disponibles se repartirá, para cada periodo tarifario, de forma proporcional a los coeficientes del perfil ajustado a efectos de facturación que calculará y publicará el operador del sistema para cada semana eléctrica el jueves anterior a la misma, a partir de los perfiles iniciales aprobados por resolución del Director General de Política Energética y Minas en desarrollo de lo previsto en el artículo 32 del Reglamento Unificado de Puntos de Medida del Sistema Eléctrico aprobado por el Real 1110/2007, de 24 de agosto, actualizando éstos últimos con la mejor estimación de demanda disponible..

b) Cuando no se disponga de la CCH _BRUTA o ésta se haya descartado completamente en el proceso de validación, para obtener la CCH_FACT el encargado de la lectura procederá a repartir la energía del saldo ATR para cada periodo tarifario de acuerdo a lo establecido en el apartado a).

c) Cuando la CCH_VAL no tenga huecos pero existan discrepancias en algún periodo tarifario entre la suma de las medidas de energía de la CCH_VAL y el saldo de ATR válido correspondientes a dicho periodo tarifario superiores a 1 kWh, se descartará la CCH_VAL para ese periodo tarifario y la CCH_FACT se obtendrá ajustando el saldo ATR correspondiente a ese periodo tarifario a la forma de la CCH_VAL de acuerdo a lo establecido en el anexo 8 del PO 10.5. En cualquier caso, el Encargado de la lectura deberá iniciar una incidencia en la medida al objeto de detectar el origen de las discrepancias.

d) Para los casos en que, en algún periodo tarifario, la diferencia entre el saldo ATR y la suma de medidas horarias disponibles sea negativo y superiores a 1 kWh en valor absoluto, las medidas horarias de la CCH no disponibles en ese periodo tarifario serán igual a 0 y se debe ajustar las medidas disponibles de la CCH al saldo ATR en ese periodo tarifario, de acuerdo a lo establecido en el anexo 8 del PO 10.5. En cualquier caso, el Encargado de la lectura deberá iniciar una incidencia en la medida al objeto de detectar el origen de las discrepancias.

7. Recálculo de las medidas de la CCH asociada a una modificación en un saldo ATR.

La CCH_FACT podrá ser objeto de modificación, de acuerdo a lo establecido en el apartado 3.3.4. del P.O. 10.13, en los siguientes supuestos:

a) Como consecuencia de una reclamación por parte del consumidor, dentro de los plazos establecidos en la normativa vigente.

b) En caso de modificación de la factura del peaje de acceso por modificación del saldo ATR.

En estos casos se obtendrá una nueva CCH_FACT, aplicando el proceso incluido en el apartado 6, en los plazos y condiciones establecidos en la normativa vigente.

En cualquier caso, una vez que se disponga de medida real de saldo ATR, se deberá volver a obtener CCH_FACT para todo el periodo comprendido entre las dos últimas lecturas reales.
