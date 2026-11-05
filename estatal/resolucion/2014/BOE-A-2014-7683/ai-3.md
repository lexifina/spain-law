## APÉNDICE III

## Descripción códigos estados ecs y condiciones para modificar las declaraciones de exportación

El régimen de exportación se ultima con la salida efectiva de las mercancías del territorio aduanero de la Unión.

A. Definiciones.

Aduana de exportación: la aduana que registra, admite y despacha la declaración de exportación.

Aduana de ubicación de la mercancía: la aduana de control del recinto o almacén autorizado donde se presenta la mercancía cuando se realiza la declaración de exportación. Cuando no coincide con la Aduana de exportación se tratará de un despacho centralizado para lo que el operador tiene que estar expresamente autorizado.

Aduana de salida: la aduana que, de acuerdo con el artículo 793 del Reglamento 2454/93, realiza el control de salida de la mercancía.

‒ Salida directa: cuando coincidan la Aduana de ubicación y la Aduana de salida.

‒ Salida indirecta: cuando la Aduana de ubicación de la mercancía y la Aduana de salida, según se ha declarado en la casilla 29, son distintas

ECS: (Export Control Systems) Aplicación de la Unión Europea para el control de aquellas exportaciones en las que intervienen aduanas de distintos Estados miembros. Está basada en mensajes entre las aduanas implicadas. Por extensión se utiliza el término para referirse al estado de la declaración de cualquier exportación respecto a su despacho por la Aduana de exportación y a la salida del territorio aduanero de la Unión de la mercancía y su control por la Aduana de salida.

EAL: Mensaje nacional mediante el cual el operador comunica a la aduana de salida que la mercancía se encuentra en su recinto y solicita autorización de salida para la misma.

B. Estados de la exportación en caso de salida directa.

| PL | Pendiente de despacho. | La declaración ha sido registrada y admitida y se encuentra pendiente de despacho por la aduana de exportación. |
| --- | --- | --- |
| DS | Despachada. | La declaración ha sido despachada por la aduana y puede ser embarcada. |
| IV | Invalidada. | No existe constancia aceptable de la salida de la mercancía del territorio aduanero de la Unión. |
| AN | Anulada. | A petición del operador. |
| SA | Salida efectiva. | Estado final: la mercancía ha salido del TAU. |

DS Despachada.

Una vez que la declaración es despachada, bien automáticamente (asignada a circuito verde) o bien por el actuario (circuitos naranja o rojo), las declaraciones de exportación con salida directa quedan en estado DS. Significa que su embarque está autorizado.

En este caso no es necesario la impresión del DAE ya que la mercancía no tiene que ser presentada en otra aduana.

Si por algún motivo esta declaración se presentara en una aduana de otro Estado miembro, ésta podrá solicitar el envío del mensaje de aviso anticipado. En ese momento la exportación pasará al estado correspondiente como salida indirecta y podrá realizarse la gestión de salida normal.

AN Anulada.

A solicitud del operador puede anularse la declaración de exportación, excepto que se encuentre pendiente de despacho. Este estado es irreversible.

IV Invalidada.

Como consecuencia de una revisión realizada por Aduana, el operador no ha podido justificar la salida real de la mercancía por lo que la declaración es invalidada. El régimen de exportación no ha sido ultimado correctamente y se considera no efectuada. Si se trata de una reexportación de mercancía, la Aduana deberá realizar la liquidación de derechos correspondientes. Este estado es irreversible.

SA Salida efectiva.

Estas declaraciones pasarán automáticamente a este estado, bien por su inclusión en un manifiesto de carga marítimo o bien porque se den las condiciones previstas cuando se trate de un recinto aéreo.

La Aduana también podrá dar salida manual a estas declaraciones.

C. Estados de la exportación en caso de salida indirecta.

| PL | Pendiente de despacho. | La declaración ha sido registrada y admitida y se encuentra pendiente de despacho por la aduana de exportación. |
| --- | --- | --- |
| DE | Despachada. | Exportación con salida indirecta, ha sido despachada por la aduana de exportación y está pendiente de su tramitación en la aduana de salida. En este momento se emite el mensaje a la aduana de salida con los datos de la exportación. |
| RE | Recibido. | Se ha declarado la recepción de la mercancía en la aduana de salida y está pendiente de reconocimiento por parte de la aduana. No está autorizada todavía la salida |
| RQ | Solicitado a la UE. | La aduana de salida no tiene información de esa exportación de otro EM. Se pide, mediante un mensaje, el envío de esa información y todavía no ha res uesta. |
| RZ | Desvío rechazado. | La aduana de salida no tiene información de esa exportación. Se ha solicitado información a la aduana de exportación y la respuesta es que no es correcto. |
| RO | Recibido en otro país. | La aduana de exportación comunica a la aduana de salida prevista que la exportación ha salido por otra aduana. |
| PS | Pendiente de salida. | El mensaje EAL se ha admitido o la declaración ha sido recibida manualmente por la aduana de salida, se ha despachado y ha sido autorizada la salida de la mercancía (ver artículo 793.bis apartado 5. |
| ST | Parada. | Reconocida la mercancía por la Aduana, no procede autorizar la salida por no corresponder esta con lo declarado en la exportación (ver artículo 793.bis apartado 5. |
| AN | Anulada. | A solicitud del operador. |
| IV | Invalidada. | Estado final del procedimiento de búsqueda cuando no existe constancia aceptable de la salida de la mercancía del territorio aduanero de la Unión artículo 796 sexies. |
| SA | Salida efectiva. | Estado final: la mercancía ha salido del TAU. |

1. En la aduana de exportación.

DE Despachada.

Una vez despachada la declaración por la aduana de exportación (automáticamente o por el actuario) queda en estado DE y, por tanto, pendiente de su tramitación en la aduana de salida. En este momento se emite el mensaje IE501 a la aduana de salida declarada en la casilla 29 de la declaración con los datos de la exportación y deberá imprimirse el DAE.

En este estado la declaración no puede ser embarcada ya que no ha sido autorizada la salida.

Modificaciones.

Si la aduana de salida es de otro Estado miembro nunca debe modificarse esta exportación, ya que el mensaje con la información de la declaración ya ha sido enviado a la aduana de salida y la aplicación ECS no contempla mensajes de modificación. Si fuera necesario, deberá solicitarse la anulación de la declaración emitida y hacer una nueva. En la nueva deberá incluirse el código 1224 con el MRN de la declaración anulada.

Si la aduana de salida es también nacional pueden realizarse modificaciones por errores de hecho.

AN Anulada.

A solicitud del operador puede anularse la declaración de exportación, excepto que se encuentre pendiente de despacho.

IV Invalidada.

Superado el plazo de 150 días previsto en el artículo 796 sexies del Reglamento (CEE) n.º 2454/1993 si el operador no ha podido justificar la salida real de la mercancía la declaración es invalidada. El régimen de exportación no ha sido ultimado correctamente y se considera no efectuada. Si se trata de una reexportación de mercancía, la Aduana deberá realizar la liquidación de derechos correspondientes.

2. En la aduana de salida (cuando ésta es nacional).

La mercancía y el DAE deben ser presentados en la aduana de salida mediante el mensaje EAL de acuerdo a lo previsto en el apartado 6.5.1 de esta Resolución o en la oficina de la aduana para su recepción manual. La declaración quedará en uno de estos estados:

PS Pendiente de salida.

El mensaje ha sido admitido o ha sido realizada la recepción manual y se ha asignado un circuito verde. También se llega a este estado una vez despachada por la Aduana y autorizada la salida. El operador debe imprimir la autorización de salida y la mercancía puede ser embarcada.

RE Recibido.

El mensaje ha sido admitido o ha sido realizada la recepción manual y ha sido asignado a un circuito rojo. La Aduana realizará las comprobaciones necesarias de acuerdo a lo previsto en el artículo 793 bis del Reglamento (CEE) n.º 2454/1993. Una vez comprobada la mercancía, la Aduana incluirá las diferencias detectadas, si las hubiera, y cambiará el estado de la declaración a PS o a ST si no autoriza la salida (ver artículo 793.bis apartado 5 del mencionado Reglamento).

RQ Solicitado a la UE.

La aduana de salida no tiene información de esa exportación de otro EM. Nuestra aplicación informática contesta al mensaje EAL pidiendo que vuelva a enviarse más tarde y mientras genera un mensaje para la aduana de exportación solicitando el envío de esa información. La declaración queda en este estado mientras no se recibe respuesta de la aduana de exportación.

El operador debe reenviar el mensaje transcurrido 1 hora. Si seguimos sin respuesta deberá presentar el DAE en la Aduana para que ésta realice las comprobaciones oportunas, vise el DAE si todo es correcto y autorice la salida.

El compromiso es que la respuesta del otro Estado miembro tarde menos de 30 minutos. Sin embargo no es inhabitual que lleguen respuestas transcurridas horas e incluso días. Pasados unos días la Aduana podrá volver a intentar gestionar la salida a través de la aplicación ECS. Si no lo consigue, avisará de dicha contingencia al servicio de helpdesk, que avisará al país correspondiente de que el visado de salida se ha realizado en el DAE.

RZ Desvío rechazado.

(Continuación de un estado RQ) La respuesta de la aduana de exportación es que ese MRN no existe, o que ya se ha producido la salida, u otro motivo de error. La aduana debe comprobar la mercancía y comunicar, en su caso, esta incidencia al servicio de helpdesk y, según las circunstancias, autorizar la salida de la mercancía.

El servicio de helpdesk pedirá información al Estado miembro de que se trate y trasladará la respuesta a la aduana.

RO Recibido en otro país.

La aduana de exportación ha comunicado a la aduana de salida prevista que la exportación ha salido por otra aduana.

SA Salida efectiva.

La Aduana de salida ha comprobado la salida efectiva de la mercancía e informa de ello mediante el mensaje «Resultados de salida» a la Aduana de exportación. Si las salidas fueran parciales, sólo se enviará el mensaje cuando hubiera salido la totalidad de la mercancía.

Los declarantes de las exportaciones con salida directa y los declarantes de los mensajes EAL son responsables de comunicar a la aduana la no salida de la mercancía.

D. Modificación de declaraciones de exportación.

Se efectuará por el operador la subsanación electrónica de los errores de hecho cometidos en las declaraciones de exportación en las siguientes condiciones:

a) No se trate de un DUA acogido a los beneficios de la restitución.

b) No haya superado los 90 días desde su admisión.

c) El régimen debe ser de exportación definitiva, es decir, código 10 cuando se trate del procedimiento normal (casilla 1.2, código A). En declaraciones simplificadas (casilla 1.2, código «C») podrán modificarse también cuando el régimen sea 31.

d) Haya obtenido levante automático, es decir, haya sido asignada a circuito verde en la aduana de exportación.

e) El estado sea:

‒ DE sólo si la aduana de salida es nacional y no ha sido solicitada por una aduana extranjera mediante un mensaje IE503. En ningún caso puede ser modificada una exportación, ni de forma electrónica ni por la Aduana, cuyos datos se hayan enviado a una aduana de otro Estado miembro mediante un IE501 o un IE503. La aplicación ECS no contempla ningún mensaje de modificación. En su caso, sólo es posible la anulación y la realización de una nueva declaración en la que deberá incluirse el código 1224, en la casilla 44, con el MRN de la declaración anulada.

‒ SA, salvo que este estado lo haya obtenido por una declaración de tránsito.

‒ SV, DS o SD.

f) No haya sido revisada en la aduana de salida o esté pendiente de revisar.

g) No son modificables: el declarante, la aduana de salida, la descripción de la mercancía ni la casilla 37.

h) No puede modificarse para solicitar restitución o añadir códigos adicionales de restituciones.

i) No pueden añadirse partidas.

El mensaje de modificación tendrá una de las siguientes respuestas:

‒ Rechazado porque incumple alguna de las condiciones anteriores;

‒ Aceptado modificándose el DUA de forma automática;

‒ Aceptado pero pendiente de revisión por la aduana. En este caso el operador debe justificar en la Aduana la modificación solicitada. No podrá volver a modificarse una exportación que tenga pendiente la revisión de una modificación.

Fuera de los supuestos anteriores, en el caso de que proceda realizar una modificación de la declaración de exportación, ésta se efectuará por la Aduana correspondiente.

E. Comunicación de no salida del territorio de la Unión de la mercancía declarada de exportación.

La comunicación prevista en el artículo 792 bis del Reglamento (CEE) n.º 2454/1993, apartado 1.º podrá ser realizada por el interesado en Sede electrónica cuando la mercancía despachada de exportación no haya salido del territorio de la Unión.

Esta solicitud de anulación podrá utilizarse también cuando se trate de corregir errores de hecho de una declaración con salida indirecta mediante su sustitución por otra.

> Se modifica el título del apartado E por el apartado primero.23 de la Resolución de 14 de enero de 2016. Ref. BOE-A-2016-646
