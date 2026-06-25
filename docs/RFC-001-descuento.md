# RFC-001: Campo discount_percent en productos
## Descripción
Agregar discount_percent (0..100) a productos.
## Motivo
Requerido por contabilidad.
## Impacto
BD (ALTER TABLE) + API + validaciones + verificación.
## Criterios de aceptación
- POST /products acepta discount_percent
- GET /products devuelve discount_percent
- discount_percent fuera de 0..100 => error