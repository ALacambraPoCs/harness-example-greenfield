---
id: T-0011
title: Las pruebas de total() viven en tests/test_total.py
owner: "@AlbertoLacambra"
status: done
done_pr: 27
risk: medio
created: 2026-11-06
acceptance:
  - id: AC1
    description: Las pruebas de total() están en tests/test_total.py y tests/test_app.py ya no existe
    check: "test -f tests/test_total.py && test ! -e tests/test_app.py"
  - id: AC2
    description: Todas las pruebas siguen pasando
    check: "python3 -m unittest discover -s tests"
---

# T-0011 · Las pruebas de total() viven en tests/test_total.py

<!-- harness:objetivo -->
## Objetivo
Cada módulo tiene su archivo de pruebas con su nombre (`test_total.py` para `total()`, `test_sitio.py` para el sitio). Renombrar un archivo de pruebas es una señal de riesgo `medio` (D-058): esta tarea es el escenario `medio` de la medición de cierre de la Fase 5 (C-8).

<!-- harness:alcance -->
## Alcance
- Dentro: `tests/test_app.py` → `tests/test_total.py` (con `git mv`, sin cambiar las pruebas).
- Fuera de alcance: `src/`, `site/`, workflows y configuración.

<!-- harness:plan -->
## Plan
1. `git mv tests/test_app.py tests/test_total.py`.
2. `check` en verde.
3. PR de riesgo `medio` y cierre con `cerrar-tarea` en el mismo PR (`ready → done`, C-4).

<!-- harness:progreso -->
## Progreso
- 2026-11-06 — cerrada en el PR #27 — @AlbertoLacambra

<!-- harness:decisiones -->
## Decisiones

<!-- harness:resultado -->
## Resultado
Renombrado tests/test_app.py a tests/test_total.py con git mv, sin cambiar las pruebas. check y AC1/AC2 en verde. Pendiente: nada; tests/test_sitio.py sigue como está (fuera de alcance).
