## ANEXO

## Etiquetas de creación y validación de firmas electrónicas para los formatos admitidos

| Información | Obligatoriedad | Campo – etiqueta – elemento1 |
| --- | --- | --- |
| XAdES | CAdES | PAdES |
| Fecha y hora de la firma | Obligatorio | SigningTime (SignedProperties) | Signing-time (SignedData) | Se indica en el campo «M» del diccionario Signature. |
| Certificado del firmante | Obligatorio | SigningCertificate (SignedProperties) | ESS signing-certificate ESS signing-certificate-v2 (SignedData) | ESS signing-certificate ESS signing-certificate-v2 |
| Política de firma | Obligatorio | SignaturePolicyldentifier – SigPolicyld (SignedProperties) | SignaturePolicyldentifier – SigPolicyld (SignedData) | SignaturePolicyldentifier |
| SignaturePolicyldentifier– SigPolicyldHash (SignedProperties) | SignaturePolicyldentifier– SigPolicyldHash (SignedData) |
| Formato del objeto original | Obligatorio | DataObjectsFormat (SignedProperties) | Content-hints (SignedData) | No permitido |
| Lugar geográfico (localización) | Opcional | SignatureProductionPlace (SignedProperties) | Signer-location (SignedData) | Se indica en el campo «Location» del diccionario Signature. |
| Rol de la persona firmante | Opcional | SignerRole - ClaimedRoles (SignedProperties) | Signer-attributes (SignedData) | Signer-attributes |
| Acción del firmante sobre el documento firmado | Opcional | CommitmentTypeIndication (SignedProperties) | Commitment-type-indication (SignedData) | Commitment-type-indication |
| Sello de tiempo | Opcional | AllDataObjectsTimeStamp (SignedProperties) | Content-time-stamp (SignedData) | Content-time-stamp |
| IndividualDataObjectsTimeStamp |
| Contador de firmas electrónicas | Opcional | CounterSignature (UnsignedProperties) | CounterSignature (UnsignedProperties) | No está permitido |
| 1 Nótese que la tabla no constituye un listado completo de las etiquetas definidas por cada estándar sino una referencia a las etiquetas que reflejarán la información para la creación y validación de la firma. |
