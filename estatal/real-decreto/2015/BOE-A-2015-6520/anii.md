## ANEXO II

## Campos codificados contenidos en los estatutos-tipo y nodo xml asociado

| Número campo codificado | Campo | Tipo de datos | Observaciones | Nodo |
| --- | --- | --- | --- | --- |
| -- | ID-CIRCE. | Alfanumérico. | Código generado por el sistema CIRCE. | <ID-CIRCE/> |
| 1.1 | Denominación social. | Alfanumérico. | Puede ser de la bolsa de denominaciones sociales. | <denominación_social/> |
| 1.2.1 | Objeto social-descripción actividad principal. | Alfabético. | 1 entrada. | <Descripcion_Actividad_principal/> |
| Objeto social-campo actividad principal. | Alfanumérico. | <Valor_codigo_actividad_principal/> |
| 1.2 | Objeto social - descripción. | Alfabético. | De 1 a n entradas. | <Descripción_CNAE/> |
| Objeto social - campo. | Alfanumérico. | <Valor_código_CNAE /> |
| 1.3 | Duración. | Alfanumérico. | Elegir uno: – Indefinida. – XX años/meses. | <Duración/> |
| 1.4 | Fecha inicio de actividad. | Fecha. |  | <Fecha_inicio_actividad/> |
| 1.5 | Cierre del ejercicio social. | Día y mes. | Día y mes del año (en letra). | <Fecha_cierre_ejercicio/> |
| 1.6 | Domicilio social. | Alfabético. | Codificación INE. | <Tipo_via/> |
| Alfabético. |  | <Nombre_via/> |
| Alfanumérico. | Opcional. | <Km/> |
| Alfanumérico. | Debe admitir S/N. | <Numero/> |
| Alfabético. | Opcional. | <Bis/> |
| Alfanumérico. | Opcional. | <Bloque/> |
| Alfanumérico. | Opcional. | <Escalera/> |
| Alfanumérico. | Opcional. | <Piso/> |
| Alfabético. | Opcional. | <Puerta/> |
| Alfanumérico. |  | <Cod_postal/> |
| Alfanumérico. | Codificación INE (de tres dígitos). | <Cod_municipio/> |
| Alfabético. |  | <Municipio/> |
| Alfabético. |  | <Provincia/> |
| Alfanumérico. | Codificación INE (de dos dígitos). | <Cod_provincia/> |
| Alfabético. | Codificación INE. | <País/> |
| Alfanumérico. | Opcional. | <Teléfono/> |
| Alfanumérico. | Opcional. | <Fax/> |
| Alfanumérico. | Opcional. | <Email/> |
| 1.7 | Capital social. | Numérico. | Si es Sociedad Limitada de Fundación Sucesiva el capital social suscrito y desembolsado deberá ser la misma cantidad y deberá estar comprendida entre 1 y 2.999 euros. | <Capital social/> |
| 1.8 | Número de participaciones. | Numérico. |  | <Participaciones/> |
| 1.9 | Valor de cada participación. | Numérico. |  | <Importe participaciones/> |
| 1.10 | Retribución administrador. | Alfanumérico. | Elegir uno: – Gratuito – Cantidad fija determinada por la Junta General para cada ejercicio económico. – Un porcentaje de XX (número) % de los beneficios repartibles de cada ejercicio económico, con arreglo a la Ley. | <Retribucion_administrador/> |
| 1.11 | Página Web de la sociedad. | Alfanumérico. | Elegir uno en función de si ya se dispone de página web. En este último caso Deberá completarse la URL (uniform resource locator) de la página web: – Conforme al art. 11 bis de la Ley de Sociedades de capital, la Junta General podrá acordar que la sociedad tenga una página web corporativa, pudiendo delegar en el órgano de administración la elección de la dirección URL o sitio en la web de la web corporativa, que una vez concretada deberá comunicar a todos los socios. Al órgano de administración de la sociedad le corresponde la modificación, el traslado o la supresión de la página web. – La Sociedad tiene una página web corporativa de acuerdo con lo dispuesto en el artículo 11 bis de la Ley de Sociedades de Capital. La dirección de la web será URL de la página web. Será competencia del órgano de administración la modificación, traslado o supresión de la página web. | <Pag_web/> |
