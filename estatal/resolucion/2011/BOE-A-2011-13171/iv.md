## IV. Reglas de confianza

IV.1 Reglas de confianza para los certificados electrónicos.

1. Las políticas de firma, marco o particulares, podrán fijar limitaciones y restricciones específicas para los certificados electrónicos que admiten en cada uno de los servicios que corresponda, siempre en consideración de la normativa aplicable en cada caso.

2. Los certificados válidos para ejecutar la firma electrónica de contenido serán los siguientes:

a) Cualquier certificado electrónico reconocido según la Ley 59/2003, de 19 de diciembre, y la Directiva 1999/93/CE, de 13 de diciembre de 1999.

b) Nuevas tipologías de certificados definidos en la Ley 11/2007, de 22 de junio.

3. Los requisitos a cumplir por los prestadores de servicios de certificación en relación con la interoperabilidad organizativa, semántica y técnica serán los establecidos en el artículo 21 de la Ley 11/2007, de 22 de junio, en el artículo 19 del Real Decreto 4/2010, de 8 de enero, y en el resto de normativa aplicable en cada caso.

4. La relación de prestadores de servicios de certificación que emiten certificados reconocidos se podrá consultar en la TSL (Lista de servicios de confianza) publicada en la sede electrónica del Ministerio de Industria, Turismo y Comercio.

5. La política de firma electrónica podrá establecer el período de precaución o de gracia que corresponda aplicar para la validación de los certificados. Este periodo podrá ser, desde el momento en que se realiza la firma o el sellado de tiempo, como mínimo, el tiempo máximo permitido para el refresco completo de las CRLs (Certificate Revocation Lists) o el tiempo máximo de actualización del estado del certificado en el servicio OCSP (Online Certificate Status Protocol). Esta definición tendrá en cuenta también la posibilidad de que estos tiempos varíen según el Prestador de Servicios de Certificación.

6. El verificador validará los certificados electrónicos en base a los procesos de validación y archivado definidos en la política de firma a la que se ajuste el servicio en cada caso.

IV.2 Reglas de confianza para sellos de tiempo.

1. Los elementos básicos de un sello digital de tiempo serán:

a) Datos sobre la identidad de la autoridad emisora del sello: identidad jurídica, clave pública a utilizar en la verificación del sello, número de bits de la clave, algoritmo de firma digital y función hash utilizados.

b) Tipo de solicitud cursada. Incluyendo, si es un valor resumen o un documento, cuál es su valor y datos de referencia.

c) Valores resumen «anterior», «actual» y «siguiente».

d) Fecha y hora UTC (Universal Time Coordinated).

e) Firma electrónica de todo lo anterior.

2. El sellado de tiempo y la información de validación podrán ser añadidos por el emisor, el receptor o un tercero y se incluirán como propiedades no firmadas en los campos correspondientes según el formato de firma utilizado.

3. En la política de firma se establecerán las condiciones según las que determinar los sellos de tiempo admitidos atendiendo a sus necesidades particulares, y en base a la normativa y legislación vigente. Esto incluye el establecimiento del tiempo máximo aceptable para realizar el sellado de tiempo, anterior, en cualquier caso, a la caducidad del certificado.

4. Los sellos de tiempo seguirán las especificaciones técnicas establecidas en el estándar ETS’ TS 102 023, «Electronic Signatures and Infrastructures (ESI); Policy requirements for time-stamping authorities».

IV.3 Reglas de confianza para firmas longevas.

1. En el caso de firmas longevas, el firmante o el verificador de la firma incluirá un sello de tiempo que permita garantizar que el certificado era válido en el momento en que se realizó la firma. En el caso de que sea incluida por el firmante, se podrá realizar una vez haya trascurrido el periodo de precaución o periodo de gracia.

2. Para la conversión de una firma electrónica a firma electrónica longeva:

a) Se verificará la firma electrónica producida o verificada, validando la integridad de la firma, el cumplimiento de los estándares XAdES, CAdES o PAdES y las referencias.

b) Se realizará un proceso de completado de la firma electrónica que consistirá en la obtención y almacenamiento de las referencias a:

i. Certificados: incluyendo los certificados del firmante y de la cadena de certificación.

ii. Informaciones de estado de los certificados, CRLs o las respuestas OCSP.

c) Aplicación del sellado a las referencias a los certificados y a las informaciones de estado.

3. Para la incorporación a la firma de la información completa de validación, se usará validación mediante CRLs u OCSP.

4. Las políticas de firma contemplarán la definición de formatos y consideraciones de uso de firmas longevas conforme a las necesidades específicas de su ámbito de aplicación y a la normativa específica aplicable.
