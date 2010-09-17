## ANEXO VIII

## CONJUNTO DE DATOS DE LA HISTORIA CLÍNICA RESUMIDA

| Variable | Formato | Valores | Aclaraciones | CM/R14 | Volcado de Datos15 | Acceso 16 |
| --- | --- | --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento | Texto | Historia Clínica Resumida |  | CM | A | P/C |
| Fecha de creación | dd/mm/aaaa | Libre |  | CM | A | P/C |
| Fecha de última actualización | dd/mm/aaaa | Libre | La fecha en la que fue modificado alguno de los componentes del registro por última vez | CM | A | P/C |
| DATOS DE LA INSTITUCIÓN EMISORA |
| Denominación del Servicio de Salud | Texto + logo | SAS. Servicio Andaluz de Salud. SALUD. Servicio Aragonés de Salud SESPA. Servicio de Salud del Principado de Asturias. Servicio Canario de Salud SCS. Servicio Cántabro de Salud. SESCAM. Servicio de Salud de Castilla-La Mancha. SACyL .Gerencia Regional de Salud de Castilla y León. DdS-GC. Departament de Salut de la Generalitat de Catalunya SES. Servicio Extremeño de Salud. SERGAS.Servizo Galego de Saúde INGESA. Instituto Nacional de Gestión Sanitaria. IB-SALUT. Servicio de Salud de Illes Balears. RIOJASALUD. Servicio Riojano de Salud. Servicio Madrileño de Salud. Servicio Murciano de Salud SNS-O. Servicio Navarro de Salud-OSASUNBIDEA. Agència Valenciana de Salut OSAKIDETZA-Servicio Vasco de Salud. |  | CM | A | P/C |
| Denominación del provisor de servicios | Texto+logo | Libre |  | R |  |  |
| DATOS DEL USUARIO/PACIENTE |
| Nombre | Texto | Dato que figure en BD de TSI de la CA |  | CM | A | P/C |
| Primer Apellido | Texto | CM | A | P/C |
| Segundo Apellido | Texto | CM | A | P/C |
| Fecha de nacimiento | dd/mm/aaaa | CM | A | P/C |
| Sexo | Texto | H/M | CM | A | P/C |
| DNI/T.Residencia/Pasaporte | Texto |  | R | A | P/C |
| NASS | Texto | CM | A | P/C |
| CIP de C. Autónoma | Texto | CM | A | P/C |
| Código SNS | Texto | R | A | P/C |
| CIP Europeo |  |  | Se reserva este espacio en previsión de que en el futuro exista un código europeo/internacional de identificación. | R | A | P/C |
| N.° Historia Clínica | Texto | Libre |  | CM | A | P/C |
| Tipo de vía | Texto | Dato que figure en la BD de TSI de la CA |  | CM | A | P/C |
| Nombre de la vía | Texto | CM | A | P/C |
| Número de la vía | Texto | CM | A | P/C |
| Piso | Texto | CM | A | P/C |
| Letra | Texto | CM | A | P/C |
| Código Postal | Texto | CM | A | P/C |
| Municipio | Texto | CM | A | P/C |
| Provincia | Texto | CM | A | P/C |
| Teléfono | Texto | R | A | P/C |
| Persona de referencia | Texto | Libre (nombre + 2 apellidos) | Se trata de la persona que representa los intereses del paciente. | R | A/M | P/C |
| Teléfono de referencia | Texto | Libre |  | R | A/M | P/C |
| Cuidador Principal | Texto | Libre (nombre + 2 apellidos) |  | R | A/M | P/C |
| DATOS DE SALUD |
| Existe información reservada por decisión del paciente | Botón s/n | SI NO | Este campo informa al profesional de que existe algún dato clínico que no figura en la HC por decisión del propio paciente. | CM | A | P/C |
| Existe documento de instrucciones previas | Botón s/n | SI NO | Informa al profesional de que existe este documento que está disponible en el Registro de Últimas Voluntades. | CM | A/M | P/C |
| Está incluido en protocolo de investigación clínica | Botón s/n | SI NO | Informa de la inclusión en un protocolo de investigación en la fecha de última actualización. | R | M | P/C |
| Alergias | Texto | Libre |  | CM | A | P/C |
| Vacunaciones | Texto | Libre |  | CM | A | P/C |
| Problemas Resueltos, Cerrados o Inactivos | Texto | Fecha + Texto Libre | Se especificará la fecha de cierre y el motivo | R | A | P/C |
| Problemas y Episodios Activos | Texto + Código | Fecha + Texto libre Sistema de Codificación CIE 9 MC/CIE 10/CIAP 2 Definida/SNOMED-CT | Los que figuren en la historia a la fecha de última actualización. Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS | CM R | A | P/C |
| Tratamiento | Texto | Libre |  | CM |  | P/C |
| Recomendaciones | Texto | Libre | Se trata de recomendaciones terapéuticas que no incluyen fármacos (oxigenoterapia, dieta, limitaciones de esfuerzo físico, etc.) | CM | A | P1C |
| Fármacos | Texto + código | Libre (Especialidad + principio activo + dosis/unidad+ n° unidades/dosis+ intervalo de dosis+ vía administración+ duración) nomenclator oficial MSPS (código nacional)/Snomed-CT | Prescripciones activas a la fecha de actualización. En la medida en que la implantación de las aplicaciones informáticas de HCE, que incluyen módulos de prescripción lo permitan, el texto libre, será reemplazado progresivamente por el vocabulario del catálogo de medicamentos autorizados (Nomenclator Oficial/Snomed-CT) | CM | A | P1C |
| Diagnósticos Enfermeros activos | Texto + Código | Literal NANDA +Código NANDA | Los que figuren en la historia a la fecha de última actualización | CM R | A | P1C |
| Resultados de Enfermería | Texto + Código | Literal NOC +Código NOC | Aquellos resultados seleccionados para identificar la evolución del paciente, como resultado de las intervenciones planificadas. Los que figuren en la historia a la fecha de última actualización | CM R | A | P1C |
| Intervenciones de Enfermería | Texto + código | Literal NIC +Código NIC | Los que figuren en la historia a la fecha de última actualización | CM R | A | P1C |
| ALERTAS | Texto | Libre | Su contenido deben ser advertencias clave de carácter objetivo que por su especial trascendencia deban ser resaltadas para ser tenidas en cuenta por cualquier profesional que deba prestar atención (Ej: Angioedema desencadenado por IECAS, Dispositivo IV con reservorio) | CM | M | P1C |
| Observaciones Subjetivas del Profesional | Texto | Libre | La única justificación de este campo es recoger valoraciones del profesional, siempre que sean de auténtico interés para el manejo de los problemas de salud por otro profesional. Sólo deberán ser reseñadas aquellas observaciones que sean encuadrables en algunos de los siguientes apartados: • VALORACIONES SOBRE HIPÓTESIS DIAGNÓSTICAS NO DEMOSTRADAS • SOSPECHA ACERCA DE INCUMPLIMIENTOS TERAPÉUTICOS • SOSPECHA DE TRATAMIENTOS NO DECLARADOS | R | M | P |
|  |  |  | • SOSPECHA DE HÁBITOS NO RECONOCIDOS |  |  |  |
|  |  |  | • SOSPECHA DE HABER SIDO VÍCTIMA DE MALOS TRATOS |  |  |  |
|  |  |  | • COMPORTAMIENTOS INSÓLITOS |  |  |  |

14 Se puede clasificar cada campo según se considere que su presencia en esencial (aunque la cumplimentación del valor no sea obligatoria) y por ello debe formar parte del conjunto mínimo del SNS (CM), o por el contrario es aconsejable su presencia, pero no imprescindible como parte del conjunto mínimo de datos (R).

15 Los datos de los campos de la Historia Clínica Resumida deben alimentarse de forma automática A, a partir de la historia de salud digital, excepto un número muy reducido de ellos que tendrá que alimentar manualmente M el profesional, en aquellos casos en que éste lo considere conveniente.

16 El campo puede estar accesible, según la naturaleza de su contenido (anotaciones subjetivas o datos ojbetivos), a los profesionales P o al ciudadano C.
