## ANEXO I

## Especificaciones técnicas para el procedimiento de embargo de cuentas por el «Canal Servicios Rest» regulado en el dispongo quinto, apartado 2

El intercambio telemático se realizará por medio de servicios REST, desarrollados por la Agencia Tributaria.

Desde su puesta en funcionamiento, las entidades adheridas a esta resolución podrán acceder a los servicios REST en cualquier momento a través de la entidad transmisora establecida en el formulario de comunicación de elección de canal y aportación de datos (en el caso de entidades colaboradoras) o en el formulario de solicitud de adhesión (en el caso de entidades no colaboradoras).

Las condiciones de seguridad para el acceso a estos servicios REST se establecen en el dispongo Décimo y en el anexo IV de esta resolución.

Se desarrollarán siete operaciones en el servicio REST:

– Consulta de número de diligencias nuevas pendientes de recuperar y obtención de los identificadores de paginación.

– Recoger diligencias de embargo de cuentas nuevas pendientes de recuperar.

– Confirmación de recuperación de diligencias.

– Recoger diligencias de embargo de cuentas pendientes de contestar que ya han sido recuperadas previamente por una entidad.

– Contestación a diligencias de embargo de cuentas.

– Recuperación de las órdenes de levantamientos de diligencias de embargo de cuentas.

– Recuperación de documentos partiendo del Código Seguro de Verificación (CSV).

La especificación técnica de los servicios en formato YAML se publicará en la Sede electrónica de la Agencia Tributaria para el libre acceso a la misma por parte de las entidades adheridas.

A continuación, se detalla el funcionamiento de cada uno de estos servicios.

1. Consulta de número de diligencias nuevas pendientes de recuperar y obtención de los identificadores de paginación.

Operación de invocación obligatoria de forma previa a recuperar diligencias nuevas, que proporciona a las entidades un resumen de las diligencias pendientes de recuperar. Recibe como respuesta el número de diligencias que están pendientes, así como los identificadores de página necesarios para poder recogerlas.

1.1 Datos de la petición para consultar el número de diligencias nuevas pendientes de recuperar y la obtención de los identificadores de paginación.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

1.2 Datos de la respuesta para consultar el número de diligencias nuevas pendientes de recuperar y la obtención de los identificadores de paginación.

Los datos que se reciben ante una petición de consulta:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– ResumenDiligencias. Bloque de información con el resultado del número de diligencias totales, así como los identificadores de página.

● numeroPaginas. Número total de páginas que se devuelven para la recogida de las diligencias pendientes de recuperar.

● numeroTotalDiligencias. Representa el número total de diligencias que tiene la entidad pendiente de recuperar.

● numeroMaximoDiligenciasPagina. Indica el número máximo de diligencias que puede haber en una página de datos.

● DatosPagina. Bloque de información relativo a los identificadores de paginación para recuperar las diligencias.

○ codigoPagina. Identificador alfanumérico de las distintas páginas que contienen diligencias pendientes de recuperar.

○ numeroDiligenciasPagina. Número de diligencias que contiene la página.

2. Recoger diligencias nuevas de embargo de cuentas pendientes de recuperar.

Esta operación permite a las entidades recoger todas las diligencias de embargo de cuentas que tengan pendientes de recuperar. Sólo se devolverán aquellas diligencias de embargo de cuentas nuevas o que no hayan sido confirmada su recogida por parte de la entidad. Para recuperar dichas diligencias es necesario emplear la información obtenida en la operación anterior.

2.1 Datos de la petición para recoger diligencias nuevas de cuentas pendientes de recuperar.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo obligatorio. Corresponde con cada uno de los identificadores de página recuperados en la operación anterior. Mediante este identificador, las entidades recogen las diligencias pendientes de recuperar.

2.2 Datos de la respuesta para recoger diligencias nuevas de cuentas pendientes de recuperar.

Como información para identificar a los deudores, la Agencia Tributaria puede llegar a proporcionar a las entidades hasta tres posibles valores que permitan determinar la titularidad de las cuentas.

Como campo obligatorio, siempre se informará el NIF del deudor que la Agencia Tributaria tenga recogido en sus sistemas de información. Para facilitar la labor de identificación, se podrán proporcionar de forma adicional al NIF anterior, un dato correspondiente al NIE o al NIF que hubiese podido tener anteriormente el deudor y/o el número de pasaporte del deudor con el que haya podido interoperar con las entidades.

La entidad, deberá utilizar la información que pueda venir en estos tres campos para proceder a la identificación del deudor en cuanto a titularidad de cuentas.

Los datos que se reciben ante una petición de diligencias pendientes de recuperar son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina. Bloque de información relacionada con la página.

● codigoPagina. Corresponde con el identificador de página informado en la petición.

● numeroDiligenciasPagina. Número de diligencias incluidas en la página.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas pendientes de recuperar.

● Diligencia. El bloque de información correspondiente a cada diligencia es el siguiente:

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo obligatorio que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Recogerá, en caso de ir informado, un identificador adicional al NIF que permita identificar al deudor, que será el n.º de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ fechaEmision. Fecha de emisión de la diligencia. Formato AAAAMMDD.

○ importeEmbargo. Importe a embargar/retener. Importe en céntimos de euro.

○ csv. CSV del documento de la diligencia de embargo de cuentas.

○ numeroJustificanteIngreso. Número de justificante de ingreso. Si se trata de una entidad colaboradora el número de justificante de ingreso coincide con el número de diligencia.

○ modelo. Modelo del documento de ingreso de diligencias de embargo. Valores permitidos: 003 (para entidades colaboradoras) y 008 (resto).

○ ListaCuentas. Bloque correspondiente a las cuentas incluidas en la diligencia (de 1 a 3).

□ cuentaIBAN. IBAN de la cuenta.

○ ListaCuentasNoCuentaNomina. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN. Si la entidad realiza una traba en alguna de estas cuentas, no puede responder con un código 13. Es un máximo de 10 posibles valores.

□ cuentaIBANNoCuentaNomina. IBAN de la cuenta sobre la que no se puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN.

○ ListaCuentasEmbargoNoExtensible. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no debe extender el embargo. Si la entidad es conocedora de otras cuentas adicionales a las tres incluidas en la diligencia no podrá extender el embargo a aquellas cuentas informadas en este bloque. Es un máximo de 10 posibles valores.

□ cuentaIBANEmbargoNoExtensible. IBAN de la cuenta sobre la que no se puede extender el embargo.

○ ListaAvisos. Este bloque incluirá, en caso de que sea necesario, uno o más avisos de carácter informativo para la entidad por cada diligencia recuperada.

□ codigoAviso. Tomará alguno de los valores indicados a continuación. Aunque a priori el único aviso que se contempla es el mostrado en la tabla, se deja como una lista de avisos por si se diese la necesidad.

□ descripcionAviso. Texto descriptivo del aviso.

2.3 Códigos de aviso en la recuperación de las diligencias pendientes.

Determinadas circunstancias podrían dar lugar a situaciones en las cuales se estima oportuno incluir un aviso de carácter informativo para la entidad:

| CódigoAviso | Descripción del aviso |
| --- | --- |
| 10 | Recuperación de diligencias fuera de plazo. |

3. Confirmación de recuperación de diligencias nuevas por una entidad.

Operación de invocación obligatoria por parte de las entidades. Permite enviar una confirmación a la Agencia Tributaria indicando que la entidad ha recogido correctamente las diligencias de embargo de cuentas pendientes de recuperar asociados a un identificador de página dado.

Se trata de una operación síncrona que asegura tanto el emisor (Agencia Tributaria) como al receptor (entidad), que se ha intercambiado correctamente la información asociada a un conjunto de diligencias de embargo de cuentas.

3.1 Datos de la petición para confirmar la recuperación de diligencias de embargo de cuentas por una entidad.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo obligatorio. Corresponde con el identificador de página recuperado en la operación anterior. Mediante este identificador, la entidad confirma la correcta recuperación de las diligencias incluidas en esa página.

– fechaConfirmacion. Campo obligatorio. Corresponde con la fecha del momento en el que la entidad ha recibido correctamente las diligencias pendientes de recuperar asociadas al identificador de página anterior.

– horaConfirmacion. Campo obligatorio. Corresponde con la hora en la que la entidad ha recibido correctamente las diligencias pendientes de recuperar asociadas al identificador de página anterior.

3.2 Datos de la respuesta a la petición para confirmar la recuperación de diligencias de embargo de cuentas por una entidad.

Los datos que se reciben como respuesta a la petición de contestación de diligencias de embargo de cuentas, son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– codigoPagina. Identificador de página enviado en la petición.

– resultado. Si el envío de la confirmación corresponde a un identificador de página valido y no se ha producido ningún error, el resultado será cero. En caso de producirse un error en la contestación, en el resultado se indicará el código de error que ha ocurrido. Ver los códigos de error en la contestación de una diligencia.

3.3. Códigos de error en la confirmación a las diligencias recogidas.

Determinadas circunstancias podrían dar lugar a situaciones en las cuales se estima oportuno incluir un aviso de carácter informativo para la entidad:

| Código | Descripción | Descripción del resultado |
| --- | --- | --- |
| 40 | Error al validar los datos proporcionados para confirmar la recepción de las diligencias contenidas en el identificador de página. Los datos de entrada de la petición contienen datos incorrectos que impiden que se procese correctamente la contestación de la diligencia. | Se pondrá una descripción del error producido. |
| 53 | Error al procesar la confirmación de la página recibida. Ya se ha confirmado la recepción de las diligencias previamente. | La situación actual de las diligencias contenidas en la página indica que ya han sido confirmadas con anterioridad. |

4. Recoger diligencias de embargo de cuentas pendientes de contestar que ya han sido recuperadas previamente por una entidad.

Esta operación permite a las entidades recoger todas las diligencias de embargo de cuentas que tengan pendientes de contestar pero que ya han sido recuperadas previamente y confirmada su recuperación por parte de la entidad.

En la respuesta de la petición se devolverá el identificador de la petición realizada si hay más diligencias a recuperar. El identificador se deberá proporcionar en una nueva petición para continuar recuperando las diligencias pendientes. Si el identificador en la respuesta de una petición es vacío indicará que es la última página de la respuesta.

Como información para identificar a los deudores, la Agencia Tributaria puede llegar a proporcionar a las entidades hasta tres posibles valores que permitan determinar la titularidad de las cuentas.

Como campo obligatorio, siempre se informará el NIF del deudor que la Agencia Tributaria tenga recogido en sus sistemas de información. Para facilitar la labor de identificación, se podrán proporcionar de forma adicional al NIF anterior, un dato correspondiente al NIE o al NIF que hubiese podido tener anteriormente el deudor y/o el número de pasaporte del deudor con el que haya podido interoperar con las entidades.

La entidad, deberá utilizar la información que pueda venir en estos tres campos para proceder a la identificación del deudor en cuanto a titularidad de cuentas.

4.1 Datos de la petición para recoger diligencias de embargo de cuentas pendientes de contestar.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta a partir de una petición anterior.

– fechaDesde. Campo opcional. Fecha desde la cual se buscarán diligencias de la pagadora. Campo en formato AAAAMMDD. Se corresponde con la fecha de emisión de las diligencias de embargo de cuentas.

– fechaHasta. Campo opcional. Fecha hasta la cual se buscarán diligencias de la pagadora. Campo en formato AAAAMMDD. Al igual que antes, se trata de la fecha de emisión de las diligencias. El intervalo de fechas delimitado por FechaDesde y FechaHasta no puede ser superior a un año.

4.2 Datos de la respuesta para recuperar diligencias de embargo de cuentas pendientes de contestar.

Los datos que se reciben ante una petición de diligencias pendientes de contestar son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina. Bloque de información de la paginación de la respuesta.

● numeroTotalDiligencias. Campo que recoge el número total de diligencias de embargo de cuentas pendientes de contestar que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar las diligencias pendientes de contestar.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de diligencias. Si el valor del identificador de la petición es vacío indica que ya no hay más diligencias que recuperar.

● numeroDiligenciasPagina. Número de diligencias recuperadas en la petición o página actual.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas pendientes de contestar.

● Diligencia. El bloque de información correspondiente a cada diligencia es el siguiente:

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo obligatorio que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Si este campo en el momento de la puesta a disposición de la diligencia estaba informado, en el levantamiento también irá informado recogiendo un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Si este campo en el momento de la puesta a disposición de la diligencia estaba informado, en el levantamiento también irá informado recogiendo un identificador adicional al NIF que permita identificar al deudor, que será el n.º de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ fechaEmision. Fecha de emisión de la diligencia. Formato AAAAMMDD.

○ fechaPresentacion. Fecha de presentación de la diligencia (es la fecha en la que la entidad recuperó correctamente por primera vez la diligencia). Formato AAAAMMDD.

○ horaPresentacion. Hora de presentación de la diligencia (es la hora en la que la entidad recuperó correctamente por primera vez la diligencia). Formato HHMMSS.

○ importeEmbargo. Importe a embargar/retener. Importe en céntimos de euro.

○ csv. CSV del documento de la diligencia de embargo de cuentas.

○ numeroJustificanteIngreso. Número de justificante de ingreso. Si se trata de una entidad colaboradora el número de justificante de ingreso coincide con el número de diligencia.

○ modelo. Modelo del documento de ingreso de diligencias de embargo. Valores permitidos: 003 (para entidades colaboradoras) y 008 (resto).

○ ListaCuentas. Bloque correspondiente a las cuentas incluidas en la diligencia (de 1 a 3).

□ cuentaIBAN. IBAN de la cuenta.

○ ListaCuentasNoCuentaNomina. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN. Si la entidad realiza una traba en alguna de estas cuentas, no puede responder con un código 13. Es un máximo de 10 posibles valores.

□ cuentaIBANNoCuentaNomina. IBAN de la cuenta sobre la que no se puede contestar, en caso de traba, con un código 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN.

○ ListaCuentasEmbargoNoExtensible. Bloque correspondiente al conjunto de cuentas sobre las que la entidad no debe extender el embargo. Si la entidad es conocedora de otras cuentas adicionales a las tres incluidas en la diligencia no podrá extender el embargo a aquellas cuentas informadas en este bloque. Es un máximo de 10 posibles valores.

□ cuentaIBANEmbargoNoExtensible. IBAN de la cuenta sobre la que no se puede extender el embargo.

○ ListaAvisos. Este bloque incluirá, en caso de que sea necesario, uno o más avisos de carácter informativo para la entidad por cada diligencia recuperada.

□ codigoAviso. Tomará alguno de los valores indicados a continuación. Aunque a priori el único aviso que se contempla es el mostrado en la tabla, se deja como una lista de avisos por si se diese la necesidad.

□ descripcionAviso. Texto descriptivo del aviso.

4.3 Códigos de aviso en la recuperación de las diligencias pendientes.

Determinadas circunstancias podrían dar lugar a situaciones en las cuales se estima oportuno incluir un aviso de carácter informativo para la entidad:

| Código de Aviso | Descripción del aviso |
| --- | --- |
| 10 | Recuperación de diligencias fuera de plazo. (Cuando la diligencia fue recogida por primera vez, se recuperó fuera de plazo). |

5. Contestación diligencias de embargo de cuentas.

Esta operación permite a las entidades contestar todas las diligencias de embargo de cuentas que tengan pendientes. El sistema devolverá, por cada diligencia contestada en la petición, el resultado de la contestación. Si el resultado de contestación ha sido erróneo se enviará un código de error, detallando el problema detectado. Si la contestación se ha grabado correctamente, en este caso creará una constancia de dicha contestación telemática indicando el certificado de acceso, la fecha de la contestación y el contenido de la respuesta.

Si una entidad envía una contestación con N diligencias, la Agencia Tributaria las procesará individualmente y en la respuesta se indicará el resultado individual de cada una. Es posible, por tanto, que en la respuesta de una contestación de diligencias haya diligencias que se hayan procesado correctamente y otras con error.

Si la Agencia Tributaria devuelve error en una diligencia, solo esta diligencia seguirá estando pendiente de contestar. Se podrá volver a contestar esta diligencia desde el servicio REST.

Cada diligencia enviada por la Agencia Tributaria contendrá hasta tres números de cuenta (IBAN) que corresponderán al mismo deudor y entidad de crédito. Cuando en las cuentas incluidas en la diligencia no se pueda trabar el total indicado en la misma, la entidad deberá extender el embargo a otras cuentas del mismo deudor y entidad, si éstas existen, con un máximo de diez cuentas en total.

Si habiendo actuado contra diez cuentas sin lograr la traba de la cantidad indicada en la diligencia, el deudor dispone de más cuentas en la misma entidad, se reflejará esta circunstancia en el campo «HayMasCuentas» informando el valor «S».

Para proceder a la identificación de la titularidad de las cuentas, las entidades tendrán que utilizar la información recogida en los tres campos de identificación del deudor proporcionados por la Agencia Tributaria, esto es, el NIF del deudor, el posible NIE o NIF anterior del deudor y/o el número de pasaporte. Para proceder a contestar la diligencia, la entidad siempre deberá consignar el NIF proporcionado por la Agencia Tributaria en el campo nifDeudor (pudiendo ser NIF o NIE) aunque la identificación del deudor se haya realizado por la entidad mediante la información contenida en cualquiera de los otros dos campos.

El campo «CodigoResultado» refleja el resultado del embargo que la entidad indica sobre cada cuenta informada en la diligencia. Podrá tomar los valores:

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

10. SITUACIÓN CONCURSAL.

12. TRABA REALIZADA EN DIVISAS.

13. TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN.

14. EMBARGO NO PROCEDENTE SEGÚN NORMATIVA VIGENTE.

Cuando en la diligencia enviada a la entidad se solicite el embargo de varias cuentas y se produzca la traba del importe total indicado en la diligencia en una o varias de estas cuentas, siendo innecesario actuar sobre el resto, el código de traba que corresponderá a las cuentas en las que se ha realizado traba será en cada caso el código de respuesta con traba de los anteriores y en aquellas sobre las que no se ha actuado será 00. Este será el único caso en que se acepte el código 00 (sin actuación).

Cabe destacar que la entidad puede realizar la traba en una cuenta con una única divisa distinta al euro, o se trate de una cuenta con varias divisas distintas al euro. En el primer caso, la entidad deberá aportar en la respuesta asociada a la cuenta en divisas, la divisa en la que se encuentra la cuenta, el importe en dicha divisa que se ha trabado, el tipo de cambio que se ha aplicado y el importe de la traba en euros. En el segundo caso, la entidad deberá aportar la información para los cuatro campos anteriores tantas veces como tipos de divisas tenga la cuenta en la que se realiza la traba.

5.1 Datos de la petición para contestación de diligencias de embargo de cuentas.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas que se quieren contestar. Para cada diligencia se tiene la siguiente información.

● Diligencia. Bloque de datos de cada diligencia.

● numeroDiligencia. Número de diligencia de embargo.

● nifDeudor. Campo que recogerá el NIF del deudor, es decir, NIF o NIE.

● importeTotalTrabado. Importe total acumulado trabado en la diligencia. Debe coincidir con la suma del importe trabado en cada cuenta. En céntimos de euro. Si la respuesta a la diligencia implica que no existe importe trabado, este campo se informará con valor cero.

● ListaCuentas. Bloque correspondiente al resultado para cada una de las cuentas incluidas en la diligencia. Se deben incluir todas las cuentas incluidas en la diligencia y además, si el deudor tuviera otras cuentas en la entidad, se deben incluir igualmente hasta un máximo de diez cuentas.

○ Cuenta. El bloque de información de cada cuenta es el siguiente:

□ cuentaIBAN. IBAN de la cuenta.

□ codigoResultado. Posibles valores descritos anteriormente.

□ importeTraba. Importe trabado en la cuenta. En céntimos de euro. Si no existe importe trabado, este campo se informará con el valor cero.

□ importeNoDisponible. Cuando la entidad conteste con un código de respuesta 04 (SALDO NO DISPONIBLE POR EMBARGO PREVIO) debe informar en este campo el importe no disponible para el embargo por la existencia de un bloqueo judicial o un embargo previo. En céntimos de euro. En cualquier otro caso, este campo no se informará ni se incluirá en la invocación al servicio.

□ infoAdicionalSaldo. Cuando la entidad conteste con un código de respuesta 07 TRABA CON DIFERENCIA ENTRE SALDO DISPONIBLE Y CONTABLE, debe informar en este campo el saldo contable de la cuenta. En céntimos de euro. Cuando la entidad conteste con un código de respuesta 13 TRABA REALIZADA EN CUENTA CON INGRESO DE SUELDO, SALARIO O PENSIÓN, debe informar en este campo el saldo disponible de la cuenta, en céntimos de euro. En cualquier otro caso, este campo no se informará ni se incluirá en la invocación al servicio.

□ fechaTraba: fecha de la traba en formato AAAAMMDD. Si no existe traba, este campo no se informará ni se incluirá en la invocación al servicio.

□ horaTraba: hora de la traba en formato HHMMSS. Si no existe traba, este campo no se informará ni se incluirá en la invocación al servicio.

□ InformacionDivisas. Bloque de información que recoge los datos relativos a Tipo de divisa, Importe de la traba en divisa y Tipo de cambio a fecha de la traba, por cada divisa de la cuenta. En el en caso de cuentas multidivisa en las que se haya aplicado la traba en euros, el bloque puede repetirse tantas veces como divisas tenga la cuenta multidivisa. En caso de que la información de la traba no corresponda a cuentas en divisas, todo este bloque de información no se informará ni se incluirá en la invocación al servicio.

■ tipoDivisa. Campo que recoge el tipo de divisa de la cuenta. El tipo de divisa se regirá según el código ISO 4217 de tres cifras.

■ importeTrabaDivisa. Importe de la divisa trabado.

■ tipoCambio. Campo que recoge el tipo de cambio aplicado en el momento de realizar la traba. Expresado en euros por divisa (Ej. 1 dólar = 0.85 euros).

○ existenciaMasCuentas. Indicador de si existen más cuentas de las incluidas en esta respuesta. Valores S/N (Sí/No).

5.2 Datos de la respuesta a la petición para contestación de diligencias de embargo de cuentas.

El resultado de la contestación será el mismo listado de diligencias de la entrada, indicando el resultado de la contestación para cada diligencia.

Los datos que se reciben como respuesta a la petición de contestación de diligencias de embargo de cuentas, son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– ListaDiligencias. Bloque de información correspondiente a la lista de diligencias de embargo de cuentas para las que se ha recibido respuesta. Para cada diligencia se tiene la siguiente información.

● Diligencia. Bloque de datos de cada diligencia.

○ numeroDiligencia. Número de diligencia.

○ resultado. Si la contestación se ha realizado correctamente el resultado será cero. En caso de producirse un error en la contestación, en el resultado se indicará el código de error que ha ocurrido. Ver los códigos de error en la contestación de una diligencia.

○ ListaAvisos. Aunque el procesamiento de la petición haya sido correcto y se ha grabado la respuesta de la diligencia, se puede dar la circunstancia en la que sea necesario incluir un aviso para la entidad. Ver los avisos posibles en la contestación de una diligencia.

□ codigoAviso. Código del aviso. Ver tabla a continuación con los posibles avisos.

□ descripcionAviso. Descripción del aviso que se envía a la entidad.

○ csv. CSV del documento justificante de la contestación de la diligencia.

○ fechaContestacion. Fecha de contestación de la diligencia. Con formato AAAAMMDD.

○ horaContestacion. Hora de contestación de la diligencia. Con formato HHMMSS.

5.3 Códigos de error en la contestación de una diligencia.

| Código | Descripción | Descripción del resultado |
| --- | --- | --- |
| 40 | Error al validar los datos proporcionados para contestar la diligencia. Los datos de entrada de la petición contienen datos incorrectos que impiden que se procese correctamente la contestación de la diligencia. | Se pondrá una descripción del error producido. |
| 43 | Error al procesar la contestación de la diligencia. Diligencia ya contestada previamente. | La situación actual de la diligencia impide que se conteste porque ésta ya ha sido contestada previamente. |
| 99 | Superado el límite de diligencias por petición. No se ha podido procesar la contestación por haberse superado el límite de diligencias por petición. | 990 - Superado el límite de diligencias por petición. |

5.4 Códigos de aviso en la contestación de una diligencia.

Determinadas circunstancias podrían dar lugar a situaciones que no constituyen un error, pero en las cuales se estima oportuno incluir un aviso para la entidad:

| Código | Detalle del aviso |
| --- | --- |
| 60 | Traba fuera de plazo. La traba se ha realizado fuera del plazo establecido. |
| 70 | Contestación fuera de plazo. La contestación se ha realizado fuera del plazo establecido. |

6. Recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Petición que permitirá a una entidad consultar los levantamientos de las diligencias de embargo de cuentas. Igual que en la operación de recogida de diligencias pendientes, la respuesta será paginada. En cada petición se devolverá un identificador para continuar recuperando los datos.

6.1 Datos de la petición para recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– codigoPagina. Campo opcional. Identificador de la petición. Se debe proporcionar el identificador en los casos en el que la respuesta del servicio esté paginada. Mediante el identificador de la petición se indicará al sistema la página que tiene que recuperar de la respuesta que se continúe recuperando levantamientos a partir de una petición anterior.

– fechaDesde. Campo obligatorio. Fecha desde la cual se buscarán levantamientos de la entidad gestora. Campo en formato AAAAMMDD. Se corresponde con la fecha de levantamiento de la diligencia.

– fechaHasta. Campo obligatorio. Fecha hasta la cual se buscarán levantamientos de la entidad gestora. Campo en formato AAAAMMDD. Se corresponde con la fecha de levantamiento de la diligencia. El intervalo de fechas delimitado por FechaDesde y FechaHasta no puede ser superior a un año.

– tipoPeticion. Campo opcional. En este campo se indica el tipo de levantamientos que se solicita en la petición. Valores posibles:

● P: Se obtienen solo los levantamientos pendientes de recuperar. Esta es la opción por defecto. Si no se informa este campo, se obtienen los levantamientos pendientes.

● R: Se obtienen los levantamientos recuperados previamente.

● T: Se obtienen todos los levantamientos, tanto los pendientes como los recuperados previamente.

6.2 Datos de la respuesta para recuperar las órdenes de levantamientos de diligencias de embargo de cuentas.

Los datos que se reciben ante una petición de levantamientos de diligencias de embargo de cuentas son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– DatosPagina. Bloque de información de la paginación de la respuesta.

● numeroTotalLevantamientos. Campo que recoge el número total de levantamientos de diligencias de embargo de cuentas que se obtienen con la petición.

● numeroTotalPaginas. Campo que recoge el número total de páginas o peticiones que será necesario realizar para recuperar los levantamientos.

● codigoPaginaSiguiente. Identificador de la petición, necesario para seguir recuperando el resto de levantamientos. Si el valor del identificador de la petición es vacío indica que ya no hay más levantamientos que recuperar.

● numeroLevantamientosPagina Número de levantamientos recuperados en la petición actual.

– ListaLevantamientos. Bloque de información correspondiente a la lista de levantamientos de cuentas pendientes de recuperar. El bloque de información correspondiente a cada levantamiento:

● Levantamiento. El bloque de información correspondiente a cada levantamiento:

○ recuperadoPreviamente. Indicador que permite determinar si el levantamiento se ha recuperado con anterioridad ya por el servicio o es la primera vez. Tomará los valores ‘S’ (Sí) o ‘N’ (No).

○ numeroDiligencia. Número de diligencia de embargo.

○ nifDeudor. Campo obligatorio que recogerá el NIF o NIE del deudor.

○ nifAdicionalDeudor. Campo opcional. Si este campo en el momento de la puesta a disposición de la diligencia estaba informado, en el levantamiento también irá informado recogiendo un identificador adicional al NIF que permita identificar al deudor, que será típicamente el NIE que el deudor tenía antes de un cambio a NIF.

○ pasaporteDeudor. Campo opcional. Si este campo en el momento de la puesta a disposición de la diligencia estaba informado, en el levantamiento también irá informado recogiendo un identificador adicional al NIF que permita identificar al deudor, que será el n.º de pasaporte utilizado por el deudor para la apertura de cuentas en la entidad. Tendrá un tamaño máximo de 20 caracteres.

○ razonSocialDeudor. Nombre o razón social correspondiente al NIF anterior.

○ importeEmbargo. En céntimos de euro.

○ importeTrabaDiligencia. Importe total trabado en la diligencia. En céntimos de euro.

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

7. Recuperar documentos a partir de CSV.

A través de esta petición, una entidad podrá recuperar un documento a partir de su CSV.

7.1 Datos de la petición de recuperación de documentos por CSV.

Los datos para realizar una petición son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Campo obligatorio. Código identificativo en el Registro del Banco de España de la entidad que actúa como transmisora. Cada entidad adherida deberá utilizar una entidad transmisora que podrá ser ella misma o cualquier otra entidad.

● codigoEntidad. Campo obligatorio. Código de la entidad adherida depositaria destinataria de las diligencias.

– csv. CSV solicitado.

El tipo de documentos que se podrán recoger mediante este servicio son: diligencias, levantamientos y constancias de contestación.

7.2 Datos de la respuesta a la petición de recuperación de documentos por CSV.

Los datos que se reciben ante una petición de recuperación de documentos por CSV son:

– DatosEntidad. Bloque de información relacionada con la entidad.

● codigoTransmisora. Código de la entidad transmisora informada en la petición.

● codigoEntidad. Código de la entidad adherida depositaria destinataria de las diligencias informada en la petición.

– Documento. Bloque de información relativo al documento asociado al CSV:

● csv. CSV que se ha solicitado.

● formato. Indica el tipo MIME del documento (por ejemplo, ‘application/pdf’).

● contenido. Campo con el contenido del documento codificado en Base64.

8. Códigos de respuesta utilizados en el intercambio telemático por los servicios REST.

A continuación, se indican los códigos de estado estándar HTTP (HTTP Status Code) usados en el intercambio de datos:

| Código de estado | Descripción |
| --- | --- |
| 200 | Petición procesada correctamente. |
| 400 | El servidor no puede procesar la petición porque hay un error en los datos de entrada. |
| 401 | Autentificación incorrecta. Acceso no autorizado a los datos. |
| 404 | Recurso no encontrado. |
| 500 | El servidor no puede procesar la petición por un problema en el sistema. |

8.1 Respuesta con códigos de estado 40x y 500.

Las respuestas con código de estado 40x o 500 son respuestas de un error producido en los datos enviados desde el cliente (códigos de estado 40x) o en el tratamiento de la petición en el servidor (código de estado 500). A continuación, se indica la relación de códigos de error que se devolverán en una respuesta con error:

| Código | Código de estado | Descripción del error |
| --- | --- | --- |
| 10 | 400 | Error al validar los datos de entrada de la petición. Los datos de entrada de la petición contienen datos incorrectos que impiden que se procese correctamente la petición. |
| 20 | 401 | Acceso no autorizado al servicio. El certificado electrónico usado en la petición no está autorizado para realizar trámites en representación de la entidad indicada. |
| 30 | 404 | No existe un documento con el CSV indicado |
| 50 | 500 | No se ha podido procesar correctamente la petición. Posibles causas: – Fallo de conexión a la base de datos. – Caída del sistema, etc. Si el error persiste, pónganse en contacto con los administradores del WS. |
