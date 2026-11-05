---
id: T-0009
title: El rollback automático del despliegue se ejecuta tras un fallo de verificación
owner: "@AlbertoLacambra"
status: done
done_pr: 24
risk: alto
created: 2026-11-05
acceptance:
  - id: AC1
    description: La instancia cumple N1 sin errores ni avisos, con despliegue-pages 0.2.1 sin deriva
    check: "harness check --strict"
  - id: AC2
    description: Los jobs revertir y verificar-reversion se ejecutan aunque falle verificar (always() y resultado del predecesor)
    check: "grep -q \"if: always() && needs.construir-reversion.result == 'success'\" .github/workflows/despliegue-pages.yml && grep -q \"if: always() && needs.revertir.result == 'success'\" .github/workflows/despliegue-pages.yml"
  - id: AC3
    description: El índice de tareas está al día
    check: "harness tasks index --check"
---

# T-0009 · El rollback automático del despliegue se ejecuta tras un fallo de verificación

<!-- harness:objetivo -->
## Objetivo
Que un fallo de `verificar` lleve de verdad a `revertir` y `verificar reversión`. En el ensayo de la F5.7 se saltaron (H-30) y el sitio quedó sirviendo la versión del ensayo.

<!-- harness:alcance -->
## Alcance
- Dentro: `.github/workflows/` (componente `despliegue-pages` 0.2.1 y `cli-ref` 0.9.2), `.harness/components.lock`.
- Fuera de alcance: `src/` y `site/`.

<!-- harness:plan -->
## Plan
1. PR con `harness components sync` (este): riesgo `alto`, pasa por la puerta.
2. Repetir el ensayo de rollback: debe acabar sirviendo HEAD con la issue «… (rollback: success)».
3. Cerrar la tarea con la evidencia del ensayo y actualizar `revisado` en el runbook.

<!-- harness:progreso -->
## Progreso
- 2026-11-05 — `despliegue-pages` 0.2.0 → 0.2.1 y workflows a `cli-v0.9.2-rc.1` — Claude a nombre de @AlbertoLacambra
- 2026-11-05 — cerrada en el PR #24 — @AlbertoLacambra

<!-- harness:decisiones -->
## Decisiones
- 2026-11-05 — El sitio se restauró antes con un despliegue manual de HEAD (runbook), sin esperar a esta corrección — @AlbertoLacambra

<!-- harness:resultado -->
## Resultado
Objetivo cumplido: un fallo de verificar ahora lleva a revertir y verificar reversión (condiciones always() en despliegue-pages 0.2.1, cli-v0.9.2-rc.1). Ensayo de rollback correcto en la issue #23 (rollback: success), con el sitio sirviendo de nuevo HEAD; runbook rollback-pages con revisado 2026-11-05. Pendiente: nada en esta tarea; el comentario de cierre de la issue #23 contiene un marcador sin rellenar (<enlace al run #8>).
