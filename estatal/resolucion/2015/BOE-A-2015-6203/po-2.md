## P.O. 10.5. Cálculo del Mejor Valor de Energía en los Puntos Frontera y Cierres de Energía del Sistema de Información de Medidas Eléctricas

1. Objeto.

Este procedimiento de operación tiene por objeto definir el tratamiento de medidas, cálculo del mejor valor de energía en los puntos frontera y cierres de energía del sistema de información de medidas eléctricas con el objeto de liquidar la energía en el mercado de producción.

Asimismo, en este procedimiento se definen los plazos establecidos para los procesos de medidas indicados en el párrafo anterior.

2. Ámbito de aplicación.

Este procedimiento es de aplicación a los participantes del sistema de información de medidas eléctricas.

El responsable de realizar el tratamiento de medidas y el cálculo del mejor valor de energía será el encargado de la lectura de cada punto.

Independientemente de quien sea el encargado de la lectura, el operador del sistema estimará las medidas de puntos o agregaciones que su encargado de la lectura no haya enviado antes del cierre provisional al concentrador principal de acuerdo con lo establecido en el P.O. 10.4. «Concentradores de medidas eléctricas y sistemas de comunicaciones».

El operador del sistema será el responsable de realizar las publicaciones de cierres de energías de acuerdo con lo indicado en este procedimiento.

Los encargados de la lectura son los responsables de resolver las objeciones de medidas o datos estructurales de acuerdo con lo indicado en este procedimiento.

3. Tratamiento de medidas de energía en puntos de medida.

3.1 General.

El cálculo del mejor valor de energía de cada punto frontera se obtendrá a partir de las medidas de los distintos puntos de medida. El cálculo del mejor valor de energía tendrá en consideración los siguientes factores:

• Tipos de medidas en puntos de medida.

• Tipo de configuración de cálculo de energía del punto frontera.

• Proceso de validación de medidas en puntos de medida y frontera.

• Incidencias en puntos de medida.

• Proceso de comprobación de medidas.

• Prelación de medidas y procedimientos de estimación.

• Objeciones en las medidas.

• Fecha de recepción de las medidas.

3.2 Tipos de medidas en punto de medida.

Cada punto de medida podrá tener asociadas distintas medidas, en función de su modo de obtención (lectura remota, lectura local, lectura visual o estimación), procedencia (operador del sistema, encargado de la lectura, participante responsable del punto de medida –en adelante participante 1–, participante no responsable del punto de medida –en adelante participante 2–, representante o comercializador), integridad, validación y fecha de obtención para los períodos de integración definidos en el Reglamento unificado de puntos de medida.

Las medidas pueden estar afectadas por coeficientes correctores de imprecisión. Dichos coeficientes se aplicarán a los distintos puntos de medida por imprecisiones detectadas en las verificaciones o por la utilización de equipos de medida que no cumplan los requisitos establecidos en el Reglamento unificado de puntos de medida. El cálculo de los coeficientes de imprecisión se realizará de acuerdo con lo indicado en el Anexo 1 de este procedimiento.

Las medidas podrán ser válidas o inválidas como consecuencia de los procesos de validación, comprobación y tratamiento de incidencias y objeciones que se indican en este procedimiento.

Se distinguen los siguientes tipos de medidas:

a. Medidas firmes.

Son las lecturas válidas obtenidas de forma local o remota de puntos de medida que cumplan los requisitos en cuanto a equipamiento, instalación e integridad recogidos en el Reglamento unificado de puntos de medida junto a lo indicado en los PP.OO. 10.1 y 10.2 (puntos de medida de instalaciones inspeccionadas con contadores verificados y con firma electrónica) indicadas a continuación:

• Medidas obtenidas por conexión directa entre concentrador principal del operador del sistema y registrador con firma electrónica correcta.

• Medidas obtenidas por conexión directa entre concentrador del encargado de la lectura y registrador (Nota 1).

• Medidas obtenidas por conexión entre concentrador principal del operador del sistema y concentrador secundario voluntario de registradores con firma electrónica correcta.

• Medidas obtenidas a través de lectura mediante terminal portátil de lectura (TPL) realizada por el encargado de la lectura.

• Medidas obtenidas a través de lectura mediante terminal portátil de lectura (TPL) realizada por cualquier participante del punto de medida con firma electrónica correcta.

• Lecturas visuales para aquellos puntos de medida que no requieran de registro horario de energía realizadas por el encargado de la lectura (Nota 2).

Nota 1: Estas medidas, aunque no dispongan de firma electrónica, podrán ser consideradas firmes de acuerdo con el criterio que establezca cada encargado de la lectura.

Nota 2: Las lecturas visuales para aquellos puntos de medida que no requieran de registro horario de energía realizadas por el encargado de la lectura tendrán consideración de firmes. No obstante, toda medida visual debe ser objeto de una validación automática por parte del encargado de la lectura, de forma que se descarten valores incoherentes.

b. Medidas provisionales.

Son las lecturas válidas obtenidas de forma local o remota de puntos de medida que no cumplan los requisitos en cuanto a equipamiento, instalación e integridad recogidos en el Reglamento unificado de puntos de medida junto a lo indicado en los procedimientos de operación 10.1 y 10.2 indicadas a continuación:

• Medidas obtenidas por conexión directa entre concentrador principal del operador del sistema y registrador sin firma electrónica o que no cumplen alguno de los requisitos del Reglamento unificado de puntos de medida (Nota 3).

• Medidas obtenidas por conexión entre concentrador principal del operador del sistema y concentrador secundario voluntario de registradores sin firma electrónica o cuyos equipos no cumplen alguno de los requisitos del Reglamento unificado de puntos de medida (Nota 4).

• Medidas obtenidas a través de lectura mediante terminal portátil de lectura (TPL) que no cumplen alguno de los requisitos del Reglamento unificado de puntos de medida.

Nota 3: Las medidas que tienen la consideración de provisionales por falta de carga de clave de firma electrónica acabarán siendo firmes si tras la lectura a través de TPL se comprueba la coincidencia entre la información del concentrador del encargado de la lectura con la almacenada en el registrador. Si no se comprueba por causas no imputables al operador del sistema (o no se puede comprobar por pérdida de información del registrador) dicha coincidencia antes del cierre del plazo de recepción de medidas, las medidas pasarán a considerarse estimaciones propuestas por el participante 1 al encargado de la lectura o inválidas. Adicionalmente, las medidas provisionales por incumplimientos en el Reglamento unificado que no queden resueltas antes del cierre provisional pasarán a considerarse estimaciones enviadas por el participante 1 o inválidas.

Nota 4: Las medidas que tienen consideración de provisionales por falta de envío de la firma electrónica pasarán a considerarse firmes una vez se reciba la firma electrónica correcta. Si no se envía dicha firma electrónica correcta antes del cierre del plazo de recepción de medidas, dichas medidas pasarán a considerarse estimaciones propuestas del participante 1 o inválidas. Adicionalmente, las medidas provisionales por incumplimientos en el Reglamento unificado que no queden resueltas antes del cierre provisional pasarán a considerarse estimaciones enviadas por el participante 1 o inválidas.

c. Estimaciones.

Son los datos de medidas válidos de puntos de medida que no son ni firmes ni provisionales obtenidos a partir de equipos o cálculos realizados por los participantes del punto de medida indicados a continuación:

• Estimaciones del encargado de la lectura.

• Estimaciones propuestas al encargado de la lectura por el participante responsable del punto de medida o su representante (participante 1) (Nota 5).

• Estimaciones propuestas al encargado de la lectura por el participante no responsable del punto de medida (participante 2) (Nota 5).

Las estimaciones utilizadas para el cálculo de mejor valor de energía descrito en el apartado 4.5 pasarán a ser firmes tras el plazo de resolución de objeciones.

Nota 5: Las estimaciones propuestas por los participantes podrán ser admitidas o no por el encargado de la lectura. Cuando un mismo participante envíe varias estimaciones para un mismo periodo de integración, el encargado de la lectura sólo considerará el último enviado. El plazo para recepción de estimaciones propuestas por los participantes coincidirá con los plazos límite de recepción de datos de medida definidos en el apartado 8 de este procedimiento.

3.3 Proceso de validación de medidas.

Los distintos tipos de medidas descritos en el apartado 3.2 deberán ser validados por los encargados de la lectura para poder ser utilizadas en el procedimiento de cálculo del mejor valor de energía en punto frontera. El encargado de la lectura establecerá uno de los estados de validación para cada medida en punto de medida:

a. Medidas válidas: Son aquellas que cumplen todas las validaciones establecidas. Una medida válida puede dejar de serlo como consecuencia del tratamiento de incidencias, por disponer de nueva información sobre la misma o por comprobaciones o validaciones posteriores realizadas por el encargado de la lectura.

b. Medidas inválidas: Son aquellas que no cumplen alguna de las validaciones establecidas. Una medida inválida puede dejar de serlo como consecuencia de análisis posteriores de su encargado de la lectura.

Los encargados de la lectura deberán poner a disposición de los participantes las medidas que pierdan la categoría de válidas junto al motivo de su invalidez.

Las medidas horarias inválidas podrán ser utilizadas, dependiendo del tipo de validación que las invalidó, para obtener el total de energía circulada en un intervalo de tiempo determinado tal como se indica en el apartado 4.4.

3.3.1 Validación de medidas.

No obstante lo previsto en el apartado 3.3.2 del presente procedimiento para clientes tipo 5 con medida horaria, los encargados de la lectura podrán realizar las validaciones que se describen a continuación:

a. Validación de cualificadores de registrador.

Se considerarán medidas válidas las procedentes de registrador sin los bits 1, 2, 3, 5, 6 y 7 marcados. Estos bits cualificadores están detallados en el protocolo de comunicaciones 8 entre registradores y concentradores definido en el P.O. 10.4.

Se considerarán medidas no válidas las procedentes de registrador con el bit de calidad de medida 7 marcado.

Las medidas procedentes de registrador que tengan alguno de los bits 1, 2, 3, 5 y 6 marcados podrán considerarse válidas o inválidas tras los análisis que realice el encargado de la lectura.

b. Validación de integridad.

Se considerarán medidas válidas las que tengan firma electrónica correcta tanto con su clave vigente como con la antigua (clave con fecha de caducidad anterior a la fecha actual).

Las medidas con firma electrónica incorrecta serán inválidas.

Los encargados de la lectura podrán considerar que todas las medidas obtenidas por comunicación directa desde su concentrador sin firma electrónica cumplen la validación de integridad.

c. Validación de eventos de registrador.

Los encargados de la lectura podrán analizar los eventos generados por los registradores que consideren más adecuados a fin de validar o invalidar medidas procedentes de registrador.

Los encargados de la lectura deberán hacer públicos a los participantes los procedimientos utilizados para realizar este tipo de validaciones, en caso de que sea solicitada cualquier aclaración al respecto. Este tipo de validaciones podrá ser función del fabricante o modelo de registrador.

d. Validación de coherencia de medidas de puntos de medida.

Los encargados de la lectura podrán invalidar medidas como consecuencia del análisis de datos de medida que identifiquen diferencias entre medidas horarias y lecturas absolutas de cierre diario o mensual de contador, acumulaciones horarias, periodos con energías que superan la potencia nominal del punto de medida, diferencias de valores entre distintos orígenes, pérdidas de sincronismo, comprobación frente a datos históricos y estadísticos del punto de medida u otras comprobaciones realizadas por el encargado de la lectura que identifiquen incoherencias en los datos de medida del punto de medida.

e. Validación de saldos y cierres de ATR de fronteras.

Las medidas de saldos de contador o cierres de facturación de puntos de medida de clientes deberán pasar las validaciones que se indican a continuación:

i) Validación por incoherencia en saldos o cierres de contador.

i.1 Las lecturas absolutas de saldos o cierres serán inferiores en valor a las lecturas de saldo o cierres realizados con posterioridad. Estas validaciones tendrán en cuenta los posibles pasos por cero del contador.

Se invalidarán individualmente los saldos o cierres que no cumplan la comprobación anterior.

i.2 El saldo total de un contador debe coincidir con la suma de todos los cierres siempre que se disponga de valor para todos y cada uno de ellos.

Caso de no cumplirse la igualdad anterior, se invalidará tanto el saldo total como cada uno de los cierres.

i.3 El número de cierres programados debe coincidir con el número de cierres para los que existe medida. Caso de no coincidir, se considerarán no validos todos los cierres del equipo (probable programación errónea).

ii) Validaciones por consumos excesivos.

ii.1 Si existe histórico de saldo de los doce últimos meses, el saldo a validar debe ser inferior al 120 % del mayor de los mismos.

ii.2 Caso de no existir el histórico anteriormente indicado, el saldo a validar debe ser inferior al producto de la máxima potencia contratada por el número de horas del periodo de saldo a considerar.

ii.3 Caso de no cumplirse cualquiera de las dos comprobaciones anteriores, no se tendrán en cuenta dichos saldos.

f. Invalidación por incumplimiento en el Reglamento unificado de puntos de medida.

Los encargados de la lectura podrán invalidar medidas de aquellos puntos de medida en que se identifiquen incumplimientos del Reglamento unificado de puntos de medida o en las disposiciones que lo desarrollan.

g. Validaciones como consecuencia de análisis de medidas en puntos frontera.

Los encargados de la lectura podrán invalidar medidas como consecuencia del análisis de datos de medida en punto frontera que identifiquen valores incompatibles, por periodos con energías que superan la potencia nominal del punto frontera, diferencias entre medidas de distintas configuraciones de cálculo de punto frontera, comparación frente a datos históricos y estadísticas del punto frontera u otras comprobaciones realizadas por el encargado de la lectura o el operador del sistema que identifiquen incoherencias en los datos de medida del punto frontera.

h. Validaciones manuales.

Los encargados de la lectura podrán invalidar medidas en punto de medida como consecuencia de análisis adicionales de la información disponible en punto de medida o frontera. Este tipo de invalidaciones, que han de ser debidamente documentadas por los encargados de lectura, aplican a periodos de integración afectados por verificación de puntos de medida, información de indisponibilidad de grupos de generación, información de instalaciones desconectadas, etc.

i. Invalidación sistemática de medidas de un punto de medida.

Cuando un encargado de la lectura identifique que las medidas procedentes de un punto de medida son invalidadas sistemáticamente por cualquiera de las causas recogidas en este procedimiento o cuando siendo válidas el encargado de la lectura detecta una posible anomalía que deba ser analizada o solucionada por el responsable del punto de medida, deberá comunicarlo al participante 1 y comercializador en las fronteras de clientes, al participante 1 o representante de puntos frontera de generación de los que el distribuidor es encargado de lectura o al participante 1 para el resto de tipos de fronteras a fin de que el responsable del punto de medida solucione las causas que lo provocan.

El responsable del punto de medida dispondrá de dos meses máximo para analizar las causas de la anomalía comunicada por el encargado de la lectura.

Si el responsable del punto de medida o su comercializador o representante no comunica las conclusiones del análisis antes de dos meses desde la comunicación por parte del encargado de la lectura, todas las medidas de dicho punto de medida serán invalidadas por el encargado de la lectura hasta que se realice el análisis.

Si de los análisis se concluye que existe una avería en alguno de los equipos de medida, el responsable del punto de medida deberá solucionarla en los plazos recogidos en el artículo 14 reglamento unificado de puntos de medida aprobado por el Real Decreto 1110/2007, de 24 de agosto, además de comunicarlo al encargado de la lectura para que éste dé de alta una incidencia según se indica en el apartado 3.4.

Si del análisis no se identifica la causa de la anomalía, se realizará una inspección y verificación de la instalación a petición del encargado de la lectura. Dicha inspección se realizará antes de los tres meses de la identificación de la anomalía por parte del encargado de la lectura. Las verificaciones e inspecciones como consecuencia de estos análisis serán costeadas:

• Si se supera la verificación correrán por cuenta del encargado de la lectura.

• Si no se supera la verificación, los gastos corren por cuenta del responsable del punto de medida. No obstante, correrán por cuenta del distribuidor los gastos ocasionados por el mal funcionamiento de un equipo de medida que haya puesto a disposición del responsable del punto de medida en alquiler.

3.3.2 Validación de medidas de clientes tipo 5 con medida horaria.

Los encargados de la lectura deberán realizar las validaciones sobre las medidas establecidas en el procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

A los efectos de este procedimiento se entiende que un punto de medida tipo 5 dispone de medida horaria cuando tenga telegestión operativa con curva de carga horaria de acuerdo con la definición dada en el procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

Invalidación sistemática de medidas de un punto de medida.

En los equipos de medida propiedad del consumidor, el procedimiento a seguir en el caso de invalidación sistemática de medidas de un punto de medida será el establecido en el apartado 3.3.1.

En el caso de equipos de medida en régimen de alquiler, cuando un encargado de la lectura identifique que las medidas procedentes de un punto de medida son invalidadas sistemáticamente por cualquiera de las causas recogidas en este procedimiento o cuando siendo válidas el encargado de la lectura detecta una posible anomalía que deba ser analizada o solucionada, deberá comunicarlo al participante 1 y al comercializador.

El encargado de la lectura dispondrá de dos meses máximo, desde la comunicación, para analizar las causas de la anomalía.

Si de los análisis se concluye que existe una avería en alguno de los equipos de medida, el encargado de la lectura dará de alta una incidencia según se indica en el apartado 3.4 y deberá solucionar la avería en los plazos recogidos en el artículo 14 reglamento unificado de puntos de medida aprobado por el Real Decreto 1110/2007, de 24 de agosto.

Si del análisis no se identifica la causa de la anomalía, se realizará una inspección y verificación de la instalación a petición del encargado de la lectura. Dicha inspección se realizará antes de los tres meses de la identificación de la anomalía por parte del encargado de la lectura. Las verificaciones como consecuencia de estos análisis serán costeadas, en su caso, por el encargado de la lectura.

3.4 Incidencias en puntos de medida.

3.4.1 General.

Una medida de un punto de medida podrá tener asociada una incidencia cuando se detecte algún tipo de situación que afecte al registro de energía del periodo de integración al que corresponde (averías en los equipos de medida, medidas correspondientes a energía inyectada durante la verificación del contador, problemas de desbordamiento, sustitución de equipos de medida, detección de errores en el inventario que afecten al cálculo de la medida, etc.). Para corregir la medida puede ser necesaria alguna modificación (invalidación de medidas, modificación de datos estructurales, etc.) en el concentrador del encargado de la lectura.

El emisor de la incidencia deberá poner la información de la misma a disposición de su encargado de la lectura y del resto de participantes a través de los canales y protocolos establecidos en los procedimientos de operación 10.4 y 10.11.

Los encargados de la lectura podrán solicitar información adicional al emisor si lo consideran necesario para resolver las incidencias comunicadas.

Las incidencias detectadas y tratadas por el propio encargado de la lectura no requieren ser comunicadas a los participantes.

No obstante, el encargado de la lectura comunicará los indicios de anomalías consecuencia del proceso de validación de medidas del 3.3. y que deben ser analizadas por el participante tal como se indica en el apartado 3.3. Si en un plazo de 2 meses, el participante no responde con el análisis de la incidencia, le será de aplicación el método de invalidación sistemática de medidas del apartado 3.3.

3.4.2 Consideraciones adicionales para incidencias de medidas de puntos frontera de los que el operador del sistema es encargado de la lectura.

Las incidencias en puntos de medida deben ser comunicadas por el participante 1 al encargado de la lectura. Cuando el participante 2 detecte cualquier incidencia, ésta será remitida al participante 1 que la transmitirá a su encargado de la lectura.

Los participantes podrán enviar incidencias al operador del sistema sobre los puntos de los que éste es encargado de lectura de acuerdo con los plazos establecidos en el apartado 8 de este procedimiento.

Las incidencias se comunicarán al encargado de la lectura en función de si están asociadas a datos de medidas o a datos estructurales de la siguiente forma:

• Incidencias asociadas a datos de medida de energía en puntos de medida.

Para la comunicación de una incidencia se aportará la información mínima que se indica a continuación:

◦ Identificación del punto de medida del que se comunica la incidencia.

◦ Identificación del participante 1.

◦ Fecha de detección de la incidencia.

◦ Fecha y hora de inicio de la incidencia.

◦ Fecha y hora de solución de la incidencia.

◦ Breve descripción de la incidencia.

◦ Cronología de actuaciones y descripción de cada una de las mismas para la solución de la incidencia por parte del responsable del punto de medida.

◦ Indicación de si existe acuerdo con el otro participante en la solución de la incidencia.

• Incidencias relativas a datos estructurales o configuraciones de cálculo de puntos frontera.

Las modificaciones de datos estructurales se comunicarán al encargado de lectura según lo indicado en el P.O. 10.7. «Alta, baja y modificación de fronteras de las que es encargado de la lectura el operador del sistema».

Adicionalmente, el participante 1 podrá aportar el saldo de energía para el intervalo afectado por la incidencia o propuesta de estimaciones para los periodos de dicho intervalo, que podrán ser utilizados por el encargado de lectura en el proceso de estimación que se indica en al apartado 4.4. En estos casos, el responsable del punto de medida indicará el método de obtención de los valores de energía propuestos al encargado de lectura así como si existe acuerdo con el otro participante en la propuesta de datos.

El encargado de lectura admitirá aquellas incidencias de puntos de medida que tras su estudio considere procedentes, en función de la información enviada y disponible. El encargado de lectura pondrá a disposición del participante 1 y del participante 2 la respuesta a las incidencias analizadas en cada plazo establecido en el apartado 8.

La aceptación de una incidencia que suponga la invalidación de los datos de medidas afectados por la misma, implica la obtención de un nuevo valor de energía. Para aquellos casos en que no se disponga de nueva medida firme en frontera, el encargado de lectura estimará el mejor valor según el proceso descrito en 4.4.

Independientemente de todo lo indicado sobre la comunicación y revisión de incidencias, el operador del sistema podrá desarrollar los procedimientos, canales y métodos que considere más adecuados a fin de facilitar los intercambios de información de incidencias.

El encargado de la lectura revisará y resolverá las incidencias en los plazos establecidos en el apartado 8 de este procedimiento.

3.4.3 Consideraciones adicionales para incidencias de medidas de puntos frontera de generación de los que el distribuidor es encargado de lectura.

Las incidencias en puntos frontera de instalaciones de generación de los que el distribuidor es encargado de lectura serán comunicadas por el representante de la instalación al encargado de la lectura. Cuando el titular de la instalación detecte cualquier incidencia, ésta será remitida al representante para que la transmita a su encargado de la lectura.

El operador del sistema no recibirá información de dichas incidencias.

El plazo de emisión de incidencias y su resolución por parte del encargado de la lectura será el establecido en el apartado 8 de este procedimiento.

El encargado de la lectura deberá actualizar los datos de la agregación que se pudiesen ver afectados como resultado de la resolución de las incidencias y enviar los nuevos datos agregados al operador del sistema en el plazo establecido en el apartado 8 de este documento.

Las incidencias de medidas deberán ser notificadas utilizando los mismos formatos que para la solicitud de objeciones de medidas de puntos frontera de generación de los que el distribuidor es encargado de lectura. Los encargados de lectura deberán comunicar la respuesta a las incidencias, así como los motivos de su rechazo, en su caso.

3.5 Proceso de comprobación de medidas.

La comprobación de una medida tiene por objeto contrastar que las medidas firmes captadas por el concentrador del encargado de la lectura coinciden con la información almacenada en un registrador de medidas. Cuando existan diferencias entre la medidas firmes almacenadas en el concentrador del encargado de la lectura y la contenida en el registrador de medidas, y sin perjuicio de las sanciones administrativas que pudieran corresponder al responsable del punto de medida o al encargado de la lectura, el encargado de la lectura o la Administración competente analizarán la causa de las discrepancias y establecerán las actuaciones para su resolución. Adicionalmente, se procederá a realizar una revisión de las medidas firmes del periodo que pudiera estar afectado por el proceso de comprobación de acuerdo con lo indicado en el artículo 30 del Reglamento unificado de puntos de medida. La frecuencia con que se comprobarán las medidas de un punto de medida serán las establecidas en las instrucciones técnicas complementarias.

Adicionalmente, para puntos en que el operador del sistema es el encargado de la lectura, el proceso de comprobación se aplicará en los casos en que a juicio del encargado de lectura sea necesario realizar lecturas visuales de contador para validar los saldos totales de energía que permitan aplicar el procedimiento indicado en el apartado a) del apartado 4.4.1 cuando por ausencia de medidas firmes sea necesario realizar una estimación de medidas. En caso de que el responsable del punto no acepte que el encargado de lectura lleve a cabo estas lecturas, le será de aplicación la estimación que penaliza indicada en el apartado 4.4.1.

El coste de las lecturas de comprobación será asumido por el encargado de la lectura si las medidas del registrador coinciden con la información almacenada en el concentrador del encargado de la lectura y por el participante 1 en caso de no coincidencia.

4. Cálculo del mejor valor de energía en punto frontera.

4.1 General.

El cálculo del mejor valor de energía en punto frontera lo realizará el encargado de la lectura.

Antes de los cierres provisional o definitivo cada punto frontera deberá tener asociado para cada uno de los periodos de integración un valor de energía.

El cálculo del mejor valor de energía se realizará al menos para las magnitudes de energía de acuerdo con la siguiente tabla:

| Actividades de la frontera | Activa saliente | Activa entrante | Reactiva (nota 6) |
| --- | --- | --- | --- |
| Interconexiones internacionales o entre subsistemas eléctricos | X | X |  |
| Generación | X |  | X |
| Distribución con distribución o transporte | X | X |  |
| Consumidor |  | X | X |

Nota 6: En fronteras de generación se registrarán las medidas de los cuadrantes 2 y 3 de energía reactiva de aquellas instalaciones donde sea necesario obtener el factor de potencia.

En fronteras de clientes en las que el cálculo del ATR utilice magnitudes de reactiva se registrarán las medidas de los cuadrantes 1 y 4 de dicha energía reactiva.

El cálculo del mejor valor de energía en cada frontera puede obtenerse a partir de medidas firmes o no. La disponibilidad de medidas firmes en una frontera determinará la necesidad o no de estimar medidas para dicha frontera.

Cada punto frontera puede tener asociados para cada periodo de integración distintos valores de energía en sucesivos cierres de medidas en función de la existencia o no de medidas en cada uno de los citados cierres de los distintos tipos descritos en el apartado 3.2 de este documento.

4.2 Tipos de configuraciones de cálculo de energía en puntos frontera.

Cada punto frontera, en función de sus características, deberá disponer de una configuración principal y, si aplica, configuraciones redundante o comprobante de acuerdo con lo establecido en el Reglamento unificado de puntos de medida.

4.2.1 Configuración principal.

Equipo de medida instalado (salvo las excepciones indicadas en los siguientes párrafos) en un punto de medida coincidente con el punto frontera que se utiliza como medida única a efectos de lo dispuesto en el Reglamento unificado de puntos de medida. Dicho punto de medida deberá cumplir los requisitos establecidos en el Reglamento unificado de puntos de medida junto con lo indicado en los PP.OO. 10.1 y 10.2.

En los puntos de medida de fronteras de generación con distribución y transporte o fronteras de distribución con transporte o fronteras de clientes cuya ubicación no coincida con la situación del punto frontera, el encargado de la lectura aplicará, a las medidas obtenidas por lectura del registrador, una corrección por pérdidas de energía activa y reactiva de acuerdo con los coeficientes indicados en el Anexo 2 de este documento.

No obstante lo anterior, en los puntos de medida de fronteras de instalaciones de producción de energía eléctrica a partir de fuentes de energía renovables, cogeneración y residuos o fronteras distribución - distribución cuya ubicación no coincida con la situación del punto frontera, se aplicarán los coeficientes acordados entre los participantes. En fronteras de instalaciones que utilicen como combustible energías renovables, cogeneración y residuos, los coeficientes deberán figurar en los contratos técnicos suscritos con el distribuidor. Si no se definen coeficientes específicos para la energía reactiva se utilizarán los mismos que para la energía activa.

La corrección por pérdidas a considerar deberá figurar expresamente en las comunicaciones de altas provisionales y definitivas descritas en el P.O. 10.1 «Condiciones de instalación de los puntos de medida» y en los contratos técnicos. En ningún caso será admisible programar el equipo de medida para que descuenten o consideren dichas pérdidas en la medida que efectúa.

Independientemente de lo indicado anteriormente, previo acuerdo entre el encargado de la lectura y los participantes de una frontera se podrán establecer puntos de medida alternativos siempre que resulte equivalente el cálculo de energía intercambiada.

4.2.2 Configuración redundante.

Equipo de medida instalado en el mismo punto frontera que un equipo principal, cuyas medidas deben ser prácticamente coincidentes con las de éste. Dicho equipo de medida deberá cumplir los requisitos establecidos en el Reglamento unificado de puntos de medida junto con lo indicado en los PP.OO. 10.1 y 10.2.

En los puntos de medida de fronteras de generación con distribución y transporte o fronteras de distribución con transporte o fronteras de clientes cuya ubicación no coincida con la situación del punto frontera, el encargado de la lectura aplicará, a las medidas obtenidas por lectura del registrador, una corrección por pérdidas de energía activa y reactiva de acuerdo con los coeficientes indicados en el Anexo 2 de este documento.

No obstante lo anterior, en los puntos de medida de fronteras de instalaciones de producción de energía eléctrica a partir de fuentes de energía renovables, cogeneración y residuos o fronteras distribución - distribución cuya ubicación no coincida con la situación del punto frontera, se aplicarán los coeficientes acordados entre los participantes siempre que cumplan los requisitos establecidos en el Anexo 3 de este procedimiento. En fronteras de instalaciones que utilicen como combustible energías renovables, cogeneración y residuos, los coeficientes deberán figurar en los contratos técnicos suscritos con el distribuidor. Si no se definen coeficientes específicos para la energía reactiva se utilizarán los mismos que para la energía activa.

Independientemente de lo indicado en el párrafo anterior, previo acuerdo entre el encargado de la lectura y los participantes de una frontera se podrán establecer puntos de medida alternativos siempre que resulte equivalente el cálculo de energía intercambiada.

4.2.3 Configuración comprobante.

Equipo o conjunto de equipos de medida instalados en el otro extremo de un solo elemento (línea, transformador, etc.) respecto del equipo o equipos de medida que forman la configuración principal del punto frontera. Las medidas en la frontera de los equipos comprobantes pueden compararse con las del principal, mediante un cálculo sencillo con determinados coeficientes, que eliminen el efecto del elemento de red que pudiera existir entre ambos. Dicho/s punto/s de medida deberá/n cumplir los requisitos establecidos en el Reglamento unificado de puntos de medida junto con lo indicado en los PP.OO. 10.1 y 10.2.

Los coeficientes correctores, siempre en sentido opuesto al participante responsable (minorando la energía suministrada y aumentando la energía adquirida por éste), se utilizarían para poder comparar los datos del equipo de medida de la configuración principal y, si fuera necesario, para sustituirlos.

Los coeficientes de energía activa (y de reactiva, si es de aplicación) se calcularán de acuerdo con lo indicado a continuación:

a. Tras el alta de puntos de medida comprobantes:

Durante los primeros tres meses se utilizarán los coeficientes indicados en el Anexo 2 de este documento, si fuera necesario utilizar las medidas de los puntos de medida comprobantes.

Después de los primeros tres meses indicados en el párrafo anterior, a solicitud de cualquiera de los participantes, y una vez se disponga simultáneamente de medidas de configuraciones principal y comprobante durante más de un mes consecutivo, siendo ambas medidas firmes, completamente válidas y cumpliendo todos los requisitos, se calcularán los coeficientes, si fuera necesario, de acuerdo con lo indicado en el Anexo 4 de este documento, aplicando dichos coeficientes de la misma forma que en el apartado b).

b. Coeficientes a partir de registros históricos:

A solicitud del propietario o su representante, y con una frecuencia no inferior a dos años, se calcularán los coeficientes correspondientes a la configuración comprobante de acuerdo con lo indicado en el Anexo 4 de este documento.

Dichos coeficientes se utilizarían, si fuera necesario, para sustituir las medidas de la configuración principal por los de la configuración comprobante, en el caso de ausencia de medidas o avería en el primero.

Los coeficientes propuestos deberán cumplir los requisitos establecidos en el Anexo 3 de este procedimiento. En fronteras de instalaciones que utilicen como combustible energías renovables, cogeneración y residuos, los coeficientes deberán figurar en los contratos técnicos suscritos con el distribuidor. Si no se definen coeficientes específicos para la energía reactiva se utilizarán los mismos que para la energía activa.

4.3 Calculo del mejor valor de energía de un punto frontera.

El encargado de la lectura asignará para cada punto frontera el mejor valor horario de energía activa (y de reactiva, si es de aplicación) de cada periodo de integración, a partir de las medidas válidas de punto de medida de acuerdo con lo indicado en el apartado 3.

La energía en frontera será la medida válida o combinación de medidas válidas de mejor prelación posible de las indicadas a continuación (de mayor a menor prelación):

1. Medidas firmes en configuración principal.

La medida del punto frontera se corresponderá con la medida firme del punto de medida principal. La medida firme del punto de medida principal se podrá ver afectada por los coeficientes de pérdidas definidos en 4.2.2, en caso de que se hubiera admitido explícitamente como configuración principal del punto frontera un punto de medida cuya ubicación no coincida con la del punto frontera.

Para fronteras que de acuerdo con el Reglamento unificado de puntos de medida no requieran de equipo de medida horario se obtendrán a partir del saldo de contador principal (firme) perfilado de acuerdo con el perfil y método de cálculo a efectos de liquidación de energía vigente establecido por el Ministerio de Industria, Energía y Turismo. Para el caso de fronteras de instalaciones que utilicen como combustible energías renovables, cogeneración y residuos, en tanto no exista método especifico, se utilizarán los perfiles definidos en la normativa de aplicación.

2. Medidas firmes en configuración redundante.

La medida del punto frontera se corresponderá con la medida firme del punto de medida redundante. La medida firme del punto de medida redundante se podrá ver afectada por los coeficientes de pérdidas definidos en 4.2.3, en caso de que se hubiera admitido explícitamente como configuración redundante del punto frontera un punto de medida cuya ubicación no coincida con la del punto frontera.

3. Medidas firmes de equipos de medida en configuración comprobante.

La medida del punto frontera se obtendrá como combinación lineal de medidas firmes de los puntos de medida que conformen la configuración comprobante afectadas por los coeficientes descritos en 4.2.4.

4. Medidas provisionales en configuración principal.

La medida del punto frontera se corresponderá con la medida provisional del punto de medida principal. La medida provisional del punto de medida principal se podrá ver afectada por los coeficientes de pérdidas definidos en 4.2.2, en caso de que se hubiera admitido explícitamente como configuración principal del punto frontera un punto de medida cuya ubicación no coincida con la del punto frontera.

5. Medidas provisionales en configuración redundante.

La medida del punto frontera se corresponderá con la medida provisional del punto de medida redundante. La medida provisional del punto de medida redundante se podrá ver afectada por los coeficientes de pérdidas definidos en 4.2.3, en caso de que se hubiera admitido explícitamente como configuración redundante del punto frontera un punto de medida cuya ubicación no coincida con la del punto frontera.

6. Medidas provisionales en configuración comprobante.

La medida del punto frontera se obtendrá como combinación lineal de medidas firmes y provisionales de los puntos de medida que conformen la configuración comprobante afectadas por los coeficientes descritos en 4.2.4.

Las medidas en frontera de prelaciones 4, 5 y 6 descritas anteriormente, que tienen la consideración de provisionales, deberán pasar a ser consideradas medidas firmes, medidas inválidas o estimaciones propuestas por el responsable del punto de medida (cuando siendo válidas no puedan ser consideradas firmes) antes del cierre provisional de medidas de acuerdo con lo descrito en el apartado 3.2.

4.4 Calculo del mejor valor de energía estimado en punto frontera.

Todo punto frontera o agregación debe tener una medida asignada en el cierre provisional. Con este objetivo, el encargado de la lectura estimará el mejor valor horario de energía de cada periodo de integración para el que no es posible asignar una medida según el apartado anterior.

Los datos disponibles que podrán ser utilizados para el cálculo de la mejor estimación de un punto frontera serán los que se indican a continuación:

• Datos de medidas estimadas descritos en el apartado 3.2.

• Saldo total de energía del intervalo de períodos a estimar validado por el encargado de la lectura.

• Otras informaciones válidas a criterio del encargado de la lectura.

Para la obtención del mejor valor estimado en frontera se establecen distintos procedimientos de acuerdo con lo indicado a continuación.

4.4.1 Fronteras de las que es encargado de la lectura el operador del sistema.

La estimación de medidas se realizará de acuerdo con uno de los dos procedimientos que se indican a continuación:

Estimación que penaliza al responsable del punto de medida.

El encargado de lectura aplicará una estimación que penalice al responsable del punto de medida en los casos en que la ausencia de medida para un periodo de integración sea debida a cualquiera de los siguientes motivos:

• Ausencia de medidas firmes o provisionales sin disponer de incidencia asociada según el apartado 3.4, siempre que la ausencia de medidas no sea por causas imputables al operador del sistema.

• Invalidación de medidas por falta de integridad sin justificar por parte del responsable a través de incidencia asociada según el apartado 3.4.

• Invalidación de medidas por incumplimiento del Reglamento unificado de puntos de medida.

• Invalidación de medidas por causa sistemática sin solucionar en plazos establecidos.

• No aceptación del responsable del punto de medida de una solicitud de lectura visual como consecuencia de un proceso de comprobación según apartado 3.5.

• Otras invalidaciones que a criterio del encargado de la lectura son consecuencia de incumplimientos o dejación de funciones por parte del responsable del punto de medida.

El encargado de lectura estimará en función del tipo de frontera y sentido de energía de la siguiente forma:

• Para puntos frontera de generación:

▪ Energía activa saliente: 0 kWh.

▪ Energía activa entrante: energía correspondiente a la potencia máxima entrante.

• Para puntos frontera de distribución con transporte o distribución.

▪ Energía activa saliente: 0 kWh.

▪ Energía activa entrante: energía correspondiente a la potencia máxima entrante.

Estimación mejor posible.

En los casos en que la ausencia de medida para un periodo de integración no sea debida a cualquiera de los motivos indicados en el apartado anterior, el encargado de lectura obtendrá la mejor estimación posible atendiendo a los siguientes criterios generales:

a. Si existe medida válida del saldo total de energía del intervalo de períodos a estimar, la suma de las estimaciones de los periodos coincidirán con el valor de dicho saldo. El saldo del total de energía podrá obtenerse a través de los siguientes métodos:

• Lecturas visuales de contador realizadas por el encargado de lectura.

• Cierres diarios o mensuales de contador validados por el encargado de lectura.

• Medidas inválidas según el procedimiento de validación del apartado 3.3 que aun habiendo sido invalidadas al no ser correcto el perfil del intervalo pueden aportar información para la obtención del saldo del intervalo de periodos a estimar.

• Saldo de energía aportado por el responsable del punto de medida para un intervalo de periodos afectados por una incidencia comunicada según el apartado 3.4 y validado por el encargado de lectura.

b. Los participantes del punto frontera podrán proponer al encargado de lectura las estimaciones que consideren oportunas para los periodos a estimar por el encargado de lectura. Estas estimaciones podrán ser admitidas o no por el encargado de lectura y deberán ser sometidas al procedimiento de validación del apartado 3.3. Las estimaciones propuestas deberán llevar indicación del método por el que se han obtenido, y que puede ser:

• Registrador de medidas.

• Acumulación de impulsos de contador obtenido por el participante.

• Integral de telemedida de potencia realizada por el participante.

• Estimador de estado del participante.

• Saldo total de energía modulado.

• Otros métodos.

• Para el caso de que el participante proponga varias estimaciones para el mismo periodo de integración, el encargado de lectura considerará únicamente la última estimación propuesta, con independencia del método por el que ésta haya sido obtenida.

c. Adicionalmente, el encargado de lectura podrá disponer de las estimaciones validadas según el procedimiento de validación del apartado 3.3 y obtenidas por los siguientes métodos de mayor a menor prelación:

• Indisponibilidad de grupo o instalación fuera de servicio o desconectada.

• Acumulación de impulsos de contador obtenido por el encargado de lectura.

• Integral de telemedida de potencia realizada por el encargado de lectura.

• Estimador de estado del encargado de lectura.

d. Para los casos en los que la medida del punto frontera se obtenga como combinación de medidas de varios puntos de medida y no se dispongan de medidas firmes de todos los puntos de medida, el encargado de lectura podrá estimar la medida en punto frontera combinando las medidas firmes de los puntos de medida para los que sí se disponga de medidas firmes con la mejor estimación posible de los otros puntos de medida que intervienen en la configuración y para los que sea necesario aplicar el procedimiento de estimación. En este caso, la medida en punto frontera estará calificada con el tipo de medida correspondiente a la medida de peor calidad de las utilizadas.

La energía en frontera será la estimación o combinación de estimaciones/medidas firmes válidas de mejor prelación posible de las indicadas a continuación (de mayor a menor prelación):

1. Si existen medidas estimadas propuestas por ambos participantes, validadas por su encargado de lectura según el procedimiento de validación del apartado 3.3 y éstas son coincidentes con una tolerancia del 5%, se tomará como medida la media de ambas estimaciones. Si adicionalmente existe saldo obtenido según lo indicado en el punto a) de este apartado, se mejorará la estimación utilizando dicho saldo.

2. Si existen medidas estimadas propuestas por ambos participantes, validadas por su encargado de lectura según el procedimiento de validación del apartado 3.3 y éstas no son coincidentes con una tolerancia del 5%, el encargado de lectura estimará en función del sentido de energía de la siguiente forma:

• Energía activa saliente: la menor estimación de las disponibles, incluida las del encargado de lectura, si existiesen, indicadas en el punto c). Si adicionalmente existe saldo obtenido según lo indicado en el punto a) de este apartado, se mejorará la estimación utilizando dicho saldo.

• Energía activa entrante: la mayor estimación de las disponibles, incluida las del encargado de lectura, si existiesen, indicadas en el punto c). Si adicionalmente existe saldo obtenido según lo indicado en el punto a) este apartado, se mejorará la estimación utilizando dicho saldo.

3. Si existen medidas estimadas propuestas por un único participante, validadas por el encargado de lectura según el procedimiento de validación del apartado 3.3, y existiese estimación del encargado de lectura según lo indicado en el punto c), se realizará la estimación conforme a los puntos 1 y 2, en función de la comparación de ambas estimaciones.

4. Si existen medidas estimadas propuestas por un único participante, validadas por el encargado de lectura según el procedimiento de validación del apartado 3.3, y no existe estimación del encargado de lectura según lo indicado en el punto c), se utilizarán aquellas medidas en la estimación. Si adicionalmente existe saldo obtenido según lo indicado en el punto a) de este apartado, se mejorará la estimación utilizando dicho saldo.

5. Si existe estimación del encargado de lectura según lo indicado en el punto c) y no existen medidas estimadas propuestas por los participantes, se utilizará dicha medida en la estimación. Si adicionalmente existe saldo obtenido según lo indicado en el punto a) de este apartado, se mejorará la estimación utilizando dicho saldo.

6. Si sólo existe como dato válido el saldo obtenido según lo indicado en el punto a) de este apartado, el encargado de lectura estimará a partir de uno de los siguientes métodos de modulación de saldo, elegido en función del tipo de punto y otros aspectos a criterio del encargado de lectura:

• Estimación en base a históricos según se indica en apartado 3.2 del Anexo 5.

• Estimación en base al programa de venta o compra (corregido o no por un desvío histórico calculado o constante) de la unidad de programación a la que pertenece el punto frontera.

• Interpolación de medidas firmes en periodos de los extremos.

• Perfil plano.

• Otros métodos.

7. Si no existe ningún dato que se considere válido, y el número consecutivo de periodos sin medida sea igual o inferior a 3 periodos de integración, el encargado de lectura estimará a partir de uno de los siguientes métodos, en función del tipo de punto y otros criterios adicionales:

• Estimación en base a históricos según se indica en el apartado 3.1 del Anexo 5, para huecos iguales o inferiores a 3 periodos de integración.

• Interpolación de medidas firmes en periodos de los extremos.

• Suma de medidas cuarto-horarias válidas del periodo a estimar.

• Otros métodos.

8. Si no existe ningún dato que se considere válido, y el número consecutivo de periodos sin medida sea superior a 3 periodos de integración, el encargado de lectura estimará en función del tipo de frontera y sentido de energía de la siguiente forma:

• Para puntos frontera de generación:

– Energía activa saliente: 0 kWh.

– Energía activa entrante: energía correspondiente a la potencia máxima entrante.

• Para puntos frontera de distribución con transporte o distribución.

– Energía activa saliente: 0 kWh.

– Energía activa entrante: energía correspondiente a la potencia máxima entrante.

Para el caso en que por la información disponible no sea posible aplicar el proceso de estimación o a criterio del encargado de la lectura la estimación realizada no resulte válida, el encargado de la lectura podrá realizar una estimación técnicamente justificada, cuya metodología deberá ser puesta a disposición de los participantes que lo soliciten.

4.4.2 Fronteras tipos 1, 2 y 3 de clientes.

La estimación de medidas se realizará de acuerdo con uno de los dos procedimientos que se indican a continuación:

Estimación que penaliza al consumidor.

En puntos frontera de clientes tipos 1, 2 y 3, en los que el consumidor o comercializador es propietario del equipo de medida y se den cualquiera de las situaciones que se describen a continuación:

• Cuando no sea posible la toma de lectura local por TPL, por imposibilidad de acceso a los equipos del consumidor, siempre que la responsabilidad sea achacable a dicho consumidor.

• Cuando no sea posible la toma de lectura por avería del registrador y el encargado de la lectura no disponga de una incidencia comunicada por el consumidor según apartado 3.4 de este procedimiento.

• Cuando no sea posible la toma de lectura por avería del registrador y se hayan superado por el consumidor los plazos establecidos para la resolución de dicha avería desde la comunicación de la misma por parte del encargado de la lectura.

• En el caso de puntos tipos 1 y 2, cuando no sea posible la toma de lectura por telemedida debido a avería del módem y el encargado de la lectura no disponga de una incidencia comunicada por el consumidor según apartado 3.4 de este procedimiento.

• En el caso de puntos tipos 1 y 2, cuando no sea posible la toma de lectura por telemedida debido a avería del módem y se hayan superado por el consumidor los plazos establecidos para la resolución de dicha avería desde la comunicación de la misma por parte del encargado de la lectura.

• Cuando el registrador no funcione adecuadamente, proporcionando una medida inválida y el encargado de la lectura no disponga de una incidencia comunicada por el consumidor según apartado 3.4 de este procedimiento.

• Cuando no sea posible la toma de lectura, local o remota, debido a que el propietario de los equipos de medida no comunique al encargado de la lectura los parámetros necesarios para tomar la lectura, local o remota.

• Otras invalidaciones como consecuencia de incumplimientos o dejación de funciones por parte del consumidor o propietario del equipo de medida.

El encargado de la lectura estimará la energía de acuerdo con el siguiente criterio:

• Energía activa saliente: 0 kWh.

• Energía activa entrante: energía correspondiente a la potencia máxima contratada multiplicada por su factor de utilización (relación entre el tiempo de operación del suministro y el tiempo que está disponible; por defecto se utilizará un factor de utilización de larga duración (575 h/mes)). Es decir, se penaliza con la potencia contratada por el máximo factor de utilización, el de larga duración.

Estimación mejor posible.

En caso de no disponer de valor de energía de acuerdo con lo indicado en 4.3 y no ser de aplicación la estimación que penaliza, el encargado de la lectura estimará un valor de energía en función de los datos disponibles atendiendo al siguiente orden de prelación (de mayor a menor prelación):

1. Estimación de energía a partir de cierres de ATR.

La energía horaria en punto frontera se obtendrá por una estimación basada en datos históricos del punto de medida principal modulada con los cierres de ATR de contador validados de acuerdo con lo indicado en el apartado 3.3 de este documento. Se pueden dar dos casos:

a. En el supuesto de falta de uno o varios intervalos de periodos y el número de dichos periodos de integración consecutivos sin medida sea inferior o igual a tres, se utilizará el algoritmo de cálculo descrito en el apartado 3.3 del Anexo 5.

b. En el supuesto de falta de uno o varios intervalos de periodos y el número de periodos de integración consecutivos sin medida sea superior a tres, el periodo a estimar no supere más de treinta y un días consecutivos y no haya cambio de mes en las medidas a estimar se utilizará el algoritmo de cálculo descrito en el apartado 3.4 del Anexo 5.

2. Estimación de energía horaria basada en el histórico del punto de medida principal modulado con su saldo.

La energía horaria en punto frontera se obtendrá por una estimación basada en datos históricos del punto de medida principal modulada con el saldo de contador validado de acuerdo con lo indicado en el apartado 3.3. de este documento. Se pueden dar dos casos:

a. En el supuesto de falta de uno o varios intervalos de periodos y el número de dichos periodos de integración consecutivos sin medida sea inferior o igual a tres, se utilizará el algoritmo de cálculo descrito en el apartado 3.5 del Anexo 5.

b. En el supuesto de falta de uno o varios intervalos de periodos y el número de dichos periodos de integración consecutivos sin medida sea superior a tres, el periodo a estimar no supere más de treinta y un días consecutivos y no haya cambio de mes en las medidas a estimar se utilizará el algoritmo de cálculo descrito en el apartado 3.6 del Anexo 5.

3. Estimación basada en histórico del punto de medida principal (sin datos de saldo o de cierre de ATR).

La energía horaria en punto frontera se obtendrá por una estimación basada en datos históricos del punto de medida principal. Se pueden dar dos casos:

a. En el supuesto de falta uno o varios intervalos de periodos y el número de periodos de integración consecutivos sin medida sea inferior o igual a tres, se utilizará el algoritmo de cálculo descrito en el apartado 3.1 del Anexo 5.

b. En el supuesto de falta de uno o varios intervalos de periodos y el número de periodos de integración consecutivos sin medida sea superior a tres, el periodo a estimar no supere más de treinta y un días consecutivos y no haya cambio de mes en las medidas a estimar se utilizará el algoritmo de cálculo descrito en el apartado 3.2 del Anexo 5.

4. Estimación técnicamente justificada tras incidencia en el equipo de medida.

En el supuesto de falta de medidas de periodos así como suficientes datos horarios históricos, el encargado de la lectura podrá realizar estimaciones de energías basados en estudios técnicamente justificados de cualquier información disponible del punto de medida, cuya metodología deberá ser puesta a disposición de los participantes que lo soliciten.

5. Estimación de energía horaria realizada basada en un factor de utilización del 33%.

Estimación de energía activa entrante del punto de medida principal igual al equivalente de suponer el 33% de la potencia contratada circulando constantemente durante todos los períodos de integración.

4.4.3 Fronteras tipo 3 de instalaciones de generación de los que el distribuidor es el encargado de lectura.

El encargado de la lectura aplicará el procedimiento de estimación descrito en 4.4.1 para fronteras tipo 3 de generación de instalaciones de generación cuyo encargado de la lectura es el distribuidor.

4.4.4 Fronteras tipo 4 de clientes.

En el caso de no disponer de valor de energía de acuerdo con lo indicado en el apartado 4.4, el encargado de lectura calculará el mejor valor para cada periodo de un punto frontera, en función de los datos de medidas disponibles de cierre atendiendo al siguiente orden de prelación (de mayor a menor prelación):

1. Estimación de medida de cierre a partir de datos históricos.

La energía de cada uno de los cierres en punto frontera se obtendrá a partir de una estimación a partir de históricos de cierres. Se pueden dar tres casos:

a. En el supuesto que sólo falte uno de los cierres disponiendo del resto de los cierres y del saldo validado de acuerdo con lo indicado en el 3.3 de este documento, la estimación del cierre a estimar será la diferencia entre el saldo y el sumatorio de los cierres disponibles.

b. En el supuesto que falte más de uno de los periodos de cierre y se disponga del saldo validado de acuerdo con lo indicado en el apartado 3.3 de este documento, la estimación se realizará de acuerdo con el procedimiento descrito en el apartado 4.2 del Anexo 5.

c. En el supuesto que falten más de uno de los periodos de cierre y no se disponga de saldo validado de acuerdo con lo indicado en el apartado 3.3.5 de este documento, la estimación de los cierres se realizará de acuerdo con el procedimiento descrito en el apartado 4.1 del Anexo 5.

2. Estimación de medidas a partir del saldo de contador si no se dispone de histórico.

La energía de cada uno de los cierres en punto frontera se obtendrá a partir del saldo total validado de acuerdo con lo indicado en el 3.3 de este documento. Se pueden dar dos casos:

a. En el caso de que sólo falte uno de los cierres disponiendo del saldo validado según lo indicado en el apartado 3.3 de este documento, la estimación del cierre será la diferencia entre el saldo y la suma del resto de los cierres.

b. En el supuesto de que falten más de uno de los cierres disponiendo del saldo validado según lo indicado en el apartado 3.3 de este documento, cada uno de ellos se calculará de acuerdo con el procedimiento descrito en el apartado 4.3 del Anexo 5.

3. Estimación técnicamente justificada tras incidencia en el equipo de medida.

En el supuesto de falta de medidas de periodos así como de suficientes datos de cierres históricos, el encargado de la lectura podrá realizar estimaciones de cierres basados en estudios técnicamente justificados de cualquier información disponible del punto de medida, cuya metodología deberá ser puesta a disposición de los participantes que la soliciten.

4. Estimación basada en factor de utilización del 33%.

Estimación de energía activa entrante del punto de medida principal igual al equivalente de suponer el 33% de la potencia contratada circulando constantemente durante todo el periodo a estimar.

Los valores de energía horarios se obtendrán a partir del saldo obtenido según lo indicado en el apartado anterior perfilado de acuerdo con el perfil y método de cálculo a efectos de liquidación de energía vigente establecido por el Ministerio de Industria, Energía y Turismo.

4.4.5 Fronteras tipo 5 de clientes sin medida horaria.

Obtención del/los saldo/s.

En el caso de no disponer de valor de energía de acuerdo con lo indicado en el apartado 4.3, el encargado de lectura estimará el mejor valor de un punto frontera, en función de los datos de medidas disponibles atendiendo al procedimiento descrito en la Resolución de 14 de mayo de 2009 de la Dirección General de Política Energética y Minas, y sus modificaciones, por la que se establece el procedimiento de facturación con estimación del consumo de energía eléctrica y su regularización con medidas reales.

Perfilado.

Los valores de energía horarios se obtendrán a partir del saldo obtenido según lo indicado en el apartado anterior, perfilado de acuerdo con el perfil final y método de cálculo a efectos de liquidación de energía vigente establecido por el Ministerio de Industria, Energía y Turismo en virtud de lo establecido en el artículo 32 del Reglamento Unificado de Puntos de medida del sistema eléctrico aprobado por el Real Decreto 1110/2007, de 24 de agosto.

4.4.6 Fronteras tipo 5 de clientes con medida horaria.

Principios generales.

La curva de carga horaria utilizada para la facturación de los consumidores acogidos al precio voluntario para el pequeño consumidor (CCH_FACT según su definición dada en el P.O. 10.12 «Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión») será igualmente utilizada para el cálculo de la agregación de puntos fronteras de clientes tipo 5 a efectos de liquidación de la energía en el mercado de producción de acuerdo con lo establecido en el P.O.10.6. «Agregaciones de puntos de medida»

La curva de carga horaria y el saldo ATR utilizados para la facturación se obtendrán de acuerdo con lo establecido en el procedimiento de operación 10.12.

La curva de carga horaria CCH_FACT, definida en el PO 10.12, puesta a disposición de los comercializadores en aquellos puntos de suministro no acogidos al precio voluntario para el pequeño consumidor será igualmente utilizada para el cálculo de la agregación de puntos fronteras de clientes tipo 5 a efectos de liquidación de la energía en el mercado de producción de acuerdo con lo establecido en el procedimiento de operación 10.6.

Una vez calculado el mejor valor de energía en un punto frontera tipo 5 de clientes con medida horaria de acuerdo con el procedimiento de operación 10.12, la medida en dicho punto frontera estará calificada con el tipo de medida que se indica a continuación.

Saldo ATR.

De acuerdo con lo establecido en el procedimiento de operación 10.12, una vez vencidos los plazos de los procesos para la captación, validación y, en su caso, tratamiento de incidencias de las medidas de clientes tipo 5 por los sistemas de telegestión podrán darse los siguientes casos:

| Relación ATR-CCH | Saldo de ATR | Curva de carga horaria |
| --- | --- | --- |
| Caso a1. | Válido. | Válida, completa. |
| Caso a2. | Válido. | Válida, completa, diferencia con saldo de ATR en valor absoluto > 1kWh. Válida incompleta, diferencia con saldo ATR en valor absoluto >1 Kwh. |
| Caso b. | Inválido o no se dispone. | Válida, completa. |
| Caso c. | Válido. | Válida, incompleta o no se dispone. |
| Caso d. | Inválido o no se dispone. | Válida, incompleta. |
| Caso e. | Inválido o no se dispone. | No se dispone. |

Para el caso a1, el saldo de ATR y la curva de carga horaria se considerarán firmes en los procesos de liquidación.

Para el caso a2, el saldo de ATR se considerará provisional en el proceso de liquidación.

Para el caso b el saldo ATR se calculará de acuerdo con lo establecido en el apartado 6.2 del procedimiento de operación 10.12. Una vez calculado, el saldo de ATR calculado se considerará firme y la CCH se considerará firme en el proceso de liquidación.

Para el caso c, el saldo de ATR se considerará firme en el proceso de liquidación.

Para los casos d y e, el saldo ATR se obtendrá de acuerdo con lo establecido en el apartado 6.3 del procedimiento de operación 10.12:

• Si el saldo de ATR se ha obtenido a partir de la lectura absoluta local o visual del encargado de lectura, una vez calculado, el saldo de ATR se considerará firme.

• Si el saldo de ATR se ha obtenido por auto-lectura absoluta visual del cliente se considerará provisional.

• Si el saldo de ATR se ha obtenido por estimación en función de históricos del año anterior, el saldo ATR se considerará provisional y del tipo de estimación empleado.

• Si el saldo de ATR se ha obtenido por estimación según un factor de utilización de la potencia contratada, el saldo ATR se considerará provisional y del tipo de estimación empleado.

En la siguiente tabla se resumen los distintos tipos de saldos de ATR con indicación de firmeza, origen y prelación.

| Relación ATR - CCH | Tipo | Firmeza del saldo de ATR | Origen del saldo de ATR | Prelación |
| --- | --- | --- | --- | --- |
| Caso a1 y c. | Real. | Firme. | Telegestión. | 1 |
| Caso a2. | Real. | Provisional. |
| Caso b. | Calculado. | Firme. | Telegestión. | 2 |
| Caso d y e. | Lectura absoluta local o visual del encargado de lectura. | Firme. | Local. | 3 |
| Caso d y e. | Auto-lectura absoluta visual del cliente. | Provisional. | Local. | 4 |
| Caso d y e. | Estimado en función de históricos del año anterior. | Provisional. | Estimación. | 5 |
| Caso d y e. | Estimado según un factor de utilización de la potencia contratada. | Provisional. | Estimación. | 6 |

En el Anexo 9 de este procedimiento se incluyen a modo de ejemplo cada uno de los casos de relación entre el saldo de ATR y su CCH asociada.

CCH.

En el caso de que la CCH sea incompleta parcial o totalmente para el periodo de facturación (casos c, d y e) o exista una diferencia mayor de 1 kWh en términos absolutos con el saldo de ATR válido (caso a2), el encargado de lectura deberá estimar o ajustar la curva de carga horaria de acuerdo con lo establecido en el apartado 6.4 del procedimiento de operación 10.12.

Una vez obtenida la Curva de carga horaria quedará marcada de acuerdo con lo establecido a continuación:

| Código | Método de obtención |
| --- | --- |
| 1 | Medida real válida. |
| 2 | Medida perfilada. |
| 3 | Medida real ajustada a un saldo de ATR. |
| 4 | Medida perfilada correspondiente a auto-lectura de cliente. |
| 5 | Estimación por consumo histórico del año anterior perfilado. |
| 6 | Estimación por factor de utilización perfilado. |

• Para el caso c:

Las medidas de la curva de carga horaria se obtendrán, según corresponda, de acuerdo con lo establecido en el apartado 6.4.a) o 6.4.b) del procedimiento de operación 10.12. Las medidas horarias perfiladas quedan marcadas con el método de obtención 2.

• Para el caso a2:

Las medidas de la curva de carga horaria se obtendrán de acuerdo con lo establecido en el apartado 6.4.c) o 6.4.d) del procedimiento de operación 10.12. Las medidas horarias ajustadas quedan marcadas con el método de obtención 3.

• Para los casos d y e:

Si el saldo de ATR se ha obtenido a partir de la lectura absoluta local o visual del encargado de lectura, las medidas de la curva de carga horaria se obtendrán, según corresponda, de acuerdo con lo establecido en el apartado 6.4.a) o 6.4.b) del procedimiento de operación 10.12. Las medidas horarias perfiladas quedan marcadas con el método de obtención 2.

Si el saldo de ATR se ha obtenido por auto-lectura absoluta visual del cliente se considerará provisional, las medidas de la curva de carga horaria se obtendrán, según corresponda, de acuerdo con lo establecido en el apartado 6.4.a) o 6.4.b) del procedimiento de operación 10.12. Las medidas horarias perfiladas quedan marcadas con el método de obtención 4.

Si el saldo de ATR se ha estimado en función de históricos, las medidas de la curva de carga horaria se obtendrán, según corresponda, de acuerdo con lo establecido en el apartado 6.4.a) o 6.4.b) del procedimiento de operación 10.12. Las medidas horarias perfiladas quedan marcadas con el método de obtención 5.

Si el saldo de ATR se ha estimado en función de un factor de utilización, las medidas de la curva de carga horaria se obtendrán, según corresponda, de acuerdo con lo establecido en el apartado 6.4.a) o 6.4.b) del procedimiento de operación 10.12. Las medidas horarias perfiladas quedan marcadas con el método de obtención 6.

En la siguiente tabla se resumen los distintos tipos de CCH con indicación del tipo de saldo de ATR asociado y su firmeza:

| Relación ATR - CCH | Tipo de Saldo de ATR | Método de obtención de la CCH | Código de método de obtención | Tipo de medida de la CCH |
| --- | --- | --- | --- | --- |
| Caso a1. | Real. | Real. | 1 | Firme. |
| Caso a2. | Real. | Ajustada. | 3 | Firme. |
| Caso b. | Calculado. | Real. | 1 | Firme. |
| Caso c. | Real. | Real/Ajustada/Real/Perfil. | 1/3/1/2 | Firme/Estimación. |
| Caso d y e. | Lectura absoluta local o visual del encargado de lectura. | Real/Ajustada/Real/Perfil. | 1/3/1/2 | Firme/Estimación. |
| Caso d y e. | Auto-lectura absoluta visual del cliente. | Real/Ajustada/Real/Perfil. | 1/3/1/4 | Firme/Estimación. |
| Caso d y e. | Estimado en función de históricos del año anterior. | Perfil. | 5 | Estimación. |
| Caso d y e. | Estimado según un factor de utilización de la potencia contratada. | Perfil. | 6 | Estimación. |

En el Anexo 9 de este documento se incluyen a modo de ejemplo cada uno de los casos de relación entre el saldo de ATR y su CCH asociada.

Modificación del saldo ATR y de la CCH.

La curva de carga horaria o el saldo ATR de facturación podrán ser objeto de modificación en los supuestos contemplados en el procedimiento de operación 10.12. Toda modificación del saldo ATR o de la CCH_FACT, supondrá una modificación de las medidas utilizadas para calcular las agregaciones a efectos de liquidación:

• Un saldo de ATR provisional podrá sustituirse por un saldo firme o provisional de mejor prelación. En estos casos, el nuevo saldo de ATR deberá tenerse en cuenta en los procesos de facturación (re-facturación) y liquidación.

• Una medida estimada de una CCH podrá sustituirse por una medida firme o una nueva estimación exclusivamente si se modifica el saldo de ATR o si existe reclamación del consumidor. La nueva CCH deberá tenerse en cuenta tanto en los procesos de facturación (re-facturación) como de liquidación.

En los casos en los que se haya producido el cierre definitivo de medidas, las modificaciones del saldo ATR o de la curva de facturación se incluirán como «restos» de acuerdo con lo establecido en el apartado 8.13.

Un saldo de ATR provisional pasará a firme en la publicación del cierre definitivo de medidas.

Una medida estimada de una CCH pasará a firme en la publicación del cierre definitivo de medidas.

4.4.7 Fronteras tipo 5 de instalaciones de generación de las que el distribuidor es encargado de lectura.

En el caso de no disponer de valor de energía de acuerdo con lo indicado en el apartado 4.3, el encargado de lectura estimará la energía entrante de acuerdo con lo indicado en el apartado 4.4.5.

Los valores horarios de energía generada se obtendrán utilizando los perfiles publicados en la normativa de aplicación con las siguientes consideraciones:

• Las instalaciones hidráulicas se perfilarán con perfil plano y en caso de que el saldo de lectura corresponda a más de un mes se aplicará el reparto de energía a cada mes de acuerdo con los factores de funcionamiento indicados en la normativa de aplicación.

• Las instalaciones fotovoltaicas se perfilarán a partir del saldo de contador aplicando los coeficientes horarios definidos a efectos de liquidación de energía vigente indicados en la normativa de aplicación de acuerdo con:

Valor energía periodo = Saldo contador * coeficiente horario/Pt

Siendo Pt el sumatorio de los coeficientes horarios definidos para el periodo a perfilar a que corresponde el saldo.

En los casos en que la falta de medida de energía saliente pueda ser debido a incumplimientos o dejación de funciones por parte del responsable del punto de medida, la estimación de energía saliente podrá ser 0 kWh.

4.5 Estimaciones de datos de energía realizadas por el operador del sistema en puntos frontera de los que los distribuidores son encargados de la lectura.

El operador del sistema estimará los datos de medidas de puntos frontera y agregaciones de consumidores y de agregaciones de instalaciones de generación de los que los distribuidores son encargados de lectura vigentes en el concentrador principal y no comunicados a éste por su encargado de la lectura, de acuerdo con lo siguiente:

a. Los puntos de suministro tipos 1 y 2 y agregaciones de consumidores tipos 3, 4, y 5 se estimarán a partir del procedimiento de estimación en base a datos históricos descrito en el Anexo 5 de este procedimiento.

b. Las agregaciones de instalaciones tipos 3 y 5 de instalaciones de generación se estimarán a 0 kWh en todos los periodos con ausencia de medida. En estos casos el operador del sistema deberá remitir a la Comisión Nacional de los Mercados y la Competencia la relación de encargados de la lectura que no remiten los datos de medida que puedan suponer un incumplimiento de las obligaciones de lectura.

El operador del sistema no estimará los puntos o agregaciones cuyo encargado de la lectura sea el distribuidor y que no hayan sido dados de alta en el concentrador principal por su encargado de la lectura.

4.6 Periodicidad del cálculo del mejor valor de energía en punto frontera.

Antes del cierre provisional cada punto frontera deberá tener asociado para cada uno de los periodos de integración un valor de energía firme o estimado. La existencia de mejor valor de energía en punto frontera antes del cierre provisional está condicionada a la fecha de recepción y firmeza de las medidas.

En función de la disponibilidad de datos de medida asociados a cada frontera el encargado de la lectura deberá realizar el cálculo y ponerlo a disposición del resto de participantes con un retraso máximo de 24 horas.

El cálculo del mejor valor de energía de cada punto frontera se realizará mientras no se haya realizado el cierre definitivo de medidas al menos en los casos y momentos descritos en el apartado 8 de este procedimiento.

4.7 Periodicidad de cálculo de agregaciones de puntos frontera de clientes y de puntos frontera de generación de los que el distribuidor es encargado de lectura.

A efectos de liquidación, el distribuidor deberá calcular las agregaciones de medida de acuerdo con el P.O.10.6, a partir de los datos de mejor valor horario de energía de los puntos frontera de clientes tipos 3, 4 y 5 y de los puntos frontera de generación de los que el distribuidor es el encargado de lectura,

El cálculo de agregaciones y su puesta a disposición del operador del sistema y del resto de participantes se realizará con los mejores valores horarios disponibles para realizar las publicaciones periódicas descritas en los PP.OO. 10.4 y 10.11. Adicionalmente y mientras no se haya realizado el cierre definitivo, si ha habido modificación en las medidas de alguna frontera de la agregación, se deberá calcular y publicar las nuevas medidas agregadas al menos en los casos y momentos descritos en el apartado 8 de este procedimiento.

Independientemente de las publicaciones anteriores, el encargado de la lectura podrá enviar al operador del sistema actualizaciones de medidas agregadas si dispone de mejores datos con las limitaciones establecidas en este procedimiento. Las medidas serán procesadas si el periodo de aceptación de medidas está abierto de acuerdo con lo indicado en el apartado 8 de este procedimiento de operación.

5. Publicación de energías liquidables.

5.1 Publicación de energías liquidables al sistema de liquidaciones del operador del sistema.

El concentrador principal pondrá a disposición del sistema de liquidaciones del operador del sistema los datos de medidas de acuerdo con los plazos definidos a fin de que pueda realizar las funciones que legalmente tiene asignadas. El operador del sistema, no adelantará en ningún caso la estimación de datos de medidas en frontera de las que no es encargado de la lectura fuera de los plazos indicados en este procedimiento.

Las publicaciones llevadas a cabo por el concentrador principal al sistema de liquidaciones para la realización de las liquidaciones descritas en apartado 6 del P.O. 14.1 «Condiciones generales del proceso de liquidación del operador del sistema» serán, al menos, las que se indican en el apartado 8 de este procedimiento.

Adicionalmente, el concentrador principal publicará la información de medidas necesaria para que los sujetos puedan comprobar sus liquidaciones de acuerdo con los medios y protocolos descritos en el P.O. 10.4.

5.2 Publicación de energías al órgano encargado de las liquidaciones del régimen retributivo específico.

Los encargados de lectura pondrán a disposición del órgano encargado de las liquidaciones del régimen retributivo específico los datos de medidas por CIL de acuerdo con los formatos y plazos que se establezcan en la normativa correspondiente.

Adicionalmente, los encargados de lectura publicarán las mismas medidas a los participantes de cada instalación, de forma que la energía enviada al organismo encargado de la liquidación del régimen retributivo específico y la existente en concentrador principal de medidas sea coincidente.

6. Cierres de energía.

6.1 Introducción.

Se define cierre de energía de un mes M es al hito en que las medidas o agregaciones de energía de los puntos frontera del sistema son o bien puestos a disposición del sistema de liquidaciones para su liquidación o bien puestos a disposición de los sujetos y encargados de lectura afectados para su comprobación.

Las medidas o agregaciones de medidas de los puntos frontera publicadas en cada cierre podrán ser provisionales o definitivas.

En la publicación de cada cierre de energía se incorporarán las medidas de los tipos de puntos frontera que sean necesarios para la liquidación correspondiente.

El operador del sistema efectuará en cada cierre las publicaciones necesarias para que los sujetos y los encargados de lectura puedan comprobar los datos de medidas de energía de su liquidación, así como publicaciones previas al cierre como avance de los mismos.

Se deben habilitar los intercambios de información necesarios para que los sujetos puedan poner en conocimiento de los encargados de lectura y del operador del sistema las reclamaciones a los datos de medida del cierre. Cada cierre y cada tipo de punto frontera podrán tener un mecanismo de tratamiento de reclamaciones diferente.

El operador del sistema publicará a los distintos participantes por los medios establecidos en el P.O. 10.4 los datos de medidas de cada cierre indicados en ese apartado.

Los plazos para la recepción de medidas para los distintos cierres y para las publicaciones del operador del sistema se recogen en el apartado 8 de este procedimiento.

6.2 Cierre del mes M+1.

El procedimiento de cierre en el mes M+1 de medidas se realiza con una periodicidad mensual correspondiente a las medidas del mes anterior y en los plazos establecidos en el apartado 8 de este procedimiento.

Con las medidas recibidas hasta el plazo límite de recepción de datos de medidas para el cierre en el mes M+1, el operador del sistema efectuará los tratamientos de medidas necesarios a fin de realizar el cierre del mes M+1 y su publicación. Las medidas correspondientes a un cierre del mes M+1 podrán ser firmes o provisionales.

Para el cierre en el mes M+1 el operador del sistema no estimará las medidas de agregaciones de las que no es encargado de la lectura por no haberlas enviado su encargado de la lectura al concentrador principal.

Los plazos para la recepción de medidas para un cierre en el mes M+1 y para las publicaciones del operador del sistema y los formatos de los distintos ficheros de estas publicaciones se recogen en el apartado 8 de este procedimiento.

6.3 Cierre del mes M+3.

El procedimiento de cierre en el mes M+3 de medidas se realiza con una periodicidad mensual correspondiente a las medidas de tres meses anteriores y en los plazos establecidos en el apartado 8 de este procedimiento.

Con las medidas recibidas hasta el plazo límite de recepción de datos de medidas para el cierre en el mes M+3, el operador del sistema efectuará los tratamientos de medidas necesarios a fin de realizar el cierre del mes M+3 y su publicación. Las medidas correspondientes a un cierre del mes M+3 podrán ser firmes o provisionales.

Para el cierre en el mes M+3 el operador del sistema no estimará las medidas de agregaciones de las que no es encargado de la lectura por no haberlas enviado su encargado de la lectura al concentrador principal.

Los plazos para la recepción de medidas para un cierre en el mes M+3 y para las publicaciones del operador del sistema y los formatos de los distintos ficheros de estas publicaciones se recogen en el apartado 8 de este procedimiento.

6.4 Procedimiento de comunicación de pre-objeciones.

Se define como pre-objeción a cualquier disconformidad con la medida de un punto frontera de un consumidor de cualquier tipo que se comunica previamente al cierre provisional de medidas.

Se distinguen dos tipos de pre-objeciones, en función de quién es el participante que las detecta:

• Detectadas por el distribuidor: Las pre-objeciones como consecuencia de validaciones o realización de verificaciones, u otras que pudiese detectar el encargado de lectura, no requieren ser comunicadas al comercializador ni al operador del sistema. Las medidas quedarían actualizadas por nuevas publicaciones del encargado de lectura, antes de la publicación del cierre provisional.

• Detectadas por el comercializador: Cualquier pre-objeción que detecte el comercializador será comunicada al operador del sistema quien las pondrá en conocimiento del encargado de lectura correspondiente.

Las pre-objeciones de medidas de los consumidores tipo 5 las comunicará el comercializador al operador del sistema mediante los formatos y medios de transmisión establecidos. El operador del sistema incorporará en su sistema las pre-objeciones que pasen las validaciones requeridas y publicará el acuse de recibo de dichas objeciones a los participantes implicados en la misma (comercializador y distribuidor).

Las pre-objeciones se pueden clasificar en dos niveles:

a. Pre-objeciones a la agregación.

b. Pre-objeciones al valor mensual de un punto de suministro.

Las pre-objeciones no deben ser respondidas por parte el encargado de lectura. En caso de que aplicara, las pre-objeciones podrían dar lugar a nuevas publicaciones de medidas del encargado de lectura antes de la publicación del cierre provisional.

Los plazos para la recepción y publicación de pre-objeciones y para las publicaciones del operador del sistema tras un cierre del mes M+3 y los formatos de los distintos ficheros de estas publicaciones se recogen en el apartado 8 de este procedimiento.

6.5 Cierre de energía provisional.

El procedimiento de cierre provisional de medidas se realiza con una periodicidad mensual y en los plazos establecidos en el apartado 8 de este procedimiento.

A partir del cierre de recepción de datos de medidas, el operador del sistema comenzará a realizar los tratamientos de medidas necesarios a fin de realizar el cierre provisional y su publicación. Las medidas utilizadas en el cierre provisional deberán ser firmes o estimaciones. Las medidas provisionales deberán pasar a ser medidas firmes, medidas inválidas o estimaciones de acuerdo con lo indicado en el apartado 4.3.

Los tratamientos antes citados incluyen la estimación de medidas utilizando el procedimiento de estimación descrito en el apartado 4.4.

El operador del sistema procederá a estimar las medidas de puntos frontera o agregaciones de las que no es encargado de la lectura por no haberlas enviado su encargado de la lectura al concentrador principal de acuerdo con lo indicado en el apartado 4.4.

La estimación por parte del operador del sistema de medidas de puntos frontera o agregaciones de las que no es encargado de la lectura no exime a los encargados de lectura de la responsabilidad en los incumplimientos del envío de medidas en que hubieran podido incurrir.

Las estimaciones publicadas para cualquier tipo de frontera podrán dar lugar a facturaciones a los distribuidores o responsables de los puntos de medida por el servicio de estimación de medidas, siempre que el motivo de la estimación sea imputable a los mismos.

El operador del sistema publicará a los distintos participantes por los medios y formatos establecidos en el P.O. 10.4 los datos de medidas en cierre provisional de los que son participes. Simultáneamente se publicarán al sistema de liquidaciones.

Excepcionalmente, el operador del sistema podrá realizar republicaciones del cierre provisional efectuados como consecuencia de reclamaciones recibidas a través del sistema de liquidaciones. Las republicaciones se harán públicas a los participantes afectados sin que se vean modificados los plazos de objeción de medidas.

El plazo de publicación del cierre provisional de medidas se establece en el apartado 8 de este procedimiento.

6.6 Periodo de objeción de medidas.

Las objeciones de medidas tienen por objeto solicitar al encargado de la lectura la revisión y el recálculo, si aplica, de las medidas de un punto frontera en uno o más periodos de integración de un mes en cierre provisional.

Las objeciones de medidas de un punto frontera las podrá realizar cualquier participante del mismo. Las objeciones de medidas deberán ser notificadas a los encargados de la lectura, participantes, comercializadores, clientes directos a mercado, representantes u operador del sistema, según cada caso, utilizando los medios y protocolos definidos en el PP.OO. 10.4 y 10.11.

Los propios encargados de la lectura pueden objetar medidas de puntos frontera de los que son encargados de la lectura. Este tipo de objeciones se denominan auto – objeciones y deberán ser tratadas de la misma forma que las objeciones, a excepción de su plazo de emisión.

El responsable de resolver las posibles objeciones es el encargado de la lectura.

Para la presentación de objeciones previas al cierre provisional en puntos frontera de clientes, o pre-objeciones, el operador del sistema publicará los formatos y calendarios dentro de la documentación aplicable al sistema de medidas eléctricas.

Desde la publicación del cierre provisional por parte del operador del sistema, se abrirá el plazo de objeción de medidas. Los plazos de objeción de medidas a partir de la publicación del cierre provisional son los que se indican en el apartado 8 de este procedimiento.

6.6.1 Objeción de medidas de puntos frontera de los que el operador del sistema es encargado de la lectura.

El operador del sistema recibirá las objeciones o emitirá sus auto - objeciones. Las objeciones de medidas de un punto frontera las podrá realizar cualquier participante del mismo. Las objeciones de medidas deberán ser notificadas al operador del sistema y resto de participantes.

Las objeciones en datos de medidas se clasifican en dos tipos:

a. Objeciones asociadas a datos de medida de energía en puntos frontera.

Adicionalmente y si aplica como complemento a la objeción, el participante podrá enviar al operador del sistema incidencias asociadas a la objeción según se indica en el apartado 3.4.

b. Objeciones relativas a datos estructurales o configuraciones de cálculo de puntos frontera.

Adicionalmente y si aplica como complemento a la objeción, el participante podrá enviar al operador del sistema las modificaciones de datos estructurales según lo indicado en el P.O. 10.7, en aplicación del apartado 3.4.

6.6.2 Objeción de medidas de puntos frontera o agregaciones de los que los distribuidores son encargados de la lectura.

Las objeciones en datos de medidas de puntos frontera o agregaciones de los que son encargados de la lectura los distribuidores se pueden clasificar en dos niveles:

a. Objeciones o auto-objeciones a la agregación.

b. Objeciones o auto-objeciones al valor mensual de un punto de suministro.

Asimismo, se clasifican en dos tipos en función del participante que las genera:

7. Objeciones emitidas por los comercializadores o consumidores directos a mercado o representantes.

a. Objeciones de fronteras de clientes tipos 1 y 2.

Estas objeciones se pondrán a disposición del operador del sistema.

b. Objeción a agregaciones de consumidores o productores de instalaciones de puntos frontera de generación de los que el distribuidor es encargado de lectura.

Estas objeciones se pondrán a disposición del operador del sistema.

Las objeciones se pueden realizar a nivel de punto frontera o a nivel de agregación. Toda objeción sobre una frontera individual debe llevar asociada una objeción sobre la agregación que la contiene.

Todas las objeciones, ya sean de punto frontera o de agregación, serán publicadas al concentrador principal de medidas, el cual realizará las publicaciones a los participantes implicados en la misma. En todo caso, es responsabilidad del emisor, y en ningún caso del operador del sistema, verificar que la objeción ha sido recibida en el concentrador principal, mientras que es responsabilidad del operador del sistema, y no del emisor, verificar que éstas han sido publicadas a los participantes implicados en el concentrador principal.

El operador del sistema sólo procesará y publicará las objeciones a los comercializadores, consumidores directos a mercado o representantes, mientras que el encargado de la lectura deberá procesar y responder todas las objeciones, tanto de puntos frontera como de agregaciones.

Si el motivo de la objeción del comercializador o consumidor directo a mercado o representante fuera que dispone de medida real o mejor medida que la del encargado de la lectura, éste deberá enviar al encargado de la lectura la curva del punto frontera. En estos casos el operador del sistema deberá remitir a la Comisión Nacional de los Mercados y la Competencia la información necesaria para que se inicien los procedimientos informativos y, en su caso, sancionadores por el incumplimiento de las obligaciones de lectura.

8. Objeciones emitidas por los propios encargados de la lectura (auto-objeciones).

a. Objeciones de fronteras de clientes tipos 1 y 2. Estas objeciones se pondrán a disposición del operador del sistema.

b. Objeción a agregaciones de consumidores tipos 3, 4 y 5 o instalaciones de puntos frontera de generación de los que el distribuidor es encargado de lectura.

Estas objeciones se pondrán a disposición del operador del sistema. Las objeciones de consumidores tipos 3, 4 y 5 e instalaciones de puntos frontera de generación de los que el distribuidor es encargado de lectura se pueden realizar a nivel de punto frontera o a nivel de agregación.

Todas las auto-objeciones, ya sean de punto frontera o de agregación, serán publicadas al operador del sistema mediante los formatos y medios de transmisión establecidos. El operador del sistema incorporará en su sistema las objeciones que pasen las validaciones requeridas y publicará el acuse de recibo de dichas objeciones a los participantes implicados en la misma (comercializador y distribuidor).

6.6.3 Resolución de objeciones.

1. Fronteras de las que el operador del sistema es encargado de la lectura.

El encargado de la lectura resolverá las objeciones recibidas en el plazo establecido en el apartado 8 de este procedimiento. Como resultado de una objeción el encargado de la lectura resolverá:

a. Medida revisada confirmada: medida del punto frontera que, tras el análisis del encargado de la lectura, no modifica su valor.

b. Medida revisada y modificada como resultado de la objeción: medida de punto frontera que, tras el análisis del encargado de la lectura, modifica su valor.

En ambos casos, el encargado de la lectura evaluará las objeciones emitidas y comunicará el resultado de las mismas a los participantes implicados durante la fase 1 del proceso de cierres descrita en el apartado 8 de este procedimiento.

2. Fronteras de las que los distribuidores son encargados de la lectura.

• Actuación del encargado de la lectura:

El encargado de la lectura responderá a todas las objeciones efectuadas por los comercializadores o consumidores directos a mercado o representantes en el plazo establecido en el apartado 8 de este procedimiento.

Independientemente de la obligación de contestar las objeciones a los comercializadores o consumidores directos a mercado o representantes anteriormente indicada, como consecuencia de la resolución de las mismas, el encargado de la lectura puede tener que generar y enviar al concentrador principal modificaciones de inventario y /o nuevos datos de medida.

Además, para los casos en que un comercializador o representante A presenta una objeción que afecta a otro comercializador o representante B, el cual no presenta objeción, si el encargado de lectura acepta la objeción deberá comunicar al concentrador principal y a los participantes implicados, en el periodo de resolución de objeciones y mediante el formato que se establezca, la identificación de los puntos o agregaciones del comercializador o representante B afectados por la objeción del comercializador o representante A.

• Actuación del operador del sistema:

El operador del sistema actuará de receptor de los datos remitidos por los encargados de la lectura consecuencia de la resolución de una objeción que les sean de aplicación, y realizará los tratamientos de medidas antes de la publicación del cierre definitivo de acuerdo con lo indicado a continuación:

a. Modificación de medidas o datos estructurales de clientes tipos 1 y 2.

El operador del sistema modificará sólo datos de medidas o datos estructurales de clientes tipos 1 y 2 si existe una auto-objeción del encargado de la lectura o una objeción de comercializador o consumidor directo a mercado o representantes aceptada por el propio encargado de la lectura. En función del tipo de objeción de que se trate, el operador del sistema deberá recibir información adicional para modificar los datos de medidas.

Si la información enviada en los plazos establecidos por el encargado de la lectura es incoherente o incompleta no se modificarán las medidas de clientes tipos 1 y 2 por parte del operador del sistema, comunicando el motivo de la no aceptación.

b. Modificación de medidas o datos estructurales de agregaciones.

El operador del sistema modificará sólo datos de medidas o datos estructurales de agregaciones si existe una auto-objeción del encargado de la lectura o una objeción del comercializador o de los consumidores directos a mercado o del representante aceptada por el propio encargado de la lectura. En función del tipo de objeción de que se trate, el operador del sistema deberá recibir información adicional para modificar los datos de medidas.

Si la información recibida por el operador del sistema es incoherente o incompleta, el operador del sistema no modificará las medidas en la publicación del cierre definitivo, comunicando el motivo de la no aceptación.

6.7 Cierre de energía definitivo.

Las medidas del cierre provisional que no hayan sido objetadas en los plazos anteriormente indicados pasarán a considerarse como firmes definitivas de acuerdo con lo establecido en el Real Decreto 1110/2007, de 24 de agosto.

Las medidas objetadas podrán cambiar su valor de acuerdo con lo indicado en el apartado 6. A partir de la resolución de las objeciones de datos de medidas, el operador del sistema comenzará a realizar los tratamientos de medidas necesarios a fin de realizar el cierre definitivo y su publicación.

Las medidas en cierre definitivo sólo podrán ser modificadas en los casos contemplados por el artículo 15 del Reglamento unificado de puntos de medida.

El operador del sistema publicará a los distintos participantes por los medios y formatos establecidos en el P.O. 10.4 los datos de medida en cierre definitivo de los que son partícipes.

Excepcionalmente, el operador del sistema podrá realizar republicaciones del cierre definitivo efectuados como consecuencia de reclamaciones recibidas a través del sistema de liquidaciones. Las republicaciones se harán públicas a los participantes afectados y tras su conformidad, se publicarán de nuevo al sistema de liquidaciones.

Como consecuencia de toda la información recibida tras el proceso de resolución de objeciones, se inicia un proceso previo al cierre definitivo por el cual, en las fases y los plazos indicados en el apartado 8 de este procedimiento, se publican nuevamente a los participantes las medidas, en los casos de no conformidad, y se solicita a los encargados de la lectura una revisión de la resolución de las objeciones. Una vez concluido este proceso, el operador del sistema publicará los datos definitivos de medidas al sistema de liquidaciones y a los participantes del sistema de medidas.

Una vez concluido este proceso, el operador del sistema publicará los datos definitivos de medidas al sistema de liquidaciones y a los participantes del sistema de medidas.

6.8 Corrección de registros de medida posterior al cierre definitivo y/o cierre excepcional.

La corrección de registros de medidas posterior a la publicación de los cierres definitivos de medidas según lo dispuesto en el artículo 15 del Real Decreto 1110/2007, de 24 de agosto, modificado según la disposición final tercera del Real Decreto 1623/2011, de 14 de noviembre, se realizará conforme a lo indicado en los siguientes apartados.

6.8.1 Solicitud a un encargado de lectura de una corrección de registros de medida.

La solicitud de corrección de registros de medida tiene por objeto solicitar al encargado de la lectura la revisión de los datos de medida como consecuencia de errores de medidas tras la publicación del cierre definitivo y/o excepcional.

La solicitud de corrección de registros de medida tiene por objeto reclamar al encargado de la lectura de un punto frontera o agregación de fronteras la revisión y corrección, si procede, de sus datos de medida tras la publicación del cierre definitivo y/o excepcional, en los supuestos indicados en el apartado 2 del artículo 15 del Real Decreto 1110/2007, de 24 de agosto.

Podrán solicitar corrección de registros de medida los participantes 1 y 2 y los representantes de fronteras de las que el operador del sistema es encargado de la lectura y los representantes / comercializadores / clientes directos a mercado / operador del sistema para el resto de fronteras y agregaciones.

La solicitud de corrección de datos de medidas se comunicará simultáneamente al encargado de la lectura y al operador del sistema en los plazos indicados en el apartado 8 de este documento, a partir de los ficheros y formatos que se publicarán en la versión vigente del documento ‘Ficheros para el Intercambio de Información de Medidas’ disponible en la página web de RED ELÉCTRICA DE ESPAÑA.

6.8.2 Comunicación de una corrección de medida por un encargado de lectura.

Adicionalmente, será de aplicación la corrección de registros a los casos en que el encargado de lectura detecte un error de medidas tras la publicación del cierre definitivo y/o excepcional, en los supuestos indicados en el apartado 3 del artículo 15 del Real Decreto 1110/2007, de 24 de agosto.

La corrección de registros de medida por un encargado de lectura se pondrá a disposición de los representantes / comercializadores / clientes directos a mercado y del operador del sistema en los plazos indicados en el apartado 8 de este documento.

6.8.3 Validación y resolución por parte del encargado de lectura.

Los encargados de la lectura analizarán las solicitudes de corrección recibidas. Para que una solicitud de corrección sea aceptada, el encargado de la lectura comprobará que se ajusta a los supuestos recogidos en el artículo 15 del Real Decreto 1110/2007, de 24 de agosto.

Los encargados de la lectura analizarán las solicitudes de corrección recibidas y resolverán las mismas en los plazos indicados en el apartado 8 de este documento. Los encargados de la lectura podrán requerir información adicional a los solicitantes a fin de resolver las solicitudes de revisión de medidas. Tras la revisión, el encargado de lectura concluirá como:

• Medida revisada y confirmada:

• Medida del punto frontera y/o agregación que tras el análisis del encargado de la lectura no modifica su valor.

• Medida revisada y modificada:

• Medida del punto frontera y/o agregación que tras el análisis del encargado de la lectura modifica su valor.

El encargado de la lectura pondrá en conocimiento de los participantes afectados y del operador del sistema la revisión de las solicitudes y la conclusión del análisis (medidas confirmadas o medidas modificadas), en los plazos indicados en el apartado 8 de este documento, a partir de los ficheros y formatos que se publicarán en la versión vigente del documento ‘Ficheros para el Intercambio de Información de Medidas’ disponible en la página web de RED ELÉCTRICA DE ESPAÑA.

6.8.4 Publicación de datos de medidas corregidas.

El encargado de la lectura publicará a los participantes afectados, al operador del sistema y al sujeto responsable de efectuar la liquidación (según se establece en el apartado 1 del artículo 15 del Real Decreto 1110/2007, de 24 de agosto), los nuevos datos de medidas horarias por punto frontera o por agregación en los plazos indicados en el apartado 8 de este procedimiento, a partir de los ficheros y formatos que se publicarán en la versión vigente del documento ‘Ficheros para el Intercambio de Información de Medidas’ disponible en la página web de RED ELÉCTRICA DE ESPAÑA..

6.9 Publicación al sistema de medidas de «restos» de energía facturada de meses en cierre definitivo.

Una vez publicado el nuevo cierre de medidas de un mes M tras las correcciones por aplicación del artículo 15 del Real Decreto 1110/2007, de 24 de agosto, el encargado de lectura comunicará al concentrador principal las modificaciones de energía consecuencia de nuevas facturaciones del peaje de acceso (refacturaciones, complementarias o regularizadoras) correspondientes al mes M efectuadas con posterioridad al cierre definitivo de medidas y que no hayan sido tenidas en cuenta en la aplicación del artículo 15 del Real Decreto 1110/2007, de 24 de agosto.

Para ello, se comunicará a través de un fichero específico la energía incremental (positiva o negativa) respecto a la publicada en el cierre definitivo tras la aplicación del artículo 15 del Real Decreto 1110/2007, de 24 de agosto («restos» de energía facturada de meses en cierre definitivo).

6.10 Cierres extraordinarios.

Además de los cierres provisional, definitivo y excepcional descritos en este apartado 6, podrá ser necesaria la realización de cierres extraordinarios de acuerdo con lo indicado en este apartado.

En situaciones de sujetos de mercado que queden suspendidos temporal o definitivamente del mercado de producción, y a solicitud del sistema de liquidaciones del operador del sistema, los plazos de envío de datos de medidas, cierre provisional y plazo de presentación de objeciones podrán reducirse a fin de acelerar el cierre definitivo de los puntos frontera de un sujeto del mercado de acuerdo con el procedimiento extraordinario que el operador del sistema establezca.

7. Comprobación de los procesos de lectura, alta o modificación de fronteras y tratamiento e intercambios de información.

A petición del Ministerio de Industria, Energía y Turismo o de la Comisión Nacional de los Mercados y la Competencia, el operador del sistema efectuará una comprobación de los procesos de lectura o alta, baja o modificación de fronteras o el tratamiento e intercambios de la información de los datos de las fronteras y periodos solicitados.

Como resultado de la solicitud, el operador del sistema emitirá informe sobre el cumplimiento de los requisitos del Reglamento Unificado de Puntos de Medida de los procesos y fronteras solicitados.

En función del alcance del proceso de comprobación solicitado, el operador del sistema podrá utilizar una muestra de fronteras y periodos para la realización de la comprobación solicitada.

En función del alcance del proceso de comprobación solicitado, el operador del sistema solicitará a los distribuidores, para fronteras de las que el operador del sistema no es encargado de la lectura, la información requerida en función de la comprobación o tipos de puntos a comprobar. Los encargados de la lectura remitirán los datos solicitados por las vías y formatos que establezca el operador del sistema antes de 30 días desde su solicitud.

Para realizar comprobaciones de puntos frontera tipos 1, 2 y tipo 3 distintos de clientes, el operador del sistema utilizará los datos de medidas disponibles en el concentrador principal.

El operador del sistema podrá, si lo estima conveniente para la elaboración de este informe, inspeccionar in situ las instalaciones de medida afectadas (o una muestra de las mismas).

El informe de la comprobación efectuado se enviará al Ministerio de Industria, Energía y Turismo o de la Comisión Nacional de los Mercados y la Competencia, según sea el peticionario, en el plazo de un mes desde que el operador del sistema disponga de la información completa sobre los datos anteriores.

8. Plazo del Sistema de Medidas.

8.1 Recepción de medidas.

Los plazos de recepción de medidas y puesta a disposición del concentrador principal y del resto de participantes (en los casos en que aplique) se detallan en la siguiente tabla:

| Tipo de punto frontera | Concentrador de medidas que efectúa la lectura del registrador | Plazo obligatorio para la lectura del registrador | Plazo obligatorio de publicación de medidas al concentrador principal | Plazo obligatorio de publicación de medidas al comercializador, representante o consumidor directo a mercado(nota 4) | Fin plazo de recepción de medidas por parte del concentrador principal |
| --- | --- | --- | --- | --- | --- |
| Tipos 1 y 2 distintos de clientes Tipo 3 distintos de clientes y distintos de instalaciones de generación de las que el distribuidor es encargado de lectura | Concentrador principal | Día D debe leerse antes de las 8:00 h del día D + 1 (Nota 3) | No aplica | No aplica | (Nota 5) |
| Tipos 1 y 2 distintos de clientes | Concentrador Secundario propiedad diferente que el encargado de lectura | Día D debe leerse antes de las 8:00 h del día D + 1 (Nota 3) | Día D debe publicarse antes de las 8:00 h del día D + 1 | No aplica | (Nota 5) |
| Tipo 3 distintos de clientes y distintos de instalaciones de generación de las que el distribuidor es encargado de lectura | Concentrador Secundario propiedad diferente que el encargado de lectura | Mes M debe leerse antes de las 8:00 h del 3.er día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | No aplica | (Nota 5) |
| Tipo 3 de instalaciones de generación de las que el distribuidor es encargado de lectura | Concentrador Secundario propiedad del encargado de lectura | Mes M debe leerse antes de las 8:00 h del 3.er día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 (Nota 2) | (Nota 5) |
| Tipo 5 de instalaciones de generación de las que el distribuidor es encargado de lectura | Concentrador Secundario propiedad del encargado de lectura | Mes M debe leerse antes de las 8:00 h del 3.er día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | (Nota 5) |
| Tipo 1 de clientes | Concentrador Secundario propiedad del encargado de lectura | Día D debe leerse antes de las 8:00 h del día D + 1 (Nota 3) | Día D debe publicarse antes de las 8:00 h del día D + 1 | Día D debe publicarse antes de las 8:00 h del día D + 1 | (Nota 5) |
| Tipo 2 de clientes | Concentrador Secundario propiedad del encargado de lectura | Mes M debe leerse antes de las 8:00 h del 3.er día hábil del mes M + 1 (Nota 3) | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 1 | (Nota 5) |
| Tipo 3 de clientes | Concentrador Secundario propiedad del encargado de lectura | Mes M debe leerse, al menos, antes de las 8:00 h del 3.er día natural del mes M + 3 (Nota 7) | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 3 (Nota 1) | Mes M debe publicarse antes de las 8:00 h del 5.º día hábil del mes M + 3 (Nota 2) | (Nota 5) |
| Tipo 4 y 5 de clientes | Concentrador Secundario propiedad del encargado de lectura | Mes M debe leerse, al menos, antes de las 8:00 h del 15.º día natural del mes M+3 (Nota 7) | Mes M debe publicarse antes de las 8:00 h del 15.º día natural del mes M+3 (Nota 1) | Mes M debe publicarse antes de las 8:00 h del 15.º día natural del mes M + 3 (Nota 2) | (Nota 5) |

Nota 1: Medidas agregadas.

Nota 2: Medidas agregadas y datos acumulados mensuales por punto de frontera. En el caso de instalaciones de puntos frontera de generación de los que el distribuidor es encargado de lectura, también medidas horarias.

Nota 3: Además de las comunicaciones remotas necesarias con los registradores de medidas para dar cumplimiento a lo indicado anteriormente, el encargado de la lectura realizará al menos los reintentos para recuperar medidas pendientes que se indican a continuación:

Puntos tipo 1 y 2:

Se realizará al menos una comunicación remota semanal con los registradores de medidas hasta el primer día hábil del mes M+3 a fin de recuperar medidas pendientes correspondientes al mes M.

Puntos tipo 3:

Se realizarán al menos tres comunicaciones remotas con los registradores de medidas en días distintos para recuperar medidas pendientes del mes M antes del primer día hábil del mes M+3.

Nota 4: La información de los datos acumulados mensuales de fronteras tipos 3, 4 y 5 deberá ser puesta a disposición de los participantes una vez se realice el cierre provisional, con un retraso inferior a veinticuatro horas.

Las comunicaciones de altas, bajas y cambios de comercializador y/o representante deberán realizarse antes de cumplirse cinco días hábiles desde su fecha efectiva.

El resto de datos estructurales y/o de medidas no incluidos en los párrafos anteriores, así como las medidas en punto de medida cuando se requiera, serán puestos a disposición de sus participantes con un retraso inferior a veinticuatro horas desde su cálculo u obtención por parte del encargado de la lectura.

Nota 5: El plazo de finalización de recepción de medidas para un cierre podrá tener distintas fechas en función del tipo de frontera.

El plazo de recepción de medidas como consecuencia del tratamiento de incidencias finaliza 30 días antes del cierre provisional de medidas.

Con objeto de disponer de datos de medidas adicionales para la validación y estimación de medidas, el concentrador del encargado de la lectura podrá comunicar y recibir datos de medidas de registrador correspondientes a saldos de energía de puntos de medida.

Con objeto de disponer de datos de medidas adicionales para la validación y estimación de medidas, los concentradores secundarios deberán enviar al concentrador principal saldos de energía diarios y/o mensuales de los puntos de medida de los que el operador del sistema es encargado de la lectura. El envío de dichos saldos de energía se realizará según los plazos de recepción de medidas del tipo de frontera.

Los envíos de medidas posteriores al cierre de recepción de medidas podrán ser tenidos en consideración por los encargados de la lectura dentro del procedimiento de resolución de objeciones.

Independientemente de los plazos de recepción de medidas establecidos y en situaciones de sujetos de mercado que queden suspendidos temporal o definitivamente del mercado de producción o por otra cualquier causa análoga, y previa solicitud del operador del sistema a los encargados de la lectura con notificación simultánea a la CNMC y Ministerio de Industria, Energía y Turismo, los plazos de envío de datos de medidas podrán reducirse a fin de acelerar el cierre definitivo de un sujeto de acuerdo con el procedimiento excepcional que el operador del sistema establezca.

La remisión de una mejor medida al operador del sistema por parte del Encargado de la lectura se podrá realizar hasta las 8:00 del 11.º día hábil del mes M+7, es decir, hasta el cierre provisional.

Nota 7: La periodicidad de las lecturas será la establecida en la normativa de aplicación.

8.2 Cálculo del mejor valor de punto frontera.

El cálculo del mejor valor de energía de cada punto frontera se realizará, mientras no se haya realizado el cierre definitivo de medidas, de acuerdo con los plazos obligatorios de recepción de medidas que se indican en el apartado 8. Adicionalmente, se realizará como consecuencia del procedimiento de resolución de incidencias y objeciones.

8.3 Cálculo de agregaciones.

El cálculo de agregaciones y su puesta a disposición del operador del sistema y del resto de participantes se realizará de acuerdo con los plazos obligatorios de recepción de medidas que se indican en el apartado 8. Adicionalmente, se realizará como consecuencia del procedimiento de resolución de incidencias y objeciones.

8.4 Publicaciones al sistema de liquidaciones.

El concentrador principal publicará los datos de medidas al sistema de liquidaciones para su liquidación, al menos con la siguiente periodicidad:

| Periodo de publicación | Tipo de publicación | Plazo de recepción de medidas en el concentrador principal para tenerse en cuenta en la publicación |
| --- | --- | --- |
| Diariamente. | Medidas del mes M de puntos frontera de generación e internacionales que sean firmes o provisionales por causas no imputables al responsable del punto. | Recibidas hasta las 8:00 h. |
| Diariamente, entre el 2.º día natural y el 5.º día hábil de cada mes. | Medidas del mes M–1 de puntos frontera de generación e internacionales que sean firmes o provisionales por causas no imputables al responsable del punto. Medidas de puntos frontera de clientes con medidas del mes M–1. | Recibidas hasta las 8:00 h del 5.º día hábil. |
| Semanalmente. | Medidas de puntos frontera de clientes con medidas del mes M y M–2. | Recibidas hasta las 8:00 h del último día hábil de la semana anterior. |
| Mensualmente, el 1er día hábil de cada mes. | Medidas del mes M–3 de puntos frontera de generación e internacionales que sean firmes o provisionales por causas no imputables al responsable del punto o estimaciones consecuencia de la resolución de incidencias en las que se disponga de medida válida del saldo total de energía del mes M–3. Medidas de puntos frontera de clientes con medidas del mes M–3. | Recibidas hasta las 8:00 h del penúltimo día hábil del mes anterior. |
| Mensualmente, el primer día hábil posterior al día 15 natural de cada mes. | Medidas de puntos frontera de clientes con medidas y del mes M–3. | Recibidas hasta las 8:00 h del 5.º día hábil del mes (para medidas de puntos de medida tipo 1, 2 y 3) y hasta las 8:00 h del 15.º día natural del mes (para puntos de medida tipo 4 y 5). |
| Mensualmente, el penúltimo día hábil de cada mes. | Medidas del cierre provisional del mes M–7. | Recibidas hasta las 8:00 h del 11.º día hábil del mes M–7. |
| Mensualmente. | Medidas del cierre definitivo y excepcional (según apartado 8). | Recibidas hasta fin del plazo de solicitud de revisión de la resolución de las objeciones (ver apartado 8). |

8.5 Publicaciones a los participantes.

El operador del sistema realizará, al menos, las siguientes publicaciones de datos estructurales y medidas previas a cada liquidación:

| Periodo de publicación | Encargado de lectura del tipo de punto frontera que se publica | Tipo de publicación |
| --- | --- | --- |
| Diariamente. | Operador del sistema. | Datos completos del mes M Datos completos del mes M–1 (entre el 1er día natural y el 5.º día hábil del mes M+1). |
| Diariamente. | Distribuidor. | Datos completos del mes M–1 (entre el 1er día natural y el 5.º día hábil del mes M+1). |
| Semanalmente, a partir del 6.º día hábil del mes. | Distribuidor. | Datos completos del mes M y M–2. |
| Semanalmente, a partir del 6.º día hábil del mes. | Operador del sistema. | Datos completos del mes M–2. |
| Semanalmente, a partir del 6.º día hábil del mes. | Distribuidor. | Datos estructurales y acumulados mensuales de los meses M–4, M–5, M–6 y M–7. |
| Mensualmente, el 1.er día hábil de cada mes. | Operador del sistema / distribuidor. | Datos completos del mes M–3 (excepto clientes). |
| Mensualmente, el 1.er día hábil posterior al día 15 de cada mes. | Distribuidor. | Datos completos del mes M–3 (clientes). |
| Mensualmente, el penúltimo día hábil de cada mes. | Operador del sistema / distribuidor. | Datos completos del cierre provisional del mes M–7. |
| Mensualmente (según apartado 8). | Operador del sistema / distribuidor. | Datos completos del cierre definitivo según apartado 8. |

8.6 Incidencias.

8.6.1 Recepción de incidencias.

El plazo de recepción de incidencias de un punto de medida finalizará 30 días antes del cierre provisional de medidas.

8.6.2 Resolución de incidencias.

Los plazos para la revisión y resolución de incidencias por parte del encargado de lectura dependerán de la fecha de recepción de la incidencia y de su tipología, de acuerdo con lo indicado a continuación:

a. Incidencias en instalaciones de las que el operador del sistema es el encargado de la lectura:

i. Incidencias recibidas hasta el primer día hábil del mes siguiente (mes M+1) al que corresponde la incidencia.

Serán revisadas antes del quinto día hábil del mes M+1 siempre que correspondan a:

1. Comunicación de modificaciones en datos estructurales.

2. Incidencia o avería solucionada que impedía la comunicación de datos de medidas.

3. Grupo de generación parado con producción cero o instalación desconectada con intercambio cero.

4. Incidencia o avería solucionada en equipos que no requiera estimaciones de medidas.

ii. Incidencias recibidas hasta el primer día hábil del segundo mes siguiente (mes M+2) al que corresponde la incidencia.

Serán revisadas antes del primer día hábil del tercer mes siguiente (M+3) siempre que correspondan a:

1. Comunicación de modificaciones en datos estructurales.

2. Incidencia o avería solucionada que impedía la comunicación de datos de medidas.

3. Grupo de generación parado con producción cero o instalación desconectada con intercambio cero.

4. Incidencia o avería solucionada en equipos que no requiera estimaciones de medidas.

5. Incidencia en la que se disponga de medida válida del saldo total de energía del intervalo de períodos afectados por la incidencia, según se indica en el punto a) del apartado 4.4.1.

iii. Incidencias recibidas hasta el límite de recepción de incidencias indicado en el apartado anterior.

El resto de incidencias que por el plazo de comunicación o tipología no hayan sido resueltas en los plazos anteriormente indicados, serán resueltas antes del cierre provisional de medidas.

b. Incidencias de instalaciones de generación de las que el distribuidor es el encargado de lectura:

▪ El plazo de emisión de incidencias y su resolución por parte del encargado de la lectura (distribuidor) se inicia el día 1 del tercer mes siguiente (mes M+3) al que corresponden las medidas y finaliza el primer día hábil del sexto mes al que corresponden las medidas (mes M+6).

▪ El distribuidor deberá actualizar los datos de la agregación que se pudiesen ver afectados como resultados de la resolución de las incidencias y enviar los nuevos datos agregados al operador del sistema antes del segundo día hábil del séptimo mes al que corresponden las medidas (mes M+7).

c. Incidencias en instalaciones de clientes: se resolverán hasta 30 días antes del cierre provisional de medidas.

8.7 Cierre del mes M+1

El distribuidor pondrá a disposición del concentrador principal antes de las ocho horas del quinto día hábil del mes siguiente (mes M+1) los datos estructurales y las medidas de los puntos frontera de clientes tipo 1 y 2.

El distribuidor pondrá a disposición del concentrador principal antes de las ocho horas del quinto día hábil del mes siguiente (mes M+1) los datos estructurales y las medidas de las agregaciones de puntos frontera de generación tipo 3 y 5 de las que el distribuidor es el encargado de lectura.

El operador del sistema realizará las publicaciones de los datos de medidas del cierre M+1 a los participantes, así como al Sistema de Liquidaciones para su liquidación, el quinto día hábil del mes M+1.

El distribuidor pondrá a disposición del concentrador principal antes de las ocho horas del tercer día hábil del mes siguiente (mes M+1) los datos estructurales de los puntos frontera de clientes tipo 5.

El concentrador principal publicará a los comercializadores antes de las diez horas del cuarto día hábil del mes siguiente (M+1) los datos estructurales de los puntos frontera de clientes tipo 5.

8.8 Cierre M+3.

El distribuidor pondrá a disposición del concentrador principal antes de las ocho horas del día 15 natural del mes M+3 los datos estructurales de las agregaciones de puntos frontera de clientes tipo 3, 4 y 5 y de sus medidas horarias asociadas, así como el acumulado mensual de cada uno de los clientes de la agregación.

Asimismo, deberá poner a disposición del concentrador principal antes de las ocho horas del día 15 natural del mes M+3 las medidas horarias individualizadas de los puntos frontera de clientes tipo 5 con curva de carga horaria.

El operador del sistema realizará las publicaciones de los datos de medidas del cierre M+3 a los participantes, así como al Sistema de Liquidaciones para su liquidación, el primer día hábil posterior al día 15 natural del mes M+3.

8.9 Cierre provisional.

El cierre provisional de medidas correspondiente al mes M se publicará a los participantes y al sistema de liquidaciones no más tarde del penúltimo día hábil del séptimo mes posterior a las medidas (mes M+7).

Coincidiendo con la publicación del cierre provisional, y en un plazo no superior a 24 horas, los distintos encargados de la lectura pondrán a disposición de los distintos representantes/comercializadores/consumidores directos a mercado el desglose de puntos frontera individualizados que componen cada agregación enviada al operador del sistema por los medios y formatos establecidos en los procedimientos de operación 10.4 y 10.11.

8.10 Objeciones.

8.10.1 Presentación de objeciones.

Los plazos de objeción de medidas tras el cierre provisional son los siguientes:

a. Veinticinco días hábiles para cualquier participante de puntos frontera de los que el operador del sistema es encargado de la lectura.

b. Diez días hábiles para auto – objeciones de los encargados de la lectura. Dentro de este plazo los encargados de lectura deberán enviar al operador del sistema los datos estructurales y de medidas necesarios para su resolución. Al día siguiente de la finalización de este plazo, el operador del sistema realizará una publicación de medidas de las que el distribuidor es encargado de lectura previa al inicio del plazo de presentación de objeciones que se establece en el siguiente apartado para comercializadores, clientes directos a mercado o representantes de medida.

c. Quince días hábiles para los comercializadores, clientes directos a mercado o representantes de medidas que correspondan a puntos frontera de los que el distribuidor es encargado de lectura. Este plazo se iniciará el día siguiente de la publicación indicada en el apartado anterior, es decir, a partir del duodécimo día hábil posterior a la publicación del cierre provisional.

Para aquellos puntos de los que el distribuidor es encargado de la lectura, el operador del sistema recibirá los datos de las objeciones y los publicará diariamente a todos los participantes de los puntos hasta el fin del plazo de recepción indicado anteriormente. En todo caso, es responsabilidad del emisor, y en ningún caso del operador del sistema, verificar que la objeción ha sido recibida y publicada a los participantes implicados en el concentrador principal.

8.10.2 Resolución de objeciones.

Los encargados de la lectura resolverán las objeciones recibidas en un plazo de quince días hábiles desde el cierre del plazo de emisión de objeciones. Para el caso de puntos de los que el distribuidor es encargado de la lectura, los distribuidores deberán enviar al operador del sistema dentro de este plazo los datos estructurales y de medidas necesarios para la resolución de las objeciones que resulten aceptadas por éstos.

Para aquellos puntos de los que el distribuidor es encargado de la lectura, el operador del sistema recibirá las respuestas a las objeciones y las publicará diariamente a todos los participantes de los puntos hasta el fin del plazo de resolución indicado anteriormente. En todo caso, es responsabilidad del emisor, y en ningún caso del operador del sistema, verificar que la objeción ha sido recibida y publicada a los participantes implicados en el concentrador principal.

8.11 Cierre definitivo.

El proceso previo al cierre definitivo consta de cuatro o seis fases, dependiendo de que el encargado de la lectura sea el operador del sistema o el distribuidor respectivamente. Dichas fases se desarrollan en los plazos que se detallan a continuación.

8.11.1 Fronteras de las que el operador del sistema es encargado de la lectura.

• Fase 1:

El operador del sistema publicará las medidas a los participantes el segundo día hábil posterior al cierre del plazo de resolución de objeciones indicado en el apartado 8.11.

• Fase 2:

Los participantes tendrán seis días hábiles para solicitar al operador del sistema la revisión de la resolución de las objeciones, acompañado, si aplica, de los datos estructurales o de medidas necesarios.

La solicitud de revisión debe referirse exclusivamente a objeciones recibidas en el plazo establecido en el apartado 8.11. Por tanto, no serán admitidas nuevas objeciones en esta fase.

• Fase 3:

El operador del sistema revisará las solicitudes de revisión de la fase anterior y publicará el sexto día hábil posterior al cierre del plazo de solicitud de revisión los datos de medidas en los que se incluirán las modificaciones que procedan en esta fase. Tras la citada publicación no se admitirán modificaciones de medidas salvo que, de forma excepcional, el operador del sistema considere que dichas modificaciones no comprometen el cumplimento de la fecha de publicación del cierre definitivo y, además, sean solicitadas por un participante con el acuerdo expreso del otro participante y con el visto bueno del operador del sistema como encargado de la lectura. En cualquier caso, las posibles modificaciones no darán lugar a nuevas publicaciones a los participantes antes del cierre definitivo de medidas, si bien estarán disponibles para su consulta según las condiciones de acceso establecidas por el operador del sistema. Estas modificaciones excepcionales serán comunicadas a la Comisión Nacional de los Mercados y la Competencia.

• Fase 4:

Una vez cumplidos los plazos anteriores, el operador del sistema publicará los datos del cierre definitivo a los participantes y, simultáneamente, al sistema de liquidaciones, antes del tercer día hábil del mes M+11. Todas las medidas del mes en cierre definitivo serán consideradas medidas firmes.

8.11.2 Fronteras de las que los distribuidores son encargados de la lectura.

• Fase 1:

El operador del sistema, publicará las medidas a los encargados de la lectura el segundo día hábil posterior al cierre del plazo de resolución de objeciones indicado en el apartado 8.11.

• Fase 2:

Los encargados de la lectura dispondrán de los cinco días hábiles siguientes a la publicación de la fase 1 para identificar y comunicar al concentrador principal los datos estructurales y de medida necesarios para resolver los posibles errores detectados tras dicha publicación.

Únicamente se admitirán modificaciones sobre datos por errores del encargado de la lectura o del operador del sistema en la resolución de las objeciones recibidas en el plazo establecido en el apartado 8.11. Por tanto, no serán admitidas nuevas objeciones en esta fase.

• Fase 3:

El operador del sistema publicará las medidas a los comercializadores o consumidores directos a mercado y representantes con las posibles modificaciones como consecuencia de la fase 2, el sexto día hábil posterior a la publicación a encargados de la lectura.

• Fase 4:

Los comercializadores o consumidores directos a mercado y representantes dispondrán de seis días hábiles para solicitar al encargado de la lectura la revisión de la resolución de las objeciones.

En ningún caso serán admitidas nuevas objeciones en esta fase.

• Fase 5:

Los encargados de la lectura, en los tres días hábiles siguientes a la finalización del plazo indicado en la fase 4, deberán enviar los datos estructurales y de medidas necesarios para modificar las solicitudes de revisión que resulten aceptadas por éstos.

El siguiente día hábil, el operador del sistema publicará las medidas actualizadas a todos los participantes. Tras esta publicación no se admitirán modificaciones de medidas salvo que, de forma excepcional, el operador del sistema considere que dichas modificaciones no comprometen el cumplimiento de la fecha de publicación del cierre definitivo y, además, sean solicitadas por el encargado de la lectura con el acuerdo expreso del otro participante o viceversa. En cualquier caso, las posibles modificaciones no darán lugar a nuevas publicaciones a los participantes antes del cierre definitivo de medidas, si bien estarán disponibles para su consulta según las condiciones de acceso establecidas por el operador del sistema. Estas modificaciones excepcionales serán comunicadas a la Comisión Nacional de los Mercados y la Competencia.

• Fase 6:

Una vez cumplidos los plazos anteriores, el operador del sistema publicará los datos del cierre definitivo a los participantes y, simultáneamente, al sistema de liquidaciones, antes del tercer día hábil del mes M+11. Todas las medidas del mes en cierre definitivo serán consideradas medidas firmes.

8.11.3 Resumen de plazos tras el cierre provisional de medidas.

En las siguientes tablas se presentan, a modo de resumen, los plazos de los distintos hitos entre el cierre provisional y el cierre definitivo de medidas:

| Hito | Puntos frontera de los que el operador del sistema es encargado de lectura |
| --- | --- |
| 1. Presentación de objeciones. | Durante 25 días hábiles. |
| 2. Resolución de objeciones. | Durante 15 días hábiles. |
| 3. Publicación de la resolución de objeciones. | 2.º día hábil posterior. |
| 4. Solicitud de revisión de resolución de objeciones. | Durante 6 días hábiles. |
| 5. Publicación de la revisión de resolución de objeciones. | 6.º día hábil posterior. |
| 6. Publicación cierre definitivo. | Antes del 3.er día hábil del mes M+11. |
| Hito | Puntos frontera de los que el distribuidor es encargado de lectura |
| --- | --- |
| 1. Presentación de auto - objeciones. | Durante 10 días hábiles. |
| 2. Presentación de objeciones. | Durante 15 días hábiles. |
| 3. Resolución de objeciones por parte de los encargados de lectura. | Durante 15 días hábiles. |
| 4. Publicación de la resolución de objeciones a encargados de lectura. | 2.º día hábil posterior. |
| 5. Revisión de los encargados de lectura de la publicación tras resolución de objeciones. | Durante 5 días hábiles. |
| 6. Publicación de la resolución de objeciones a comercializadores o clientes directos a mercado y representantes. | 1.er día hábil posterior. |
| 7. Solicitud de revisión de resolución de objeciones. | Durante 6 días hábiles. |
| 8. Revisión de resolución de objeciones por parte de los encargados de lectura. | Durante 3 días hábiles. |
| 9. Publicación de la revisión de resolución de objeciones. | 1.er día hábil posterior. |
| 10. Publicación cierre definitivo. | Antes del 3.er día hábil del mes M+11. |

8.12 Plazos para la aplicación del proceso de corrección de medidas con posterioridad al cierre definitivo.

Los plazos para la aplicación del proceso de corrección de registros tras la publicación de un cierre definitivo y/o excepcional de medidas se indican en la siguiente tabla:

| Hito | Plazo |
| --- | --- |
| 1. Solicitud a un encargado de lectura de una corrección de registros de medida. | Durante 120 días desde la publicación del cierre definitivo y/o excepcional de medidas. |
| 2. Comunicación de una corrección de registros de medida por un encargado de lectura. | Durante 120 días desde la publicación del cierre definitivo y/o excepcional de medidas. |
| 3. Validación y resolución por parte del encargado de lectura. | Durante 20 días hábiles desde el cierre del plazo indicado en los hitos 1 y 2. |
| 4. Publicación por parte del encargado de lectura de la revisión de solicitudes. | 1.er día hábil posterior. |
| 5. Publicación por parte del encargado de lectura de los datos de medida corregidos. | 10.º día hábil posterior. |

8.13 Publicación al sistema de medidas de «restos» de energía facturada de periodos en cierre definitivo.

Los encargados de lectura remitirán al operador del sistema las modificaciones de energías facturadas en cada mes que correspondan a periodos en cierre definitivo antes del décimo día hábil de cada mes.

9. Días hábiles y calendario de cierre.

El operador del sistema pondrá a disposición de los participantes del sistema de medidas, antes del inicio de cada año natural, el calendario de cierres provisionales y definitivos con indicación de los días límite para presentación y resolución de objeciones así como los días inhábiles que no sean sábados ni domingos.

A efectos de los procedimientos de medidas serán días inhábiles: los sábados, los domingos, los festivos en la plaza de Madrid, el 24 de diciembre, el 31 de diciembre, y los que, hasta un máximo de dos días anuales, determine el operador del sistema.
