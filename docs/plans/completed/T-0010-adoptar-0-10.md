---
id: T-0010
title: Adoptar el estándar 0.10.0 (cierre de la Fase 5)
owner: "@AlbertoLacambra"
status: done
done_pr: 28
risk: alto
created: 2026-11-06
acceptance:
  - id: AC1
    description: La instancia cumple N1 del estándar 0.10.0 sin errores ni avisos (incluye HS-CI-010 y componentes sin deriva)
    check: "harness check --strict"
  - id: AC2
    description: El índice de tareas está al día
    check: "harness tasks index --check"
---

# T-0010 · Adoptar el estándar 0.10.0 (cierre de la Fase 5)

<!-- harness:objetivo -->
## Objetivo
El repositorio declara el estándar 0.10.0, que recoge las correcciones del cierre de la Fase 5:
- C-1: origen de los checks y bypass de administradores comprobados por `platform check`.
- C-3: permisos de `git -C … push`, `git fetch`, `git switch -c` y `gh issue view`.
- C-4: `ready → done` en un PR.
- C-5: la puerta falla cerrada.
- C-6: `despliegue-pages` 0.2.2.
- C-7: hook 0.3.2.

<!-- harness:alcance -->
## Alcance
- Dentro: manifiesto, `.claude/`, `.harness/components.lock` y `.github/workflows/`.
- Fuera de alcance: `src/` y `tests/` (el escenario de riesgo `medio` va en T-0011).

<!-- harness:plan -->
## Plan
1. PR de adopción (este): riesgo `alto`, pasa por la puerta.
2. `harness platform check` con 0.10.0: origen de los checks y bypass (C-1).
3. Medición C-8 con T-0011 y cierre de esta tarea.

<!-- harness:progreso -->
## Progreso
- 2026-11-06 — workflows a `cli-v0.10.0-rc.1`, `settings.json` alineado con la plantilla 0.10.0 y componentes sincronizados — Claude a nombre de @AlbertoLacambra
- 2026-11-06 — cerrada en el PR #28 — @AlbertoLacambra

<!-- harness:decisiones -->
## Decisiones

<!-- harness:resultado -->
## Resultado
Repositorio adoptado al estándar 0.10.0 (C-1 a C-7): harness check --strict en N1 sin errores ni avisos y AC2 al día. La medición C-8 se hizo en T-0011 (PR #27); no queda nada pendiente.
