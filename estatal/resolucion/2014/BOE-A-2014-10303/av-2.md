## ANEXO VI

## Relación mínima de pruebas de integración

Este Anexo tiene por objeto la descripción de las pruebas que obligatoriamente han de ser realizadas para la certificación de la integración de los sistemas técnicos de juego de los operadores.

Las pruebas de integración deberán realizarse siempre en el entorno efectivamente empleado por el operador para el desarrollo y explotación del juego objeto de la licencia.

En las pruebas de integración que requieran datos personales de residentes en España, las entidades de certificación podrán hacer uso de los juegos de ensayo que facilitará a tal efecto la Dirección General de Ordenación del Juego para el entorno de producción de los servicios web de verificación.

Las pruebas se clasifican en función del tipo de licencia.

Se definen los siguientes tipos de pruebas junto con las evidencias mínimas que deberán recogerse en cada uno de ellos:

a) Funcional.

Las pruebas funcionales consistirán en la evaluación de características externas de una aplicación o sistema, utilizando los mismos medios que están a disposición de un participante o las aplicaciones de gestión que están a disposición del personal del operador.

Como evidencia deberá recogerse como mínimo:

• La conformidad o disconformidad de la prueba.

• Las capturas de pantalla resultado de la interacción entre el participante o personal del operador que realiza la prueba y la plataforma de juego.

b) Trazabilidad.

Las pruebas de trazabilidad consistirán en el análisis y contraste de los registros y trazas que se generan en el sistema cuando se realiza la prueba descrita. Los registros y trazas de este tipo de prueba serán los del sistema de información de la unidad central de juegos, no los del sistema de control interno.

Como evidencia deberá recogerse como mínimo:

• La conformidad o disconformidad de la prueba.

• Las capturas de pantalla que muestren la información del objeto de registro o traza.

• La descripción de la fuente de información (fichero, tabla…) donde se ha obtenido el registro o traza.

c) Datos reales.

El análisis de datos reales consistirá en verificar la correcta contabilidad, formato e integridad de los datos generados por la interacción entre participantes y el sistema técnico de juego.

Estas pruebas de integración con datos reales necesitarán que el sistema técnico de juego disponga al menos de un mes de datos, que no podrán ser completados mediante pruebas o simulaciones.

Como evidencia deberá recogerse como mínimo:

• La conformidad o disconformidad de la prueba.

• La fuente (fichero, tablas, etc.) de la que ha sido obtenida la información.

• Aquellos datos representativos que en cada prueba se requieran.

Las pruebas mínimas de integración en función del tipo de licencia y clasificadas por áreas son las siguientes:

A. Licencias Generales

A.1 Registro de usuario y comprobación de las prohibiciones.

| Referencia de la prueba | A.1.1 |
| --- | --- |
| Nombre de la prueba. | Alta de registro de usuario. |
| Tipo de prueba. | Funcional, Trazabilidad. |
| Descripción de la prueba. | Desde el punto de vista de un participante, se procederá a realizar el registro de: – Un participante residente en España, con datos de identidad correctos, mayor de edad y no inscrito en el RGIAJ. – Un participante no residente. Esta prueba deberá realizarse por parte de todos los operadores, independientemente de que el registro de usuario se requiera para la participación en el juego o para el registro de los ganadores. |
| Resultado Esperado. | Se incluirá en el resultado el DNI/NIE, fecha y hora en la que se ha realizado cada alta, de forma que la Dirección General de Ordenación del Juego pueda verificar a posteriori que los servicios de verificación de la DGOJ han sido consultados. En el registro del no residente, se incluirá el código utilizado para identificar al cliente, fecha y hora en la que se ha realizado las pruebas. Funcional Deberá validarse que el usuario ha sido dado de alta en el sistema. El sistema deberá recoger del participante todos los campos de información del participante descritos en la RES_TEC Anexo I apartado 2.1.1. En el caso de participante no residente, el sistema deberá solicitar una copia de un documento identificativo. Trazabilidad Se analizarán los registros y trazas del sistema que recogen los datos del registro de usuario realizado. Deberá verificarse la trazabilidad de la aceptación del contrato de juego firmado por el jugador. |
| Referencia de la prueba. | A.1.2 |
| --- | --- |
| Nombre de la prueba. | Comprobación de las prohibiciones subjetivas. |
| Tipo de prueba. | Funcional, trazabilidad. |
| Descripción de la prueba. | Desde el punto de vista de un participante, se procederá a realizar el registro de: – Un participante residente en España que aporta datos incorrectos de identidad. – Un participante residente en España, con datos correctos de identidad, que figura inscrito en el RGIAJ. – Un participante residente en España, con datos correctos de identidad, menor de edad. – Un participante no residente en España, menor de edad. La prueba se deberá realizar con los servicios de verificación operativos de la Dirección General de Ordenación del Juego. |
| Resultado Esperado. | Se incluirá en el resultado el DNI, fecha y hora en la que se ha realizado cada alta, de forma que la Dirección General de Ordenación del Juego pueda verificar a posteriori que los servicios de verificación de la DGOJ han sido consultados. Funcional El sistema no debe permitir el registro de los participantes menores, inscritos en el RGIAJ o cuyos datos de verificación resulten ser incorrectos. Trazabilidad Se analizarán los registros y trazas del sistema que recogen los datos del registro de usuario. |
| Referencia de la prueba. | A.1.3 |
| --- | --- |
| Nombre de la prueba. | Validación del campo DNI/NIE. |
| Tipo de prueba. | Funcional, trazabilidad. |
| Descripción de la prueba. | En esta prueba se verificará que el sistema de control interno dispone de mecanismos para evitar los siguientes escenarios: – Introducir valores erróneos en el DNI o NIE, como por ejemplo, errores de formato o letras incongruentes con el número. – Pasar a estado activo un registro de usuario cuyo DNI o NIE incluye errores. – Confundir el campo NIE con el campo DNI y viceversa. |
| Resultado Esperado. | Se deberá describir el comportamiento del sistema para cada uno de los escenarios anteriormente expuestos, y una valoración sobre éste. |

A.2 Cuenta de juego, cobros y pagos.

| Referencia de la prueba. | A.2.1 |
| --- | --- |
| Nombre de la prueba. | Registro correcto de operaciones en la cuenta de juego. |
| Tipo de prueba. | Funcional, trazabilidad. |
| Descripción de la prueba. | Desde el punto de vista del participante, se realizarán operaciones de depósito y retirada en la cuenta de juego. Se analizará si existen otras operaciones disponibles en la cuenta de juego. |
| Resultado Esperado. | Se incluirá en el resultado el DNI, fecha y hora, y descripción de cada operación realizada, de forma que la Dirección General de Ordenación del Juego pueda verificar a posteriori que los datos llegan correctamente al sistema de control interno. Funcional Se verificará la correcta contabilización en la cuenta de juego de los depósitos y retiradas. En el caso de existir otras operaciones disponibles en la cuenta de juego, se incluirá en el resultado la relación de las mismas. Se verificará que entre las operaciones no existe ninguna que permita recibir crédito del operador o realizar transferencias entre participantes. Trazabilidad Se analizarán los registros y trazas del sistema que recogen los datos de la contabilización de depósitos y retiradas. |

A.3 Límites a los depósitos.

| Referencia de la prueba | A.3.1 |
| --- | --- |
| Nombre de la prueba. | Depositar por encima de los límites. |
| Tipo de prueba. | Funcional, trazabilidad. |
| Descripción de la prueba. | Se accederá con una cuenta que tenga límites de depósito diario, semanal o mensual por defecto. Se bajarán los límites a 10, 15 y 20 euros respectivamente. Se realizarán depósitos por debajo del límite. Se realizarán depósitos por encima del límite. Se deberá probar cada límite, ya sea diario, semanal o mensual, utilizando diversas combinaciones de rangos horarios. |
| Resultado Esperado. | Funcional. El sistema permite reducir los límites. El sistema permite depósitos por debajo del límite y no los permite por encima. Trazabilidad. Se analizarán los registros y trazas del sistema que muestren los cambios de los límites. |
| Referencia de la prueba. | A.3.2 |
| --- | --- |
| Nombre de la prueba. | Datos de límites de depósito. |
| Tipo de prueba. | Datos reales. |
| Descripción de la prueba. | Se consultarán los datos reales del sistema para averiguar cuántos participantes tienen importes superiores a los preestablecidos. En caso de que existan participantes cuyos límites sean superiores a los preestablecidos, se verificará que se han realizado y evaluado correctamente las necesarias solicitudes de incremento de límites. A los efectos de esta prueba, bastará con realizar la comprobación de una muestra de 5 participantes, en caso de haberlos. |
| Resultado Esperado. | Se incluirá en el resultado los códigos de identificación «JugadorId» de los participantes analizados, indicando las fechas en que realizaron las peticiones de incremento de límites y las fechas en que fueron autorizadas. Se verificará que el sistema conserva registros y trazas de las solicitudes, análisis realizados y autorización de incremento de límites. |

A.4 Internet. Redirección a dominio «.es».

| Referencia de la prueba. | A.4.1 |
| --- | --- |
| Nombre de la prueba. | Redirección a dominio «.es» |
| Tipo de prueba. | Funcional. |
| Descripción de la prueba. | El operador proporcionará a la entidad de certificación la lista de dominios diferentes a «.es» en los que él mismo, su matriz o sus filiales ofrecen juego. La entidad de certificación accederá a cada uno de los sitios desde una dirección IP asociada al territorio español y verificará la redirección. |
| Resultado Esperado. | Se verificará que se efectúa la redirección a dominio «.es». La entidad de certificación listará los dominios diferentes de «.es» que se han utilizado en la prueba. |

A.5 Sistema de Control Interno.

| Referencia de la prueba. | A.5.1 |
| --- | --- |
| Nombre de la prueba. | Integridad de los registros RUT y CJT. |
| Tipo de prueba. | Datos reales. |
| Descripción de la prueba. | En esta prueba se contrastarán los datos del SCI respecto a los datos del sistema de información del operador, con objeto de evaluar la integridad de los datos del SCI. Se obtendrán los siguientes datos mensuales: A partir del registro RUT mensual: • Número de altas. • Número de participantes por estado. A partir del registro CJT mensual: • Saldo inicial. • Depósitos. • Retiradas. • Participación. • Devolución de la participación. • Premios. • Saldo final. • Premios en especie. • Otros movimientos. Esta prueba requiere que la entidad de certificación acceda a datos reales en claro. El operador deberá proporcionar en claro los ficheros RUT y CJT mensuales a la entidad de certificación y ésta deberá validar que éstos coinciden con los almacenados realmente en el sistema de información del operador. En ningún caso se requiere que la entidad de certificación conozca la clave de cifrado. |
| Resultado Esperado. | Para el RUT mensual: – Se contrastarán los datos del fichero RUT con listados obtenidos del backoffice del sistema técnico de juego. Es necesario que la entidad de certificación se cerciore de la veracidad de estos listados, dado que son la fuente para contrastar la integridad de los datos reales del SCI. Para el CJT mensual: – Se contrastarán los datos del fichero CJT con listados obtenidos del backoffice del sistema técnico de juego. Es necesario que la entidad de certificación se cerciore de la veracidad de estos listados, dado que son la fuente para contrastar la integridad de los datos reales del SCI. – Se verificará que el saldo inicial de un mes es igual al saldo final del mes inmediatamente anterior. – Se verificará que el saldo final equivale al saldo inicial y la suma del resto de movimientos. Como resultado de esta prueba, la entidad de certificación deberá incluir: – La conformidad de las comprobaciones realizadas y evidencias de las mismas. NOTA: Las comprobaciones y los cálculos se realizarán por separado, tanto en unidades monetarias «EUR», como en cualquier otra unidad, ya sean puntos de bonificación u otros. |
| Referencia de la prueba | A.5.2 |
| --- | --- |
| Nombre de la prueba. | Certificado válido. |
| Tipo de prueba. | Datos reales. |
| Descripción de la prueba. | En esta prueba se verificará con qué certificado se están firmando los datos y acreditará que se trata de un certificado válido y que no ha sido objeto de revocación. En ningún caso se requiere que la entidad de certificación conozca la clave de cifrado. |
| Resultado Esperado. | La entidad de certificación verificará con qué certificado se están firmando los datos y acreditará que se trata de un certificado válido y que no ha sido objeto de revocación. La entidad de certificación indicará en el resultado la parte pública del certificado con que se están firmando los datos del almacén. |

Modelo de resumen ejecutivo de las pruebas de integración para licencias generales.

| Área y requisito | Calificación |
| --- | --- |
| A.1 Registro de usuario y comprobación de las prohibiciones. |  |
| A.1.1 Alta de registro de usuario. |  |
| A.1.2 Comprobaciones de las prohibiciones subjetivas. |  |
| A.1.3 Validación campo DNI/NIE. |  |
| A.2 Cuenta de juego, cobros y pagos. |  |
| A.2.1 Registro correcto de operaciones en la cuenta de juego. |  |
| A.3 Límites a los depósitos. |  |
| A.3.1 Depositar por encima de los límites. |  |
| A.3.2 Datos de límites de depósito. |  |
| A.4 Internet. Redirección a dominio «.es» |  |
| A.4.1 Redirección a dominio «.es» |  |
| A.5 Sistema de Control Interno. |  |
| A.5.1 Integridad de los registros RUT y CJT. |  |
| A.5.2 Certificado válido. |  |

B. Licencias Singulares.

B.1. Oferta de juego.

| Referencia de la prueba. | B.1.1 |
| --- | --- |
| Nombre de la prueba. | Oferta de juego y variantes de juego. |
| Tipo de prueba. | Funcional. |
| Descripción de la prueba. | Desde el interfaz del jugador, se accederá a comprobar la oferta de juego correspondiente a la licencia singular. Se analizará la oferta disponible de juego desde cada una de las diferentes aplicaciones o terminales de participación. Se analizará cada uno de los juegos y variantes ofrecidas, y se buscará la correspondencia con los juegos y variantes permitidas por la reglamentación básica. Para realizar esta prueba no se requiere jugar, sino analizar la información publicada por el operador, ya sea informativa o reglas de los juegos. |
| Resultado Esperado. | Se indicará en el resultado una relación con la siguiente información: – el nombre comercial de los juegos y variantes encontrados. – las aplicaciones o terminales desde los que están disponibles. – la correspondencia con las variantes de la reglamentación básica. – la versión de las reglas particulares evaluadas. Se contrastará esta información con el cuestionario descriptivo de la licencia cumplimentado por el operador. |
| Referencia de la prueba. | B.1.2 |
| --- | --- |
| Nombre de la prueba. | Desarrollo del juego y correcta contabilización. |
| Tipo de prueba. | Funcional, trazabilidad. |
| Descripción de la prueba. | Desde el interfaz del jugador se realizará participación en el juego, verificándose: – la correcta contabilización de apuestas, premios, comisiones u otros. – en el caso de juegos en los que exista comisión del operador, se deberá verificar que el cálculo de comisiones se corresponde con lo establecido en las reglas particulares. – se intentará realizar una participación por importe superior al saldo disponible en la cuenta de juego. En el caso de determinados juegos, se verificará: – Para apuestas, que no se pueden realizar apuestas en momentos no previstos por las reglas particulares, y en particular con posterioridad al cierre de la comercialización, del inicio del evento para apuestas convencionales, o del final del evento para apuestas en directo. – Para bingo, que no permite comprar cartones fuera del periodo de comercialización, o cuando la partida hubiera comenzado. – Para póquer o casino, que no se pueden realizar apuestas fuera de los momentos designados para ello en las reglas particulares. – Para máquinas de azar, se comprobará que cuando la sesión destinada al juego de máquinas de azar finalice automáticamente por alcanzar el tiempo predeterminado o la cantidad fijada al configurar dicha sesión, la partida en curso finaliza ordenadamente, y la contabilización es correcta. Nota: Esta prueba se repetirá para cada una de las diferentes aplicaciones o terminales de participación, y para cada uno de los juegos, variantes o modalidades. |
| Resultado Esperado. | Funcional La conformidad de las verificaciones descritas anteriormente, desglosadas para cada variante analizada. Se verificará que no es posible realizar participación por importe superior al saldo disponible en la cuenta de juego. Asimismo se indicará la versión de las reglas particulares. Trazabilidad. Se describirá en el resultado las tablas, ficheros u otros que contienen la información. Se emitirá juicio sobre si el sistema de registro del sistema técnico de juego permite recuperar información para explicar cada una de las situaciones, así como reconstruir totalmente lo acontecido en cada una de las partidas. |
| Referencia de la prueba | B.1.3 |
| --- | --- |
| Nombre de la prueba | Traza de la participación para canales diferentes a internet |
| Tipo de prueba | Trazabilidad |
| Descripción de la prueba | En el caso de que existan, se realizarán varias participaciones de cada uno de los canales diferentes de internet, por ejemplo, SMS y teléfono. |
| Resultado Esperado | Trazabilidad Se analizarán los registros y trazas del sistema de cada una de los canales de participación utilizados, verificando que en el caso de SMS y teléfono el sistema conserva detalle de: – fecha/hora de cada mensaje o llamada realizada. – número de teléfono que ha originado el mensaje o llamada. – contenido del mensaje o de la llamada. |

B.2. Límites a la participación.

| Referencia de la prueba. | B.2.1 |
| --- | --- |
| Nombre de la prueba. | Límites a la participación. |
| Tipo de prueba. | Funcional. |
| Descripción de la prueba. | Se verificará que el sistema es conforme a los límites económicos: importes máximos de participación y de premio. Para ello la entidad de certificación participará en el juego intentando superar cada uno de los límites descritos en las órdenes ministeriales de los juegos, en el anexo III apartado segundo. Para las máquinas de azar se verificará que el sistema es conforme a los límites establecidos al iniciar la sesión destinada al juego de máquinas de azar, tanto el límite económico como el límite temporal. Asimismo, se verificará que la cantidad de dinero que un mismo participante puede dedicar a la participación en la máquina de azar no podrá exceder del importe del saldo que el participante tenga en su cuenta de juego en el momento en que se inicie la sesión de destinada al juego de máquinas de azar de las máquinas de azar, incrementado en el importe de los premios obtenidos en dicha sesión. |
| Resultado Esperado. | Se dejará constancia de las pruebas realizadas y el resultado obtenido. |

B.3. Comportamiento ante errores técnicos.

| Referencia de la prueba. | B.3.1 |
| --- | --- |
| Nombre de la prueba. | Pérdida de la comunicación con el cliente. |
| Tipo de prueba. | Funcional. |
| Descripción de la prueba. | Se realizarán pruebas de iniciar una partida y se provocará la pérdida de comunicación con la unidad central de juegos. Se restablecerá la conexión al transcurrir 1 minuto, 5 minutos o 15 minutos (diferentes intervalos de tiempo). Se verificará la reacción del sistema para finalizar la partida y su conformidad con lo descrito en las reglas particulares. Esta prueba se deberá realizar para cada uno de los terminales, aplicaciones o clientes y cada uno de los juegos o modalidades ofrecidas. |
| Resultado Esperado. | Se indicará la conformidad con las reglas particulares. Se indicará en el resultado el comportamiento obtenido para cada terminal, aplicación o cliente, y para cada juego o modalidad. Se incluirá también la versión de reglas particulares analizadas. |
| Referencia de la prueba. | B.3.2 |
| --- | --- |
| Nombre de la prueba. | Error en el cliente. |
| Tipo de prueba. | Funcional. |
| Descripción de la prueba. | Se iniciará una partida y se provocará el apagado inesperado del terminal cliente. Se iniciará de nuevo el terminal al transcurrir 1 minuto, 5 minutos o 15 minutos (diferentes intervalos de tiempo). Se verificará la reacción del sistema para finalizar la partida, y su conformidad con lo descrito en las reglas particulares. Esta prueba se deberá realizar para cada uno de los terminales, aplicaciones o clientes y cada uno de los juegos o modalidades ofrecidas. |
| Resultado Esperado. | Se indicará la conformidad con las reglas particulares. Se indicará en el resultado el comportamiento obtenido para cada terminal, aplicación o cliente, y para cada juego o modalidad. Se incluirá también la versión de las reglas particulares analizadas. |

B.4. Sistema de control interno.

| Referencia de la prueba. | B.4.1 |
| --- | --- |
| Nombre de la prueba. | Integridad de los registros OPT/ORT. |
| Tipo de prueba. | Datos reales. |
| Descripción de la prueba. | En esta prueba se contrastarán los datos del SCI respecto a los datos del sistema de información del operador, con objeto de evaluar la integridad de los datos del SCI. Se obtendrán los siguientes datos mensuales: A partir del registro OPT/ORT mensual: • Participación. • Devolución de la participación. • Premios. • Premios en especie. Esta prueba requiere que la entidad de certificación acceda a datos reales en claro. El operador deberá proporcionar en claro los ficheros OPT/ORT a la entidad de certificación y ésta deberá validar que éstos coinciden con los almacenados realmente en el sistema de información del operador. No se requiere que la entidad de certificación tenga acceso a datos personales. En ningún caso se requiere que la entidad de certificación conozca la clave de cifrado. |
| Resultado Esperado. | Se contrastarán los datos de los ficheros OPT/ORT con listados obtenidos del backoffice del sistema técnico de juego. Es necesario que la entidad de certificación se cerciore de la veracidad de estos listados, dado que son la fuente para contrastar la integridad de los datos reales del SCI. Como resultado de esta prueba, la entidad de certificación deberá incluir: – La conformidad de las comprobaciones realizadas. – Los siguientes datos de OPT/ORT, calculados a partir de los datos mensuales, para cada mes: El cociente entre el importe de premios y el importe de participación (expresado con 4 decimales). Nota: No se incluirá en el resultado cifras de facturación directamente. Nota: Las comprobaciones y los cálculos se realizarán por separado, tanto en unidades monetarias «EUR», como en cualquier otra unidad, ya sean puntos de bonificación u otros. |
| Referencia de la prueba. | B.4.2 |
| --- | --- |
| Nombre de la prueba. | Integridad de los registros JUD/JUT. |
| Tipo de prueba. | Datos reales. |
| Descripción de la prueba. | En esta prueba se contrastarán los datos del SCI respecto a los datos del sistema de información del operador, con objeto de evaluar la integridad de los datos del SCI. Se obtendrán los siguientes datos diarios de los 5 días previos a la realización de la prueba: A partir de los registros JUT/JUD: • Número de partidas de cada modalidad • Se tomará una muestra aleatoria de 5 partidas y se contrastarán sus datos con el sistema de información del operador. Por ejemplo, los participantes, los premios, el evento en el caso de una apuesta o el número de SMS’s en el caso de un concurso. Esta prueba requiere que la entidad de certificación acceda a datos reales en claro. El operador deberá proporcionar en claro los ficheros JUT/JUD a la entidad de certificación y ésta deberá validar que éstos coinciden con los almacenados realmente en el sistema de información del operador. No se requiere que la entidad de certificación tenga acceso a datos personales. En ningún caso se requiere que la entidad de certificación conozca la clave de cifrado. |
| Resultado Esperado. | Se contrastarán los datos de los ficheros JUT/JUD con listados obtenidos del backoffice del sistema técnico de juego. Es necesario que la entidad de certificación se cerciore de la veracidad de estos listados, dado que son la fuente para contrastar la integridad de los datos reales del SCI. Como resultado de esta prueba, la entidad de certificación deberá incluir: – La conformidad de las comprobaciones realizadas. Nota: No se incluirá en el resultado cifras de facturación directamente. Nota: Las comprobaciones y los cálculos se realizarán por separado, tanto en unidades monetarias «EUR», como en cualquier otra unidad, ya sean puntos de bonificación u otros. |

Modelo de resumen ejecutivo de las pruebas predefinidas para licencias singulares

| Área y requisito | Calificación |
| --- | --- |
| B.1 Oferta de Juego.. |  |
| B.1.1 Oferta de juego y variantes de juego. |  |
| B.1.2 Desarrollo del juego y correcta contabilización. |  |
| B.1.6 Traza de la participación para canales diferentes a internet. |  |
| B.2 Límites económicos a la participación. |  |
| B.2.1 Límites económicos a la participación. |  |
| B.3 Comportamiento ante errores técnicos. |  |
| B.3.1 Pérdida de la comunicación con el cliente. |  |
| B.3.2 Error en el cliente. |  |
| B.4 Sistema de control interno. |  |
| B.4.1 Integridad de los registros OPT/ORT. |  |
| B.4.2 Integridad de los registros JUT/JUD. |  |
