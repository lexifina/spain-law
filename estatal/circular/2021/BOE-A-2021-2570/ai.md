## ANEXO I

## Método de cálculo de etiquetado de la electricidad

En lo que sigue, y salvo indicación expresa en contra, todos los valores se entenderán referidos al año «n» para el que se calcula el etiquetado.

1. Obtención del Mix Residual Nacional Preliminar (Preliminary Domestic Residual Mix, PDRM).

Para obtener la participación de cada tecnología t en el Mix Residual Nacional Preliminar se aplica la siguiente fórmula:

PDRMt = Generaciónt - Expedidast + Expiradast

Siendo:

PDRMt:Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Nacional Preliminar.

Generaciónt: Energía eléctrica neta en MWh generada con la tecnología t en el conjunto del Sistema Eléctrico Español.

Las tecnologías «t» a considerar serán las siguientes:

– Renovables.

– Cogeneración de Alta Eficiencia.

– Ciclos Combinados de gas natural.

– Carbón.

– Fuel/Gas.

– Nuclear.

– Otras no renovables.

Para la energía renovable de origen hidráulico, se deducirá, en su caso, la producción asociada al consumo de bombeo.

Para la cogeneración de alta eficiencia se considerará exclusivamente la energía para la que han sido concedidas garantías de origen de cogeneración de alta eficiencia.

Se consideran tecnologías convencionales a las tecnologías distintas a Renovables y Cogeneración de Alta Eficiencia.

Expedidast: Garantías de origen expedidas para la tecnología t.

Expiradast: Garantías de origen para la tecnología t que tienen como último tenedor el titular de la instalación a las que se expidieron dichas garantías, bien porque hayan caducado, bien porque no pueden ser transferidas, redimidas o exportadas al haberse agotado los plazos de solicitudes definidos en la Circular 1/2018, de 18 de abril, de la CNMC.

Solo pueden existir garantías de origen, ya sean Expedidas o Expiradas, para las tecnologías t no convencionales: «Renovables» o «Cogeneración de Alta Eficiencia».

2. Obtención del Mix Residual Nacional (Domestic Residual Mix, DRM).

Para obtener la participación de la tecnología t en el Mix Residual Nacional se aplica la siguiente fórmula:

DRMt = PDRMt - Exportacion_netat + Importacion_netat

Siendo:

DRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Nacional.

PDRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Nacional Preliminar.

Exportación netat: Energía eléctrica exportada neta hacia un País Externo1 desde el Sistema Eléctrico Español en MWh correspondiente a la tecnología t. Para su cálculo se tomará la energía neta exportada a cada País Externo y se multiplicará por el peso relativo en porcentaje de la tecnología t en el Mix Residual Nacional Preliminar (Preliminary Domestic Residual Mix, PDRM).

1 Según las definiciones del artículo 3, Francia, Portugal no son Países Externos; Sin embargo, sí tendrían la consideración de Países Externos, entre otros, Marruecos y Andorra.

Importación netat: Energía eléctrica importada neta desde un País Externo hacia el Sistema Eléctrico Español en MWh correspondiente a la tecnología t. Para su obtención se consultarán fuentes oficiales del país del que se importe la energía eléctrica.

Las tecnologías a considerar serán las correspondientes al apartado 1.

3. Obtención del consumo sin trazabilidad (Untracked Consumption, UC).

UC = Consumo energía eléctrica – Consumo garantizado

Siendo:

UC: Consumo sin trazabilidad, conforme a la definición dada en el artículo 3.b).

Consumo energía eléctrica: Total de energía eléctrica medida en MWh en barras de central consumida en el Sistema Eléctrico Español.

Consumo garantizado: Total de energía eléctrica medida en MWh en barras de central consumida en el Sistema Eléctrico Español garantizada mediante el Sistema de Garantías de Origen. Para su obtención se deben considerar todas las redenciones directas desde titulares de instalaciones hacia consumidores más las garantías de origen cuyo último tenedor es una empresa comercializadora, con independencia de si se ha realizado una posterior redención desde dicha comercializadora hacia un consumidor final.

4. Obtención del Mix Residual Final (Final Residual Mix, FRM).

Para la obtención del Mix Residual Final (FRM) deben contemplarse las posibilidades descritas en los subapartados 4.a y 4.b:

4.a) Si el consumo sin trazabilidad (UC) es menor o igual que el Mix Residual Nacional (DRM), se dice entonces que el Sistema Eléctrico Español tiene exceso de atribuciones2 y la composición del Mix Residual Final (FRM) se corresponde con la del Mix Residual Nacional (DRM):

2 En los años en los que hay superávit o exceso de atribuciones dicho exceso es utilizado junto al de otros países excedentarios para conformar el Mix Europeo de Atribuciones (European Attribute Mix -EAM-):

Es decir, si UC ≤ DRM, entonces:

FRMt = DRMt

Siendo:

FRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Final.

DRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Nacional según lo calculado en el apartado correspondiente.

4.b) Si el consumo sin trazabilidad (UC) es mayor que el Mix Residual Nacional (DRM), se dice entonces que el Sistema Eléctrico Español tiene déficit de atribuciones, déficit que debe ser completado.

Es decir, si UC > DRM, entonces:

Déficit atribuciones = UC - DRM

Siendo la definición del déficit de atribuciones la recogida en el artículo 3.d).

La participación de la tecnología t en el Mix Residual Final (FRM) se obtiene aplicando la siguiente fórmula:

FRMt = DRMt + EAMt

Siendo:

FRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Final.

DRMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Residual Nacional según lo calculado en el apartado correspondiente.

EAMt: Energía eléctrica en MWh correspondiente a la tecnología t en el Mix Europeo de Atribuciones. Para obtenerla, se multiplica el déficit de atribuciones por el peso relativo de cada tecnología t en el EAM; la suma de los EAMt de todas las tecnologías coincide por lo tanto con la cifra del déficit de atribuciones.

En el caso de que en el momento de realizar los cálculos no se hubiera publicado el correspondiente EAM, los pesos relativos de cada tecnología en el EAM se tomarán utilizando la media de los tres años disponibles inmediatamente anteriores.

4.c) Según lo calculado en los apartados anteriores, se obtendrá la tabla correspondiente a los pesos relativos de las distintas tecnologías en el Mix Residual Final (FRM). Este es el Mix correspondiente a las comercializadoras que no han participado en el Sistema de Garantías de origen (o comercializadoras genéricas).

%FRMt=Peso relativo en porcentaje, correspondiente a la tecnología t en el Mix Residual Final:

| Origen | Comercializadora genérica |
| --- | --- |
| Renovables. | %FRM renovables. |
| Cogeneración de Alta Eficiencia. | %FRM Cogen. alta eficiencia. |
| Ciclos Combinados gas natural. | %FRM C.C. gas natural. |
| Carbón. | %FRM Carbón. |
| Fuel/Gas. | %FRM Fuel/Gas. |
| Nuclear. | %FRM Nuclear. |
| Otras no renovables. | %FRM Otras no renov. |
| Total. | 100% |

5. Obtención del Mix correspondiente a cada empresa comercializadora de electricidad.

Para cada empresa deberá calcularse la energía vendida correspondiente a cada una de las fuentes. Para ello se calcula en primer lugar la energía comercializada de origen renovable y de cogeneración de alta eficiencia del siguiente modo:

RE_A = [(VENTAS_A - GOcogen. alta eficiencia_A - GO renov_A )× %FRM renovables]+ GO renov_A

Siendo:

RE_A: Energía eléctrica en MWh de origen renovable vendida por la comercializadora A.

VENTAS_A: Energía eléctrica total en MWh vendida por la comercializadora A, a partir de los datos obtenidos según el artículo 6 de esta Circular.

GOcogen. alta eficiencia_A = Garantías de origen de cogeneración de alta eficiencia cuyo último tenedor es la empresa comercializadora A, con independencia de si se ha realizado una posterior redención desde dicha comercializadora hacia un consumidor final.

GOrenov_A: Garantías de origen renovable cuyo último tenedor es la empresa comercializadora A, con independencia de si se ha realizado una posterior redención desde dicha comercializadora hacia un consumidor final.

%FRM renovables: Porcentaje de renovables en el Mix Residual Final.

Si el término (VENTAS_A - GOcogen. alta eficiencia_A - GO renov_A ) es negativo, dicho término se considerará nulo.

La energía vendida de cogeneración de alta eficiencia (Cog) se calcula de modo análogo.

Cog_A=[(VENTAS_A - GOcogen. alta eficiencia_A - GO renov_A )× %FRM cogen. alta eficiencia] + GOcogen. alta eficiencia_A

Siendo:

Cog_A: Energía eléctrica en MWh de cogeneración de alta eficiencia vendida por la comercializadora.

VENTAS_A: Energía eléctrica total en MWh vendida por la comercializadora A, a partir de los datos obtenidos según el artículo 6 de esta Circular.

%FRM cogen. alta eficiencia: Porcentaje de cogeneración de alta eficiencia en el Mix Residual Final.

GOcogen. alta eficiencia_A = Garantías de origen de cogeneración de alta eficiencia cuyo último tenedor es la empresa comercializadora A, con independencia de si se ha realizado una posterior redención desde dicha comercializadora hacia un consumidor final.

Si el término (VENTAS_A - GOcogen. alta eficiencia_A - GO renov_A ) es negativo, dicho término se considerará nulo.

Una vez obtenidas dichas variables pueden darse los siguientes casos:

– RE_A ≥ Ventas_A. Se asignará como porcentaje de renovable de la empresa A (%A renovables) el 100%. El porcentaje del resto de tecnologías será cero.

– Cog_A ≥ Ventas_A. Se asignará como porcentaje de cogeneración de alta eficiencia de la empresa A (%A Cogen. Alta eficiencia) el 100%. El porcentaje del resto de tecnologías será cero.

– RE_A + Cog_A ≥ Ventas_A.

• Se asignará como porcentaje de renovable de la empresa A (%A renovables) el correspondiente a RE_A / Ventas_A.

• Se asignará como porcentaje de cogeneración de alta eficiencia de la empresa A (%A Cogen. alta eficiencia) el complemento a 100 del porcentaje de renovable de dicha empresa: 100 - (%A renovables). El porcentaje del resto de tecnologías será cero.

– Resto de casos:

• %A renovables: Porcentaje de renovables=100 × (RE_A / Ventas_A).

• %A Cogen. alta eficiencia: Porcentaje de cogeneración de alta eficiencia=100 × (Cog_A / Ventas_A).

• Porcentaje de cada una de las tecnologías convencionales: Se considera la cifra resultante de la resta (Ventas_A) - (Re_A + Cog_A) y se reparte de forma proporcional según el peso de esa tecnología en la totalidad de tecnologías convencionales del FRM.

De esta forma se obtiene el Mix de comercialización de la empresa A:

| Origen | Comercializadora A |
| --- | --- |
| Renovables. | %A renovables. |
| Cogeneración de Alta Eficiencia. | %A Cogen. alta eficiencia. |
| Ciclos Combinados gas natural. | %A C.C. gas natural. |
| Carbón. | %A Carbón. |
| Fuel/Gas. | %A Fuel/Gas. |
| Nuclear. | %A Nuclear. |
| Otras no renovables. | %A Otras no renov. |
| Total. | 100% |

6. Obtención del impacto ambiental asociado en emisiones de CO2.

La CNMC utilizará el dato de las correspondientes emisiones específicas (en gramos equivalentes de CO2 por kilovatio-hora, gCO2eq/kWh) para cada una de las tecnologías de generación consideradas. Dicha información será la obtenida durante el año anterior (año «n»); en caso de no disponer de dicha información para el ejercicio señalado, se utilizarán los datos de emisiones correspondientes al ejercicio inmediatamente anterior (año «n-1»).

Dicho factor de emisión específico por tecnología se aplicará de forma proporcional al Mix correspondiente de cada empresa comercializadora para obtener el impacto ambiental de las emisiones de CO2 equivalente (en gramos equivalentes de CO2 por kilovatio-hora, gCO2eq/kWh) asociadas al etiquetado de dicha comercializadora. En el caso de la comercializadora genérica se utilizará el Mix Residual Final. Asimismo, se calculará el factor de emisión correspondiente a la generación eléctrica del Sistema Eléctrico Español, que se utilizará en el etiquetado a efectos comparativos y para la obtención de la clasificación energética de cada empresa comercializadora en función del impacto ambiental relacionado con las emisiones de CO2 equivalente.

7. Obtención del impacto ambiental asociado en residuos radiactivos de alta actividad.

La CNMC utilizará fuentes oficiales para obtener la información relativa a las emisiones de residuos radioactivos de alta actividad medidos en microgramos por kilovatio-hora µg/kWh que se hayan generado en el Sistema Eléctrico Español en el ejercicio anterior (año «n»). Para ello calculará la media aritmética anual de los tres últimos años de los que se disponga de información, al objeto de contemplar los diferentes «ciclos de recarga» de las distintas centrales nucleares. Dicha cifra se utilizará en el etiquetado a efectos comparativos, y para la obtención de la clasificación energética de cada empresa comercializadora en función del impacto ambiental relacionado con los residuos radiactivos de alta actividad.

Dicho valor se aplicará de forma proporcional al porcentaje de tecnología ‘Nuclear’ del Mix correspondiente de cada empresa comercializadora, para obtener los residuos radioactivos de alta actividad medidos en µg/kWh asociados al etiquetado de dicha comercializadora. En el caso de la comercializadora genérica se utilizará el porcentaje de tecnología nuclear del Mix Residual Final.

8. Obtención de la calificación energética relacionada con el impacto ambiental de las emisiones de CO2 equivalente.

La CNMC asignará una letra a cada una de las empresas comercializadoras –incluida la comercializadora genérica– en función del impacto ambiental relacionado con las emisiones de CO2 equivalente.

La mencionada clasificación variará desde la letra «A» a la «G», correspondiendo la letra «A» al mínimo impacto ambiental, la «D» al impacto ambiental más próximo al promedio nacional y la «G» al máximo impacto ambiental.

Las bandas de fluctuación correspondientes a cada letra serán las siguientes:

A: EA / ENAL < 0,35

B: 0,35 ≤ EA / ENAL < 0,65

C: 0,65 ≤ EA / ENAL < 0,95

D: 0,95 ≤ EA / ENAL < 1,05

E: 1,05 ≤ EA / ENAL < 1,35

F: 1,35 ≤ EA / ENAL < 1,65

G: 1,65 ≤ EA / ENAL

Siendo:

EA: Emisiones de CO2 equivalente (en gramos equivalentes de CO2 g/kWh) asociadas a la comercializadora A.

ENAL: Emisiones de CO2 equivalente (en gramos equivalentes de CO2 g/kWh) asociadas al conjunto de la generación eléctrica del Sistema Eléctrico Español.

9. Obtención de la calificación energética relacionada con el impacto ambiental de los residuos radiactivos de alta actividad.

Se procederá del mismo modo con la clasificación relativa al impacto ambiental ocasionado por los residuos radiactivos de alta actividad:

Las bandas de fluctuación correspondientes a cada letra serán las siguientes:

A: RA / RNAL < 0,35

B: 0,35 ≤ RA / RNAL < 0,65

C: 0,65 ≤ RA / RNAL < 0,95

D: 0,95 ≤ RA / RNAL < 1,05

E: 1,05 ≤ RA / RNAL < 1,35

F: 1,35 ≤ RA / ENAL < 1,65

G: 1,65 ≤ EA / ENAL

Siendo:

RA: Emisiones de residuos radioactivos de alta actividad (en µg/kWh) asociadas a la comercializadora A.

RNAL: Emisiones de residuos radioactivos de alta actividad (en µg/kWh) asociadas al conjunto de la generación eléctrica del Sistema Eléctrico Español.
