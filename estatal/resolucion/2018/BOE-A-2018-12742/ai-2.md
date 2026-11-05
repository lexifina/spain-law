## ANEXO II

## Diseño de registro y contenido del fichero de reparos RppmmmIA.aaa

El fichero RppmmmIA.aaa tendrá estructura de fichero de intercambio con cola de errores de 150 posiciones y un campo adicional para una denominación de fichero, que se añade al final de la cola de errores, con una longitud de 45 posiciones.

Este fichero contendrá tres tipos de registros que se distinguirán por el valor de TIPOINF=D, R o S.

Registros D:

Son los registros que no han pasado la validación del apartado VII. Estarán cumplimentados del siguiente modo:

TIPOINF: D.

CDEV: En blanco.

Resto de datos: Los que consten en el fichero CppmmmAI.aaa.

Cola de errores: En blanco.

Nombre del fichero: En blanco.

Registros S:

Son los registros contabilizados por el INE que no se han encontrado en el fichero CppmmmAI.aaa.

Datos de identificación: Los que figuren en el fichero del INE.

CVAR+CAUV: Los que figuren en el fichero del INE.

TIPOINF: S.

CDEV: En blanco.

FVAR: La que conste en el fichero del INE.

Datos tras variación: Los que consten en fichero del INE.

Cola de errores: En blanco.

Nombre del fichero: En blanco.

Registros R:

Registros que figuran en el fichero del Ayuntamiento y que el INE no ha contabilizado.

Datos de identificación: Los que consten en el fichero CppmmmAI.aaa.

CVAR+CAUV: Los que figuren en el fichero CppmmmAI.aaa.

TIPOINF: R.

CDEV:

NO, registro que consta en base INE con alguna incidencia pendiente (1).

GE, registro devuelto por error de gestión (2).

IN, registro devuelto por error invalidante.

NE, registros no encontrados en la base del INE.

FVAR: La que conste en el fichero justificativo CppmmmAI.aaa.

Datos tras variación: Los que consten en el fichero CppmmmAI.aaa.

Cola de errores: Cumplimentada con el último error/incidencia de esa variación comunicado al Ayuntamiento que impide su contabilización.

Nombre el fichero: Fichero en el que fue remitido al Ayuntamiento la comunicación del último error/incidencia de esa variación que impide su contabilización.

(1) Incidencias pendientes:

– A NA error 72.

– B CR pendientes con errores 76, 80,106.

– B DE pendiente con error 82.

– B DE confirmada con error 77.

– B DU pendiente con error 83, 84 X.

– Baja confirmada con error 101.

– Habitante no contabilizado por caducidad de la inscripción, error 112.

– Baja por cambio de residencia por expulsión de extranjero ejecutada, error 115.

– Baja por duplicado gestionada por la OCE, error 114.

– Baja por cambio de residencia de extranjero (o familiar de) por retorno voluntario a su país de origen, error 116.

– Inscripción afectada por la incidencia 135 (habitantes mayores de 16 años sin identificador, para los que el INE ha comunicado el DNI/NIEX mediante esta incidencia).

– Inscripción afectada por la incidencia 137 (comunicación del DNI expedido por adquisición de nacionalidad española por el Ministerio del Interior; se trata de inscripciones que constan como extranjeros no actualizadas).

– Inscripción afectada por la incidencia 144 (habitante español mayor de 16 años que no figura en la base de DNIs), comunicada antes del 1 de octubre del año anterior.

– Inscripción de extranjero NO_ENCSARP afectada por alguna de las incidencias 141, 142 o 143 de comprobación de residencia, comunicadas antes del 1 de octubre del año anterior.

(2) Errores de gestión:

– 71 Alta ya existente en el municipio.

– 78 Modificación no encontrada.

– 79 Habitante con movimiento pendiente de confirmación o rechazo.

– 89 Habitante fallecido.

– 92 Existe par alta-baja con la misma fecha de variación para el mismo habitante.

– 99 Habitante con movimiento posterior al comunicado.

Estas relaciones podrían verse ampliadas, previo informe favorable del Consejo de Empadronamiento, en cuyo caso se actualizará y publicará a través del aplicativo IDA_Padrón.
