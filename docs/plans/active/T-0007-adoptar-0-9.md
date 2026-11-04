---
id: T-0007
title: Adoptar el estándar 0.9.1 con despliegue en Pages y revisor informativo
owner: "@AlbertoLacambra"
status: in_progress
risk: alto
created: 2026-10-30
acceptance:
  - id: AC1
    description: La instancia cumple N1 del estándar 0.9.1 sin errores ni avisos (sandbox, workflows seguros, runbook de rollback, sin deriva de componentes)
    check: "harness check --strict"
  - id: AC2
    description: El índice de tareas está al día
    check: "harness tasks index --check"
  - id: AC3
    description: El sitio versionado coincide con lo que genera el script
    check: "python3 scripts/generar_sitio.py --check"
  - id: AC4
    description: El sitio publicado sirve un SHA (primer despliegue verificado tras fusionar el PR de adopción)
    check: "curl -fsS https://alacambrapocs.github.io/harness-example-greenfield/version.txt | grep -Eq '^[0-9a-f]{40}$'"
---

# T-0007 · Adoptar el estándar 0.9.1 con despliegue en Pages y revisor informativo

<!-- harness:objetivo -->
## Objetivo
El repositorio declara el estándar 0.9.1 (F5.2–F5.7): clase de riesgo calculada con puerta de aprobación, comprobación de plataforma programada, sandbox, despliegue en GitHub Pages con verificación y rollback, runbook de rollback y revisor informativo en modo simulador.

<!-- harness:alcance -->
## Alcance
- Dentro: manifiesto, `.claude/`, `.harness/`, `.github/workflows/`, `AGENTS.md`, `site/`, `scripts/generar_sitio.py`, `tests/test_sitio.py` y `docs/runbooks/`.
- Fuera de alcance: `src/` (la funcionalidad nueva va en T-0008).

<!-- harness:plan -->
## Plan
1. Preparar la plataforma: Pages con origen Actions, environments `github-pages` y `aprobacion-riesgo-alto`, check `tasks / puerta riesgo alto` en el ruleset (guía F5.7, §1).
2. PR de adopción (este): riesgo `alto`, pasa por la puerta.
3. Tras fusionar: primer despliegue verificado y `harness platform check` sin errores.
4. Cerrar con `cerrar-tarea` en una sesión de Claude Code (medición de confirmaciones, F3.8).

<!-- harness:progreso -->
## Progreso
- 2026-10-30 — workflows a `cli-v0.9.1-rc.1`, `harness-platform.yml`, sandbox en `settings.json`, componentes sincronizados y `despliegue-pages` 0.2.0 y `revisor-informativo` 0.1.0 instalados — Claude a nombre de @AlbertoLacambra

<!-- harness:decisiones -->
## Decisiones
- 2026-10-30 — El runbook de rollback es contenido de la instancia, no archivo del componente (H-22) — Claude
- 2026-10-30 — El revisor queda en `MODO=simulador` (D-055): sin clave de modelo en el laboratorio — Claude

<!-- harness:resultado -->
## Resultado
