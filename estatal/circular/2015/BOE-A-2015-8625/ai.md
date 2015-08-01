## ANEXO I

## Formularios

Los Formularios a remitir por los sujetos obligados consisten en una agrupación de Bloques que contiene la información requerida. Los Bloques se componen a su vez de un conjunto de Campos, distintos para cada Bloque, que deberán en todos los casos ser cumplimentadas.

Determinados Campos de los Bloques deben ser cumplimentados por los sujetos obligados mediante la selección de una de las referencias que figuran en la tabla definida al efecto. Las tablas que se utilizarán para la cumplimentación de los Bloques se encuentran contenidas en el documento Anexo II Tablas.

El formato que debe tener cada uno de los campos se indica con la siguiente codificación.

| Formato de los Campos | Descripción |
| --- | --- |
| N(n, m) | Valor numérico, positivo o negativo, con n posiciones máximas en la parte entera y m en la parte decimal. |
| NP(n, m) | Valor numérico positivo con n posiciones máximas en la parte entera y m en la parte decimal. |
| C(n) | Cadena de texto de longitud igual a n caracteres. |
| C(≤n) | Cadena de longitud máxima de n caracteres. |
| F | Fecha en formato aaaa-mm-dd. |
| B | Booleano. Sólo pueden tener los valores: Sí y No. |

1. Formulario 1: F1_Activos_E.

Sector de aplicación: Eléctrico.

Este Formulario contiene la base de datos de activos regulados y sus características técnicas a 31 de diciembre del ejercicio de declaración.

1.1 Bloque F1-E1: Líneas eléctricas.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código Único de Activo Regulado. | C(33) | Coherencia del CUAR. |
| Nombre. | Nombre de la Línea. | C(≤25) |  |
| Tipo. | Tipo de línea. 1. Aérea. 2. Subterránea. 3. Submarina. | NP(1,0) | Número de la lista. |
| Corriente. | Tipo de corriente de la línea. 1. Alterna. 2. Continua. | NP(1,0) | Número de la lista. |
| N.º circuitos. | Número de circuitos de la línea: 1. Simple. 2. Doble. 3. Triple. 4. Cuádruple. 5. Simple sobre apoyos de doble circuito. 6. Segundo circuito en línea con apoyos para doble circuito. | NP(1,0) | Número de la lista. |
| N.º conductores. | Número de conductores de la línea: 1. Simplex. 2. Dúplex. 3. Triplex. 4. Otros. | NP(1,0) | Número de la lista. |
| Tensión. | Tensión de la línea. 1. 400kV≤U. 2. 220kV≤U<400kV. 3. 132kV≤U<220kV. 4. 66kV≤U<132kV. 5. Otras. | NP(1,0) | Número de la lista. |
| Sección. | Sección de la línea. 1. S≤50 mm2. 2. 50<S≤60 mm2. 3. 60<S≤100 mm2. 4. 100<S≤125 mm2. 5. 125<S≤150 mm2. 6. 150<S≤200 mm2. 7. 200<S≤300 mm2. 8. 300<S≤400 mm2. 9. 400<S≤500 mm2. 10. 500<S≤630 mm2. 11. 630<S≤800 mm2. 12. 800<S≤1100 mm2. 13. 1100<S≤1200 mm2. 14. 1200<S≤2000 mm2. 15. 2000<S≤2500 mm2. 16. 2500 mm2<S. | NP(2,0) | Número de la lista. |
| Material. | Material de la línea. 1. Aluminio. 2. Cobre. 3. Otros materiales y aleaciones. | NP(1,0) | Número de la lista. |
| Repotenciación. | Si es una repotenciación de una línea, Sí, en caso contrario No. | B |  |
| CUAR repotenciación. | En caso de ser una repotenciación, CUAR de la línea repotenciada. En caso contrario, NA. | C(≤33) | Si es un CUAR, debe estar declarado en el mismo Bloque. |
| Viento de diseño. | Viento máximo de diseño de la línea, en km/h. | NP(3,0) |  |
| CUAR origen 1. | CUAR de origen de la línea. Debe ser el de otra Línea o de una Posición/Transformador/Máquina. | C(33) | El CUAR debe estar declarado en los Bloques F1-E1, F1-E2, F1-E3, o en el F1-E4. |
| CUAR origen 2. | En el caso de una línea de doble circuito, CUAR de origen del mimo. Debe ser el de otra Línea o de una Posición/Transformador/Máquina. En caso contrario, NA. | C (≤33) | En el caso de CUARdebe estar declarado en los Bloques F1-E1, F1-E2, F1-E3, o en el F1-E4. |
| CUAR fin 1. | CUAR de fin de la línea. Debe ser el de otra Línea o de una Posición/Transformador/Máquina. En el caso de conexión internacional indicar: PT: Portugal. FR: Francia. MR: Marruecos. AN: Andorra. | C(≤33) | El CUAR debe estar declarado en los Bloques F1-E1, F1-E2, F1-E3, o en el F1-E4. |
| CUAR fin 2. | En el caso de una línea de doble circuito, CUAR fin del mismo. Debe ser el de otra Línea o de una Posición/Transformador/Máquina. En caso contrario, NA. En el caso de conexión internacional indicar: PT: Portugal. FR: Francia. MR: Marruecos. AN: Andorra. | C(≤33) | En el caso de CUAR debe estar declarado en los Bloques F1-E1, F1-E2, F1-E3, o en el F1-E4. |
| Municipio origen. | Código INE del municipio de origen de la línea. | NP(5,0) | Valor válido de un municipio. |
| Municipio fin. | Código INE del municipio de fin de la línea. | NP(5,0) | Valor válido de un municipio. |
| Capacidad. | Capacidad de transporte, en MVA, de la línea. | NP(5,0) |  |
| Longitud. | Longitud admitida de la línea, en metros. | NP(6,2) |  |
| Centro mantenimiento. | Centro de mantenimiento desde el cual se realiza el mantenimiento de la línea. | C(9) | Valor declarado en el Bloque F1-E6. |

1.2 Bloque F1-E2: Posiciones.

Descripción de los campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código Único de Activo Regulado. | C(33) | Coherencia CUAR. |
| Denominación. | Nombre de la posición. | C(≤255) |  |
| Configuración. | Configuración de la Posición. 1. Barra simple. 2. Doble Barra. 3. Triple Barra. 4. Anillo. 5. Doble anillo. 6. Anillo en plano vertical. 7. Interruptor y medio. 8. Móvil. | NP(1,0) | Número de la lista. |
| Tipo. | Tipo de Posición. 1. Convencional. 2. Blindada sin fluoductos. 3. Blindada con fluoductos. | NP(1,0) | Número de la lista. |
| Ubicación. | Ubicación de la Posición. 1. En intemperie. 2. En edificio. | NP(1,0) | Número de la lista. |
| Tensión. | Tensión de la Posición. 1. 400kV≤U. 2. 220kV≤U<400kV. 3. 132kV≤U<220kV. 4. 66kV≤U<132kV. 5. Otras. | NP(1,0) | Número de la lista. |
| Intensidad. | Intensidad de la Posición. 1. 63kA. 2. 50 kA. 3. 40 kA. 4. 31,5 kA. | NP(1,0) | Número de la lista. |
| Equipamiento. | Equipamiento de la Posición. 1. Posición equipada. 2. Posición de reserva sin equipar. 3. Equipamiento de posición de reserva. | NP(1,0) | Número de la lista. |
| Centro mantenimiento. | Código del Centro de mantenimiento desde el que se mantiene la posición. En caso de posición móvil se declarará el centro de mantenimiento al que este asociada la posición al cierre del ejercicio. | C(9) | Valor declarado en el Bloque F1-E6. |

1.3 Bloque F1-E3: Transformadores.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Denominación. | Nombre del transformador. | C(≤255) |  |
| Relación Transformación. | Relación de transformación. 1. 400/220 kV. 2. 400/220/132-110 kV. 3. 400/132-1 1 0 kV. 4. 220/132 kV. 5. 220/132/66 kV. 6. 220/66 kV. 7. 132/66 kV. 8. 66 kV/MT. | NP(1,0) | Número de la lista. |
| Fases. | Número de fases del transformador. 1. Monofásico. 2. Trifásico. | NP(1,0) | Número de la lista. |
| Potencia. | Indicar la potencia, en MVA, del transformador. | NP(5,0) |  |
| Centro mantenimiento. | Código del Centro de mantenimiento desde el que se mantiene. En caso de transformador móvil se declarará el centro de mantenimiento al que este asociada la posición al cierre del ejercicio. | NP(3,0) | Valor declarado en el Bloque F1-E6. |

1.4 Bloque F1-E4: Máquinas.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Denominación. | Nombre de la máquina. | C(≤255) |  |
| Tipo. | Tipo de máquina. 1. Reactancia. 2. Condensador. 3. Desfasador. 4. Estación conversora. | NP(1,0) | Número de la lista. |
| Tensión. | Tensión de la máquina. 1. 400 kV. 2. 220 kV. 3. 132 kV. 4. 66 kV. 5. Otras. | NP(1,0) | Número de la lista. |
| Capacidad. | Capacidad de la máquina en MVA o MVAr. | NP(5,0) |  |
| Centro mantenimiento. | Código del Centro de mantenimiento desde el que se mantiene. | C(9) | Valor declarado en el Bloque F1-E6. |

1.5 Bloque F1-E5: Despachos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Denominación. | Descripción de la actuación que se realiza sobre el activo. | C(≤255) |  |
| CUAR asociado. | Código CUAR del activo sobre el que se realiza la actuación. |  |  |

1.6 Bloque F1-E6: Centros de mantenimiento.

Descripción de campos:

|  | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código. | Código del centro de mantenimiento. | C(9) | El código se asignará según lo definido en la Tabla 5. En el caso de ser declaraciones sucesivas, los códigos declarados en ejercicios anteriores se deben mantener, y sobre centros nuevos se debe continuar a partir del último código declarado años anteriores. |
| Nombre. | Nombre del centro de mantenimiento. | C(≤255) |  |
| Municipio. | Código INE del municipio donde está situado el centro de mantenimiento. | NP(5,0) | Valor válido de un municipio. |

1.7 Bloque F1-E7: Otros activos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Denominación. | Descripción del activo. | C(≤255) |  |

1.8 Bloque F1-E8: Correspondencia Base de Datos Instalaciones Eléctricas.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Declarado en los Bloques F2-E1 a E5 y Bloque F1-E7 que no se encuentren en estado Y Z. |
| Código Base de Datos Instalaciones Eléctricas. | Código Base de Datos Instalaciones Eléctricas para el activo regulado. | C(12) |  |

1.9 Bloque F1-E9: Entradas y Salidas.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de línea nueva. | C(33) | Contenido en F1-E1. |
| Nombre. | Nombre de la Línea. | C(≤255) |  |
| Fecha. | Fecha de modificación. | F |  |
| CUAR 1. | CUAR de la línea dividida. | C(33) | Contenido en F1-E1. |
| CUAR 2. | CUAR de la línea de Entrada/Salida. En caso de que la línea dividida sea de múltiple circuito y que la entrada y salida se haga sobre un circuito, para el circuito en el que no se realiza la apertura indicar NA. | C(33) | Contenido en F1-E1. |

2. Formulario 2: F2 Activos G.

Sector de aplicación: Gas.

Este Formulario contiene la base de datos de activos regulados con acta de puesta en servicio y sus características técnicas a 31 de diciembre del año de declaración.

2.1 Bloque F2-GT1: Gasoductos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Obra Lineal de gasoducto. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la instalación asociada al CUAR. | C(≤255) |  |
| CUAR Modificada. | En caso de que el CUAR sea una modificación o actuación complementaria, indicar el CUAR de la instalación sobre la que se realiza. En caso contrario, NA. | C(≤33) | En el caso de declarar CUAR, debe estar declarado en el mismo Bloque F2-GT1. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |
| CUAR origen. | CUAR de la Posición inicial a la que la Obra Lineal del gasoducto está conectada. En el supuesto que el inicio se corresponda con un límite provincial, se indicará el CUAR de la Obra Lineal a la que se conecta. | C(33) | Existencia de CUAR en el Bloque F2-GT1 o F2-GT2. |
| CUAR fin. | CUAR de la Posición final a la que la Obra Lineal del gasoducto está conectada. En el supuesto que el final se corresponda con un límite provincial, se indicará el CUAR de la Obra Lineal a la que se conecta. | C(33) | Existencia de CUAR en el Bloque F2-GT1 o F2-GT2. |
| Provincia. | Código INE de la provincia en la que se encuentra ubicada la Obra Lineal del CUAR. | NP(2,0) | Valor válido de la provincia de la lista del INE. |
| Municipio origen. | Código INE del término municipal de la instalación inicial a la que la Obra Lineal del gasoducto está conectada. | NP(5,0) | Valor válido del término municipal de la lista del INE. |
| Municipio fin. | Código INE del término municipal de la instalación final a la que la Obra Lineal del gasoducto está conectada. | NP(5,0) | Valor válido del término municipal de la lista del INE. |
| Titular de Operación. | Operación del activo. 1. Activo operado por el titular. 2. Activo operado por un GRI. | NP(1,0) | Número de la lista. |
| Tipo gasoducto. | Tipo de gasoducto: 1. Transporte primario troncal. 2. Transporte primario no troncal. 3. Transporte secundario. 4. Transporte gasoducto submarino. | NP(1,0) | Número de la lista. |
| Longitud. | Longitud real, en metros, del gasoducto. | NP(6,3) |  |
| Presión. | Presión máxima autorizada en bar. | NP(3,3) |  |
| Diámetro. | Diámetro del gasoducto. | C(6) | Contenido en la Tabla 62. |

2.2 Bloque F2-GT2: Posiciones.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la posición/modificación posición. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la unidad constructiva asociada al CUAR. | C(≤255) |  |
| Tipo. | Tipo de posición. En el caso de modificación indicar tipo tras la modificación. 1. Tipo S. 2. Tipo D. 3. Tipo T. | NP(1,0) | Número de la lista. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación simultánea junto con gasoducto. 2. Instalación en gasoducto existente. 3. Transformación de una Tipo S a Tipo D. 4. Transformación de una Tipo S a Tipo T. 5. Transformación de una Tipo D a Tipo T. 6. Nueva derivación en posición existente Tipo D. 7. Nueva derivación en posición existente Tipo T. | NP(1,0) | Número de la lista. |
| CUAR Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR (posición) previo existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Diámetro. | Diámetro del gasoducto. | C(6) | Contenido en la Tabla 62. |
| CUAR. Instalación Conectada. | Código CUAR de la unidad constructiva a la que está conectada: Se indicará el CUAR del gasoducto sobre el que está instalada. | C(33) | Declarado en el Bloque Gasoductos F2-GT1. |
| Tipo gasoducto. | Tipo de gasoducto: 1. Transporte primario troncal. 2. Transporte primario no troncal. 3. Transporte secundario. 4. Transporte gasoducto submarino. | NP(1,0) | Número de la lista. |
| Titular de la Operación. | Operación del activo. 1. Activo operado por el titular. 2. Activo operado por un GRI. | NP(1,0) | Número de la lista. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.3 Bloque F2-GT3: ERM/EM/ERP/ERC.

Descripción de campos:

| Nombre código | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la ERM/EM/ERP/ERC. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la unidad constructiva asociada al CUAR. | C(≤255) |  |
| Tipo. | Tipo de estación. 1. ERM. 2. EM. 3. ERC. 4. ERP. | NP(1,0) | Número de la lista. |
| Tipo G. | Para ERM/EM se indicará el Tipo de G de la turbina de medición que se lista a continuación. En el caso de instalaciones con medición por ultrasonidos se corresponderá con el Tipo G de una ERM clásica equivalente. En el caso de modificación indicar tipo tras la modificación. | C(6) | Contenido en Tabla 63. |
| Ultrasonidos. | Indicar si ultrasonidos: Sí/No. | B |  |
| Tipo gasoducto. | Tipo de gasoducto: 1. Transporte primario troncal. 2. Transporte primario no troncal. 3. Transporte secundario. 4. Transporte gasoducto submarino. | NP(1,0) | Número de la lista. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación simultánea junto con gasoducto. 2. Instalación en gasoducto existente. 3. Línea adicional. 4. Sustitución de equipos de medición existentes. | NP(1,0) | Número de la lista. |
| Número de líneas en operación. | Indicar el número de líneas en operación que dispone la ERM. En caso de línea adicional y sustitución de equipos indicar la actuación. | NP(1,0) |  |
| Número de líneas en reserva. | Indicar el número de líneas en reserva que dispone la ERM. En caso de línea adicional y sustitución de equipos indicar la actuación. | NP(1,0) |  |
| CUAR Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | Declarado en el mismo Bloque. |
| CUAR Instalación Conectada. | Se indicará el CUAR de la Posición a la que está Conectada. | C(33) | Declarado en Bloque Posiciones F2-GT2. |
| Sistema de calentamiento. | Indicar si incorpora sistema de calentamiento, con calderas situadas en otro recinto y cambiadores de calor sobre las líneas de regulación: SÍ/NO. | B |  |
| Equipamiento telemático. | Indicar si incorpora equipamiento telemático: Sí/No. | B |  |
| Edificio/Caseta. | Tipo de edificio /caseta. 1, edificio cerrado/caseta. 2, intemperie / techo de protección. 3. Armario. | NP(1,0) | Número de la lista. |
| Seguridad patrimonial. | Indicar si incorpora recinto vallado y dotado, en su caso, de sistemas de seguridad patrimonial (aplicable sólo a casetas y posiciones de válvulas): Sí/No. | B |  |
| Presión aguas arriba. | Presión autorizada del gasoducto aguas arriba de la Estación, en bar. | NP(3,3) |  |
| Presión aguas abajo. | Presión autorizada del gasoducto aguas abajo de la Estación, en bar. | NP(3,3) |  |
| Titular de la operación. | Operación del activo. 1. Activo operado por el titular. 2. Activo operado por un GRI. | NP(1,0) | Número de la lista. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.4 Bloque F2-GT4: Estaciones de Compresión.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la unidad constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la unidad constructiva asociada al CUAR. | C(≤255) |  |
| Tipo. | Tipo de EC: 1. Tubocompresores de gas. 2. Motores eléctricos. | NP(1,0) |  |
| CUAR Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | Declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1 Instalación adicional. 2 Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| Titular de la Operación. | Operación del activo. 1. Activo operado por el titular. 2. Activo operado por un GRI. | NP(1,0) | Número de la lista. |
| Número Turbo Compresores/motores eléctricos en Operación. | Número de turbocompresores para operación. Indicar sobre los que se realiza la actuación. | NP(1,0) |  |
| Potencia En Operación. | Potencia total de los turbocompresores para operación, en kW. Indicar instalada en la actuación. | NP(9,0) |  |
| Número Turbo Compresores en Reserva. | Número de turbocompresores para reserva Indicar sobre los que se realiza la actuación. | NP(1,0) |  |
| Potencia en Reserva. | Potencia total de los turbocompresores para reserva, en kW. Indicar la instalada en la actuación. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.5 Bloque F2-GT5: Centros de Mantenimiento o CMOCS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la unidad constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la unidad constructiva asociada al CUAR. | C(≤255) |  |
| CUAR Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | Declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1 Instalación adicional. 2 Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| Superficie total. | Superficie total, en m2, que ocupa el centro. | NP(9,0) |  |
| Superficie urbanizada. | Superficie total urbanizada, en m2. | NP(9,0) |  |
| Superficie edificada. | Superficie total edificada, en m2. | NP(9,0) |  |
| N.º Referencia Catastral de la Finca. | Se indicará el N.º Referencia Catastral de la finca donde se ubique. En caso de ubicarse sobre varias fincas, se indicará el N.º Referencia de Catastral de la finca con mayor superficie. www.catastro.meh.es/esp/referencia_catastral_1.asp. | C(20) |  |
| Código Centro de Mantenimiento. | Código del CECOS Principal al que corresponde el centro de mantenimiento. | C(9) | Existencia en la Tabla 6. |

2.6 Bloque F2-GT6: Gas de llenado.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la instalación asociado al CUAR. | C(≤255) |  |
| CUAR asociado. | CUAR del activo asociado al que se destina el gas de llenado. | C(33) | CUAR declarado en el Bloque F2-GT1. |
| Cantidad de Gas. | Cantidad de Gas adquirida en kWh. | NP(9,0) |  |
| Precio de Adquisición. | Precio de Adquisición (€/MWh). | NP(6,2) |  |

2.7 Bloque F2-GT7: Otras instalaciones o servicios de transporte.

Descripción de campos:

| Nombre código | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |

2.8 Bloque F2-R1: Tanques GNL Descripción de campos.

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Capacidad. | Capacidad m3 de GNL. | NP(9,0) |  |
| Bombas en operación. | Número de bombas primarias en operación. | NP(2,0) |  |
| Caudal bombas en operación. | Caudal Nominal total en m3/h de GNL de las Bombas Primarias en Operación. | NP(9,0) |  |
| Bombas en reserva. | Número de bombas primarias en reserva. | NP(2,0) |  |
| Caudal bombas en reserva. | Caudal Nominal total en m3/h de GNL de las Bombas Primarias en Reserva. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.9 Bloque F2-R2: Sistema de bombas secundarias.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Caudal de operación. | Caudal nominal en, m3/h de GNL. | NP(9,0) |  |
| Estado operativo de la unidad. | Indicar si la unidad está en: 1. Operación. 2. Reserva. | NP(1,0) | Número de la lista. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.10 Bloque F2-R3: Vaporizadores de agua de mar.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Caudal de operación. | Caudal nominal en, Nm3/h de GN. | NP(9,0) |  |
| Estado operativo de la unidad. | Indicar si la unidad está en: 1. Operación. 2. Reserva. | NP(1,0) | Número de la lista. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.11 Bloque F2-R4: Vaporizadores de combustión sumergida.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Caudal de operación. | Caudal nominal en, Nm3/h de GN. | NP(9,0) |  |
| Estado operativo de la unidad. | Indicar si la unidad está en: 1. Operación. 2. Reserva. | NP(1,0) | Número de la lista. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.12 Bloque F2-R5: Sistema de medida y odorización (ERM/EM).

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación simultánea junto con gasoducto. 2. Instalación en gasoducto existente. 3. Línea adicional. 4. Sustitución de equipos de medición existente. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2- Rx. |
| Estado operativo de la unidad. | Indicar si la unidad está en: 1. Operación. 2. Reserva. | NP(1,0) | Número de la lista. |
| Ultrasonido. | Indicar si tiene medición por ultrasonidos: Sí/No. | B |  |
| Tipo G líneas. | Para cada línea de medición se indicará el Tipo de G de la turbina de medición que se lista a continuación. En el caso de instalaciones con medición por ultrasonidos se corresponderá con el Tipo G de una línea clásica equivalente. | C(6) | Contenido en Tabla 63. |
| Número de líneas en operación. | Indicar el número de líneas en operación que dispone la ERM. En caso de línea adicional y sustitución de equipos indicar la actuación. | NP(1,0) |  |
| Número de líneas en reserva. | Indicar el número de líneas en reserva que dispone la ERM. En caso de línea adicional y sustitución de equipos indicar la actuación. | NP(1,0) |  |
| Sistema de calentamiento. | Indicar si incorpora sistema de calentamiento, con calderas situadas en otro recinto y cambiadores de calor sobre las líneas de regulación: Sí/No. | B |  |
| Equipamiento telemático. | Indicar si incorpora equipamiento telemático: Sí/No. | B |  |
| Edificio/Caseta. | Tipo de edificio /caseta. 1, edificio cerrado/caseta. 2, intemperie /techo de protección Armario. | NP(1,0) | Número de la lista. |
| Seguridad patrimonial. | Indicar si incorpora recinto vallado y dotado, en su caso, de sistemas de seguridad patrimonial (aplicable sólo a casetas y posiciones de válvulas): Sí/No. | B |  |
| Presión aguas arriba. | Presión aguas arriba de la Estación, en bar. | NP(3,3) |  |
| Presión aguas abajo. | Presión autorizada del gasoducto aguas abajo de la Estación, en bar. | NP(3,3) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.13 Bloque F2-R6: Sistema de antorcha combustor.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| Caudal. | Caudal nominal, en kg/h, de GN. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.14 Bloque F2-R7: Sistema de compresión boil-off para procesado interno.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Estado operativo de la unidad. | Indicar si la unidad está en: 1. Operación. 2. Reserva. | NP(1,0) | Número de la lista. |
| Caudal en operación. | Potencia total, en kW, de las unidades en operación. | NP(9,0) |  |
| Caudal. | Caudal nominal de procesado, en m3/h, de GN de las unidades en operación. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.15 Bloque F2-R8: Relicuador boil-off.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1 Instalación adicional. 2 Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Caudal GN. | Caudal nominal, en kg/h, de GN del relicuador. | NP(9,0) |  |
| Caudal GNL. | Caudal nominal, en kg/h, de GNL del relicuador. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.16 Bloque F2-R9: Sistema de compresión boil-off para emisión directa a la red.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado eN Bloques F2-Rx. |
| Número Turbo Compresores en operación. | Número de turbocompresores para operación. | NP(9,0) |  |
| Potencia en operación. | Potencia total, en kW, de los turbocompresores en operación. | NP(9,0) |  |
| Número de Turbo Compresores en reserva. | N.º de turbocompresores en reserva. | NP(9,0) |  |
| Potencia en reserva. | Potencia total, en kW, de los turbocompresores en reserva. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.17 Bloque F2-R10: Cargaderos de cisternas de GNL.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Capacidad. | Capacidad del cargadero, en número de cargas/día. | NP(9,0) |  |
| Líneas de carga. | Número de líneas de carga. | NP(1,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.18 Bloque F2-R11: Interconexiones de GNL.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Longitud. | Longitud total, en m, de la red de tuberías de GNL. | NP(9,0) |  |
| Diámetro. | Diámetro medio ponderado, en pulgadas, de la red de tuberías de GNL. | NP(2,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.19 Bloque F2-R12: Interconexiones de GN.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado e Bloques F2-Rx. |
| Longitud. | Longitud total, en m, de la red de tuberías de GN. | NP(9,0) |  |
| Diámetro. | Diámetro medio ponderado, en pulgadas, de la red de tuberías de GN. | NP(2,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.20 Bloque F2-R13: Obra civil terrestre.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso deCUAR, declarado en Bloques F2-Rx. |
| Superficie total. | Superficie total, en m2, que ocupa la planta. | NP(9,0) |  |
| Superficie urbanizada. | Superficie total urbanizada de la planta, en m2. | NP(9,0) |  |
| Superficie edificada. | Superficie total edificada de la planta, en m2. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.21 Bloque F2-R14: Muelles e instalaciones de descarga.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Capacidad buque. | Capacidad máxima del buque, en m3 de GNL. | NP(9,0) |  |
| Longitud. | Longitud, en m, del muelle. | NP(9,0) |  |
| Capacidad descarga. | Capacidad máxima de descarga de GNL, en m3/h. | NP(9,0) |  |
| Capacidad carga GNL. | Capacidad máxima de carga de GNL, en m3/h. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.22 Bloque F2-R15: Sistema de suministro eléctrico.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado e Bloques F2-Rx. |
| Potencia. | Potencia instalada, en MW. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.23 Bloque F2-R16: Sistema de captación de agua.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Caudal. | Caudal nominal, en m3/h, de agua. | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.24 Bloque F2-R17: Sistema de Gestión y Control.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado e Bloques F2-Rx. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.25 Bloque F2-R18: Sistemas Auxiliares.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.26 Bloque F2-R19: Cimentaciones y obra civil asociada a los tanques de almacenamiento de GNL.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.27 Bloque F2-R20: Otras instalaciones o servicios.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2012, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea (Tanque GNL, Vaporizador, Cargadero GNL, Atraque). Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-Rx. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.28 Bloque F2-R21: Gas Talón.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la instalación asociado al CUAR. | C(≤255) |  |
| CUAR asociado. | CUAR del activo asociado al que se destina el gas. | C(33) | CUAR declarado en el Bloque F2-R1. |
| Cantidad de Gas. | Cantidad de Gas adquirida en kWh. | NP(9,0) |  |
| Precio de Adquisición. | Precio de Adquisición (€/MWh). | NP(6,2) |  |

2.29 Bloque F2-AS1: Instalaciones terrestres en superficie del AASS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2013, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea. Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2 -ASx. |
| Potencia inyección. | Potencia total, en MW, de las unidades en operación. | NP(9,0) |  |
| Capacidad inyección. | Capacidad nominal de inyección, en m3(N)/h. | NP(9,0) |  |
| Potencia extracción. | Potencia total, en MW, de las unidades en operación (si son las mismas que las unidades de inyección poner cero). | NP(9,0) |  |
| Capacidad extracción. | Capacidad nominal de extracción, en m3(N)/h (si son las mismas que las unidades de inyección poner cero). | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.30 Bloque F2-AS2: Instalaciones Off-Shore en superficie del AASS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2013, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea. Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2 -ASx. |
| Potencia inyección. | Potencia total, en MW, de las unidades en operación. | NP(9,0) |  |
| Capacidad inyección. | Capacidad nominal de inyección, en m3(N)/h. | NP(9,0) |  |
| Potencia extracción. | Potencia total, en MW, de las unidades en operación (si son las mismas que las unidades de inyección poner cero). | NP(9,0) |  |
| Capacidad extracción. | Capacidad nominal de extracción, en m3(N)/h (si son las mismas que las unidades de inyección poner cero). | NP(9,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.31 Bloque F2-AS3: Instalaciones en subsuelo.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR unidad constructiva Modificada. | Código CUAR a rellenar cuando es modificación, ampliación o transformación de un CUAR existente. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en el mismo Bloque. |
| Tipo de actuación. | Tipo de actuación. 1. Instalación adicional. 2. Sustitución/modificación de instalaciones existentes. | NP(1,0) | Número de la lista. |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2013, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea. Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2-ASx. |
| Capacidad útil nominal. | Capacidad útil nominal del almacenamiento, en Millones de m3(N). | NP(6,0) |  |
| Gas colchón. | Volumen de gas colchón, en Millones de m3(N). | NP(6,0) |  |
| Pozos de Producción. | Número de pozos de producción. | NP(2,0) |  |
| Pozos de Control. | Número de pozos de control. | NP(2,0) |  |
| Pozos de reinyección. | Número de pozos de reinyección. | NP(2,0) |  |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

2.32 Bloque F2-AS4: Inversiones en investigación y exploración.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR de la Unidad Constructiva. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Nombre de la Unidad Constructiva. | C(≤255) |  |
| CUAR de la Instalación Vinculada con Retribución Reconocida. | Para instalaciones PEM antes de 2013, Código CUAR de la unidad constructiva asociada a esta unidad que tiene Retribución Reconocida individualizada y que fue PEM de forma coetánea/simultánea. Cuando se trate de la propia instalación con retribución reconocida, se indicará su CUAR. En caso contrario, NA. | C(≤33) | En el caso de CUAR, declarado en Bloques F2 -ASx. |
| Autorización administrativa permiso investigación /exploración. | Identificación del permiso (Fecha de BOE, y número BOE de la disposición). | C(≤255) |  |

2.33 Bloque F2-AS5: Gas Colchón.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33). | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo de la instalación asociado al CUAR. | C(≤255). |  |
| CUAR asociado. | CUAR del activo asociado al que se destina el gas. | C(33). | CUAR declarado en el Bloque F2-AS3. |
| Cantidad de Gas. | Cantidad de Gas adquirida en kWh. | NP(9,0). |  |
| Precio de Adquisición. | Precio de Adquisición (€/MWh). | NP(6,2). |  |

2.34 Bloque F2-G1: Correspondencia SIDRA.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Declarado en los Bloques F2-GTx, F2-Rx y F2-ASx. |
| Código SIDRA. | Código asignado en SIDRA para el activo regulado. | C(14) |  |

3. Formulario 3: F3_Activos_GRI.

Sector de aplicación: Gas.

Este Formulario deberá ser cumplimentado por los gestores de red independiente e identifica las instalaciones de la red troncal de transporte de gas natural que son gestionados por el mismo.

3.1 Bloque F3-GRI Activos Gestionados por el GRI.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado gestionado. | C(33) | Coherencia CUAR. Existencia del CUAR en la declaración de la empresa propietaria. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asignada la instalación. | C(9) | Existencia en la Tabla 6. |

4. Formulario 4: F4_Activos GTS/OS.

Sector de aplicación: Electricidad y gas.

Este Formulario deberá ser cumplimentado por el OS y el GTS y contiene la base de datos de activos regulados y sus características técnicas.

4.1 Bloque F4-A1: Instalaciones y edificios.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo del activo asociada al CUAR. | C(≤256) |  |
| Superficie total. | Superficie total, en m2, que ocupa el centro. | NP(9,0) |  |
| Superficie urbanizada. | Superficie total urbanizada, en m2. | NP(9,0) |  |
| Superficie edificada. | Superficie total edificada, en m2. | NP(9,0) |  |
| N.º Referencia Catastral de la Finca. | En el caso de Edificios, se indicará el N.º Referencia de Catastral de la finca. En caso contrario, NA. www.catastro.meh.es/esp/referencia_catastral_1.asp. | C(≤20) |  |

4.2 Bloque F4-A2: Hardware informático y equipos telecomunicaciones.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo del activo asociada al CUAR. | C(≤256) |  |

4.3 Bloque F4-A3: Software.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo del activo asociada al CUAR. | C(≤256) |  |

4.4 Bloque F4-A4: Otras inversiones o servicios.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo del activo asociada al CUAR. | C(≤256) |  |

4.5 Bloque F4-A5: Instalaciones eléctricas asociadas al sistema de medidas del OS.

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo. | C(33) | Coherencia CUAR. |
| Descriptivo del CUAR. | Descriptivo del activo asociada al CUAR. | C(≤256) |  |

5. Formulario 5: F5_Datos generales de activos.

Sector de aplicación: Electricidad y gas.

Este Formulario contiene información relativa a los activos regulados puestos en servicio y con acta de cierre o desmantelamiento.

5.1 Bloque F5-G1: Datos Generales.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Se deben declarar todos los CUAR declarados en los Formularios 1 para electricidad (salvo Y y Z), 2 para gas y 4 para el OS/GTS. |
| Singular. | Indicar si la instalación es singular o no: SI/ NO. | B |  |
| Fecha de Puesta en marcha/ cierre/desmantelamiento /Ejecución. | En el caso de Instalaciones con Acta de puesta en servicio/cierre o desmantelamiento, fecha del Acta correspondiente. En el caso de Inversiones en investigación y exploración, fecha de presentación de la solicitud. En el caso de gas mínimo de llenado, gas talón o gas colchón indicar la fecha de registro contable de la compra. Para los activos del OS/GTS, y resto de activos de los que no se disponga de acta poner fecha de registro contable. | F |  |
| Valor reconocido. | Valor reconocido, en €, a efectos de retribución, si aplica. En el caso de activos regulados que no tienen un valor retributivo reconocido, reflejar 0 (cero). | NP(10,0) |  |
| Vida útil regulatoria. | Vida útil regulatoria, en años, reconocida del activo regulado. En el caso de no tener una vida útil regulatoria definida, reflejar 0 (cero). | NP(2,0) |  |
| Valor declarado. | Valor bruto declarado de la inversión, en €, declarado en la auditoría, sin descontar posibles subvenciones o instalaciones cedidas y financiadas por terceros. En el caso de no tener un valor declarado, reflejar 0 (cero). | NP(10,0) |  |
| Subvenciones. | Importe total, en €, de las subvenciones declaradas en la auditoría de inversión asociadas al activo regulado, si aplica. En el caso de no existir subvenciones o no tener auditoría de inversión, reflejar 0 (cero). | NP(10,0) |  |
| Instalaciones cedidas. | Importe, en €, de las instalaciones cedidas y financiadas por terceros declaradas en la auditoría de inversión asociadas al activo regulado. | NP(10,0) |  |
| Forma incorporación al Inmovilizado. | Indicar si es: 1. Inversión realizada directamente por el titular. 2. Adquisición mediante compra a un tercero. 3. Adquisición a título gratuito (Cesión y financiación por terceros). 4. Activo no Incorporado al inmovilizado (imputado en la Cuenta de Resultados). 5. Combinación de negocios. 6. Aportación de capital no dineraria. | NP(1,0) | Número de la lista. |

5.2 Bloque F5-G2: Compra-Venta de Activos Regulados.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado que se compra o vende durante el ejercicio. | C(33) | Declarado en los Formularios 1 para electricidad y 2 para gas y 4 para OS/GTS. |
| Operación. | Tipo de operación. 1. Compra. 2. Venta. | NP(1,0) | Número de la lista. |
| Fecha. | Fecha de la operación. | F |  |
| Importe. | Importe, en €, de la operación. | NP(9,2) |  |
| Empresa. | Nombre de la Empresa a la que se compra o vende el activo. | C(≤255) |  |
| CIF. | CIF de la empresa a la que se compra o vende el activo. | C(9) |  |
| Valor. | En el caso de venta, valor en libros del activo vendido la fecha de venta. En caso contrario 0. | NP(9,0) |  |
| CUAR anterior. | En el caso de compra, CUAR del activo en la empresa de origen. En caso contrario, CUAR del activo vendido. En caso de no existir CUAR anterior indicar NA. | C(33) | En el caso de compra, contenido en la base de datos de la empresa vendedora. En el caso de venta, debe coincidir con el del primer campo. |

5.3 Bloque F5-G3: Cambio de estado de los activos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código CUAR anterior. | Código CUAR anterior del activo que ha cambiado el estado (grado de materialización). | C(33) | Código CUAR declarado a cierre del ejercicio anterior o declarado por primera vez en los Formularios 1 o 2 en el ejercicio. |
| Cod CUAR nuevo. | Nuevo Código CUAR nuevo del activo. | C(33) | Declarado en los Formularios 1 para electricidad y 2 para gas. |
| Fecha. | Fecha de cambio de estado. | F | Fecha del ejercicio. |

6. Formulario 6: F6_Geolocalización de activos regulados.

Sector de aplicación: Electricidad y gas.

En este Formulario se identifican las coordenadas de los activos regulados.

6.1 Bloque F6-AR1: Coordenadas de los Activos Punto.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Declarado en el Formulario 1 para electricidad, 2 para gas y Bloque F4-A1 para el OS. Coherencia de activos Punto. |
| X. | Coordenada X de la localización del activo. | NP(10,2) |  |
| Y. | Coordenada Y de la localización del activo. | NP(10,2) |  |
| Z. | Coordenada Z de la localización del activo. | NP(10,2) |  |

6.2 Bloque F6-AR2: Coordenadas de los Activos Tramo.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado. | C(33) | Declarado en los Formularios 1 para electricidad en estado declarado S o Y, y en el Formulario 2 para gas. Coherencia de activos Tramo. |
| X. | Coordenada X de la localización del activo. | NP(10,2) |  |
| Y. | Coordenada Y de la localización del activo. | NP(10,2) |  |
| Z. | Coordenada Z de la localización del activo. | NP(10,2) |  |

6.3 Bloque F6-AR3: Coordenadas de los Terrenos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| ID Terreno. | Código del terreno sobre la que se asientan los activos regulados. Se construirá como un secuencial de hasta cinco (5) dígitos empezando por el 00001. | C(5) | La identificación de los terreno se mantendrá de un ejercicio al siguiente y se utilizarán códigos nuevos para nuevos terrenos. |
| X. | Coordenada X de la localización del vértice del terreno. | NP(10,2) |  |
| Y. | Coordenada Y de la localización del vértice del terreno. | NP(10,2) |  |
| Z. | Coordenada Z de la localización del vértice del terreno. | NP(10,2) |  |

6.4 Bloque F6-AR4: Correlación Activos-Terreno.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| ID Terreno. | Código del terreno sobre la que se asientan los activos regulados. | C(5) | Declarada en Bloque F6-AR3. |
| CUAR. | Código CUAR del activo incluido en el terreno. | C(33) | Declarado en los Formularios 1 para electricidad, 2 para gas y Bloque F4-A1 para el OS/GTS. |

7. Formulario 7: F7_ Localización y reparto de costes e ingresos.

Sector de aplicación: Electricidad y Gas Natural.

En este formulario el sujeto obligado debe declarar la localización de los costes e ingresos del ejercicio en los diferentes CECOS, OFC y activos regulados.

7.1 Bloque F7-L1: Localización de Costes en CECOS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el coste. | C(≤7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| Código CECOS. | Código del CECOS en el que se localiza el coste. | C(≤9) | Contenido en las Tablas 3 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| Importe. | Importe del coste localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L1, F7-L3 y F7-L5 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC4). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo Coste. | Código del tipo de coste localizado. | C(5) | Contenido en la Tabla 9. |
| Código Operación. | En el caso de provenir el coste de una operación con partes vinculadas, indicar el código de la operación. En caso contrario COD-OP-0. | C(8) | En caso de operación, contenido en el Bloque F9-DC7. |

7.2 Bloque F7-L2: Localización de Ingresos en CECOS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el ingreso. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| Código CECOS. | Código del CECOS en el que se localiza el ingreso. | C(≤9) | Contenido en las Tablas 3 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| Importe. | Importe del ingreso localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L2, F7-L4 y F7-L6 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC5). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo Ingreso. | Código del Tipo de Ingreso localizado. | C(5) | Contenido en la Tabla 8. |
| Código Operación. | En el caso de provenir el ingreso de una operación con partes vinculadas, o de un ingreso por subvenciones a la explotación o de ingresos por traspasos a resultados de subvenciones, donaciones o legados de capital. En caso contrario COD-OP-0. | C(8) | En el caso de una OPV, declarado en el Bloque F9-DC8. En el caso de una subvención a la explotación, F9-DC6. En el caso de una subvención al capital, F9-SI1. En el caso de una instalación cedida, F9- SI2. En el caso de una instalación financiada, F9-SI3. |

7.3 Bloque F7-L3: Localización de costes en OFC de inversión.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR-OFC. | En el caso de activos regulados, código del activo en el que se localiza el coste. En el caso inversiones en Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en el Bloque F10-P2. Los OFC contenidos en la Tabla 21. |
| Importe. | Importe del coste localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L1, F7-L3 y F7-L5 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC4). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo Coste. | Código del tipo de coste localizado. | C(5) | Contenido en la Tabla 9. |
| Concepto de coste. | Código del Concepto de coste. En el caso de compras de gas talón, gas colchón o gas mínimo de llenado de gasoducto y de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, Contenido en las Tablas 23 (Trasporte eléctrico), 25 (OS/GTS), 28 (Gas). |
| Materiales y equipos. | En el caso de que el Concepto de coste sea «Materiales y equipos», identificar los materiales y equipos según el tipo de activo. En caso contrario NA. | C(≤13) | Contenido en las tablas de materiales y equipos correspondientes. |
| Código OPV. | En el caso de provenir el coste de una operación con partes vinculadas, indicar el código de la operación. En caso contrario COD-OP-0. | C(8) | En caso de operación, contenido en el Bloque F9-DC7. |
| Código Operación. | En el caso de cesión y financiación por terceros, indicar el código de la operación. En caso contrario COD-OP- 0. | C(8) | En caso de operación, contenido en el Bloque F9-SI2 o F9-SI3. |

7.4 Bloque F7-L4: Localización de ingresos en OFC de inversión.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR-OFC. | Código del activo en el que se localiza ingreso. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en el bloque F10-P2. Los OFC contenidos en la Tabla 21. |
| Importe. | Importe del ingreso localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L2, F7-L4 y F7-L6 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC5). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo Ingreso. | Código del tipo de ingresos localizado. | C(5) | Contenido en la Tabla 8. |
| Código Operación. | En el caso de provenir el ingreso de una operación con partes vinculadas, o una subvención a la explotación. En caso contrario COD-OP-0. | C(8) | En el caso de una OPV, declarado en el Bloque F9-DC8. En el caso de una subvención a la explotación, F9-DC6. |

7.5 Bloque F7-L5: Localización de costes en OFC de O&M.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR-OFC. | Para actividades reguladas, Código CUAR/OFC en el que se localiza el coste. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en los Formularios 1,2 o 4. Los OFC contenidos en las Tablas 14-16 (electricidad) o 17-20 (gas). Los OFC de resto de actividades, contenidos en la Tabla 22. |
| Importe. | Importe del coste localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L1, F7-L3 y F7-L5 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC4). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo coste. | Código del tipo de costes localizado. | C(5) | Contenido en la Tabla 9. |
| Concepto de coste. | Código del Concepto de coste. En el caso de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, contenido en las Tablas 26 (electricidad), 27 (OS/GTS), 58 (Gas), 59 (carga y descarga de buques). |
| Centro de Mantenimiento. | Código del centro de mantenimiento al que está asociado el CUAR-OFC en el que se localizan los costes. | C(9) | Contenido en la Tabla 5 o declarados en Bloque F1-E6 para electricidad o en la Tabla 6 para Gas. |
| Código Operación. | En el caso de provenir el coste de una operación con partes vinculadas, indicar el código de la operación. En caso contrario COD-OP-0. | C(8) | En caso de operación, contenido en el Bloque F9-DC7. |
| Fijo / Variable. | Indicar si el coste localizado se considera respecto del uso: 1. Fijo. 2. Variable. | NP(1,0) | Número de la lista. |
| Recurrente. | Indicar si el coste localizado se considera: 1. Recurrente. 2. No recurrente. | NP(1,0) | Número de la lista. |

7.6 Bloque F7-L6: Localización de ingresos en OFC de O&M.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR-OFC. | Para actividades reguladas, Código CUAR/OFC en el que se localiza el ingreso. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en los Formularios 1, 2 o 4. Los OFC contenidos en las Tablas 14-16 (electricidad) o 17-20 (gas). Los OFC de resto de actividades, contenidos en la Tabla 22. |
| Importe. | Importe del ingreso localizado, en €. | N(10,0) | Todos los importes localizados por Cuenta de BSS y Tipo de coste en los Bloques F7-L2, F7-L4 y F7-L6 no pueden superar el saldo de dicha cuenta (Bloque F9-DC1) y tipo (Bloque F9-DC5). |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Tipo Ingreso. | Código del tipo de ingresos localizado. | C(5) | Contenido en la Tabla 8. |
| Centro de mantenimiento. | Código del centro de mantenimiento al que está asociado el CUAR-OFC en el que se localizan los ingresos. | C(9) | Contenido en la Tabla 5 o declarados en Bloque F1-E6 para electricidad o en la Tabla 6 para Gas. |
| Código Operación. | En el caso de provenir el ingreso de una operación con partes vinculadas, o de un ingreso por subvenciones a la explotación o de ingresos por traspasos a resultados de subvenciones, donaciones o legados de capital.. En caso contrario COD-OP-0. | C(8) | En el caso de una OPV, declarado en el Bloque F9-DC8. En el caso de una subvención a la explotación, F9-DC6. En el caso de una subvención al capital, F9-SI1. En el caso de una instalación cedida, F9- SI2. En el caso de una instalación financiada, F9-SI3. |

7.7 Bloque F7-R1: Parámetros CECOS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Cod CECOS. | Código del CECOS principal del que se declaran los parámetros. | C(≤9) | Contenido en las Tablas 4 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| IC-1. | Número medio de personas del CECOS durante el ejercicio. | NP(8,0) |  |
| IC-2. | Número de personas equivalentes del CECOS durante el ejercicio. | NP(8,0) |  |
| IC-3. | Número de pedidos generados por el CECOS Principal al CECOS auxiliar de Compras y Aprovisionamientos durante el ejercicio. | NP(8,0) |  |
| IC-4. | Importe total de pedidos generados por el CECOS Principal al CECOS auxiliar de Compras y Aprovisionamientos durante el ejercicio durante el ejercicio. | NP(8,0) |  |
| IC-5. | Número de equipos TIC corporativos asignados al CECOS. | NP(8,0) |  |
| IC-6. | Número de incidencias TIC generadas por el CECOS durante el ejercicio. | NP(8,0) |  |

7.8 Bloque F7-R2: Reparto primario. Modo de Referencia. Dedicación CECOS Asesoría jurídica y Regulación.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CECOS origen. | Código del CECOS Auxiliar del que se reparten los costes. | C(5) | Contenido en la Tabla 3: Sólo CC -A5 o CC-A8. |
| CECOS destino. | Código del CECOS Principal al que se reparten los costes. | C(≤9) | Contenido en la Tablas 4 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| Nivel de dedicación. | % Nivel de dedicación del CECOS auxiliar al CECOS referido. | NP(3,6) | Debe sumar 100 todas las dedicaciones por CECOS de origen. |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.9 Bloque F7-R3: Reparto primario. Modo Separación Actividades.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad que se reparte el coste. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| CECOS origen. | Código del CECOS Auxiliar del que se reparten los costes. | C(5) | Contenido en la Tabla 3. |
| CECOS destino. | Código del CECOS Principal al que se reparten los costes. | C(≤9) | Contenido en la Tablas 4 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| Nivel de dedicación. | % Nivel de dedicación del CECOS auxiliar al CECOS referido. | NP(3,6) | Debe sumar 100 todas las dedicaciones por CECOS de origen y actividad. |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.10 Bloque F7-R4: Reparto secundario a OFC Inversión. Modo de Referencia.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CECOS origen. | Código del CECOS principal del que se declaran los repartos. | C(9) | CC-P1/ CC-P2/ CCP6. Para los Centros de Mantenimiento de electricidad, en la Tabla 5 o, declarados en el Bloque F1-E6. Para los centros de mantenimiento de gas, en la Tabla 6. |
| CUAR/OFC. | Código CUAR del activo regulado. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en el Bloque F10-P2. Los OFC contenidos en la Tabla 21 |
| Concepto de coste. | Código del Concepto de coste. En el caso de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, Contenido en las Tablas 23 (Trasporte eléctrico), 25 (OS/GTS), 28 (Gas). |
| Nivel de dedicación. | % Nivel de dedicación del CECOS Principal al CUAR/OFC. | NP(3,6) | Debe sumar 100 todas las declaraciones por CECOS de origen, junto con lo declarado en el Bloque F7-R5 |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.11 Bloque F7-R5: Reparto secundario a OFC O&M. Modo de Referencia.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CECOS origen. | Código del CECOS principal del que se declaran los repartos. | C(9) | CC-P1/ CC-P2/ CCP6. Para los Centros de Mantenimiento de electricidad, en la Tabla 5 o, declarados en el Bloque F1-E6. Para los centros de mantenimiento de gas, en la Tabla 6. |
| CUAR/OFC. | Código del activo regulado/OFC al que se imputan costes. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en los Formularios 1, 2 y 4. Los OFC contenidos en las Tablas 14-16 (electricidad) o 17- 20 (gas). Los OFC de resto de actividades, contenidos en la Tabla 22. |
| Concepto de coste. | Código del Concepto de coste. En el caso en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, contenido en las Tablas 26 (electricidad), 27 (OS/GTS), 58 (Gas), 59 (carga y descarga de buques). |
| Centro de Mantenimiento. | Código del centro de mantenimiento al que está asociado el CUAR-OFC en el que se localizan los costes, si aplica. | C(9) | Contenido en la Tabla 5 o declarados en Bloque F1-E6 para electricidad y Tabla 6 o para Gas. |
| Nivel de dedicación. | % Nivel de dedicación del CECOS auxiliar al CUAR/OFC referido. | NP(3,6) | Debe sumar 100 todas las declaraciones por CECOS de origen, junto con lo declarado en el Bloque F7-R4. |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.12 Bloque F7-R6: Contratos ATR.

Descripción de campos:

| Campo | Declarados en los bloques correspondientes | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Declarados en los Bloques correspondientes. | C(5) | Contenido en las Tablas 1 (electricidad) o 2 (gas). |
| N.º contratos. | Número de contratos celebrados durante el año. | NP(4,0) |  |

7.13 Bloque F7-R7: Reparto secundario a OFC Inversión. Modo Separación de Actividades.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad de la que se está declarando el reparto. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| CECOS origen. | Código del CECOS principal del que se declaran los repartos. | C(≤9) | CC-P1/ CC-P2/ CC-P6. Para los Centros de Mantenimiento de electricidad, en la Tabla 5 o, declarados en el Bloque F1-E6. Para los centros de mantenimiento de gas, en la Tabla 6. |
| CUAR/OFC. | Código del activo regulado/OFC al que se imputan costes. | C (≤33 ) | Los CUAR deben estar declarados en el Bloque F10-P2. Los OFC contenidos en la Tabla 21. |
| Concepto de coste. | Código del Concepto de coste. En el caso de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, contenido en las Tablas 23/25 para electricidad, o 28 para gas. |
| Nivel de dedicación. | % Nivel de dedicación del CECOS Principal al CUAR/OFC. | NP(3,6) | Debe sumar 100 todas las declaraciones por CECOS de origen y actividad, junto con lo declarado en el Bloque F7-R8. |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.14 Bloque F7-R8: Reparto secundario a OFC O&M. Modo Separación Actividades.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad de la que se está declarando el reparto. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| CECOS origen. | Código del CECOS principal del que se declaran los repartos. | C(≤9) | CC-P1/ CC-P2/ CC-P6. Para los Centros de Mantenimiento de electricidad, en la Tabla 5 o, declarados en el Bloque F1-E6. Para los centros de mantenimiento de gas, en la Tabla 6. |
| CUAR/OFC. | Código del activo regulado/OFC al que se imputan costes. En el caso de Distribución, Otras reguladas o No Reguladas, código del OFC. | C(≤33) | Los CUAR deben estar declarados en los Bloques F1, F2 o F4. Los OFC contenidos en las Tablas 14-16 (electricidad) o 17-20 (gas). Los OFC de resto de actividades, contenidos en la Tabla 22. |
| Concepto de coste. | Código del Concepto de coste. En el caso de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(≤13) | En el caso de Concepto de Coste, contenido en las Tablas 26/27 para electricidad o 58/59 para gas. |
| Centro de Mantenimiento. | Código del centro de mantenimiento al que está asociado el CUAR-OFC en el que se localizan los costes, si aplica. En el caso de inversiones en Distribución, Otras reguladas o No Reguladas, NA. | C(9) | Contenido en la Tabla 5 o Bloque F1-E6 para electricidad o Tabla 6 para gas. |
| Nivel de dedicación. | % Nivel de dedicación del CECOS Principal al CUAR/OFC. | NP(3,6) | Debe sumar 100 todas las declaraciones por CECOS de origen y actividad junto con lo declarado en el Bloque F7-R7. |
| Descripción. | Descripción del método utilizado para la obtención de los porcentajes declarados. | C(≤255) |  |

7.15 Bloque F7-R9: Asignación de activos a CECOS.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asignado el activo. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| Código CECOS. | Código del CECOS en el que se localizan los activos. | C(≤9) | Contenido en las Tablas 3 a 6. Para los Centros de Mantenimiento de electricidad declarados en el Bloque F1-E6. |
| Inmovilizado Intangible. | Importe total, en €, del inmovilizado intangible localizado en el CECOS a 31 de diciembre de cada ejercicio. | NP(9,2) |  |
| Amortización Acumulada II. | Importe total, en €, de la amortización acumulada del inmovilizado intangible localizado en el CECOS a 31 de diciembre de cada ejercicio. | NP(9,2) |  |
| Inmovilizado Material. | Importe total, en €, del inmovilizado material localizado en el CECOS a 31 de diciembre de cada ejercicio. | NP(9,2) |  |
| Amortización Acumulada IM. | Importe total, en €, de la amortización acumulada del inmovilizado material localizado en el CECOS a 31 de diciembre de cada ejercicio. | NP(9,2) |  |

8. Formulario 8: F8_Reclasificación de costes e ingresos en un proyecto.

Sector de aplicación: Electricidad y Gas Natural.

En este formulario el sujeto obligado podrá, en caso de necesidad, reasignar coste e ingresos localizados en determinados OFC (CUAR) de inversión en ejercicios anteriores, a otros OFC (CUAR) de inversión del mismo proyecto de inversión.

Bloque F8-R1: Reclasificación de costes e ingresos en un proyecto.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR 1. | Código CUAR del activo del que se reparten los costes. | C(33) | Declarado el ejercicio anterior. |
| CUAR 2. | Código CUAR del activo al que se reparten los costes. | C(33) | Declarado en Bloque F10-P2. |
| Concepto de Coste. | Concepto de coste del que se reparten los costes en los nuevos CUAR. | C(≤13) |  |
| Materiales y equipos. | En el caso de que el Concepto de Coste sea «Materiales y equipos», identificar el código correspondiente. En caso contrario NA. | C(≤13) | Contenido en las tablas correspondientes. |
| Porcentaje. | Porcentaje, en base 100, de costes acumulados en el CUAR original y del Concepto de Coste/Materiales y equipos seleccionado que se asignan al nuevo CUAR. | NP(3,1) | La suma de todos los porcentajes repartidos a distintos CUAR por Concepto de Coste no debe superar 100. |

9. Formulario 9: F9_Datos Económicos y Contables.

Sector de aplicación: Electricidad y Gas Natural.

En este formulario el sujeto obligado deberá aportar información económico-financiera general de la empresa que permita comprobar las asignaciones anteriores así como la traza de otra información enviada a la CNMC.

9.1 Bloque F9-DC1: Balance de sumas y saldos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Cuenta BSS. | Número de cuenta contable, de 10 dígitos, del balance de sumas y saldos de la empresa. | NP(10,0) |  |
| Nombre. | Nombre de la cuenta contable en la contabilidad de la empresa. | C(≤255) |  |
| Saldo Inicial. | Saldo, en €, al inicio del ejercicio de la cuenta contable Los saldos deudores con signo positivo, y los acreedores con negativo. | N(10,0) | La columna debe sumar cero. |
| Debe. | Importe total, en €, de las anotaciones al Debe de la cuenta contable durante el ejercicio. Los incrementos de los saldos deudores en signo positivo. | N(10,0) |  |
| Haber. | Importe total, en €, de las anotaciones al Haber de la cuenta contable durante el ejercicio. Los incrementos en los saldos acreedores serán negativos. | N(10,0) |  |
| Saldo final. | Saldo, en €, al final del ejercicio de la cuenta contable. Los saldos deudores con signo positivo, y los acreedores con negativo. | N(10,0) | Igual de Saldo inicial+Debe-Haber. La columna debe sumar cero. |

9.2 Bloque F9-DC2: Correspondencia BSS-SICSE Balance.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Año. | Ejercicio contable al que se refiere la declaración. | NP(4,0) |  |
| Cod_SICSE. | Código correspondiente al epígrafe de los estados financieros de SICSE en el que se encuentre recogida cada cuenta contable. | C(≤8) | Correspondencia con las Tablas 10 para electricidad y 12 para gas. |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Saldo, en €, a cierre del ejercicio n de cada una de las cuentas contables o parte de ellas. | N(10,0) |  |

9.3 Bloque F9-DC3: Correspondencia BSS-SICSE Cuenta de PyG.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Cod_SICSE. | Código correspondiente al epígrafe de los estados financieros de SICSE en el que se encuentre recogida cada cuenta contable. | C(≤8) | Correspondencia con las Tablas 11 para electricidad y 13 para gas. |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Saldo, en €, a cierre del ejercicio n de cada una de las cuentas contables o parte de ellas. | N(10,0) |  |

9.4 Bloque F9-DC4: Clasificación de Costes.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el Coste. | C(7) | Contenido en la Tabla 1 (electricidad) y Tabla 2 (gas). |
| Tipo coste. | Código de coste. | C(5) | Contenido en la Tabla 9. |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el coste. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Importe, en €, del coste. | N(10,0) | Los importes totales por cuenta de BSS deben sumar el saldo de la misma en el Bloque F9-DC1, excepto en los tipos de coste CC-43 a CC-50, que no deberá superar las altas en dicha cuenta durante el ejercicio. |

9.5 Bloque F9-DC5: Clasificación de Ingresos.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el ingreso. | C(7) | Contenido en la Tabla 1 (electricidad) y Tabla 2 (gas). |
| Tipo ingresos. | Código de ingreso. | C(5) | Contenido en la Tabla 8. |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el ingreso. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Importe, en €, del ingreso. | N(10,0) | Los importes totales por cuenta de BSS deben sumar el saldo de la misma en el Bloque F9-DC1. |

9.6 Bloque F9-DC6: Subvenciones a la explotación.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Se codificarán todas las subvenciones recibidas en el ejercicio de forma secuencial empezando por el SBE-0001. | C(8) |  |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizada. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Importe, en €, de la subvención recibida. | N(10,0) |  |
| Actividad subvencionada. | Actividad subvencionada. | C(≤255) |  |
| Descripción. | Descripción y motivo de la subvención. | C(≤255) |  |
| Entidad concedente. | Entidad u organismo que concede la subvención. | C(≤255) |  |
| Fecha de concesión. | Fecha de obtención de la subvención. | F |  |

9.7 Bloque F9-DC7: Operaciones con partes vinculadas de coste.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Se codificarán todas las operaciones con partes vinculadas recibidas en el ejercicio de forma secuencial empezando por el OPVC-001. | C(8) |  |
| Tipo PV. | Seleccione el tipo de parte vinculada con el que realiza la operación. 1. Empresa del grupo según el artículo 42 del Código de Comercio (incluye dominantes, dependientes y otras dependientes de la misma dominante). 2. Empresa asociada o negocios conjuntos. 3. Accionistas con una participación superior al 10% y sociedades de su grupo. | NP(1,0) | Número de la lista. |
| Tipo operación. | Seleccione el tipo de operación realizada: 1. Gastos financieros. 2. Alquileres. 3. Recepción de servicios: servicios corporativos. 4. Recepción de servicios: servicios de O&M. 5. Recepción de servicios: servicios de ATR. 6. Adquisición de inmovilizado: en curso o terminado (incluye anticipos a cuenta de entregas futuras). 7. Otras compras. 8. Otros. | NP(1,0) | Número de la lista. |
| Razón Social. | Razón social o denominación de la parte vinculada con la que se realiza la operación. | C(≤255) |  |
| CIF-NIF. | CIF o NIF de la parte vinculada. | C(9) |  |
| Descripción. | Descripción de la operación realizada. | C(≤255) |  |
| Importe. | Importe, en €, de la operación contabilizada durante el ejercicio. | NP(10,0) |  |
| Margen. | Margen de la operación, en porcentaje, aplicado por la empresa de origen sobre el coste de la empresa de origen. | NP(3,2) |  |
| Código del Contrato. | Se indicará el código del contrato que recoge la operación con partes vinculadas. La codificación de dichos contratos se hará de forma secuencial empezando por COPV-001. | C(8) | Deberá aportarse el contrato en formato .pdf según las instrucciones. |

9.8 Bloque F9-DC8: Operaciones con partes vinculadas de ingreso.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Se codificarán todas las operaciones con partes vinculadas realizadas en el ejercicio de forma secuencial empezando por el OPVI-001. | C(8) |  |
| Tipo PV. | Seleccione el tipo de parte vinculada con el que realiza la operación. 1. Empresa del grupo según el artículo 42 del Código de Comercio (incluye dominantes, dependientes y otras dependientes de la misma dominante). 2. Empresa asociada o negocios conjuntos. 3. Accionistas con una participación superior al 10% y sociedades de su grupo. | NP(1,0) | Número de la lista. |
| Tipo Operación. | Seleccione el tipo de operación realizada: 1. Ingresos financieros. 2. Dividendos recibidos. 3. Alquileres. 4. Prestación de servicios: servicios corporativos. 5. Prestación de servicios: servicios de O&M. 6. Prestación de servicios: trabajos para el inmovilizado. 7. Venta de inmovilizado. 8. Otros. | NP(1,0) | Número de la lista. |
| Razón Social. | Razón social o denominación de la parte vinculada con la que se realiza la operación. | C(≤255) |  |
| CIF-NIF. | CIF o NIF de la parte vinculada. | C(9) |  |
| Descripción. | Descripción de la operación realizada. | C(≤255) |  |
| Importe. | Importe, en €, de la operación contabilizada durante el ejercicio. | N(10,0) |  |
| Margen. | Margen de la operación, en porcentaje, aplicado por la empresa sobre su coste. | NP(3,2) |  |
| Código del Contrato. | Se indicará el código del contrato que recoge la operación con partes vinculadas. La codificación de dichos contratos se hará de forma secuencial empezando por COPV-001. | C(8) |  |

9.9 Bloque F9-DC9 Descomposición de los TREI.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizado el gasto activado. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Importe. | Importe, en €, del gasto activado. | NP(10,0) |  |

9.10 Bloque F9-DC10: Inversiones en instrumentos financieros.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Tipo de inversión. | Seleccione el tipo de inversión. 1. Acciones. 2. Bonos. 3. Obligaciones. 4. Otros. | NP(1) | Número de la lista. |
| Nombre empresa. | Nombre de la empresa. | C(≤255) |  |
| Identificación empresa. | Código CIF empresa. | C(≤50) |  |
| Fecha. | Fecha de adquisición. | F |  |
| Importe adquisición. | Importe, en €, de la adquisición en la fecha de la misma. | NP(9,0) |  |
| Valoración. | Valor contable a cierre de ejercicio. | NP(9,0) |  |
| Cuenta BSS. | Número de cuenta a 10 dígitos del BSS donde está contabilizada la inversión. | NP(10,0) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |

9.11 Bloque F9-DI1: Clasificación del inmovilizado por actividades.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el inmovilizado. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| Tipo. | Seleccione el tipo de inmovilizado. 1. Activo Regulado. 2. Activo No Regulado. | NP(2,0) | Número de la lista. |
| Inmovilizado bruto. | Importe, en €, del inmovilizado, material, inmaterial o en curso, incluyendo el totalmente amortizado, a 31 de diciembre del ejercicio. | NP(10,0) |  |
| Cuenta BSS IB. | Número de cuenta a 10 dígitos del BSS donde está registrado el inmovilizado anterior. | NP(10,0) | Contenida en Campo «Cuenta BSS» del Bloque F9-DC 1. |
| Amortización Acumulada. | Importe, en €, de la amortización acumulada del inmovilizado anterior a 31 de diciembre del ejercicio. En caso de inmovilizado no amortizable, se indicará 0. | N(10,0) |  |
| Cuenta BSS AA. | Número de cuenta a 10 dígitos del BSS donde está registrada la amortización acumulada anterior. En caso de inmovilizado no amortizable, se indicará 0. | NP(10,0) | Contenida en Campo «Cuenta BSS» del Bloque F9-DC 1. |

9.12 Bloque F9-DI2: Movimiento del inmovilizado por actividades.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Actividad. | Código de la actividad a la que está asociado el inmovilizado. | C(7) | Contenido en las Tabla 1 para Electricidad y Tabla 2 para Gas. |
| Estado. | Seleccione el estado del inmovilizado: 1. En funcionamiento. 2. En curso. | NP(1,0) | Número de la lista. |
| Tipo. | Seleccione el tipo del inmovilizado: 1. Activo Regulado. 2. Activo No Regulado. | NP(1,0) | Número de la lista. |
| Valor al inicio. | Importe, en €, del inmovilizado correspondiente (para la actividad, estado y tipo), al inicio del ejercicio, incluyendo los activos totalmente amortizados. | NP(10,0) |  |
| Altas. | Importe, en €, de las altas del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | NP(10,0) |  |
| Bajas. | Importe, en €, de las bajas del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | NP(10,0) |  |
| Traspasos. | Importe, en €, de los traspasos de inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| Valor al cierre. | Importe, en €, del inmovilizado bruto correspondiente (para la actividad, estado y tipo), al final del ejercicio, incluyendo los activos totalmente amortizados. | NP(10,0) |  |
| AA Valor al inicio. | Importe, en €, de la amortización acumulada del inmovilizado correspondiente (para la actividad, estado y tipo), al inicio del ejercicio. | N(10,0) |  |
| AA Dotaciones. | Importe, en €, de las dotaciones a la amortización del inmovilizado (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| AA Bajas. | Importe, en €, de las bajas de amortización acumulada del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| AA Traspasos. | Importe, en €, de los traspasos de amortización acumuladas del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| AA Valor al cierre. | Importe, en €, de la amortización acumulada del inmovilizado bruto correspondiente (para la actividad, estado y tipo), al final del ejercicio. | N(10,0) |  |
| Deterioro inicio. | Importe, en €, de la provisión por deterioro del inmovilizado (para actividad, estado y tipo) al inicio del ejercicio. | N(10.0) |  |
| Dotaciones deterioro. | Importe, en €, de la dotación por deterioro del inmovilizado correspondiente y revalorizaciones (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| Traspasos. | Importe, en €, de los aumentos o disminuciones por traspasos de la provisión por deterioro del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| Aplicaciones. | Importe, en €, de las disminuciones por aplicaciones de la provisión por deterioro del inmovilizado correspondiente (para la actividad, estado y tipo), durante el ejercicio. | N(10,0) |  |
| Deterioro cierre. | Importe, en €, de la provisión por deterioro del inmovilizado (para actividad, estado y tipo) al cierre del ejercicio. | N(10,0) |  |

9.13 Bloques F9-DI3: Correlación de Activos regulados - Activos contables.

Descripción de campos:

| Nombre campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código único asignado al activo según reglas de codificación establecidas. | C(33) | Declarado en los Formularios 1 (declarados en estado S o X), 2 y 4 y en los Formularios 11, 12 y 13. |
| Cuentas BSS. | Número de cuenta a diez dígitos de inmovilizado del Balance de Sumas y Saldos en la que se encuentra registrada la inversión realizada en el activo regulado. | NP(10) | Contenida en campo «Cuenta BSS» del Bloque F9-DC1. |
| Código interno. | Código asignado por la empresa en el registro auxiliar de inmovilizado a cada uno de los elementos contables que componen el activo regulado. En su defecto, partida contable en la que se encuentra registrado el activo regulado. | C(≤25) |  |
| Denominación | Denominación del elemento contable que compone el activo regulado. | C(≤255) |  |

9.14 Bloques F9-DI4: Información de los activos contables regulados.

Descripción de campos:

| Nombre campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código interno. | Código asignado por la empresa en el registro auxiliar de inmovilizado a cada uno de los elementos contables que componen el activo regulado. En su defecto, partida contable en la que se encuentra registrado el activo regulado. | C(≤25) | Declarado en Bloque F9-DI3. |
| Valor contable alta. | Coste de producción o precio de adquisición, en €, de las partidas contables. | NP(10,0) |  |
| Fecha alta. | Fecha de registro contable del activo: fecha de adquisición del activo o fecha de reclasificación del activo de inmovilizado en curso a inmovilizado terminado. | F |  |
| Valor contable cierre. | Valor bruto contable, en €, del elemento contable a fecha de cierre del ejercicio. | NP(10,0) |  |
| Amortización acumulada. | Importe de la amortización acumulada, en €, correspondiente al elemento contable a cierre del ejercicio. | N(10,0) |  |
| Valor neto contable. | Valor neto contable, en €, del elemento contable a fecha de cierre del ejercicio. | NP(10,0) |  |
| Método de amortización. | Seleccione el método de amortización utilizado, vigente en el ejercicio de la declaración. 1. Lineal. 2. Otro. | NP(1,0) |  |
| Vida útil. | Número de años de vida útil, en años, del elemento contable, vigente en el ejercicio de la declaración. | NP(10,2) |  |
| Revalorizaciones anteriores a 1996. | Importe, en €, de las revalorización anteriores al año 1996 por leyes de Actualización de Balances. | NP(10,0) |  |
| Revalorizaciones 1996. | Importe, en €, de la revalorización incluida en el valor contable bruto a cierre del ejercicio para el elemento contable, que se haya contabilizado por la ley de Actualización de Balances (RD-Ley 7/1996). | NP(10,0) |  |
| Revalorizaciones 2013. | Importe de la revalorización incluida en el valor contable bruto a cierre del ejercicio para el elemento contable, que se hayan contabilizado por la ley de Actualización de Balances (Ley 12/2012). | NP(10,0) |  |
| Costes por desmantelamiento. | Importe, en €, de la estimación por costes de desmantelamiento activada como mayor valor contable bruto del activo. | NP(10,0) |  |
| Modificaciones. | Importe de las modificaciones (valor total acumulado) que haya experimentado el valor contable bruto del elemento contable desde la fecha de alta en el inmovilizado hasta la fecha de cierre del ejercicio. | NP(10,0) |  |
| Motivo. | Descripción de las modificaciones que hayan tenido lugar en el ejercicio de la declaración. Si no hay modificaciones, NA. | C(≤255) |  |
| Deterioros. | Importe de los deterioros (valor total acumulado) asociados al activo. | N(10,0) |  |
| Motivo Deterioros. | Descripción del motivo del deterioro del inmovilizado que haya tenido lugar en el ejercicio de la declaración. | C(≤255) |  |
| Subvenciones. | Importe bruto, en €, de las subvenciones de capital concedidas para financiar el elemento contable (sin tener en cuenta el efecto impositivo). | N(10,0) |  |
| Origen. | Indicar el origen de los elementos contables correspondientes a cada activo regulado: 1. Construcción propia. 2. Adquirido a terceros a título oneroso. 3. Adquirido a título gratuito o cedido por terceros. 4. Combinaciones de negocios. 5. Aportación no dineraria. | NP(1,0) |  |

9.15 Bloque F9-SI1: Desglose subvenciones de capital a cierre del ejercicio.

Descripción de campos:

| Nombre campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Se codificarán todas las subvenciones que figuran en el BSS a cierre del ejercicio de forma secuencial empezando por el SBC-0001. | C(8) | La codificación se mantendrá de un ejercicio al siguiente para las mismas subvenciones. |
| Importe. | Importe bruto, en €, concedido correspondiente a las subvención. | N(10,0) |  |
| Valor contable. | Importe, en €, neto de efecto impositivo, pendiente de imputar a resultados de la subvención de capital al cierre de ejercicio. Este importe debe ser coincidente con el importe reflejado en las cuentas anuales auditadas del ejercicio. | N(10,0) |  |
| Fecha. | Fecha de concesión de la subvención. | F |  |
| Nombre. | Nombre de la subvención concedida. | C(≤255) |  |
| Organismo. | Organismo que concede la subvención. | C(≤255) |  |
| Tipo Organismo. | Tipo de organismo que concede la Subvención: 1. Administración General del Estado. 2. Comunidad Autónoma. 3. Administración local. 4. Unión Europea. 5. Otros. | NP(1,0) | Número de la lista. |
| Descripción. | Describir la subvención recibida. | C(≤255) |  |
| Tipo Activo. | Indicar si activo asociado a la subvención es regulado o no regulado: 1. Activos Regulados. 2. Activos No Regulados. 3. Ambos. | N(10) | Número de la lista. |

9.16 Bloque F9-SI2: Identificación de instalaciones cedidas por terceros.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Código asignado por la empresa para la identificación de la cesión mediante un código asignado por la empresa. La empresa deberá crear un código secuencial para su identificación empezando por el ICT-0001. | C(8) | Los códigos de las operaciones se mantendrán de un ejercicio al siguiente. |
| Importe. | Importe bruto, en €, de la cesión. | NP(9,0) |  |
| Descripción de la Cesión. | Descripción de las instalaciones cedidas por terceros asociada a activos regulados. | C(≤255) |  |
| Nombre Sujeto Cedente. | Nombre del Sujeto que ha cedido la instalación que forma parte de la unidad constructiva. | C(≤255) |  |
| CIF Sujeto Cedente. | NIF del Sujeto que ha cedido la instalación que forma parte de la unidad constructiva. | C(9) |  |
| Valoración de la Cesión. | Importe total, en €, de las instalaciones cedidas por terceros. | NP(10,0) |  |
| Fecha de la cesión. | Fecha en la que se produce la cesión de la instalación. | F |  |

9.17 Bloque F9-SI3: Identificación de instalaciones financiadas por terceros.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Operación. | Código asignado por la empresa para la identificación de la financiación mediante un código asignado por la empresa. La empresa deberá crear un código secuencial para su identificación empezando por el IFT-0001. | C(8) | Los códigos de las operaciones se mantendrán de un ejercicio al siguiente. |
| Valoración de la financiación. | Importe, en €, de las instalaciones financiadas por terceros asociada activos regulados. | NP(10,0) |  |
| Descripción de la financiación. | Descripción de las instalaciones financiadas por terceros. | C(≤255) |  |
| Nombre Sujeto financiador. | Nombre del Sujeto que ha financiado la instalación que forma parte de la unidad constructiva. | C(≤255) |  |
| CIF Sujeto financiador. | NIF del Sujeto que ha financiado la instalación que forma parte de la unidad constructiva. | C(9) |  |

9.18 Bloque F9-SI4: Asignación de Subvenciones de Capital, Instalaciones Cedidas e Instalaciones financiadas por terceros a CUAR.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado al que se asocian las operaciones. | C(33) |  |
| Código Operación. | Código de la operación que se asigna al CUAR. | C(8) | Declaradas en los Bloques F9-SI1, F9-SI2 y F9-SI3. |
| Importe. | Importe bruto, en €, de la operación que se asigna al CUAR. | NP(9,0) | La suma de los importes por código de operación no pueden superar el importe de la misma. |

9.19 Bloque F9-PC1: Identificación de proveedores.

Descripción de campos:

| Nombre campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Proveedor. | Código asignado por la empresa para la identificación del proveedor. La empresa deberá crear un código secuencial para su identificación empezando por el PRO-0001. | C(8) | El código de proveedor se debe mantener de un ejercicio al siguiente. |
| Razón Social. | Razón social o denominación del proveedor. | C(≤255) |  |
| CIF-NIF. | CIF o NIF del proveedor, según aplique. | C(9) |  |
| Tipo de suministro. | Explicación de los tipos de suministro que realiza el proveedor. | C(≤255) |  |
| Importe gasto. | Importe, en €, contabilizado como gasto en el ejercicio. | NP(9,0) |  |
| Importe inversión. | Importe total, en €, contabilizado como inversión en el ejercicio. | NP(9,0) |  |
| Parte vinculada. | Indicar si el proveedor es una parte vinculada: Sí/No. | B |  |

9.20 Bloque F9-PC2: Identificación de Contratos/pedidos principales.

Descripción de campos:

| Nombre campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Contrato. | Código asignado por la empresa para la identificación del contrato/pedido. La empresa deberá crear un código secuencial para su identificación empezando por el CTP-0001. | C(8) | El código se debe mantener de un ejercicio al siguiente, si aplica. |
| Objeto contrato/ pedido. | Descripción del objeto contrato/pedido. | C(≤255) |  |
| Fecha Inicio. | Fecha de inicio. | F |  |
| Razón social. | Razón social de la empresa contratada. | C(≤255) |  |
| CIF. | CIF de la empresa contratada. | C(9) |  |
| Importe Total previsto. | Importe, en €, total previsto del contrato/pedido. | NP(8,0) |  |
| Importe ejecutado en el ejercicio. | Importe, en €, ejecutado en el ejercicio con cargo al contrato/pedido. | NP(8,0) |  |
| Importe ejecutado acumulado. | Importe, en €, ejecutado acumulado con cargo al contrato/pedido. | NP(8,0) |  |

10. Formulario 10: F10_Proyectos de inversión.

Sector de aplicación: Electricidad y Gas Natural.

En este formulario el sujeto obligado deberá aportar información económico-financiera general de la empresa que permita comprobar las asignaciones anteriores así como la traza de otra información enviada a la CNMC.

10.1 Bloque F10-P1: Proyectos en curso, planificados y en desmantelamiento.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código Proyecto. | Código del proyecto constructivo de la empresa. Será un secuencia de 5 dígitos, empezando por el P0001. | C(5) |  |
| Descriptivo. | Descripción del proyecto. | C(≤255) |  |
| Fecha comienzo. | Fecha de comienzo real de la inversión en el caso de haber comenzado, o fecha prevista de inicio en el caso de no haberlo hecho. | F |  |
| Fecha fin. | Fecha prevista de finalización del proyecto. | F |  |
| Presupuesto. | Presupuesto total de ejecución del proyecto, en €, sin descontar subvenciones ni instalaciones cedidas y financiadas por terceros. | N(9,0) |  |

10.2 Bloque F10-P2: Activos en curso y en desmantelamiento.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código CUAR. | Código del activo. | C(33) | Coherencia del CUAR. |
| Nombre. | Descriptivo de activo. | C(≤255) |  |
| Código Proyecto. | Código del proyecto al que está asociado el activo. | C(5) | Declarado en Bloque F10-P1. |
| Fecha comienzo. | Fecha de comienzo real de la inversión. | F |  |
| Fecha fin. | Fecha de finalización prevista. Fecha de finalización efectiva, cuando el activo haya entrado en servicio. | F |  |
| Presupuesto total. | Presupuesto total de ejecución del activo, en €, sin descontar subvenciones ni instalaciones cedidas y financiadas por terceros. | NP(9,0) |  |
| Presupuesto ejecutado. | Coste total incurrido, en €, en el activo hasta fin de ejercicio de la declaración (n). | NP(9,0) |  |
| Presupuesto n+1. | Presupuesto de ejecución previsto para el ejercicio n+1, en €. | NP(9,0) |  |
| Presupuesto n+2. | Presupuesto de ejecución previsto para el ejercicio n+2, en €. | NP(9,0) |  |
| Presupuesto n+3. | Presupuesto de ejecución previsto para el ejercicio n+3. | NP(9,0) |  |
| Resto presupuesto. | Presupuesto de ejecución previsto hasta la finalización a partir del n+4 (n+4 incluido), en €. | NP(9,0) |  |
| Subvenciones. | Importe de las subvenciones previstas de recibir para la construcción del activo regulado, en €. | NP(9,0) |  |
| Tipo Organismo. | Tipo de organismo que concede la Subvención: 1. NA. No hay prevista subvención. 2. Administración General del Estado. 3. Comunidad Autónoma. 4. Administración local. 5. Unión Europea. 6. Otros. | NP(1,0) | Número de la lista. |
| Instalaciones cedidas. | Importe previsto de instalaciones cedidas asociadas al activo. | NP(9,0) |  |
| Instalaciones financiadas. | Importe previsto de instalaciones financiadas por terceros asociadas al activo. | NP(9,0) |  |

10.3 Bloque F10-P3: Activos planificados.

Descripción de campos:

| Nombre código | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código planificación. | Código asignado al activo planificado. | C(13) | Corresponde a los Bloques 1 y 2 del código CUAR. |
| Nombre. | Descriptivo de activo. | C(≤255) |  |
| Código Proyecto. | Código del proyecto al que está asociado el activo. | C(5) | Declarado en Bloque F10-P1. |
| Fecha comienzo. | Fecha prevista de inicio (ejercicio m). | F |  |
| Fecha fin. | Fecha de finalización prevista del proyecto. | F |  |
| Presupuesto total. | Presupuesto total de ejecución del activo, sin descontar subvenciones ni instalaciones cedidas y financiadas por terceros. | NP(9,0) |  |
| Presupuesto n+1. | Presupuesto de ejecución previsto para el ejercicio n+1. | NP(9,0) |  |
| Presupuesto n+2. | Presupuesto de ejecución previsto para el ejercicio n+2. | NP(9,0) |  |
| Presupuesto n+3. | Presupuesto de ejecución previsto para el ejercicio n+3. | NP(9,0) |  |
| Resto presupuesto. | Presupuesto de ejecución previsto hasta la finalización a partir del n+4 (incluido n+4). | NP(9,0) |  |
| Subvenciones. | Importe de las subvenciones previstas de recibir para la construcción del activo regulado. | NP(9,0) |  |
| Tipo Organismo. | Tipo de organismo que concede la Subvención: 1. NA. No hay prevista subvención. 2. Administración General del Estado. 3. Comunidad Autónoma. 4. Administración local. 5. Unión Europea. 6. Otros. | NP(1,0) | Número de la lista. |
| Instalaciones cedidas. | Importe previsto de instalaciones cedidas asociadas al activo. | NP(9,0) |  |
| Instalaciones financiadas. | Importe previsto de instalaciones financiadas por terceros asociadas al activo. | NP(9,0) |  |
| Código TA. | Tipo de Actuación en función de la necesidad y la probabilidad: 0. NA (Gas). 1. A: Actuaciones programadas sin ningún tipo de condicionante. 2. B1: Actuaciones conexión condicionadas con incertidumbre moderada en cuanto a su ejecución. 3. B2:Actuaciones de conexión condicionadas con incertidumbre media-alta en cuanto a su ejecución. 4. R:Retrasada. | NP(1,0) | Número de la lista. |
| MRDT. | Indicar si la motivación de la actuación es debido a Mallado de la red de Transporte: 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| CINT. | Indicar si la motivación de la actuación es debido Conexión internacional: 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| ATA. | Indicar si la motivación de la actuación es debido a Alimentación del Tren de Alta velocidad: 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| EVRO. | Indicar si la motivación de la actuación es debido a Evacuación de régimen ordinario: 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| EVRE. | Indicar si la motivación de la actuación es debido a Evacuación de régimen especial: 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| APD. | Indicar si la motivación de la actuación es debido a Apoyo a la distribución o demanda de grandes consumidores (excepto ATA): 0. NA (Gas). 1. Sí. 2. No. | NP(1,0) | Número de la lista. |
| Código función. | 0. NA (Gas). 1. Estructural. 2. De conexión. | NP(1,0) | Número de la lista. |
| Código actuación. | 0. NA (Gas). 1. Actuación nueva. 2. Ampliación. 3. Renovación. | NP(1,0) | Número de la lista. |

10.4 Bloque F10-P4: Recodificación de activos en curso.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR 1. | Código CUAR original del activo. | C(33) | Declarado el ejercicio anterior. |
| CUAR 2. | Nuevo código CUAR del activo anterior. | C(33) | Coherencia CUAR. |
| Motivo cambio. | Indicar el motivo del cambio. | C(≤255) |  |

10.5 Bloque F10-P5: Compra venta de activos en curso.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado en curso que se compra o vende durante el ejercicio. | C(33) | Declarado en los Formularios 11 para electricidad y 12 para gas. |
| Operación. | Tipo de operación. 1. Compra. 2. Venta. | NP(1,0) | Número de la lista. |
| Fecha. | Fecha de la operación. | F |  |
| Importe. | Importe, en €, de la operación. | NP(9,2) |  |
| Empresa. | Nombre de la Empresa a la que se compra o vende el activo. | C(≤255) |  |
| CIF. | CIF de la empresa a la que se compra o vende el activo. | C(9) |  |
| Valor. | En el caso de venta, valor en libros del activo vendido la fecha de venta. En caso contrario 0. | NP(9,0) |  |
| CUAR anterior. | En el caso de compra, CUAR del activo en la empresa de origen. En caso contrario, CUAR del activo vendido. | C(33) | En el caso de compra, contenido en la base de datos de la empresa vendedora. En el caso de venta, debe coincidir con el del primer campo. |

11. Formulario 11: F11_Activos_E en curso.

Sector de aplicación: Eléctrico.

Este Formulario contiene la base de datos de activos regulados que aún no estén puestos en servicio así como sus características técnicas.

Los Bloques que lo componen y sus campos son los mismos que el Formulario 1 con la salvedad de que la información aportada en relación a las características técnicas será estimada.

En la asignación del centro de mantenimiento se deberá cumplimentar con 000.

Los bloques a rellenar son los siguientes:

Bloque F11-E1: Líneas eléctricas.

Bloque F11-E2: Posiciones.

Bloque F11-E3: Transformadores.

Bloque F11-E4: Máquinas.

Bloque F11-E5: Despachos.

Bloque F11-E7: Otros activos.

12. Formulario 12: F12_Activos_G en curso.

Sector de aplicación: Gas.

Este Formulario contiene la base de datos de activos regulados que aún no estén puestos en servicio así como sus características técnicas.

Los bloques que lo componen y sus campos son los mismos que el Formulario 2 con la salvedad de que la información aportada en relación a las características técnicas será estimada.

En la asignación del centro de mantenimiento se deberá cumplimentar con 000 y la Referencia catastral «NA» si aún no se dispone de la parcela.

Los bloques a rellenar son los siguientes:

Bloque F12-GT1: Gasoductos.

Bloque F12-GT2: Posiciones.

Bloque F12-GT3: ERM/EM/ERP/ERC.

Bloque F12-GT4: Estaciones de Compresión.

Bloque F12-GT5: Centros de Mantenimiento o CMOCS.

Bloque F12-GT7: Otras instalaciones o servicios de transporte.

Bloque F12-R1: Tanques GNL.

Bloque F12-R2: Sistema de bombas secundarias.

Bloque F12-R3: Vaporizadores de agua de mar.

Bloque F12-R4: Vaporizadores de combustión sumergida.

Bloque F12-R5: Sistema de medida y odorización (ERM/EM).

Bloque F12-R6: Sistema de antorcha combustor.

Bloque F12-R7: Sistema de compresión boil-off para procesado interno.

Bloque F12-R8: Relicuador boil-off.

Bloque F12-R9: Sistema de compresión boil-off para emisión directa a la red.

Bloque F12-R10: Cargaderos de cisternas de GNL.

Bloque F12-R11: Interconexiones de GNL.

Bloque F12-R12: Interconexiones de GN.

Bloque F12-R13: Obra civil terrestre.

Bloque F12-R14: Muelles e instalaciones de descarga.

Bloque F12-R15: Sistema de suministro eléctrico.

Bloque F12-R16: Sistema de captación de agua.

Bloque F12-R17: Sistema de Gestión y Control.

Bloque F12-R18: Sistemas Auxiliares.

Bloque F12-R19: Cimentaciones y obra civil asociada a los tanques de almacenamiento de GNL.

Bloque F12-R20: Otras instalaciones o servicios.

Bloque F12-AS1: Instalaciones terrestres en superficie del AASS.

Bloque F12-AS2: Instalaciones Off-Shore en superficie del AASS.

Bloque F12-AS3: Instalaciones en subsuelo.

Bloque F12-AS4: Inversiones en investigación y exploración.

13. Formulario 13: F13_ Activos GTS/OS en curso.

Sector de aplicación: Electricidad y gas.

Este Formulario deberá ser cumplimentado por el OS y el GTS y contiene la base de datos de activos que aún no estén puestos en servicio y sus características técnicas.

Los bloques que lo componen y sus campos son los mismos que el Formulario 4 con la salvedad de que la información aportada en relación a las características técnicas será estimada.

Los bloques a rellenar son los siguientes:

Bloque F13-A1: Instalaciones y edificios.

Bloque F13-A2: Hardware informático y equipos telecomunicaciones.

Bloque F13-A3: Software.

Bloque F13-A4: Otras inversiones o servicios.

Bloque F13-A5: Instalaciones eléctricas asociadas al sistema de medidas del OS.

14. Formulario 14: F14_Geolocalización de activos en curso.

Sector de aplicación: Electricidad y gas.

En este Formulario se identifican las coordenadas estimadas de los activos que aún no disponen de acta de puesta en servicio. Los bloques que lo componen y sus campos son los mismos que el Formulario 6.

Los bloques a rellenar son los siguientes:

Bloque F14-AR1: Coordenadas de los Activos Punto.

Bloque F14-AR2: Coordenadas de los Activos Tramo.

Bloque F14-AR3: Coordenadas de los Terrenos.

Bloque F14-AR4: Correlación Activos-Terreno.

15. Formulario 15: F15_Disponibilidad y mantenimiento.

Sector de aplicación: Electricidad.

En este formulario se facilita información relativa a la disponibilidad de los activos titularidad del sujeto obligado así como relativa al uso de los mismos durante el ejercicio.

15.1 Bloque F15-D1: Disponibilidad y mantenimiento.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código CUAR. | Código CUAR del activo regulado sobre el que se declara. | C(33) | Declarado en Bloque F1-E1, F1-E3 y F1-E4 (estados S e Y). |
| N.º Averías. | Número de actuaciones realizadas sobre el activo debido a mantenimiento correctivo. | NP(3,0) |  |
| N.º Incidencias. | Número de actuaciones por causas de fuerza mayor o acciones de terceros realizadas sobre el activo debido a incidencias. | NP(3,0) |  |
| N.º Preventivo. | Número de actuaciones realizadas sobre el activo debido a mantenimientos preventivos y predictivos. | NP(3,0) |  |
| N.º modificaciones. | Número de actuaciones realizadas sobre el activo debido a modificaciones. | NP(3,0) |  |
| Indisponibilidad Averías. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas debido a mantenimiento correctivo. | NP(4,0) |  |
| Indisponibilidad Incidencias No programadas. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas por causas de fuerza mayor o acciones de terceros correctivo. | NP(4,0) |  |
| Indisponibilidad Incidencias programadas. | Número de horas de indisponibilidad del activo causado por actuaciones programadas ajenas al mantenimiento. | NP(4,0) |  |
| Indisponibilidad Preventivo. | Número de horas de indisponibilidad del activo debido a mantenimientos preventivos y predictivos. | NP(4,0) |  |
| Indisponibilidad Modificaciones no programadas. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas debido a circunstancias fortuitas previstas en las condiciones de diseño. | NP(4,0) |  |
| Indisponibilidad Modificaciones programadas. | Número de horas de indisponibilidad programadas por modificaciones/mejoras en el activo. | NP(4,0) |  |

15.2 Bloque F15-U1: Datos de Uso.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas validación |
| --- | --- | --- | --- |
| Código CUAR. | Código CUAR del activo regulado sobre el que se declara. | C(33) | Para todos los activos declarado en los Bloques F1-E1 / E2 / E3 y E4. |
| Parámetro de uso 1. | Indicar el parámetro de uso 1. Podrá ser el de la Tabla 60, u otro que el sujeto obligado utilice para definir sus programas de mantenimiento preventivo en función del uso. | C(≤255) |  |
| Parámetro de uso 2. | Indicar el parámetro de uso 2. Podrá ser el de la Tabla 60, u otro que el sujeto obligado utilice para definir sus programas de mantenimiento preventivo en función del uso. | C(≤255) |  |
| Parámetro de uso 3. | Indicar el parámetro de uso 3. Podrá ser el de la Tabla 60, u otro que el sujeto obligado utilice para definir sus programas de mantenimiento preventivo en función del uso. | C(≤255) |  |

16. Formulario 16: F16_Disponibilidad y mantenimiento.

Sector de aplicación: Gas.

En este formulario se facilita información relativa a la disponibilidad de los activos titularidad del sujeto obligado así como relativa al uso de los mismos durante el ejercicio.

16.1 Bloque F16-D1: Disponibilidad y mantenimiento.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| Código CUAR. | Código CUAR del activo regulado sobre el que se declara. | C(33) | Declarado en Bloque F2, en servicio, excepto F2-GT6, F2- R21 y F2-AS5. |
| N.º Averías. | Número de actuaciones realizadas sobre el activo debido a mantenimiento correctivo. | NP(3,0) |  |
| N.º Incidencias. | Número de actuaciones por causas de fuerza mayor o acciones de terceros realizadas sobre el activo debido a incidencias. | NP(3,0) |  |
| N.º Preventivo. | Número de actuaciones realizadas sobre el activo debido a mantenimientos preventivos y predictivos. | NP(3,0) |  |
| N.º modificaciones. | Número de actuaciones realizadas sobre el activo debido a modificaciones. | NP(3,0) |  |
| Indisponibilidad Averías. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas debido a mantenimiento correctivo. | NP(4,0) |  |
| Indisponibilidad Incidencias No programadas. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas por causas de fuerza mayor o acciones de terceros correctivo. | NP(4,0) |  |
| Indisponibilidad Incidencias programadas. | Número de horas de indisponibilidad del activo causado por actuaciones programadas ajenas al mantenimiento. | NP(4,0) |  |
| Indisponibilidad Preventivo. | Número de horas de indisponibilidad del activo debido a mantenimientos preventivos y predictivos. | NP(4,0) |  |
| Indisponibilidad Modificaciones no programadas. | Número de horas de indisponibilidad del activo causado por actuaciones no programadas debido a circunstancias previstas en las condiciones de diseño. | NP(4,0) |  |
| Indisponibilidad Modificaciones programadas. | Número de horas de indisponibilidad programadas por modificaciones/mejoras en el activo. | NP(4,0) |  |

16.2 Bloque F16-U1: Datos de Uso.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas validación |
| --- | --- | --- | --- |
| Código OFC. | Código OFC sobre el que se declara. | C(33) | Solo para los tipos de OFC definidos en la Tabla 61. |
| Centro de mantenimiento. | Centro de mantenimiento al que están asignados los activos del OFC. | C(9) | Existencia en la Tabla 6. |
| Parámetro de uso 1. | Indicar el parámetro de uso 1 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 2. | Indicar el parámetro de uso 2 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 3. | Indicar el parámetro de uso 3 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 4. | Indicar el parámetro de uso 4 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 5. | Indicar el parámetro de uso 5 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 6. | Indicar el parámetro de uso 6 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 7. | Indicar el parámetro de uso 7 según la Tabla 61. | NP(9,0) |  |
| Parámetro de uso 8. | Indicar el parámetro de uso 8 según la Tabla 61. | NP(9,0) |  |

17 Formulario 17: Activos en curso antes de la primera declaración.

Sector de aplicación: Electricidad y Gas Natural.

Este formulario deberá ser cumplimentado por los sujetos obligados únicamente el primer ejercicio del Sistema IRC. Contiene los costes acumulados descontados los ingresos incorporables correspondientes en los diferentes OFC de inversión a fecha de 31 de diciembre del ejercicio anterior a la primera declaración.

17.1 Bloque F17-AC1: Declaración de costes a CUAR iniciados antes de la primera declaración.

Descripción de campos:

| Campo | Descripción | Tipo dato | Reglas de validación |
| --- | --- | --- | --- |
| CUAR. | Código CUAR del activo regulado del que se declaran los costes. | C(33) | Coherencia CUAR. |
| Importe. | Importe de los costes declarados acumulados a 31 de diciembre del ejercicio anterior a la primera declaración. | NP(10,0) |  |
| Concepto de Coste. | Concepto de coste del que se reparten los costes en los nuevos CUAR. | C(≤13) | Contenido en las Tablas 23-25 para electricidad o 28 para gas. |
