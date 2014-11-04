## Sexto. Funcionamiento del sistema de comunicación, ejecución y control del servicio de gestión de la demanda de interrumpibilidad.

6.1 Inicialización.

El SG-SCECI iniciará siempre el proceso de establecimiento del enlace TCP/IP.

Una vez establecido el enlace TCP/IP el SG-SCECI solicitará al EMCC el envío de su Certificado Digital. El SG-SCECI validará el Certificado recibido, informará al EMCC del resultado de la validación y finalizará el enlace TCP/IP en caso de tratarse de un Certificado no válido.

Una vez que se ha validado el Certificado del EMCC, el SG-SCECI solicitará al EMCC la siguiente información general:

– Identificación del EMCC: CUPS.

– Hora del equipo EMCC.

– Pmax (Potencia residual de referencia prevista en el artículo 10.3 b) de la Orden IET/2013/2013, de 31 de octubre).

– Psub (Potencia asignada en la subasta, de acuerdo a lo dispuesto en la Orden IET/2013/2013, de 31 de octubre, y en su normativa de desarrollo).

– Progh (Programa de consumo horario correspondiente a la hora siguiente conforme a lo dispuesto en el artículo 10.4 de la Orden IET/2013/2013, de 31 de octubre).

– Estado del EMCC: Fallo del equipo EMCC y fallo en las comunicaciones con el SG-SCECI desde la última solicitud de información general.

– Cuatro últimos valores de potencia activa media demanda cuarto horaria registrados por el maxímetro a que hace referencia el apartado 3.10.c)1 del presente procedimiento.

El SG-SCECI registrará la información recibida, validará el CUPS, los valores de Pmax y Psub, recibidos del EMCC contra su base de datos estructural. En caso de discrepancia finalizará la comunicación.

La comunicación entre SG-SCECI y el EMCC no se considerará establecida, a los efectos de lo indicado en el artículo 9.7 de la Orden IET/2013/2013, de 31 de octubre, hasta que se haya finalizado con éxito el proceso de inicialización que se describe en este apartado.

Dentro del proceso de actualización del Protocolo de Comunicación, el Operador del Sistema podrá introducir modificaciones en la información general solicitada para atender a nuevas necesidades o evolución del servicio.

6.2 Información periódica.

EL SG-SCECI solicitará al EMCC periódicamente, los valores del potencia activa instantánea demandada, en su caso generada, y potencia reactiva instantánea registradas por el sistema a que hace referencia el apartado Tercero. 3.10 c) 3.º. La periodicidad se definirá en el Protocolo de Comunicación y no podrá ser inferior a 4 segundos.

El SG-SCECI intercambiará periódicamente información para asegurar la sincronización, con resolución de segundos, de los relojes del EMCC y SG-SCECI. La periodicidad se definirá en el Protocolo de Comunicación y no podrá ser inferior a 32 segundos.

El SG-SCECI solicitará y validará con periodicidad horaria la información general a que se hace referencia en el apartado Sexto. 6.1, finalizando la comunicación en caso de discrepancia.

6.3 Información espontánea.

El EMCC, en cada respuesta al SG-SCECI, indicará, por los medios que se establezcan en el Protocolo de Comunicación, la existencia de información que desea notificar al SG-SCECI. En respuesta a esta indicación, el SG-SCECI solicitará la información al EMCC.

El EMCC deberá notificar al SG-SCECI la siguiente información:

– Estado del EMCC: Fallo del equipo y fallo de la comunicación con el SG-SCECI desde el último intercambio de información con el SG-SCECI.

– Activación del relé de deslastre por subfrecuencia.

– Existencia de un nuevo programa horario de consumo.

– Existencia de una modificación en los periodos de indisponibilidad.

– Cambios en las entradas digitales de reserva del apartado Tercero. 3.10 h) 2.º cuando se defina su función.

6.4 Programa de consumo medio horario de la instalación interrumpible.

El EMCC notificará al SG-SCECI el programa de consumo medio horario de la instalación para el mes siguiente con el formato establecido en el Protocolo de Comunicación. El último programa de consumo medio recibido antes de que expire el plazo establecido en la Orden IET/2013/2013, de 31 de octubre, será el programa de consumo válido. Cada programa de consumo enviado por el EMCC reemplazará completamente al anterior.

El Protocolo de Comunicación dispondrá de mecanismos para que los Proveedores del Servicio puedan consultar el último Programa de consumo aceptado por el SG-SCECI.

6.5 Periodos de indisponibilidad de la instalación interrumpible.

El EMCC notificará al SG-SCECI los periodos en los cuales la instalación interrumpible no estará disponible para la prestación del servicio de gestión de la demanda de interrumpibilidad. Esta notificación se podrá realizar con carácter mensual, en los plazos que se establezcan en el correspondiente Procedimiento de Operación.

Las indisponibilidades declaradas en el horizonte de un envío al SG-SCECI, reemplazarán a todas las indisponibilidades declaradas para el mismo horizonte en envíos anteriores. Se entenderá por horizonte de un envío, el periodo de tiempo desde el instante de inicio de la primera indisponibilidad hasta el instante final de la última indisponibilidad declaradas.

El SG-SCECI validará las indisponibilidades programadas recibidas del EMCC de acuerdo con los criterios que se establezcan en el correspondiente Procedimiento de Operación, aceptando y registrando únicamente aquellas que cumplan los criterios citados.

El Protocolo de Comunicación dispondrá de mecanismos para que los Proveedores del Servicio puedan consultar la última notificación de indisponibilidad aceptada por el SG-SCECI.

6.6 Programación y ejecución de una orden de reducción de potencia.

El SG-SCECI respetando los criterios establecidos en el Procedimiento de Operación por el que se regula el servicio de gestión de la demanda de interrumpibilidad, determinará los proveedores del servicio a los que solicitará una reducción de potencia, enviando a continuación a los equipos EMCC de dichos proveedores un preaviso de orden de reducción de potencia que incluirá:

– el instante de inicio de la orden de reducción de potencia,

– el instante de finalización de la orden,

– la opción de ejecución de las previstas en la Orden IET/2013/2013, de 31 de octubre,

– el valor de potencia residual de referencia definido en el artículo 10.3 de la Orden IET/2013/2013, de 31 de octubre,

– el identificar de potencia residual.

Los valores que tomarán dichas variables, se indican en la tabla siguiente:

| Opción de ejecución de las previstas en la Orden IET/2013/2013, de 31 de octubre | Potencia residual de referencia definida en Orden IET/2013/2013, de 31 de octubre | Tipo de reducción de los previstos en la Orden ITC/2370/2007, de 26 de julio | Máximo valor de potencia residual según Orden ITC/2370/2007, de 26 de julio | Identificador de potencia residual |
| --- | --- | --- | --- | --- |
| n/a | n/a | 1 | P50% | 0 |
| n/a | n/a | 1 | Pmax,1 | 1 |
| n/a | n/a | 2 | Pmax,2 | 1 |
| C | Pmax | 3 | Pmax,3 | 1 |
| B | Pmax | 4 | Pmax,4 | 1 |
| A | Pmax | 5 | Pmax,5 | 1 |

Al recibir la orden de reducción de potencia, el EMCC del proveedor del servicio deberá verificar su autenticidad y validez, y enviar un acuse de recibo al SG-SCECI, aceptando o rechazando, en su caso, la orden recibida.

El SG-SCECI, al recibir del EMCC el acuse de recibo aceptando la orden de reducción de potencia, una vez verificada la autenticidad y validez del acuse de recibo, enviará al equipo EMCC del proveedor una validación de la orden de reducción de potencia.

Al recibir la validación de la orden de reducción de potencia, el equipo EMCC del proveedor deberá verificar su autenticidad y validez, enviando un acuse de recibo al SG-SCECI, aceptando o rechazando en su caso la validación de orden de reducción de potencia recibida. El EMCC deberá de verificar que en el instante de recibir la validación se cumple lo siguiente:

| Opción de Ejecución. (Orden IET/2013/2013) | Instante de Inicio de la orden de reducción - Instante de recepción de la validación de orden (Tiempo de Preaviso mínimo) | Tipo de Reducción | Instante de Inicio de la orden de reducción - Instante de recepción de la validación de orden (Tiempo de Preaviso mínimo) |
| --- | --- | --- | --- |
| – | – | 1 | ≥ 2 horas |
| – | – | 2 | ≥ 2 horas |
| C | ≥ 120 minutos | 3 | ≥ 1 hora |
| B | ≥15 minutos | 4 | ≥ 5 minutos |
| A | ≥1 minuto | 5 | ≥ 1 minuto |

En caso contrario el EMCC deberá rechazar el preaviso de orden de reducción.

El instante de recepción de la validación de una orden de reducción en el EMCC, se considerará como el instante de envío de la orden de reducción de potencia a efectos de lo indicado en el apartado 10.3 a) de la Orden IET/2013/2013, de 31 de octubre.

Una vez que el equipo EMCC del proveedor del servicio envía el acuse de recibo aceptando la validación, la orden de reducción de potencia se considerará como preavisada y el proveedor del servicio deberá reducir su potencia consumida a un valor igual o inferior a la Potencia residual que corresponda.

Al alcanzar el instante de finalización de una orden de reducción, el EMCC notificará esta condición al SG-SCECI, el cual en respuesta solicitará el archivo de la orden de reducción. Este archivo contendrá toda la información descriptiva de la orden y los valores de potencia activa media registrados por el maxímetro integrador cincominutal del apartado Tercero. 3.10 c) 2.º del presente procedimiento, correspondientes al periodo desde el instante de inicio hasta el instante de finalización de la orden de reducción.

En caso de rechazo por parte del proveedor del servicio de una orden de reducción de potencia o su validación, el Operador del Sistema iniciará de nuevo el proceso de envío de la orden de reducción, modificando en su caso las características de la orden.

El Operador del Sistema, a través del SG-SCECI, realizará un Número Máximo de Reintentos con periodicidad igual al Tiempo de Espera para el envío de una orden de reducción de potencia o su validación, de los cuales no haya recibido acuse de recibo o que hayan sido incorrectamente rechazados por el EMCC. Una vez realizado el Número Máximo de Reintentos sin recibir el acuse de recibo aceptando una orden de reducción de potencia o su validación, se considerará definitivamente fallido el envío de la orden de reducción de potencia.

Los valores de Número Máximo de Reintentos y Tiempo de Espera, serán definidos en el documento del Protocolo de Comunicación.

Una vez que una orden de reducción está preavisada, el SG-SCECI podrá solicitar al EMCC el estado de la orden de interrupción de potencia así como, en su caso, la lista de órdenes de reducción que este último tuviera en curso.

6.7 Modificación o anulación de una orden de reducción de potencia.

El Operador del Sistema podrá modificar una orden de reducción de potencia antes del inicio del tiempo de preaviso mínimo que se indica en el apartado Sexto. 6.6.

El Operador del Sistema podrá anular en cualquier momento una orden de reducción de potencia, incluso si está en ejecución, en los términos establecidos en artículo 8.4 de la Orden IET/2013/2013, de 31 de octubre.

El proceso de modificación o anulación de una orden de reducción de potencia será el mismo que se ha descrito en el apartado Sexto. 6.6 para la programación de una orden de reducción de potencia.

6.8 Comunicaciones entre el Operador del Sistema y proveedores del servicio en caso de fallo del sistema de comunicaciones entre el EMCC y el SG-SCECI.

El Operador del Sistema, con carácter excepcional y teniendo en cuenta las necesidades de operación del sistema, podrá utilizar el correo electrónico o fax como medio alternativo de comunicación.

El proveedor del servicio indicará al Operador del Sistema, una o varias direcciones de correo electrónico específicas para este propósito, así como un número de fax según lo dispuesto en el apartado Tercero. 3.11 del presente procedimiento.

6.9 Pruebas de los equipos y del sistema de interrumpibilidad.

A petición de un proveedor del servicio o del Operador del Sistema, se podrán efectuar pruebas de prestación del servicio de gestión de la demanda de interrumpibilidad.

El inicio del periodo de pruebas y la forma de operar en modo de prueba, deberá contar con el acuerdo previo de las partes. En cualquier caso, las pruebas deberán realizarse en un plazo no superior a 30 días laborables, una vez recibida la solicitud.

El sistema de comunicación, ejecución y control del servicio de gestión de demanda de interrumpibilidad (SCECI) deberá estar capacitado para que se puedan llevar a cabo pruebas de funcionamiento de las distintas modalidades de reducción de potencia.

El proceso de pruebas de los equipos EMCC, incluirá todos los componentes del sistema: SG-SCECI, sistema de comunicaciones y EMCC, salvo la activación de los contactos de los apartados Tercero. 3.10. g) 1.º, 2.º y 3.º y sus equivalentes en el bus de comunicaciones del 3.10. i).

Los equipos EMCC podrán incorporar la posibilidad de activar, en modo prueba, los contactos de los apartados Tercero. 3.10. g) 1.º, 2.º y 3.º y sus equivalentes en el bus de comunicaciones del apartado Tercero. 3.10. i). En este caso, el proveedor del servicio o el Operador del Sistema deberán indicar explícitamente, al solicitar una prueba, si esta incluye o no la activación de dichos contactos. Esta condición deberá quedar registrada en el equipo EMCC.

En el registro histórico del Operador del Sistema, quedarán registradas todas las señales de prueba, con indicación explícita del solicitante, bien sea el propio prestador del servicio o el Operador del Sistema.

Tras la ejecución por el Operador del Sistema de la prueba solicitada, éste emitirá un informe en el que se reflejen las incidencias detectadas así como el origen de las mismas: comunicaciones, equipos, etc., según los criterios que se hubieran seleccionado para llevar a cabo la prueba.

Las órdenes de reducción de potencia enviadas por el Operador del Sistema en modo prueba no se contabilizarán, en ningún caso, a efectos del cómputo de órdenes de reducción establecido en el artículo 5.5 de la Orden IET/2013/2013, de 31 de octubre.
