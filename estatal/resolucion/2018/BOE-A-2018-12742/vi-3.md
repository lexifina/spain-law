## VIII. Comparación con el fichero del INE y formulación de reparos mediante el fichero RppmmmIA.aaa

La comparación entre el fichero CppmmmAI.aaa remitido por el Ayuntamiento y la información que consta en poder del INE, a partir de la cual se ha obtenido la cifra comunicada, se realizará sólo con los ficheros que hayan superado la validación anterior, y sin los registros marcados con TIPOINF=D.

El INE iniciará en la fecha establecida en el calendario anual la comparación de los ficheros CppmmmAI.aaa de forma simultánea para todos los ficheros recibidos. Por tanto, no se considerará ningún fichero recibido con posterioridad a la fecha fijada.

El contraste se realizará por comparación de los campos CPRO, CMUN y los siguientes campos tras variación: NOMB, APE1, APE2, IDEN, NDOCU, NIA, CPRON, CMUNN y FNAC, previa normalización de los campos numéricos y alfabéticos.

La comparación dará lugar a registros S, contabilizados por el INE y no encontrados en el fichero del Ayuntamiento, y registros R, contabilizados por el Ayuntamiento y no por el INE, que este último intentará casar entre sí (pues puede haber registros R y S que se refieran al mismo habitante pero que no se identifiquen por los campos de contraste del párrafo anterior).

De este modo se generarán dos ficheros:

– El fichero RppmmmIA.aaa, específico de reparos (cuando las cifras del INE y el Ayuntamiento sean distintas), que contendrá los registros R y S no casados entre sí y los registros D que no han superado la validación.

– Un fichero EppmmmIA.aaa, en el que se incluirán los registros R/D y S casados entre sí, que supuestamente se refieren al mismo habitante pero que presentan diferencias en los datos de identificación.

Los diseños de registro y contenido de estos ficheros se incluyen en los Anexos II y III respectivamente.

El fichero de reparos, RppmmmIA.aaa, se pondrá a disposición de los Ayuntamientos a través del aplicativo IDA-Padrón antes de la fecha establecida en el calendario anual de cifras, junto con un resumen de su contenido, que cumplirá la siguiente fórmula:

Cifra del Ayuntamiento – registros D – registros R + registros S = Cifra del INE.

Con la puesta a disposición de este fichero, cuando el INE no esté de acuerdo con la cifra remitida por el Ayuntamiento, se dará cumplimiento a la formulación de los reparos según lo previsto en el artículo 82.1 del Reglamento de Población y Demarcación Territorial de las Entidades Locales.

Asimismo y con el fin de corregir las diferencias de identificación que pudieran existir entre la base de datos que mantiene el INE y el Padrón de cada municipio, se facilitará al Ayuntamiento el fichero EppmmmIA.aaa, con formato de intercambio de modificación. Este fichero se cumplimentará en la parte de inicio con los datos de identificación correspondientes al registro contabilizado de la base del INE y en los datos tras variación con los correspondientes al registro enviado por el Ayuntamiento en su fichero CppmmmAI.aaa con el que se ha casado (anexo III).

Desligado del procedimiento de la revisión, el Ayuntamiento podrá enviar al INE este fichero, o los registros del mismo que estime conveniente, en un único fichero con la denominación EppmmmAI.aaa (AI), a la mayor brevedad y, en todo caso, antes de que acabe el año. El INE incorporará a su base de datos las modificaciones sin generar variación y sin comunicar error o incidencia alguna a los Ayuntamientos en los ficheros de devolución mensual, aunque se generará un fichero NppmmmIA.aaa con información de los registros no cargados, cuya descripción se incluye en el Anexo VII.

Por otro lado puede ocurrir que, aun cuando las cifras del INE y del Ayuntamiento sean coincidentes, al realizar la comparación también se generen registros R y registros S. En estos casos, no se formularán reparos pero, con el fin de que puedan subsanarse las diferencias existentes, se facilitará al Ayuntamiento un fichero denominado DppmmmIA.aaa, con el mismo contenido y estructura que el fichero RppmmmIA.aaa, e igualmente, en su caso, facilitará un fichero EppmmmIA.aaa, con el mismo contenido y tratamiento especificado en los párrafos anteriores.

Cuando se devuelva al Ayuntamiento un fichero DppmmmIA.aaa, las posibles correcciones que se deriven del mismo se desligarán del procedimiento de aprobación de cifras y se remitirán al INE en los ficheros de variaciones mensuales.

Todos estos ficheros podrán asimismo descargarse por el Ayuntamiento a través de IDA_Padrón.
