## QUINTO. Estructura de campos usuales.

a) Código de aplicación presupuestaria de gastos.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Ejercicio presupuestario. | Ejercicio presupuestario. | 1 | 4 | Num |
| Código de Sección. | Código de Sección presupuestaria, contenido en el fichero de Tabla de clasificación orgánica de gastos, tipo de registro «T03». | 5 | 2 | Num |
| Código de servicio. | Código de servicio presupuestario, contenido en el fichero de Tabla de clasificación orgánica de gastos, tipo de registro «T03» (en caso que se utilice, y en caso contrario, espacios). | 7 | 2 | Alf |
| Código de Orgánica 2. | Código de Orgánica 2 (en caso que se utilice, y en caso contrario, espacios). | 9 | 2 | Alf |
| Código de Programa. | Código de Programa presupuestario contenido en el fichero de Tabla de clasificación funcional de gastos, tipo de registro «T04». | 11 | 4 | Alf |
| Código de Subprograma. | Código de Subprograma contenido en el fichero de Tabla de clasificación funcional de gastos, tipo de registro «T04» (en caso que se utilice, y en caso contrario, espacios). | 15 | 1 | Alf |
| Código de Elemento de programa. | Código de Elemento de programa (en caso que se utilice, y en caso contrario, espacios). | 16 | 2 | Alf |
| Código de Concepto. | Código de Concepto Presupuestario contenido en el fichero de Tabla de clasificación económica de gastos, tipo de registro «T05». | 18 | 3 | Num |
| Código de Subconcepto. | Código de Subconcepto contenido en el fichero de Tabla de clasificación económica de gastos, tipo de registro «T05». (en caso que se utilice, y en caso contrario, espacios). | 21 | 2 | Alf |
| Código de Partida. | Código de Partida. (en caso que se utilice, y en caso contrario, espacios). | 23 | 2 | Alf |

b) Código de aplicación presupuestaria de ingresos.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Concepto. | Código de Concepto, contenido en el fichero de Tabla de clasificación económica de ingresos, tipo de registro «T02». | 1 | 3 | Num |
| Código de Subconcepto. | Código de Subconcepto, contenido en el fichero de Tabla de clasificación económica de ingresos, tipo de registro «T02». (en caso que se utilice, y en caso contrario, espacios). | 4 | 2 | Alf |

c) Clave de concepto contable de ingresos.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Sección | Código de Sección (en caso que se utilice, y en caso contrario, espacios). | 1 | 2 | Alf |
| Código de Orgánica-1 | Código de Orgánica-1 contenido en el fichero de Tabla de códigos de orgánica-1, tipo de registro «T12» | 3 | 2 | Num |
| Código de Orgánica-2 | Código de Orgánica-2 (en caso que se utilice, y en caso contrario, espacios). | 5 | 2 | Alf |
| Código de Concepto. | Código de Concepto contable de ingresos, contenido en el fichero de Tabla de conceptos contables de ingresos, tipo de registro «T08». | 7 | 6 | Num |

d) Código de aplicación no presupuestaria.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Orgánica-1 | Código de Orgánica-1 contenido en el fichero de Tabla de códigos de orgánica-1, tipo de registro «T12» | 1 | 2 | Num |
| Código de Orgánica-2 | Código de Orgánica-2 (en caso que se utilice, y en caso contrario, espacios). | 3 | 2 | Alf |
| Código de Concepto. | Código de Concepto de operación no presupuestaria, contenido en el fichero de Tabla de conceptos no presupuestarios, tipo de registro «T06». | 5 | 6 | Num |

e) Clave de concepto de recursos locales.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Sección | Código de sección (en caso que se utilice, y en caso contrario, espacios). | 1 | 2 | Alf |
| Código de Orgánica-1 | Código de Orgánica-1 contenido en el fichero de Tabla de códigos de orgánica-1, tipo de registro «T12» | 3 | 2 | Num |
| Código de Orgánica-2 | Código de Orgánica-2 (en caso que se utilice, y en caso contrario, espacios). | 5 | 2 | Alf |
| Código de Concepto. | Código de Concepto de recursos locales, contenido en el fichero de Tabla de conceptos de recursos locales, tipo de registro «T09». | 7 | 6 | Num |

f) Clave de cuenta del P.G.C.P.

Se solicita al siguiente nivel de agregación:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Cuenta. | Código de Cuenta, contenida en el fichero de Tabla de cuentas del P.G.C.P., tipo de registro «T01». | 1 | 6 | Num |
| Código de orgánica-1 | Código de Orgánica-1 contenido en el fichero de Tabla de códigos de orgánica-1, tipo de registro «T12»). | 7 | 2 | Alf |

g) Código de Adjudicatario.

Se solicita con la siguiente estructura:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de País. | Indicador del país del adjudicatario, codificado de acuerdo con el apartado séptimo «Contenido de tablas» de este anexo. | 1 | 2 | Alf |
| NIF / CIF. | NIF o CIF del adjudicatario. | 3 | 12 | Alf |

h) Código de localización del bien de inmovilizado material

Se solicita con la siguiente estructura:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Código de Provincia | Código de Provincia contenido en el fichero de tablas de localización, tipo de registro «T10». | 1 | 2 | Num |
| Código de Municipio. | Código de Municipio contenido en el fichero de tablas de localización, tipo de registro «T10». | 3 | 3 | Num |
| Código de Localidad. | Código de localidad contenido en el fichero de tablas de localización, tipo de registro «T10». | 6 | 2 | Num |

i) Código de inversión financiera

Se solicita con la siguiente estructura:

| NOMBRE | CONTENIDO Y DESCRIPCIÓN | POS | LON | TIP |
| --- | --- | --- | --- | --- |
| Clave de cuenta de la inversión financiera | Clave de cuenta del P.G.C.P. (según apartado «f», anterior) | 1 | 8 | Alf |
| Código de entidad en la que se ha invertido | Código de entidad, contenido en el fichero de tabla de códigos de entidades en las que se ha invertido, tipo de registro «T11». | 9 | 4 | Alf |

> Redactado el apartado a) conforme a la corrección de errores publicada en BOE núm. 281, de 23 de noviembre de 2002. Ref. BOE-A-2002-22810.
