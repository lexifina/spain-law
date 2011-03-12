## ANEXO I

## Especificaciones informáticas del fichero de perceptores

Diseño registro

Existirán dos tipos de registros. Los dos serán de la misma longitud: 1000 caracteres.

Registro cabecera: será único. Su diseño es el siguiente:

| FMT | Nombre | Observaciones / Valor del campo |
| --- | --- | --- |
| A1 1-1 | Código Registro | Tendrá el valor fijo de 1. |
| A1 72-18 | Número de Propuesta | Blancos. |
| A1 419-32 | Proponente Nif | NIF del organismo que efectúa el Pago. Su formato es ES000 + NIF. |
| N7 33-39 | Número de Registros | Número de registros de detalle presentes en el fichero. |
| N9 40-48 | Total Clave Autenticación | Suma del campo clave autenticación de cada uno de los registros de detalle. |
| N14,2 49-64 | Total Importe Divisas | Suma del campo Importe en divisas de cada uno de los registros de detalle. El importe vendrá sin punto decimal. No se admitirán valores negativos. |
| N14,2 65-80 | Total Importe en Euros | Suma del campo Importe en euros de cada uno de los registros de detalle. El importe vendrá sin punto decimal. No se admitirán valores negativos. |
| A5 81-85 | Código de Centro Gestor | Código asignado por la Dirección General del Tesoro y Política Financiera que identificará elCentro Gestor del fichero de pagos en divisas. |
| N8 86-93 | Fecha de referencia | Su formato será: DDMMAAAA |
| N5 94-98 | Número secuencial | Número secuencial del fichero de pagos en divisas para el Centro Gestor en el ejercicio. |
| A5 99-103 | Versión | Tendrá el valor fijo de: 1.0 |
| A898 104-1000 | FILLER | Disponible para uso futuro. |

Registro de detalle: existirá uno por cada pago a realizar.

| FMT | Nombre | Observaciones/Valor del campo |
| --- | --- | --- |
| A1 1-1 | Código Registro | Tendrá siempre el valor de 2. |
| A1 2-2 | Marca del Beneficiario | Los valores posibles son: - “ “ : cuando el beneficiario sea un particular. - “B” : cuando el beneficiario sea un banco. |
| A70 3-72 | Beneficiario | Nombre del Beneficiario a quién hay que realizar el pago. Titular de la Cuenta Bancaria |
| A11 73-83 | Código BIC/SWIFT Beneficiario | Campo Opcional. Código BIC/SWIFT del Beneficiario, si se trata de un Banco. |
| A35 84-118 | Domicilio Beneficiario | Campo Opcional. Dirección (Calle) del Beneficiario. |
| A35 119-153 | Ciudad Beneficiario | Campo Opcional. Ciudad del Beneficiario. |
| A35 154-188 | País Beneficiario | Campo Opcional. País del Beneficiario. |
| A2 189-190 | Código País Beneficiario | Código del País del Beneficiario. |
| A1 191-191 | Forma de pago | Tendrá siempre el valor de ‘T’ → Transferencia. |
| A70 192-261 | Nombre del Banco | Nombre del Banco del Beneficiario donde se realizará el Pago. |
| A33 262-294 | Banco del beneficiario. Código doméstico | Campo opcional. Será el código de identificación del banco en su sistema doméstico de compensación. Se admitirán los siguientes valores en función del país del banco del beneficiario: |
|  | Código del país | Valores admitidos |  |
| US | 9 dígitos //FW seguido de 9 dígitos FW seguido de 9 dígitos |
| DE | 8 dígitos //BL seguido de 8 dígitos BL seguido de 8 dígitos |
| GB | 6 dígitos //SC seguido de 6 dígitos SC seguido de 6 dígitos |
| A11 295-305 | Banco del beneficiario. Código BIC/SWIFT | BIC/SWIFT en vigor. Hay que grabar dicho código, excepto cuando el banco del beneficiario haya comunicado que no dispone de él. |
| A35 306-340 | Domicilio Banco Beneficiario | Opcional. Dirección (Calle) del Banco del Beneficiario. |
| A35 341-375 | Ciudad Banco Beneficiario | Opcional. Ciudad del Banco del Beneficiario. |
| A35 376-410 | País Banco Beneficiario | Opcional. País del Banco del Beneficiario. |
| A2 411-412 | Código País Banco Beneficiario | Código del País del Banco del Beneficiario. |
| A34 413-446 | Número de cuenta del beneficiario | Identificación de la cuenta que el beneficiario mantiene en el banco del beneficiario. En pagos realizados en España será obligatorio el formato IBAN. Cuando se trate de un formato en código IBAN su estructura está formada por un conjunto máximo de 34 caracteres alfanuméricos contiguos que contienen los siguientes elementos consecutivos: - Código de país: código de dos letras especificado en la norma ISO 3166 del país en eque se encuentra el banco/sucursal que utiliza el IBAN. En España, será siempre ES. - Dígitos de Control, serán dos dígitos de control calculados según lo especificado. - Código Básico de Cuenta Bancaria (BBAN), hasta 30 caracteres alfanuméricos, del 0 al 9,de la A a la Z (únicamente mayúsculas), sin espacios de separación. El BBAN posee un número de caracteres específico por país, y la identificación de la Entidad y Oficina que tienen la cuenta, se recogen en posiciones fijas. En el caso de España, serán los 20 dígitos del Código Cuenta Cliente (C.C.C.). Por lo tanto,el IBAN español estará formado por 24 posiciones alfanuméricas. Ejemplo: ES07 0012 0345 03 0000067890. |
| A1 447-447 | Marca IBAN | Los valores posibles son: - I: el número de cuenta del beneficiario es un IBAN. - N: el número de cuenta del beneficiario no es un IBAN. |
| A70 448-517 | Nombre del Banco Intermediario | Campo Opcional. Nombre del Banco Intermediario del Beneficiario donde se realizará el Pago. |
| A33 518-550 | Banco Intermediario del beneficiario. Código doméstico | Campo opcional. Será el código de identificación del banco en su sistema doméstico de compensación. Se admitirán los siguientes valores en función del país del banco delbeneficiario: |
|  | Código del país | Valores admitidos |  |
| US | 9 dígitos //FW seguido de 9 dígitos FW seguido de 9 dígitos |
| DE | 8 dígitos //BL seguido de 8 dígitos BL seguido de 8 dígitos |
| GB | 6 dígitos //SC seguido de 6 dígitos SC seguido de 6 dígitos |
| A11 551-561 | Banco Intermediario del beneficiario. Código BIC/SWIFT | Campo opcional. Cuando tenga contenido deberá ser un BIC/SWIFT en vigor. |
| A35 562-596 | Domicilio Banco Intermediario Beneficiario | Campo Opcional. Dirección (Calle) del Banco Intermediario del Beneficiario. |
| A35 597-631 | Ciudad Banco Intermediario Beneficiario | Campo Opcional. Ciudad del Banco Intermediario del Beneficiario. |
| A35 632-666 | País Banco Intermediario Beneficiario | Campo Opcional. País del Banco Intermediario del Beneficiario. |
| A2 667-668 | Código País Banco Intermediario Beneficiario | Campo Opcional Código del País del Banco Intermediario del Beneficiario. |
| A34 669-702 | Número de cuenta en Banco Intermediario | Campo opcional. Identifica la cuenta que el banco del beneficiario mantiene en el banco intermediario. No se dará este dato si no se utiliza el banco intermediario. |
| A3 703-705 | Moneda | Código de la Moneda en la que se efectuará el pago. Será una de las incluidas en las Normas para el intercambio de soportes entre el Banco de España y la Dirección General del Tesoro y Política Financiera.- Operaciones con el Exterior |
| N13,2 706-720 | Importe en divisas | Importe del pago en la divisa establecida en el campo Moneda. El importe vendrá sin punto decimal. Será 0 para las propuestas cuyos Tipos de pago sean 30,31 o 32. Y vendrá relleno para propuestas cuyos Tipos de pago sean 33, 34 o 35., excepto cuando se trate de multianexos y de la moneda 978. No se admiten valores negativos. Se comprobará la coherencia entre el número de decimales distintos de cero de este campo yl a moneda, ya que no todas las monedas permiten el empleo de decimales: en la mayoría se aceptan hasta dos, pero en algunas no se acepta ninguno. Ejemplo: no se admitiría que un importe en yenes japoneses (moneda 392) presentara alguna cifra decimal distinta de cero. Coherente con el Tipo de Cambio. |
| N13,2 721-735 | Importe en euros | Importe del pago en la moneda doméstica (euros). El importe vendrá sin punto decimal. No se admiten valores negativos. |
| N6,6 736-747 | Tipo de Cambio | Obligatorio si el importe Divisas está relleno. El importe vendrá sin punto decimal. No se admite valores negativos. |
| N7 748-754 | Clave de autenticación | Se determina según lo establecido en las normas que se acuerden entre la Intervención General de la Administración del Estado y la Dirección General del Tesoro y Política Financiera. |
| N5 755-759 | Número de secuencia | Se exigirá que este número sea consecutivo comenzando por el número 1. |
| A1 760-760 | Órgano AGE | Los valores posibles son: - S : El beneficiario es un órgano de la A.G.E. - N : En caso contrario. |
| A14 761-774 | NIF beneficiario | Su formato es ES000 + NIF Obligatorio para personas físicas o jurídicas que tengan NIF/NIE español |
| A226 775-1000 | FILLER | Disponible para uso futuro. |

Campos nuevos del registro de cabecera:

| FMT | Nombre | Observaciones/Valor del campo |
| --- | --- | --- |
| A5 81-84 | Código de Centro Gestor | Código asignado por la Dirección General del Tesoro y Política Financiera que identificará el Centro Gestor del fichero de pagos en divisas. |
| N8 85-92 | Fecha | Su formato será: DDMMAAAA |
| N5 93-97 | Número secuencial | Número secuencial del fichero de pagos en divisas para el Centro Gestor en el ejercicio. |
| A5 98-102 | Versión | Tendrá el valor fijo de: 1.0 |

Campos nuevos del registro de detalle:

| FMT | Nombre | Observaciones / Valor del campo |
| --- | --- | --- |
| A1 760-760 | Órgano AGE | Los valores posibles son: - S : El beneficiario es un órgano de la A.G.E. - N : En caso contrario. |
| A14 761-774 | NIF | Su formato es ES000 + NIF |
