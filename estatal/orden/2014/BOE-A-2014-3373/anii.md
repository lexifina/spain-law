## ANEXO II

## Reglas de validación a las que se refiere la disposición adicional cuarta

1. Verificación del cumplimiento del esquema XSD de "Facturae" de la versión correspondiente (3.2 ó 3.2.1), así como verificación de los XSD de las extensiones aprobadas.

2. Verificación de la política de firma en vigor asociada al formato "Facturae".

3. Respecto al número de la factura:

a) El número de factura será obligatorio.

b) No deberá existir en el registro contable de facturas una factura con el mismo NIF y país del emisor, número y serie de factura, emitida en la misma fecha, salvo que estuviera rechazada o anulada.

4. Respecto al tipo de factura electrónica.

a) La tipología de facturas rectificativas admitidas en el formato Facturae, de acuerdo con el Real Decreto 1619/2012, de 30 de noviembre, por el que se aprueba el Reglamento por el que se regulan las obligaciones de facturación, será la siguiente:

1.º "01" - Rectificación modelo íntegro.

2.º "02" - Rectificación modelo por diferencias.

3.º "03" - Rectificación por descuento por volumen de operaciones durante un período y rectificación por devolución de mercancías o de envases y embalajes previstos en el artículo 15.2, 2.º párrafo, del Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre.

4.º "04" - Autorizadas por la Agencia Estatal de Administración Tributaria.

b) Cuando el tipo de factura es rectificativa, será obligatorio el criterio de rectificación y, cuando este criterio fuera 01, rectificación modelo íntegro, o 02, rectificación modelo por diferencias, el número de factura del emisor que rectifica. En el resto de supuestos no será necesario identificar el número de factura del emisor que rectifica.

c) Si en el registro contable de facturas ha sido ya registrada la factura original, debería rechazarse el duplicado o copia de la misma previsto en el artículo 14 del Reglamento por el que se regulan las obligaciones de facturación, aprobado por el Real Decreto 1619/2012, de 30 de noviembre. En el caso de que la factura original llegara al registro contable de facturas una vez registrado el duplicado o copia, se rechazaría aquélla.

5. Respecto al emisor y cesionario de la factura.

a) El código de tipo de persona, física o jurídica, será obligatorio. En el caso de entidades sin personalidad jurídica se utilizará el código correspondiente a personas jurídicas.

b) En el caso de que el país emisor del NIF sea España, se validará que el NIF se ajuste a las normas y criterios de formación del mismo. Si los dos primeros caracteres del NIF son letras, se asumirá que equivalen al país, y el resto al NIF. En otro caso, el código equivaldrá al NIF y se asumirá que el país es España.

c) Se validará la existencia del código del país de acuerdo con el propio esquema "Facturae".

d) Si se trata de persona física, se validará que el nombre y el primer apellido tengan algún contenido.

e) Si se trata de persona jurídica, se validará que la razón social tenga algún contenido.

f) Si existe cesionario, se comprobará que el NIF del emisor de la factura y del cesionario no coinciden.

6. Respecto a los importes de la factura.

a) En las facturas emitidas en euros, se validará que los importes totales de las líneas relativos al coste total sean numéricos y estén redondeados, de acuerdo con el método común de redondeo, a dos decimales, como resultado del producto del número de unidades por el precio unitario, y que los importes brutos de las líneas sean el resultado de restar del coste total los descuentos, y de sumar los cargos, todos ellos numéricos y con dos decimales. Asimismo se validará que el resto de importes a nivel de línea, con excepción del importe unitario, vengan expresados en euros con dos decimales. No se consideran importes los tipos impositivos o los porcentajes a aplicar que, al igual que el importe unitario, podrán tener los decimales que permita el formato Facturae.

b) En las facturas emitidas en euros, se validará que el total importe bruto de la factura sea numérico y a dos decimales, por suma de los importes brutos de las líneas. Asimismo se validará que el resto de importes vengan expresados en euros con dos decimales. No se consideran importes los tipos impositivos o los porcentajes a aplicar que podrán tener los decimales que permita el formato Facturae.

c) Se validará la existencia del código de moneda de acuerdo con lo establecido en el propio esquema "Facturae".

d) Si el "total importe bruto antes de impuestos" es positivo, se validará que el "total impuestos retenidos", si tiene contenido, sea mayor o igual que cero.

e) Se validará que el "total importe bruto antes de impuestos" sea igual al "total importe bruto" menos el "total general descuentos" más el "total general cargos".

f) Se validará que el "total Factura" sea igual al "total importe bruto antes de impuestos" más el "total impuestos repercutidos" menos el "total impuestos retenidos".

7. Respecto a las fechas de la factura.

a) Se validará que la fecha de anotación en el registro administrativo tenga valor, sea válida y anterior o igual a la fecha actual y mayor o igual que la fecha de emisión de la factura.

8. Respecto a los órganos administrativos que participan en la tramitación de la factura.

a) Se validará que los códigos DIR3 de los tres órganos administrativos que resulta obligatorio identificar en la factura electrónica tengan valor y existan en las tablas de órganos administrativos del registro contable de facturas.

b) Se validará que las relaciones oficina contable-órgano gestor; oficina contable-unidad tramitadora; y órgano gestor-unidad tramitadora existan en las tablas de órganos administrativos del registro contable de facturas.

9. Otras validaciones.

a) Será obligatorio que el punto general de entrada de facturas electrónicas proporcione, por cada factura electrónica presentada, el número de registro asignado en dicho punto.

b) Se validará que la descripción de las líneas de la factura tenga algún contenido.

> Se añade por el art. 1.4 de la Orden HAP/1650/2015, de 31 de julio. Ref. BOE-A-2015-8844.
