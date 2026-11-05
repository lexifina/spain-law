## ANEJO 2

## Registro detalle de los depósitos recibidos

El archivo tendrá las siguientes características generales:

• Archivo de texto con caracteres ASCII imprimibles (desde el ASCII 32 hasta el ASCII 126, ambos inclusive). No se permiten caracteres ASCII extendido, salvo en los campos en los que se indique expresamente.

• Caracteres admitidos: letras minúsculas y mayúsculas, números, signos «+» y «-». Se podrán utilizar caracteres especiales cuando se indique expresamente en cada uno de los campos.

• Para cada cuenta o depósito, incluidos los fondos procedentes de situaciones transitorias por operaciones de tráfico conforme a lo señalado en el artículo 4.1 del Real Decreto 2606/1996 y los procedentes de los saldos mantenidos por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo abiertas en la entidad o sucursal adscrita al FGD declarante, a nombre de la empresa de servicios de inversión por cuenta de sus clientes, según lo establecido en el artículo 30 quáter del Real Decreto 217/2008 (en adelante, “depósitos”), se incluirá un registro por titular y depósito, con las siguientes excepciones:

– En caso de tratarse de depósitos multidivisa, se informará un registro por titular, depósito y divisa.

– En caso de tratarse de depósitos que cuenten con imposiciones con diferentes fechas de vencimiento, se informará un registro por titular, depósito y fecha de vencimiento de la imposición.

– En el caso de los saldos mantenidos por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo abiertas en la entidad o sucursal adscrita al FGD, a nombre de la empresa de servicios de inversión por cuenta de sus clientes cuyos depósitos no estén excluidos de la cobertura del FGD en virtud de apartado 4 del artículo 4 del Real Decreto 2606/1996, se incluirá un registro individualizado para cada uno de estos clientes con su correspondiente saldo.

En consecuencia, debe existir un único registro por “Tipo de documento de identificación” (campo 1), “Número del documento de identificación” (campo 2), “Fecha de vencimiento” (campo 14) y “Código del depósito registrado en España o en sucursal de otro país de la UE” (campo 15). Estos campos conforman la clave única del registro.

• En el registro se incluirán los depósitos y los fondos de las sociedades no financieras, los hogares y las Administraciones Locales con un presupuesto anual igual o inferior a 500.000 euros, con independencia de que los depósitos y fondos sean admisibles o no para su cobertura por el FGD. También se incluirán los saldos mantenidos por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo abiertas en la entidad o sucursal adscrita al FGD a nombre de la empresa de servicios de inversión por cuenta de sus clientes cuyos depósitos no estén excluidos de la cobertura del FGD en virtud del apartado 4 del artículo 4 del Real Decreto 2606/1996, debidamente individualizados para cada uno de ellos.

> Téngase en cuenta que esta última actualización de los puntos tercero y cuarto, establecida por la norma única.d) de la Circular 2/2021, de 28 de enero. Ref. BOE-A-2021-1475, entra en vigor el 30 de junio de 2021, según determina su disposición final única.

> Redacción anterior:

> "• Para cada cuenta o depósito, incluidos los fondos procedentes de situaciones transitorias por operaciones de tráfico (en adelante, «depósitos»), se incluirá un registro por titular y depósito, con las siguientes excepciones:

> ○ En el caso de tratarse de depósitos multidivisa, se informará un registro por titular, depósito y divisa.

> ○ En el caso de tratarse de depósitos que cuenten con imposiciones con diferentes fechas de vencimiento, se informará un registro por titular, depósito y fecha de vencimiento de la imposición.

> En consecuencia, debe existir un único registro por “Tipo de documento de identificación” (campo 1), “Número del documento de identificación” (campo 2), “Fecha de vencimiento” (campo 14) y “Código del depósito registrado en España o en sucursal de otro país de la UE” (campo 15). Estos campos conforman la clave única del registro."

> • En el registro se incluirán los depósitos y los fondos de las sociedades no financieras, los hogares y las Administraciones Locales con un presupuesto anual igual o inferior a 500.000 euros, con independencia de que los depósitos y fondos sean admisibles o no para su cobertura por el FGD."

• Contenido del campo “Importe”: en los depósitos con varios titulares, su importe se dividirá entre los titulares, de acuerdo con lo previsto en el contrato de depósito, y, en su defecto, a partes iguales, conforme a lo establecido en el artículo 7 del Real Decreto 2606/1996.

• Los campos con formato “Numérico” se completarán con ceros (“0”) a la izquierda. Los campos con formato “Alfanumérico” se completarán con espacios a la derecha, excepto los campos en los que se indique otra cosa.

Descripción.

Campo 1. Tipo de documento de identificación.

• Formato: Alfanumérico.

• Longitud: 3.

• Contenido: “DNI”, “NIF”, “NIE”, “PAS” (pasaporte) u “OTR” (otros) del titular del depósito.

Campo 2. Número del documento de identificación.

• Formato: Alfanumérico.

• Longitud: 30.

• Contenido: Código numérico o alfanumérico del documento de identificación señalado en el campo 1.

Campo 3. Nombre del titular.

• Formato: Alfanumérico.

• Longitud: 55.

• Contenido: Nombre del titular del depósito. En este campo podrán utilizarse caracteres especiales del ASCII extendido.

Campo 4. Dirección.

• Formato: Alfanumérico.

• Longitud: 110.

• Contenido: Domicilio del titular del depósito. En este campo podrán utilizarse caracteres especiales del ASCII extendido.

Campo 5. Población.

• Formato: Alfanumérico.

• Longitud: 50.

• Contenido: Población del domicilio del titular del depósito. En este campo podrán utilizarse caracteres especiales del ASCII extendido.

Campo 6. Provincia.

• Formato: Alfanumérico.

• Longitud: 20.

• Contenido: Provincia del domicilio del titular del depósito. En este campo podrán utilizarse caracteres especiales del ASCII extendido.

Campo 7. Distrito postal.

• Formato: Alfanumérico.

• Longitud: 8.

• Contenido: Distrito postal del domicilio del titular del depósito.

Campo 8. País.

• Formato: Alfanumérico.

• Longitud: 2.

• Contenido: Código ISO 3166 alfa-2 del país o territorio del domicilio del titular del depósito, compuesto por dos letras.

Campo 9. Código de país del número de teléfono.

• Formato: Alfanumérico.

• Longitud: 6.

• Contenido: Código de país del número de teléfono de contacto del depositante. La primera posición será siempre “+”. Este campo se rellenará cuando este dato se encuentre disponible. En caso contrario, se rellenará con 6 espacios en blanco.

Campo 10. Número de teléfono.

• Formato: Alfanumérico.

• Longitud: 15.

• Contenido: Teléfono de contacto del depositante, sin incluir el código de país del campo 9 anterior. Este campo se rellenará siempre que este dato se encuentre disponible. En caso contrario, se rellenará con 15 espacios en blanco.

Campo 11. Correo electrónico del titular.

– Formato: Alfanumérico.

– Longitud: 125.

– Contenido: Correo electrónico (e-mail) de contacto del depositante. El formato deberá cumplir con el estándar de Internet RFC-822. Este campo se rellenará siempre que el dato se encuentre disponible. En caso contrario, se rellenará con 125 espacios en blanco.

> Téngase en cuenta que esta última actualización del Campo 11, establecida por la norma única.d) de la Circular 2/2021, de 28 de enero. Ref. BOE-A-2021-1475, entra en vigor el 30 de junio de 2021, según determina su disposición final única.

> Redacción anterior:

> "Campo 11. Correo electrónico del titular.

> • Formato: Alfanumérico.

> • Longitud: 55.

> • Contenido: Correo electrónico (e-mail) de contacto del depositante. El formato deberá cumplir con el estándar de Internet RFC-822. Este campo se rellenará siempre que este dato se encuentre disponible. En caso contrario, se rellenará con 55 espacios en blanco."

Campo 12. Admisible.

• Formato: Alfanumérico.

• Longitud: 1.

• Contenido: Indica si el depósito es admisible para estar garantizado por el Fondo de Garantía de Depósitos (siempre “S” o “N”, sí o no, respectivamente).

Campo 13. Depósito en garantía.

• Formato: Alfanumérico.

• Longitud: 1.

• Contenido: Depósito pignorado o afecto en garantía de otras operaciones (siempre “S” o “N”, sí o no, respectivamente).

Campo 14. Fecha de vencimiento.

• Formato: Numérico.

• Longitud: 8.

• Contenido: Formato AAAAMMDD (solo se completará si el depósito tiene vencimiento; en caso contrario, se rellenará con ceros).

Campo 15. Código del depósito registrado en España o en una sucursal de otro país de la UE.

– Formato: Alfanumérico.

– Longitud: 39.

– Contenido: El campo se formará de la siguiente forma:

− Las dos primeras posiciones contendrán los caracteres “ES” para los depósitos registrados en España, o el código ISO 3166 alfa-2 del país donde esté radicada la sucursal para depósitos en otros países de la UE.

− Las tres siguientes posiciones contendrán el código ISO 4217 de la moneda del depósito.

− Las 34 posiciones restantes contendrán el código que la entidad o sucursal adscrita al FGD asigne al depósito. Este código será único para cada depósito mantenido por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo abiertas en la entidad o sucursal adscrita al FGD, a nombre de la empresa de servicios de inversión por cuenta de sus clientes. En consecuencia, el código será el mismo en cada uno de los registros individualizados correspondientes a los clientes de la empresa de servicios de inversión incluidos en dicho depósito.

Campo 16. Tipo de depósito.

– Formato: Numérico.

– Longitud: 3.

– Contenido: Código interno que la entidad o sucursal adscrita al FGD asigne al tipo de depósito de que se trate. A título de ejemplo, podrían asignarse los códigos del siguiente modo: cuentas de ahorro (001), cuentas corrientes (002), etc. Los saldos mantenidos en la entidad o sucursal adscrita al FGD, por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo por cuenta de sus clientes, deberán figurar identificados mediante un código propio.

Campo 17. Número total de titulares.

– Formato: Numérico.

– Longitud: 8.

– Contenido: Número total de titulares del depósito. Siempre será un número mayor de cero. En el caso de los saldos mantenidos en la entidad o sucursal adscrita al FGD, por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo por cuenta de sus clientes, figurará el número de clientes.

Campo 18. Número de titular.

– Formato: Numérico.

– Longitud: 8.

– Contenido: Número de orden que corresponde al titular en el número total de titulares del depósito.

Campo 19. Importe.

– Formato: Alfanumérico.

– Longitud: 15.

– Contenido: Importe principal o nominal más los intereses devengados en la fecha a la que se refieren los datos del depósito. En caso de que se trate de un depósito con más de un titular, el importe se incluirá en la parte correspondiente a cada titular. En el caso de los saldos mantenidos por empresas de servicios de inversión en cuentas instrumentales y transitorias de efectivo abiertas en la entidad o sucursal adscrita al FGD, a nombre de la empresa de servicios de inversión por cuenta de sus clientes cuyos depósitos no estén excluidos de la cobertura del FGD en virtud del apartado 4 del artículo 4 del Real Decreto 2606/1996, el importe incluirá el saldo correspondiente a cada cliente.

El importe se incluirá con un signo y dos decimales. La primera posición siempre será “−” si el saldo del depósito es negativo (descubiertos en cuenta corriente) y se cumplen las condiciones establecidas en el artículo 7.2 del Real Decreto 2606/1996, o “+” si es positivo. Las otras 14 posiciones se completarán con ceros a la izquierda y contendrán el importe, que deberá estar expresado en céntimos de euro, siendo los dos últimos dígitos los correspondientes a los decimales del importe, sin incluir en ningún caso el signo decimal “,”. Cuando el importe sea cero, la primera posición será “+” y las 14 posiciones siguientes serán ceros.

Los depósitos no denominados en euros se convertirán a euros:

– En caso de evento de pago, los depósitos se convertirán a euros aplicando el tipo de cambio del día en que se produzca alguno de los hechos citados en el artículo 8.1 del Real Decreto 2606/1996, o del día anterior hábil cuando fuese festivo.

– En el resto de los casos, se aplicará el tipo de cambio correspondiente a la fecha de referencia de los datos.

> Téngase en cuenta que esta última actualización de los Campos 15 a 19, establecida por la norma única.d) de la Circular 2/2021, de 28 de enero. Ref. BOE-A-2021-1475, entra en vigor el 30 de junio de 2021, según determina su disposición final única.

> Redacción anterior:

> "Campo 15. Código del depósito registrado en España o en una sucursal de otro país de la UE.

> • Formato: Alfanumérico.

> • Longitud: 39.

> • Contenido: El campo se formará de la siguiente forma:

> – Las primeras dos posiciones contendrán los caracteres “ES” para los depósitos registrados en España, o el código ISO 3166 alfa-2 del país donde esté radicada la sucursal para depósitos en otros países de la UE.

> – Las tres siguientes posiciones contendrán el código ISO 4217 de la moneda del depósito.

> – Las 34 posiciones restantes contendrán el código que la entidad asigne al depósito.

> Campo 16. Tipo de depósito.

> • Formato: Numérico.

> • Longitud: 3.

> • Contenido: Código interno que la entidad asigne al tipo de depósito de que se trate. A título de ejemplo, podrían asignarse los códigos del siguiente modo: cuentas de ahorro (001), cuentas corrientes (002), etc.

> Campo 17. Número total de titulares.

> • Formato: Numérico.

> • Longitud: 4.

> • Contenido: Número total de titulares del depósito. Siempre será un número mayor de cero.

> Campo 18. Número de titular.

> • Formato: Numérico.

> • Longitud: 4.

> • Contenido: Número de orden que le corresponde en el número total de titulares del depósito.

> Campo 19. Importe.

> • Formato: Alfanumérico.

> • Longitud: 15.

> • Contenido:

> Importe principal o nominal más los intereses devengados en la fecha a la que se refieren los datos del depósito. En el caso de que se trate de un depósito con más de un titular, el importe se incluirá en la parte correspondiente a cada titular.

> El importe se incluirá con un signo y dos decimales. La primera posición siempre será “-”, si el saldo es negativo, o “+”, si es positivo. Las otras catorce posiciones se completarán con ceros a la izquierda y contendrán el importe, que deberá estar expresado en céntimos de euro, siendo los dos últimos dígitos los correspondientes a los decimales del importe, sin incluir en ningún caso el signo decimal “,”. Cuando el importe sea cero, la primera posición será “+”, y las catorce posiciones siguientes serán ceros.

> Los depósitos no denominados en euros se convertirán a euros:

> – En caso de evento de pago, los depósitos se convertirán a euros aplicando el tipo de cambio del día en que se produzca alguno de los hechos citados en el artículo 8.1 del Real Decreto 2606/1996, o del día anterior hábil cuando fuese festivo.

> – En el resto de los casos, se aplicará el tipo de cambio correspondiente a la fecha de referencia de los datos."

Campo 20. Importe especialmente protegido.

• Formato: Alfanumérico.

• Longitud: 15.

• Contenido:

Cuantía que, estando incluida en el saldo positivo de la cuenta o depósito de que se trate, corresponda a importes especialmente protegidos, conforme se definen en la nota (i) del estado “Base para el cálculo de las aportaciones al Fondo de Garantía de Depósitos”. Por tanto, este importe será positivo e igual o menor que el saldo de la cuenta de que se trate consignado en el campo 19, “Importe”.

El importe se incluirá con un signo y dos decimales. La primera posición siempre será “+”. Las otras catorce posiciones se completarán con ceros a la izquierda y contendrán el importe, que deberá estar expresado en céntimos de euro, siendo los dos últimos dígitos los correspondientes a los decimales del importe, sin incluir en ningún caso el signo decimal (“,”).

Este campo solo se completará cuando existan depósitos especialmente protegidos. En caso contrario, la primera posición será “+”, y las catorce posiciones siguientes serán ceros.

Los depósitos no denominados en euros se convertirán a euros:

– En caso de evento de pago, los depósitos se convertirán a euros aplicando el tipo de cambio del día en que se produzca alguno de los hechos citados en el artículo 8.1 del Real Decreto 2606/1996, o del día anterior hábil cuando fuese festivo.

– En el resto de los casos, se aplicará el tipo de cambio correspondiente a la fecha de referencia de los datos.

Campo 21. Importe en divisa.

• Formato: Alfanumérico.

• Longitud: 15.

• Contenido:

Este campo solo se completará en el caso de que el depósito no esté denominado en euros.

El importe en divisa se incluirá con un signo y dos decimales. La primera posición será siempre “-”, si es negativo, o “+”, si es positivo. Las otras catorce posiciones se completarán con ceros a la izquierda y contendrán el importe, que deberá estar expresado en céntimos de divisa, siendo los dos últimos dígitos los correspondientes a los decimales del importe, sin incluir en ningún caso el signo decimal (“,”). Cuando el importe sea cero o no exista importe en divisa, la primera posición será “+”, y las catorce posiciones siguientes serán ceros.

Campo 22. Importe en divisa especialmente protegido.

• Formato: Alfanumérico.

• Longitud: 15.

• Contenido:

Cuantía que, estando incluida en el saldo positivo de la cuenta o depósito de que se trate, corresponda a importes no denominados en euros especialmente protegidos, conforme se definen en la nota (i) del estado “Base para el cálculo de las aportaciones al Fondo de Garantía de Depósitos”. Por tanto, este importe será positivo e igual o menor que el saldo de la cuenta de que se trate consignado en el campo 21, “Importe en divisa”.

El importe en divisa se incluirá con un signo y dos decimales. La primera posición será “-”, si es negativo, o “+”, si es positivo. Las otras catorce posiciones se completarán con ceros a la izquierda y contendrán el importe, que deberá estar expresado en céntimos de divisa, siendo los dos últimos dígitos los correspondientes a los decimales del importe, sin incluir en ningún caso el signo decimal (“,”).

Este campo solo se completará cuando existan depósitos en divisa especialmente protegidos. En caso contrario, la primera posición será “+”, y las catorce posiciones siguientes serán ceros.

Campo 23. Situación especial de pago.

• Formato: Alfanumérico.

• Longitud: 1.

• Contenido: Recoge alguna de las situaciones previstas en el artículo 9.1.a) del Real Decreto 2606/1996, por las que el pago del depósito podrá aplazarse, así como la situación recogida en el artículo 4.6, por la que podrá suspenderse el pago. Se rellenará con un número del 0 al 4, de acuerdo con las siguientes consideraciones:

– “1” si no existe certeza sobre derechos legales de cobro o cuando el depósito sea objeto de litigio.

– “2” si el depósito es objeto de sanciones que restringen las facultades de disposición.

– “3” si no se ha producido ninguna operación en relación con el depósito en los últimos 24 meses.

– “4” cuando el depositante, o cualquier otra persona con derecho o interés sobre el depósito, haya sido procesado, o se hubiera dictado apertura de juicio oral por delitos relacionados con operaciones de blanqueo de capitales, cuando se hubiera incoado el procedimiento abreviado que se regula en el título III del libro IV de la Ley de Enjuiciamiento Criminal y hasta tanto finalice el procedimiento.

– “0” para el resto de los casos.

A modo ilustrativo, se presentan a continuación unos ejemplos sobre cómo debería completarse el fichero en determinados casos. A estos efectos, únicamente se muestran los campos que configuran la clave única (campos 1, 2, 14 y 15), así como los campos 19 y 21. Ello no exime de la obligación de rellenar el resto de los campos del registro a los que se refiere este anejo 2.

Ejemplo 1. Una cuenta con un saldo total de 100.000 euros y cuyo importe se divide entre dos titulares a partes iguales.

| Tipo de documento de identificación | Número de documento de identificación | Fecha de vencimiento | Código del depósito | Importe en euros | Importe en divisa |
| --- | --- | --- | --- | --- | --- |
| Campo 1 | Campo 2 | Campo 14 | Campo 15 | Campo 19 | Campo 21 |
| NIF | 00000000A | 00000000 | ESEU990000000810123456111 | +000000005000000 |  |
| NIF | 11111111B | 00000000 | ESEU990000000810123456111 | +000000005000000 |  |

En total, dos registros en el archivo.

Ejemplo 2. Una cuenta multidivisa de un mismo titular con un saldo de 1.000 dólares y 1.000 libras esterlinas.

| Tipo de documento de identificación | Número de documento de identificación | Fecha de vencimiento | Código del depósito | Importe en euros | Importe en divisa |
| --- | --- | --- | --- | --- | --- |
| Campo 1 | Campo 2 | Campo 14 | Campo 15 | Campo 19 | Campo 21 |
| NIF | 22222222C | 00000000 | ESGBP990000000810123456222 | +00000000088496 | +00000000100000 |
| NIF | 22222222C | 00000000 | ESUSD990000000810123456222 | +00000000117000 | +00000000100000 |

En total, dos registros en el archivo.

Ejemplo 3. Un depósito de un mismo titular con dos imposiciones con distinta fecha de vencimiento. La primera, de 10.000 euros, con vencimiento el 12 de junio de 2019. La segunda, de 10.000 euros, con vencimiento el 30 de diciembre de 2019.

| Tipo de documento de identificación | Número de documento de identificación | Fecha de vencimiento | Código del depósito | Importe en euros | Importe en divisa |
| --- | --- | --- | --- | --- | --- |
| Campo 1 | Campo 2 | Campo 14 | Campo 15 | Campo 19 | Campo 21 |
| NIF | 33333333D | 20190612 | ESEUR990000000810123456333 | +00000001000000 |  |
| NIF | 33333333D | 20191230 | ESEUR990000000810123456333 | +00000001000000 |  |

En total, dos registros en el archivo.

Ejemplo 4. Un depósito de un mismo titular con dos imposiciones de 10.000 euros cada una, y ambas con la misma fecha de vencimiento.

| Tipo de documento de identificación | Número de documento de identificación | Fecha de vencimiento | Código del depósito | Importe en euros | Importe en divisa |
| --- | --- | --- | --- | --- | --- |
| Campo 1 | Campo 2 | Campo 14 | Campo 15 | Campo 19 | Campo 21 |
| NIF | 44444444E | 20180930 | ESEUR990000000810123456444 | +00000002000000 |  |

En total, un registro en el archivo, porque los campos que conforman la clave única son iguales.

> Se modifica, con efectos de 30 de junio de 2021, por la norma única.d) de la Circular 2/2021, de 28 de enero. Ref. BOE-A-2021-1475

> Se modifica, con efectos de 8 de agosto de 2019, por la norma única de la Circular de 30 de enero de 2019. Ref. BOE-A-2019-1694
