## SEGUNDO. Nombre de los ficheros.

## Grupo 1

El fichero de «Información adicional a la Memoria» tendrá como nombre el código de la Administración General del Estado como entidad que lo remite, el tipo de información y una extensión en formato MS-DOS, de acuerdo con el siguiente detalle:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de la Entidad Contable. | Código de la Administración General del Estado. | 1 | 5 | Num |
| Tipo de Información. | Valor fijo «IAM». | 6 | 3 | Alf |
| Extensión. | Identificador del procesador de textos empleado en su generación, con un punto delante. Por ejemplo: «.doc». | 9 | 3 | Alf |

Con la extensión se pretende reconocer el procesador de textos utilizado para la edición de la «Información adicional a la Memoria». Se podrán utilizar como procesadores de textos, a estos efectos, todas aquellas versiones cuya utilización sea generalizada y previamente autorizada por la Intervención General de la Administración del Estado.

Grupo 2

Los ficheros de la «Información sobre el Endeudamiento», «Información sobre las operaciones de Intercambio Financiero», «Información sobre operaciones de compraventa dobles sobre valores de la Deuda del Estado», «Información sobre Créditos» e «Información sobre Inversiones Financieras en Patrimonio», tendrán como nombre el código de la Administración General del Estado como entidad que lo remite, el tipo de información y una extensión en formato MS-DOS, de acuerdo con el siguiente detalle:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de la Entidad Contable. | Código de la Administración General del Estado. | 1 | 5 | Num |
| Tipo de Información. | Tipo de información | 6 | 3 | Alf |
| Extensión. | Identificador de la hoja de cálculo empleada en su generación, con un punto delante. Por ejemplo: «.xls». | 9 | 3 | Alf |

Con la extensión se pretende reconocer la hoja de cálculo utilizada para la edición de este grupo de información. Se podrá utilizar como hoja de cálculo, a estos efectos, todas aquellas versiones cuya utilización sea generalizada y previamente autorizada por la Intervención General de la Administración del Estado.

Los tipos de Información que se enviarán en este grupo son los que se detallan a continuación:

| TIPO DE INFORMACIÓN | DESCRIPCIÓN |
| --- | --- |
|  | INFORMACIÓN SOBRE ENDEUDAMIENTO |
|  | Situación y movimiento de la Deuda del Estado: |
| D01 | Situación de la Deuda del Estado. Euros |
| D02 | Creación de la Deuda del Estado. Euros |
| D03 | Disminuciones de la Deuda del Estado. Euros |
| D04 | Situación de la Deuda del Estado. Moneda distinta de euro |
| D05 | Creación de la Deuda del Estado. Moneda distinta de euro |
| D06 | Disminuciones de la Deuda del Estado. Moneda distinta de euro |
|  | Situación de Deudas amortizadas: |
| D07 | Deuda amortizada pendiente de reembolso. Euros y moneda distinta de euro |
| D08 | Amortizaciones pendientes de aplicar al Presupuesto |
|  | Intereses: |
| D09 | Intereses explicitos de la Deuda del Estado. Euros |
| D10 | Intereses explícitos de la Deuda del Estado. Moneda distinta de euro |
| D11 | Rendimientos implícitos y diferencias negativas entre los valores de reembolso y emisión de la Deuda del Estado. Euros |
| D12 | Rendimientos implícitos y diferencias negativas entre los valores de reembolso y emisión de la Deuda del Estado. Moneda distinta de euro |
| D13 | Diferencias de cambio de la Deuda del Estado |
| D14 | Coste total de la Deuda del Estado |
|  | Situación de los intereses vencidos: |
| D15 | Intereses pendientes de pago. Euros y moneda distinta de euro |
| D16 | Intereses pendientes de aplicar a Presupuesto |
|  | Letras del Tesoro y Papel comercial: |
| D17 | Letras del Tesoro |
| D18 | Situación y movimiento del papel comercial en moneda distinta de euro |
| D19 | Rendimientos implícitos del papel comercial en moneda distinta de euro |
|  | Avales: |
| D20 | Avales |
|  | INFORMACIÓN SOBRE LAS OPERACIONES DE INTERCAMBIO FINANCIERO: |
|  | Información sobre las operaciones de Intercambio Financiero de divisas: |
| I01 | Descripción y características de las operaciones de intercambio financiero de divisas |
| I02 | Situación de las operaciones de intercambio financiero de divisas |
| I03 | Intereses de las operaciones de intercambio financiero de divisas |
| I04 | Resultado de las operaciones de intercambio financiero de divisas |
| I05 | Valor de mercado de las operaciones de intercambio financiero de divisas y garantías recibidas |
|  | Información sobre las operaciones de Intercambio Financiero de intereses: |
| I06 | Descripción y características de las operaciones de intercambio financiero de intereses |
| I07 | Situación de las operaciones de intercambio financiero de intereses |
| I08 | Resulfado de las operaciones de intercambio financiero de intereses |
|  | INFORMACIÓN SOBRE OPERACIONES DE COMPRAVENTA DOBLES SOBRE VALORES DE LA DEUDA DEL ESTADO: |
| J01 | Información sobre operaciones de compraventa dobles sobre valores de la Deuda del Estado |
|  | INFORMACIÓN SOBRE CRÉDITOS: |
| C01 | Información sobre Créditos |
|  | INFORMACIÓN SOBRE INVERSIONES FINANCIERAS EN PATRIMONIO: |
| C02 | Información sobre Inversiones Financieras en Patrimonio |

Grupo 3

El resto de ficheros, con formato definido, tendrán como nombre el código de la Administración General del Estado como entidad que lo remite y el tipo de información en formato MS-DOS, de acuerdo con el siguiente detalle:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de la Entidad Contable. | Código de la Administración General del Estado. | 1 | 5 | Num |
| Tipo de Información. | Tipo de información | 6 | 3 | Alf |

Los nombres de estos ficheros no llevaran extensión que condicione la utilización de un editor concreto.

Los tipos de Información que se enviarán en este grupo, son los que se detallan a continuación:

| TIPO DE INFORMACIÓN | DESCRIPCIÓN |
| --- | --- |
| A01 | Presupuesto de gastos. Ejercicio corriente. |
| A02 | Proyectos de inversión. |
| A03 | Contratación administrativa: procedimientos y situación. |
| A04 | Contratación administrativa: adjudicatarios. |
| A05 | Transferencias de capital concedidas. |
| A06 | Subvenciones de capital concedidas. |
| A07 | Transferencias corrientes concedidas. |
| A08 | Subvenciones corrientes concedidas. |
| A09 | Acreedores por operaciones pendientes de aplicar a presupuesto. |
| A10 | Acreedores por periodificación de gastos presupuestarios. |
| A11 | Anticipos de tesorería. |
| A12 | Presupuesto de gastos. Ejercicios cerrados. |
| A13 | Gastos plurianuales. |
| A14 | Presupuesto de ingresos. Ejercicio corriente. Previsiones. |
| A15 | Presupuesto de ingresos. Ejercicio corriente. Ejecución. |
| A16 | Presupuesto de ingresos. Ejercicios cerrados. |
| A17 | Derechos presupuestarios pendientes de cobro según su grado de exigibilidad (presupuesto corriente). |
| A18 | Derechos presupuestarios pendientes de cobro según su grado de exigibilidad (presupuestos cerrados). |
| A19 | Información sobre el inmovilizado material. |
| A20 | Información sobre inversiones financieras en capital y valores de renta fija. |
| A21 | Operaciones no presupuestarias de tesorería. |
| A22 | Operaciones de la Caja General de Depósitos por garantías y depósitos en efectivo. |
| A23 | Valores recibidos en depósito. |
| A24 | Operaciones de la Caja General de Depósitos por otras garantías. |
| A25 | Operaciones por administración de recursos por cuenta de otros entes públicos: – Gestión de los recursos administrados. – Devoluciones de ingresos. – Obligaciones derivadas de la gestión de los recursos administrados por cuenta de otros entes públicos. |
| A26 | Operaciones por administración de recursos por cuenta de otros entes públicos. – Cuentas corrientes en efectivo. |
| A27 | Derechos presupuestarios pendientes de cobro según su grado de exigibilidad de recursos recaudados por cuenta de otros entes públicos. |
| A28 | Cuentas P.G.C.P. (antes de asientos de regularización). |
| A29 | Cuentas P.G.C.P. (antes del asiento de cierre). |
| A30 | Cuentas de los grupos 6 y 7 del ejercicio anterior (antes del asiento de regularización). |
| A31 | Balance de situación. |
| A32 | Cuenta del resultado económico-patrimonial. |
| A33 | Resultado presupuestado. |
| A34 | Remanente de tesorería. |
| A35 | Estado de tesorería. |
| A36 | Variación de resulfados presupuestarios de ejercicios anteriores. |
| T01 | Tabla de cuentas del P.G.C.P. |
| T02 | Tabla de clasificación económica de ingresos. |
| T03 | Tabla de clasificación orgánica de gastos. |
| T04 | Tabla de clasificación funcional de gastos. |
| T05 | Tabla de clasificación económica de gastos. |
| T06 | Tabla de conceptos no presupuestarios. |
| T07 | Tabla de relación conceptos contables de ingresos-Clasificación económica de ingresos. |
| T08 | Tabla de conceptos contables de ingresos. |
| T09 | Tabla de conceptos de recursos locales. |
| T10 | Tabla de localización de bienes de inmovilizado material. |
| T11 | Tabla de códigos de entidades en las que se ha invertido. |
| T12 | Tabla de códigos de orgánica-1. |
