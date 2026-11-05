## ANEXO

<?xml version="1.0" encoding="UTF-8"?>

<!--

INSTANCIA DEL FORMATO XML DE INTERCAMBIO DE INFORMACIÓN CON NOTARIOS Y REGISTRADORES DE LA PROPIEDAD (NOTREG)

El presente documento XML es una instancia explicativa del XML Schema "notreg.xsd".

Este esquema utiliza los elementos definidos en el núcleo del lenguaje de descripción catastral XCAT contenido en el XML Schema "ldc.xsd".

Ambos se encuentran disponibles en:

http://www.catastro.meh.es/ws/esquemas/esquemas.htm

La correcta interpretación de todos los aspectos del formato implica consultar no sólo esta instancia, sino también el correspondiente XML Schema del formato y el XML Schema XCAT, en especial todo lo relacionado con las ocurrencias y restricciones de los diferentes elementos.

Para cada etiqueta, a su derecha, se indica su logitud máxima y formato.

Los formatos se denotan por:

X para los campos alfanuméricos

N para los numéricos (por ejemplo: 10,2 N para un numérico de 10 enteros máximo y 2 decimales)

AAAA-MM-DD para las fechas

HH:MM:SS para campos temporales

BINARIO: Para datos binarios adjuntos.

-->

<notreg xmlns="http://www.catastro.meh.es/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

<cab>

CABECERA

<ieg>

ENTIDAD GENERADORA DEL FICHERO

<teg>TIPO DE ENTIDAD GENERADORA N (NOTARÍAS), R (REGISTROS DE LA PROPIEDAD) (1 X)</teg>

<ceg>CÓDIGO DE LA ENTIDAD GENERADORA DEL FICHERO (Se elige una opción: Registro de la Propiedad, Código de Notaría o Gerencia del Catastro)

<rp>

REGISTRO DE LA PROPIEDAD

<cp>CÓDIGO DE PROVINCIA (2 X) </cp>

<crp>CÓDIGO DEL REGISTRO DE LA PROPIEDAD (3 X)</crp>

</rp>

<not>

<cp>CÓDIGO DE PROVINCIA (2 X)</cp>

<cpb>CÓDIGO DE POBLACIÓN (4 X)</cpb>

<cnt>CÓDIGO DE NOTARÍA (3 X)</cnt>

</not>

<cd>CÓDIGO DE DELEGACIÓN (2 X)</cd>

</ceg>

<neg>NOMBRE DE LA ENTIDAD GENERADORA ( 27 X)</neg>

</ieg>

<ifi>

INFORMACIÓN DEL FICHERO

<ffi>FECHA DE GENERACIÓN EL FICHERO (AAAA-MM-DD)</ffi>

<hfi>HORA DE GENERACIÓN DEL FICHERO (HH:MM:SS)</hfi>

<tfi>TIPO DE FICHERO, LITERAL "NRGE" (4 X)</tfi>

<dfi>DESCRIPCIÓN DEL FICHERO (39 X)</dfi>

<nfi>NOMBRE DEL FICHERO (Cumplimentado por la D.G.C.)(21 X)</nfi>

</ifi>

<iper>

INFORMACIÓN DEL PERÍODO

<fip>FECHA DE INICIO DEL PERÍODO (AAAA-MM-DD)</fip>

<ffp>FECHA DE FINALIZACIÓN DEL PERÍODO (AAAA-MM-DD)</ffp>

</iper>

<cubi>NÚMERO TOTAL DE BIENES INMUEBLES INCLUIDOS (7 N)</cubi>

</cab>

<luden>

LISTA DE UNIDADES DE DATOS DE ENTRADA

<udennr>UNIDAD DE DATOS DE ENTRADA (Dependiendo del tipo de alteración puede ser un movimiento físico económico (Tipos de alteración 2 ,3 ,4 5) ó jurídico (Tipos de alteración1,6). Existirá un elemento bicec (Movimiento físico económico) o bij (movimiento jurídico) por cada unidad de datos de entrada)

<bicec>

MOVIMIENTO FÍSICO ECONÓMICO (exitirá este elemento o el elemento bij)

<bi>

BIEN INMUEBLE

<idbis>IDENTIFICACIÓN DEL BIEN INMUEBLE (Según la presencia o ausencia de la referencia catastral (cumplimiento del art.40 TRLCI) existirá un elemento idbic o idbip)

<idbic>BIEN INMUEBLE CON REFERENCIA CATASTRAL (En cumplimiento del artículo 40 TRLCI, casos: 1 RC de la finca incorporada, 2 RC de la finca incorporada y dudosa, 3 Incorporada de la finca origen (40.2) )

<cn>CLASE DEL BIEN INMUEBLE (2 X)</cn>

<lrc>REFERENCIA CATASTRAL (20 X)</lrc>

<drc>CUMPLIMIENTO ARTÍCULO 40 TRLCI (Casos 1,2,3 anteriores) (1 X)</drc>

</idbic>

<idbip>BIEN INMUEBLE SIN REFERENCIA CATASTRAL (En cumplimiento del artículo 40 TRLCI, casos: 4 RC presentada no incorporada, 5 no se ha presentado RC)

<cn>CLASE DEL BIEN INMUEBLE (2 X)</cn>

<mar>CUMPLIMIENTO ARTÍCULO 40 TRLCI (Casos 4,5 anteriores) (1 X)</mar>

</idbip>

</idbis>

<idad>

INFORMACIÓN ADICIONAL DE IDENTIFICACIÓN

<nfr>

NÚMERO DE FINCA REGISTRAL

<rp>

REGISTRO DE LA PROPIEDAD

<cp>CÓDIGO DE PROVINCIA (2 X)</cp>

<crp>CÓDIGO DEL REGISTRO (3 X)</crp>

</rp>

<sc>SECCIÓN (2 X)</sc>

<fr>NÚMERO DE FINCA (6 X)</fr>

<sfr>NÚMERO DE SUBFINCA (6 X)</sfr>

</nfr>

</idad>

<dt>

DOMICILIO TRIBUTARIO

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 X)</np>

<nm>NOMBRE DE MUNICIPIO (40X)</nm>

<nem>NOMBRE DE LA ENTIDAD MENOR (30X)</nem>

<locs>

LOCALIZACIÓN SELECTIVA (Existirá sólo una de las dos posibles, la localización urbana completa, o la rústica

completa, siendo las dos iguales en sus elementos, no así en sus ocurrencias)

<lous>

LOCALIZACIÓN URBANA COMPLETA

<lourb>

LOCALIZACIÓN URBANA

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (3 X)</pu>

</loint>

<dp>CÓDIGO POSTAL (5 N)</dp>

</lourb>

<lorus>

LOCALIZACIÓN RÚSTICA

<cpp>

CÓDIGO POLÍGONO-PARCELA

<cpo>CÓDIGO DE POLÍGONO (3 N)</cpo>

<cpa>CÓDIGO DE PARCELA (5 N)</cpa>

</cpp>

<npa>NOMBRE DEL PARAJE (30 X)</npa>

</lorus>

</lous>

<lors>

LOCALIZACIÓN RÚSTICA COMPLETA

<lorus>

LOCALIZACIÓN RÚSTICA

<cpp>

CÓDIGO POLÍGONO-PARCELA

<cpo>CÓDIGO DE POLÍGONO (3 N)</cpo>

<cpa>CÓDIGO DE PARCELA (5 N)</cpa>

</cpp>

<npa>NOMBRE DEL PARAJE (30 X)</npa>

</lorus>

<lourb>

LOCALIZACIÓN URBANA

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (3 X)</pu>

</loint>

<dp>CÓDIGO POSTAL (5 N)</dp>

</lourb>

</lors>

</locs>

</dt>

<inrbi>

INFORMACIÓN PROPIA DEL BIEN INMUEBLE

<sup>SUPERFICIE EN METROS CUADRADOS (10 N)</sup>

<ciur>CLASE DE INMUEBLES URBANOS EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (2 X)</ciur>

<tcons>TIPOS DE CONSTRUCCIÓN EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (1 X)</tcons>

<tnfr>TIPOS DE NATURALEZA DE FINCA RÚSTICA EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (1 X)</tnfr>

</inrbi>

</bi>

<mov>

DATOS DEL MOVIMIENTO

<eoe>ENTIDAD ORIGEN (NT Notarios, RG Registradores de la Propiedad))</eoe>

<tal>TIPO DE ALTERACIÓN CATASTRAL (1 X) 2 Obra nueva en Construcción, 3 Obra nueva terminada, 4 Otras alteraciones catastrales, 5 Actos de naturaleza urbanística</tal>

<fac>FECHA DE ALTERACIÓN (AAAA-MM-DD)</fac>

<fhm>

FECHA Y HORA DEL MOVIMIENTO

<fm>FECHA DEL MOVIMIENTO (AAAA-MM-DD)</fm>

<hm>HORA DEL MOVIMIENTO (HH:MM:SS)</hm>

</fhm>

<inr>

INFORMACIÓN NOTARIAL

<npn>

NÚMERO DE PROTOCOLO NOTARIAL

<not>

NOTARÍA

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cpb>CÓDIGO DE POBLACIÓN (4 N)</cpb>

<cnt>CÓDIGO DE NOTARÍA (3 N)</cnt>

</not>

<pn>

PROTOCOLO NOTARIAL

<aprt>AÑO DEL PROTOCOLO (4 N)</aprt>

<prt>PROTOCOLO (6 N)</prt>

</pn>

</npn>

<pvd>PRECIO O VALOR DECLARADO DE TRANSMISIÓN (10,2 N)</pvd>

<imp>SUJECIÓN AL IMPUESTO (Según codificación del ICGN) (1 X)</imp>

<cgn>CLAVE DE OPERACIÓN NOTARIAL (Según codificación del ICGN) (8 X)</cgn>

</inr>

<dec>

DATOS DEL DECLARANTE

<idp>

IDENTIFICACIÓN

<nif>NIF (9 x)</nif>

<nom>APELLIDOS Y NOMBRE (60 X)</nom>

</idp>

<dfn>

DOMICILIO FISCAL DEL DECLARANTE

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 N)</np>

<nm>NOMBRE DE MUNICIPIO (40 N)</nm>

<nem>NOMBRE DE ENTIDAD MENOR (30 N)</nem>

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (4 X)</pu>

</loint>

<pos>

DATOS POSTALES

<dp>CÓDIGO POSTAL (5 N)</dp>

<ac>APARTADO DE CORREOS (5 N)</ac>

</pos>

</dfn>

</dec>

</mov>

</bicec>

<bij>

MOVIMIENTO JURÍDICO (exitirá este elemento o el elemento bicec)

<bi>

BIEN INMUEBLE

<idbis>

IDENTIFICACIÓN DEL BIEN INMUEBLE (Según la presencia o ausencia de la referencia catastral (cumplimiento del art.40 TRLC) existirá un elemento idbic o idbip)

<idbic>

BIEN INMUEBLE CON REFERENCIA CATASTRAL (En cumplimiento del artículo 40 TRLCI, casos: 1 RC de la finca incorporada, 2 RC de la finca incorporada y dudosa, 3 Incorporada de la finca origen (40.2) )

<cn>CLASE DEL BIEN INMUEBLE (2 X)</cn>

<lrc>REFERENCIA CATASTRAL (20 X)</lrc>

<drc>CUMPLIMIENTO ARTÍCULO 40 TRLCI (Casos 1,2,3 anteriores) (1 X)</drc>

</idbic>

<idbip>

BIEN INMUEBLE SIN REFERENCIA CATASTRAL (En cumplimiento del artículo 40 TRLCI, casos: 4 RC presentada no incorporada, 5 no se ha presentado RC)

<cn>CLASE DEL BIEN INMUEBLE (2 X)</cn>

<mar>CUMPLIMIENTO ARTÍCULO 40 TRLCI (Casos 4,5 anteriores) (1 X)</mar>

</idbip>

</idbis>

<idad>

INFORMACIÓN ADICIONAL DE IDENTIFICACIÓN

<nfr>

NÚMERO DE FINCA REGISTRAL

<rp>

REGISTRO DE LA PROPIEDAD

<cp>CÓDIGO DE PROVINCIA (2 X)</cp>

<crp>CÓDIGO DEL REGISTRO (3 X)</crp>

</rp>

<sc>SECCIÓN (2 X)</sc>

<fr>NÚMERO DE FINCA (6 X)</fr>

<sfr>NÚMERO DE SUBFINCA (6 X)</sfr>

</nfr>

</idad>

<dt>

DOMICILIO TRIBUTARIO

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 X)</np>

<nm>NOMBRE DE MUNICIPIO (40X)</nm>

<nem>NOMBRE DE LA ENTIDAD MENOR (30X)</nem>

<locs>

LOCALIZACIÓN SELECTIVA (Existirá sólo una de las dos posibles, la localización urbana completa, o la rústica

completa, siendo las dos iguales en sus elementos, no así en sus ocurrencias)

<lous>

LOCALIZACIÓN URBANA COMPLETA

<lourb>

LOCALIZACIÓN URBANA

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (3 X)</pu>

</loint>

<dp>CÓDIGO POSTAL (5 N)</dp>

</lourb>

<lorus>

LOCALIZACIÓN RÚSTICA

<cpp>

CÓDIGO POLÍGONO-PARCELA

<cpo>CÓDIGO DE POLÍGONO (3 N)</cpo>

<cpa>CÓDIGO DE PARCELA (5 N)</cpa>

</cpp>

<npa>NOMBRE DEL PARAJE (30 X)</npa>

</lorus>

</lous>

<lors>

LOCALIZACIÓN RÚSTICA COMPLETA

<lorus>

LOCALIZACIÓN RÚSTICA

<cpp>

CÓDIGO POLÍGONO-PARCELA

<cpo>CÓDIGO DE POLÍGONO (3 N)</cpo>

<cpa>CÓDIGO DE PARCELA (5 N)</cpa>

</cpp>

<npa>NOMBRE DEL PARAJE (30 X)</npa>

</lorus>

<lourb>

LOCALIZACIÓN URBANA

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (3 X)</pu>

</loint>

<dp>CÓDIGO POSTAL (5 N)</dp>

</lourb>

</lors>

</locs>

</dt>

<inrbi>

INFORMACIÓN PROPIA DEL BIEN INMUEBLE

<sup>SUPERFICIE EN METROS CUADRADOS (10 N)</sup>

<ciur>CLASE DE INMUEBLES URBANOS EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (2 X)</ciur>

<tcons>TIPOS DE CONSTRUCCIÓN EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (1 X)</tcons>

<tnfr>TIPOS DE NATURALEZA DE FINCA RÚSTICA EN TRANSMISIONES ONEROSAS (Según codificación del ICGN) (1 X)</tnfr>

</inrbi>

</bi>

<mov>

DATOS DEL MOVIMIENTO

<eoe>ENTIDAD ORIGEN (NT Notarios, RG Registradores de la Propiedad))</eoe>

<tal>TIPO DE ALTERACIÓN CATASTRAL (1 X) 1 Cambio de dominio simple sin alteración del bien, 6 Variaciones en la composición interna o cuota de participación de comunidades o entidades sin personalidad jurídica</tal>

<fac>FECHA DE ALTERACIÓN (AAAA-MM-DD)</fac>

<fhm>

FECHA Y HORA DEL MOVIMIENTO

<fm>FECHA DEL MOVIMIENTO (AAAA-MM-DD)</fm>

<hm>HORA DEL MOVIMIENTO (HH:MM:SS)</hm>

</fhm>

<inr>

INFORMACIÓN NOTARIAL

<npn>

NÚMERO DE PROTOCOLO NOTARIAL

<not>

NOTARÍA

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cpb>CÓDIGO DE POBLACIÓN (4 N)</cpb>

<cnt>CÓDIGO DE NOTARÍA (3 N)</cnt>

</not>

<pn>

PROTOCOLO NOTARIAL

<aprt>AÑO DEL PROTOCOLO (4 N)</aprt>

<prt>PROTOCOLO (6 N)</prt>

</pn>

</npn>

<pvd>PRECIO O VALOR DECLARADO DE TRANSMISIÓN (10,2 N)</pvd>

<imp>SUJECIÓN AL IMPUESTO (Según codificación del ICGN) (1 X)</imp>

<cgn>CLAVE DE OPERACIÓN NOTARIAL (Según codificación del ICGN) (8 X)</cgn>

</inr>

<dec>

DATOS DEL DECLARANTE (opcional)

<idp>

IDENTIFICACIÓN

<nif>NIF (9 x)</nif>

<nom>APELLIDOS Y NOMBRE (60 X)</nom>

</idp>

<dfn>

DOMICILIO FISCAL DEL DECLARANTE

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 N)</np>

<nm>NOMBRE DE MUNICIPIO (40 N)</nm>

<nem>NOMBRE DE ENTIDAD MENOR (30 N)</nem>

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (4 X)</pu>

</loint>

<pos>

DATOS POSTALES

<dp>CÓDIGO POSTAL (5 N)</dp>

<ac>APARTADO DE CORREOS (5 N)</ac>

</pos>

</dfn>

</dec>

</mov>

<lsf>

SITUACIÓN FINAL DE TITULARIDAD (Adquirentes)

<ltit>

LISTA DE TITULARES

<tit>

TITULAR

<der>

DERECHO

<cdr>CÓDIGO DE DERECHO ( PR : Propiedad plena, NP: Nuda propiedad, US : Usufructo, CA : Concesión administrativa, DS : Derecho de superficie (2 X)</cdr>

<pct>PORCENTAJE (3,2 N)</pct>

</der>

<ord>ORDINAL DEL DERECHO (secuencial del derecho del titular sobre el bien) (3 N)</ord>

<idpa>

IDENTIFICACIÓN (Se hará constar el NIF o el motivo de su ausencia)

<nif>NIF (9 X)</nif>

<anif>MOTIVO DE AUSENCIA DE NIF (1 N)</anif>

<nom>APELLIDOS Y NOMBRE (60 X)</nom>

</idpa>

<df>

DOMICILIO FISCAL

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 N)</np>

<nm>NOMBRE DE MUNICIPIO (40 N)</nm>

<nem>NOMBRE DE ENTIDAD MENOR (30 N)</nem>

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (4 X)</pu>

</loint>

<pos>

DATOS POSTALES

<dp>CÓDIGO POSTAL (5 N)</dp>

<ac>APARTADO DE CORREOS (5 N)</ac>

</pos>

</df>

<iatit>

INFORMACIÓN ADICIONAL DE TITULARIDAD

<nifcy>NIF DEL CÓNYUGE (9 X)</nifcy>

<nifcb>NIF DE LA COMUNIDAD DE BIENES (9 X)</nifcb>

<ct>COMPLEMENTO DE TITULARIDAD (20 X)</ct>

</iatit>

</tit>

</ltit>

<lcbi>

LISTA DE COMUNIDADES DE BIENES

<cbi>

COMUNIDAD DE BIENES

<idcbf>

IDENTIFICACIÓN DE LA COMUNIDAD DE BIENES

<nifcb>NIF DE LA COMUNIDAD DE BIENES (9 X)</nifcb>

<nomcb>DENOMINACIÓN O RAZÓN SOCIAL DE LA COMUNIDAD DE BIENES (60 X)</nomcb>

</idcbf>

<df>

DOMICILIO FISCAL

<loine>

LOCALIZACIÓN INE

<cp>CÓDIGO DE PROVINCIA (2 N)</cp>

<cm>CÓDIGO DE MUNICIPIO (3 N)</cm>

</loine>

<np>NOMBRE DE PROVINCIA (25 N)</np>

<nm>NOMBRE DE MUNICIPIO (40 N)</nm>

<nem>NOMBRE DE ENTIDAD MENOR (30 N)</nem>

<dir>

DIRECCIÓN

<cv>LITERAL "NOAPL" (no aplicable) (5 X)</cv>

<tv>TIPO DE VÍA (5 X)</tv>

<nv>NOMBRE DE VÍA (25X)</nv>

<pnp>PRIMER NÚMERO DE POLICÍA (4 N)</pnp>

<plp> LETRA ASOCIADA AL PRIMER NÚMERO DE POLICÍA (1 X)</plp>

<snp>SEGUNDO NÚMERO DE POLICÍA (4 N)</snp>

<slp> LETRA ASOCIADA AL SEGUNDO NÚMERO DE POLICÍA (1 X)</slp>

<km> KILÓMETRO (5 N)</km>

<td>TEXTO DE DIRECCIÓN NO ESTRUCTURADA (25 X)</td>

</dir>

<loint>

LOCALIZACIÓN INTERNA

<bq>BLOQUE (4 X)</bq>

<es>ESCALERA (2 X)</es>

<pt>PLANTA (3 X)</pt>

<pu>PUERTA (4 X)</pu>

</loint>

<pos>

DATOS POSTALES

<dp>CÓDIGO POSTAL (5 N)</dp>

<ac>APARTADO DE CORREOS (5 N)</ac>

</pos>

</df>

</cbi>

</lcbi>

</lsf>

<lsi>

SITUACIÓN INICIAL DE TITULARIDAD (Transmitentes)

<tit>

TITULAR

<der>

DERECHO

<cdr>CÓDIGO DE DERECHO ( PR : Propiedad plena, NP: Nuda propiedad, US : Usufructo, CA : Concesión administrativa, DS : Derecho de superficie (2 X)</cdr>

<pct>PORCENTAJE (3,2 N)</pct>

</der>

<idpa>

IDENTIFICACIÓN (Se hará constar el NIF o el motivo de su ausencia)

<nif>NIF (9 X)</nif>

<anif>MOTIVO DE LA AUSENCIA DE NIF (1 N)</anif>

<nom>APELLIDOS Y NOMBRE (60 X)</nom>

</idpa>

</tit>

</lsi>

</bij>

</udennr>

</luden>

</notreg>

> Se modifica por el anejo.1 y anexo de la Resolución de 7 de agosto de 2006. Ref. BOE-A-2006-15050.

> Se modifica por el anejo.1 y anexo de la Resolución de 5 de febrero de 2004. Ref. BOE-A-2004-2656.
