# Observabilité runtime vs process

**Summary** : Une harness mature a **deux couches** d'observabilité. **Runtime** : signaux système (logs, traces, état des process) répondent à "qu'a fait le système". **Process** : artefacts décisionnels (sprint contracts, rubrics, task traces) répondent à "pourquoi cette décision était justifiée". Les deux se renforcent mutuellement.

**Sources** : `raw/ingested/lecture-11-making-the-agents-runtime-observable.md`

**Last updated** : 2026-05-24

---

## Contenu

### La distinction critique

> "Code review shows 'what was written'; runtime tracing shows 'what actually ran.'" — Lecture 11

| Couche | Question | Artefacts typiques |
|--------|----------|---------------------|
| **Runtime observability** | Que a-t-il fait ? | Logs, traces, métriques, health checks, OpenTelemetry |
| **Process observability** | Pourquoi cette décision était bonne ? | Sprint contracts, evaluator rubrics, task traces, decision logs |

L'une sans l'autre = aveugle à la moitié de la réalité.

### Pourquoi les deux

#### Runtime seule

Tu sais que la requête a échoué, à 14h32, sur ce endpoint. Mais tu ne sais pas **si c'était attendu** (l'agent testait un cas d'erreur ?) ou un vrai bug.

#### Process seule

Tu sais que le sprint contract spécifiait "implémenter login". Mais tu ne sais pas **si ça marche réellement** sans signaux runtime.

#### Les deux

```
Runtime: "login endpoint returned 500"
Process: "evaluator rubric scored 'reliability: 0/2'"
Conclusion: bug confirmé, agent ne savait pas, evaluator l'a détecté → re-iterate
```

### Runtime observability

Voir [agent-observability](agent-observability.md) (page existante du wiki) pour le socle. Le curriculum **étend** avec :

#### Signal collection automatique

> "Don't rely on the agent to log itself; the harness must capture proactively." — Lecture 11

Logger automatiquement (via hooks, instrumentation) :

- **Lifecycle** : startup, ready, running, shutdown
- **Feature paths** : checkpoints au passage de chaque feature critique
- **Data flow** : input/output des fonctions clés
- **Resource utilization** : memory creep, file handles, connections
- **Errors** : full context (stack, params, env)

#### OpenTelemetry standardisation

```
trace per session
  ├── span per task
  │     ├── sub-span: lint
  │     ├── sub-span: tests
  │     └── sub-span: e2e verification
  └── span per session-end
```

Backends recommandés : Jaeger, Zipkin (self-hosted), Honeycomb, DataDog.

### Process observability — les 3 artefacts

#### 1. Sprint contract

Voir [sprint-contract-pattern](sprint-contract-pattern.md) :

```yaml
sprint: dark-mode-toggle
scope:
  - theme toggle button in header
  - CSS variables globales
  - tests visuels
verification:
  - regression tests pass
  - E2E test : toggle changes theme
  - no FOUC (flash of unstyled content)
exclusions:
  - print styles
  - third-party components
```

Capture ce qui est **attendu** avant l'écriture du code.

#### 2. Evaluator rubric

Voir [template-evaluator-rubric](template-evaluator-rubric.md) : grille de scoring structurée qui transforme l'évaluation subjective en scoring reproductible.

#### 3. Task trace

Enregistrement complet du chemin décisionnel d'une tâche, début à fin. Analogue au request tracing en systèmes distribués.

```json
{
  "task_id": "001",
  "trace": [
    {"step": "read AGENTS.md", "timestamp": "..."},
    {"step": "read feature_list.json", "timestamp": "..."},
    {"step": "decision: implement register endpoint", "reason": "..."},
    {"step": "write src/auth/register.ts", "timestamp": "..."},
    {"step": "run unit tests", "result": "247/247 passing"},
    {"step": "run e2e tests", "result": "1/1 passing"},
    {"step": "transition state to passing", "evidence": "..."}
  ]
}
```

Rejouable pour audit.

### Cas réel Anthropic mars 2026 (DAW experiment)

Build d'un DAW (Digital Audio Workstation) avec 3 agents :

| Phase | Durée | Coût | Output |
|-------|-------|------|--------|
| Planner | 4.7 min | $0.46 | Sprint contracts |
| Build R1 (Generator) | 2h 07 | $71.08 | Implementation |
| QA R1 (Evaluator) | 8.8 min | $3.24 | "DAW lacks draggable clips, synth knobs UI, effects editor" |
| Build R2 | (suite) | ... | Fix |
| QA R2 | ... | ... | Re-eval |
| Build R3 | ... | ... | Fix |
| **Total** | **3h 50** | **$124.70** | Full working DAW |

L'evaluator détecte **précisément** ce qui manque, avec rubric. Le generator corrige. **Process** observability rend possible cette boucle.

### "Information cliff" du handoff

> "Session handoff information cliff. When incomplete work is handed to the next session, missing observability means the new session has to diagnose the system state from scratch." — Lecture 11

Sans observabilité (les 2 couches) :
- Session N+1 voit seulement le code final
- Pas de raison des décisions
- Pas de signaux d'exécution
- → diagnostic from scratch (15-20 min)

Avec :
- Sprint contract → "voici ce qu'on visait"
- Rubric → "voici comment c'est évalué"
- Task trace → "voici ce qui s'est passé"
- Runtime logs → "voici le comportement actuel"
- → reprise en 3 min

Voir [cross-session-context-loss](cross-session-context-loss.md) et [rebuild cost](rebuild-cost-metric.md).

### Layered observability — design simultané

> "Observability is a harness architecture property. It's not a feature you add after the fact — it's a core capability that must be designed in from the start." — Lecture 11

Les deux couches doivent être **conçues ensemble** :

- Quand un agent commence une tâche → crée le sprint contract (process) **et** ouvre un OpenTelemetry trace (runtime)
- Quand l'evaluator score → produit la rubric (process) **et** capture les logs d'exécution (runtime)
- Quand la session finit → handoff inclut **les deux** (process artifacts + trace summary)

### Lien avec agent-observability existante

[agent-observability](agent-observability.md) couvre la **couche runtime** (logs tool calls, network attempts, OpenTelemetry, baseline session, kill switch link). Cette page **complète** avec la couche process, et formalise la distinction.

Cross-link à faire à l'avenir : étendre `agent-observability` avec une section "Process layer" pointant vers cette page.

### Evaluator reliability evolution

Note Anthropic : les premières versions d'evaluator s'auto-convainquaient de dismisser des issues valides. Correction :

1. Analyser les logs d'evaluator
2. Trouver les divergences avec jugement humain
3. Mettre à jour le QA prompt
4. Itérer

Le scoring devient **stable** après quelques itérations. C'est l'observabilité du **process** qui rend cette amélioration possible.

### Antipatterns

- ❌ Runtime sans process → "ça marche", on ne sait pas pourquoi ni si c'est désiré
- ❌ Process sans runtime → "c'était attendu", on ne sait pas si réel
- ❌ Observability ajoutée après coup → fragile, partielle
- ❌ Logs verbeux mais non-structurés → impossible à query
- ❌ Sprint contracts non-versionnés → on ne peut pas retracer

### À retenir

1. **Deux couches** : runtime (signaux exécution) + process (artefacts décisionnels).
2. Process = sprint contracts + rubrics + task traces.
3. Runtime = logs + traces + métriques (OpenTelemetry).
4. **Concevoir les deux ensemble**, pas l'une après l'autre.
5. Sans observabilité → information cliff au handoff (diagnostic from scratch).

## Related pages

- [sprint-contract-pattern](sprint-contract-pattern.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [agent-observability](agent-observability.md)
- [template-evaluator-rubric](template-evaluator-rubric.md)
- [cross-session-context-loss](cross-session-context-loss.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
