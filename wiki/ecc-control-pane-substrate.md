# ECC — Control-pane substrate

**Summary** : Couche de contrôle harness-neutre introduite par ECC v2.0.0 — des adapters de session (`ecc.session.v1`) unifient Claude Code, Codex, OpenCode et dmux sous une même interface, avec un prototype Rust `ecc2/` et des snapshots d'état pour le handoff.

**Sources** : affaan-m-ecc-2-0-0-release-notes.md, affaan-m-ecc-2-0-0-rc1-notes.md

**Last updated** : 2026-06-11

---

## Contenu

Le **control-pane substrate** est la pièce maîtresse de la v2.0.0 d'[ECC](ecc-overview.md) : il transforme ECC d'un bundle de skills en véritable « agent harness operating system ». L'idée est de **rendre les harnesses interchangeables** derrière une interface commune (source: affaan-m-ecc-2-0-0-release-notes.md).

### Session adapters (`ecc.session.v1`)

Des adapters de session harness-neutres exposent une vue unifiée des sessions à travers **Claude Code, Codex, OpenCode et dmux** (source: affaan-m-ecc-2-0-0-release-notes.md). Conséquence : un même workflow opérateur (skills, rules, hooks, conventions MCP, release gates) fonctionne quel que soit le harness sous-jacent, Claude Code restant « first-class ».

Cette abstraction est une application concrète de la définition du [harness](harness-definition-et-philosophie.md) : tout ce qui entoure les poids du modèle est ici factorisé en une couche réutilisable.

### Prototype Rust `ecc2/`

La v2.0.0-rc.1 a introduit un **control-plane Rust en alpha** dans le répertoire `ecc2/`, qui build localement et expose les commandes `dashboard`, `start`, `sessions`, `status`, `stop`, `resume`, `daemon` (source: affaan-m-ecc-2-0-0-rc1-notes.md). C'est un alpha, pas encore une release générale.

### Operator status snapshots

`ecc status --markdown --write status.md` sérialise le state store local en un **handoff portable** couvrant : readiness, sessions actives, santé des skill-runs, santé de l'install, événements de gouvernance en attente, et work items liés (Linear/GitHub) (source: affaan-m-ecc-2-0-0-rc1-notes.md).

Mécanismes associés :
- `ecc work-items upsert ...` — entrées manuelles
- `ecc work-items sync-github --repo owner/repo` — état de la file PR/issue
- `ecc status --exit-code` — fait échouer l'automatisation quand la readiness demande attention

Ce snapshot est l'incarnation outillée du [pattern de stockage de session](session-storage-pattern.md) et du [clean handoff](session-clean-handoff.md) : un état d'agent durable, portable et vérifiable entre sessions.

### Pourquoi ça compte

Le control-pane sépare **l'orchestration de l'exécution** : les skills et agents (couche exécution) ne dépendent plus du harness précis, et l'état vit dans un substrat commun. Cela rejoint la logique d'[architecture par sous-agents](subagent-architecture.md) et prépare le terrain pour la [famille d'orchestrateurs orch-*](ecc-orchestrator-family.md).

## Related pages

- [ecc-overview](ecc-overview.md)
- [ecc-orchestrator-family](ecc-orchestrator-family.md)
- [harness-definition-et-philosophie](harness-definition-et-philosophie.md)
- [session-storage-pattern](session-storage-pattern.md)
- [session-clean-handoff](session-clean-handoff.md)
- [subagent-architecture](subagent-architecture.md)
