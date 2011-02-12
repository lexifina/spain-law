## ANEXO I

## Registro de datos de productores de leche y productos lácteos de ovino

| Descripción | Campo | Posición | Longitud | Definición | Formato | Rango | Nulo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Comunidad Autónoma. | 1 | 1-2 | 2 | Código de la Comunidad Autónoma remitente. | FA2 | Ver tabla códigos CCAA. | N |
| Empresa. | 2 | 3-42 | 40 | Nombre o razón social del comprador. | FA1 |  | N |
| Letra del DNI. | 3 | 43-43 | 1 | Letra DNI del comprador. | FA2 |  | S |
| Número del DNI/NIF. | 4 | 44-51 | 8 | N.º DNI/NIF del comprador. | FA2 |  | N |
| Letra del NIF. | 5 | 52-52 | 1 | Letra NIF del comprador. | FA1 |  | S |
| Apellidos y nombre. | 6 | 53-92 | 40 | Apellidos y nombre o razón social del productor. | FA1 |  | N |
| Letra DNI. | 7 | 93-93 | 1 | Letra DNI del productor. | FA2 |  | S |
| Número DNI/NIF. | 8 | 94-101 | 8 | Nº DNI/NIF del productor. | FA2 |  | N |
| Letra NIF. | 9 | 102-102 | 1 | Letra NIF del productor. | FA1 |  | S |

Explicación de los de campos:

FA1: campo alfanumérico, ajustado a al izquierda y completado en blanco a la derecha si fuera necesario.

FA2: campo alfanumérico, ajustado a la derecha y completado con ceros a la izquierda si fuese necesario.

N: el campo es obligatorio.

S: el campo no es obligatorio si ya se ha completado la información en otro campo.
