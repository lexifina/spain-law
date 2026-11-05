## ANEXO I

## Formato y especificaciones de los archivos de comunicación de datos

1. Juego de caracteres: ISO/IEC - 8859 - 1 («latin alphabet – 1»).

2. Formato: conforme con XML 1.0 (W3C Recommendation de 4 de febrero de 2004).

3. Estructura y codificación del archivo a remitir.

3.1 Adjudicaciones de contratos.

Este esquema se utilizará para enviar información relativa a adjudicaciones de contratos. Se podrán notificar tantos contratos como se deseen en un único archivo. Únicamente se tendrá que repetir tantas veces como contratos se envíen los datos comprendidos entre las etiquetas <contrato...> y </contrato>.

En caso necesario, dentro de cada contrato se podrán introducir los datos de más de un adjudicatario, repitiendo la información comprendida entre las etiquetas <contratista...> y </contratista>.

## Estructura del fichero

<?xml version="1.0" encoding="iso-8859-1"?> <dgp_sitt_schema anio="Año del contrato"> <cabecera> <usuario> <nombre>Nombre del usuario que envía la información </nombre> <apellido1>Primer apellido del usuario </apellido1> <apellido2>Segundo apellido del usuario </apellido2> <cargo>Cargo del usuario</cargo> <direccion>Dirección postal del organismo</direccion> <provincia>Codigo de la provincia (Tabla 5)</provincia> <municipio>Código del municipio (Tabla 7)</municipio> <codPostal>Código postal</codPostal> <telefono>Número de teléfono</telefono> <fax>Número de Fax</fax> <mail>Correo electrónico</mail> </usuario> <RegistrosEnviados>Número de contratos que se envian en la remesa</RegistrosEnviados> <tipoAdmin>Código de tipo de Administración (Tabla 1)</tipoAdmin> <tipoAdminLocal>Código de tipo de Administración Local (Tabla 2) Sólo si los contratos son de una Entidad Local</tipoAdminLocal> </cabecera> <enteContratante codEnteContratante="nnnnnnnn" nombreEnteContratante="nombre de la Administración pública o Entidad contratante" (Nota 1)> <departamento codigoDepartamento="nn" (Código del Ministerio, Consejería o Departamento asignado en los Presupuestos del año del contrato)nombreDepartamento="nombre Ministerio, Consejería o Departamento" (Nota 2)> <organoContratante codigoOrganoContratante="xxxxx" nombreOrganoContratante="nombre del órgano, organismo o ente contratante" (Nota 3)> <contrato numero="numero de contrato"> <tipoContrato>Tipo de contrato (Tabla 9)</tipoContrato> <provincia>Código de la provincia donde se realiza el contrato (Tabla 5) </provincia> <modalidad>Sólo en los contratos tipos B (Tabla 10)</modalidad> <objeto> objeto del contrato </objeto> <codigoCpa>Código Cpa del objeto del contrato (6 dígitos) </codigoCpa> <caracteristicaBienes>Solo en los contratos tipo C (Tabla 11)</caracteristicaBienes> <conMixto>si/no.No aplica en los contratos tipo F o I </conMixto> <conMarco>si/no. No aplica en los contratos tipo B, F o I </conMarco> <complementario>si/no. Sólo aplica en contratos tipo D</complementario> <publicidad>si/no</publicidad> <anuncioBoe>Fecha anuncio Boletín Oficial del Estado</anuncioBoe> <anuncioDOUE>Fecha anuncio Diario Oficial Unión Europea </anuncioDOUE> <anuncioBoca>Fecha anuncio Boletín Oficial Comunidad Autónoma </anuncioBoca> <anuncioBop>Fecha anuncio Boletín Oficial de la Provincia </anuncioBop> <tramite>Tipo de tramitación del expediente (Tabla 12)</tramite> <procedimientoAdjud>Procedimiento de adjudicación (Tabla 13)</procedimientoAdjud> <procNegArticulo>Artículo y apartado de la LCAP por el que se aplica procedimiento negociado</procNegArticulo> <procNegSubapartado>Subapartado de la LCAP por el que se aplica procedimiento negociado </procNegSubapartado> <invitaciones>Número de invitaciones </invitaciones> <formaAdjud>Forma de adjudicación (tabla 14)</formaAdjud> <importePresupuesto>Importe presupuesto licitación (en euros, sin puntuación ni decimales)</importePresupuesto> <plazo>De ejecución en meses</plazo> <plazoConcesion>en meses, sólo en los contratos de tipos B o H </plazoConcesion> <plurianual>Si/no</plurianual> <anualidad1>Importe para la primera anualidad, sin puntuación ni decimales </anualidad1> <anualidad2>Importe para la segunda anualidad, sin puntuación ni decimales </anualidad2> <anualidad3>Importe para la tercera anualidad, sin puntuación ni decimales</anualidad3> <anualidad4>Importe para la cuarta anualidad, sin puntuación ni decimales </anualidad4> <anualidad5>Importe para la quinta anualidad, sin puntuación ni decimales </anualidad5> <revisionPrecios>Si/no </revisionPrecios> <formulaTipo>Numero que identifica la fórmula tipo de revisión de precios aplicada (sólo para contratos de obras)</formulaTipo> <contratista nif="Nif del contratista"> <descripcion>Nombre del contratista </descripcion> <nacionalidad>Nacionalidad del contratista</nacionalidad> </contratista> <paisOrigen>Código ISO del pais de origen de los productos, en los contratos de suministro</paisOrigen> <fechaAdjudicacion>Fecha de adjudicación</fechaAdjudicacion> <importeAdjudicacion>Importe de adjudicación (en euros, sin decimales ni puntuación)</importeAdjudicacion> <esIngreso>si/no (Sólo en contratos tipo I)</esIngreso> <modalidadImporte>Sólo en contratos tipo B o H (Tabla 15)</modalidadImporte> <valorModalidad>Sólo en contratos tipo B o H</valorModalidad> <unidadModalidad>Sólo en contratos tipo B o H</unidadModalidad> <aportacionAdministracion>Sólo en contratos tipo B o H</aportacionAdministracion> <fechaFormalizacion>Fecha de formalización del contrato </fechaFormalizacion> <observaciones>Observaciones</observaciones> </contrato> </organoContratante> </departamento> </enteContratante> </dgp_sitt_schema>

3.2 Modificaciones, prórrogas y resoluciones de contratos.

Este esquema se utilizará para enviar información relativa a las modificaciones, prórrogas y resoluciones de contratos cuya adjudicación ya fue comunicada. Se podrán notificar tantos contratos como se deseen en un único archivo. Únicamente se tendrá que repetir tantas veces como contratos se envíen los datos comprendidos entre las etiquetas <contrato...> y </contrato>.

## Estructura del fichero

<?xml version="1.0" encoding="iso-8859-1"?> <dgp_sitt_schema anio="Año del contrato"> <cabecera> <usuario> <nombre>Nombre del usuario que envía la información </nombre> <apellido1>Primer apellido del usuario </apellido1> <apellido2>Segundo apellido del usuario </apellido2> <cargo>Cargo del usuario</cargo> <direccion>Dirección postal del organismo</direccion> <provincia>Codigo de la provincia (Tabla 5)</provincia> <municipio>Código del municipio (Tabla 7)</municipio> <codPostal>Código postal</codPostal> <telefono>Número de teléfono</telefono> <fax>Número de Fax</fax> <mail>Correo electrónico</mail> </usuario> <RegistrosEnviados>Número de contratos que se envian en la remesa</RegistrosEnviados> <tipoAdmin>Código de tipo de Administración (Tabla 1)</tipoAdmin> <tipoAdminLocal>Código de tipo de Administración Local (Tabla 2) Sólo si los contratos son de una Entidad Local</tipoAdminLocal> </cabecera> <enteContratante codEnteContratante="nnnnnnnn" nombreEnteContratante="nombre de la Administración pública o Entidad contratante" (Nota 1)> <departamento codigoDepartamento="nn" (Código del Ministerio, Consejería o Departamento asignado en los Presupuestos del año del contrato) nombreDepartamento="nombre Ministerio, Consejería o Departamento"(Nota 2)> <organoContratante codigoOrganoContratante="xxxxx" nombreOrganoContratante="nombre del órgano, organismo o ente contratante" (Nota 3)> <modificacionContrato numero="Número del contrato" numeroMod="Número de la modificación"> <articuloAplicado>Artículo LCAP aplicado en la resolución si la hubiere </articuloAplicado> <apartadoAplicado>Apartado LCAP aplicado en la resolución si la hubiere</apartadoAplicado> <causaResolucion>Motivo de la resolución si la hubiere</causaResolucion> <fechaAcuerdoRes>Fecha acuerdo resolución</fechaAcuerdoRes> <modifImporte>Importe de todas las modificaciones realizadas </modifImporte> <modifPlazo>Incremento total de plazo por todas las modificaciones realizadas</modifPlazo> <perdidaGarantia>si/no</perdidaGarantia> <resolucionContrato>si/no</resolucionContrato> </modificacionContrato> </organoContratante> </departamento> </enteContratante> </dgp_sitt_schema>

3.3 Reglas de cumplimentación.

| Dato | Tipo, tamaño y reglas de cumplimentación |
| --- | --- |
| Anio | Numérico de 4 dígitos. |
| Nombre | Alfanumérico de 50 posiciones. |
| Apellido1 | Alfanumérico de 50 posiciones. |
| Apellido2 | Alfanumérico de 50 posiciones. |
| Cargo | Texto libre de 100 posiciones. |
| Direccion | Alfanumérico de 50 posiciones. |
| Provincia | Numérico de 2 dígitos, compuesto según la codificación oficial del Instituto Nacional de Estadística. |
| Municipio | Numérico de 4 dígitos, compuesto según la codificación oficial del Instituto Nacional de Estadística. |
| CodPostal | Numérico de 5 dígitos. |
| Telefono | Numérico de 9 dígitos. |
| Fax | Numérico de 9 dígitos. |
| Mail | Alfanumérico de 50 posiciones. |
| tipoAdmin | Tipo de Administración o entidad contratante (Tabla 1). |
| tipoAdminLocal | Tipo de Administración Local contratante (Tabla 2). |
| enteContratante | Ver Nota 1. |
| departamento | Ver Nota 2. |
| OrganoContratante | Ver Nota 3. |
| Numero de contrato | Alfanumérico de 30 posiciones, permitiendo introducir además los siguientes caracteres: / - _ ( ) Objeto: Texto libre de 120 posiciones. |
| CodigoCpa | Numérico de 6 posiciones como máximo. |
| Fechas | aaaa-mm-dd (10 posiciones). |
| Importes | Numérico de 10 posiciones, sin puntuación ni decimales. |
| Plazo | Numérico de 4 posiciones. |
| PlazoConcesion | Numérico de 4 posiciones. |
| Plurianual | Alfabético de 2 posiciones (si/no). |
| RevisionPrecios | Alfabético de 2 posiciones (si/no). |
| FormulaTipo | Numérico de 2 posiciones. |
| ConMixto | Alfabético de 2 posiciones (si/no) |
| ConMarco | Alfabético de 2 posiciones (si/no) |
| Complementario | Alfabético de 2 posiciones (si/no) |
| Publicidad | Alfabético de 2 posiciones (si/no) |
| ProcNegArticulo | Alfanumérico de 5 posiciones: nnn.n |
| ProcNegSubapartado | Alfanumérico de 2 posiciones |
| Invitaciones | Numérico de 4 posiciones |
| ValorModalidad | Numérico de 10 posiciones sin puntuación ni decimales. |
| UnidadModalidad | Alfanumérico de 12 posiciones. |
| AportacionAdministracion | Texto libre de 50 posiciones. |
| Observaciones | Texto libre de 120 posiciones. |
| País | Código alfabético de 2 posiciones, según norma ISO-3166-1:1997. (código de España = es). |
| Datos Contratistas: |  |
| Nif: | Carácter de 9 posiciones. |
| Descripcion | Carácter de 120 posiciones. |
| Nacionalidad | Código alfabético del país, de 2 posiciones, según norma ISO3166-1:1997. (código de España = es). |

3.4. Tablas.

## Tabla 1. Tipo de administración

| Código | Tipo |
| --- | --- |
| 1 | Órgano Constitucional |
| 2 | Estado |
| 3 | CCAA |
| 4 | Entidad Local |
| 5 | Otros |

## Tabla 2. Tipo de administración local

| Código | Tipo |
| --- | --- |
| A | Ayuntamiento |
| C | Cabildo / Consell Insular |
| D | Diputación Provincial/Foral |
| M | Mancomunidad |
| X | Consorcio |

## Tabla 3. Órganos constitucionales

| Código | Órgano |
| --- | --- |
| 0100001 | CASA S.M. EL REY |
| 0200001 | CORTES GENERALES |
| 0200002 | CONGRESO DE LOS DIPUTADOS |
| 0200003 | SENADO |
| 0200004 | JUNTA ELECTORAL CENTRAL |
| 0200005 | DEFENSOR DEL PUEBLO |
| 0300001 | TRIBUNAL DE CUENTAS |
| 0400001 | TRIBUNAL CONSTITUCIONAL |
| 0500001 | CONSEJO DE ESTADO |
| 0800001 | CONSEJO GRAL DEL PODER JUDICIAL |

## Tabla 4. Comunidades Autónomas

| Código | Comunidad Autónoma |
| --- | --- |
| 01 | ANDALUCÍA |
| 02 | ARAGÓN |
| 03 | ASTURIAS |
| 04 | ILLES BALEARS |
| 05 | CANARIAS |
| 06 | CANTABRIA |
| 07 | CASTILLA-LA MANCHA |
| 08 | CASTILLA-LEON |
| 09 | CATALUÑA |
| 10 | EXTREMADURA |
| 11 | GALICIA |
| 12 | MADRID |
| 13 | MURCIA |
| 14 | NAVARRA |
| 15 | PAÍS VASCO |
| 16 | RIOJA |
| 17 | COMUNIDAD VALENCIANA |
| 18 | CEUTA |
| 19 | MELILLA |

## Tabla 5. Provincias/diputaciones provinciales y forales

Se usarán los códigos numéricos de 2 dígitos asignados por el Instituto Nacional de Estadística para la codificación de las provincias.

## Tabla 6. Cabildos/Consells

| Código | Cabildo/Consell |
| --- | --- |
| 07006 | CONSELL INSULAR IBIZA Y FORMENTERA |
| 07008 | CONSELL INSULAR MALLORCA |
| 07009 | CONSELL INSULAR MENORCA |
| 35002 | CABILDO FUERTEVENTURA |
| 35004 | CABILDO GRAN CANARIA |
| 35007 | CABILDO LANZAROTE |
| 38003 | CABILDO GOMERA, LA |
| 38005 | CABILDO HIERRO, EL |
| 38010 | CABILDO PALMA, LA |
| 38011 | CABILDO TENERIFE |

## Tabla 7. Ayuntamientos/municipios

Para la cumplimentación del campo «municipio» se usarán los códigos numéricos de 4 dígitos asignados por el Instituto Nacional de Estadística para la codificación de los municipios.

En el caso de contratos adjudicados por un Ayuntamiento, el campo «ayuntamiento» se formará con los 2 dígitos del código de la provincia seguidos de los 4 dígitos del código del municipio.

## Tabla 8. Mancomunidades

Código alfanumérico de 8 posiciones, todas ellas obligatorias. El código estará formado por el número de registro en el R.E.L.

## Tabla 9. Tipo de contrato

| Código | Tipo |
| --- | --- |
| A | Obras |
| B | Gestión de servicios públicos |
| C | Suministros |
| D | Consultoría y asistencia |
| E | Servicios |
| F | Administrativos especiales |
| G | Sectores agua, energía, transportes y comunicaciones |
| H | Concesión Obras públicas |
| I | Privados |

## Tabla 10. Modalidad

| Código | Modalidad |
| --- | --- |
| C | (Concesión) |
| G | (Gestión Interesada) |
| M | (Concierto o sociedad de economía mixta) |

## Tabla 11. Características de los bienes

| Código | Significado |
| --- | --- |
| 1 | Entrega sucesiva y por precio unitario (Art. 172.1.a) |
| 2 | (Equipos, sistemas y programas TIC (Art. 172.1.b)) |
| 3 | (Suministro de Fabricación (Art. 172.1.c)) |
| 4 | (Otros) |

## Tabla 12. Trámite

| Código | Trámite |
| --- | --- |
| O | (Ordinario) |
| U | (Urgente) |
| E | (Emergencia) |

## Tabla 13. Procedimiento adjudicación

| Código | Procedimiento |
| --- | --- |
| A | (Abierto) |
| R | (Restringido) |
| N | (Negociado) |

## Tabla 14. Forma adjudicación

| Código | Forma adjudicación |
| --- | --- |
| C | (Concurso) |
| S | (Subasta) |
| N | (Otras) |

## Tabla 15. Modalidad importe

| Código | Modalidad |
| --- | --- |
| C | (Canon Global) |
| T | (Tarifas) |
| P | (Precios Unitarios) |

3.5 Notas.

Nota 1. enteContratante.

codEnteContratante: código de la Administración pública o Entidad contratante, de acuerdo con la tabla de códigos que corresponda por su naturaleza o tipo (Tablas 3 a 8).

En el caso de la Administración General del Estado, se asignará el valor "0".

En el caso de Mancomunidades o Consorcios, se asignará su código en el Registro de Entidades Locales.

En el caso de empresas, se asignará su CIF, prescindiendo de la letra.

nombreEnteContratante: se incorporará la denominación oficial de la Administración pública o Entidad contratante. En el caso de órganos de la Administración General del Estado, se tomará el valor "Estado".

Nota 2. departamento.

Sólo aplicable a la Administración General del Estado y a las de las Comunidades Autónomas.

Para cada Ministerio, Departamento o Consejería se usará la codificación asignada en los respectivos presupuestos anuales y su denominación oficial.

Nota 3. organoContratante.

Aplicable a todos los casos.

Se usará la codificación y denominación oficiales que en cada caso corresponda.

Si la Entidad que notifica los contratos sólo tiene un órgano contratante, se podrá asignar, por defecto, el valor "1" al atributo codigoOrganoContratante.
