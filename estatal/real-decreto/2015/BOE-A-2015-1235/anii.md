## ANEXO II

## MODELO DE DATOS DEL RAE-CMBD

## Anexo II.a

Estructura del fichero de intercambio

| Número | Nombre variable | Descripción | Valores(1) | Formato | Longitud | Observaciones |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | TIP_CIP | Tipo de código de Identificación Personal. | 1. Código de identificación Personal de la CA. 2. Tarjeta Individual Sanitaria del SNS. 3. Código de Identificación de MUFACE/ISFAS/MUGEJU. 4. Tarjeta Sanitaria Europea. 5. DNI. 6. Pasaporte. 9. Desconocido. | Carácter. | 1 |  |
| 2 | CIP | Código de identificación personal. |  | Carácter. | 16 |  |
| 3 | HISTORIA | Número de Historia Clínica. |  | Carácter. | 20 |  |
| 4 | FECNAC | Fecha de nacimiento. |  | Fecha (ddmmaaaa). | 8 |  |
| 5 | SEXO | Sexo. | 1. Varón. 2. Mujer. 9. No especificado. | Carácter. | 1 |  |
| 6 | PAIS_NAC | Código ISO del país de nacimiento. |  | Carácter. | 3 | Código ISO. En caso de no conocerse se codificará ZZZ. |
| 7 | RESIDE_CP | Código postal del domicilio. |  | Carácter. | 5 | 53+ código ISO país para residentes en el extranjero. |
| 8 | RESIDE_MUNI | Código de municipio del domicilio. |  | Carácter. | 6 | 530 + código ISO país para residentes en el extranjero. |
| 9 | REGFIN | Régimen de financiación. | 1. Sistema Nacional de Salud (SNS). 2. Reglamentos europeos y convenios bilaterales. 3. Mutualidades de funcionarios del estado y otras AAPP. 4. Mutuas colaboradoras con la Seguridad Social. 5. Accidentes de tráfico. 6. Financiación privada directa (personas físicas). 7. Financiación privada mediante seguro privado (Compañías de seguro sanitario). 8. Asistencia sanitaria transfronteriza. 9. Otros y Desconocido. | Carácter. | 1 |  |
| 10 | FECINICONT | Fecha y hora de inicio del contacto. |  | Fecha (ddmmaaaa hhmi). | 13 | En caso de no conocerse la hora-min consignar 9999. |
| 11 | FECINGHOSP | Fecha y hora de curso de la orden de ingreso del paciente. |  | Fecha (ddmmaaaa hhmi). | 13 | En caso de no conocerse la hora-min consignar 9999. |
| 12 | TIPCONT | Tipo de contacto. | 1. Hospitalización. 2. Hospitalización a domicilio. 3. Hospital de día médico. 4. Cirugía ambulatoria. 5. Procedimientos ambulatorios de especial complejidad. 6. Urgencias. 8. Otros. | Carácter. | 1 |  |
| 13 | TIPVISITA | Tipo de la visita. | 1. Contacto inicial. 2. Contacto sucesivo. 9. Desconocido. | Carácter. | 1 |  |
| 14 | PROCEDENCIA | Solicitante del contacto. | 10. Atención Primaria. 21. Servicios del propio hospital: Urgencias. 22. Servicios del propio hospital: Cirugía ambulatoria. 23. Servicios del propio hospital: Hospital de día médico. 24. Servicios del propio hospital: Hospitalización. 25. Servicios del propio hospital: Hospitalización a domicilio. 26. Servicios del propio hospital: Procedimientos de especial complejidad. 27. Servicios del propio hospital: Consultas. 28. Otros servicios. 30. Servicios de otro hospital/centro sanitario. 40. Por iniciativa del paciente. 50. Emergencias médicas. 60. Centro sociosanitario. 70. Por orden judicial. 80. Otros. 90. Desconocido. | Carácter. | 2 |  |
| 15 | CIRCONT | Circunstancias del contacto. | 1. No programado. 2. Programado. 9. Desconocido. | Carácter. | 1 |  |
| 16 | SERVICIO | Código del Servicio. | Ver listado de servicios en el anexo II.b. | Carácter. | 3 |  |
| 17 | FECFINCONT | Fecha y hora de fin del contacto. |  | Fecha (ddmmaaaa hhmi). | 13 | En caso de no conocerse la hora-min consignar 9999. |
| 18 | TIPALT | Destino tras el contacto. | 1. Domicilio. 2. Traslado a otro Hospital. 3. Alta voluntaria. 4. Exitus. 5. Traslado a centro sociosanitario. 8. Otros. 9. Desconocido. | Carácter. | 1 |  |
| 19 | DISPOSITIVO CONTINUIDAD | Continuidad asistencial. | 1. No precisa. 2. Hospitalización en el propio hospital. 3. Hospitalización a domicilio. 4. Hospital de día médico. 5. Urgencias. 6. Consultas. 8. Otros. 9. Desconocido. | Carácter. | 1 |  |
| 20 | FECINT | Fecha y hora de la intervención. |  | Fecha (ddmmaaaa hhmi). | 13 | En caso de no conocerse la hora-min consignar 9999. |
| 21 | UCI | Ingreso en UCI. | 1. SÍ. 2. NO. | Carácter. | 1 |  |
| 22 | DIAS_UCI | Días de estancia en UCI. |  | Numérico. | 3 |  |
| 23 | D1 | Diagnóstico Principal. |  | Carácter. | 8 | CIE10ES (a partir del 1 de enero de 2016). |
| 24 | POAD1 | Marcador POA del diagnóstico principal. Diagnóstico Principal presente al ingreso. | S. SÍ. N. NO. D. Desconocido. I. Indeterminado clínicamente. E. Exento. | Carácter. | 1 |  |
| 25 | D2 - D20 | Diagnósticos secundarios (hasta un máximo de 19). |  | Carácter. | 8 | CIE10ES (a partir del 1 de enero de 2016). |
| 26 | POAD2 - POAD20 | Marcador POA de los diagnósticos secundarios. Diagnóstico presente al ingreso. | S. SÍ. N. NO. D. Desconocido. I. Indeterminado clínicamente. E. Exento. | Carácter. | 1 |  |
| 27 | PROC1- PROC20 | Procedimientos en el centro (1 al 20). |  | Carácter. | 7 | CIE10ES (a partir del 1 de enero de 2016). |
| 28 | PROCEXT1 - PROCEXT6 | Procedimientos en otros centros (1 al 6). |  | Carácter. | 7 | CIE10ES (a partir del 1 de enero de 2016). |
| 29 | M1 M6 | Morfología de neoplasias (1 a 6). |  | Carácter. | 7 | CIEO (a partir del 1 de enero de 2016). |
| 30 | CEN_ SAN | Centro sanitario. |  | Carácter. | 9 | Código del Catálogo Nacional de hospitales o del REGCESS(2) |
| 31 | CCAA | Comunidad Autónoma. | Anexo II.c. | Carácter. | 2 | Código INE de Comunidad Autónoma. |
| (1) Los valores posibles son los establecidos con números o letras para cada variable y, en su caso, las clasificaciones o listados de referencia que se señalan en la columna de «observaciones». (2) Registro General de Centros Establecimientos y Servicios Sanitarios Orden SCO/3866/2007, de 18 de diciembre, por la que se establece el contenido y la estructura del Registro General de centros, servicios y establecimientos sanitarios del Ministerio de Sanidad y Consumo. |

## Anexo II.b

Tabla de Servicios y Unidades

ACL Análisis Clínicos.

ACV Angiología y Cirugía Vascular.

ADM Admisión y documentación clínica.

ALG Alergología.

ANR Anestesia y Reanimación.

APA Anatomía Patológica.

BCS Banco de Sangre.

BIO Bioquímica Clínica.

CAR Cardiología.

CCA Cirugía Cardiaca.

CCI Cirugía Cardiaca Infantil.

CIR Cirugía General y Digestiva.

CMF Cirugía Maxilofacial.

CPE Cirugía Pediátrica.

CPL Cirugía Plástica y Reparadora.

CTO Cirugía Torácica.

DCL Documentación Clínica.

DER Dermatología.

DIE Dietética.

DIG Digestivo.

END Endocrinología.

EST Estomatología.

FAC Farmacología Clínica.

FAR Farmacia.

GEN Genética.

GRT Geriatría.

HEL Hematología Laboratorio.

HEM Hematología Clínica.

INF Enfermedades infecciosas.

INM Inmunología.

LAB Laboratorios.

LIT Litotricia.

MFC Medicina Familiar y Comunitaria.

MIC Microbiología y Parasitología.

MIN Medicina Intensiva Neonatal.

MIP Medicina Intensiva Pediátrica.

MIR Medicina Interna.

MIV Medicina Intensiva.

MNU Medicina Nuclear.

MPR Medicina Preventiva.

NEF Nefrología.

NEO Neonatología.

NFC Neurofisiología Clínica.

NML Neumología.

NRC Neurocirugía.

NRL Neurología.

OBG Obstetricia y Ginecología.

OFT Oftalmología.

ONC Oncología Médica.

ONR Oncología Radioterápica.

ORL Otorrinolaringología.

OTR Otros.

PED Pediatría.

PSQ Psiquiatría.

RAD Radiología.

RAI Radiología Intervencionista.

RDT Radioterapia.

REH Rehabilitación.

REU Reumatología.

TRA Traumatología y C. Ortopédica.

UCE Unidad de Corta Estancia.

UCP Unidad de Cuidados Paliativos.

UCR Unidad de Coronaria.

UDO Unidad del Dolor.

UHD Unidad de Hemodiálisis.

ULE Unidad de Larga Estancia.

ULM Unidad de Lesionados Medulares.

URG Urgencias.

URH Unidad de Reproducción Humana.

URO Urología.

USO Unidad del Sueño.

UTR Unidades de Extracción y Trasplantes.

UTX Unidad de Desintoxicación.

## Anexo II.c

Tabla de Códigos de Comunidades Autónomas

1 Andalucía.

2 Aragón.

3 Asturias (Principado de).

4 Balears (Illes).

5 Canarias.

6 Cantabria.

7 Castilla y León.

8 Castilla-La Mancha.

9 Cataluña.

10 Comunidad Valenciana.

11 Extremadura.

12 Galicia.

13 Madrid (Comunidad de).

14 Murcia (Región de).

15 Navarra (Comunidad Foral de).

16 Pais Vasco.

17 Rioja (La).

18 Ceuta.

19 Melilla.

## Anexo II.d

Tabla de Códigos ISO de países(1)

| Código numérico | Nombre | Código numérico | Nombre |
| --- | --- | --- | --- |
| 004 | Afganistán. | 096 | Brunéi. |
| 248 | Åland. | 100 | Bulgaria. |
| 008 | Albania. | 854 | Burkina Faso. |
| 276 | Alemania. | 108 | Burundi. |
| 020 | Andorra. | 064 | Bután. |
| 024 | Angola. | 132 | Cabo Verde. |
| 660 | Anguila. | 116 | Camboya. |
| 028 | Antigua y Barbuda. | 120 | Camerún. |
| 682 | Arabia Saudita. | 124 | Canadá. |
| 012 | Argelia. | 634 | Catar. |
| 032 | Argentina. | 535 | Caribe Neerlandés. |
| 051 | Armenia. | 148 | Chad. |
| 533 | Aruba. | 152 | Chile. |
| 036 | Australia. | 156 | China. |
| 040 | Austria. | 196 | Chipre. |
| 031 | Azerbaiyán. | 170 | Colombia. |
| 044 | Bahamas. | 174 | Comoras. |
| 050 | Bangladés. | 408 | Corea del Norte. |
| 052 | Barbados. | 410 | Corea del Sur. |
| 048 | Bahréin. | 384 | Costa de Marfil. |
| 056 | Bélgica. | 188 | Costa Rica. |
| 084 | Belice. | 191 | Croacia. |
| 204 | Benín. | 192 | Cuba. |
| 060 | Bermudas. | 531 | Curazao. |
| 112 | Bielorrusia. | 208 | Dinamarca. |
| 104 | Birmania. | 212 | Dominica. |
| 068 | Bolivia. | 218 | Ecuador. |
| 070 | Bosnia y Herzegovina. | 818 | Egipto. |
| 072 | Botsuana. | 222 | El Salvador. |
| 076 | Brasil. | 784 | Emiratos Árabes Unidos. |
| 232 | Eritrea. | 344 | Hong Kong. |
| 703 | Eslovaquia. | 348 | Hungría. |
| 705 | Eslovenia. | 356 | India. |
| 724 | España. | 360 | Indonesia. |
| 840 | Estados Unidos. | 368 | Irak. |
| 233 | Estonia. | 364 | Irán. |
| 231 | Etiopía. | 372 | Irlanda. |
| 608 | Filipinas. | 833 | Isla de Man. |
| 246 | Finlandia. | 574 | Norfolk. |
| 242 | Fiyi. | 352 | Islandia. |
| 250 | Francia. | 136 | Islas Caimán. |
| 266 | Gabón. | 184 | Islas Cook. |
| 270 | Gambia. | 234 | Islas Feroe. |
| 268 | Georgia. | 238 | Islas Malvinas. |
| 288 | Ghana. | 580 | Islas Marianas del Norte. |
| 292 | Gibraltar. | 584 | Islas Marshall. |
| 308 | Granada. | 612 | Islas Pitcairn. |
| 300 | Grecia. | 090 | Islas Salomón. |
| 304 | Groenlandia. | 796 | Islas Turcas y Caicos. |
| 312 | Guadalupe. | 581 | Islas ultramarinas de Estados Unidos. |
| 316 | Guam. | 092 | Islas Vírgenes Británicas. |
| 320 | Guatemala. | 850 | Islas Vírgenes de los Estados Unidos. |
| 254 | Guayana Francesa. | 376 | Israel. |
| 831 | Guernsey. | 380 | Italia. |
| 324 | Guinea. | 388 | Jamaica. |
| 624 | Guinea-Bisáu. | 392 | Japón. |
| 226 | Guinea Ecuatorial. | 832 | Jersey. |
| 328 | Guyana. | 400 | Jordania. |
| 332 | Haití. | 398 | Kazajistán. |
| 340 | Honduras. | 404 | Kenia. |
| 417 | Kirguistán. | 500 | Montserrat. |
| 296 | Kiribati. | 508 | Mozambique. |
| 414 | Kuwait. | 516 | Namibia. |
| 418 | Laos. | 520 | Nauru. |
| 426 | Lesoto. | 524 | Nepal. |
| 428 | Letonia. | 558 | Nicaragua. |
| 422 | Líbano. | 562 | Níger. |
| 430 | Liberia. | 566 | Nigeria. |
| 434 | Libia. | 570 | Niue. |
| 438 | Liechtenstein. | 578 | Noruega. |
| 440 | Lituania. | 540 | Nueva Caledonia. |
| 442 | Luxemburgo. | 554 | Nueva Zelanda. |
| 446 | Macao. | 512 | Omán. |
| 450 | Madagascar. | 528 | Países Bajos. |
| 458 | Malasia. | 586 | Pakistán. |
| 454 | Malaui. | 585 | Palaos. |
| 462 | Maldivas. | 275 | Estado de Palestina. |
| 466 | Malí. | 591 | Panamá. |
| 470 | Malta. | 598 | Papúa Nueva Guinea. |
| 504 | Marruecos. | 600 | Paraguay. |
| 474 | Martinica. | 604 | Perú. |
| 480 | Mauricio. | 258 | Polinesia Francesa. |
| 478 | Mauritania. | 616 | Polonia. |
| 175 | Mayotte. | 620 | Portugal. |
| 484 | México. | 630 | Puerto Rico. |
| 583 | Micronesia. | 826 | Reino Unido. |
| 498 | Moldavia. | 140 | República Centroafricana. |
| 492 | Mónaco. | 203 | República Checa. |
| 496 | Mongolia. | 807 | República de Macedonia. |
| 499 | Montenegro. | 178 | República del Congo. |
| 180 | República Democrática del Congo. | 728 | Sudán del Sur. |
| 214 | República Dominicana. | 752 | Suecia. |
| 638 | Reunión. | 756 | Suiza. |
| 646 | Ruanda. | 740 | Surinam. |
| 642 | Rumania. | 744 | Svalbard y Jan Mayen. |
| 643 | Rusia. | 764 | Tailandia. |
| 732 | Sahara Occidental. | 834 | Tanzania. |
| 882 | Samoa. | 762 | Tayikistán. |
| 016 | Samoa Americana. | 626 | Timor Oriental. |
| 652 | San Bartolomé. | 768 | Togo. |
| 659 | San Cristóbal y Nieves. | 772 | Tokelau. |
| 674 | San Marino. | 776 | Tonga. |
| 663 | San Martín. | 780 | Trinidad y Tobago. |
| 666 | San Pedro y Miquelón. | 788 | Túnez. |
| 670 | San Vicente y las Granadinas. | 795 | Turkmenistán. |
| 654 | Santa Helena, A. y T. | 792 | Turquía. |
| 662 | Santa Lucía. | 798 | Tuvalu. |
| 678 | Santo Tomé y Príncipe. | 804 | Ucrania. |
| 686 | Senegal. | 800 | Uganda. |
| 688 | Serbia. | 858 | Uruguay. |
| 690 | Seychelles. | 860 | Uzbekistán. |
| 694 | Sierra Leona. | 548 | Vanuatu. |
| 702 | Singapur. | 336 | Ciudad del Vaticano. |
| 534 | Sint Maarten. | 862 | Venezuela. |
| 760 | Siria. | 704 | Vietnam. |
| 706 | Somalia. | 876 | Wallis y Futuna. |
| 144 | Sri Lanka. | 887 | Yemen. |
| 748 | Suazilandia. | 262 | Yibuti. |
| 710 | Sudáfrica. | 894 | Zambia. |
| 729 | Sudán. | 716 | Zimbabue. |
| ZZZ | Desconocido. |  |  |
| (1) Norma ISO 3166, de la Organización internacional para la Estandarización, en su versión ISO 3166-1 (código alfanumérico, a tres dígitos), corresponde al definido por la División estadística de las Naciones Unidas. |

> Redactado el anexo II.a conforme a la corrección de errores publicada en BOE núm. 163, de 9 de julio de 2015. Ref. BOE-A-2015-7664.
