## ANEXO V

## Especificaciones del Formato de Intercambio de Contratos de Arrendamiento de vivienda (FICCA)

| Nombre del campo | Descripción | Tipo de campo (N, numérico; X, texto) y [longitud] | Campo obligatorio (O) o voluntario (V) |
| --- | --- | --- | --- |
| Datos de localización |
| RefCat. | Referencia catastral de la vivienda (20 caracteres). En caso de tratarse del alquiler de una parte, se recogerá la referencia del inmueble en que se ubica la vivienda. | X [20] | O |
| Municipio. | Nombre del municipio en el que se ubica el inmueble. | X [40] | O |
| CodMunIne. | Código INE del municipio. | X [5] | O |
| CodPostal. | Código postal. | X [5] | V |
| TipoVia. | Abreviatura del tipo de vía. Ver listado de abreviaturas en el anexo I. | X [2] | V |
| NombreVia. | Nombre de la vía en la que se ubica el inmueble. | X [25] | V |
| NP. | Número de policía. | N [4] | V |
| NPD. | Carácter de duplicado. | X [1] | V |
| ES. | Escalera o portal. | X [3] | V |
| PL. | Planta. | X [3] | V |
| PT. | Puerta. | X [3] | V |
| Datos del contrato de arrendamiento |
| FechaSCA. | Fecha de suscripción del contrato de arrendamiento en formato AAAAMMDD. | X [8] | O |
| FechaICA. | Fecha de inicio del arrendamiento objeto del contrato en formato AAAAMMDD (se cumplimentará únicamente cuando sea distinta de la fecha de suscripción del contrato). | X [8] | O |
| Duración. | Duración del contrato de arrendamiento expresado en años. | X [3] | O |
| PArrendador. | Personalidad del propietario/arrendador (Persona física PF/Persona jurídica PJ/Entidad pública EP). | X [2] | O |
| Arbitraje. | ¿El contrato incluye alguna cláusula de sumisión a mediación o arbitraje en caso de incumplimiento? (S/N). | X [1] | V |
| PlazaAparc. | Número de plazas de aparcamiento con la que se alquila la vivienda en el presente contrato de arrendamiento. | N [1] | V |
| Trastero. | ¿La vivienda se alquila con trastero? (S/N). | X [1] | V |
| Amueblado. | ¿La vivienda se alquila amueblada (A) o sin amueblar (S)? | X [1] | V |
| RentaMes. | Importe de la renta mensual en euros. | N [10] | O |
| ActRenta. | ¿La actualización anual de la renta se determina de acuerdo con el IPC (I), con otro indicador (O), o no se establece la actualización de renta (N)? | X [1] | O |
| Fianza. | Importe de la fianza establecida. | N [10] | O |
| GarantiaAdic. | ¿El contrato establece como garantía adicional un aval (A) un depósito (D) o no se establecen garantías adicionales (N)? | X [1] | V |
| ImporteGA. | Importe del aval o depósito establecido como garantía adicional en euros. | N [10] | V |
| IndemDesest. | ¿El contrato establece indemnización en caso de desistimiento por parte del arrendatario? (S/N). | X [1] | V |
| RenunDAdqPref. | ¿Se recoge en el contrato la renuncia del derecho de adquisición preferente por parte del arrendatario? (S/N). | X [1] | V |
