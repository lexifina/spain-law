## ANEXO IV

## CONJUNTO DE DATOS DEL INFORME CLÍNICO DE ATENCIÓN PRIMARIA

| Variable | Formato | Valores | Aclaraciones | CM/R4 |
| --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento | Texto | Informe Clínico de Atención Primaria |  | CM |
| Fecha de firma | dd/mm/aaaa | Libre | Fecha en la cual se emite el informe. Es común a ambos pies de firma. | CM |
| Fecha inicio periodo | dd/mm/aaaa | Libre | Fecha en la que se inicia el periodo de seguimiento en el que se inscriben los diferentes episodios y actuaciones que se describen. | CM |
| Fecha fin periodo | dd/mm/aaaa | Libre | Fecha en la que finaliza el periodo de seguimiento en el que se inscriben los diferentes episodios y actuaciones que se describen. | CM |
| Nombre Responsable 1 | Texto | Libre (nombre + 2 apellidos) | Es parte del primer pie de firma del informe. | CM |
| Categoría profesional 1 | Texto | Médico Residente Médico de Familia Pediatra de AP Texto Libre | CM |
| Nombre Responsable 2 | Texto | Libre (nombre + 2 apellidos) | Es parte del segundo pie de firma, que suele supervisar el primer firmante. | CM |
| Categoría responsable 2 | Texto | Médico de Familia Pediatra de AP Texto Libre | CM |
| DATOS DE LA INSTITUCIÓN EMISORA |
| Denominación del Servicio de Salud | Texto + logo | SAS. Servicio Andaluz de Salud. SALUD. Servicio Aragonés de Salud. SESPA. Servicio de Salud del Principado de Asturias. Servicio Canario de Salud. SCS. Servicio Cántabro de Salud. SESCAM. Servicio de Salud de Castilla-La Mancha. SACyL .Gerencia Regional de Salud de Castilla y León. DdS-GC. Departament de Salut de la Generalitat de Catalunya. SES. Servicio Extremeño de Salud. SERGAS. Servizo Galego de Saúde. INGESA. Instituto Nacional de Gestión Sanitaria. IB-SALUT. Servicio de Salud de Illes Balears. RIOJASALUD. Servicio Riojano de Salud. Servicio Madrileño de Salud. Servicio Murciano de Salud. SNS-O. Servicio Navarro de Salud-OSASUNBIDEA. Agència Valenciana de Salut. OSAKIDETZA-Servicio Vasco de Salud. |  | CM |
| Denominación del provisor de servicios | Texto +logo | Libre |  | R |
| Denominación del Centro | Texto + Logo | Inventario de Centros de Atención Primaria y posteriormente RECESS cuando esté disponible + texto libre | Existirá un campo adicional de texto libre para aquellos centros no recogidos en el inventario en vigor por ser de reciente apertura. | CM |
| Dirección del Centro |  |  |  |
| Tipo de vía | Texto | Inventario de Centros de Atención Primaria y posteriormente RECESS cuando esté disponible + texto libre | CM |
| Nombre de la vía | Texto | CM |
| Número de la vía | Texto | CM |
| Piso | Texto | CM |
| Letra | Texto | CM |
| Código Postal | Texto | CM |
| Municipio | Texto | CM |
| Provincia | Texto | CM |
| País | Texto | CM |
| Teléfono | Texto | CM |
| Dirección Web/Correo Electrónico | Texto | Libre | Se incluirá la dirección Web sólo si contiene información de interés para el usuario. | R |
| DATOS DEL USUARIO/PACIENTE |
| Nombre | Texto | Dato que figure en BD de la TSI de la CA |  | CM |
| Primer Apellido | Texto | CM |
| Segundo Apellido | Texto | CM |
| Fecha de nacimiento | dd/mm/aaaa | CM |
| Sexo | Texto | H/M | CM |
| DNI/T.Residencia/Pasaporte | Texto |  | R |
| NASS | Texto | CM |
| CIP de la C. Autónoma | Texto | CM |
| Código SNS | Texto | R |
| CIP Europeo |  |  | Se reserva este espacio en previsión de que en el futuro, exista un código europeo/internacional de identificación. | R |
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
| País | Texto |  |
| Teléfono | Texto | R |
| Persona de Referencia | Texto | Libre (nombre + 2 apellidos) | Se trata de la persona que representa los intereses del paciente. | R |
| Teléfono de Referencia | Texto | Libre |  | R |
| DATOS DE SALUD |
| Antecedentes | Texto | Libre | Se recomienda su clasificación en subapartados. | CM |
| Enfermedades familiares hereditarias Enfermedades previas Antecedentes neonatales, obstétricos y quirúrgicos Alergias Hábitos tóxicos Actuaciones preventivas (1) Medicación previa Situación funcional (2) Antecedentes sociales y profesionales |  |  | (1) Vacunaciones infantiles, del adulto, quimioprofilaxis realizadas, etc. (2) Se refiere a la valoración del impacto funcional de los problemas activos o enfermedades y se podrán utilizar una o varias escalas (Escalas de dependencia, clasificación funcional de la insuficiencia cardíaca, valoraciones del grado de demencia, escalas de calidad de vida, etc.). | R |
| Resumen pruebas complementarias | Texto | Libre |  | CM |
| Laboratorio Imagen Otras pruebas | Texto | Libre | Se recomienda la clasificación en subapartados. | R |
| Resumen de Episodios Atendidos | Texto + código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Evolución y comentarios | Texto | Libre | Se pueden realizar comentarios del seguimiento evolutivo. También es el lugar adecuado para describir reacciones adversas a fármacos utilizados o describir complicaciones evolutivas de la/las enfermedades, realizar valoraciones diagnósticas o comentarios adicionales. | CM |
| Diagnósticos | Texto + código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Procedimientos | Texto + código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Tratamiento | Texto | Libre | Se refiera al último tratamiento que esté activo. | CM |
| Recomendaciones | Texto | Libre | Se trata de recomendaciones terapéuticas que no incluyen fármacos (oxigenoterapia, dieta, reposo o limitaciones de esfuerzo físico, etc.). | R |
| Fármacos | Texto +código | Libre (Especialidad+principio activo+ dosis/unidad+ n.º unidades/dosis+ intervalo de dosis+ vía administración+ duración) nomenclator oficial MSPS (código nacional)/Snomed- CT | Prescripciones activas al final del período de seguimiento. En la medida en que la implantación de las aplicaciones informáticas de HCE, que incluyen módulos de prescripción lo permitan, el texto libre, será reemplazado progresivamente por el vocabulario del catálogo de medicamentos autorizados (Nomenclator Oficial/ Snomed-CT). | CM R |
| Otras Recomendaciones | Texto | Libre | Se refiere a los planes de actuación previstos que no son propiamente medidas terapéuticas. Por ejemplo: fecha de próxima cita, conveniencia de una nueva revisión, petición de pruebas, etc... | R |

4 Se puede clasificar cada campo según se considere que su presencia es esencial (aunque la cumplimentación del valor no sea obligatoria) y por ello debe formar parte del conjunto mínimo del SNS /CM) o por el contrario es aconsejable su presencia pero no imprescindible como parte del conjunto mínimo de datos (R)
