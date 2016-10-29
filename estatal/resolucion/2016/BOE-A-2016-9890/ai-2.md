## ANEXO II

![imagen](https://www.boe.es/datos/imagenes/disp/2016/261/09890_7234.png)

Detalle de los datos a incluir para generar el NRC:

Para generar el NRC es imprescindible que todos estos datos a incluir en los procedimientos de cifrado estén generados en EBCDIC.

MMM: Código de modelo para constitución de depósitos (960).

BBBB: Cuatro primeros dígitos del Código asignado por el Banco de España a la entidad de crédito.

NNNNN: Número secuencial correlativo, comenzando por 00000. Caso de llegar a 99999, se comenzaría por 00000.

D: Dígito de control del «MMMBBBBNNNNN», generado con el mismo algoritmo utilizado actualmente por las entidades colaboradoras de la Agencia Tributaria para el número de justificante de las autoliquidaciones.

C: Carácter de control complementario, generado aplicando un algoritmo facilitado a las entidades colaboradoras de la Agencia Tributaria.

Sólo se utilizará para el NRC.

MMMBBBBNNNNNDC: Conforman el Número de Referencia que formará parte del NRC.

NIF: NIF del titular del depósito.

Fecha del depósito: Año, mes y día de la constitución del depósito.

Importe: Se indicará la cifra expresada en céntimos de euro y ajustada a la derecha, rellena con ceros a la izquierda, hasta completar las trece posiciones.

Reservado: Se rellenarán con ceros las cuatro posiciones.

Segundo. Registros en la pasarela de depósitos de subastas de la Agencia Tributaria.

1. Registro de orden de cargo

| N.º | POS. | LONG. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 2 | 10 | 8 | N | Fecha AAAAMMDD. |
| 3 | 18 | 10 | N | Hora HHMMSSSSSS. |
| 4 | 28 | 3 | An | Tipo de operación de alta. 003 Constitución de Depósitos. |
| 5 | 31 | 2 | An | Alta 01, Consulta 02. |
| 6 | 33 | 3 | N | Concepto o modelo 960. |
| 7 | 36 | 4 | N | Ceros. |
| 8 | 40 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 9 | 49 | 5 | N | Ceros. |
| 10 | 54 | 13 | N | Importe del depósito. (Ajustado a la derecha y relleno de ceros a la izquierda). |
| 11 | 67 | 16 | N | Ceros. |
| 12 | 83 | 20 | N | Reservado. |
| 13 | 103 | 8 | N | AAAAMMDD fecha constitución depósito. |
| 14 | 111 | 9 | An | NIF del representante 1 o blancos. |
| 15 | 120 | 9 | An | NIF del representante 2 o blancos. |
| 16 | 129 | 16 | An | MAC de 8 con salida en hexadecimal cifrado. |
| 17 | 145 | 4 | An | Letras de etiqueta del titular del depósito en personas físicas. |
| 18 | 149 | 40 | An | Apellidos y nombre o razón social del titular del depósito. |
| 19 | 189 | 40 | An | Apellidos y nombre del representante 1 o blancos. |
| 20 | 229 | 40 | An | Apellidos y nombre del representante 2 o blancos. |
| 21 | 269 | 32 | An | Blancos. |
| 22 | 301 | 34 | An | Código IBAN. |
| 23 | 335 | 6 | An | Reservado para nuevos datos que intervengan en el cálculo del MAC. |
| 24 | 341 | 100 | An | Reservado. |

El MAC de 8 será generado a partir del contenido de las 128 primeras posiciones junto con el contenido de las posiciones 301 a 340.

Existe la posibilidad de que los datos de los campos 4 en adelante se transmitan cifrados, además del cifrado que realiza el SSL. La clave y sistema de este cifrado se acordará entre la Entidad y la Agencia Tributaria.

2. Registro de comunicación del NRC

| N.º | POS. | LONG. | Tipo | Descripción |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | An | Tipo de operación. 003 Constitución de Depósitos. |
| 2 | 4 | 2 | An | Alta 01, Consulta 02. |
| 3 | 6 | 3 | N | Concepto o modelo 960. |
| 4 | 9 | 6 | N | Ceros. |
| 5 | 15 | 9 | An | NIF del titular del depósito (XNNNNNNNX). |
| 6 | 24 | 4 | An | Letras de etiqueta en personas físicas. |
| 7 | 28 | 5 | N | Ceros. |
| 8 | 33 | 13 | N | Importe del depósito (Ajustado a la derecha y relleno de ceros a la izquierda). |
| 9 | 46 | 12 | N | Ceros. |
| 10 | 58 | 20 | N | Reservado. |
| 11 | 78 | 12 | N | Ceros. |
| 12 | 90 | 8 | N | Fecha de la operación (AAAAMMDD). |
| 13 | 98 | 22 | An | Número de referencia completo. (MMMBBBBNNNNNDCXXXXXXXX). |
| 14 | 120 | 2 | An | Código de retorno. |
| 15 | 122 | 1 | N | Cero. |
| 16 | 123 | 34 | An | Código IBAN. |
| 17 | 157 | 54 | An | Reservado para posibles ampliaciones. |
| 18 | 211 | 189 | An | Libre. |
| 19 | 400 | 50 | An | Reservado para posibles ampliaciones. |
