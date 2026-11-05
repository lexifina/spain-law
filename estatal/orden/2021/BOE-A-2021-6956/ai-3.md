## ANEXO III

## Especificaciones técnicas de los precios ordinarios del billete

| N.º orden | Denominación del campo | Tamaño del campo | Contenido del campo |
| --- | --- | --- | --- |
| 1 | Código de tarifa o tipo de billete | 5 | Código alfanumérico de cinco caracteres, que identifica el tipo de billete que emite la empresa ferroviaria. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 2 | Empresa ferroviaria | 3 | Código alfanumérico de tres caracteres, que identifica a la empresa ferroviaria que realiza el transporte. Caracteres permitidos: A-Z, 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 3 | Origen | 6 | El Código de Identificación de Localidad INE de seis números. Caracteres permitidos: 0-9. |
| 4 | Destino | 6 | El Código de Identificación de Localidad INE de seis números. Caracteres permitidos: 0-9. |
| 5 | Precio ordinario o máximo sin IVA | 7 | Importe del precio ordinario o máximo del billete sin IVA expresado en céntimos de euros, sin separador decimal. Caracteres permitidos: 0-9. Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). El campo se rellenará con ceros a la izquierda si el importe tiene menos de seis dígitos. |
| 6 | Fecha efectividad desde | 10 | Fecha en el que comienza la validez del precio del billete en el formato DD/MM/AAAA en la que: DD es el número de día del mes. Si es inferior a 10 se añadirá un cero a la izquierda. MM es el número del mes. Si es inferior a 10 se añadirá un cero a la izquierda. AAAA es el año con cuatro dígitos. Caracteres permitidos: 0-9 y «/» (ASCII 47 decimal). Nota: No se aceptará el carácter «espacio» (ASCII 32 decimal). |
| 7 | Fecha efectividad hasta | 10 | Último día en el que tiene validez el precio del billete en el formato DD/MM/AAAA en la que DD, MM, AAAA se conformarán a lo establecido para el campo 6 del fichero de precios ordinarios del billete. |
| 8 | Estación Origen | 5 | Código numérico de Identificación de la estación de origen, utilizado por el Administrador de la Infraestructura. Caracteres permitidos: 0-9, A-Z. |
| 9 | Estación Destino | 5 | Código numérico de Identificación de la estación de origen, utilizado por el Administrador de la Infraestructura. Caracteres permitidos: 0-9, A-Z. |

El campo código del billete es de utilidad a la propia empresa ferroviaria para identificar o localizar los billetes mediante código interno. Este dato será incluido en todos los ficheros de billetes.

Los campos numéricos irán ajustados a la derecha y rellenos con ceros. Los campos alfanuméricos (son únicamente válidos los caracteres ASCII 32 a 255) irán ajustados a la izquierda.

> Se modifica por el art. único.4 de la Orden TMA/821/2023, de 10 de julio. Ref. BOE-A-2023-16813
