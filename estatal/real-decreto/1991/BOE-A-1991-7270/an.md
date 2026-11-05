## ANEXO

## Fichero técnico de pensiones no contributivas

| N.º Ref. | Dato | Longitud | Pos. en reg. | Tipo de dato | Descripción |
| --- | --- | --- | --- | --- | --- |
| Campo | Subcampo | C | S |
| 1 | Autonomía. |  | 2 |  | 1 | N | Clave numérica de la Autonomía. |
| 2 | Provincia. |  | 2 |  | 3 | N | Clave numérica de la Provincia. |
| 3 | Tipo de Pensión. |  | 1 |  | 5 | A/N | Clase de la pensión. |
| 4 | Situación de la pensión. |  | 1 |  | 6 | N | Situación de la pensión. |
|  | Identificación. |  | 12 |  |  |  |  |
| 5 |  | Tipo Ident. |  | 1 | 7 | A/N | Tipo de identificación del pensionista. |
| 6 |  | Identif. |  | 9 | 6 | A/N | Identificación del pensionista (D.N.I. o N.I.E.). |
| 7 |  | D.C. DNI. |  | 2 | 17 | N | Dígitos de control del D.N.I. del pensionista. |
| 8 | Apellidos y Nombre. |  | 36 |  | 19 | A/N | Apellidos y nombre del pensionista. |
| 9 | Fecha Nacimiento. |  | 8 |  |  |  | Fecha de nacimiento del pensionista. |
|  |  | Año. |  | 4 | 55 |  | Año de nacimiento del pensionista. |
|  |  | Mes. |  | 2 | 59 |  | Mes de nacimiento del pensionista. |
|  |  | Día. |  | 2 | 61 |  | Día de nacimiento del pensionista. |
| 10 | Sexo. |  | 1 |  | 63 | N | Sexto del pensionista. |
| 11 | Estado Civil. |  | 1 |  | 64 | N | Estado civil del pensionista. |
| 12 | Domicilio. |  | 36 |  | 65 | A/N | Domicilio del pensionista. |
| 13 | Código Postal. |  | 5 |  | 110 | A/N | Código postal del pensionista. |
| 14 | Localidad. |  | 30 |  | 106 | A/N | Nombre de la localidad de residencia del pensionista. |
| 15 | Municipio. |  | 6 |  | 136 | N | Código de municipio del pensionista. |
| 16 | Nacionalidad. |  | 3 |  | 142 | N | Código de la nacionalidad del pensionista. |
| 17 | Número de la S.S. |  | 11 |  | 145 | N | Número de Afiliación a la Seguridad Social. |
| 18 | Ingr. pensionista. |  | 6 |  | 156 | N | Ingresos totales anuales del pensionista. |
| 19 | Trabaja el pensionista. |  | 1 |  | 162 | N | Indicador de si trabaja el pensionista. |
| 20 | Pensión concurrente primera. |  | 3 |  | 163 | A/N | Código de la primera pensión concurrente del pensionista. |
| 21 | Pensión concurrente segunda. |  | 3 |  | 166 | A/N | Código de la segunda pensión concurrente del pensionista. |
| 22 | Rég. Procedencia. |  | 1 |  | 169 | A/N | Código del Régimen de procedencia del pensionista. |
| 23 | N. Total Conviv. |  | 2 |  | 170 | N | Número total de convivientes con el pensionista. |
|  | Identif. del primer Conviv. |  | 10 |  |  |  |  |
| 24 |  | Tipo Identif. |  | 1 | 172 | A/N | Tipo de identificación del conviviente (D.N.I. o N.I.E.). |
| 25 |  | Identif. |  | 9 | 173 | A/N | Identificación del conviviente. |
| 26 | Apell. y Nombre del primer Conviv. |  | 36 |  | 182 | A/N | Apellidos y nombre del conviviente. |
| 27 | Pens. de Jubilación o Invalidez. |  | 1 |  | 218 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
|  | Identif. del segundo Conviv. |  | 10 |  |  |  |  |
| 28 |  | Tipo Identif. |  | 1 | 219 | A/N | Tipo de identificación del conviviente (D.N.I. o N.I.E.). |
| 29 |  | Identif. |  | 9 | 220 | A/N | Identificación del conviviente. |
| 30 | Apell. y Nombre del segundo Conviv. |  | 36 |  | 229 | A/N | Apellidos y nombre del conviviente. |
| 31 | Pens. de Jubilación o Invalidez. |  | 1 |  | 265 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
|  | Identif. del tercer Conviv. |  | 10 |  |  |  |  |
| 32 |  | Tipo Identif. |  | 1 | 266 | A/N | Tipo de identificación del conviviente (D.N.I. o N.I.E.). |
| 33 |  | Identf. |  | 9 | 267 | A/N | Identificación del conviviente. |
| 34 | Apell. y Nombre del tercer Conviv. |  | 36 | 276 |  | A/N | Apellidos y nombre del conviviente. |
| 35 | Pens. de Jubilación o Invalidez. |  | 1 |  | 312 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
|  | Identif. del cuarto Conviv. |  | 10 |  |  |  |  |
| 36 |  | Tipo Identif. |  | 1 | 313 | A/N | Tipo de identificación del conviviente (D.N.I. o N.I.E.). |
| 37 |  | Identif. |  | 9 | 314 | A/N | Identificación del conviviente. |
| 38 | Apell. y Nombre del cuarto Conviv. |  | 36 |  | 323 | A/N | Apellidos y nombre del conviviente. |
| 39 | Pens. de Jubilación o Invalidez. |  | 1 |  | 359 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
|  | Identif. del quinto Conviv. |  | 10 |  |  |  |  |
| 40 |  | Tipo Identif. |  | 1 | 360 | A/N | Tipo de identificación del conviviente (D.N.I. o N.I.E.). |
| 41 |  | Identif. |  | 9 | 361 | A/N | Identificación del conviviente. |
| 42 | Apell. y Nombre del quinto Conviv. |  | 36 |  | 320 | A/N | Apellidos y nombre del conviviente. |
| 43 | Pens. de Jubilación o Invalidez. |  | 1 |  | 406 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
|  | Identif. del sexto Conviv. |  | 10 |  |  | A/N |  |
| 44 |  | Tipo Identif. |  | 1 | 407 | A/N | Tipo de Identificación del conviviente (D.N.I. o N.I.E.). |
| 45 |  | Identif. |  | 9 | 408 | A/N | Identificación del conviviente. |
| 46 | Apell. y Nombre del sexto Conviv. |  | 36 |  | 417 | A/N | Apellidos y nombre del conviviente. |
| 47 | Pens. de Jubilación o Invalidez. |  | 1 |  | 453 | A/N | Indicador de si el conviviente percibe una pensión de invalidez o jubilación. |
| 48 | Ingr. Convivientes. |  | 7 |  | 454 | N | Ingresos totales anuales de los convivientes. |
| 49 | Grado Minusvalía. |  | 3 |  | 461 | N | Grado de minusvalía del pensionista. |
|  | Discapacidad primera. |  | 9 |  |  |  | Discapacidad primera del pensionista. |
| 50 |  | Código. |  | 4 | 464 | N | Código de discapacidad. |
| 51 |  | Diagnóst. |  | 3 | 468 | N | Código del diagnóstico. |
| 52 |  | Etiolog. |  | 2 | 471 | N | Código de etiología. |
|  | Discapacidad segunda. |  | 9 |  |  | N | Discapacidad segunda del pensionista. |
| 53 |  | Código. |  | 4 | 473 | N | Código de discapacidad. |
| 54 |  | Diagnóst. |  | 3 | 477 | N | Código del diagnóstico. |
| 55 |  | Etiolog. |  | 2 | 480 | N | Código de etiología. |
|  | Discapacidad tercera. |  | 9 |  |  | N | Discapacidad tercera del pensionista. |
| 56 |  | Código. |  | 4 | 482 | N | Código de discapacidad. |
| 57 |  | Diagnóst. |  | 3 | 486 | N | Código del diagnóstico. |
| 58 |  | Etiolog. |  | 2 | 489 | N | Código de etiología. |
| 59 | Porcentaje discapac. |  | 3 |  | 491 | N | Porcentaje de la discapacidad. |
| 60 | Fact. Soc. y Complem. |  | 3 |  | 494 | N | Total del baremo de factores sociales y complementarios. |
| 61 | Necesidad otra pers. |  | 2 |  | 497 | N | Total baremo de necesidad de otra persona. |
| 62 | Fecha solicitud. |  | 6 |  |  |  | Fecha en que solicitó la pensión. |
|  |  | Año. |  | 2 | 499 | N | Año en que solicitó la pensión. |
|  |  | Mes. |  | 2 | 501 | N | Mes en que solicitó la pensión. |
|  |  | Día. |  | 2 | 503 | N | Día en que solicitó la pensión. |
| 63 | Fecha resolución. |  | 6 |  |  | N | Fecha de resolución de la pensión. |
|  |  | Año. |  | 2 | 505 | N | Año de resolución de la pensión. |
|  |  | Mes. |  | 2 | 507 | N | Mes de resolución de la pensión. |
|  |  | Día. |  | 2 | 509 | N | Día de resolución de la pensión. |
| 64 | Fecha Alta Nómina. |  | 4 |  |  |  | Año y mes de alta en nómina. |
|  |  | Año. |  | 2 | 511 | N | Año de alta en nómina de la pensión. |
|  |  | Mes. |  | 2 | 513 | N | Mes de alta en nómina de la pensión. |
| 65 | Importe Mensual. |  | 6 |  | 515 | N | Importe mensual de la pensión. |
| 66 | Compl. Neces. otra persona. |  | 6 |  | 521 | N | Importe mensual por complemento necesidad de otra persona. |
| 67 | Perceptor. |  | 1 |  | 527 | N | Código de relación del perceptor con el pensionista. |
|  | Identif. Perceptor. |  | 12 |  |  |  |  |
| 68 |  | Tipo Identif. |  | 1 | 528 | A/N | Tipo de identificación del perceptor. |
| 69 |  | Identif. |  | 9 | 529 | A/N | Identificación del perceptor. |
| 70 |  | D.C. DNI. |  | 2 | 538 | A/N | Dígitos de control del D.N.I. del perceptor. |
| 71 | Apell. y Nombr. Percep. |  | 36 |  | 540 | A/N | Apellidos y nombre del perceptor. |
| 72 | Domicilio Perceptor. |  | 36 |  | 576 | A/N | Domicilio del perceptor. |
| 73 | Códig. Postal Percep. |  | 5 |  | 612 | A/N | Código Postal del perceptor. |
| 74 | Localidad Perceptor. |  | 30 |  | 617 | A/N | Nombre de la localidad de residencia del perceptor. |
| 75 | Sistema de cobro. |  | 1 |  | 647 | A/N | Sistema de cobro de la pensión (76). |
| 76 | Entidad Bancaria. |  | 4 |  | 648 | A/N | Código de entidad bancaria conforme al Consejo Superior Bancario (77). |
| 77 | Agencia Bancaria. |  | 4 |  | 652 | A/N | Código de agencia bancaria conforme al Consejo Superior Bancario (78). |
| 78 | Número de cuenta. |  | 15 |  | 656 | A/N | Número de cuenta bancaria (79). |

Observaciones:

1. Los campos cuyo tipo sea numérico (N) se consignarán justificados a la derecha y rellenados por la izquierda a ceros.

2. Los campos cuyo tipo sea alfanumérico (A/N) se consignarán justificados a la izquierda y rellenados por la derecha a espacios excepto cuando se especifique el modo exacto en que deben ser consignados.

3. Se considerarán caracteres numéricos los siguientes: 0,1, 2, 3, 4, 5, 6, 7, 8, 9.

4. Si el número de convivientes es mayor que seis se registrarán en el ficho técnico prioritariamente aquéllos que posean ingresos.
