## Cuarto. Procedimiento.

1. Normas generales.

Los intercambios de información que, en aplicación de la presente Resolución, deban llevarse a cabo entre la Agencia Estatal de Administración Tributaria y las diferentes entidades de crédito serán efectuados de forma centralizada mediante el empleo de técnicas de remisión telemática de ficheros por teleproceso.

A tales efectos, cada entidad de crédito deberá utilizar una entidad transmisora (que puede ser ella misma o cualquier otra entidad).

Una entidad transmisora podrá dar servicio a varias entidades de crédito, con la única limitación de que para un mismo ciclo mensual todas las transmisiones de información correspondientes a una entidad de crédito se realizarán a través de la misma entidad transmisora.

A los efectos de lo establecido en la presente Resolución, se considerarán inhábiles los sábados y aquellas festividades que afecten a las localidades donde radique bien el Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria o bien la oficina desde la que cada entidad de crédito transmita los datos a la Administración Tributaria.

En aquellos casos en los que, debido a motivos técnicos, sea imposible para las entidades la conexión telemática con la Agencia Estatal de Administración Tributaria, deberán ponerlo en conocimiento del Departamento de Informática Tributaria a los efectos que pudieran resultar procedentes. Del mismo modo deberán actuar las entidades cuando los ficheros que les suministre la Agencia Estatal de Administración Tributaria contengan errores que impidan el correcto tratamiento por parte de aquéllas.

2. Fases del procedimiento.

2.1 Iniciación. El procedimiento se iniciará mediante la selección por la Agencia Estatal de Administración Tributaria de los deudores y las cuentas a la vista de las que aquéllos sean titulares.

Una vez obtenida dicha información, se seleccionarán la entidad y sucursal de la misma donde se encuentren abiertas las cuentas con el fin de obtener las diligencias de embargo correspondientes, sin que en ningún caso puedan simultanearse para un mismo deudor varias diligencias en la misma entidad.

2.2 Transmisión de las diligencias de embargo a las entidades. El Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria generará un fichero por entidad transmisora con las diligencias de embargo dictadas a nivel nacional para las entidades de crédito a las que aquélla dé servicio y que en ese ciclo mensual tuvieran diligencias y lo pondrá a disposición de dichas entidades transmisoras el último día de cada mes o el inmediato hábil posterior cuando aquél resulte inhábil. En la Comisión de seguimiento a que se refiere el apartado sexto de esta Resolución podrán acordarse periodicidades y plazos de puesta a disposición diferentes de los anteriores.

Cada entidad transmisora deberá recuperar la información contenida en el fichero de diligencias en el plazo de dos días hábiles a contar desde el siguiente al de su puesta a disposición.

El horario disponible para conexiones de las entidades con el Departamento de Informática Tributaria será el siguiente: de lunes a jueves desde las 8 a las 20 horas y los viernes desde las 8 a las 15 horas.

La recepción por parte de la entidad transmisora del fichero de diligencias supondrá el borrado del mismo y su sustitución por otro fichero con un único registro de control, que indicará que se ha realizado dicha recepción.

Cuando para una entidad transmisora no existan diligencias de embargo en algún ciclo mensual, al conectarse con el Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria, encontrará el registro de control correspondiente al último ciclo mensual finalizado.

Cada diligencia de embargo contendrá los siguientes datos:

a) NIF del deudor.

b) Nombre y apellidos o razón social del deudor.

c) Datos sobre el domicilio del deudor.

d) Número de diligencia de embargo.

e) Importe total a embargar.

f) Fecha de la diligencia de embargo.

g) Codificación de la cuenta o cuentas a embargar. Se consignarán los códigos de un máximo de tres cuentas a la vista por cada diligencia, todas ellas abiertas en la misma sucursal de la entidad de crédito.

A través de la sede electrónica de la Agencia Estatal de Administración Tributaria (https://www.agenciatributaria.gob.es) las entidades de crédito podrán obtener copias de las diligencias de embargo que se incluyen en los ficheros.

2.3 Traba. Antes de las 9 de la mañana del día siguiente a aquel en que la entidad de crédito (o, en su caso, su entidad transmisora) recupere el fichero de diligencias, deberá efectuarse la retención del importe a embargar si existe saldo suficiente o el total de los saldos en otro caso. Previo requerimiento de los órganos competentes de la Agencia Estatal de Administración Tributaria, la entidad de crédito estará obligada a justificar de forma fehaciente la fecha y hora en la que se ha producido la traba efectiva.

La entidad de crédito deberá efectuar la traba con respecto a las cuentas consignadas por la Agencia Estatal de Administración Tributaria en la diligencia de embargo. Cuando en dichas cuentas no existiera saldo disponible que cubra el importe total a embargar, la entidad extenderá el embargo a aquellas otras cuentas a la vista de titularidad del deudor que se encontrasen abiertas en la misma sucursal, hasta un máximo de seis cuentas por diligencia (incluidas las comunicadas por la Agencia Estatal de Administración Tributaria).

A los efectos de su posterior comunicación a la Agencia Estatal de Administración Tributaria, el resultado de las actuaciones se consignará por la entidad de crédito conforme a los siguientes códigos:

00 Sin actuación: Solo podrá utilizarse en aquellas cuentas sobre las que no se practique ninguna actuación, por haberse cubierto la totalidad del embargo en otras cuentas incluidas en la misma diligencia.

01 Traba realizada: Este código será utilizado en aquellas cuentas en las que se haya efectuado alguna retención, tanto por la totalidad del importe a embargar como por una parte del mismo.

02 NIF no titular de la cuenta comunicada por la Agencia Estatal de Administración Tributaria.

03 Inexistencia de saldo: Será utilizado cuando la cuenta tenga un saldo susceptible de embargo inferior o igual a tres euros.

04 Saldo no disponible: Será consignado en aquellos supuestos en los que exista saldo en la cuenta a embargar, pero éste no sea total o parcialmente disponible de acuerdo con la normativa vigente (existencia de otros embargos ordenados por órganos administrativos o judiciales con anterioridad a la recepción de la diligencia por la entidad…).

05 Cuenta inexistente o cancelada.

06 Otros motivos: Se utilizará cuando el embargo en la cuenta sea cero por una causa distinta a las reflejadas en el resto de los códigos.

07 Traba condicionada: Se utilizará cuando, por la práctica bancaria, el saldo contable de la cuenta sea mayor al disponible en el momento de efectuarse la traba.

En estos casos, la entidad retendrá, en todo caso, el importe del saldo contable. A estos efectos se entenderá que no forman parte del saldo contable los importes correspondientes a aquellas operaciones ejecutadas con anterioridad a la fecha en que deba realizarse la traba, siempre que dichas operaciones tengan carácter irrevocable.

08 Cuenta excluida del procedimiento: Será consignado cuando se incluyesen erróneamente por la Agencia Estatal de Administración Tributaria diligencias de embargo que se refiriesen a cuentas o depósitos que no estuvieran incluidos en el objeto de la presente Resolución.

09 Saldo pignorado: Se empleará en aquellos casos en los que el saldo de la cuenta a embargar se encuentre total o parcialmente afecto a pignoración debidamente constituida.

En estos casos, la entidad pospondrá la traba al momento en el que la Agencia Estatal de Administración Tributaria, de forma centralizada, ponga la diligencia de embargo a disposición de dicha entidad, de acuerdo con el apartado octavo de la presente Resolución.

10 Situación concursal: Será utilizado en aquellos supuestos en los que el deudor al que se refiere la diligencia de embargo se encuentre incurso en un proceso concursal.

En estos casos, la entidad pospondrá la traba al momento en el que la Agencia Estatal de Administración Tributaria, de forma centralizada, ponga la diligencia de embargo a disposición de dicha entidad, de acuerdo con el apartado octavo de la presente Resolución.

La entidad de crédito podrá entender no ordenada la traba cuando el importe susceptible de embargo en la cuenta sea inferior a 3 euros. En este caso, la entidad comunicará la traba a la Agencia Estatal de Administración Tributaria utilizando el código 03 (Inexistencia de saldo).

2.4 Transmisión de la información de trabas desde las entidades a la Agencia Estatal de Administración Tributaria. En el plazo de los cuatro días hábiles siguientes al de la fecha de recepción del fichero de diligencias, cada entidad transmisora transmitirá al Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria el fichero que contenga la información con el resultado de las trabas.

Cuando una entidad transmisora dé servicio a varias entidades de crédito, aquélla podrá transmitir individualmente el resultado de las trabas de cada una de ellas en el momento en que las tenga disponibles, sin que sea necesario esperar al resultado de todas las entidades de crédito de las que sea transmisora. En cualquier caso, el resultado de las trabas de la totalidad de las entidades de crédito deberá ser transmitido en el plazo anteriormente señalado.

2.5 Transmisión por la Agencia Estatal de Administración Tributaria a las entidades del resultado de la validación de información de trabas. Dentro de los dos días hábiles siguientes a la recepción del fichero de trabas por el Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria, éste pondrá a disposición de las entidades transmisoras el resultado de la validación de las trabas.

Dicha validación puede suponer la aceptación de las trabas o su rechazo por contener errores la información transmitida. En este último caso, la entidad dispondrá de dos días hábiles a contar desde el siguiente a la recepción del rechazo de la información para subsanar los errores detectados y transmitir de nuevo dicha información (que deberá contener nuevamente todas las trabas de ese envío para la entidad de crédito).

Cuando una entidad transmisora dé servicio a varias entidades de crédito, la aceptación o rechazo del envío de cada una de ellas es independiente.

Se entenderá que la aceptación de las trabas por la Agencia Estatal de Administración Tributaria se produce en la fecha en que el Departamento de Informática Tributaria ponga a disposición de la entidad que corresponda el resultado de la validación con la aceptación de la información.

2.6 Incorporación de la información de trabas a la Base de Datos de la Agencia Estatal de Administración Tributaria. Una vez aceptada la información de trabas transmitida por las diferentes entidades, el Departamento de Informática Tributaria, a través de la ejecución de los procesos informáticos diseñados al efecto, procederá a incorporar dicha información a las Bases de Datos de la Agencia Estatal de Administración Tributaria.

2.7 Levantamientos de embargo. En el caso de que en el plazo de veinte días naturales a contar desde el siguiente al que se produjo la traba fuera necesario levantar total o parcialmente algún embargo, la Agencia Estatal de Administración Tributaria remitirá la correspondiente orden de levantamiento a la entidad de crédito, la cual procederá a liberar la traba de la cantidad o cantidades indicadas en dicha orden.

Con carácter general, el envío de las órdenes de levantamiento se realizará diaria y centralizadamente por medios telemáticos, de acuerdo con el procedimiento y especificaciones que se recogen en el anexo IV de esta Resolución.

En caso de que la entidad de crédito no atendiese correctamente la orden de levantamiento de embargo recibida, será de su exclusiva responsabilidad cualquier perjuicio que pudiera causarse al deudor por tal motivo. Asimismo, las entidades responderán ante los deudores en aquellos casos en los que, sin causa justificada, no recuperen los ficheros de órdenes de levantamiento puestas a su disposición por la Agencia Estatal de Administración Tributaria en la forma y plazos que establece la presente Resolución.

En circunstancias excepcionales, y previa autorización del Departamento de Recaudación, el órgano de recaudación competente podrá remitir la orden de levantamiento a la entidad mediante fax o correo electrónico dirigido a la persona de contacto designada por la entidad de crédito en esta materia.

La Agencia Estatal de Administración Tributaria deberá poner el fichero con las órdenes de levantamiento de embargo a disposición de las entidades de crédito afectadas por las mismas (o, en casos excepcionales, remitir la orden de levantamiento) antes de las catorce horas y treinta minutos del vigésimo día natural contado a partir del siguiente al de la traba.

2.8 Ingreso en el Tesoro Público de las cantidades embargadas. Una vez transcurridos veinte días naturales desde el siguiente a la traba, la entidad de crédito procederá a abonar en cuenta restringida el importe de los saldos embargados, minorando, en su caso, las cantidades objeto de levantamientos realizados de acuerdo con las órdenes recibidas al efecto de los órganos de recaudación de la Agencia Estatal de Administración Tributaria.

La entidad efectuará el abono en la cuenta restringida «Tesoro Público. Cuenta restringida de colaboración en la recaudación de la Agencia Estatal de Administración Tributaria de liquidaciones practicadas por la Administración y otros ingresos no tributarios y de la Caja General de Depósitos» a que se refiere el artículo 5.2 c) de la Orden EHA/2027/2007, de 28 de junio, por la que se desarrolla parcialmente el Real Decreto 939/2005, de 29 de julio por el que se aprueba el Reglamento General de Recaudación, en relación con las entidades de crédito que prestan el servicio de colaboración en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria.

Sin perjuicio de las comprobaciones que posteriormente puedan realizar al respecto los órganos de recaudación de la Agencia Estatal de Administración Tributaria, en aquellos casos en los que la entidad de crédito hubiera efectuado trabas condicionadas (código 07), no se efectuará el ingreso en cuenta restringida, sin necesidad de recibir orden de levantamiento, de la parte del saldo trabado con dicho código (saldo contable) que, al finalizar el plazo señalado, no hubiese alcanzado la condición de disponible.

La operación de ingreso en el Banco de España de las cantidades embargadas y la presentación a la Administración Tributaria de la información de detalle de estos ingresos se efectuará según los plazos, forma y condiciones establecidos en los capítulos II y III de la Orden EHA/2027/2007, de 28 de junio, por la que se desarrolla parcialmente el Real Decreto 939/2005, de 29 de julio por el que se aprueba el Reglamento General de Recaudación, en relación con las entidades de crédito que prestan el servicio de colaboración en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria.

En el caso de que la Entidad de crédito no actúe como colaboradora en la gestión recaudatoria de la Agencia Estatal de Administración Tributaria, procederá a efectuar el ingreso de las cantidades embargadas a través de cualquiera de las Entidades de crédito que ostente esa condición.
