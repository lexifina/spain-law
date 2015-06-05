## ANEXO

## Formatos relativos a los ficheros de curvas de carga horaria

Los ficheros F5D y P5D serán ficheros planos de texto con las siguientes características generales:

a) El fichero estará en ASCII.

b) Cada nueva versión de los ficheros publicada a lo largo de un día para un CUPS contendrá información incremental respecto a la versión anterior, de forma que, para disponer de toda la información publicada un día, será necesario tener en cuenta las diferentes versiones publicadas ese día.

De publicarse la información fraccionada en varios ficheros por día, se emplearán versiones consecutivas con el mismo nombre empezando por la versión 0.

Para rectificar información horaria en un mismo día ya publicada, se incluirá la información de medida horaria rectificada en un fichero del mismo nombre pero de versión posterior.

La carga secuencial de los ficheros publicados por el distribuidor al comercializador garantizará la correcta actualización de la misma.

c) El carácter «;» (punto y coma) delimita el final de cada campo, incluido el final de cada línea.

d) Los campos sin dato deberán dejarse vacíos (sin insertar ningún valor ni espacios) pero con separadores.

e) Los datos de medidas de un mismo suministro irán consecutivos en el fichero y ordenados del más antiguo al más moderno, según el campo de tipo fecha del formato del fichero.

f) En los campos de fechas en que figure la hora se entenderá ésta en el formato 00 <= hh < 24, es decir, el periodo 24 figurará como la hora 00, con fecha del día siguiente a la que se ha producido el consumo.

g) El día de cambio horario de invierno a verano tiene 23 horas y no existirá la hora 2. La hora 1 llevará la bandera de estación a 0 (invierno) y la hora 3 llevará la bandera de estación a 1 (verano).

El día de cambio horario de verano a invierno tiene 25 horas y en él se repetirá la hora 2 en: hora 2 con bandera de estación a 1 (verano), y hora 2 con bandera de estación a 0 (invierno).

Los ficheros F5D, P5D y CCH_CONS tendrán los siguientes formatos:

Fichero F5D (CCH_FACT)

| Datos horarios de energía incremental de puntos frontera de cliente tipo 5 | F5D_DIS_COM_ aaaammdd.v |
| --- | --- |
| Objeto | Comunicación de datos horarios de energía incremental en punto frontera de cliente |
| Parámetros | aaaammdd: Fecha de generación del fichero v: versión del fichero |
| Tipo de fichero | COM |
| Emisor | DIST |
| Receptor | COM |
| Categoría | Curva de carga horaria |
| Periodicidad | Diaria |
| Observaciones |  |
| Cód. | Descripción del campo | Formato |
| A | Código universal de punto de suministro | 22*c |
| B | Fecha y hora de la medida (1) Horas de 0 a 23 | aaaa/mm/dd hh:mi |
| C | Bandera verano/invierno (2) | 1*c |
| D | Medida de la magnitud activa entrante (3) | 10*n |
| E | Medida de la magnitud activa saliente (4) | 10*n |
| F | Medida de la magnitud reactiva Cuadrante 1 (4) | 10*n |
| G | Medida de la magnitud reactiva Cuadrante 2 (4) | 10*n |
| H | Medida de la magnitud reactiva Cuadrante 3 (4) | 10*n |
| I | Medida de la magnitud reactiva Cuadrante 4 (4) | 10*n |
| J | Método de obtención (5) | 2*n |
| K | Indicador de firmeza (6) | 1*n |
| L | Código de factura de acceso (7) | 26*c |

Notas:

(1) Las etiquetas de tiempo de cada periodo corresponden al final del periodo de integración de energía.

(2) Podrá tomar los siguientes valores: 0 Invierno 1 Verano.

(3) Campo obligatorio, en Wh.

(4) Campo no obligatorio, en Wh/VArh según corresponda.

(5) De 1 a 6 de acuerdo al cálculo de mejor de energía en punto frontera:

1. Medida real válida.

2. Medida perfilada a partir de saldo ATR real de acuerdo con lo establecido en el apartado 6.4.a) y 6.4.b) del Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

3. Medida ajustada a un saldo ATR real de acuerdo con lo establecido en el apartado 6.4.c) y 6.4.d) del Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

4. Medida perfilada a partir de autolectura de acuerdo a lo establecido en el apartado 6.4.a) o 6.4.b) del Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

5. Medida perfilada a partir de estimación por consumo histórico del año anterior de acuerdo a lo establecido en el apartado 6.4.a) o 6.4.b) del Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

6. Medida perfilada a partir de estimación por factor de utilización de acuerdo a lo establecido en el apartado 6.4.a) o 6.4.b) del Procedimiento para la comprobación, validación y cálculo del mejor valor de energía de los datos procedentes de los equipos de medida tipo 5 efectivamente integrados en el sistema de telegestión.

(6) 0 Provisional, 1 Firme de acuerdo a lo establecido en el PO 10.5.

(7) Toma el valor del campo numerofactura del formato F1 de facturación.

Fichero P5D (CCH_VAL)

| Datos horarios de energía incremental validada de puntos frontera de cliente tipo 5 | P5D_DIS_COM_ aaaammdd.v |
| --- | --- |
| Objeto | Comunicación de datos horarios de energía incremental validada en punto frontera de cliente |
| Parámetros | aaaammdd: Fecha de generación del fichero v: versión del fichero |
| Tipo de fichero | COM |
| Emisor | DIST |
| Receptor | COM |
| Categoría | Curva de carga horaria |
| Periodicidad | Diaria |
| Observaciones |  |
| Cód. | Descripción del campo | Formato |
| A | Código universal de punto de suministro | 22*c |
| B | Fecha y hora de la medida (1) Horas de 0 a 23 | aaaa/mm/dd hh:mi |
| C | Bandera verano/invierno (2) | 1*c |
| D | Medida de la magnitud activa entrante (3) | 10*n |
| E | Medida de la magnitud activa saliente (4) | 10*n |

Notas:

(1) Las etiquetas de tiempo de cada periodo corresponden al final del periodo de integración de energía.

(2) Podrá tomar los siguientes valores: 0 Invierno 1 Verano.

(3) Campo obligatorio, en Wh.

(4) Campo no obligatorio, en Wh.

Fichero CCH-CONS

| Datos horarios de energía incremental de puntos frontera de cliente tipo 5 |  |
| --- | --- |
| Objeto | Comunicación de datos horarios de energía al consumidor en kWh |
| Cód. | Descripción del campo | Formato |
| A | Código universal de punto de suministro | 22*c |
| B | Fecha de la medida (1) | dd/mm/aaa |
| C | Hora de la medida Horas de 1 a 24 (2) | 2*n |
| D | Medida de la magnitud activa entrante (3) | n(7,3) |
| E | Método de obtención (4) | 1*c |

Notas:

(1) Las etiquetas de fechas de cada periodo corresponden a día donde se realizar el consumo.

(2) El día del cambio de hora de invierno a verano tendrá el formato de 1-23 y el día del cambio de verano a invierno tendrá el formato de 1-25.

(3) En kWh con 3 decimales. Se utilizará la coma «,» como separador de los decimales.

(4) R (real, para el valor 01 del campo «Método de obtención» del formato de fichero F5D) o E (estimado, para los valores 02, 03, 04, 05 y 06 del mencionado campo).
