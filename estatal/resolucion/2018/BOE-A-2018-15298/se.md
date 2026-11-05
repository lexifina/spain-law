## Segundo.

Modificar la Resolución de 6 de octubre de 2014, por la que se aprueba el modelo de datos del sistema de monitorización de la información correspondiente a los registros de operaciones de juego, en los siguientes términos:

1. En el apartado 2 («Definiciones») se modifica el apartado «Activación del registro de usuario», que queda redactado del siguiente modo:

«Activación del registro de usuario.

La activación del registro de usuario es el proceso a través del cual el operador habilita al usuario para poder participar en el juego, toda vez, que se han realizado las verificaciones establecidas por la normativa de juego.»

2. El apartado 3.3 («Periodicidad») queda redactado del siguiente modo:

«3.3 Periodicidad.

La periodicidad del reporte de la información para cada tipo de registro se indica en la siguiente tabla:

![imagen](https://www.boe.es/datos/imagenes/disp/2018/302/15298_5496.png)

El envío al almacén de los registros de periodicidad diaria, debe producirse antes de las 4 a.m. del día siguiente al día sobre el que se está informando.

El envío al almacén de los registros de periodicidad mensual, debe producirse antes de las 23:59 del primer día del mes siguiente.»

3. En el apartado 3.4.1 («Registro de usuario detallado (RUD)»), en el apartado «Contenido del registro», el epígrafe «Datos de verificación de identidad», queda redactado del siguiente modo:

«– Validación del SVDI. Tomará valor “Sí”, si se ha usado el Sistema de Verificación de Identidad de la DGOJ y se ha obtenido verificación positiva, o “No” en caso contrario.

– Fecha en la que se ha verificado positivamente por primera vez la identidad del usuario a través del SVDI.

– Validación documental. Tomará valor “Sí”, si se ha realizado la verificación de usuario documentalmente y dicha verificación es positiva, o “No” en caso contrario.

– Fecha en la que se ha verificado positivamente por primera vez la identidad del usuario a través de la verificación documental.»

4. En el apartado 3.4.5, («Cuenta de juego detallada (CJD)»), en el epígrafe rubricado «Contenido del registro», los apartados donde se describen los «Depósitos del participante» y las «Retiradas del participante» quedan redactados de la siguiente manera:

«– (+/-) Depósitos del participante, desglosado por fecha y medio de pago, de acuerdo a la clasificación de tipos de medio de pago establecida en el epígrafe “Tipos de medios de pago” de esta Resolución.

Se reflejarán con signo positivo los importes depositados por los participantes y con signo negativo las posibles anulaciones o ajustes realizados.

Para cada una de las operaciones de depósito realizadas por el jugador, se incluirán además:

– IP: dirección IP del dispositivo del jugador desde el que se conecta con la plataforma de juego, puede ser IPv4 o IPv6.

– Tipo de dispositivo: desde el que se produce la conexión (móvil, PC, tablet, terminal fijo u otro).

– Id dispositivo: identificador del dispositivo desde el que se realiza la conexión.»

«– (+/-) Retiradas del participante, desglosado por fecha y medio de pago, de acuerdo a la clasificación de tipos de medio de pago establecida en el epígrafe “Tipos de medios de pago” de esta Resolución.

Se reflejarán con signo negativo los importes retirados por los participantes de su cuenta de juego y con signo positivo las posibles anulaciones o ajustes realizados.

Para cada una de las operaciones de retirada realizadas por el jugador, se incluirán además:

– IP: dirección IP del dispositivo del jugador desde el que se conecta con la plataforma de juego, puede ser IPv4 o IPv6.

– Tipo de dispositivo: desde el que se produce la conexión (móvil, PC, tablet, terminal fijo u otro).

– Id dispositivo: identificador del dispositivo desde el que se realiza la conexión.»

5. El apartado 3.4.10 [«Registros de juegos (JUT, JUD)»], el epígrafe «Datos genéricos comunes a todos los juegos» queda redactado del siguiente modo:

«Datos genéricos comunes a todos los juegos.

La información a transmitir es la siguiente (se incluye el signo más probable):

– Identificador del juego: apuesta, partida, mano, torneo, concurso, sesión.

– Descripción del juego.

– Tipo de juego.

– Fecha/hora de inicio (apuesta, partida, mano, torneo, concurso, sesión).

– Fecha/hora de fin (apuesta, partida, mano, torneo, concurso, sesión).

– Juego en red: sí/no.

– Juego aplazado: sí/no (en el caso de juegos por sesión no debe ser cumplimentado).

– Juego anulado: sí/no (en el caso de juegos por sesión no debe ser cumplimentado).

– Juego suspendido: sí/no (en el caso de juegos por sesión no debe ser cumplimentado).

– Totales.

– Desglose a nivel de jugador:

• IP: dirección IP del dispositivo del jugador desde el que se conecta con la plataforma de juego, puede ser IPv4 o IPv6.

• Tipo de dispositivo: desde el que se produce la conexión (móvil, PC, tablet, terminal fijo u otro).

• Id dispositivo: identificador del dispositivo desde el que se realiza la conexión.

En el caso de juegos con liquidez internacional, el operador solo reportará los datos de los jugadores del dominio “.es”.»

6. El apartado 3.4.10 [«Registros de juegos (JUT, JUD)»], en el epígrafe «Datos específicos a cada tipo de juego», se añade al final del párrafo rubricado «Apuestas» un nuevo punto:

«– Cuota: Valor de la cuota de la apuesta (en valor decimal) en el momento en que es aceptada por el jugador.»

7. El apartado 3.4.12 «Catálogo de Eventos (CEV)» queda redactado de la siguiente manera:

«Información en catálogo de eventos.

Datos normalizados de los eventos que componen la oferta de apuestas del operador. Recogerá todos los nuevos eventos o actualizaciones sobre eventos reportados previamente sobre los que el operador ha comercializado apuestas en el periodo, independientemente que dichos eventos hayan finalizado o no.

Operadores obligados.

Los operadores que comercializan apuestas.

Periodicidad.

– Diaria: Diariamente se incluirá la información de los eventos nuevos o que hayan sido modificados en el día.

– Mensual: Mensualmente se incluirá la información de todos los eventos reportados durante el mes, tanto las altas como las modificaciones. En el caso de haber varias modificaciones en el mes para el mismo evento, se reportará la información de la última actualización.

Datos del catálogo.

El catálogo contendrá los siguientes datos:

– Identificador del evento.

– Descripción del evento.

– Tipo de evento. Deportivo, hípico u otras apuestas.

– Deporte: se identificará el deporte, siguiendo la clasificación oficial publicada en la web de la DGOJ, que contiene el listado normalizado de deportes utilizados por los operadores en sus programas de apuestas. Ejemplo: “6” para el “béisbol” o “9” para el deporte “boxeo”.

– Competición: Las apuestas identificarán la competición. Este campo es obligatorio en caso de que el evento pertenezca a una competición deportiva.

– Fecha de inicio del evento.

– Fecha de fin del evento, o fecha aproximada si se desconoce en el momento de reportar.

– Actualizado. Campo booleano que informará si el evento reportado es nuevo (‘N’) o es una actualización de un evento reportado en un CEV de un mes previo (‘S’).

Controles principales.

Todos los eventos reportados en las apuestas mediante un identificador de evento deberán estar recogidos en el catálogo correspondiente. No debe haber eventos duplicados, en caso de reportar un duplicado se entiende que es una actualización de los datos de un evento previo y por tanto debe ser señalizado con el campo actualizado = ’S’ o será considerado erróneo.»

8. En el apartado 3.5.1.1 «Registro RUD: Registro de usuario detallado», las entradas del cuadro relativas a la verificación del jugador (VSVDI, FVSVDI, VDocumental y FVDocumental) quedan redactadas del siguiente modo:

«VSVDI: Verificación del SVDI. Tomará valor S (Sí), si se ha usado el Sistema de Verificación de Identidad de la DGOJ y se ha obtenido verificación positiva, o N (No) en caso contrario.

FVSVDI: Fecha de la primera verificación positiva en el SVDI.

VDocumental: Verificación documental. Tomará valor S (Sí), si se ha realizado la verificación de usuario documentalmente y ha resultado positiva, o N (No) en caso contrario.

FVDocumental: Fecha de la primera verificación documental positiva.»

9. En el apartado 3.5.2.1 «Registro CJD: Cuenta de juego detallada», los apartados del cuadro relativos a «Depósitos» y «Retiradas» quedan redactados de la siguiente forma:

«Depósitos: Se consignará el total del importe en euros depositado durante el período, así como cada uno de los depósitos realizados, indicando la fecha del depósito, el código del tipo de medio de pago utilizado –basado en la lista de medios de pago incluida en el apartado «Tipos de medios de pago»–, el proveedor del medio de pago, el importe, la IP desde la cual se ha realizado la operación, el tipo de dispositivo y su identificador.

![imagen](https://www.boe.es/datos/imagenes/disp/2018/270/15298_5564.png)

Retiradas: Se consignará el total del importe en euros retirado durante el período, así como cada una de las retiradas realizadas, indicando la fecha de la operación, el código del tipo de medio de pago utilizado –basado en la lista de medios de pago incluida en el apartado «Tipos de medios de pago»–, el proveedor del medio de pago, el importe, la IP desde la cual se ha realizado la operación, el tipo de dispositivo y su identificador.»

10. En el apartado 3.5.4.1 [«Datos genéricos comunes a todos los juegos (JUT y JUD)»], el epígrafe «Datos de juego desglosados (JUD)» queda sustituido por el siguiente:

«Datos de juego desglosados (JUD).

Identificador del juego: Identificador único del suceso que genera la obligación de informar al SCI. El suceso depende del tipo de juego:

– Apuestas: cada combinación de eventos y hechos sobre los que el que el jugador realice la apuesta.

– Póquer cash y Punto y Banca: cada mano.

– Póquer torneo: cada torneo.

– Bingo: cada partida de bingo.

– Concursos: cada concurso.

– Ruleta, Blackjack, Juegos Complementarios y máquinas de azar: cada sesión.

Fecha/hora de fin: Fecha y hora del final del suceso que genera la obligación de informar al SCI. Esta Fecha debe corresponderse a la misma Fecha/hora de fin reportada en el fichero JUT para el mismo Identificador de juego.

Desglose a nivel de jugador:

– (-) Participación.

– (+) Premios.

– (+) Premios en especie, valoración monetaria.

– Desglose de los premios en especie: descripción y valoración del premio (+).

– IP.

– Dispositivo [PC; MO (móvil); TB (tablet); TF (terminal fijo); OT (otros)].

– Id dispositivo.

11. En el apartado 3.5.4.2 («Datos específicos de apuestas») el epígrafe «A nivel de desglose por jugador se contemplan» queda redactado del siguiente modo:

«A nivel de desglose por jugador se contemplan.

TicketId: Ticket obtenido por participante una vez cerrada la apuesta.

Fecha y hora de apuesta: Fecha y hora en la que jugador realiza la apuesta.

Relación de apuestas cruzadas: Se deberá indicar si se trata de un reto o no. Se considera que hay un reto cuando el apostante conoce a la persona contra la que está apostando.

Se incluirá además una lista de tickets asociados a cada cruce:

![imagen](https://www.boe.es/datos/imagenes/disp/2018/270/15298_5623.png)

Cuota: Valor de la cuota de la apuesta en el momento en que es aceptada por el jugador.»

12. En el apartado 3.5.6 («Registro de Catálogo de eventos»), se incluirá una última fila en la tabla con el siguiente texto:

«Actualizado: S/N.

El campo es opcional, si no se reporta implica que el evento es nuevo. En caso de ser una actualización de un evento previamente reportado, el campo es obligatorio, y debe ser reportado con valor ‘S’.»

13. El apartado 3.5.7.2 («Estado del jugador») se sustituye por el siguiente:

«3.5.7.2 Estado del jugador.

El «estado» del jugador está compuesto por dos campos:

EstadoCNJ, en el que se pide al operador diferenciar entre:

– A: Activo. Refleja el estado en el que el jugador se encuentra debidamente identificado y verificado documentalmente.

– PV: Pendiente de verificación documental. Refleja el estado de un jugador residente, cuya identificación no ha sido cotejada fehacientemente mediante un sistema de verificación documental.

– S: Suspendido. Refleja el estado del jugador que, tras dos años de inactividad ininterrumpidos, el operador ha optado por suspender.

– C: Cancelado. Refleja el estado del jugador que, transcurridos cuatro años desde su suspensión, ha sido cancelado.

– SC: Suspendido cautelarmente. Refleja el estado del jugador suspendido cautelarmente por el operador por sospecha de comportamiento colusorio o fraudulento o por haber permitido la utilización del registro de usuario por terceros.

– AC: Anulación contrato. Refleja el estado del jugador que, estando suspendido cautelarmente, el operador haya considerado probado que el participante ha incurrido en fraude, colusión o puesta a disposición de terceros de su propia cuenta, y haya procedido a resolver unilateralmente el contrato.

– PR: Prohibición subjetiva. Refleja el estado del jugador sujeto a cualquiera de las prohibiciones subjetivas establecidas en el artículo 6 de la Ley 13/2011 (menores, inscritos en el RGIAJ, vinculados,...).

– AE: Autoexcluido. Refleja el estado del jugador que voluntariamente ha decidido autoexcluirse del juego ofertado por el operador.

– O: Otros. Resto de situaciones en que pueda encontrarse un jugador y no estén incluidas en ninguna de las anteriores.

EstadoOperador, en el que el operador introducirá el nombre del estado tal y como se denomina en su plataforma.»

14. En el apartado 4.2 («Estructura de directorios»), epígrafe «Niveles 3, 4, 5 y 6», se modifica el párrafo «JU: Juego», quedando redactado del siguiente modo:

«JU: Juego.

– <AAAAMMDD>: Día en curso:

• JUT: Juego (totales): Subcarpeta para cada tipo de Juego (según lista del apartado “Tipo de juego”).

• JUD: Juego (por jugador): Subcarpeta para cada tipo de Juego (según lista del apartado “Tipo de juego”).

– Anteriores.

– Mensual:

• JUA: Ajustes de apuestas.

• CEV: Catálogo de eventos (mensuales).

– Diario:

• CEV: Catálogo de eventos (diarios).»

15. En el apartado 4.3 («Empaquetado de los datos de juegos») se modifica el segundo párrafo, que queda redactado de la siguiente manera:

«El nivel 4 para los juegos tendrá una carpeta para los ficheros de periodicidad mensual, otra para los de periodicidad diaria, una carpeta para el día en curso, y otra carpeta para días anteriores:

– Mensual: Para depositar los ficheros con los ajustes de apuestas (JUA) y catálogo de eventos (CEV), de periodicidad mensual.

– Diario: Para depositar los ficheros del catálogo de eventos (CEV), de periodicidad diaria.

– AAAAMMDD: Para el día en curso. Los registros de juegos (JUT y JUD) se generan en tiempo real. El día en curso contendrá todos los lotes/ficheros generados individualmente.

– Anteriores: Para días anteriores.»

16. El apartado 4.4.5 («JUA: Ajustes de Apuestas y CEV: Catálogo de Eventos») queda redactado del siguiente modo:

«La nomenclatura es:

<OperadorId>_<AlmacenId>_<Tipo>_<Subtipo>_<Periodicidad>_<Fecha>_<LoteId>.zip

Valores:

– <OperadorId> es el identificador del operador.

– <AlmacenId> es el identificador del Almacén.

– <Tipo> será JU.

– <Subtipo> puede ser: JUA o CEV.

– <Periodicidad> puede ser: D (diario) o M (mensual).

– <Fecha> es la fecha sobre la que se declaran los datos (no la fecha de escritura en el Almacén). Para información diaria tendrá el valor AAAAMMDD y para información mensual AAAAMM.

– <LoteId> es el identificador del lote.»

17. El apartado 4.5.6 («Registros periódicos») queda redactado de la siguiente manera:

«4.5.6 Registros periódicos.

Los registros de información periódica se basan en dos tipos derivados del RegistroBase, con campos adicionales que permiten determinar el periodo respecto al cuál se reportan los datos. Son de nuevo tipos abstractos, que no pueden presentarse directamente.

– Si el registro es susceptible de reporte mensual y diario (RUD, RUT, CJD, CJT y CEV), se utilizará RegistroPeriodicoBase.

![imagen](https://www.boe.es/datos/imagenes/disp/2018/270/15298_5681.png)

| Periodicidad | Diaria o mensual |
| --- | --- |
| Día/Mes | AAAAMMDD/AAAAMM |

– Si el registro sólo se puede reportar mensualmente (OPT, ORT, BOT, RUR, RUG y JUA), se utilizará RegistroMensualBase.

![imagen](https://www.boe.es/datos/imagenes/disp/2018/270/15298_5727.png)

| Mes | AAAAMM» |
| --- | --- |

18. En el apartado 4.5.11 («Desgloses que se repiten varias veces»), la sección «DesgloseOperaciones» queda redactada de la siguiente manera:

«DesgloseOperaciones.

Importe total y desglose de cada una de las operaciones de cobro o pago.

![imagen](https://www.boe.es/datos/imagenes/disp/2018/270/15298_5769.png)

> Redactado conforme a la corrección de errores publicada por Resolución de 5 de diciembre de 2018. Ref. BOE-A-2018-17134
