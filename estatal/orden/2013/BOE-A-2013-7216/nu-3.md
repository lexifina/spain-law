## III. Instrucciones para la cumplimentación del mensaje de modificación del destino

Durante la circulación con e-DA se puede proceder a modificar el destino inicialmente consignado en el documento para lo cual el expedidor enviará un mensaje indicando el nuevo destino, formalizando el mensaje de acuerdo con las instrucciones contenidas en estas normas de cumplimentación.

Los supuestos de reintroducción de productos en el establecimiento de salida se realizarán al amparo de un mensaje de cambio de destino formalizado por el expedidor inicial.

1. Atributo

Este grupo de datos no se cumplimentará y serán facilitados por la AEAT tras la aceptación del mensaje de modificación del destino.

1a. Fecha de validación.

1b. Hora de validación.

1c. Código Seguro de Verificación (CSV).

2. Documento

Grupo de datos obligatorio.

2a. ARC.

Obligatorio.

Se indicará el ARC del documento administrativo electrónico para el que se solicita la modificación del destino.

2b. Número de secuencia.

Obligatorio.

Se indicará el número de secuencia del documento administrativo electrónico para el que se solicita la modificación del destino.

3. Nuevo destinatario

Grupo de datos obligatorio.

3a. Régimen fiscal.

Obligatorio.

Se indicará la clave del régimen fiscal correspondiente, según las siguientes claves:

| Régimen fiscal | Descripción |
| --- | --- |
| A | Avituallamientos exentos a buques y aeronaves que se documentan con e-DA. |
| D | Envíos de productos al amparo de supuestos de exención por entregas en el marco de las relaciones internacionales. |
| E | Envíos de productos al amparo de supuestos de exención distintos de los señalados en las letras A y D. |
| F | Salida de productos a tipo reducido con destino a consumidores finales. |
| R | Salida de productos a tipo reducido con destino a almacenes fiscales y a detallistas inscritos. |
| S | Productos que se expiden en régimen suspensivo. |

Únicamente se podrán realizar cambios sobre el régimen fiscal indicado en el envío original en los supuestos de exención (valores A, D o E, debiendo ser el nuevo régimen fiscal otro supuesto de exención) o entre supuestos de salidas a tipo reducido (valores F o R, entre sí).

3b. Código de tipo de destino.

Obligatorio.

Se indicará el nuevo destino de la circulación mediante uno de los siguientes valores:

| Valores | Descripción |
| --- | --- |
| 1 | Establecimientos censados con CAE. |
| 2 | Destinatarios interiores sin CAE. |
| 3 | Exportación. |

3c. Destinatario NIF

Condicional.

Se indicará el NIF del nuevo destinatario.

Cuando se trate de entregas exentas en el marco de relaciones internacionales se consignará el NIF de la Misión de cada país u Organismo Internacional acreditado en España, así como el nombre (3d) y lugar de entrega (3f).

Si se trata de exportaciones y avituallamientos que se documenten como exportaciones se indicará el NIF y el nombre (3d) de la persona que representa al consignatario en el lugar de exportación, así como el lugar de entrega (3f).

Cuando se trate de avituallamientos exentos que no se documenten como exportaciones se consignará el NIF, o cualquier otro número que permita su identificación, de la compañía aérea o de la persona privada propietaria de la aeronave o el NIF del armador o consignatario del buque.

3d. Destinatario nombre.

Condicional.

Deberá consignarse el nombre y apellidos o razón social del destinatario.

3e. Destinatario CAE.

Condicional.

Deberá consignarse el CAE correspondiente al establecimiento al que se remiten los productos, cuando aquél esté inscrito en el registro territorial (valor 1 en la casilla 3b).En los demás casos, esta casilla no se cumplimentará.

3f. Lugar de entrega.

Condicional.

Se indicará la dirección correspondiente al lugar de entrega de los productos cuando los valores de la casilla 3b (tipo de destino) sean 2 (destinatarios interiores sin CAE) ó 3 (exportación).

3g. Número de factura.

Condicional.

En los casos de circulación tras despacho de importación a libre practica, no será necesario cumplimentar esta casilla.

En los demás casos, deberá consignarse el tipo y el número de documento comercial que acompaña la expedición (factura de venta, albarán de entrega, entréguese, nota de entrega o cualquier otro documento comercial que remita a los registros financieros y de existencias de la empresa). En aquellos casos en que los expedidores no sean propietarios de los productos expedidos, se deberá consignar el número y, en su caso, el tipo de documento que sirva de soporte para facturar los servicios prestados.

Se indicará el tipo de documento, de acuerdo con las siglas que se relacionan a continuación, seguido del número que le corresponda:

| Siglas | Tipo documento |
| --- | --- |
| FAC | Factura. |
| ALB | Albarán. |
| NOT | Nota de entrega. |
| ORD | Órdenes de entrega. |
| OTR | Otros no expresados anteriormente o cuando sólo exista un número de control. |

3h. Fecha de la factura.

Condicional.

Se consignará la fecha de expedición del documento mencionado en la casilla 3g, cuando se haya cumplimentado ésta.

4. Nuevos datos para la exportación

Grupo de datos condicional.

4a. Código de la Aduana de exportación.

Condicional. Se cumplimentará si en la casilla 3b (código de tipo de destino) se ha indicado el valor 3 (exportación).

Se indicará el código de la aduana de presentación de la declaración de la exportación de acuerdo con las claves señaladas en el anexo 1.

4b. País de destino.

Condicional. Se cumplimentará si en la casilla 3b (código de tipo de destino) se ha indicado el valor 3 (exportación).

Cuando se trate de exportaciones (valor 3 de la casilla 3b, tipo de destino) se consignará el país de destino de acuerdo con los códigos del anexo 2 y, si se trata de avituallamientos que se documenten como exportaciones (avituallamiento a buques de bandera no comunitaria, artículo 102.3 del Reglamento de los Impuestos Especiales), se deberá consignar el código EX.

5. Datos nueva organización exenta

Grupo de datos opcional.

Se podrá cumplimentar este grupo cuando en la casilla 3a (Régimen fiscal) se haya puntualizado el valor «D» (envíos de productos al amparo de supuestos de exención por entregas en el marco de las relaciones internacionales).

5a. Código de la organización exenta.

Opcional.

Se podrá indicar alguna de las siguientes claves:

| Código | Descripción |
| --- | --- |
| 1 | Organismo internacional. |
| 2 | Embajada u oficina consular. |
| 3 | Fuerzas Armadas de la OTAN. |
| 4 | Otros. |

5b. País de la organización exenta.

Opcional.

Cuando se haya seleccionado el valor 2 (embajada u oficina consular), se podrá indicar el código del país al que pertenece la representación diplomática de acuerdo con las claves del anexo 2.

6. Transporte

Grupo de datos obligatorio.

6a. Código del modo de transporte.

Obligatorio.

Se indicará el modo de transporte, de acuerdo con los siguientes códigos:

| Código | Descripción |
| --- | --- |
| 1 | Transporte marítimo. |
| 2 | Transporte ferroviario. |
| 3 | Transporte por carretera. |
| 4 | Transporte aéreo. |
| 5 | Envío postal. |
| 7 | Instalaciones fijas de transporte. |
| 8 | Transporte por vías navegables. |
| 0 | Otros. |

6b. Duración del transporte.

Obligatorio.

Deberá consignarse el número de días y horas previstos para la duración del transporte, teniendo en cuenta el medio de transporte utilizado y la distancia.

Se expresará en horas (H) o días (D) seguido de un número de dos cifras. La indicación para H deberá ser igual o inferior a 24.

En el transporte por tuberías fijas se indicará el tiempo transcurrido desde el inicio hasta el fin de la circulación.

6c. Código del organizador del transporte.

Obligatorio.

Se indicará la persona responsable de organizar el primer transporte, mediante uno de los siguientes valores:

| Valores | Descripción |
| --- | --- |
| 1 | Expedidor. |
| 2 | Destinatario. |
| 3 | Propietario de los productos. |
| 4 | Otro. |

6d. Información complementaria del transporte.

Opcional.

Se consignará cualquier información relativa al transporte, por ejemplo, la descripción del modo de transporte si se ha consignado el valor 0 (Otros) en la casilla 6a (Código del modo de transporte), la identidad de cualquier transportista posterior, interrupciones previstas, introducción de los productos en un depósito aduanero para su exportación o en un centro de distribución física (identificar establecimientos y dirección), etc.

7. Operador organizador del transporte

Grupo de datos condicional.

Cuando el transporte se organice por el expedidor o el destinatario no se cumplimentará este grupo de datos. Sólo se cumplimentará si el agente del primer transporte consignado en la casilla 6c (código del organizador del transporte) es valor 3 (propietario de los productos) ó valor 4 (otro, distinto del expedidor, destinatario y propietario).

7a. País.

Condicional.

Deberá cumplimentarse con las siglas del país de la nacionalidad del organizador del transporte, de acuerdo con las claves contenidas en la tabla del anexo 2, en el transporte no organizado por el expedidor o el destinatario.

7b. NIF.

Condicional.

Deberá consignarse el NIF o cualquier otro número que permita su identificación en caso de transporte no organizado por el expedidor o el destinatario.

7c. Nombre.

Condicional.

Se consignará el nombre y apellidos o razón social del organizador del transporte, en el transporte no organizado por el expedidor o por el destinatario.

7d. Calle.

Condicional.

Se consignará en caso de que el transporte no sea organizado por el expedidor o el destinatario, y el organizador resida fuera del territorio de la Comunidad.

7e. Ciudad.

Condicional.

Se consignará en caso de que el transporte no sea organizado por el expedidor o el destinatario, y el organizador resida fuera del territorio de la Comunidad.

7f. Código Postal.

Condicional.

Se consignará en caso de que el transporte no sea organizado por el expedidor o el destinatario, y el organizador resida fuera del territorio de la Comunidad.

8. Detalles del transporte

Grupo de datos obligatorio.

Este grupo de datos puede repetirse hasta 9 veces, es decir si durante la circulación se va a utilizar más de una unidad de transporte se repetirán las casillas de este grupo para indicar los detalles de las distintas unidades de transporte, por ejemplo la cabeza tractora y el remolque o contenedor.

8a. Medio de transporte.

Obligatorio.

Se indicará la clave correspondiente al medio de transporte utilizado de acuerdo con la siguiente tabla:

| Código | Descripción |
| --- | --- |
| 1 | Camión. |
| 2 | Barco. |
| 3 | Vagón. |
| 4 | Aeronave. |
| 5 | Instalaciones fijas de transporte. |
| 6 | Otro. |

8b. País del medio de transporte.

Condicional.

No se formalizará en caso de que se consigne el valor 5 (Instalaciones fijas de transporte) en la casilla 8a (Medio de transporte).

Se indicará el código ISO del país o bandera del medio de transporte de acuerdo con la tabla del anexo 2.

8c. Identificación del medio de transporte.

Obligatoria.

Se indicará la matrícula del vehículo, aeronave o embarcación, con puntualización, en su caso, de la matrícula de la cabeza tractora, del remolque y del contenedor.

En caso de que en la casilla 8a (Medio de transporte) se haya consignado el valor 5 (Instalaciones fijas de transporte), se deberá consignar el código FIJO.

8d. Código de la unidad de transporte.

Obligatorio.

Se indicará el código o códigos de la unidad de transporte, de acuerdo con la siguiente lista de códigos:

| Código | Descripción |
| --- | --- |
| 1 | Contenedor. |
| 2 | Vehículo. |
| 3 | Remolque. |
| 4 | Cabina tractora/tractor. |
| 5 | Tubería fija. |
| 6 | Otro. |

8e. Precinto comercial.

Opcional.

Se podrá indicar la identificación de los precintos comerciales, si se utilizan para precintar la unidad de transporte.
