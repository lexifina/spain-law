## CUARTO. Características generales de los campos. (Grupo 3)

a) Campos alfanuméricos.

Su contenido se presentará justificado a la izquierda y con caracteres espacio a la derecha hasta completar la longitud del campo, admitiéndose tanto mayúsculas como minúsculas así como vocales acentuadas. Si el campo no tuviera contenido se rellenarán con espacios todas sus posiciones.

b) Campos numéricos.

Su contenido se presentará sin empaquetar y sin signo, justificado a la derecha, con ceros a la izquierda hasta completar la longitud del campo. Si el campo no tuviera contenido, se rellenarán con ceros todas sus posiciones.

c) Campos de importes.

Los importes incluidos en los registros se ajustarán al siguiente formato:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Signo. | Signo del importe. Contendrá «+» si es positivo o cero y «-» si es negativo. | 1 | 1 | Alf |
| Importe. Parte entera. | Parte entera del importe, sin separadores de miles. | 2 | 14 | Num |
| Importe. Parte decimal. | Parte decimal del importe, sin separador decimal. | 16 | 2 | Num |

d) Campos de fecha.

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Año | Año | 1 | 4 | Num |
| Mes | Mes | 5 | 2 | Num |
| Día | Día | 7 | 2 | Num |
