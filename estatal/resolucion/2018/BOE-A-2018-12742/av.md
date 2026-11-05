## ANEXO V

## Diseño de registro del fichero FppmmmIA.aaa, con el resultado de la estimación/desestimación de alegaciones

El diseño de registro del fichero FppmmmIA.aaa tendrá la misma estructura y contenido que el fichero de alegaciones, AppmmmAI.aaa, con tres campos finales adicionales:

– RESALEGINI (A2).

– RESALEG (A2).

– OBSVINE (A200).

Donde se incluirán las claves y observaciones con el resultado de la estimación/desestimación de las alegaciones, incluyendo en RESALEGINI el resultado inicial tras el tratamiento automático del INE y en RESALEG el resultado final coincidente con RESALEGINI, salvo cuando haya sido preciso revisión manual.

Valores posibles RESALEGINI:

| RESALEG-INI | Descripción |
| --- | --- |
| NR | No en Reparos1. (Desestimada automáticamente). |
| AI | Alegación inconsistente2. (Desestimada automáticamente). |
| DM | Depuración manual. (Pasa a tratamiento manual). |
| DU | Alegación duplicada. |
| AC | Aceptada. |
| RA | Caso raro. (Pasa a tratamiento manual). |
| T2 | Tratamiento manual de alegaciones que van a carga. |
| T1 | Tratamiento manual de alegaciones que no van a carga. |
| GB | Genera baja. (Desestimada automáticamente). |
| MA | Alegación en tabla de manuales. (Tratamiento mixto posterior (automático y manual)). |
| NV | No válida3. (Desestimada automáticamente). |
| BA | Baja. (Sólo para alegaciones de baja. Implica baja aceptada). |
| DS | Desestimada. (Desestimada automáticamente). |
| N.º de error | Invalidante o de gestión. Generado por la alegación al intentar la carga en la base. |
| 1 Se ha realizado un contraste entre el registro de alegaciones y el devuelto en el fichero de Reparos. Cualquier cambio en alguno de los campos implica que no se identifiquen, por tanto, con esta clave pueden aparecer alegaciones devueltas en Reparos, para las que se habrá modificado algún campo no incluido en las salvedades previstas. 2 Por ejemplo si se alega con un ANA72 para un nacimiento NO devuelto en Reparos con error 72. 3 Cuando se ha utilizado una CALEG distinta a las contempladas en esta Resolución o en la relación actualizada de IDA-Padrón. |

Valores posibles RESALEG:

| RESALEG | Descripción |
| --- | --- |
| NR | No en Reparos |
| AI | Alegación inconsistente |
| DU | Alegación duplicada |
| AC | Aceptada |
| GB | Genera baja |
| NV | No válida |
| BA | Baja |
| DS | Desestimada |
| N.º de error | Invalidante o de gestión. Generado por la alegación al intentar la carga en la base |

Combinaciones posibles de valores de RESALEG-INI RESALEG que pueden encontrarse en los ficheros FppmmmIA.aaa:

| RESALEG-INI | RESALEG | Interpretación |
| --- | --- | --- |
| NR | NR | No en Reparos. El Ayto. ha enviado una Alegación que no corresponde al reparo enviado. |
| AI | AI | El Ayto. ha realizado una alegación inconsistente con el reparo devuelto. |
| DU | DU | Alegación duplicada |
| DS | DS | Existía par R-S enlazado en el fichero de reparos y el Ayto. sólo ha alegado al de la R. |
| AC | AC | Alegación aceptada. |
| DM | DS | Alegación revisada manualmente y desestimada porque no procede. |
| AC | Alegación revisada manualmente y estimada. |
| NV | NV | Alegación con CALEG no contemplada. |
| nn(<71) | nn(<71) | Alegación desestimada por error invalidante nn. |
| nn(>70) | DS | Alegación desestimada por error de gestión nn4. |
| nn(>70) | Alegación desestimada por error de gestión nn |
| AC | Alegación revisada automática o manualmente y estimada. |
| GB | La alegación genera una baja en el mismo u otro municipio donde ya se ha contabilizado (procedimiento automático) |
| GB | GB | La alegación genera una baja en el mismo u otro municipio donde ya se ha contabilizado (procedimiento automático). |
| MA | DS | Alegación que tras intentar su carga se ha ido a Manuales. Revisada automática o manualmente se desestima porque no procede. |
| AC | Alegación que tras intentar su carga se ha ido a Manuales. Revisada automática o manualmente ha sido estimada. |
| GB | La alegación genera una baja en el mismo u otro municipio donde ya se ha contabilizado (procedimiento automático). |
| RA | DS | Alegación revisada manualmente y desestimada porque no procede. |
| AC | Alegación revisada manualmente y estimada. |
| T2 | DS | Alegación que se ha intentado su carga. Revisada automática o manualmente ha sido desestimada. |
| AC | Alegación que se ha intentado su carga. Revisada automática o manualmente ha sido estimada. |
| T1 | DS | Alegación que no va a carga. Revisada automática o manualmente ha sido desestimada. |
| AC | Alegación que no va a carga. Revisada automática o manualmente ha sido estimada. |
| BA | BA | Alegación de baja aceptada. |
| 4 En el caso de error 71 porque ya se ha contabilizado en el mismo u otro municipio. |
