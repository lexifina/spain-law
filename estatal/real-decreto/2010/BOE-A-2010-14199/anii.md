## ANEXO II

## CONJUNTO DE DATOS DEL INFORME CLÍNICO DE CONSULTA EXTERNA

| Variable | Formato | Valores | Aclaraciones | CM/R2 |
| --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento | Texto | Informe Clínico de Consulta Externa |  | CM |
| Fecha de firma | dd/mm/aaaa | Libre | Es común a ambos pies de firma del informe | CM |
| Fecha de Consulta | dd/mm/aaaa | Libre |  | CM |
| Nombre Responsable 1 | Texto | Libre (nombre+2 apellidos) | Es parte del primer pie de firma del informe | CM |
| Categoría profesional 1 | Texto | Médico Residente Facultativo Especialista de Área Jefe de Sección Jefe de Servicio | CM |
| Nombre Responsable 2 | Texto | Libre (nombre+2 apellidos) | Es parte del segundo pie de firma, que suele supervisar al primer firmante | CM |
| Categoría profesional 2 | Texto | Facultativo Especialista de Área Jefe de Sección Jefe de Servicio | CM |
| Servicio | Texto | Según normativa en vigor en cada momento. | Actualmente: clasificación de Servicios del CMBD/SIFCO | CM |
| Unidad | Texto | Libre |  | CM |
| DATOS DE LA INSTITUCIÓN EMISORA |
| Denominación del Servicio de Salud | Texto + Logo | SAS. Servicio Andaluz de Salud. SALUD. Servicio Aragonés de Salud. SESPA. Servicio de Salud del Principado de Asturias. Servicio Canario de Salud. SCS. Servicio Cántabro de Salud. SESCAM. Servicio de Salud de Castilla-La Mancha. SACyL .Gerencia Regional de Salud de Castilla y León. DdS-GC. Departament de Salut de la Generalitat de Catalunya. SES. Servicio Extremeño de Salud. SERGAS. Servizo Galego de Saúde. INGESA. Instituto Nacional de Gestión Sanitaria. IB-SALUT. Servicio de Salud de Illes Balears. |  | CM |
|  |  | RIOJASALUD. Servicio Riojano de Salud. Servicio Madrileño de Salud. Servicio Murciano de Salud. SNS-O. Servicio Navarro de SaludOSASUNBIDEA. Agència Valenciana de Salut OSAKIDETZA-Servicio Vasco de Salud. |  |  |
| Denominación del provisor de servicios | Texto + Logo | Libre |  | R |
| Denominación del Centro | Texto + Logo | CNH y posteriormente RECESS cuando esté disponible+texto libre | Existirá un campo adicional de texto libre para aquellos centros no recogidos en el inventario en vigor por ser de reciente apertura. | CM |
| Dirección del centro |  |  |  |  |
| Tipo de vía | Texto | CNH y posteriormente RECESS cuando esté disponible+texto libre | Existirá un campo adicional de texto libre para aquellos centros no recogidos en el inventario en vigor por ser de reciente apertura | CM |
| Nombre de la vía | Texto | CM |
| Número de la vía | Texto | CM |
| Código Postal | Texto | CM |
| Municipio | Texto | CM |
| Provincia | Texto | CM |
| País | Texto | CM |
| Teléfono | Texto | CM |
| Dirección Web/Correo electrónico | Texto | Libre | Se incluirá la dirección Web sólo si contiene información de interés para el usuario | R |
| DATOS DEL PACIENTE |
| Nombre | Texto | Dato que figure en la BD de la TSI de la CA |  | CM |
| Primer Apellido | Texto | CM |
| Segundo Apellido | Texto | CM |
| Fecha nacimiento | dd/mm/aaaa | CM |
| Sexo | Texto | H/M | CM |
| DNI/T.Residencia/Pasaporte | Texto |  | R |
| NASS | Texto | CM |
| CIP de C Autónoma | Texto | CM |
| Código SNS | Texto | R |
| CIP Europeo | Texto |  | Se reserva este espacio en previsión de que, en el futuro, exista un código europeo/internacional de identificación. | R |
| N.º Historia Clínica | Texto | Libre |  | CM |
| Domicilio |  |  |  |  |
| Tipo de vía | Texto | Dato que figure en la BD de TSI de la CA |  | CM |
| Nombre de la vía | Texto | CM |
| Número de la vía | Texto | CM |
| Piso | Texto | CM |
| Letra | Texto | CM |
| Código Postal | Texto | CM |
| Municipio | Texto | CM |
| Provincia | Texto | CM |
| País | Texto |  |  |  |
| Teléfono | Texto | Dato que figure en la BD de la TSI de la CA+texto libre | Existirá texto libre para añadir un segundo número de teléfono | R |
| DATOS DEL PROCESO ASISTENCIAL |
| Motivo de Consulta | Texto +código | Libre + Código CIE 9 MC / CIE 10 / SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Antecedentes | Texto | Libre | Se recomienda la clasificación en subapartados | CM |
| Enfermedades familiares hereditarias Enfermedades previas Antecedentes Neonatales, Obstétricos y Quirúrgicos Alergias Hábitos tóxicos Actuaciones Preventivas (1) Medicación previa |  |  | (1) Vacunaciones infantiles, del adulto, quimioprofilaxis realizadas, etc. (2) Se refiere a la valoración del impacto funcional de los problemas activos o enfermedades y se podrán utilizar una o varias escalas (Escalas de dependencia, clasificación | R |
| Situación funcional (2) Antecedentes sociales y profesionales |  |  | funcional de la Insuficiencia cardiaca, Valoraciones del grado de demencia, Escalas de Calidad de vida, etc.) |  |
| Historia Actual | Texto | Libre |  | CM |
| Exploración Física | Texto | Libre |  | CM |
| Resumen pruebas complementarias | Texto | Libre |  | CM |
| Laboratorio Imagen Otras pruebas | Texto | Libre | Se recomienda la clasificación en subapartados | R |
| Evolución y comentarios | Texto | Libre | Se pueden realizar comentarios del seguimiento evolutivo, en el caso de que el informe no se refiera a una sola consulta sino a un periodo de seguimiento en el que se han realizado varias entrevistas clínicas. En este caso se puede incluir aquí el periodo de tiempo del que es comprensivo el informe o reseñar las fechas en las que se produjeron las consultas. También es el lugar adecuado para describir reacciones adversas a fármacos utilizados en este episodio o describir complicaciones evolutivas de la/las enfermedades, realizar valoraciones diagnósticas o comentarios adicionales | CM |
| Diagnóstico Principal | Texto +código | Libre + Código CIE 9 MC / CIE 10 / SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Otros Diagnósticos | Texto +código | Libre + Código CIE 9 MC / CIE 10 / SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Procedimientos | Texto +código | Libre + Código CIE 9 MC / CIE 10 / SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Tratamiento | Texto | Libre |  | CM |
| Recomendaciones | Texto | Libre | Se trata de recomendaciones terapéuticas que no incluyen fármacos (oxigenoterapia, dieta, reposo o limitaciones de esfuerzo físico, etc.) | R |
| Fármacos | Texto +código | Libre (Especialidad+principio activo+ dosis/unidad+ n.º unidades/dosis+ intervalo de dosis+ vía administración + duración) nomenclator oficial MSPS (código nacional)/Snomed-CT | Prescripciones activas al final del período de seguimiento. En la medida en que la implantación de las aplicaciones informáticas de HCE, que incluyen módulos de prescripción lo permitan, el texto libre, será reemplazado progresivamente por el vocabulario del catálogo de medicamentos autorizados (Nomenclator Oficial/ Snomed-CT). | R |
| Otras recomendaciones | Texto | Libre | Se refiere a los planes de actuación previstos que no son propiamente medidas terapéuticas. Por ejemplo: fecha de próxima cita, conveniencia de nueva revisión, petición de pruebas, etc. | CM |

2 Se puede clasificar cada campo según se considere que su presencia es esencial (aunque la cumplimentación del valor no sea obligatoria) y por ello debe formar parte del conjunto mínimo del SNS /CM) o por el contrario es aconsejable su presencia pero no imprescindible como parte del conjunto mínimo de datos (R)
