## ANEXO III

## CONJUNTO DE DATOS DEL INFORME CLÍNICO DE URGENCIAS

| Variable | Formato | Valores de referencia | Aclaraciones | CM/R3 |
| --- | --- | --- | --- | --- |
| DATOS DEL DOCUMENTO |
| Tipo de documento | Texto | Informe Clínico de Urgencias |  | CM |
| Fecha de firma | dd/mm/aaaa | Libre | Es común a ambos pies de firma del informe. | R |
| Fecha y hora de ingreso o de activación del recurso | dd/mm/aaaa hh:mm | Libre |  | CM |
| Fecha y hora de alta | dd/mm/aaaa hh:mm | Libre |  | CM |
| Nombre Responsable 1 | Texto | Libre (nombre + 2 apellidos) | Es parte del primer pie de firma del informe. | CM |
| Categoría profesional 1 | Texto | Médico Residente Facultativo Jefe de Sección Jefe de Servicio | CM |
| Nombre Responsable 2 |  | Libre (nombre + 2 apellidos) | Es parte del segundo pie de firma, que suele supervisar al primer firmante. | CM |
| Categoría responsable 2 |  | Facultativo Jefe de Sección Jefe de Servicio | CM |
| Unidad Asistencial responsable | Texto | Servicio de Urgencia Hospitalaria Servicio de Urgencia de A.Primaria SAMU S.º Urgencias + texto libre |  | CM |
| DATOS DE LA INSTITUCIÓN EMISORA |
| Denominación del Servicio de Salud | Texto + Logo | SAS. Servicio Andaluz de Salud. SALUD. Servicio Aragonés de Salud. SESPA. Servicio de Salud del Principado de Asturias. Servicio Canario de Salud. SCS. Servicio Cántabro de Salud. SESCAM. Servicio de Salud de Castilla-La Mancha. SACyL. Gerencia Regional de Salud de Castilla y León. DdS-GC. Departament de Salut de la Generalitat de Catalunya. SES. Servicio Extremeño de Salud. SERGAS. Servizo Galego de Saúde. INGESA. Instituto Nacional de Gestión Sanitaria. IB-SALUT. Servicio de Salud de Illes Balears. RIOJASALUD. Servicio Riojano de Salud. Servicio Madrileño de Salud. Servicio Murciano de Salud. SNS-O. Servicio Navarro de Salud-OSASUNBIDEA. Agència Valenciana de Salut . OSAKIDETZA-Servicio Vasco de Salud. |  | CM |
| Denominación del provisor de servicios | Texto +logo | Libre |  | R |
| Denominación del Centro | Texto + Logo | CNH para Centros de Atención Especializada. Inventario para Centros de Primaria RECESS para ambos cuando esté disponible +texto libre | Existirá un campo adicional de texto libre para aquellos centros no recogidos en el inventario en vigor por ser de reciente apertura. | CM |
| Dirección del Centro |  |  |
| Tipo de vía | Texto | CM |
| Nombre de la vía | Texto | CM |
| Número de la vía | Texto | CM |
| Código Postal | Texto | CM |
| Municipio | Texto | CM |
| Provincia | Texto | CM |
| País | Texto | CM |
| Teléfono | Texto | CM |
| Dirección Web/Correo Electrónico | Texto | Se incluirá la dirección Web sólo si contiene información de interés para el usuario. | R |
| DATOS DEL PACIENTE |
| Nombre | Texto | Dato que figure en BD de la TSI de la CA |  | CM |
| Primer Apellido | Texto | CM |
| Segundo Apellido | Texto | CM |
| Fecha de nacimiento | dd/mm/aaaa | CM |
| Sexo | Texto | H/M | CM |
| DNI/T.Residencia/Pasaporte | Texto |  | R |
| NASS | Texto | CM |
| CIP de la C. Autónoma | Texto | CM |
| Código SNS | Texto | R |
| CIP Europeo |  |  | Se reserva este espacio en previsión de que en el futuro exista un código europeo/internacional de identificación. | R |
| N.º Historia Clínica | Texto | Libre |  | R |
| Domicilio |
| Tipo de vía | Texto | Dato que figure en la BD de TSI de la CA |  | CM |
| Nombre de la vía | Texto |  |  | CM |
| Número de la vía | Texto | CM |
| Piso | Texto | CM |
| Letra | Texto | CM |
| Código Postal | Texto | CM |
| Municipio | Texto | CM |
| Provincia | Texto | CM |
| País | Texto |  |
| Teléfono | Texto | R |
| Persona de Referencia | Texto | Libre (nombre + 2 apellidos) | R |
| Teléfono de Referencia | Texto | Libre | R |
| DATOS DEL PROCESO ASISTENCIAL |
| Procedencia | Texto | Médico de Familia/Pediatra de AP Por decisión del paciente o familiar Cuerpos de Seguridad Otros Servicios de Urgencias |  | R |
| Tipo de Consulta | Texto | Enfermedad Accidente de tráfico Accidente Laboral Otros Accidentes |  | R |
| Motivo de Alta | Texto | Ingreso Traslado a domicilio Traslado de Servicio Traslado a otro centro hospitalario Traslado a un centro sociosanitario Alta voluntaria Fallecimiento Otros | Se incluyen aquellas categorías correspondientes al CMBD nacional, independientemente de que los CMBD autonómicos incorporen categorías adicionales cuyas respuestas luego se reclasifican. La categoría de respuesta fallecimiento, será recodificada a éxitus. | CM |
| Motivo de Consulta | Texto + código | Libre + Código CIE 9 MC / CIE 10 / SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Antecedentes | Texto | Libre |  | CM |
| Enfermedades Previas Antecedentes neonatales, obstétricos y quirúrgicos Medicación previa Alergias Situación funcional (1) Antecedentes sociales y profesionales | Texto | Libre | (1) Se refiere a la valoración del impacto funcional de los problemas activos o enfermedades, y se podrán utilizar una o varias escalas (Escalas de dependencia, clasificación funcional de la insuficiencia cardiaca, valoraciones del grado de demencia, escalas de calidad de vida, etc.). | R |
| Historia Actual | Texto | Libre |  | CM |
| Exploración física |  |  |  | CM |
| TA ( / ) FC ( )lat/min FR ( ) resp/min Temp. ( )ºC Saturación O2 Glucemia capilar Resumen de exploración | Texto | Libre |  | R |
| Resumen de pruebas complementarias | Texto | Libre | Se recomienda la clasificación en subapartados. | CM |
| Laboratorio Imagen Otras pruebas | Texto | Libre |  | R |
| Evolución y comentarios | Texto | Libre | En su caso pueden incluirse, además de comentarios evolutivos y del período de observación, la descripción de técnicas realizadas durante el proceso de atención. También es el lugar adecuado para describir reacciones adversas a fármacos utilizados en este episodio, complicaciones evolutivas de la/las enfermedades, realizar valoraciones diagnósticas o comentarios adicionales. | CM |
| Diagnóstico principal | Texto +código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Otros diagnósticos | Texto +código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Procedimientos | Texto +código | Libre Código CIE 9 MC/CIE 10/CIAP2 definida/SNOMED-CT | Los sistemas de codificación serán sustituidos por versiones posteriores si así se acordara en el Consejo Interterritorial del SNS. | CM R |
| Tratamiento | Texto | Libre |  | CM |
| Recomendaciones | Texto | Libre | Se trata de recomendaciones terapéuticas que no incluyen fármacos (oxigenoterapia, dieta, reposo o limitaciones de esfuerzo físico, etc.). | R |
| Fármacos | Texto +código | Libre (Especialidad+principio activo+ dosis/unidad+ n.º unidades/dosis+ intervalo de dosis+ vía administración+ duración) nomenclator oficial MSPS (código nacional)/Snomed-CT | Prescripciones activas. En la medida en que la implantación de las aplicaciones informáticas de HCE, que incluyen módulos de prescripción lo permitan, el texto libre, será reemplazado progresivamente por el vocabulario del catálogo de medicamentos autorizados (Nomenclator Oficial/ Snomed-CT). | R |
| Otras recomendaciones | Texto | Libre | Se refiere a los planes de actuación previstos que no son propiamente medidas terapéuticas. Por ejemplo: fecha de próxima cita, conveniencia de nueva revisión, petición de pruebas, etc. | CM |

3 Se puede clasificar cada campo según se considere que su presencia es esencial (aunque la cumplimentación del valor no sea obligatoria) y por ello debe formar parte del conjunto mínimo del SNS /CM) o por el contrario es aconsejable su presencia pero no imprescindible como parte del conjunto mínimo de datos (R)
