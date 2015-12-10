## ANEXO VII

## Tipos de ofertas

Ofertas simples:

Las ofertas simples se caracterizan por lo siguiente:

• Incluyen la cantidad de producto a adquirir o entregar, así como el precio solicitado.

• Admiten la posibilidad de casación parcial.

• La cantidad no casada permanece en el Libro de Ofertas al precio incluido en la oferta.

• En cuanto a la validez temporal, pueden ser válidas exclusivamente para la Sesión de Negociación, cancelándose en caso de que no sea casada en el cierre de dicha sesión, o pueden extender su validez a Sesiones de Negociación del mismo producto en días posteriores.

• Una oferta o la oferta parcial que permanezca en el Libro de Ofertas tras una casación parcial, puede ser cancelada mientras la Sesión de Negociación esté en un estado que permita el envío de ofertas para el mismo producto.

Ofertas con condiciones:

Las ofertas con condiciones se clasifican según las diferentes condiciones de ejecución a las que estén sometidas.

Market Order:

Las ofertas Market Order, tienen las siguientes características:

• Incluyen únicamente la cantidad de producto a adquirir o entregar.

• Casan con las ofertas más competitivas en sentido contrario existentes en el Libro de Ofertas, independientemente de su precio.

• El precio de la Transacción es el de la(s) oferta(s) con las que casa (preexistentes).

• Admiten la posibilidad de casación parcial.

• La cantidad no casada es eliminada y no permanece en el Libro de Ofertas.

• Se ejecutan en el momento de introducción, nunca permanecen, por lo que, además, no hay posibilidad de ser canceladas por el Agente.

Fill and Kill:

Las ofertas Fill and Kill, tienen las siguientes características:

• Incluyen la cantidad de producto a adquirir o entregar, así como el precio solicitado.

• Casan con las ofertas más competitivas en sentido contrario existentes en el Libro de Ofertas, en caso de que los precios sean aceptables, tal y como se define en la Regla Casación de ofertas en Mercado Continuo.

• Admiten la posibilidad de casación parcial.

• La cantidad no casada es eliminada y no permanece en el Libro de Ofertas.

• Se ejecutan en el momento de introducción, nunca permanecen, por lo que, además, no hay posibilidad de que puedan ser canceladas por el Agente.

Fill or Kill:

Las ofertas Fill or Kill, tienen las siguientes características:

• Incluyen la cantidad de producto a adquirir o entregar, así como el precio solicitado.

• Casan con las ofertas más competitivas en sentido contrario existentes en el Libro de Ofertas, en caso de que los precios sean aceptables, tal y como se define en la Regla Casación de ofertas en Mercado Continuo.

• No admiten la posibilidad de casación parcial, si no se casa toda la cantidad, la oferta es eliminada de forma completa.

• Se ejecutan en el momento de introducción, nunca permanecen, por lo que, además, no hay posibilidad de ser canceladas por el Agente.

Iceberg:

Las ofertas Iceberg, tienen las siguientes características:

• Incluyen la cantidad total de producto a adquirir o entregar, la parte reducida de esa cantidad que se quiere mostrar, así como el precio solicitado.

• En el Libro de Ofertas únicamente se muestra al resto de Agentes una parte reducida de la cantidad total y el precio solicitado.

• Al introducir una oferta Iceberg con un precio no competitivo, dicha oferta se incluye en el Libro de Ofertas, mostrando la parte reducida de la cantidad total y el precio especificados. El Agente que introdujo la oferta podrá ver, adicionalmente, la cantidad total de dicha oferta.

• Cuando la parte reducida visible de la oferta se casa en su totalidad, instantáneamente se genera de forma automática (se instancia) una nueva oferta en el Libro de Ofertas, siendo la cantidad, la parte reducida de la cantidad total, y el precio, el especificado cuando se introdujo la oferta Iceberg.

• Si se introduce una oferta Iceberg con un precio competitivo, la cantidad a considerar será la cantidad total de la oferta Iceberg, registrando una Transacción por cada oferta contraria con la que case. Además, si no casa la cantidad total, la cantidad visible que aparecerá en el Libro de Ofertas, será como máximo la parte reducida especificada al crear la oferta, aunque la cantidad casada no haya sido múltiplo de dicha parte reducida.

• Si, existiendo una oferta Iceberg en el Libro de Ofertas, llega una oferta contraria con un precio competitivo y una cantidad superior a la cantidad visible de la oferta Iceberg, se llevarán a cabo transacciones diferentes por cada instanciación de la oferta Iceberg, cada una con su tiempo de creación. La cantidad visible de la oferta Iceberg en el Libro de Ofertas, será la cantidad que haya quedado sin casar tras la última instanciación.

• Pueden ser mantenidas exclusivamente para la Sesión de Negociación en curso o extender su validez a otras sesiones. En caso de incorporarse a una Subasta de apertura, por extender su validez a otras sesiones, lo harán con su cantidad total pendiente de casar. En caso de no casar totalmente en la Subasta, se incorporarán como ofertas Iceberg para la negociación en el Mercado Continuo posterior, con la cantidad no casada como cantidad total, y como cantidad reducida la introducida en la oferta.

• Además de las validaciones recogidas en la Regla «Validación de Ofertas», se comprobará que la parte reducida que se quiere mostrar de la oferta sea menor o igual que la cantidad total del producto ofertada.

Admiten la posibilidad de ser canceladas en los momentos en que se permite la cancelación de ofertas por la parte no casada.
