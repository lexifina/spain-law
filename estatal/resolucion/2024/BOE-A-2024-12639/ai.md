## ANEXO I

## Modelo de datos del sistema de monitorización de la información correspondiente a los registros de operaciones de juego

Índice

1. Contenido.

2. Definiciones.

3. Modelo de datos funcional.

3.1 Tipos de información.

3.2 Obligación de reporte.

3.2.1 Obligaciones del gestor de liquidez compartida.

3.3 Periodicidad.

3.4 Descripción de la información.

3.4.1 Registro de usuario.

3.4.2 Registro de Cuenta de juego.

3.4.3 Registro de Cuenta del operador.

3.4.4 Registros de Datos de Juego.

3.4.4.1 Registro JUC: juegos.

3.4.5 Registro de Ajustes de Apuestas.

3.4.6 Registro de Catálogo de eventos.

3.4.7 Rectificaciones.

3.4.8 Clasificaciones y normalizaciones.

4. Modelo técnico.

4.1 Estructura de la información.

4.1.1 Registros.

4.1.2 Subregistros.

4.1.3 Lote.

4.1.4 Firma del lote.

4.1.5 Compresión y cifrado del lote.

4.2 Estructura de directorios.

4.3 Empaquetado de los datos de juegos.

4.4 Nomenclatura de archivos.

4.4.1 RU: Registro de Usuario.

4.4.2 CJ: Cuenta de juego.

4.4.3 OP: Cuenta de Operador.

4.4.4 JU: Registro de Juego.

4.4.5 JUA: Ajustes de Apuestas y CEV: Catálogo de Eventos.

4.5 Conceptos generales.

4.5.1 OperadorId.

4.5.2 AlmacenId.

4.5.3 Registro.

4.5.4 Rectificaciones.

4.5.5 Registros periódicos.

4.5.6 Registros de Juego (JUC).

4.5.7 Lote.

4.5.8 Periodicidad y fragmentación.

4.5.9 Tipos de movimiento libres.

4.5.10 Desgloses que se repiten varias veces.

4.5.11 Sobre campos económicos vacíos en ficheros.

1. Anexos.

1.1 Listas y enumerados.

CambioEnDatos: Cambio en datos (RUD).

ConceptoBonos: Concepto bonos (CJD, CJT, CJR).

ConceptoOPT: Ajustes de cuenta del operador (OPT, ORT).

EstadoCNJ: Estado CNJ (RUD, RUR, RUT).

ListaCodigo: Lista de códigos de eventos admitidos (CEV).

MotivoEstado: Motivo por el cual la cuenta del jugador ha sido Suspendida o Cancelada (RUD).

MotivoFinSesion: Motivo por el cual se ha cerrado la sesión (RegistroOtrosJuegos, RegistroLoteriaPresorteada).

PaisISO: Países y territorios según el código ISO de 2 caracteres (RUD, RUG, CEV). (Códigos ISO 3166).

PerfilJugador: Perfil del jugador especial según RD de juego seguro (RUD).

PeriodoLimite: Periodo al que aplica el límite del jugador (RUD).

Sexo: Sexo del jugador (RUD, RUR).

SexoCompeticion: Género a la que pertenece la competición deportiva (CEV).

TipoApuesta: Tipo de apuesta realizada (RegistroApuestaContrapartida, RegistroApuestaMutua).

TipoDispositivo: Tipo de dispositivo del jugador (CJD, RUD, RegistroPoquerTorneo, RegistroApuestaContrapartida, RegistroApuestaMutua, RegistroLoteriaPresorteada).

TipoDocumento: Tipo de documento aportado por el jugador no residente (RUD, RUG).

TipoJuego: Tipo de juego (todos los registros).

TipoLimite: Tipo de limite (RUD).

TipoMedioPago: Lista de códigos de medios de pago admitidos (CJD).

TipoRegistro: Tipos de registro JUC.

TipoResultado: Resultado de la operación de depósito o retirada (CJD).

TipoVerificacionDocumental: Tipo de verificación documental del jugador realizada (RUD).

UnidadLimite: Valores posibles de las unidades de los límites del jugador (RUD).

VariantePoker: Variante de juego de póquer (RegistroPoquerTorneo).

VarianteSesion: Variantes de los juegos de Póquer Cash, Black Jack y Ruleta (RegistroOtrosJuegos).

1.2 Tipos de campos.

Campos de cadena de caracteres.

Campos numéricos.

Campos de tipo fecha.
