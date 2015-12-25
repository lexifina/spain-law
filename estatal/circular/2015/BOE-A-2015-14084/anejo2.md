## ANEJO 2

## Registro detalle de los depósitos recibidos

El archivo tendrá las siguientes características:

• Archivo de texto en código ASCII.

• Caracteres admitidos: letras mayúsculas, números, signos «+» y «-».

• Los registros se atendrán a lo especificado en el siguiente diseño.

• Un registro por titular y depósito o fondos no registrados como depósito, procedente de situaciones transitorias por operaciones de tráfico; se incluirán tantos registros como depósitos tenga el titular; en los depósitos con varios titulares, su importe se dividirá entre los titulares, de acuerdo con lo previsto en el contrato de depósito y, en su defecto, a partes iguales, conforme al artículo 7 del Real Decreto 2606/1996. En el registro se incluirán los depósitos y fondos de las sociedades no financieras, los hogares y las Administraciones Locales con un presupuesto anual igual o inferior a 500.000 euros con independencia de que los depósitos y fondos no sean admisibles para su cobertura por el Fondo de Garantía de Depósitos.

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_002.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_003.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_004.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_005.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_006.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2015/307/14084_007.png)

| Descripción |  |  |
| --- | --- | --- |
| CAMPO 1 |  | USO PROPIO |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 2 |
|  | CONTENIDO: | Siempre con espacios. |
| CAMPO 2 |  | DNI/NIF |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 10 |
|  | CONTENIDO: | Número de DNI o NIF del titular del depósito. |
| CAMPO 3 |  | DIRECCIÓN |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 43 |
|  | CONTENIDO: | Domicilio del titular del depósito. |
| CAMPO 4 |  | POBLACIÓN |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 30 |
|  | CONTENIDO: | Población del titular del depósito. |
| CAMPO 5 |  | PROVINCIA |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 20 |
|  | CONTENIDO: | Provincia del titular del depósito. |
| CAMPO 6 |  | DISTRITO POSTAL |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 5 |
|  | CONTENIDO: | Distrito postal del titular del depósito. En caso de no tener distrito postal, se rellenará con ceros. |
| CAMPO 7 |  | PAÍS |
|  | FORMATO: | Alfabético |
|  | LONGITUD: | 2 |
|  | CONTENIDO: | Código ISO del país del titular del depósito. |
| CAMPO 8 |  | FECHA DE VENCIMIENTO |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 8 |
|  | CONTENIDO: | Formato AAAAMMDD (solo se completará si el depósito tiene vencimiento; en caso contrario, se rellenará con ceros). |
| CAMPO 9 |  | IMPORTE |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 15 |
|  | CONTENIDO: | Importe principal o nominal más los intereses devengados a la fecha a la que se refieren los datos del depósito con dos decimales y signo (si es negativo, la primera posición será «–»; si es positivo, «+»); siempre se completará con ceros a la izquierda. |
|  |  | Los depósitos no denominados en euros se convertirán a euros aplicando el tipo de cambio correspondiente a la fecha de referencia de los datos. |
| CAMPO 10 |  | IMPORTE ESPECIALMENTE PROTEGIDO |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 15 |
|  | CONTENIDO: | Cuantía que, estando incluida en el saldo positivo de la cuenta o depósito de que se trate, corresponda a importes especialmente protegidos, conforme estos se definen en la nota (i) del estado «Base para el cálculo de las aportaciones al Fondo de Garantía de Depósitos». Por tanto, este importe será positivo e igual o menor que el saldo de la cuenta de que se trate consignado en el campo IMPORTE. |
|  |  | Importe con dos decimales y signo (la primera posición contendrá el signo «+»); siempre se completará con ceros a la izquierda. Este campo solo se completará en el caso de que existan depósitos especialmente garantizados; en caso contrario, siempre con ceros. |
|  |  | Los depósitos no denominados en euros se convertirán a euros aplicando el tipo de cambio correspondiente a la fecha de referencia de los datos. |
| CAMPO 11 |  | NÚMERO DE TITULAR |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 2 |
|  | CONTENIDO: | Indicará el número de orden que le corresponde en el número total de titulares del depósito. |
| CAMPO 12 |  | CÓDIGO DEL DEPÓSITO (REGISTRADO EN ESPAÑA). ENTIDAD |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 4 |
|  | CONTENIDO: | Código de entidad que figura en el código del depósito. |
| CAMPO 13 |  | CÓDIGO DEL DEPÓSITO (REGISTRADO EN ESPAÑA). OFICINA |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 4 |
|  | CONTENIDO: | Código de oficina que figura en el código del depósito. |
| CAMPO 14 |  | CÓDIGO DEL DEPÓSITO (REGISTRADO EN ESPAÑA). D. C. |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 2 |
|  | CONTENIDO: | Dígitos de control que figuran en el código del depósito. |
| CAMPO 15 |  | CÓDIGO DEL DEPÓSITO (REGISTRADO EN ESPAÑA). NÚMERO DEL DEPÓSITO |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 10 |
|  | CONTENIDO: | Número asignado a la cuenta o depósito que figura en el código del depósito. |
| CAMPO 16 |  | NOMBRE DEL TITULAR |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 55 |
|  | CONTENIDO: | Nombre del titular del depósito. |
| CAMPO 17 |  | TIPO DE DEPÓSITO |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 3 |
|  | CONTENIDO: | Código que la entidad asigne al tipo de depósito de que se trate. |
| CAMPO 18 |  | DEPÓSITO EN GARANTÍA |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 1 |
|  | CONTENIDO: | Depósito pignorado o afecto en garantía de otras operaciones (siempre «S» o «N»). |
| CAMPO 19 |  | NÚMERO TOTAL DE TITULARES |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 3 |
|  | CONTENIDO: | Número total de titulares de la cuenta o depósito. Siempre será número mayor que cero. |
| CAMPO 20 |  | CÓDIGO DE LA DIVISA |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 3 |
|  | CONTENIDO: | Código de ISO de la divisa en la que esté denominado el depósito. Solo se completará cuando el depósito no sea en euros. |
| CAMPO 21 |  | CANTIDAD DE DIVISAS |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 15 |
|  | CONTENIDO: | Solo se completará en el caso de que el depósito sea una divisa; en caso contrario, se completará siempre con ceros. |
| CAMPO 22 |  | CANTIDAD DE DIVISAS EN IMPORTES ESPECIALMENTE PROTEGIDOS |
|  | FORMATO: | Numérico |
|  | LONGITUD: | 15 |
|  | CONTENIDO: | Cuantía que, estando incluida en el saldo positivo de la cuenta o depósito de que se trate, corresponda a importes, no denominados en euros, especialmente protegidos, conforme estos se definen en la nota (i) del estado «Base para el cálculo de las aportaciones al Fondo de Garantía de Depósitos». Por tanto, este importe será positivo e igual o menor que el saldo de la cuenta de que se trate consignado en el campo CANTIDAD DE DIVISAS. |
|  |  | Importe con dos decimales y signo (la primera posición contendrá el signo «+»); siempre se completará con ceros a la izquierda. |
|  |  | Solo se completará si existen importes especialmente garantizados no denominados en euros; en caso contrario, siempre con ceros. |
| CAMPO 23 |  | ADMISIBLE |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 1 |
|  | CONTENIDO: | Indica si el depósito es admisible para estar garantizado por el Fondo de Garantía de Depósito (siempre «S» o «N»). |
| CAMPO 24 |  | CÓDIGO DEL DEPÓSITO (REGISTRADO EN UNA SUCURSAL DE OTRO PAÍS DE LA UE) |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 30 |
|  | CONTENIDO: | Solamente se completará si el depósito está registrado en una sucursal radicada en otro Estado miembro de la Unión Europea. En este caso, no se completarán los campos 12 a 14 correspondientes al código de los depósitos registrados en España. |
| CAMPO 25 |  | ESPACIO RESERVADO |
|  | FORMATO: | Alfanumérico |
|  | LONGITUD: | 19 |
|  | CONTENIDO: | Siempre con espacios. |
