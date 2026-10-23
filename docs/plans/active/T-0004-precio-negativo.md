---
id: T-0004
title: Rechazar precios negativos en total()
owner: "@AlbertoLacambra"
status: in_progress
risk: bajo
created: 2026-10-22
issue: 8
acceptance:
  - id: AC1
    description: total() lanza ValueError indicando la línea si un precio es negativo
    check: "python3 -m unittest tests.test_app.TotalTest.test_precio_negativo"
  - id: AC2
    description: Las pruebas existentes siguen pasando
    check: "python3 -m unittest discover -s tests"
---

# T-0004 · Rechazar precios negativos en total()

<!-- harness:objetivo -->
## Objetivo
Un pedido con un precio unitario negativo no produce un total: `total()` lo rechaza con `ValueError` y un mensaje que indica la línea, igual que con las cantidades (T-0002).

<!-- harness:alcance -->
## Alcance
- Dentro: `src/app.py` y `tests/test_app.py`.
- Fuera de alcance: descuentos (se modelarán aparte).

<!-- harness:plan -->
## Plan
1. Añadir la prueba `test_precio_negativo`.
2. Validar los precios en `total()`.
3. Verificar con el subagente `verificador` y cerrar con la skill `cerrar-tarea`.

<!-- harness:progreso -->
## Progreso
- [ ] (pendiente; la hará Claude Code en la F3.6)

<!-- harness:decisiones -->
## Decisiones
- 2026-10-22 — AC1 nombra la prueba exacta antes de implementar — @AlbertoLacambra

<!-- harness:resultado -->
## Resultado
(Se rellena al pasar a done.)
