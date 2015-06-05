## P.O. 10.13. Procedimiento por el que los distribuidores intercambian información con los comercializadores de energía eléctrica, y ponen a disposición de los comercializadores y los consumidores los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión

1. Objeto.

El objeto del presente procedimiento es:

a) Definir los ficheros de intercambios de determinada información que deben ser utilizados por los distribuidores y comercializadores de energía eléctrica para los suministros que dispongan de equipos de medida tipo 5.

b) Regular el proceso de intercambio de la información relativa a los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión, entre los distribuidores, como sujetos encargados de la lectura, y los comercializadores y consumidores, a efectos de facturación de la energía.

En el procedimiento se establecen las obligaciones relativas a la información, tanto de las medidas horarias que puedan servir, en su caso, para la facturación de la energía de los consumidores, como de las mejores medidas horarias validadas disponibles en cada momento, los formatos y plazos en que dicha información debe ser remitida, así como determinados aspectos sobre la seguridad y confidencialidad con los que se realizarán los intercambios de dicha información entre los agentes.

El presente procedimiento tiene en cuenta lo dispuesto en el P.O. 10.12 «Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión».

2. Ámbito de aplicación.

1. Este procedimiento es de aplicación a los sujetos siguientes:

– distribuidores de energía eléctrica con respecto a los suministros conectados a sus redes que dispongan de equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión;

– comercializadores de referencia respecto a los consumidores que tengan contratado el Precio Voluntario para el Pequeño Consumidor y dispongan de equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión;

– comercializadores de energía eléctrica que utilicen los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión para la facturación a los consumidores.

La información referente a los datos procedentes de los equipos de medida de los consumidores a los que el procedimiento resulte de aplicación deberá ser intercambiada de acuerdo a lo en él descrito.

2. Los ficheros de intercambio de información definidos en el apartado 3.1.a) son de aplicación a los distribuidores y comercializadores respecto a todos los suministros que dispongan de equipos de medida tipo 5.

3. En caso de que el consumidor contrate directamente el peaje de acceso con el distribuidor y compre la energía a través de un comercializador, el comercializador accederá a la información de medida del consumidor regulada en este procedimiento y tanto el consumidor, como el comercializador, utilizarán los ficheros de intercambio que le sean de aplicación.

3. Procedimientos de intercambio de información entre el distribuidor y el comercializador.

3.1 Ficheros de intercambio de información.

a) Se definen los siguientes ficheros que serán utilizados por los distribuidores y comercializadores para intercambiar información:

• Fichero A3: Alta de un punto de suministro. Fichero de intercambio de información entre el distribuidor y el comercializador para dar de alta un nuevo punto de suministro.

• Fichero B1: Baja o Suspensión de suministro. Fichero de intercambio de información entre el comercializador y el distribuidor para solicitar la baja o suspensión de un punto de suministro.

• Fichero C1: Cambio de comercializador sin modificaciones en el contrato de peaje de acceso. Fichero de intercambio de información entre el comercializador entrante, el distribuidor y el comercializador saliente a efectos de efectuar un cambio de comercializador para un punto de suministro sin cambios que afecten al contrato de acceso.

• Fichero C2: Cambio de comercializador con modificaciones en el contrato de peaje de acceso. Fichero de intercambio de información entre el comercializador entrante, el distribuidor y el comercializador saliente a efectos de efectuar un cambio de comercializador para un punto de suministro con cambios que afecten al contrato de acceso.

• Fichero D1: Notificación de cambios. Fichero de intercambio de información entre el distribuidor y el comercializador para la notificación de cambios que afecten al punto de suministro.

• Fichero M: Modificación en el contrato de peaje de acceso. Fichero de intercambio de información entre el comercializador con contrato vigente y el distribuidor para solicitar modificaciones que afecten a los parámetros de contratación de peaje de acceso.

• Fichero F1: Facturación de peajes de acceso y otros conceptos regulados. Fichero de intercambio de información entre el distribuidor y el comercializador para la facturación de peajes de acceso y en su caso, otros conceptos regulados, de los consumidores. Este fichero se emite para un determinado CUPS el día en que se factura el peaje de acceso.

• Fichero Q1: Saldos y lecturas de consumidores con peaje directo. Fichero de intercambio de información entre el distribuidor y el comercializador para que el distribuidor de energía eléctrica aporte al comercializador el saldo de las lecturas de energía de aquellos consumidores que han contratado el peaje de acceso directamente con el distribuidor. Este fichero será opcional en el caso de que el peaje de acceso sea contratado a través del comercializador.

• Fichero R1: Reclamaciones. Fichero de intercambio de información entre el distribuidor y el comercializador a efectos de reclamaciones de los consumidores.

• Fichero W1: Autolecturas. Fichero de intercambio de información entre el distribuidor y el comercializador a efectos de comunicaciones de autolecturas aportadas por los consumidores.

b) En relación a los formatos de ficheros de intercambio de información de las curvas de carga horaria definidas en el Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión, se utilizarán los siguientes ficheros, cuyos formatos se establecen en el anexo del presente procedimiento:

• Fichero F5D: Fichero que incluye las curvas de carga horaria CCH_FACT, de todos los suministros de un comercializador cuyo peaje de acceso ha sido facturado ese mismo día. Se emite para todos los CUPS cuyo fichero F1 correspondiente se ha emitido ese día.

• Fichero P5D: Fichero que incluye las curvas de carga horaria CCH_VAL de los suministros de un comercializador que el distribuidor ha validado ese mismo día.

• Fichero CCH-CONS: Fichero con la curva de carga horaria que coincidirá con la CCH_FACT entre una fecha inicial y una fecha final, que se pone a disposición de un consumidor.

• Fichero RF5D: Fichero que incluye la nueva curva de carga horaria emitida tras una reclamación interpuesta por el comercialización que no haya dado lugar a una modificación del saldo ATR.

3.2 Comunicación del distribuidor al comercializador sobre el estado de los equipos de medida de los consumidores conectados a sus redes.

El distribuidor utilizará el campo de «MotivoCambioATRDesdeDistribuidora» del fichero D1, para indicar al comercializador que un punto de suministro se ha integrado efectivamente en el sistema de telegestión o que estando telemedido no opera todavía con curva de carga horaria.

Adicionalmente, se indicará en el campo «TipodeTelegestion» de los formatos de fichero C1, C2, A3 y M1 si el punto de suministro está integrado efectivamente en el sistema de telegestión o si estando telemedido no opera todavía con curva de carga horaria.

En caso de haber indicado erróneamente que un equipo de medida se encuentra efectivamente integrado en el sistema de telegestión, el distribuidor deberá comunicarlo al comercializador a través del fichero D1.

3.3 Puesta a disposición del distribuidor al comercializador de la CCH_FACT.

3.3.1 Puesta a disposición de la CCH_FACT.

a) Una vez que se notifique al comercializador a través del fichero D1 con la información indicada en el apartado 3.2 de la efectiva integración de un equipo de medida en el sistema de telegestión, la facturación del peaje de acceso del periodo correspondiente a los consumos registrados a partir de la primera lectura que se efectúe con posterioridad al envío del fichero D1, deberá implicar la puesta a disposición simultánea de la curva de carga horaria CCH_FACT del periodo facturado.

b) En el fichero F1 utilizado para la facturación del peaje de acceso se utilizará el campo «IndicativoCurvadeCarga» para indicar que el suministro está efectivamente integrado en el sistema de telegestión, y se utilizarán los campos «FechaDesdeCCH» y «FechaHastaCCH» para indicar la fecha de inicio y de fin, respectivamente, del periodo de facturación al que corresponde la CCH, atendiendo al criterio establecido en la normativa vigente.

Del mismo modo, en el fichero F5D se recogerán los registros de la curva de carga horaria CCH_FACT, según el formato recogido en el anexo.

c) El total de energía para cada periodo tarifario del peaje de acceso que corresponda al que se refiera la facturación del suministro, debe coincidir con el total resultante de la suma de los registros de la curva de carga horaria CCH_FACT para dicho periodo. La diferencia en valor absoluto de más de 1 kWh en alguno de los periodos tarifarios entre la energía facturada del correspondiente peaje de acceso y la energía resultante de sumar las medidas horarias correspondientes a dicho periodo tarifario, será motivo por el que el comercializador podrá reclamar la factura asociada a dicha energía del distribuidor.

3.3.2 Canales y protocolos de comunicación.

Cada distribuidor o agrupación de distribuidores en el caso de asociaciones, habilitará un servidor FTP para la puesta a disposición de otros sujetos de los ficheros establecidos. Dicho servidor será el mismo que se utilice para la puesta a disposición de la información que se utilice, en su caso, a efectos de facturación de energía eléctrica, para consumidores con punto de medida de tipo 1, 2 y 3.

El acceso al servidor del distribuidor se realizará mediante el protocolo SFTP sobre SSH (Secure Shell).

El servidor incluirá un proceso de borrado de ficheros con antigüedad nunca inferior a veinticuatro meses.

En el servidor habilitado por cada distribuidor se habilitará una carpeta para cada comercializador identificada por su código de agente en el SIMEL.

Dentro de esta carpeta de agente, se habilitará una subcarpeta denominada 01_Salida_FACT donde el distribuidor pondrá a disposición la información relativa a la curva CCH_FACT. Esta carpeta será la misma que se utilice para la puesta a disposición del comercializador de la información que se utilice, en su caso, a efectos de facturación de energía, para los consumidores que dispongan de equipos de medida tipo 1,2 y 3.

3.3.3 Plazos para la puesta a disposición de la CCH_FACT.

El distribuidor pondrá a disposición antes del 5.º día hábil incluido posterior a la fecha final del periodo de facturación, la CCH_FACT correspondiente a dicho periodo de facturación, de forma simultánea al envío del fichero de facturación de peajes.

El cambio de comercializador en los consumidores cuyo equipo esté efectivamente integrado en el sistema de telegestión, se realizará con el resumen diario o lectura absoluta del día de cambio, a efectos tanto de facturación del peaje de acceso como de curva de carga horaria publicada a cada comercializador, garantizando la coherencia de ambos. En el caso de no disponer del resumen diario, se aplicará el procedimiento establecido en la Resolución de 30 de diciembre de 2002, de la Dirección General de Política Energética y Minas, por la que se establece el procedimiento de estimación de medida aplicable a los cambios de suministrador o norma que le sustituya.

Se mantendrá un histórico de la CCH_FACT de al menos 2 años.

3.3.4 Actualizaciones de la CCH_FACT.

La CCH_FACT puesta a disposición del comercializador en el plazo contemplado en el apartado 3.3.3 únicamente podrá ser objeto de modificación si se cumple alguno de los supuestos siguientes:

a) Como consecuencia de una reclamación por parte del consumidor, dentro de los plazos establecidos en la normativa vigente.

En el caso de que la reclamación cliente conlleve la modificación del saldo ATR, se emitirá un nuevo fichero F5D conforme a lo dispuesto en el párrafo 3.3.4.b).

El fichero RF5D definido en el apartado 3.1.b) se utilizará únicamente en el caso de que la reclamación cliente relativa a la curva de carga horaria, no haya dado lugar a una modificación del saldo ATR.

Los ficheros RF5D que recojan las nuevas curvas de medida horarias CCH_FACT consecuencia de la reclamación del consumidor incluirán en el campo de código de la factura de peaje de acceso la identificación de la factura de peaje de acceso original.

b) En caso de modificación de la factura del peaje de acceso por modificación del saldo ATR, definido en el Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

La modificación de la factura del peaje de acceso por modificación del saldo ATR conllevará la publicación de una nueva curva de carga horaria CCH_FACT y, por tanto, la emisión de una nueva factura al consumidor atendiendo a lo dispuesto en el presente apartado.

Las facturas que modifiquen el peaje de acceso previamente facturado podrán ser de tres tipos:

b.1) Factura complementaria: factura que complementa a otra ya emitida, que no se anula, tras detectarse una anomalía en el equipo de medida que impidió el correcto registro de energía.

El nuevo fichero F5D que se pondrá a disposición del comercializador contendrá las variaciones de la nueva curva de carga horaria con respecto a la curva inicial, indicando en el campo «métodos de obtención» el que se hubiera aplicado, de acuerdo al formato recogido en el anexo.

La suma de las energías horarias por periodo incluidas en el nuevo fichero F5D coincidirá con la energía de la nueva factura de peaje complementaria en cada periodo. La diferencia en valor absoluto de más de 1 kWh en alguno de los periodos tarifarios entre la energía facturada del correspondiente peaje de acceso y la energía resultante de sumar las medidas horarias correspondientes a dicho periodo tarifario, será motivo por el que el comercializador podrá reclamar la factura asociada a dicha energía del distribuidor.

b.2) Factura rectificadora: factura que anula a otra factura ya emitida que incluía valores estimados, motivada por la disposición de un mejor valor de la energía a facturar, para el mismo periodo de facturación.

Requiere la nueva publicación de la curva de carga horaria CCH_FACT que corresponda al nuevo consumo total facturado por periodo tarifario en el mismo periodo de facturación.

El nuevo fichero F5D a poner a disposición del comercializador incluirá la nueva curva de carga horaria CCH_FACT completa que afecta al periodo refacturado, indicando en el campo «método de obtención» el que se hubiera aplicado, de acuerdo al formato recogido en el anexo.

b.3) Factura regularizadora: factura que modifica una o varias facturas ya emitidas con anterioridad, que no se anulan, motivada por la disposición de un mejor valor de la energía a facturar o por un cambio de precios recogidos en la normativa.

La factura regularizadora incluirá los consumos de los periodos de facturación afectados. El nuevo fichero F5D a poner a disposición del comercializador incluirá la nueva curva de carga horaria completa CCH_FACT correspondiente a dichos periodos de facturación, indicando en el campo «método de obtención» el que se hubiera aplicado, de acuerdo al formato recogido en el anexo.

En este caso el sumatorio de las energías horarias debe coincidir con la suma de las energías de los saldos ATR para el conjunto de los periodos de facturación afectados, no siendo necesario que coincidan en cada periodo de facturación.

3.4 Puesta a disposición del distribuidor al comercializador de la CCH_VAL.

3.4.1 Canales y protocolos de comunicación.

En el servidor habilitado por cada distribuidor o asociación de distribuidores al que hace referencia el apartado 3.3.2, dentro de cada carpeta para un comercializador se habilitará una subcarpeta denominada 02_Salida_VAL en donde el distribuidor pondrá a disposición la información relativa a la curva CCH_VAL.

3.4.2 Plazos y actualizaciones.

La CCH_VAL de cada suministro efectivamente integrado en el sistema de telegestión deberá ser puesta a disposición del comercializador al menos con una periodicidad semanal por el distribuidor.

La información se actualizará de forma incremental. Mediante la publicación de la CCH_VAL el distribuidor pondrá a disposición del comercializador la información de los datos de medida de todas las horas y para todos los CUPS para los que tiene medida real más actualizada que la remitida, en su caso, en la anterior CCH_VAL.

El distribuidor pondrá a disposición del comercializador las actualizaciones de la CCH_VAL, hasta publicar la curva CCH_VAL que haya dado lugar a la CCH_FACT, no enviándose actualizaciones posteriores a la CCH_FACT, sin perjuicio de las actualizaciones a las que se hace referencia en el apartado 3.3.4.

3.5 Mecanismos de seguridad y confidencialidad en el acceso a la información.

Los ficheros F5D, P5D y RF5D tendrán carácter confidencial y serán accesibles únicamente por el comercializador con contrato vigente para el consumidor en el período temporal al que corresponde la información que contiene, salvo autorización expresa por parte del consumidor, sin coste alguno, para que puedan acceder a sus datos otros comercializadores. Para ello, el comercializador deberá acreditar su capacidad de representación ante el distribuidor.

En el caso en que el consumidor haya dado su autorización expresa para que accedan a sus datos de medida horaria otros comercializadores con los que no tenga contrato en vigor, dichos comercializadores podrán acceder gratuitamente a los datos del fichero CCH_CONS disponible en el portal web del distribuidor al que hace referencia el apartado 4 del presente procedimiento.

El encargado de recabar el consentimiento expreso del consumidor para que accedan a la información sobre los datos de curva de carga horaria otros comercializadores sin contrato en vigor con el consumidor, será el distribuidor.

El comercializador será plenamente responsable de garantizar la confidencialidad de la información sobre la curva de carga horaria de sus clientes y no podrá utilizarla para fines ajenos a su actividad como comercializador de energía eléctrica, sin perjuicio de las obligaciones de información impuestas por la normativa vigente en cada momento.

Dicha responsabilidad no podrá delegarse ni transferirse a terceros, sin perjuicio de que la gestión de la facturación de la energía pueda corresponder a otra entidad que no coincida jurídicamente con la titular. En estos supuestos, el comercializador habrá de establecer con dicha entidad los pactos que en cada caso se puedan requerir.

Cada sujeto dispondrá de un usuario y clave que garantice la seguridad de acceso a los datos y recursos autorizados y la confidencialidad de los mismos.

3.6 Estructura y Formatos.

La información relativa a la CCH_FACT y CCH_VAL será puesta a disposición del comercializador de acuerdo con los formatos de los ficheros F5D y P5D, respectivamente, establecidos en el anexo.

4. Puesta a disposición del distribuidor al consumidor de la curva de carga horaria.

4.1 Canales y protocolos de comunicación.

El distribuidor habilitará un portal web que permita la consulta por parte de los consumidores titulares de los puntos de suministro conectados a su red de distribución de su curva de carga horaria facturada (CCH-FACT).

4.2 Estructura y Formatos.

El distribuidor habilitará la posibilidad de que la misma curva CCH_FACT puesta a disposición del comercializador se pueda descargar por parte del consumidor en formato de fichero plano CSV y Excel, de acuerdo con el formato establecido en el anexo para el fichero CCH-CONS, acompañado de una gráfico que represente los datos de medida horaria del consumidor para el periodo de facturación al que corresponde la CCH_FACT y permita la integración entre fechas incluidas en dicho periodo. En todo caso, el gráfico permitirá la visualización de la energía consumida en cada una de las horas incluidas entre dos fechas comprendidas dentro del periodo de facturación seleccionadas por el consumidor.

El comercializador informará al consumidor en la factura de la posibilidad de acceder gratuitamente a los datos de la medida horaria que hayan servido para la facturación a través de su distribuidor.

Asimismo, los consumidores podrán tener acceso al fichero CCH_CONS solicitándolo a través de los canales de atención del distribuidor.

4.3 Plazos y actualizaciones.

El distribuidor pondrá a disposición del consumidor la curva CCH_FACT en el mismo plazo establecido para la puesta a disposición de dicha curva al comercializador definido en el apartado 3.3.3 del presente procedimiento.

El distribuidor no mostrará actualizaciones posteriores para un punto de suministro una vez que se disponga de la CCH_FACT correspondiente, sin perjuicio de lo dispuesto en el apartado 3.3.4 relativo a las actualizaciones de la misma. Una vez que la CCH_FACT esté disponible, ésta será la única curva de carga horaria accesible por el consumidor.

El distribuidor deberá mantener a disposición del consumidor un histórico mínimo de 24 meses de la CCH_FACT.

4.4 Confidencialidad de la información.

La información relativa a las medidas horarias tendrá carácter confidencial y será accesible mediante un sistema de claves únicamente por el consumidor titular del contrato de suministro durante el período temporal al que corresponda dicha información, sin perjuicio de lo establecido en el apartado 3.5 del presente procedimiento para dar acceso a la curva de carga horaria de un consumidor a comercializadores con los que el consumidor no tenga un contrato en vigor, y sin perjuicio de las obligaciones de información impuestas por la normativa vigente en cada momento.

El consumidor deberá darse de alta en el sistema para tener acceso a esta información.

Los distribuidores no podrán ceder dicha información a terceros ni utilizarla para fines distintos a los de su propia actividad de distribución de energía eléctrica.
