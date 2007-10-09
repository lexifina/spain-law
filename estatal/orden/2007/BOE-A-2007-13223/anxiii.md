## ANEXO XIII

## PRESENTACIÓN CENTRALIZADA INGRESOS ENTIDADES COLABORADORAS: ESPECIFICACIONES TÉCNICAS. VALIDACIONES

ERROR GRAVE

Del que se pueda deducir que la transmisión tiene algún error que cuestione la fiabilidad de todo su contenido.

La corrección la efectúa la Entidad colaboradora.

ERROR LEVE

Error no grave que debe ser corregido.

La corrección la efectúa la A.E.A.T. (en cada Delegación). Puede deberse a errores de cumplimentación.

Se requiere el justificante de ingreso para confirmar que es un error de cumplimentación.

RECHAZO DE LA TRANSMISIÓN

• Cuando exista un error grave o más.

* Cuando el número de errores leves sea tal que se pueda deducir un error sistemático por parte de la Entidad colaboradora.

– 100 Errores en valor absoluto

– 1% de errores sobre el total en valor relativo

* Por descuadre con la orden de transferencia.

| TIPO DE REGISTRO 1 (ENTIDAD TRANSMISORA) |  |
| --- | --- |
| Tipo de registro distinto de 1 o A | GRAVE |
| Código de Entidad Transmisora no es un código válido | GRAVE |
| Tipo de presentación distinto de I | GRAVE |
| Tipo de ingresos distinto de A, E, L, T , Z o G | GRAVE |
| Número de quincena no se ajusta al formato AAAAMM01 o AAAAMM02. | GRAVE |
| Siendo AAAA el ejercicio y MM el mes. |  |
| Código Delegación de presentación distinto de 57 | GRAVE |
| TIPO DE REGISTRO 2 (ENTIDAD COLABORADORA) |  |
| Tipo de registro distinto de 2 | GRAVE |
| Código de Entidad Colaboradora no es un código válido | GRAVE |
| No coincide el código de Entidad con el de la orden de transferencia | GRAVE |
| Tipo de presentación distinto de I | GRAVE |
| Tipo de ingresos distinto de A, E, L, T, Z o G | GRAVE |
| Número de quincena no se ajusta al formato AAAAMM01 o AAAAMM02. Siendo AAAA el ejercicio y MM el mes. | GRAVE |
| Número de quincena no coincide con el de la Entidad Transmisora | GRAVE |
| Código Delegación de presentación distinto de 57 | GRAVE |
| Número de orden de la transmisión sin que conste una transmisión con número anterior | GRAVE |
| TIPO DE REGISTRO 3 (REGISTRO DE DETALLE) |  |
| (Autoliquidaciones excepto Especiales) |  |
| Tipo de registro distinto de 3 | GRAVE |
| Número de secuencia con saltos en la numeración | GRAVE |
| Ejercicio no válido (Sin iniciar el período de devengo) | LEVE |
| Período no válido (Distinto a 1T, 2T, 3T 4T,1P ,2P, 3P o OA, o cuyo período de devengo aún no se hubiera iniciado) | LEVE |
| El período no se corresponde a la periodicidad de presentación del modelo. | LEVE |
| Modelo de autoliquidación distinto a los autorizados | GRAVE |
| No se corresponde con el grupo subtotal en que se presenta | GRAVE |
| Número de justificante Más de 10 números de justificante ficticios No se cumple rutina c/control | GRAVE |
| Configuración del NIF no existente o con dígito de control erróneo | LEVE |
| Anagrama o comienzo del apellido: Inexistencia en personas físicas | LEVE |
| No se cumple rutina c/control o no coincide con los cuatro primeros caracteres del apellido | LEVE |
| Código de sucursal del ingreso desconocida | GRAVE |
| Importe del ingreso = 0 | GRAVE |
| Fecha de ingreso ilógica | LEVE |
| Dato específico no capturado cuando sea exigido | LEVE |
| TIPO DE REGISTRO 3 (REGISTRO DE DETALLE) |  |
| (Autoliquidaciones Especiales) |  |
| Tipo de registro distinto de 3 | GRAVE |
| Número de secuencia con saltos en la numeración | GRAVE |
| Ejercicio no válido (Sin iniciar el período de devengo) | LEVE |
| Período no válido | LEVE |
| Modelo de autoliquidación: |  |
| – Distinto a los autorizados | LEVE |
| – No se corresponde con el grupo-subtotal en que se presenta | GRAVE |
| Número de justificante: |  |
| – Más de 10 números de justificante ficticios | GRAVE |
| – No se cumple rutina c/control | GRAVE |
| Configuración del NIF no existente o con dígito de control erróneo | LEVE |
| Anagrama: |  |
| – Inexistencia en personas físicas | LEVE |
| – No se cumple rutina c/control o no coincide con los cuatro primeros caracteres del apellido | LEVE |
| Código de sucursal del ingreso desconocida | GRAVE |
| Importe del ingreso = 0 | GRAVE |
| Fecha de ingreso ilógica | GRAVE |
| Dato específico no capturado cuando sea exigido | LEVE |
| TIPO DE REGISTRO 3 (REGISTRO DE DETALLE) |  |
| (Liquidaciones) |  |
| Tipo de registro distinto de 3 | GRAVE |
| Número de secuencia con saltos en la numeración | GRAVE |
| Código de modelo distinto a 002, 003, 004 ,008, 010, 012, 031, 032, 060, 061 o 069 | GRAVE |
| Clave de justificante |  |
| – No se ajusta a la configuración definida para cada código de modelo | GRAVE |

Modelo 002 Clave de justificante (13 posiciones)

Posiciones 1-2: Delegación (01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: Valores permitidos:

00 a 12 y 28

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 003 Clave de justificante (13 posiciones)

Posiciones 1-2: Delegación (01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: Siempre "20">Posiciones 5-6: Siempre "20"

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 004 Clave de justificante (13 posiciones)

Posiciones 1-2 Delegación (01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: 70 y 71

Posiciones 7-12: Numérico

Posición 13: Dígito de control

Modelo 008 Clave de justificante (13 posiciones)

Posiciones 1-2:Delegación (01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: 22, 25 y 27

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 010 Clave de justificante (13 posiciones)

Posiciones 1-2:Delegación (01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: “13 a 19”, “22”,“25”, “27” y del “60” al “65

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 012 Clave de justificante (13 posiciones)

Posiciones 1-2: Delegación(01 a 56)

Posiciones 3-4: Numérico

Posiciones 5-6: Siempre "12">Posiciones 5-6: Siempre "12"

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 031 Clave de justificante (13 posiciones)

Posiciones 1-2: Delegación (01 a 99)

Posiciones 3-4: Numérico

Posiciones 5-6: «50, 51 y 59»

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 032 Clave de justificante (13 posiciones)

Posiciones 1-2: Delegación (91 ó 92)

Posiciones 3-4: Numérico

Posiciones 5-6: "52 y 58">Posiciones 5-6: "52 y 58"

Posiciones 7-12: Numérico

Posición 13: Carácter de control

Modelo 060 Clave de justificante (13 posiciones)

Posiciones 1-12: Numérico

Posición 13: Carácter de control

Modelo 061 Clave de justificante (13 posiciones)

Posiciones 1-12: Numérico

Posición 13: Carácter de control

Modelo 069 Clave de justificante (13 posiciones)

Posiciones 1-12: Numérico

Posición 13: Carácter de control

| Justificante no cumple rutina carácter de control | GRAVE |
| --- | --- |
| Justificante no reconocido por el sistema (excepto modelos 060, 061 y 069) | LEVE |
| Fecha de ingreso ilógica | GRAVE |
| Importe del ingreso |  |
| – Igual a cero | GRAVE |
| – Distinto al que figura en el justificante de los modelos 002, 004, 010, 012, 031, 032, 060, 061 y 069 | LEVE |
| Código de sucursal del ingreso desconocida | GRAVE |
| Código de NIF no existe o con dígito de control erróneo | LEVE |

TIPO DE REGISTRO 3 (REGISTRO DE DETALLE)

(Tasas)

Cualquier error de los descritos se considerará error grave y provocará rechazo de la transmisión:

– Tipo de registro distinto de 3

– Número de secuencia con saltos en la numeración

– Código de Tasa no es uno de los permitidos para el tipo de ingreso

– Número de justificante:

– No cumple dígito de control

– Las posiciones 1 a 3 son distintas, de 790, 791, 990 ó 991

– Las posiciones 4 a 6 no se corresponde con los tres últimos dígitos de un código de tasa permitido.

– N.I.F.: Configuración de NIF no existente o con dígito de control erróneo.

– Apellidos y nombre sin contenido en registros con DNI (sin carácter de control)

– Importe = 0

– Fecha de ingreso ilógica.

– Código de sucursal del ingreso desconocida.

TIPO DE REGISTRO 3 (REGISTRO DE DETALLE)

(Anulaciones de NRC’s)

Cualquier error de los descritos se considerará error grave y provocará rechazo de la transmisión:

– Tipo de registro distinto de 3

– Número de secuencia con saltos en la numeración

– NRC sin contenido

– N.I.F.: Configuración de NIF no existente o con carácter de control erróneo.

– Tipo diferente de I.

– Ejercicio no numérico.

– Importe = 0

– Fecha de ingreso ilógica.

– Fecha de anulación ilógica o menor que la de operación.

– Código de sucursal del ingreso desconocida.

| TIPO DE REGISTRO 4 (SUBTOTALES) |  |
| --- | --- |
| (Autoliquidaciones y Autoliquidaciones Especiales) |  |
| Tipo de registro distinto de 4 | GRAVE |
| Número de secuencia con saltos en la numeración | GRAVE |
| Código de modelo de autoliquidación distinto a los autorizados | GRAVE |
| Contador de registros por modelo no cuadra | GRAVE |
| Suma de importes por modelos no cuadra | GRAVE |
| TIPO DE REGISTRO 5 (TOTALES) |  |
| (Autoliquidaciones y Autoliquidaciones Especiales) |  |
| Tipo de registro distinto de 5 | GRAVE |
| Número de registros con saltos en la numeración | GRAVE |
| Contador de registros tipo 4 no cuadra | GRAVE |
| Contador total de registros no cuadra (Internamente, con los registros de subtotales o externamente con la orden de transferencia) | GRAVE |
| Suma de importes no cuadra | GRAVE |
| Código de Entidad Colaboradora es distinta a la del registro tipo 02 | GRAVE |
| TIPO DE REGISTRO 5 (TOTALES) |  |
| (Liquidaciones) |  |
| Tipo de registro distinto de 5 | GRAVE |
| Número de registros con saltos en la numeración | GRAVE |
| Contador total de registros no cuadra (Internamente, con los registros de subtotales o externamente con la orden de transferencia) | GRAVE |
| Suma de importes no cuadra | GRAVE |
| Código de Entidad Colaboradora es distinta a la del registro tipo 02 | GRAVE |
| TIPO DE REGISTRO 6 (TOTALES) |  |
| Tipo de registro distinto de 6 | GRAVE |
| Código de Entidad Transmisora es distinta a la del registro tipo 01 | GRAVE |
| Contador total del número de Entidades Colaboradoras no cuadra | GRAVE |
| Número total de registros no coincide con los recibidos en la transmisión | GRAVE |
