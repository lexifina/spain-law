## ANEXO IV

## Diseño de registro y contenido del fichero de alegaciones AppmmmAI.aaa

El diseño de registro del fichero AppmmmAI.aaa tendrá la misma estructura y contenido que el fichero de reparos, RppmmmIA.aaa, con dos campos finales adicionales:

– CALEG, Clave de Alegación (A5).

– OBSVR, Observaciones (A200).

En el campo CALEG se especificará la clave de alegación según la tabla anexa y en el campo OBSVR, el Ayuntamiento podrá especificar lo que considere conve¬niente, en relación con el registro sobre el que presenta la alegación.

Para cada registro sobre el que se alegue deberá venir cumplimentado el valor TIPOINF=D, R o S remitido por el INE en el fichero de reparos. Asimismo, en el resto de campos coincidentes con el fichero de reparos, se mantendrá el mismo contenido enviado, pues en caso de modificar alguno de los campos previos la alegación no podrá ser atendida, con las siguientes salvedades:

– Registros devueltos en el fichero de reparos con CDEV=IN.–Se podrán modificar exclusivamente los campos afectados por el error invalidante marcado en la cola de errores.

– Registros devueltos con TIPOINF=D.–Deberá rectificarse el valor de CVAR, CAUV o FVAR en el caso de que los enviados en el fichero CppmmmAI fueran valores no admitidos o fuera de rango respectivamente.

– Registros devueltos con TIPOINF=S. Sólo pueden alegarse de BAJA.–En FVAR se consignará la fecha con la que ha sido dado de baja en el Padrón del Ayuntamiento y en CVAR+CAUV la causa de variación de la baja. En caso de no modificarse estos campos la baja se repercutirá en la base del INE como B II con fecha 31 de diciembre del año anterior a la fecha de referencia.

– Registros alegados con CALEG=EXTRJ. Cuando se alegue por renovación de la inscripción de un ENCSARP en FVAR deberá consignarse la fecha de la renovación.

– Registros alegados con CALEG=IN135.–Deberán cumplimentarse las variables: TIDEN, LEXTR, IDEN y LIDEN, de la parte de los datos tras variación, con la información relativa al documento (DNI o NIEX) expedido por el Ministerio del Interior incluido en la comunicación de la incidencia 135 por parte del INE.

– Registros alegados con CALEG=IN137.–Deberán cumplimentarse con CVAR=M, CAUV=PE e incluyendo en los campos TIDEN, LEXTR, IDEN y LIDEN, de la parte de los datos tras variación, la información relativa al DNI expedido por el Ministerio del Interior incluida en la comunicación de la incidencia 137 por parte del INE, así como la NACI=108, NDOCU=blanco y resto de los campos de identificación (nombre, apellidos, incluidas partículas de apellidos, fecha de nacimiento) que hayan podido verse modificados por la adquisición de la nacionalidad española.

Reparos con CDEV=NE, GE o IN y CVAR=’M’ que sean alegados con CALEG= CINEX, GEST, ERR99 o INVAL. Deberán cumplimentarse las variables: CVAR, CAUV y FVAR con los valores del ALTA en el municipio previa a la modificación que el Ayuntamiento envió en su fichero C de cifras, manteniéndose el resto de campos con los correspondientes a la modificación, al tener que ser coincidentes con los que figuran en el fichero de reparos enviado por el INE. No obstante, en el caso de los reparos CDEV=IN se deberán corregir además los posibles campos afectados por el error.

Estas especificaciones podrían verse ampliadas, en cuyo caso se actualizarán y publicarán a través del aplicativo IDA_Padrón.

Valores posibles del campo CLAVE de ALEGACIÓN para reparos devueltos con TIPOINF=R o S.

Están determinadas por los valores TIPOINF, CDEV y Errores incluidos en el fichero de Reparos.

| TIPOINF | CDEV | ERROR | PRETENSION AY. | CALEG | Observaciones |
| --- | --- | --- | --- | --- | --- |
| R | IN | * | Contar en cifras. | INVAL |  |
| R | NO | 72 | Contar en cifras. | ANA72 |  |
| R | NO | 77 | Contar en cifras. | BDE77 |  |
| R | NO | 82 | Contar en cifras. | BDE82 |  |
| R | NO | 76 | Contar en cifras. | BCR76 |  |
| R | NO | 80 | Contar en cifras. | FBCR |  |
| R | NO | 83X | Contar en cifras. | FBDU |  |
| R | NO | 84X | Contar en cifras. | FBDU |  |
| R | NO | 101 | Contar en cifras. | FBCR | ** |
| R | NO | 101 | Contar en cifras. | FBDU | ** |
| R | NO | 101 | Contar en Cifras. | IN101 | ** |
| R | NO | 106 | Contar en cifras. | FBCR |  |
| R | NO | 114 | Contar en cifras. | DU114 |  |
| R | NO | 115 | Contar en cifras. | CR115 |  |
| R | NO | 116 | Contar en cifras. | CR116 |  |
| R | NO | 112 | Contar en cifras. | EXTRJ |  |
| R | NO | 135 | Contar en cifras. | IN135 |  |
| R | NO | 137 | Contar en cifras. | IN137 |  |
| R | NO | 144 | Contar en cifras. | IN144 |  |
| R | NO | 141 | Contar en cifras. | NOENC |  |
| R | NO | 142 | Contar en cifras. | NOENC |  |
| R | NO | 143 | Contar en cifras. | NOENC |  |
| R | GE | * | Contar en cifras. | GEST |  |
| R | GE | 99 | Contar en cifras. | ERR99 |  |
| R | NE |  | Contar en cifras. | CINEX |  |
| S |  |  | No contar en cifras. | BAJA |  |

* Error invalidante o de gestión en su caso.

** Según el 101 proceda de una confirmación de BCR, BDU o BII/BBC respectivamente.

CALEG válidas para reparos con TIPOINF=D.

En el caso de los Reparos con TIPOINF=D, como no se han podido contrastar, deberá comprobarse la situación en la base padronal del INE a través de IDA_Padrón, de modo que si el registro ya existe en la base del INE deberá utilizarse la CALEG correspondiente al error que haya impedido su contabilización.

La CALEG=CINEX únicamente deberá utilizarse tras comprobar que el habitante no existe en la base del INE (o se encuentra indebidamente de baja) para evitar la generación de duplicados.

| Situación en IDA_Padrón a 1 de enero |
| --- |
| TIPOINF | Consultas Padronales | Errores Pendientes | PRETENSION AY. | CALEG | Observaciones |
| D | Existe. | ANA72 | Contar en cifras. | ANA72 |  |
| D | Existe. | BDE77 | Contar en cifras. | BDE77 |  |
| D | Existe. | BDE82 | Contar en cifras. | BDE82 |  |
| D | Existe. | BCR76 | Contar en cifras. | BCR76 |  |
| D | Existe. | BCR80 | Contar en cifras. | FBCR |  |
| D | Existe. | BDU 83 X | Contar en cifras. | FBDU |  |
| D | Existe. | BDU 84 X | Contar en cifras. | FBDU |  |
| D | Existe. | BCR101 | Contar en cifras. | FBCR |  |
| D | Existe. | BDU101 | Contar en cifras. | FBDU |  |
| D | Existe. | BBC/BII 101 | Contar en Cifras. | IN101 |  |
| D | Existe. | BCR106 | Contar en cifras. | FBCR |  |
| D | Existe. | BDU114 | Contar en cifras. | DU114 |  |
| D | Existe. | BCR115 | Contar en cifras. | CR115 |  |
| D | Existe. | BCR116 | Contar en cifras. | CR116 |  |
| D | Existe. | BBC111 | Contar en cifras. | EXTRJ |  |
| D | Existe. | MPE135 | Contar en cifras. | IN135 |  |
| D | Existe. | MPE137 | Contar en cifras. | IN137 |  |
| D | Existe. | BII144 | Contar en cifras. | IN144 |  |
| D | Existe. | BII141 | Contar en cifras. | NOENC |  |
| D | Existe. | BII142 | Contar en cifras. | NOENC |  |
| D | Existe. | BII143 | Contar en cifras. | NOENC |  |
| D | No existe o está de baja sin error. |  | Contar en cifras. | CINEX | * |

* Deberá justificarse documentalmente que la baja es errónea.

Descripción de claves:

ANA72: Alta por nacimiento no existente en Registro Civil, requiere documentación.

BDE82: Defunción errónea, generada por Registro Civil, requiere documentación.

BCR76: Rechazo de baja por cambio de residencia con destino al extranjero, requiere documentación.

BDE77: Defunción errónea, no encontrada en Registro Civil, enviada erróneamente por el Ayuntamiento.

CINEX: Ciudadano inexistente en base del INE.

INVAL: Ciudadano devuelto con error invalidante.

GEST: Ciudadano devuelto con error de gestión.

FBDU: Falso duplicado, se acompaña documentación justificativa.

FBCR: Falso duplicado, se acompaña documentación justificativa.

ERR99: Habitante devuelto con error 99.

EXTRJ: Inscripción de extranjero no caducada, requiere documentación.

CR115: Expulsión de extranjero errónea, requiere documentación.

CR116: Baja por retorno voluntario errónea, requiere documentación.

DU114: Duplicado erróneo, requiere documentación.

IN101: Baja por caducidad o por inscripción indebida con error 101, requiere documentación.

IN135: Habitante mayor de 16 años con identificador, para el que el INE haya comunicado el mismo mediante la incidencia 135.

IN137: Habitante extranjero que ha adquirido la nacionalidad española, para el que el INE ha comunicado la adquisición, n.º de DNI y cambios en nombre, apellidos o fecha de nacimiento, mediante la incidencia 137.

IN144: Habitante español mayor de 16 años con DNI, requiere DNI.

NOENC: NO_ENCSARP continúa residiendo en el municipio, requiere documentación.

BAJA: Habitante baja en Padrón del Ayuntamiento.

Esta relación podrá modificarse en el transcurso de las distintas revisiones anuales, procediéndose a su actualización en la página web de IDA-Padrón, previo informe favorable del Consejo de Empadronamiento.
