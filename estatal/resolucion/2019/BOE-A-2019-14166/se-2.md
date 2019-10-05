## Sexto. Generación del código seguro de verificación.

1. El CSV se generará de forma automatizada.

2. Se compondrá de dos partes y se generará del modo siguiente:

a) 5 posiciones que delimitarán el ámbito del documento dentro del Fondo Español de Garantía Agraria, O.A.

b) El resto de posiciones tendrá una longitud de 31 caracteres que serán:

Una posición para la identificación de la versión del CSV.

Las 20 posiciones más significativas obtenidas del resumen criptográfico del documento electrónico original mediante el algoritmo hash SHA-256.

10 posiciones de la fecha y hora en formato epoch.

3. En caso de obtenerse un CSV ya existente almacenado en el sistema, vinculado a otro documento, se repetirá el proceso generando un nuevo código.
