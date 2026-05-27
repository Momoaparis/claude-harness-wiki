# Learn Harness Engineering — Résumé du curriculum

**Summary** : Cours en 12 lectures + 6 projets pratiques (walkinglabs.github.io) qui codifie comment construire une infrastructure (harness) autour de Claude Code / Codex pour transformer un modèle capable en agent réellement fiable. Cœur du cours : le repo est le système d'enregistrement, l'agent est borné par des contraintes mécaniques, et "fait" se prouve par exécution observable — jamais par sentiment.

**Sources** : `raw/ingested/lecture-01-*.txt` à `lecture-12-*.md`, `raw/ingested/project-01-*.txt` à `project-06-*.txt`, `raw/ingested/template-*.{md,txt}`, `raw/ingested/english-reference.txt`, `raw/ingested/openai-advanced-pack.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Métadonnées de la source

- **Site** : https://walkinglabs.github.io/learn-harness-engineering/en/
- **Format** : 12 lectures théoriques + 6 projets hands-on + 8 templates + Resource library
- **Cible** : ingénieurs construisant leurs propres harnesses pour agents codeurs (Claude Code, Codex, Cursor)
- **Positionnement** : complète [the-longform-guide-summary](the-longform-guide-summary.md) et [ecc-overview](ecc-overview.md) par une approche curriculum-style

### Le diagnostic central (Lecture 01)

Les modèles forts (SWE-bench ~60%) échouent en production (~40% de succès net). Ce n'est pas un problème de modèle, c'est un problème de **harness**. Tout ce qui n'est pas les poids du modèle — instructions, tools, environnement, state, feedback — détermine combien de la capacité du modèle se traduit en travail réel.

Voir [harness-definition-et-philosophie](harness-definition-et-philosophie.md), [five-failure-modes-agents-en-prod](five-failure-modes-agents-en-prod.md).

### Les 5 subsystèmes (Lecture 02)

Une harness complète = 5 composants : Instructions, Tools, Environment, State, Feedback. Étude de cas Anthropic : même modèle, taux de succès 20% → 100% en ajoutant les subsystèmes manquants. Voir [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md).

### Les 12 thèmes du curriculum

| Lecture | Thème central | Page wiki principale |
|---------|---------------|---------------------|
| 01 | Pourquoi les modèles forts échouent | [five-failure-modes-agents-en-prod](five-failure-modes-agents-en-prod.md) |
| 02 | Définition d'une harness | [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md) |
| 03 | Repo = système d'enregistrement | [repository-as-system-of-record](repository-as-system-of-record.md) |
| 04 | Instructions modulaires | [modular-instruction-architecture](modular-instruction-architecture.md) |
| 05 | Contexte multi-session | [cross-session-context-loss](cross-session-context-loss.md) |
| 06 | Phase d'initialisation dédiée | [initialization-phase-separation](initialization-phase-separation.md) |
| 07 | Limites de scope claires (WIP=1) | [wip-limit-discipline](wip-limit-discipline.md) |
| 08 | Feature lists comme primitives | [feature-list-as-primitive](feature-list-as-primitive.md) |
| 09 | Empêcher "victoire prématurée" | [three-layer-termination-validation](three-layer-termination-validation.md) |
| 10 | Seul l'end-to-end vérifie | [end-to-end-verification-only](end-to-end-verification-only.md) |
| 11 | Observabilité runtime + process | [observability-runtime-vs-process](observability-runtime-vs-process.md) |
| 12 | Handoff propre en fin de session | [session-clean-handoff](session-clean-handoff.md) |

### Les 6 projets pratiques

Voir [harness-curriculum-projects-overview](harness-curriculum-projects-overview.md). Progression : baseline (P01) → workspace lisible (P02) → continuité multi-session (P03) → feedback runtime (P04) → role separation (P05) → harness complet + ablation (P06).

### Les templates concrets

Le cours fournit 7 templates copy-paste pour démarrer immédiatement :

- [template-claude-md](template-claude-md.md) — fichier root d'instructions (Claude Code et variant AGENTS.md pour Codex)
- [template-claude-progress-md](template-claude-progress-md.md) — journal de session
- [template-feature-list-json](template-feature-list-json.md) — état machine-lisible des features
- [template-session-handoff-md](template-session-handoff-md.md) — note de transition inter-session
- [template-clean-state-checklist](template-clean-state-checklist.md) — checklist 6-points de clôture
- [template-evaluator-rubric](template-evaluator-rubric.md) — grille d'évaluation 6 dimensions

### Concepts-clés extraits dans le wiki

#### Fondamentaux
- [harness-definition-et-philosophie](harness-definition-et-philosophie.md)
- [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md)
- [five-failure-modes-agents-en-prod](five-failure-modes-agents-en-prod.md)
- [harness-rot-et-dette-technique](harness-rot-et-dette-technique.md)

#### Repository = SSoT
- [repository-as-system-of-record](repository-as-system-of-record.md)
- [fresh-session-readability-test](fresh-session-readability-test.md)
- [acid-principles-agent-state](acid-principles-agent-state.md)

#### Instructions modulaires
- [modular-instruction-architecture](modular-instruction-architecture.md)
- [lost-in-the-middle-effect](lost-in-the-middle-effect.md)
- [instruction-design-patterns](instruction-design-patterns.md)

#### Continuité multi-session
- [cross-session-context-loss](cross-session-context-loss.md)
- [context-anxiety-modeles](context-anxiety-modeles.md)
- [progress-file-pattern](progress-file-pattern.md)
- [decision-log-pattern](decision-log-pattern.md)
- [compaction-vs-reset-strategie](compaction-vs-reset-strategie.md)

#### Initialisation
- [initialization-phase-separation](initialization-phase-separation.md)
- [startup-readiness-checklist](startup-readiness-checklist.md)
- [task-breakdown-structure](task-breakdown-structure.md)

#### Contrôle de scope
- [wip-limit-discipline](wip-limit-discipline.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [verified-completion-rate-metric](verified-completion-rate-metric.md)
- [atomic-task-decomposition](atomic-task-decomposition.md)

#### Feature lists
- [feature-list-as-primitive](feature-list-as-primitive.md)
- [feature-state-machine](feature-state-machine.md)
- [harness-pipeline-scheduler-verifier-handoff](harness-pipeline-scheduler-verifier-handoff.md)

#### Vérification
- [three-layer-termination-validation](three-layer-termination-validation.md)
- [confidence-calibration-bias](confidence-calibration-bias.md)
- [worker-checker-separation](worker-checker-separation.md)
- [end-to-end-verification-only](end-to-end-verification-only.md)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md)

#### Observabilité
- [observability-runtime-vs-process](observability-runtime-vs-process.md)
- [sprint-contract-pattern](sprint-contract-pattern.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)

#### Handoff & entropie
- [session-clean-handoff](session-clean-handoff.md)
- [harness-entropy-management](harness-entropy-management.md)

#### Pratique
- [harness-curriculum-projects-overview](harness-curriculum-projects-overview.md)
- [ablation-study-methodology](ablation-study-methodology.md)

### Sources & références externes citées

- **OpenAI 2026** — agent-first repos, repo-local context, structural guardrails
- **Anthropic novembre 2025** — initializer agents, feature lists, context-window handoffs
- **Anthropic mars 2026** — planner/generator/evaluator + context resets (étude DAW, $124.70 pour 3h50m)
- **Liu et al. 2023** — "Lost in the Middle" (effet de position dans les longs contextes)
- **Guo et al. 2017** — calibration bias des réseaux neuronaux modernes
- **Lehman's laws** — croissance entropique des logiciels sous changement continu
- **Steve McConnell** — *Rapid Development* (scope creep)
- **David Anderson** — *Kanban*, principes WIP

### Lien avec le reste du wiki

- [ecc-overview](ecc-overview.md) est ton bundle perso ECC ; ce curriculum fournit la **théorie** que ECC opérationnalise.
- [the-longform-guide-summary](the-longform-guide-summary.md) couvre les techniques avancées Claude Code ; ce curriculum couvre la **discipline** d'opération.
- [agent-observability](agent-observability.md) cadrait jusqu'ici la couche runtime ; [observability-runtime-vs-process](observability-runtime-vs-process.md) ajoute la couche process.
- [session-storage-pattern](session-storage-pattern.md) décrit le pattern `.tmp` ; [progress-file-pattern](progress-file-pattern.md) et [decision-log-pattern](decision-log-pattern.md) formalisent les artefacts du curriculum.

### Philosophie centrale à retenir

> "If it is not model weights, it is harness. Your harness determines how much of the model's capability gets realized." (Lecture 02)

> "Information that doesn't exist in the repo, doesn't exist for the agent." (Lecture 03)

> "Done ≠ 'code looks fine'. Done = 'behavior passes tests'." (Lecture 09)

> "Clean up later means never clean up." (Lecture 12)

## Related pages

- [ecc-overview](ecc-overview.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
- Index complet : [index](index.md)
