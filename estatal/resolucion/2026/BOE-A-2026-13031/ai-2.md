## ANEXO II

## Especificaciones técnicas para el procedimiento de embargo de cuentas por el «Nuevo Sistema Editran» regulado en el dispongo quinto, apartado 3

1. Consideraciones técnicas sobre el procedimiento por el «nuevo sistema EDITRAN».

1.1 Consideraciones sobre los intercambios dentro de un ciclo.

El procedimiento de embargo de cuentas para las entidades que hagan uso del «nuevo sistema EDITRAN» está regulado en el dispongo Quinto, apartado 3 de esta resolución.

El intercambio de información para el embargo de cuentas mediante EDITRAN entre la Agencia Tributaria y las entidades repite el siguiente ciclo:

![imagen](https://www.boe.es/datos/imagenes/disp/2026/146/13031_17130107_1.png)

Las diligencias, las contestaciones y los resultados de validación de las mismas pertenecientes a un mismo ciclo se identifican por una fecha. El campo que contiene esta fecha en todos los ficheros recibe el nombre de FECHA DE COMIENZO DE CICLO.

Las diligencias correspondientes a una entidad adherida que se transmiten a una entidad transmisora en un mismo fichero se agrupan en lo que en este documento se denomina «envío», que queda identificado por los campos CÓDIGO DE ENTIDAD ADHERIDA y NÚMERO DE ENVÍO. En consecuencia, un fichero de diligencias puede contener envíos correspondientes a distintas entidades adheridas, cuya numeración será independiente.

En las transmisiones en las que el origen de la información sea la Agencia Tributaria (diligencias y resultados de validación) el último registro del fichero transmitido será un registro de control, cuya estructura será similar tanto si se transmiten diligencias como si se transmiten resultados de validación; sin embargo, habrá diferencias en el contenido de los campos, según se detalla más adelante en este documento. Este registro de control no existirá en el fichero de contestaciones transmitido por las entidades a la Agencia Tributaria.

Sea cual sea el origen de la información, la iniciativa de la comunicación corresponderá a las entidades transmisoras, en las fechas y plazos que se indican en este documento. La recepción por parte de estas entidades de los ficheros con origen en la Agencia Tributaria supone el borrado de los mismos y su sustitución por un fichero con un único registro de control, que indica que se ha realizado dicha recepción.

De esta forma, la entidad transmisora siempre tendrá a su disposición un registro con los datos de estado del ciclo, evitando la posibilidad de que se recupere un fichero vacío, en caso de que la entidad transmisora intente una nueva recepción en ese ciclo, o en el caso de que no hubiera diligencias para la entidad en ciclos sucesivos.

1.2 Consideraciones sobre la validación del fichero de contestaciones a las diligencias.

En relación a la validación que realiza la Agencia Tributaria del fichero de contestaciones a las diligencias enviado por las entidades transmisoras, habrá de tenerse en cuenta lo siguiente:

– Porcentaje máximo de errores: 0 %.

– Máximo de registros erróneos: 0 %.

Cualquier error en el registro de cabecera o de fin de entidad Transmisora dará lugar al rechazo del fichero completo (lo que en este documento es denominado «rechazo global»). El mismo efecto tendrá un error en la secuencia de registros.

Cualquier error en el registro de cabecera, de detalle o de fin de entidad adherida dará lugar al rechazo completo del envío de la entidad adherida correspondiente.

El único error que no provocará el rechazo de un envío de una entidad adherida es la retransmisión de las contestaciones a las diligencias de un envío previamente aceptado en el mismo ciclo. La respuesta contendrá, para la entidad adherida de que se trate, un par de registros de tipo 1 y 3, en el primero de los cuales se incluirá el código de error (115).

2. Estructura del fichero de diligencias de embargo.

2.1 Estructura.

El fichero para cada entidad transmisora, que contendrá información de las diligencias de embargo para tantas entidades adheridas como sea necesario, tiene la estructura siguiente:

![imagen](https://www.boe.es/datos/imagenes/disp/2026/146/13031_17130108_1.png)

* El fichero de una entidad transmisora para un ciclo concreto se identifica por el campo «FECHA DE COMIENZO DE CICLO».

** La parte del fichero que corresponde a una entidad adherida determinada (un envío) se identifica por la combinación de los campos «CÓDIGO DE ENTIDAD DE DEPOSITO» y «NÚMERO DE ENVÍO».

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD. Los campos que reflejen una hora serán numéricos de 7 posiciones, utilizando el formato HHMMSSD. Los campos numéricos que carezcan de contenido estarán rellenos con ceros; no se consideran válidos en estos campos los espacios en blanco.

2.2 Fichero de diligencias de embargo. Registro de cabecera de entidad transmisora. Registro tipo 0.

El primer registro, para cada entidad transmisora, será un registro de cabecera, con la siguiente configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: 0. |
| 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8-15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16-23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: D (DILIGENCIAS DE EMBARGO). |
| 25-500 | ALF. | 476 | POSICIONES LIBRES DE CONTENIDO. |

2.3 Fichero de diligencias de embargo. Registro de cabecera de entidad adherida. Registro tipo 1.

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD ADHERIDA. CONTENIDO: 1. |
| 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA. |
| 8-15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN). FORMATO: AAAANNNN. |
| 16-23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: D (DILIGENCIAS DE EMBARGO DE CUENTAS). |
| 25-32 | NUM. | 8 | FECHA DE GENERACIÓN DEL ENVÍO MENSUAL DE DILIGENCIAS. |
| 33-36 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 37-37 | ALF. | 1 | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE DILIGENCIAS. CONTENIDO: E (CÉNTIMOS DE EURO). |
| 38-170 | ALF. | 133 | MENSAJE INFORMATIVO PARA EL DEUDOR: «Si desea mayor información sobre el expediente de embargo, puede dirigirse al teléfono de la Agencia Tributaria XXX-XXX-XXX» (*). |
| 171-500 | ALF. | 330 | POSICIONES LIBRES DE CONTENIDO. |
| (*) Se incluirá el número de teléfono de información que en cada momento establezca la Agencia Tributaria. |

2.4 Fichero de diligencias de embargo. Registro de detalle de diligencia de embargo. Registro tipo 2.

Los registros de detalle que sigan al registro de cabecera de entidad adherida tendrán la configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE DILIGENCIA DE EMBARGO. CONTENIDO: 2. |
| 2-10 | ALF. | 9 | NIF DEL DEUDOR. |
| 11-50 | ALF. | 40 | NOMBRE/RAZON SOCIAL DEL DEUDOR. |
| 51-52 | ALF. | 2 | SIGLAS DE LA VIA PÚBLICA | DATOS DEL DOMICILIO DEL DEUDOR. |
| 53-77 | ALF. | 25 | NOMBRE DE LA VIA PÚBLICA |
| 78-82 | NUM. | 5 | NÚMERO DEL PORTAL |
| 83-83 | ALF. | 1 | LETRA DEL PORTAL |
| 84-85 | ALF. | 2 | ESCALERA |
| 86-87 | ALF. | 2 | PISO |
| 88-89 | ALF. | 2 | PUERTA |
| 90-101 | ALF. | 12 | NOMBRE DEL MUNICIPIO |
| 102-106 | NUM. | 5 | CÓDIGO POSTAL |
| 107-119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |
| 120-134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |
| 135-142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |
| 143-157 | NUM. | 15 | POSICIONES LIBRES DE CONTENIDO. |
| 158-158 | ALF. | 1 | POSICIONES LIBRES DE CONTENIDO. |
| 159-174 | NUM. | 16 | POSICIONES LIBRES DE CONTENIDO. |
| 175-194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1. |
| 195-211 | NUM. | 17 | POSICIONES LIBRES DE CONTENIDO. |
| 212-231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2. |
| 232-248 | NUM. | 17 | POSICIONES LIBRES DE CONTENIDO. |
| 249-268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3. |
| 269-500 | ALF. | 232 | POSICIONES LIBRES DE CONTENIDO. |

2.5 Fichero de diligencias de embargo. Registro de fin de entidad adherida. Registro tipo 3.

Al final de los registros de detalle de cada entidad adherida, el fichero contiene un registro totalizador de las diligencias incluidas en el fichero para dicha entidad, que quedan identificadas por un número de envío. El formato será el siguiente:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD ADHERIDA. CONTENIDO: 3. |
| 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA. |
| 8-13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA. |
| 14-28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA. |
| 29-32 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 33-500 | ALF. | 468 | POSICIONES LIBRES DE CONTENIDO. |

2.6 Fichero de diligencias de embargo. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero se incluye un registro de fin de entidad transmisora, con la siguiente configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN ENTIDAD TRANSMISORA. CONTENIDO: 8. |
| 2-5 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 6-13 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE TRANSMISION. |
| 14-500 | ALF. | 487 | POSICIONES LIBRES DE CONTENIDO. |

2.7 Fichero de diligencias de embargo. Registro de control para la entidad transmisora. Registro tipo 9.

Se incluye a continuación la descripción de cada campo del registro de tipo 9 en el fichero de diligencias.

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1-1 | ALF. | 1 | INDICADOR DE REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA. CONTENIDO: 9. |
| 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8-15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16-24 | ALF. | 9 | POSICIONES LIBRES DE CONTENIDO. |
| 25-27 | NUM. | 3 | NÚMERO DE ENTIDADES ADHERIDAS INCLUIDAS EN EL FICHERO DE DILIGENCIAS. |
| 28-28 | ALF. | 1 | INDICADOR DE ESTADO DE LAS DILIGENCIAS PARA LA ENTIDAD. TRANSMISORA. CONTENIDO: «P» (PENDIENTE DE RECUPERAR POR LA ENTIDAD TRANSMISORA) ó R (RECIBIDAS POR LA ENTIDAD TRANSMISORA). |
| 29-31 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 32-34 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 35-37 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 38-40 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 41-43 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 44-44 | ALF. | 1 | ESTADO GENERAL DE LA ENTIDAD TRANSMISORA PARA EL CICLO MENSUAL. CONTENIDO: «P» (EN PROCESO). |
| 45-52 | NUM. | 8 | FECHA DE ALTA DEL REGISTRO. |
| 53-59 | NUM. | 7 | HORA DE ALTA DEL REGISTRO. |
| 60-500 | ALF. | 441 | POSICIONES LIBRES DE CONTENIDO. |

3. Estructura del fichero de contestación a las diligencias.

3.1 Estructura.

El fichero de contestación a las diligencias tiene la siguiente estructura:

![imagen](https://www.boe.es/datos/imagenes/disp/2026/146/13031_17130109_1.png)

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros. No se consideran válidos en estos campos los espacios en blanco.

3.2 Fichero de contestación a las diligencias. Registro de cabecera de entidad transmisora. Registro tipo 0.

El fichero de contestación a las diligencias comenzará con un registro de cabecera de entidad transmisora, con la siguiente configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: 0. |
| 2-3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8-15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16-23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS. |
| 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: T (TRABAS). |
| 25-400 | ALF. | 376 | POSICIONES LIBRES DE CONTENIDO. |

3.3 Fichero de contestación a las diligencias. Registro de cabecera de entidad adherida. Registro tipo 1.

El primer registro, para cada entidad adherida, será un registro de cabecera, con la siguiente configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD ADHERIDA. CONTENIDO: 1. |
| 2-3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA. |
| 8-15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN). |
| 16-23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS. |
| 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: T (TRABAS). |
| 25-28 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 29-29 | ALF. |  | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE TRABAS. CONTENIDO: E (CÉNTIMOS DE EURO). |
| 30-400 | ALF. | 371 | POSICIONES LIBRES DE CONTENIDO. |

3.4 Fichero de contestación a las diligencias. Registro de detalle de trabas realizadas. Registro tipo 2.

En este registro las entidades adheridas informan del resultado de las trabas realizadas conforme a la diligencia de embargo recibida de la Agencia Tributaria.

En la respuesta de las entidades no deberá alterarse el orden ni el contenido de las cuentas enviadas en el fichero del Departamento de Informática Tributaria, las cuentas adicionales a las que se extiende el embargo deberán añadirse a continuación de ellas, sin dejar cuentas vacías.

Si habiendo actuado contra seis cuentas sin lograr la traba de la cantidad indicada en la diligencia, el deudor dispone de más cuentas en la misma entidad, se reflejará esta circunstancia poniendo en el fichero de contestación a las diligencias un 1 en el campo INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO. El campo CÓDIGO DE RESULTADO DE TRABA podrá tomar los valores regulados en el dispongo Séptimo de esta resolución.

Los registros de detalle que sigan al registro de cabecera de entidad adherida tendrán el siguiente contenido:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE TRABAS DE DILIGENCIA DE EMBARGO. CONTENIDO: 2. |
| 2-10 | ALF. | 9 | NIF DEL DEUDOR. |
| 11-50 | ALF. | 40 | NOMBRE/RAZON SOCIAL DEL DEUDOR. |
| 51-52 | ALF. | 2 | SIGLAS DE LA VIA PÚBLICA. | DATOS DEL DOMICILIO DEL DEUDOR. |
| 53-77 | ALF. | 25 | NOMBRE DE LA VIA PÚBLICA. |
| 78-82 | NUM. | 5 | NÚMERO DEL PORTAL. |
| 83-83 | ALF. | 1 | LETRA DEL PORTAL. |
| 84-85 | ALF. | 2 | ESCALERA. |
| 86-87 | ALF. | 2 | PISO. |
| 88-89 | ALF. | 2 | PUERTA. |
| 90-101 | ALF. | 12 | NOMBRE DEL MUNICIPIO. |
| 102-106 | NUM. | 5 | CÓDIGO POSTAL. |
| 107-119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |
| 120-134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |
| 135-142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |
| 143-157 | NUM. | 15 | IMPORTE TOTAL TRABADO. |
| 158-158 | ALF. | 1 | INDICADOR DE EXISTENCIA DE MAS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO. CONTENIDO: 0 (NO EXISTEN MAS CUENTAS) O 1 (EXISTEN MAS CUENTAS). |
| 159-166 | NUM. | 8 | FECHA DE LA TRABA O ACTUACIÓN. |
| 167-174 | NUM. | 8 | FECHA LIMITE DE INGRESO DEL IMPORTE TRABADO. SI NO HAY IMPORTE TRABADO SE RELLENARA CON CEROS. |
| 175-194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1 (CCC1). |
| 195-196 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC1. |
| 197-211 | NUM. | 15 | IMPORTE TRABADO EN CCC1. |
| 212-231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2 (CCC2). |
| 232-233 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC2. |
| 234-248 | NUM. | 15 | IMPORTE TRABADO EN CCC2. |
| 249-268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3 (CCC3). |
| 269-270 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC3. |
| 271-285 | NUM. | 15 | IMPORTE TRABADO EN CCC3. |
| 286-305 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 4 (CCC4). |
| 306-307 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC4. |
| 308-322 | NUM. | 15 | IMPORTE TRABADO EN CCC4. |
| 323-342 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 5 (CCC5). |
| 343-344 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC5. |
| 345-359 | NUM. | 15 | IMPORTE TRABADO EN CCC5. |
| 360-379 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 6 (CCC6). |
| 380-381 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC6. |
| 382-396 | NUM. | 15 | IMPORTE TRABADO EN CCC6. |
| 397-400 | ALF. | 4 | POSICIONES LIBRES DE CONTENIDO. |

3.5 Fichero de contestación a las diligencias. Registro de fin de entidad adherida. Registro tipo 3.

Al final de los registros de detalle de cada entidad, deberá incluirse un registro totalizador de las trabas. El formato será el siguiente:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD ADHERIDA. CONTENIDO: 3. |
| 2-3 | NUM. | 2 | DELEGACION DE LA AGENCIA RECEPTORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA. |
| 8-13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA. |
| 14-28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA. |
| 29-43 | NUM. | 15 | IMPORTE TOTAL TRABADO POR LA ENTIDAD ADHERIDA. |
| 44-47 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 48-400 | ALF. | 353 | POSICIONES LIBRES DE CONTENIDO. |

3.6 Fichero de contestación a las diligencias. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero se incluye un registro de fin de entidad transmisora, o de fin de fichero, con la siguiente configuración:

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN ENTIDAD TRANSMISORA. CONTENIDO: 8. |
| 2-5 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 6-13 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS. |
| 14-400 | ALF. | 387 | POSICIONES LIBRES DE CONTENIDO. |

4. Estructura del fichero de resultados de la validación de las contestaciones a las diligencias.

4.1. Estructura.

La estructura del fichero resultado de la validación de contestación a las diligencias variará según el resultado de la misma:

a) Si se produce el rechazo global para una entidad transmisora, sin respuesta específica para cada entidad adherida, el fichero de respuesta contendrá tres registros: de tipo 0 (cabecera de entidad transmisora), 8 (fin de entidad transmisora) y 9 (registro de control), respectivamente. En estos registros se indicará el motivo del rechazo.

| ENTIDAD TRANSMISORA | TIPO 0 |
| --- | --- |
| FIN ENTIDAD TRANSMISORA | TIPO 8 |
| REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA | TIPO 9 |

Los tres registros se enviarán siempre; si en el fichero de contestación de diligencias transmitido por la entidad transmisora no existieran estos registros, se generarían con los datos mínimos precisos y con los errores que hayan podido detectarse.

b) Cuando no se produce el rechazo global para una entidad transmisora, la aceptación o rechazo se realiza individualmente para cada una de las entidades adheridas a la que aquella dé servicio en el ciclo en curso. En la estructura anterior se introducirá, entre el registro de tipo O y el registro de tipo 8 la respuesta que corresponda a cada una de las entidades adheridas a la que se esté respondiendo. El código indicando la aceptación o rechazo para cada entidad adherida estará incluido en el registro de cabecera de entidad adherida (tipo 1).

La respuesta será diferente, según se acepte o rechace el envío de la entidad adherida, e incluso puede variar según la causa del rechazo:

– Para aquellas entidades adheridas cuyo envío se acepta, la parte correspondiente del fichero de respuesta tendrá la forma:

| ENTIDAD ADHERIDA N | TIPO 1 (aceptado) |
| --- | --- |
| FIN ENTIDAD ADHERIDA N | TIPO 3 |

– Para aquellas entidades adheridas en las que el error se produzca en el registro de cabecera de entidad adherida del fichero de contestación a las diligencias, la estructura de la parte del fichero de validación correspondiente a esa entidad será:

| ENTIDAD ADHERIDA N | TIPO 1 (rechazado) |
| --- | --- |
| FIN ENTIDAD ADHERIDA N | TIPO 3 |

Los registros de detalle no se validan en este caso.

– Cuando siendo correcto el registro de cabecera de entidad adherida se produzcan errores en los registros de detalle o de fin de entidad, en la validación se incluirán, además de los registros de cabecera y fin de entidad adherida, los registros de detalle (de tipo 2) erróneos, si los hay, con la indicación del error que contienen; los registros de detalle correctos no se incluyen en la respuesta. Para la entidad adherida en cuestión, la parte del fichero de validación será (suponiendo que hay errores en X registros de detalle):

| ENTIDAD ADHERIDA N | TIPO 1 (rechazado) |
| --- | --- |
| ERRORES TRABAS DILIGENCIA 1 ERRORES TRABAS DILIGENCIA 2 – – – ERRORES TRABAS DILIGENCIA X | TIPO 2 |
| FIN ENTIDAD ADHERIDA N | TIPO 3 |

En general, la respuesta para los registros erróneos de cualquier tipo tendrá la siguiente configuración:

– Una primera parte que será igual al registro erróneo transmitido por la entidad (las 400 primeras posiciones del registro de resultados).

– A continuación, el código de error y número de campo en que éste se produce, conforme a la numeración que se indica en la descripción de los registros que se hace a continuación, hasta un máximo de 20 errores por registro (posiciones 401-500).

No siempre va a ser posible utilizar esta configuración, pues puede haber errores (particularmente en registros de tipo 0 y 1) para los que, en lugar de repetir exactamente el registro erróneo, se reconstruirá el contenido de algunos de sus campos.

Se incluye un ejemplo, para el caso de 4 entidades adheridas, de las que:

– Se rechaza el envío de la entidad 1 por contener errores en N registros de detalle.

– Se rechaza el envío de la entidad 2 por errores en el registro de cabecera de entidad.

– Se acepta el envío de la entidad 3.

– Se rechaza el envío de la entidad 4 por errores solamente en el registro de fin de entidad.

| ENTIDAD TRANSMISORA | TIPO 0 |
| --- | --- |
| ENTIDAD ADHERIDA 1 | TIPO 1 (rechazado) |
| ERRORES TRABAS DILIGENCIA 1 ERRORES TRABAS DILIGENCIA 2 – – – ERRORES TRABAS DILIGENCIA N | TIPO 2 |
| FIN ENTIDAD ADHERIDA 1 | TIPO 3 |
| ENTIDAD ADHERIDA 2 | TIPO 1 (rechazado) |
| FIN ENTIDAD ADHERIDA 2 | TIPO 3 |
| ENTIDAD ADHERIDA 3 | TIPO 1 (rechazado) |
| FIN ENTIDAD ADHERIDA 3 | TIPO 3 |
| ENTIDAD ADHERIDA 4 | TIPO 1 (rechazado) |
| ENTIDAD ADHERIDA 4 | TIPO 3 |
| FIN ENTIDAD TRANSMISORA | TIPO 8 |
| REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA | TIPO 9 |

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD. Los campos que reflejen una hora serán numéricos de 7 posiciones, utilizando el formato HHMMSS.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros; no se consideran válidos en estos campos los espacios en blanco.

4.2 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro de cabecera de entidad transmisora. Registro tipo 0.

El primer registro del fichero de resultados de la validación será la cabecera de entidad transmisora, con la siguiente configuración:

| N.º campo | Posición | Tipo | Long. | Descripción del campo |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD TRANSMISORA. CONTENIDO: 0. |
| 2 | 2-3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. |
| 3 | 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 4 | 8-15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 5 | 16-23 | NUM. | 8 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS (cuando se produzca el rechazo global del fichero de contestación a las diligencias) o FECHA DE PROCESO DE VALIDACIÓN (en el resto de los casos). |
| 6 | 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: R. (RESULTADO DE VALIDACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS). |
| 7 | 25-400 | ALF. | 376 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401-403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI CÓDIGO DE ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES). |
|  | 404-405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406-408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409-410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411-413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414-415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416-418 | NUM. | 3 | CÓDIGO DE ERROR-4 |
|  | 419-420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4 |
|  | 421-423 | NUM. | 3 | CÓDIGO DE ERROR-5 |
|  | 424-425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5 |
|  | 426-428 | NUM. | 3 | CÓDIGO DE ERROR-6 |
|  | 429-430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6 |
|  | 431-433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434-435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436-438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439-440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441-443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444-445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446-448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449-450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451-453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454-455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456-458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459-460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461-463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464-465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466-468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469-470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471-473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474-475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476-478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479-480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481-483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484-485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486-488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489-490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491-493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494-495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496-498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499-500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el Departamento de Informática Tributaria reproduce los datos transmitidos por las entidades.

4.3 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro de cabecera de entidad adherida. Registro tipo 1.

El primer registro, para cada entidad adherida, será un registro de cabecera, con la siguiente configuración:

| N.º campo | Posición | Tipo | Long. | Descripción del campo |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE CABECERA DE ENTIDAD ADHERIDA. CONTENIDO: 1. |
| 2 | 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 3 | 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA. |
| 4 | 8-15 | NUM. | 8 | NÚMERO DE ENVÍO (AÑO Y NÚMERO ORDEN). FORMATO: AAAANNNN |
| 5 | 16-23 | NUM. | 8 | FECHA DE PROCESO DE VALIDACIÓN (si el registro 1 no contiene errores; el FORMATO es: AAAAMMDD) o FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS (si el registro de tipo 1 contiene errores). |
| 6 | 24-24 | ALF. | 1 | INDICADOR DE TIPO DE FICHERO. CONTENIDO: R. (RESULTADOS DE VALIDACIÓN DE CONTESTACIONES), si el registro 1 no tiene errores, o lo que contuviera el fichero de contestación a las diligencias, si el registro 1 los contiene. |
| 7 | 25-28 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 | 29-29 | ALF. | 1 | INDICADOR DE ENVÍO ACEPTADO O RECHAZADO. CONTENIDO: A (ACEPTADO EL ENVÍO DE TRABAS) O R (RECHAZADO EL ENVÍO DE TRABAS). |
| 9 | 30-30 | ALF. | 1 | INDICADOR DE MONEDA EN EL QUE SE EXPRESAN TODOS LOS IMPORTES DEL ENVÍO DE TRABAS. CONTENIDO: E (CÉNTIMOS DE EURO). |
| 10 | 31-400 | ALF. | 370 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401-403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI CÓDIGO DE ERROR-1 = 0. EL REGISTRO NO CONTIENE ERRORES) |
|  | 404-405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406-408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409-410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411-413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414-415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416-418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419-420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421-423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424-425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426-428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429-430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431-433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434-435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436-438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439-440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441-443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444-445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446-448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449-450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451-453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454-455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456-458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459-460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461-463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464-465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466-468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469-470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471-473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474-475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476-478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479-480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481-483 | NUM. | 3 | CÓDIGO DE ERROR-17 |
|  | 484-485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486-488 | NUM. | 3 | CÓDIGO DE ERROR-18 |
|  | 489-490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491-493 | NUM. | 3 | CÓDIGO DE ERROR-19 |
|  | 494-495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496-498 | NUM. | 3 | CÓDIGO DE ERROR-20 |
|  | 499-500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el Departamento de Informática Tributaria reproduce los datos transmitidos por las entidades.

4.4 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro de detalle de errores en trabas. Registro tipo 2.

Los registros de detalle que sigan al registro de cabecera de entidad adherida, tendrán el siguiente formato:

| N.º campo | Posición | Tipo | Long. | Descripción del campo |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE DETALLE DE ERRORES EN LA VALIDACIÓN DE CONTESTACIONES. CONTENIDO: 2. |
| 2 | 2-10 | ALF. | 9 | NIF/CI DEL DEUDOR |
| 3 | 11-106 | ALF. | 96 | POSICIONES LIBRES DE CONTENIDO. |
| 4 | 107-119 | ALF. | 13 | NÚMERO DE DILIGENCIA DE EMBARGO. |
| 5 | 120-134 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR. |
| 6 | 135-142 | NUM. | 8 | FECHA DE GENERACIÓN DE LA DILIGENCIA. |
| 7 | 143-157 | NUM. | 15 | IMPORTE TOTAL TRABADO. |
| 8 | 158-158 | ALF. | 1 | INDICADOR DE EXISTENCIA DE MAS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO. |
| 9 | 159-166 | NUM. | 8 | FECHA DE LA TRABA O ACTUACION. |
| 10 | 167-174 | NUM. | 8 | FECHA LIMITE DE INGRESO DEL IMPORTE TRABADO. |
| 11 | 175-194 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 1 (CCC1). |
| 12 | 195-196 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC1. |
| 13 | 197-211 | NUM. | 15 | IMPORTE TRABADO EN CCC1. |
| 14 | 212-231 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 2 (CCC2). |
| 15 | 232-233 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC2. |
| 16 | 234-248 | NUM. | 15 | IMPORTE TRABADO EN CCC2. |
| 17 | 249-268 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 3 (CCC3). |
| 18 | 269-270 | NUM. | 2 | CÓDIGO RESULTADO DE TRABA EN CCC 3. |
| 19 | 271-285 | NUM. | 15 | EN IMPORTE TRABADO CCC3 |
| 20 | 286-305 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 4 (CCC4). |
| 21 | 306-307 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC4. |
| 22 | 308-322 | NUM. | 15 | IMPORTE TRABADO EN CCC4. |
| 23 | 323-342 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 5 (CCC5). |
| 24 | 343-344 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC5. |
| 25 | 345-359 | NUM. | 15 | IMPORTE TRABADO EN CCC5. |
| 26 | 360-379 | NUM. | 20 | CÓDIGO DE CUENTA CLIENTE 6 (CCC6). |
| 27 | 380-381 | NUM. | 2 | CÓDIGO DE RESULTADO DE TRABA EN CCC6. |
| 28 | 382-396 | NUM. | 15 | IMPORTE TRABADO EN CCC6. |
| 29 | 397-400 | ALF. | 4 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401-403 | NUM. | 3 | CÓDIGO DE ERROR-1. |
|  | 404-405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406-408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409-410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411-413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414-415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416-418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419-420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421-423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424-425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426-428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429-430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431-433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434-435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436-438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439-440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441-443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444-445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446-448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449-450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451-453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454-455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456-458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459-460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461-463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464-465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466-468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469-470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471-473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474-475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476-478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479-480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481-483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484-485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486-488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489-490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491-493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494-495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496-498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499-500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el Departamento de Informática Tributaria reproduce los datos transmitidos por las entidades.

4.5 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro tipo 3.

Tras los registros de detalle erróneos de cada entidad adherida, se incluirá un registro de cierre de los resultados de la validación para esa entidad. Este registro de fin de entidad adherida existirá incluso aunque no haya errores para la misma y se acepte el envío; su formato será el siguiente:

| N.º campo | Posición | Tipo | Long. | Descripción del campo |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD ADHERIDA. CONTENIDO: 3. |
| 2 | 2-3 | NUM. | 2 | DELEGACION DE LA AGENCIA EMISORA DEL FICHERO. |
| 3 | 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD ADHERIDA |
| 4 | 8-13 | NUM. | 6 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA. |
| 5 | 14-28 | NUM. | 15 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD. |
| 6 | 29-43 | NUM. | 15 | IMPORTE TOTAL TRABADO POR LA ENTIDAD ADHERIDA. |
| 7 | 44-47 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8 | 48-400 | ALF. | 353 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401-403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI EL CÓDIGO ERROR-1 = 0  EL REGISTRO NO CONTIENE ERRORES) |
|  | 404-405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406-408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409-410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411-413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414-415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416-418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419-420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421-423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424-425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5. |
|  | 426-428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429-430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431-433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434-435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-7. |
|  | 436-438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439-440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441-443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444-445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446-448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449-450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451-453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454-455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456-458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459-460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461-463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464-465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466-468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469-470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471-473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474-475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476-478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479-480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481-483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484-485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486-488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489-490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491-493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494-495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496-498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499-500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el Departamento de Informática Tributaria reproduce los datos transmitidos por las entidades.

4.6 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro de fin de entidad transmisora. Registro tipo 8.

Al final del fichero deberá incluirse un registro de fin de entidad transmisora. Este registro tendrá la siguiente configuración:

| N.º campo | Posición | Tipo | Long. | Descripción del campo |
| --- | --- | --- | --- | --- |
| 1 | 1 | ALF. | 1 | INDICADOR DE REGISTRO DE FIN DE ENTIDAD TRANSMISORA. CONTENIDO: 8. |
| 2 | 2-5 | NUM. | 4 | CÓDIGO DE ENTIDAD DE TRANSMISORA. |
| 3 | 6-13 | NUM. | 8 | FECHA DE PROCESO DE VALIDACIÓN (si el registro de tipo 8 no contiene errores; el FORMATO es: AAAAMMDD) o FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS (si el registro de tipo 8 sí los contiene). |
| 4 | 14-400 | ALF. | 387 | POSICIONES LIBRES DE CONTENIDO. |
|  | 401-403 | NUM. | 3 | CÓDIGO DE ERROR-1. (SI EL CÓDIGO ERROR-1 = 0. EL REGISTRO NO CONTIENE ERRORES) |
|  | 404-405 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-1. |
|  | 406-408 | NUM. | 3 | CÓDIGO DE ERROR-2. |
|  | 409-410 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-2. |
|  | 411-413 | NUM. | 3 | CÓDIGO DE ERROR-3. |
|  | 414-415 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-3. |
|  | 416-418 | NUM. | 3 | CÓDIGO DE ERROR-4. |
|  | 419-420 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-4. |
|  | 421-423 | NUM. | 3 | CÓDIGO DE ERROR-5. |
|  | 424-425 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-5 |
|  | 426-428 | NUM. | 3 | CÓDIGO DE ERROR-6. |
|  | 429-430 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-6. |
|  | 431-433 | NUM. | 3 | CÓDIGO DE ERROR-7. |
|  | 434-435 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR ERROR-7. |
|  | 436-438 | NUM. | 3 | CÓDIGO DE ERROR-8. |
|  | 439-440 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-8. |
|  | 441-443 | NUM. | 3 | CÓDIGO DE ERROR-9. |
|  | 444-445 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-9. |
|  | 446-448 | NUM. | 3 | CÓDIGO DE ERROR-10. |
|  | 449-450 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-10. |
|  | 451-453 | NUM. | 3 | CÓDIGO DE ERROR-11. |
|  | 454-455 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-11. |
|  | 456-458 | NUM. | 3 | CÓDIGO DE ERROR-12. |
|  | 459-460 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-12. |
|  | 461-463 | NUM. | 3 | CÓDIGO DE ERROR-13. |
|  | 464-465 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-13. |
|  | 466-468 | NUM. | 3 | CÓDIGO DE ERROR-14. |
|  | 469-470 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-14. |
|  | 471-473 | NUM. | 3 | CÓDIGO DE ERROR-15. |
|  | 474-475 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-15. |
|  | 476-478 | NUM. | 3 | CÓDIGO DE ERROR-16. |
|  | 479-480 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-16. |
|  | 481-483 | NUM. | 3 | CÓDIGO DE ERROR-17. |
|  | 484-485 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-17. |
|  | 486-488 | NUM. | 3 | CÓDIGO DE ERROR-18. |
|  | 489-490 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-18. |
|  | 491-493 | NUM. | 3 | CÓDIGO DE ERROR-19. |
|  | 494-495 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-19. |
|  | 496-498 | NUM. | 3 | CÓDIGO DE ERROR-20. |
|  | 499-500 | NUM. | 2 | NÚMERO DEL CAMPO QUE DA LUGAR AL ERROR-20. |

El formato (numérico/alfanumérico) de las posiciones 2 a 400 podría no coincidir con el indicado en la descripción de este registro, cuando se trate de registros erróneos en los que el Departamento de Informática Tributaria reproduce los datos transmitidos por las entidades.

4.7 Fichero de resultados de la validación de las contestaciones a las diligencias. Registro de control para la entidad transmisora. Registro tipo 9.

Se incluye a continuación la descripción de cada campo del registro de tipo 9 en el fichero de diligencias.

| Posición | Tipo | Longitud | Descripción del campo |
| --- | --- | --- | --- |
| 1-1 | ALF. | 1 | INDICADOR DE REGISTRO DE CONTROL PARA LA ENTIDAD TRANSMISORA. CONTENIDO: 9. |
| 2-3 | NUM. | 2 | DELEGACIÓN DE LA AGENCIA EMISORA DEL FICHERO. CONTENIDO: 57. |
| 4-7 | NUM. | 4 | CÓDIGO DE ENTIDAD TRANSMISORA. |
| 8-15 | NUM. | 8 | FECHA DE COMIENZO DE CICLO. |
| 16-24 | ALF. | 9 | POSICIONES LIBRES DE CONTENIDO. |
| 25-27 | NUM. | 3 | NÚMERO DE ENTIDADES ADHERIDAS INCLUIDAS EN EL FICHERO DE DILIGENCIAS. |
| 28-28 | ALF. | 1 | INDICADOR DE ESTADO DE LAS DILIGENCIAS PARA LA ENTIDAD TRANSMISORA. CONTENIDO: R (RECIBIDAS POR LA ENTIDAD TRANSMISORA). |
| 29-31 | NUM. | 3 | NÚMERO DE ENTIDADES ADHERIDAS DE LAS QUE HA TRANSMITIDO TRABAS LA ENTIDAD TRANSMISORA EN EL CICLO EN CURSO. |
| 32-34 | NUM. | 3 | NÚMERO DE ENTIDADES ADHERIDAS CORRESPONDIENTES A LA ENTIDAD TRANSMISORA CUYOS ENVÍOS HAN SIDO RECHAZADOS EN EL CICLO EN CURSO. |
| 35-37 | NUM. | 3 | NÚMERO DE ENTIDADES ADHERIDAS CORRESPONDIENTES A LA ENTIDAD TRANSMISORA CUYOS ENVÍOS HAN SIDO ACEPTADOS EN EL CICLO EN CURSO. |
| 38-40 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 41-43 | NUM. | 3 | POSICIONES LIBRES DE CONTENIDO. |
| 44-44 | ALF. | 1 | ESTADO GENERAL DE LA ENTIDAD TRANSMISORA PARA EL CICLO MENSUAL. CONTENIDO: P (EN PROCESO) O F (FINALIZADO). |
| 45-52 | NUM. | 8 | FECHA DE ALTA DEL REGISTRO. |
| 53-59 | NUM. | 7 | HORA DE ALTA DEL REGISTRO. |
| 60-500 | ALF. | 441 | POSICIONES LIBRES DE CONTENIDO. |

4.8 Relación de códigos de error en los resultados de la validación a las contestaciones.

| Errores comunes a todos los tipos de registro |
| --- |
| 601 | ERROR DE SECUENCIA DE REGISTROS. |
| 602 | DELEGACIÓN DE LA AGENCIA RECEPTORA DEL FICHERO DISTINTA DE 57. |
| 608 | FECHA DE COMIENZO DE CICLO INCORRECTA. |
| Registro de cabecera de entidad transmisora (Tipo 0) |
| --- |
| 003 | CÓDIGO DE ENTIDAD TRANSMISORA incorrecto. |
| 006 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS errónea. |
| 007 | INDICADOR DE TIPO DE FICHERO distinto de T. |
| Registro de cabecera de entidad (Tipo 1) |
| --- |
| 103 | CÓDIGO DE ENTIDAD incorrecto. |
| 105 | NÚMERO DE ENVÍO inexistente. |
| 106 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS errónea. |
| 107 | INDICADOR DE TIPO DE FICHERO distinto de T. |
| 110 | CÓDIGO DE ENTIDAD TRANSMISORA no corresponde con la que comenzó el ciclo. |
| 112 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del contenido en el registro de cabecera de entidad transmisora. |
| 113 | NÚMERO DE ENVÍO no numérico. |
| 114 | INDICADOR DE MONEDA distinto de E. |
| 115 | Envío para esta entidad previamente aceptado en este ciclo |
| Registro de detalle (Tipo 2) |
| --- |
| 202 | NIF DEL DEUDOR no cumplimentado. |
| 203 | NIF DEL DEUDOR incorrecto o distinto del incluido en la diligencia transmitida a la entidad. |
| 204 | NÚMERO DE DILIGENCIA DE EMBARGO no cumplimentado o incorrecto. |
| 205 | NÚMERO DE DILIGENCIA DE EMBARGO inexistente en el fichero de diligencias transmitido a la entidad. |
| 206 | IMPORTE TOTAL A EMBARGAR distinto del que figuraba en la diligencia transmitida a la entidad. |
| 207 | FECHA DE GENERACIÓN DE LA DILIGENCIA incorrecta o distinta de la que figura en la diligencia transmitida a la entidad. |
| 208 | IMPORTE TOTAL TRABADO no numérico o superior al importe a embargar indicado en la diligencia transmitida a la entidad. |
| 209 | IMPORTE TOTAL TRABADO no coincide con la suma de los importes trabados en cada una de las cuentas incluidas en la diligencia. |
| 210 | INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO, igual a 1 cuando no se han cumplimentado las 6 cuentas posibles a aportar. |
| 211 | FECHA DE TRABA O ACTUACIÓN no cumplimentada, incorrecta o menor que la fecha de generación de la diligencia. |
| 212 | FECHA LÍMITE DE INGRESO DEL IMPORTE TRABADO incorrecta, menor que la fecha de traba, no cumplimentada (siendo distinto de cero el importe total trabado) o distinta de ceros (siendo cero el importe total trabado). |
| 213 | Error en CÓDIGO DE CUENTA CLIENTE (1-6): Se comprueba que se incluyen, sin alteraciones y en el mismo orden, las mismas cuentas que figuraban en el fichero de diligencias transmitido a la entidad. Para las cuentas añadidas por la entidad se comprueba que son correctas y corresponden con la misma entidad que figuraban en las cuentas originales. Las cuentas añadidas deben figurar a continuación de las cuentas que se incluían en el fichero de diligencias, sin dejar huecos entre ellas. |
| 214 | CÓDIGO DE RESULTADO DE TRABA (1-6) distinto de los valores admitidos |
| 215 | IMPORTE TRABADO EN CUENTA (1-6) no numérico o superior al IMPORTE TOTAL A EMBARGAR de la diligencia. |
| 216 | CÓDIGO DE RESULTADO DE TRABA (1-6) incoherente con el IMPORTE TRABADO EN CUENTA (1-6). Este error se produce cuando: – El código de resultado (1-6) no es 01, 04 o 07, siendo mayor que 0 el importe trabado en la cuenta (1-6). El código de resultado (1-6) es 01, siendo nulo el importe trabado en la cuenta (1-6). |
| 217 | Existen CÓDIGOS DE CUENTA CLIENTE duplicados. |
| 218 | IMPORTE TOTAL A EMBARGAR no numérico. |
| 219 | INDICADOR DE EXISTENCIA DE MÁS CUENTAS QUE LAS APORTADAS EN ESTE REGISTRO distinto de 0 ó 1. |
| Registro de fin de entidad adherida (Tipo 3) |
| --- |
| 303 | CÓDIGO DE ENTIDAD ADHERIDA distinto del que figura en el registro de cabecera de entidad. |
| 304 | NÚMERO DE DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD ADHERIDA distinto al contenido en el fichero de diligencias transmitido a la entidad o distinto del número de registros de detalle contenidos en el fichero de contestación a las diligencias devuelto por ésta. |
| 305 | IMPORTE TOTAL A EMBARGAR DE LAS DILIGENCIAS INCLUIDAS EN EL ENVÍO A LA ENTIDAD distinto al contenido en el fichero de diligencias transmitido a la entidad. |
| 306 | IMPORTE TOTAL TRABADO POR LA ENTIDAD ADHERIDA descuadrado con importe total acumulado de los registros de detalle. |
| 308 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del que figura en el registro de cabecera de entidad adherida. |
| Registro de fin de entidad tranmisora (Tipo 8) |
| --- |
| 804 | CÓDIGO DE ENTIDAD TRANSMISORA distinto del contenido en el registro de cabecera de entidad transmisora. |
| 805 | FECHA DE CREACIÓN DEL FICHERO DE CONTESTACIÓN A LAS DILIGENCIAS distinta de la del registro de cabecera de entidad transmisora. |

5. Fichero de levantamiento de trabas.

5.1 Estructura.

El fichero de levantamientos tendrá la siguiente estructura:

![imagen](https://www.boe.es/datos/imagenes/disp/2026/146/13031_17130110_1.png)

Todos los campos que reflejen una fecha en este fichero serán numéricos de 8 posiciones, utilizando el formato AAAAMMDD.

Los campos numéricos que carezcan de contenido estarán rellenos con ceros. No se considerarán válidos en estos campos los espacios en blanco.

5.2 Fichero de levantamiento de trabas. Registro de cabecera de entidad transmisora. Registro Tipo 0.

El fichero de levantamiento de trabas comenzará con un registro de cabecera de entidad transmisora, con la siguiente configuración:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de entidad transmisora. Contenido «0». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de entidad transmisora. |
| 8-15 | 8 | NUM. | Fecha de comienzo de ciclo. |
| 16-23 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 24 | 1 | ALF. | Indicador de tipo de fichero. Contenido «L» (levantamientos). |
| 25-400 | 376 | ALF. | Posiciones libres de contenido. |

5.3 Fichero de levantamiento de trabas. Registro de cabecera de entidad adherida. Registro Tipo 1.

El primer registro para cada entidad adherida será un registro de cabecera con la siguiente configuración:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de entidad. Contenido «1». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de entidad. |
| 8-15 | 8 | NUM. | Número de envío (Año y número orden). |
| 16-23 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 24 | 1 | ALF. | Indicador de tipo de fichero. Contenido «L» (levantamientos). |
| 25-28 | 4 | NUM. | Código de entidad transmisora. |
| 29 | 1 | ALF: | Indicador de moneda Contenido «E» (céntimos de euro). |
| 30-400 | 371 | ALF. | Posiciones libres de contenido. |

5.4 Fichero de levantamiento de trabas. Registro de detalle de trabas realizadas. Registro Tipo 2.

Los registros de detalle que sigan al registro de cabecera de entidad adherida tendrán el contenido siguiente:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de detalle de levantamiento de trabas. Contenido «2». |
| 2-10 | 9 | ALF. | NIF del deudor. |
| 11-50 | 40 | ALF. | Nombre y apellidos/Razón social del deudor |
| 51-106 | 56 | ALF. | Posiciones libres de contenido. |
| 107-119 | 13 | ALF. | Número de diligencia de embargo. |
| 120-134 | 15 | NUM. | Importe total a embargar. |
| 135-142 | 8 | NUM. | Fecha de generación de la diligencia. |
| 143-157 | 15 | NUM. | Importe total trabado. |
| 158 | 1 | ALF. | Posición de contenido libre. |
| 159-166 | 8 | NUM. | Fecha de la traba. |
| 167-174 | 8 | NUM. | Fecha límite de ingreso del importe trabado. |
| 175-194 | 20 | NUM. | Código Cuenta Cliente 1 (CCC1) |
| 195-196 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC1 |
| 197-211 | 15 | NUM. | Importe a levantaren CCC1 |
| 212-231 | 20 | NUM. | Código Cuenta Cliente 2 (CCC2) |
| 232-233 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC2 |
| 234-248 | 15 | NUM. | Importe a levantar en CCC2 |
| 249-268 | 20 | NUM. | Código Cuenta Cliente 3 (CCC3) |
| 269-270 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC3 |
| 271-285 | 15 | NUM. | Importe a levantar en CCC3 |
| 286-305 | 20 | NUM. | Código Cuenta Cliente 4 (CCC4) |
| 306-307 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC4 |
| 308-322 | 15 | NUM. | Importe a levantar en CCC4 |
| 323-342 | 20 | NUM. | Código Cuenta Cliente 5 (CCC5) |
| 343-344 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC5 |
| 345-359 | 15 | NUM. | Importe a levantar en CCC5 |
| 360-379 | 20 | NUM. | Código Cuenta Cliente 6 (CCC6) |
| 380-381 | 2 | NUM. | Código de tipo de levantamiento de embargo en CCC6 |
| 382-396 | 15 | NUM. | Importe a levantar en CCC6 |
| 397-400 | 4 | ALF. | Posiciones libres de contenido. |

Los códigos de tipos de levantamiento serán:

– 01: Levantamiento total del embargo en esa cuenta.

– 02: Levantamiento parcial del embargo en esa cuenta.

– 03: No hay levantamiento en esa cuenta.

Los códigos pueden ser diferentes para las cuentas incluidas en una misma diligencia de embargo.

La estructura de este registro es un reflejo de la utilizada en el registro de detalle del fichero de resultados de trabas. Se incluirán en él tantas cuentas como haya en este último registro y en el mismo orden. Sólo podrán incluirse levantamientos en aquellas cuentas en las que se hubiera producido traba y el importe levantado no podrá superar al trabado.

Para una misma cuenta podrán producirse varias órdenes de levantamiento en días distintos dentro del mismo ciclo mensual. Cada una de ellas es independiente de las restantes, no acumulándose en los levantamientos sucesivos el importe de los transmitidos con anterioridad.

5.5 Fichero de levantamiento de trabas. Registro de fin de entidad adherida. Registro Tipo 3.

Al final de los registros de detalle de cada entidad, deberá incluirse un registro totalizador de los levantamientos. El formato será el siguiente:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de fin de entidad adherida. Contenido «3». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57». |
| 4-7 | 4 | NUM. | Código de entidad adherida. |
| 8-13 | 6 | NUM. | Número de diligencias con levantamientos incluidas en el envío a la entidad adherida. |
| 14-28 | 15 | NUM. | Importe total a levantar de las diligencias incluidas en el envío a la entidad adherida. |
| 29-43 | 15 | NUM. | Posiciones libres de contenido. |
| 44-47 | 4 | NUM. | Código de la entidad transmisora |
| 48-400 | 353 | ALF. | Posiciones libres de contenido. |

5.6 Fichero de levantamiento de trabas. Registro de fin de entidad transmisora. Registro Tipo 8.

Al final del fichero se incluye un registro de fin de entidad transmisora, o de fin de fichero, con la siguiente configuración:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de cabecera de entidad transmisora. Contenido «8». |
| 2-5 | 4 | NUM. | Código de entidad transmisora. |
| 6-13 | 8 | NUM. | Fecha de creación del fichero de levantamiento de trabas. |
| 14-400 | 387 | ALF. | Posiciones libres de contenido. |

5.7 Fichero de levantamiento de trabas. Registro de control para la entidad transmisora. Registro Tipo 9.

A continuación, se incluye la descripción de cada campo del registro de tipo 9 en el fichero de levantamientos:

| Posición | Longitud | Tipo | Descripción |
| --- | --- | --- | --- |
| 1 | 1 | ALF. | Indicador de registro de control para la entidad transmisora. Contenido «9». |
| 2-3 | 2 | NUM. | Delegación de la AEAT receptora del fichero. Contenido «57» |
| 4-7 | 4 | NUM. | Código de entidad transmisora. |
| 8-15 | 8 | NUM. | Fecha de comienzo de ciclo. |
| 16-24 | 9 | ALF. | Posiciones libres de contenido. |
| 25-27 | 3 | NUM. | Número de entidades adheridas incluidas en el fichero de levantamientos. |
| 28 | 1 | ALF. | Indicador de estado de los levantamientos para la entidad transmisora. Contenido «P» (pendiente de recuperar por la entidad transmisora) ó «R» (recibidas por la entidad transmisora). |
| 29-44 | 16 | ALF: | Posiciones libres de contenido. |
| 45-52 | 8 | NUM. | Fecha de alta del registro. |
| 53-59 | 7 | NUM. | Hora de alta del registro. |
| 60-400 | 341 | ALF: | Posiciones libres de contenido. |

Este registro contendrá, en caso de ausencia de nuevos datos de levantamientos, una «R» en la posición 28.

Para mantener la coherencia del procedimiento, cuando una entidad transmisora comience a funcionar con este sistema, antes de que se produzca la transmisión del primer fichero con levantamientos el Departamento de Informática Tributaria generará y pondrá a disposición de la entidad un fichero con un único registro de tipo 9 en el que los campos «NUMERO DE ENTIDADES ADHERIDAS INCLUIDAS EN EL FICHERO DE LEVANTAMIENTOS» y «FECHA DE COMIENZO DE CICLO» estarán rellenos con ceros, situación que se repetirá en ausencia de nuevos datos.

Con ello se evita que se produzca un error en la comunicación cuando la entidad intente recuperar un fichero de levantamientos, una vez aceptados los resultados de alguna de las entidades adheridas a las que da servicio, sin que haya realizado todavía ningún levantamiento.

Este es el único caso en el que un campo de tipo fecha («FECHA DE COMIENZO DE CICLO») carece de una estructura AAAAMMDD válida, puesto que estará relleno con ceros.
