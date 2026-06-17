## ANEXO III

## Especificaciones técnicas para el procedimiento de embargo de cuentas previamente contestadas con los códigos 09 y 10, y de deudores en situaciones concursales, regulado en el apartado 4 del dispongo sexto

El intercambio telemático se realizará por medio de servicios REST, desarrollados por la Agencia Tributaria.

Las entidades adheridas a esta resolución podrán acceder a los servicios REST en cualquier momento a través de la entidad transmisora establecida en el formulario de comunicación de elección de canal y aportación de datos (en el caso de entidades colaboradoras) o en el formulario de solicitud de adhesión (en el caso de entidades no colaboradoras).

Se desarrollarán seis operaciones en el servicio REST:

– Recuperar diligencias pendientes de contestar.

– Contestación a diligencias de embargo de cuentas.

– Recuperar diligencias con trabas pendientes de ingreso.

– Recuperación de las órdenes de levantamientos de diligencias de embargo de cuentas.

– Consulta de importes a ingresar diarios.

– Recuperar documentos a partir del CSV.

La especificación técnica de los servicios se publicará en la Sede electrónica de la Agencia Tributaria para el libre acceso a la misma por parte de las entidades adheridas.

A continuación, se detalla el funcionamiento de cada uno de estos servicios.

1. Recuperar diligencias pendientes de contestar.

Esta operación permite a las entidades recoger todas las diligencias de embargo de cuentas que tengan pendientes de contestar.

En la respuesta de la petición se devolverá el identificador de la petición realizada si hay más diligencias a recuperar. El identificador se deberá proporcionar en una nueva petición para continuar recuperando las diligencias pendientes. Si el identificador en la respuesta de una petición es vacío indicará que es la última página de la respuesta.

Como información para identificar a los deudores, la Agencia Tributaria puede llegar a proporcionar a las entidades hasta tres posibles valores que permitan determinar la titularidad de las cuentas.

Como campo obligatorio, siempre se informará el NIF del deudor que la Agencia Tributaria tenga recogido en sus sistemas de información. Para facilitar la labor de identificación, se podrán proporcionar de forma adicional al NIF anterior, un dato correspondiente al NIE o al NIF que hubiese podido tener anteriormente el deudor y/o el número de pasaporte del deudor con el que haya podido interoperar con las entidades.

La entidad, deberá utilizar la información que pueda venir en estos tres campos para proceder a la identificación del deudor en cuanto a titularidad de cuentas.

1.1 Datos de la petición para recuperar diligencias de embargo cuentas pendientes de contestar.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta a partir de una petición anterior.

– tipoPeticion. Campo obligatorio que puede tomar los siguientes valores:

● ‘T’. Todas las diligencias pendientes de contestar (presentadas o no con anterioridad).

● ‘R’. Diligencias que ya han sido presentadas previamente.

● ‘N’. Diligencias nuevas, no presentadas previamente.

– deudorConcursal. Campo obligatorio. Indica si las diligencias corresponden a deudores en situación concursal o no. Puede tomar los siguientes valores:

● ‘T’. Todas las diligencias independientemente del tipo de deudor.

● ‘S’. Diligencias en las que el deudor está en situación concursal.

● ‘N’. Diligencias en las que el deudor no está en situación concursal.

1.2 Datos de la respuesta para recuperar diligencias de embargo de cuentas pendientes de contestar.

Los datos que se reciben ante una petición de diligencias pendientes de contestar son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina: Bloque de información de la paginación de la respuesta.

● numeroTotalDiligencias. Campo que recoge el número total de diligencias de cuentas pendientes de contestar que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar las diligencias pendientes de contestar.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de diligencias. Si el valor del identificador de la petición es vacío indica que ya no hay más diligencias que recuperar.

● numeroDiligenciasPagina. Número de diligencias recuperadas en la petición o página actual.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas pendientes de contestar.

● Diligencia: El bloque de información correspondiente a cada diligencia es el siguiente:

○ numeroDiligencia. Número de la diligencia de embargo.

○ nifDeudor. Campo obligatorio que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será el número de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ deudorConcursal. Campo que indica si el deudor está en concurso o no. Valor ‘S’ o ‘N’.

○ fechaEmision. Fecha de emisión de la diligencia. Formato AAAMMDD.

○ fechaPresentacion. Fecha de presentación de la diligencia (es la fecha en la que la entidad recuperó correctamente por primera vez la diligencia). Formato AAAAMMDD.

○ horaPresentacion. Hora de presentación de la diligencia (es la hora en la que la entidad recuperó correctamente por primera vez la diligencia). Formato HHMMSS.

○ importeEmbargo. Importe a embargar/retener. Importe en céntimos de euro.

○ csv. CSV del documento de la diligencia de embargo de cuentas.

○ numeroJustificanteIngreso. Número de justificante de ingreso. Si se trata de una entidad colaboradora el número de justificante de ingreso coincide con el número de diligencia.

○ modelo. Modelo del documento de ingreso de diligencias de embargo. Valores permitidos: 003 (para entidades colaboradoras) y 008 (resto).

○ ListaCuentas. Bloque correspondiente a las cuentas incluidas en la diligencia (de 1 a 3).

□ cuentaIBAN. IBAN de la cuenta.

□ codigoResultado. El código de respuesta previo podrá ser «09» (cuenta pignorada), «10» (deudor en proceso concursal según la Entidad de crédito) o «99» (deudor en proceso concursal según la información disponible en la Agencia Tributaria).

○ ListaCuentasNoCuentaNomina. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN. Si la entidad realiza una traba en alguna de estas cuentas, no puede responder con un código 13. Es un máximo de 10 posibles valores.

□ cuentaIBANNoCuentaNomina. IBAN de la cuenta sobre la que no se puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN.

○ ListaCuentasEmbargoNoExtensible. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no debe extender el embargo. Si la entidad es conocedora de otras cuentas adicionales a las tres incluidas en la diligencia no podrá extender el embargo a aquellas cuentas informadas en este bloque. Es un máximo de 10 posibles valores.

□ cuentaIBANEmbargoNoExtensible. IBAN de la cuenta sobre la que no se puede extender el embargo.

2. Contestación diligencias de embargo de cuentas.

Esta operación permite a las entidades contestar todas las diligencias de embargo de cuentas que tengan pendientes. El sistema devolverá, por cada diligencia contestada en la petición, el resultado de la contestación. Si el resultado de contestación ha sido erróneo se enviará un código de error, detallando el problema detectado. Si la contestación se ha grabado correctamente, en este caso creará una constancia de dicha contestación telemática indicando el certificado de acceso, la fecha de la contestación y el contenido de la respuesta.

Si una entidad envía una contestación con N diligencias, la Agencia Tributaria las procesará individualmente y en la respuesta se indicará el resultado individual de cada una. Es posible, por tanto, que en la respuesta de una contestación de diligencias haya diligencias que se hayan procesado correctamente y otras con error.

Si la Agencia Tributaria devuelve error en una diligencia, solo esta diligencia seguirá estando pendiente de contestar. Se podrá volver a contestar esta diligencia desde el servicio REST.

Para diligencias de deudores en proceso concursal, si las cuentas incluidas originalmente en la diligencia no son suficientes para cubrir el embargo, la entidad debe añadir en la contestación cuentas nuevas que no estén originalmente en la diligencia. Deberá extender el embargo hasta un máximo de diez cuentas por diligencia.

La entidad puede realizar la traba en una cuenta con una única divisa distinta al euro, o se trate de una cuenta con varias divisas distintas al euro. Para cuentas que no estén pignoradas, en caso de una única divisa, la entidad deberá aportar en la respuesta asociada a la cuenta en divisas, la divisa en la que se encuentra la cuenta, el importe en dicha divisa que se ha trabado, el tipo de cambio que se ha aplicado y el importe de la traba en euros; y en caso de cuenta con varias divisas, la entidad deberá aportar la información para los cuatro campos anteriores tantas veces como tipos de divisas tenga la cuenta en la que se realiza la traba.

En el caso de que la cuenta pignorada estuviera denominada en divisas o multidivisas, la entidad deberá comunicar en euros el «importe trabado libre de pignoración» y el «importe trabado afecto a pignoración», aplicando las reglas de conversión de tipo de cambio fixing establecidas para la utilización del código «12 Traba realizada en divisa» en el apartado 4.6. del dispongo Séptimo.

2.1. Datos de la petición para contestación de diligencias de embargo de cuentas.

En función del código de resultado de la cuenta, la entidad, en el momento de contestar a la diligencia, deberá informar el bloque de datos ContestacionGeneral, para aquellas cuentas que no estén pignoradas y el bloque de datos ContestacionPignorada si la cuenta está pignorada. Ambos bloques de datos son excluyentes.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas que se quiere contestar. Por cada diligencia se debe informar:

● Diligencia. Bloque de datos de cada diligencia.

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo que recogerá el NIF o NIE del deudor.

○ deudorConcursal. Campo que indica si el deudor está en concurso o no.

○ importeTotalTrabado. Importe total acumulado trabado en la diligencia. Debe coincidir con la suma del importe trabado en cada cuenta. En céntimos de euro. Si la respuesta a la diligencia implica que no existe importe trabado, este campo se informará con valor cero.

○ ListaCuentas. Bloque correspondiente a las cuentas incluidas en la respuesta a la diligencia. Si la entidad respondió con el código ‘09’ a la diligencia, únicamente hay que proporcionar información sobre las cuentas pignoradas.

□ Cuenta. El bloque de información de cada cuenta es el siguiente:

■ cuentaIBAN. IBAN de la cuenta.

■ tipoCuenta. Tomará alguno de los valores siguientes:

1. Cuenta corriente.

2. Cuenta ahorro.

3. Imposiciones plazo.

4. Cuentas financieras.

5. Cuentas de crédito.

6. Cuentas soportadas en contratos financieros atípicos.

7. Cuentas de pago.

8. Cuentas de dinero electrónico.

9. Otras cuentas.

La Agencia Tributaria verificará, si ya posee la información de esta cuenta, que este código coincide con el código que ya tiene en su poder. En caso de no coincidir se devolverá un error de validación de datos para la diligencia, que seguirá pendiente de contestar.

■ codigoResultado. Este campo refleja el resultado del embargo que la entidad indica sobre cada cuenta informada en la diligencia.

Si la diligencia fue contestada previamente en «nuevo sistema EDITRAN» o en «canal servicios REST» con código 09, deberá indicarse obligatoriamente código 09. En el resto de casos puede tomar alguno de los siguientes valores:

00. SIN ACTUACIÓN.

01. TRABA REALIZADA.

02. NIF NO TITULAR DE LA CUENTA COMUNICADA.

03. INEXISTENCIA DE SALDO (SALDO CERO O NEGATIVO).

04. SALDO NO DISPONIBLE POR EMBARGO PREVIO O BLOQUEO JUDICIAL.

05. CUENTA INEXISTENTE O CANCELADA.

06. OTROS MOTIVOS.

07. TRABA CON DIFERENCIA ENTRE SALDO DISPONIBLE Y CONTABLE.

08. CUENTA EXCLUIDA DEL PROCEDIMIENTO.

09. SALDO PIGNORADO.

12. TRABA REALIZADA EN DIVISAS.

13. TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN.

14. EMBARGO NO PROCEDENTE SEGÚN NORMATIVA VIGENTE.

■ ContestacionPignorada. Bloque de información condicional, correspondiente a los datos de pignoración de la cuenta. Solo se informará este bloque si la cuenta está pignorada.

► importeNoPignorado. Importe de traba libre de pignoración (no afecto a la pignoración), en céntimos de euro. Si la cuenta pignorada estuviera denominada en divisas, este importe se deberá comunicar en euros aplicando las reglas de conversión de tipo de cambio fixing establecidas en el apartado 4.6. del dispongo Séptimo.

► importePignorado Importe trabado afecto a pignoración (importe de traba pignorado), en céntimos de euro. Si la cuenta pignorada estuviera denominada en divisas, este importe se deberá comunicar en euros aplicando las reglas de conversión de tipo de cambio fixing establecidas en el apartado 4.6. del dispongo Séptimo.

► fechaPignoracion. Fecha de la pignoración. En formato: AAAAMMDD.

► importeObligacionGarantizada. Importe de la obligación garantizada. En céntimos de euro.

► fechaVencimientoObligacionGarantizada. Fecha de vencimiento de la obligación garantizada. En formato: AAAAMMDD.

► interposicionTerceria. Indicador de si existe intención por parte de la entidad de interponer imponer tercería. Toma los valores ‘S’ o ‘N’.

■ ContestacionGeneral. Bloque de información condicional. Únicamente se informará este bloque si la cuenta no está pignorada.

► ImporteTraba. Importe trabado en la cuenta. En céntimos de euro. Si la respuesta implica que no existe importe trabado en la cuenta, este campo se informará con valor cero.

► importeNoDisponible. Cuando la entidad conteste con un código de respuesta 04 (SALDO NO DISPONIBLE POR EMBARGO PREVIO) debe informar en este campo el importe no disponible para el embargo por la existencia de un bloqueo judicial o un embargo previo. En céntimos de euro. En cualquier otro caso, este campo no se informará ni se incluirá en la invocación al servicio.

► infoAdicionalSaldo. Cuando la entidad conteste con un código de respuesta 07 TRABA CON DIFERENCIA ENTRE SALDO DISPONIBLE Y CONTABLE, debe informar en este campo el saldo contable de la cuenta. En céntimos de euro. Cuando la entidad conteste con un código de respuesta 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN, debe informar en este campo el saldo disponible de la cuenta, en céntimos de euro. En cualquier otro caso, este campo no se informará ni se incluirá en la invocación al servicio.

► fechaTraba: fecha de la traba en formato AAAAMMDD. Si no existe traba, este campo no se informará ni se incluirá en la invocación al servicio.

► horaTraba: hora de la traba en formato HHMMSS. Si no existe traba, este campo no se informará ni se incluirá en la invocación al servicio.

► InformacionDivisas. Bloque de información que recoge los datos relativos a Tipo de divisa, Importe de la traba en divisa y Tipo de cambio a fecha de la traba, por cada divisa de la cuenta. En el en caso de cuentas multidivisa en las que se haya aplicado la traba en euros, el bloque puede repetirse tantas veces como divisas tenga la cuenta multidivisa. En caso de que la información de la traba no corresponda a cuentas en divisas, todo este bloque de información no se informará ni se incluirá en la invocación al servicio.

— tipoDivisa. Campo que recoge el tipo de divisa de la cuenta. El tipo de divisa se regirá según el código ISO 4217 de tres cifras.

— importeTrabaDivisa. Importe de la divisa trabado.

— tipoCambio. Campo que recoge el tipo de cambio aplicado en el momento de realizar la traba. Expresado en euros por divisa (Ej. 1 dólar = 0.85 euros).

○ existenciaMasCuentas. Indicador de si existen más cuentas de las incluidas en esta respuesta. Valores S/N (Sí/No).

2.2. Datos de la respuesta a la petición para contestación de diligencias de embargo de cuentas.

El resultado de la respuesta será el mismo listado de diligencias de la entrada, indicando el resultado de la contestación para cada diligencia.

Los datos que se reciben como respuesta a la petición de contestación de diligencias de embargo de cuentas, son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– ListaResultados. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas para las que se ha recibido respuesta. Para cada diligencia se tiene la siguiente información.

● Diligencia. Bloque de datos de cada diligencia.

○ numeroDiligencia. Número de diligencia.

○ resultado. Si la contestación se ha realizado correctamente el resultado será cero. En caso de producirse un error en la contestación, en el resultado se indicará el código de error que ha ocurrido. Ver los códigos de error en la contestación de una diligencia.

○ csv. CSV del documento justificante de la contestación de la diligencia.

○ fechaContestacion. Fecha de contestación de la diligencia. Con formato AAAAMMDD.

○ horaContestacion. Hora de contestación de la diligencia. Con formato HHMMSS.

2.3 Códigos de error en la contestación de una diligencia.

| Código | Descripción | Descripción del resultado |
| --- | --- | --- |
| 102 | Error al validar los datos proporcionados para contestar la diligencia. Los datos de entrada de la petición contienen datos incorrectos que impiden que se procese correctamente la contestación de la diligencia. | Se pondrá una descripción del error producido. |
| 101 | Error en el formato de la respuesta de la diligencia. | Se pondrá una descripción del error producido. |

3. Recuperar diligencias con trabas pendientes de ingreso.

Operación para consultar las diligencias pendientes de ingreso tramitadas en los formularios de la Sede de la Agencia Tributaria.

En la respuesta de la petición se devolverá el identificador de la petición realizada si hay más diligencias a recuperar. El identificador se deberá proporcionar en una nueva petición para continuar recuperando las diligencias pendientes. Si el identificador en la respuesta de una petición es vacío indicará que es la última página de la respuesta.

Como información para identificar a los deudores, la Agencia Tributaria puede llegar a proporcionar a las entidades hasta tres posibles valores que permitan determinar la titularidad de las cuentas.

Como campo obligatorio, siempre se informará el NIF del deudor que la Agencia Tributaria tenga recogido en sus sistemas de información. Para facilitar la labor de identificación, se podrán proporcionar de forma adicional al NIF anterior, un dato correspondiente al NIE o al NIF que hubiese podido tener anteriormente el deudor y/o el número de pasaporte del deudor con el que haya podido interoperar con las entidades.

La entidad, deberá utilizar la información que pueda venir en estos tres campos para proceder a la identificación del deudor en cuanto a titularidad de cuentas.

3.1 Datos de la petición para recuperar las diligencias con trabas pendientes de ingreso.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta a partir de una petición anterior.

– tipoPeticion. Campo obligatorio que puede tomar los siguientes valores:

● ‘T’. Todas las diligencias con traba.

● ‘N’-> Diligencias no ingresadas y con la fecha límite no vencida.

● ‘V’ -> Diligencias no ingresadas y con la fecha límite vencida.

– deudorConcursal. Campo obligatorio. Indica si las diligencias corresponden a deudores en situación concursal o no. Puede tomar los siguientes valores:

● ‘T’. Todas las diligencias independientemente del tipo de deudor.

● ‘S’. Diligencias en las que el deudor está en situación concursal.

● ‘N’. Diligencias en las que el deudor no está en situación concursal.

– pignoracion. Campo obligatorio. Recoge si las diligencias tienen cuentas pignoradas. Puede tomar los siguientes valores:

● ‘T’. Todas las diligencias independientemente del estado de las cuentas.

● ‘S’. Diligencias en las que alguna cuenta está pignorada.

● ‘N’. Diligencias en las que ninguna cuenta está pignorada.

– tercerias. Campo obligatorio. Recoge el estado de las tercerías en las diligencias. Puede tomar los siguientes valores:

● ‘T’. Todas las diligencias independientemente del estado de las tercerías.

● ‘A’. Con alguna tercería aceptada a trámite.

● ‘R’. Con alguna tercería rechazada a trámite.

● ‘H. Con alguna tercería resuelta a favor de la Agencia Tributaria.

● ‘E’. Con alguna tercería resuelta a favor de la Entidad.

● ‘G’. Con alguna tercería y garantía total aplicada.

● ‘P’. Con alguna tercería y garantía parcial o no aplicada.

3.2 Datos de la respuesta a la petición para recuperar las diligencias con trabas pendientes de ingreso.

Los datos que se reciben como respuesta a la petición para recuperar las diligencias con trabas pendientes de ingreso son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina: Bloque de información de la paginación de la respuesta.

● numeroTotalDiligencias. Campo que recoge el número total de diligencias de cuentas pendientes de contestar que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar las diligencias pendientes de contestar.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de diligencias. Si el valor del identificador de la petición es vacío indica que ya no hay más diligencias que recuperar.

● numeroDiligenciasPagina. Número de diligencias recuperadas en la petición o página actual.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas con traba pendientes de ingreso.

● Diligencia: El bloque de información correspondiente a cada diligencia es el siguiente:

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo obligatorio que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será el número de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ deudorConcursal. Campo que indica si el deudor está en situación concursal o no.

○ fechaEmision. Fecha de emisión de la diligencia. Formato AAAMMDD.

○ fechaPresentacion. Fecha de presentación de la diligencia (es la fecha en la que la entidad recuperó correctamente por primera vez la diligencia). Formato AAAAMMDD.

○ horaPresentacion. Hora de presentación de la diligencia (es la hora en la que la entidad recuperó correctamente por primera vez la diligencia). Formato HHMMSS.

○ csv. CSV del documento de la diligencia de embargo de cuentas.

○ numeroJustificanteIngreso. Número de justificante de ingreso. Si se trata de una entidad colaboradora el número de justificante de ingreso coincide con el número de diligencia.

○ modelo. Modelo del documento de ingreso de diligencias de embargo. Valores permitidos: 003 (para entidades colaboradoras) y 008 (resto).

○ importeEmbargo. Importe a embargar/retener. Importe en céntimos de euro.

○ ImporteIngresado. Importe ingresado por la entidad y aplicado sobre la diligencia. Importe en céntimos de euro.

○ importePendienteIngresar. Importe pendiente de ingreso efectivo en la diligencia. Importe en céntimos de euro.

○ importesAIngresarComunicados. Bloque que recoge la lista de importes a ingresar de la diligencia comunicados a la entidad.

□ ImporteAIngresar. Bloque correspondiente a cada ingreso a realizar.

■ fecha. Fecha del importe a ingresar.

■ importe. Importe a ingresar. En céntimos de euro.

■ cuentaIBAN. IBAN de la cuenta desde la que se debe realizar el ingreso.

○ Ingresos. Bloque que recoge la lista de ingresos aplicados de forma efectiva sobre la diligencia.

○ Ingreso. Bloque correspondiente a cada ingreso realizado.

□ fecha. Fecha del ingreso realizado.

□ importe. Importe ingresado. En céntimos de euro.

4. Recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Petición que permitirá a una entidad consultar los levantamientos de las diligencias de cuentas.

En la respuesta de la petición se devolverá el identificador de la petición realizada si hay más levantamientos a recuperar. El identificador se deberá proporcionar en una nueva petición para continuar recuperando los levantamientos pendientes. Si el identificador en la respuesta de una petición es vacío indicará que es la última página de la respuesta.

Como información para identificar a los deudores, la Agencia Tributaria puede llegar a proporcionar a las entidades hasta tres posibles valores que permitan determinar la titularidad de las cuentas.

Como campo obligatorio, siempre se informará el NIF del deudor que la Agencia Tributaria tenga recogido en sus sistemas de información. Para facilitar la labor de identificación, se podrán proporcionar de forma adicional al NIF anterior, un dato correspondiente al NIE o al NIF que hubiese podido tener anteriormente el deudor y/o el número de pasaporte del deudor con el que haya podido interoperar con las entidades.

La entidad, deberá utilizar la información que pueda venir en estos tres campos para proceder a la identificación del deudor en cuanto a titularidad de cuentas.

4.1 Datos de la petición para recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta a partir de una petición anterior.

– tipoPeticion. Campo obligatorio que puede tomar los siguientes valores:

● ‘T’. Todos los levantamientos producidos en los últimos tres meses.

● ‘P’. Levantamientos pendientes de notificar sin límite temporal.

● ‘N’. Levantamientos ya notificados en los últimos tres meses.

– deudorConcursal. Campo obligatorio. Indica si los levantamientos corresponden a deudores en situación concursal o no. Puede tomar los siguientes valores:

● ‘T’. Todos los levantamientos de diligencias independientemente del tipo de deudor.

● ‘S’. Levantamientos de diligencias en las que el deudor está en situación concursal.

● ‘N’. Levantamientos de diligencias en las que el deudor no está en situación concursal.

4.2 Datos de la respuesta para recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Los datos que se reciben ante una petición de levantamientos de diligencias de embargo de cuentas son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina: Bloque de información de la paginación de la respuesta.

● numeroTotalLevantamientos. Campo que recoge el número total de levantamientos de cuentas que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar las diligencias pendientes de contestar.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de diligencias. Si el valor del identificador de la petición es vacío indica que ya no hay más diligencias que recuperar.

● numeroLevantamientosPagina. Número de levantamientos recuperados en la petición o página actual.

– ListaLevantamientos. Bloque de información correspondiente a la lista de levantamientos de diligencias de embargo de cuentas.

● Levantamiento. El bloque de información correspondiente a cada levantamiento:

○ recuperadoPreviamente. Indicador que permite determinar si el levantamiento se ha recuperado con anterioridad ya por el servicio o es la primera vez. Tomará los valores ‘S’ (Sí) o ‘N’ (No)

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será el número de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ importeEmbargo. En céntimos de euro.

○ importeTrabaDiligencia. Importe total trabado en la diligencia después de aplicar el levantamiento. En céntimos de euro.

○ csv. CSV del documento del levantamiento de la diligencia de embargo de cuentas.

○ fechaLevantamiento. Fecha de emisión del levantamiento. Formato AAAAMMDD.

○ ListadoCuentas. Lista de cuentas.

□ Cuenta. El bloque de información correspondiente a cada cuenta:

■ cuentaIBAN. IBAN de la cuenta.

■ codigoTipoLevantamiento. Los posibles valores son:

► 01: Levantamiento total del embargo de la cuenta.

► 02: Levantamiento parcial del embargo de la cuenta.

► 03: No hay levantamiento para esa cuenta.

■ importeLevantado. En céntimos de euro. Cuando se trate de cuentas en divisas, el importe en divisas a reintegrar a la cuenta del cliente será el resultante de aplicar al importe levantado en euros el tipo de cambio existente a la fecha de aplicación de la traba.

5. Consulta de importes a ingresar diarios.

A través de esta petición, una entidad podrá consultar los importes a ingresar que venzan cada día.

En la respuesta de la petición se devolverá el identificador de la petición realizada si hay más importes a recuperar. El identificador se deberá proporcionar en una nueva petición para continuar recuperando los importes pendientes. Si el identificador en la respuesta de una petición es vacío indicará que es la última página de la respuesta.

5.1 Datos de la petición para la consulta de los importes a ingresar diarios.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta a partir de una petición anterior.

– deudorConcursal. Campo obligatorio. Indica si las diligencias corresponden a deudores en situación concursal o no. Puede tomar los siguientes valores:

● ‘T’. Todas las diligencias independientemente del tipo de deudor.

● ‘S’. Diligencias en las que el deudor está en situación concursal.

● ‘N’. Diligencias en las que el deudor no está en situación concursal.

5.2 Datos de la respuesta a la petición para la consulta de los importes a ingresar diarios.

Los datos que se reciben como respuesta a la petición para la consulta de los importes a ingresar diarios son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina: Bloque de información de la paginación de la respuesta.

● numeroTotalImportes. Campo que recoge el número total de importes a ingresar que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar las diligencias pendientes de contestar.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de diligencias. Si el valor del identificador de la petición es vacío indica que ya no hay más diligencias que recuperar.

● numeroImportesPagina. Número de importes a ingresar recuperados en la petición o página actual.

– ListaImportesAIngresar. Bloque de información correspondiente a la lista de importes a ingresar correspondientes a importes vencidos diariamente.

● ImporteAIngresar. Bloque correspondiente a cada ingreso a realizar.

○ importe. Importe a ingresar. Importe en céntimos de euro.

○ numeroDiligencia. Número de diligencia de embargo.

○ cuentaIBAN. IBAN de la cuenta desde la que se debe realizar el ingreso.

6. Recuperar documentos a partir de CSV.

A través de esta petición, una entidad podrá recuperar un documento a partir de su CSV.

6.1 Datos de la petición de recuperación de documentos por CSV.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– csv. CSV solicitado.

El tipo de documentos que se podrán recoger mediante este servicio son: diligencias, levantamientos y constancias de contestación.

6.2 Datos de la respuesta a la petición de recuperación de documentos por CSV.

Los datos que se reciben ante una petición de recuperación de documentos por CSV son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– Documento. Bloque de información relativo al documento asociado al CSV:

● csv. CSV que se ha solicitado.

● formato. Indica el tipo MIME del documento (por ejemplo, ‘application/pdf’).

● contenido. Campo con el contenido del documento codificado en Base64.

7. Códigos de respuesta utilizados en el intercambio telemático de los servicios REST.

A continuación, se indican los códigos de estado estándar HTTP (HTTP Status Code) usados en el intercambio de datos:

| Código de estado | Descripción |
| --- | --- |
| 200 | Petición procesada correctamente. |
| 400 | El servidor no puede procesar la petición porque hay un error en los datos de entrada. |
| 401 | Autentificación incorrecta. Acceso no autorizado a los datos. |
| 404 | Recurso no encontrado. |
| 500 | El servidor no puede procesar la petición por un problema en el sistema. |

7.1 Respuesta con códigos de estado 40x y 500.

Las respuestas con código de estado 40x o 500 son respuestas de un error producido en los datos enviados desde el cliente (códigos de estado 40x) o en el tratamiento de la petición en el servidor (código de estado 500). A continuación, se indica la relación de códigos de error que se devolverán en una respuesta con error:

| Código | Código de estado | Descripción del error |
| --- | --- | --- |
| 10 | 400 | Error al validar los datos de entrada de la petición. Los datos de entrada de la petición contienen datos incorrectos que impiden que se procesen correctamente la petición. |
| 20 | 401 | Acceso no autorizado al servicio. El certificado electrónico usado en la petición no está autorizado para realizar trámites en representación de la entidad indicada. |
| 30 | 404 | No existe un documento con el CSV indicado. |
| 50 | 500 | No se ha podido procesar correctamente la petición. Posibles causas: – Fallo de conexión a la base de datos. – Caída del sistema, etc. Si el error persiste, pónganse en contacto con los administradores del WS. |
