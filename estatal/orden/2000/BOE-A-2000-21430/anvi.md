## ANEXO VI

A) CARACTERÍSTICAS DE LOS SOPORTES MAGNÉTICOS

Los soportes directamente legibles por ordenador para la presentación del resumen anual de retenciones e ingresos a cuenta sobre determinadas rentas o rendimientos procedentes del arrendamiento o subarrendamiento de inmuebles urbanos del Impuesto sobre la Renta de las Personas Físicas, del Impuesto sobre Sociedades y del Impuesto sobre la Renta de no Residentes, correspondiente a establecimientos permanentes (Modelo 180), habrán de cumplir las siguientes características:

Cinta magnética

Pistas: 9

Densidad: 1.600ó 6.250 BPI.

Código: EBCDIC, en mayúsculas.

Etiquetas: Sin etiquetas.

Marcas: En principio y fin de cinta.

Registros de: 250 posiciones.

Factor de bloqueo: 10

Disquetes

De 3 1/2” doble cara. Doble densidad (720 KB) Sistema operativo MS-DOS y compatibles.

De 3 1/2” doble cara. Alta densidad (1.44 MB) Sistema operativo MS-DOS y compatibles.

Código ASCII en mayúsculas sin caracteres de control o tabulación.

Registros de 250 posiciones.

Los disquetes de 3 1/2” deberán llevar un sólo fichero, cuyo nombre será RTPAxxxx, siendo xxxx las cuatro cifras del ejercicio fiscal al que corresponde la declaración, conteniendo este único fichero los diferentes tipos de registros y en el orden que se menciona en el apartado B).

Si el fichero ocupa más de un disquete, deberá particionarse en tantos ficheros como sea necesario. Cada uno de los ficheros parciales tendrá la denominación RTPAxxxx.NNN (NNN=001,002,...), siendo xxxx las cuatro cifras del ejercicio fiscal al que corresponde la declaración y NNN el número consecutivo del fichero comenzando por el 001.

Los archivos parciales contendrán siempre registros completos, es decir, nunca podrá particionarse el fichero dejando registros incompletos en los ficheros parciales.

Si las características del equipo de que dispone el declarante no le permite ajustarse a las especificaciones técnicas exigidas, y está obligado a presentar resumen anual de retenciones e ingresos a cuenta sobre determinadas rentas o rendimientos procedentes del arrendamiento o subarrendamiento de inmuebles urbanos, en soporte directamente legible por ordenador, deberá dirigirse por escrito a la Subdirección General de Aplicaciones del Departamento de Informática Tributaria de la Agencia Estatal de Administración Tributaria (A.E.A.T.), calle Santa María Magdalena, 16, 28016 Madrid, exponiendo sus propias características técnicas y el número de registros que presentaría, con objeto de encontrar, si lo hay, un sistema compatible con las características técnicas de la A.E.A.T.

B) DISEÑOS LÓGICOS

DESCRIPCIÓN DE LOS REGISTROS

Para cada declarante se incluirán dos tipos diferentes de registro, que se distinguen por la primera posición, con arreglo a los siguientes criterios:

Tipo 1: Registro del declarante: Datos identificativos y resumen de la declaración. Diseño de tipo de registro 1 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

Tipo 2: Registro de perceptor: Diseño de tipo de registro 2 de los recogidos más adelante en estos mismos apartados y Anexo de la presente Orden.

El orden de presentación será el del tipo de registro, existiendo un único registro del tipo 1 y tantos registros del tipo 2 como percepciones tenga la declaración.

Todos los campos alfanuméricos y alfabéticos se presentarán alineados a la izquierda y rellenos de blancos por la derecha, en mayúsculas sin caracteres especiales, y sin vocales acentuadas.

Para los caracteres específicos del idioma se utilizará la codificación IS0-8859-1. De esta forma la letra «Ñ» tendrá el valor ASCII 209 (Hex. D1) y la «C»(cedilla mayúscula) el valor ASCII 199 (Hex. C7).

Todos los campos numéricos se presentarán alineados a la derecha y rellenos a ceros por la izquierda sin signos y sin empaquetar.

Todos los campos tendrán contenido, a no ser que se especifique lo contrario en la descripción del campo. Si no lo tuvieran, los campos numéricos se rellenarán a ceros y tanto los alfanuméricos como los alfabéticos a blancos.

En los supuestos de presentación colectiva (más de un declarante en el mismo archivo) se presentará como primer registro del soporte un registro tipo cero, con arreglo al diseño del tipo de registro cero que se incluye a continuación en este mismo apartado, el cual contendrá los datos de la persona o entidad responsable de la presentación y existirá en todo caso, aunque dicha persona o Entidad figure también en el soporte como declarante. A continuación seguirán los datos del primer declarante (tipo 1), seguidos de sus perceptores (tipo 2); a continuación los datos del siguiente declarante y así sucesivamente.

El primer registro del fichero (tipo 0 para presentaciones colectivas o tipo 1 para presentaciones individuales), contendrá un campo de 13 caracteres, en las posiciones 238 a 250 reservado para el sello electrónico, que será cumplimentado exclusivamente por los programas oficiales de la A.E.A.T. En cualquier otro caso se rellenará a blancos.

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_029.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_030.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_031.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_032.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_033.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_034.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_035.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_036.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_037.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_038.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_039.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_040.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_041.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_042.png)

![imagen](https://www.boe.es/datos/imagenes/disp/2000/285/21430_043.png)
