## ANEXO I

## Especificaciones del fichero CppmmmAI.aaa

El fichero CppmmmAI.aaa, donde pp es el código de provincia, mmm es el código de municipio y aaa son las tres últimas cifras del año correspondiente a la revisión, se ajustará al diseño de registro de los ficheros de intercambio publicados en IDA-Padrón para padrones completos. Es decir, con los datos de inicio y tras variación cumplimentados, con los datos iguales en los campos coincidentes.

También estarán cumplimentados los campos FVAR, CVAR y CAUV con los datos correspondientes a la última variación (de alta o modificación), vigente a 31 de diciembre del año anterior a la fecha de referencia de las cifras, y enviada por el Ayuntamiento al INE.

No se incluirán bajas.

Los valores válidos para los campos CVAR y CAUV son los siguientes:

CVAR+CAUV:

Blanco (para las altas iniciales de la renovación a 1-5-96)

AOM

ACR

ANA

MPE

MRD

MCD

MRN

MCO

Esta relación podría verse ampliada, previo informe favorable del Consejo de Empadronamiento, en cuyo caso se actualizará y publicará a través del aplicativo IDA_Padrón.

El fichero se remitirá al INE mediante el aplicativo IDA-Padrón y se obtendrá de acuerdo a las siguientes características:

Para ficheros obtenidos con MS-DOS/Windows:

– Longitud de registro: Fija con 554 posiciones para los datos.

– Caracteres de control de fin de línea: Cada registro debe terminar en los caracteres de control CR y LF (en este orden), sus equivalentes en Hexadecimal y en Decimal son 0D, 0A y 13,10 respectivamente.

– Carácter de fin de fichero: Ninguno.

Para ficheros obtenidos con UNIX:

– Longitud de registro: Fija con 554 posiciones para los datos.

– Caracteres de control de fin de línea: Cada registro debe terminar con el carácter de control LF, sus equivalentes en Hexadecimal y en Decimal es 0A y 10 respectivamente.

– Carácter de fin de fichero: Ninguno.
