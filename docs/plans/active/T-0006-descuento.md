---
id: T-0006
title: Descuento porcentual en total()
owner: "@AlbertoLacambra"
status: in_progress
risk: bajo
created: 2026-10-24
issue: 12
acceptance:
  - id: AC1
    description: total() aplica un descuento porcentual opcional y rechaza valores fuera de 0–100 con ValueError
    check: "python3 -m unittest tests.test_app.TotalTest.test_descuento"
  - id: AC2
    description: Las pruebas existentes siguen pasando
    check: "python3 -m unittest discover -s tests"
---

# T-0006 · Descuento porcentual en total()

<!-- harness:objetivo -->
## Objetivo
`total(lines, descuento=0)` aplica un descuento porcentual sobre la suma (0 por defecto) y redondea a 2 decimales. Un descuento menor que 0 o mayor que 100 lanza `ValueError`.

<!-- harness:alcance -->
## Alcance
- Dentro: `src/app.py` y `tests/test_app.py`.
- Fuera de alcance: descuentos por línea e impuestos.

<!-- harness:plan -->
## Plan
1. Añadir la prueba `test_descuento` (casos válidos y fuera de rango).
2. Implementar el parámetro `descuento`.
3. Verificar con el subagente `verificador` y cerrar con la skill `cerrar-tarea`.

<!-- harness:progreso -->
## Progreso

<!-- harness:decisiones -->
## Decisiones
- 2026-10-24 — AC1 nombra la prueba exacta antes de implementar — @AlbertoLacambra

<!-- harness:resultado -->
