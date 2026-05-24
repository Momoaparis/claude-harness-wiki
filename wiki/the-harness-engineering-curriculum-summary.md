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
- **Positionnement** : complète [[the-longform-guide-summary]] et [[ecc-overview]] par une approche curriculum-style

### Le diagnostic central (Lecture 01)

Les modèles forts (SWE-bench ~60%) échouent en production (~40% de succès net). Ce n'est pas un problème de modèle, c'est un problème de **harness**. Tout ce qui n'est pas les poids du modèle — instructions, tools, environnement, state, feedback — détermine combien de la capacité du modèle se traduit en travail réel.

Voir [[harness-definition-et-philosophie]], [[five-failure-modes-agents-en-prod]].

### Les 5 subsystèmes (Lecture 02)

Une harness complète = 5 composants : Instructions, Tools, Environment, State, Feedback. Étude de cas Anthropic : même modèle, taux de succès 20% → 100% en ajoutant les subsystèmes manquants. Voir [[five-subsystem-harness-architecture]].

### Les 12 thèmes du curriculum

| Lecture | Thème central | Page wiki principale |
|---------|---------------|---------------------|
| 01 | Pourquoi les modèles forts échouent | [[five-failure-modes-agents-en-prod]] |
| 02 | Définition d'une harness | [[five-subsystem-harness-architecture]] |
| 03 | Repo = système d'enregistrement | [[repository-as-system-of-record]] |
| 04 | Instructions modulaires | [[modular-instruction-architecture]] |
| 05 | Contexte multi-session | [[cross-session-context-loss]] |
| 06 | Phase d'initialisation dédiée | [[initialization-phase-separation]] |
| 07 | Limites de scope claires (WIP=1) | [[wip-limit-discipline]] |
| 08 | Feature lists comme primitives | [[feature-list-as-primitive]] |
| 09 | Empêcher "victoire prématurée" | [[three-layer-termination-validation]] |
| 10 | Seul l'end-to-end vérifie | [[end-to-end-verification-only]] |
| 11 | Observabilité runtime + process | [[observability-runtime-vs-process]] |
| 12 | Handoff propre en fin de session | [[session-clean-handoff]] |

### Les 6 projets pratiques

Voir [[harness-curriculum-projects-overview]]. Progression : baseline (P01) → workspace lisible (P02) → continuité multi-session (P03) → feedback runtime (P04) → role separation (P05) → harness complet + ablation (P06).

### Les templates concrets

Le cours fournit 7 templates copy-paste pour démarrer immédiatement :

- [[template-claude-md]] — fichier root d'instructions (Claude Code et variant AGENTS.md pour Codex)
- [[template-claude-progress-md]] — journal de session
- [[template-feature-list-json]] — état machine-lisible des features
- [[template-session-handoff-md]] — note de transition inter-session
- [[template-clean-state-checklist]] — checklist 6-points de clôture
- [[template-evaluator-rubric]] — grille d'évaluation 6 dimensions

### Concepts-clés extraits dans le wiki

#### Fondamentaux
- [[harness-definition-et-philosophie]]
- [[five-subsystem-harness-architecture]]
- [[five-failure-modes-agents-en-prod]]
- [[harness-rot-et-dette-technique]]

#### Repository = SSoT
- [[repository-as-system-of-record]]
- [[fresh-session-readability-test]]
- [[acid-principles-agent-state]]

#### Instructions modulaires
- [[modular-instruction-architecture]]
- [[lost-in-the-middle-effect]]
- [[instruction-design-patterns]]

#### Continuité multi-session
- [[cross-session-context-loss]]
- [[context-anxiety-modeles]]
- [[progress-file-pattern]]
- [[decision-log-pattern]]
- [[compaction-vs-reset-strategie]]

#### Initialisation
- [[initialization-phase-separation]]
- [[startup-readiness-checklist]]
- [[task-breakdown-structure]]

#### Contrôle de scope
- [[wip-limit-discipline]]
- [[completion-evidence-executable]]
- [[verified-completion-rate-metric]]
- [[atomic-task-decomposition]]

#### Feature lists
- [[feature-list-as-primitive]]
- [[feature-state-machine]]
- [[harness-pipeline-scheduler-verifier-handoff]]

#### Vérification
- [[three-layer-termination-validation]]
- [[confidence-calibration-bias]]
- [[worker-checker-separation]]
- [[end-to-end-verification-only]]
- [[architectural-boundary-enforcement]]

#### Observabilité
- [[observability-runtime-vs-process]]
- [[sprint-contract-pattern]]
- [[planner-generator-evaluator-3-agent-architecture]]

#### Handoff & entropie
- [[session-clean-handoff]]
- [[harness-entropy-management]]

#### Pratique
- [[harness-curriculum-projects-overview]]
- [[ablation-study-methodology]]

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

- [[ecc-overview]] est ton bundle perso ECC ; ce curriculum fournit la **théorie** que ECC opérationnalise.
- [[the-longform-guide-summary]] couvre les techniques avancées Claude Code ; ce curriculum couvre la **discipline** d'opération.
- [[agent-observability]] cadrait jusqu'ici la couche runtime ; [[observability-runtime-vs-process]] ajoute la couche process.
- [[session-storage-pattern]] décrit le pattern `.tmp` ; [[progress-file-pattern]] et [[decision-log-pattern]] formalisent les artefacts du curriculum.

### Philosophie centrale à retenir

> "If it is not model weights, it is harness. Your harness determines how much of the model's capability gets realized." (Lecture 02)

> "Information that doesn't exist in the repo, doesn't exist for the agent." (Lecture 03)

> "Done ≠ 'code looks fine'. Done = 'behavior passes tests'." (Lecture 09)

> "Clean up later means never clean up." (Lecture 12)

## Related pages

- [[ecc-overview]]
- [[the-longform-guide-summary]]
- [[the-agentic-security-summary]]
- Index complet : [[index]]
