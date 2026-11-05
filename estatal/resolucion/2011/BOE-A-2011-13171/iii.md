## III. Reglas comunes

III.1 Reglas comunes.

1. Las reglas comunes permitirán establecer responsabilidades respecto a la firma electrónica sobre la persona o entidad que crea la firma y la persona o entidad que la verifica, definiendo los requisitos mínimos que deben presentarse, debiendo estar firmados si son requisitos para el firmante, o no firmados si son requisitos para el verificador.

2. Estas reglas se definirán en base a los formatos de firma electrónica admitidos, teniendo en cuenta los diferentes usos de la firma electrónica basada en certificados, al uso de algoritmos y a los procesos de creación y validación de firma.

III.2 Formatos admitidos de firma electrónica.

1. Los formatos admitidos por las organizaciones para las firmas electrónicas basadas en certificados electrónicos, se ajustarán a las especificaciones de los estándares europeos relativos a los formatos de firma electrónica así como a lo establecido en la NTI de Catálogo de estándares.

2. Los formatos de firma electrónica serán:

a) Estándares abiertos basados en estándares de firma europeos y ampliamente utilizados.

b) Seleccionados de entre los definidos por la Comisión Europea para la política de interoperabilidad de firmas electrónicas que será regulada a través de Decisión Comunitaria.

c) Compatibles con la definición de políticas de generación y validación de firmas para facilitar la interoperabilidad deseada y el automatismo en el tratamiento de firmas electrónicas generadas por distintas organizaciones.

d) Tales que permitan desarrollar funcionalidades avanzadas como la generación de firmas longevas de cara a garantizar su preservación.

e) Si procede, interoperables con la política marco en la que se basan.

3. Cada organización determinará los formatos y estructuras concretas de firma a incluir en su política, aplicando los criterios expuestos en esta NTI de forma proporcional al uso y necesidades de la firma electrónica en cada caso.

4. Cada organización identificará a la entidad gestora encargada de publicar y actualizar la relación de las especificaciones relativas a los formatos admitidos en su política.

5. La política de firma incluirá los requisitos o, en su caso, procedimientos de actualización, para considerar la inclusión de nuevas versiones de los formatos soportados.

III.3 Formatos de firma electrónica de transmisiones de datos.

1. La firma electrónica de transmisiones de datos estará basada en estándares recogidos en la NTI de Catálogo de estándares, siendo responsabilidad del emisor y gestor de la política la definición de las consideraciones concretas a aplicar por cada organización.

2. Cada política definirá las versiones soportadas así como los cambios en aquellas que pueden provocar una actualización de dicha política.

III.4 Formatos de firma electrónica de contenido.

1. En la política de firma se especificarán los formatos admitidos para la firma electrónica de contenido.

2. Los formatos para la firma electrónica de contenido, atendiendo a la NTI de Catálogo de estándares, serán:

a) XAdES (XML Advanced Electronic Signatures), según la especificación técnica ETSI TS 101 903, versión 1.2.2 y versión 1.3.2.

b) CAdES (CMS Advanced Electronic Signatures), según la especificación técnica ETSI TS 101 733, versión 1.6.3 y versión 1.7.4.

c) PAdES (PDF Advanced Electronic Signatures), según la especificación técnica ETSI TS 102 778-3.

3. El perfil mínimo de formato que se utilizará para la generación de firmas de contenido en el marco de una política será «-EPES», esto es, clase básica (BES) añadiendo información sobre la política de firma. En cualquier caso, cada organización podrá definir en su política de firma las consideraciones adicionales que considere respecto a la interpretación y utilización de diferentes perfiles y clases de los formatos siempre en consonancia con lo establecido en esta NTI.

4. Las organizaciones aplicarán consideraciones de casos particulares para firma de contenido, al menos, en los siguientes casos:

a) Los documentos electrónicos a los que se aplique firma basada en certificados de cara a su intercambio se ajustarán a las especificaciones de formato y estructura establecidas en la NTI de Documento electrónico.

El formato de firma basada en certificados que acompaña a un documento electrónico se reflejará en el metadato mínimo obligatorio definido en la NTI de Documento electrónico `Tipo de firma’, que, en este caso, podrá tomar uno de los siguientes valores:

i. XAdES internally detached signature. XAdES enveloped signature.

iii. CAdES detached/explicit signature.

iv. CAdES attached/implicit signature.

v. PAdES.

b) La firma de facturas electrónicas según el formato «Facturae» se realizará conforme a lo regulado por la Orden PRE/2971/2007, de 5 de octubre.

III.5 Reglas de uso de algoritmos.

1. La política de firma especificará las reglas de uso de algoritmos en los diferentes formatos así como la longitud de las claves asociadas a aquéllos de forma proporcional a las necesidades detectadas en los diferentes usos de la firma electrónica, cumpliendo en cualquier caso lo establecido en la NTI de Catálogo de estándares.

2. Para los entornos de seguridad genérica se tomará la referencia a la URN (Uniform Resource Name) en la que se publican las funciones hash y los algoritmos de firma utilizados por las especificaciones XAdES, CAdES y PAdES, como formatos de firma adoptados, de acuerdo con las especificaciones técnicas ETS’ TS 102 176-1, «Electronic Signatures and Infrastructures (ESI); Algorithms and Parameters for Secure Electronic Signatures; Pan 1: Hash functions and asymmetric algorithms». Todo ello sin perjuicio de los criterios que al respecto se establezcan atendiendo al Real Decreto 3/2010, de 8 de enero.

3. Se admitirán como válidos los algoritmos de generación de hash, codificación en base64, firma, normalización y transformación definidos en los estándares XML-DSig (XML Digital Signature) y CMS (Cryptographic Message Syntax).

4. Para los entornos de alta seguridad, de acuerdo con el criterio del Centro Criptológico Nacional (CCN) serán de aplicación las recomendaciones revisadas de la CCN-STIC 405 así como en la norma CCN-STIC 807 del Esquema Nacional de Seguridad relativa al uso de criptografía.

5. La definición de usos de algoritmos podrá contemplar diferentes posibilidades según las necesidades en cada caso.

III.6 Reglas de creación de firma electrónica.

1. Las políticas de firma definirán las condiciones particulares bajo las que, en su ámbito, se generará la firma electrónica.

2. Las plataformas que presten el servicio de creación de firma electrónica proporcionarán las funcionalidades necesarias para soportar un proceso de creación de firmas basado en los siguientes puntos:

a) Selección por parte del usuario firmante del fichero, formulario u otro objeto binario para ser firmado. Los formatos de ficheros atenderán a lo recogido en la NTI de Catálogo de estándares.

El firmante se asegurará de que el fichero que se quiere firmar no contiene contenido dinámico que afecte a su validez y que pudiese modificar el resultado de la firma a lo largo del tiempo.

b) El servicio de firma electrónica ejecutará las siguientes verificaciones previas a la creación de la firma:

i. La firma electrónica puede ser validada para el formato del fichero específico que va a ser firmado.

ii. Los certificados a utilizar han sido expedidos bajo una Declaración de Políticas de Certificación específica y son certificados válidos según la legislación aplicable.

iii. Validez del certificado, comprobando si el certificado ha sido revocado, o suspendido, si entra dentro de su periodo de validez, y la validación de la cadena de certificación, incluyendo la validación de todos los certificados en la cadena.

Si alguna de estas verificaciones es errónea, el proceso de firma se interrumpirá.

Si no fuese posible realizar estas comprobaciones en el momento de la firma, será necesario, en todo caso, que los sistemas correspondientes asuman dicha validación, antes de aceptar el fichero, formulario u otro objeto binario firmado.

c) El servicio creará un fichero con la firma según corresponda en función del formato utilizado.

En el momento de la firma, se incluirá la referencia del identificador único de la versión del documento de política de firma electrónica en el que se ha basado su creación.

3. La vinculación del firmante se establecerá a través de etiquetas que, incluidas bajo la firma, y definidas según los estándares correspondientes (XAdES, CAdES y/o PAdES), proporcionarán la siguiente información complementaria a ésta:

a) Fecha y hora de firma, que podrá ser meramente indicativa en función de cómo se haya generado la firma.

b) Certificado del firmante.

c) Política de firma sobre la que se basa el proceso de generación de firma electrónica.

d) Formato del objeto original.

4. Como datos opcionales, la firma electrónica podrá incluir:

a) Lugar geográfico donde se ha realizado la firma del documento.

b) Rol de la persona firmante en la firma electrónica.

c) Acción del firmante sobre el documento firmado (lo aprueba, lo informa, lo recibe, lo certifica, etc.).

d) Sello de tiempo sobre algunos o todos los objetos de la firma.

5. La información indicada en los epígrafes 3 y 4 del presente subapartado se recogerá en cada formato de firma según las etiquetas del anexo.

6. En caso de creación de firmas electrónicas por distintos firmantes sobre un mismo objeto, donde el segundo firmante ratifica la firma del primero se utilizará la etiqueta correspondiente, CounterSignature, para contabilizarlas.

7. En el caso de que las múltiples firmas se realicen al mismo nivel, cada una de ellas se representará como una firma independiente.

III.7 Reglas de validación de firma de electrónica.

1. Las políticas de firma definirán las condiciones particulares bajo las que, en su ámbito, será posible validar la firma electrónica de un documento.

2. En el caso de documentos electrónicos, para acceder a la visualización de la firma, el usuario podrá presentar dicho documento electrónico, que contenga los datos, metadatos y firma o firmas, en una sede electrónica o en otros sistemas generales que proporcionen herramientas de reproducción de documentos electrónicos, como el servicio Valide, en el 060.

3. Las condiciones mínimas que se producirán para la validación de la firma serán las siguientes:

a) Garantía de que la firma es válida para el fichero específico que está firmado.

b) Validez de los certificados:

i. El instante de tiempo que se tomará como referencia para la validación será:

1) El momento en que se produjo la firma si se da alguno de los siguientes supuestos:

a) los servicios de los prestadores facilitan los históricos de estado de los certificados y la firma lleva un sello de tiempo válido en el momento de la verificación.

b) se trata de firmas longevas que incluyen las evidencias de la validez de la firma electrónica en el momento de la generación o primera validación, y dichas evidencias se encuentran selladas con un sello de tiempo válido.

2) En otros casos, el momento de la validación.

ii. Se comprobará que los certificados no fueron revocados ni suspendidos y que no han expirado.

iii. Se comprobará la validez de toda la cadena de certificación, incluyendo todos los certificados que la componen, con independencia de que éstos se encuentren incluidos en la propia firma o no.

iv. Se verificará que el certificado ha sido expedido por un prestador de servicios de certificación de confianza bajo una Declaración de Prácticas de Certificación que cumplirá la normativa y estará incluido en la política de firma aplicable.

v. Verificación, si existen y si así lo requiere la política de la plataforma de relación electrónica o un servicio concreto de dicha plataforma, de los sellos de tiempo de los formatos implementados, incluyendo la verificación de los periodos de validez de los sellos.

4. Para validar la firma electrónica se considerará la siguiente información:

a) Fecha y hora de la firma: Si se ha realizado el sellado de tiempo, el sello más antiguo dentro de la estructura de la firma se utilizará para determinar la fecha de la firma. En caso de que no existan sellos de tiempo, la fecha y hora de la firma tendrán carácter indicativo, pero no se utilizarán para determinar el momento en que se realizó la firma. En caso de que no existan sellos de tiempo en la firma, la validación del certificado se realizará en el momento de la validación de la firma.

b) Certificado del firmante. Este campo se utilizará para verificar el estado del certificado, y en su caso la cadena de certificación, en la fecha de la generación de la firma.

c) Política de firma sobre la que se basa el proceso de generación de firma electrónica. Se utilizará para identificar, mediante su hash y su identificador (01D), que la política de firma que se ha utilizado para la generación de la firma se corresponde con la que se utilizará para el servicio en cuestión.

Esta validación de la política de firma, implicará que el verificador dispondrá de los medios para verificar las condiciones impuestas en la política de firma concreta. La disponibilidad de la política de firma en un formato interpretable por medios automatizados (XML o ASN.1) y siguiendo los estándares europeos de representación de políticas de firma, indicada en el epígrafe 3.d del subapartado 11.5 de esta NTI, facilitará la labor de las aplicaciones receptoras de firmas electrónicas en aplicar distintas políticas de firma.

5. Si se han realizado varias firmas sobre un mismo documento, se seguirá el mismo proceso de verificación que con la primera firma, comprobando cada firma o la etiqueta CounterSignature en el campo de propiedades no firmadas, donde se informa de los refrendos de firma generados.

6. El encargado de la verificación de la firma podrá definir sus procesos de validación y de archivado, siempre en consonancia con los requisitos de la política de firma a la que se ajuste el servicio y con lo establecido en la NTI de Política de gestión de documentos electrónicos.

7. Para la verificación del estado de los certificados en el caso de formatos de firma longeva, la validez de la firma vendrá determinada por la validez del sello de tiempo de las evidencias de la validación incluidas en la firma. En estos casos la validez de la firma a lo largo del tiempo se mantendrá resellando la firma antes de la caducidad del certificado de la TSA (Autoridad de sellado de tiempo) que realizó el sello anterior, de forma que siempre sea posible verificar que en el momento en que se realizó la firma, el certificado era válido.
