## ANEXO

## Campos factura

1. De conformidad con lo señalado en el artículo 5 de esta Orden, se deberá incluir una serie de campos dentro de la propia factura para la correcta remisión a los destinatarios. Algunos de estos campos serán cumplimentados con carácter obligatorio en todas las facturas, y en otros campos, su cumplimentación es opcional, pero en el caso de que se desee informar de los mismos debe utilizarse el campo que se indica.

2. Dentro del documento de factura electrónica será obligatorio, para la correcta remisión de la factura al órgano destinatario final, informar del órgano gestor, la unidad tramitadora y la oficina contable destinatarios. Y opcionalmente, del órgano proponente.

Las unidades deberán ir codificadas bajo la etiqueta de centros administrativos del «<BuyerParty>» de la factura

| ROL | RoleTypeCode | CentreCode | Descripción | Tipo |
| --- | --- | --- | --- | --- |
| Fiscal | 01 | Código de la unidad en DIRECTORIO | Oficina Contable | Obligatorio |
| Receptor | 02 | Código de la unidad en DIRECTORIO | Órgano Gestor | Obligatorio |
| Pagador | 03 | Código de la unidad en DIRECTORIO | Unidad Tramitadora | Obligatorio |
| Comprador | 04 | Código de la unidad en DIRECTORIO | Órgano proponente | Opcional |

El código del centro <CentreCode> será el código de dicha unidad en el sistema «Directorio Común de Unidades Orgánicas y Oficinas DIR3» recogido en el artículo 9 del Esquema Nacional de Interoperabilidad (Real Decreto 4/2010).

Ejemplo de XML todos los roles de centros administrativos rellenos:

![imagen](https://www.boe.es/datos/imagenes/disp/2014/154/06662_001.png)
