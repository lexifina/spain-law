## Tercero.

Modificar la Resolución de 6 de octubre de 2014, de la Dirección General de Ordenación del Juego, por la que se aprueba el modelo de datos del sistema de monitorización de la información correspondiente a los registros de operaciones de juego, en los siguientes términos:

1. Se añaden las siguientes definiciones en el apartado 2:

«Juego ofertado en un entorno de liquidez internacional.

Aquel en el que las cantidades económicas que se dedican a la participación en el juego provienen de jugadores con registro de usuario español y de jugadores sin registro de usuario español.

Gestor de liquidez internacional.

El operador que gestiona un juego ofertado en un entorno de liquidez internacional.

Jugador con registro de usuario español.

Aquel que participa en el juego mediante una cuenta abierta en un operador de juego, de acuerdo con la Ley 13/2011, de 27 de mayo, de regulación del juego.»

2. Se añade un nuevo apartado 3.2.1:

«3.2.1 Obligaciones del gestor de liquidez internacional.

El gestor de liquidez internacional solo deberá informar de los juegos (partida, sesión o torneo) en los que participe, al menos, un jugador con registro de usuario español.

En los ficheros RUR/RUT, CJD/CJT, BOT, JUD, JUT, JUA, CEV solo se incluirán datos de jugadores con registro de usuario español. En el fichero ORT, se remitirá la información económica correspondiente a los juegos con liquidez internacional desglosada por operador (B2C) del dominio “.es” y por jurisdicción para los operadores no pertenecientes al dominio “.es” que participen en el juego.»

3. Se añade al apartado 3.4.8, entre los epígrafes «operadores obligados» y «periodicidad», el siguiente epígrafe:

«Juegos ofertados en un entorno de liquidez internacional.

En los juegos ofertados en un entorno de liquidez internacional en los que participe al menos un jugador con registro de usuario español, deberán reportarse:

• Por las operaciones de operadores de la jurisdicción española, los datos agregados por operador.

• Por las operaciones de operadores de otras jurisdicciones, los datos agregados por jurisdicción.»

4. En el Apartado 3.4.10 [Registros de juegos (JUT, JUD)], en el epígrafe «Datos genéricos comunes a todos los juegos», se añade el siguiente campo:

«• BooleanLI: S/N (debe marcarse como afirmativo cuando en la apuesta, partida, torneo o mano haya participado algún jugador sin registro de usuario español. Para juegos que no estén en red de liquidez internacional el campo es opcional).»

5. El Apartado 3.5.3.2 («Registro ORT: Cuenta del operador de red») se sustituye por el siguiente:

«3.5.3.2. Registro ORT: Cuenta del operador de red.

La descripción de la información es igual que la del registro OPT, teniendo en cuenta que los apuntes vendrán desglosados por operador que ha aportado los participantes a la red.

En el caso de juegos ofertados en un entorno de liquidez internacional, el gestor de liquidez internacional deberá informar de las magnitudes económicas desglosándolas por operador en el caso de los operadores que dispongan de licencia en España, y por un agregado por jurisdicción para el resto de los operadores.»

6. En el Apartado 3.5.4.1 [«Datos genéricos comunes a todos los juegos (JUT y JUD)»] en el epígrafe «Datos de juego totalizados (JUT)», se añade el siguiente campo:

| BooleanLI | S/N |
| --- | --- |
