## ANEXO VII

## Diseño de registro y contenido de los ficheros NppmmmIA.aaa y PppmmmIA.aaa

El diseño de registro de estos ficheros es el de intercambio con cola de errores (704 posiciones) figurando en datos de inicio los datos que figuran en la base padronal del INE en el momento de la comparación, y en datos tras variación los remitidos por el Ayuntamiento en su fichero C.

Los ficheros NppmmmIA.aaa y PppmmmIA.aaa contienen los registros no cargados en la base padronal del INE correspondientes a los ficheros EppmmmAI.aaa y OppmmmAI.aaa, respectivamente, remitidos por los Ayuntamientos al INE como respuesta a los ficheros EppmmmIA.aaa y OppmmmIA.aaa.

Los distintos motivos por los que no ha sido posible cargar los registros son los siguientes:

1. No se ha localizado al habitante en la base padronal del INE.

2. Registro con alguno de los siguientes errores: 23-34, 36-39, 47-66, 70. En este caso, irá marcado en la cola de error con una «X» en la posición correspondiente.

3. Existen movimientos posteriores al registro enviado por el Ayuntamiento en el fichero EppmmmAI.aaa u OppmmmAI.aaa.

4. Se ha encontrado más de un habitante en la base padronal del INE sobre el que cargar dicho registro.

5. Registro con CNES (código de nivel de estudios) inferior al que figura en la base padronal del INE o CNES=99, salvo en los siguientes supuestos, en cuyo caso sí se permitirá la incorporación del registro a la base:

a) Cuando afecte a un menor de hasta 16 años y sea igual a 00.

b) Cuando CNES de la base padronal del INE sea 21: Sin estudios y el CNES del registro remitido por el Ayuntamiento en el fichero EppmmmAI.aaa u OppmmmAI.aaa sea 20: Titulación inferior a Graduado Escolar.

1 La descripción de los errores figura en el documento Normas para el tratamiento de las incidencias resultantes de la incorporación de las variaciones mensuales a los ficheros padronales del INE, que figura en IDA-Padrón (apartado Diseños de registro).
