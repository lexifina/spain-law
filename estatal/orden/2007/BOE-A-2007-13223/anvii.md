## ANEXO VII

## GENERACIÓN, CONSOLIDACIÓN Y ANULACIÓN NRC

1. Generación del NRC.

1.1 De autoliquidaciones:

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| Código de Modelo. | Entrada. | Alfanumérico (3). |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| NIF del obligado. | Entrada. | Alfanumérico (9). |
| Ejercicio. | Entrada. | Numérico (4). |
| Periodo. | Entrada. | Alfanumérico (2). |
| Importe. | Entrada. | Numérico. |
| NRC. | Salida. | Alfanumérico (22). |
| Fecha y hora de generación. | Salida. | Fecha y hora. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

1.2 De predeclaraciones:

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| N.º Justificante. | Entrada. | Alfanumérico (13). |
| NIF del obligado. | Entrada. | Alfanumérico (9). |
| Ejercicio. | Entrada. | Numérico (4). |
| Periodo. | Entrada. | Alfanumérico (2). |
| Importe. | Entrada. | Numérico (positivo). |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| Fecha y hora de confirmación de la predeclaración/borrador. | Entrada. | Fecha y hora. |
| NRC. | Salida. | Alfanumérico (22). |
| Fecha de generación. | Salida. | Fecha. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

1.3 De documentos de ingreso (modelo 100):

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| Código de modelo. | Entrada. | Alfanumérico (3). Valor constante «100». |
| Ejercicio. | Entrada. | Numérico (4). |
| Importe. | Entrada. | Numérico. |
| Periodo. | Entrada. | Alfanumérico (2). |
| NIF del obligado. | Entrada. | Alfanumérico (9). |
| N.º Justificante. | Entrada. | Alfanumérico (13). |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| NRC. | Salida. | Alfanumérico (22). |
| Fecha de generación. | Salida. | Fecha. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

1.4 De liquidaciones practicadas por la Administración:

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| Código de Modelo. | Entrada. | Alfanumérico (3). |
| N.º Justificante. | Entrada. | Alfanumérico (13). |
| NIF del obligado. | Entrada. | Alfanumérico (9). |
| Importe. | Entrada. | Numérico. |
| Fecha de ingreso. | Entrada. | Fecha. |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| NRC. | Salida. | Alfanumérico (22). |
| Fecha y hora de generación. | Salida. | Fecha y hora. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

1.5 De tasas.

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| N.º Justificante. | Entrada. | Alfanumérico (13). |
| NIF del obligado. | Entrada. | Alfanumérico (9). |
| Importe. | Entrada. | Numérico. |
| Fecha y hora del ingreso. | Entrada. | Fecha y hora. |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| NRC. | Salida. | Alfanumérico (22). |
| Fecha y hora de generación. | Salida. | Fecha y hora. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

2. Consolidación del NRC.

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| NRC a consolidar. | Entrada. | Alfanumérico (22). |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| Fecha y hora del ingreso. | Entrada. | Fecha y hora. |
| Fecha y hora de consolidación. | Salida. | Fecha y hora. |
| Estado del NRC. | Salida. | Alfanumérico. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

3. Anulación del NRC.

| Parámetro | Tipo | Tipo Formato |
| --- | --- | --- |
| NRC a anular. | Entrada. | Alfanumérico (22). |
| Código de la entidad colaboradora. | Entrada. | Alfanumérico (4). |
| Estado del NRC. | Salida. | Alfanumérico. |
| Fecha y hora de anulación. | Salida. | Fecha y hora. |
| Código de respuesta. | Salida. | Numérico. |
| Descripción respuesta. | Salida. | Alfanumérico. |

> Se modifica por el art. 1.13 de la Orden HFP/915/2021, de 1 de septiembre. Ref. BOE-A-2021-14453#ap
