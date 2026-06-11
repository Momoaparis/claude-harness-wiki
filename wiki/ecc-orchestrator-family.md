# ECC — Famille d'orchestrateurs `orch-*`

**Summary** : Famille de skills `orch-*` introduite par ECC v2.0.0 pour l'orchestration dynamique d'équipes de workflow — coordonner plusieurs agents/skills sous un même plan plutôt que d'exécuter des tâches isolées.

**Sources** : affaan-m-ecc-2-0-0-release-notes.md

**Last updated** : 2026-06-11

---

## Contenu

La **famille `orch-*`** est une surface d'orchestration ajoutée dans la v2.0.0 d'[ECC](ecc-overview.md), accompagnée d'une **dynamic workflow team orchestration** (source: affaan-m-ecc-2-0-0-release-notes.md). Là où une skill classique exécute un workflow, un orchestrateur `orch-*` **coordonne une équipe** de skills/agents : il décompose, dispatche, suit l'avancement et recompose les résultats.

### Place dans l'écosystème

Cette famille s'appuie directement sur le [control-pane substrate](ecc-control-pane-substrate.md) : parce que les sessions sont harness-neutres (`ecc.session.v1`), un orchestrateur peut piloter des agents au travers de Claude Code, Codex ou OpenCode de façon uniforme.

### Lien avec les patterns d'orchestration du wiki

`orch-*` est l'opérationnalisation chez ECC de plusieurs patterns déjà documentés :

- [subagent-driven-development](subagent-driven-development.md) — un sous-agent frais par tâche + revue à deux étapes.
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md) — séparation planificateur / générateur / évaluateur.
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md) — boucle orchestrateur ↔ sous-agent bornée.
- [subagent-architecture](subagent-architecture.md) — déléguer chaque tâche au modèle le moins cher suffisant.

La nouveauté d'`orch-*` est de packager ces patterns en **skills invocables** plutôt qu'en conventions à reconstruire à chaque session, et d'y greffer une orchestration d'équipe **dynamique** (composition décidée au runtime).

### Optimization pack associé

La v2.0.0 livre aussi un pack d'optimisation qui se combine avec l'orchestration : `parallel-execution-optimizer`, `benchmark-optimization-loop`, `data-throughput-accelerator`, `latency-critical-systems`, `recursive-decision-ledger` (source: affaan-m-ecc-2-0-0-release-notes.md). Ces skills transforment des prompts répétés de vitesse/récursion en workflows bornés de benchmark, throughput et journal de décision.

## Related pages

- [ecc-overview](ecc-overview.md)
- [ecc-control-pane-substrate](ecc-control-pane-substrate.md)
- [subagent-driven-development](subagent-driven-development.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
- [subagent-architecture](subagent-architecture.md)
