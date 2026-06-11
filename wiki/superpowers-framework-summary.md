# Superpowers — Framework de skills agentiques

**Summary** : Méthodologie de développement logiciel pour agents de code, construite sur des skills composables qui se déclenchent automatiquement, créée par obra (Jesse Vincent).

**Sources** : obra-superpowers-readme.md

**Last updated** : 2026-06-11

---

## Contenu

**Superpowers** est une méthodologie de développement logiciel complète pour les agents de code (*coding agents*), construite sur deux ingrédients :

1. un ensemble de **skills composables** (compétences réutilisables) ;
2. des **instructions initiales** qui garantissent que l'agent invoque ces skills au bon moment.

L'idée directrice : l'agent ne saute pas directement dans l'écriture de code. Dès qu'il détecte une intention de construction, il **prend du recul** et interroge l'utilisateur sur le besoin réel avant d'agir (source: obra-superpowers-readme.md).

### Mode de fonctionnement

Le cycle naturel décrit par le framework :

1. L'agent **tease un spec** depuis la conversation, puis le présente par morceaux assez courts pour être lus et validés.
2. Après validation du design, il rédige un **plan d'implémentation** suffisamment clair pour qu'un « junior enthousiaste sans goût, sans jugement, sans contexte projet et allergique aux tests » puisse le suivre. Le plan met l'accent sur le TDD red/green, [YAGNI](https://github.com/obra/superpowers) et DRY.
3. Sur ordre (« go »), il lance un processus de **développement piloté par sous-agents** — voir [subagent-driven-development](subagent-driven-development.md) — capable de travailler en autonomie plusieurs heures sans dévier du plan.

Le déclenchement étant **automatique**, l'utilisateur n'a rien de spécial à faire : l'agent « a simplement des Superpowers ».

### Déclenchement automatique des skills

Le principe central : **l'agent vérifie les skills pertinents avant toute tâche**. Ce sont des *workflows obligatoires*, pas des suggestions (source: obra-superpowers-readme.md). Ce mécanisme de triggering rejoint les questions de design abordées dans [skill-description-optimization](skill-description-optimization.md).

### Multi-harness

Superpowers ne cible pas un seul agent. Le framework s'installe sur : Claude Code, Codex CLI, Codex App, Factory Droid, Gemini CLI, OpenCode, Cursor et GitHub Copilot CLI. C'est donc un patron de [skill](skill-anatomy.md) portable entre harnesses.

### Bibliothèque de skills (catégories)

Le README organise les skills en quatre familles :

- **Testing** : `test-driven-development` (cycle RED-GREEN-REFACTOR + anti-patterns de test).
- **Debugging** : `systematic-debugging` (processus en 4 phases : root-cause-tracing, defense-in-depth, condition-based-waiting), `verification-before-completion`.
- **Collaboration** : `brainstorming`, `writing-plans`, `executing-plans`, `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`, `using-git-worktrees`, `finishing-a-development-branch`, `subagent-driven-development`.
- **Meta** : `writing-skills` (créer de nouveaux skills), `using-superpowers` (introduction au système).

Ces skills s'enchaînent dans un pipeline — voir [superpowers-workflow-pipeline](superpowers-workflow-pipeline.md).

### Philosophie

Quatre principes affichés (source: obra-superpowers-readme.md) :

- **Test-Driven Development** — écrire les tests d'abord, toujours.
- **Systematic over ad-hoc** — un processus plutôt que de deviner.
- **Complexity reduction** — la simplicité comme objectif premier.
- **Evidence over claims** — vérifier avant de déclarer le succès.

Ces principes résonnent avec [completion-evidence-executable](completion-evidence-executable.md) (« done » = preuve exécutable) et [end-to-end-verification-only](end-to-end-verification-only.md).

> Annonce de sortie originale : [blog.fsck.com — Superpowers (oct. 2025)](https://blog.fsck.com/2025/10/09/superpowers/).

### Note d'auto-référence

Ce framework est celui chargé dans la session Claude Code qui maintient ce wiki : les skills `superpowers:*` (brainstorming, writing-plans, test-driven-development, etc.) proviennent de ce dépôt.

## Related pages

- [superpowers-workflow-pipeline](superpowers-workflow-pipeline.md)
- [subagent-driven-development](subagent-driven-development.md)
- [skill-anatomy](skill-anatomy.md)
- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [metaprompting](metaprompting.md)
- [ecc-overview](ecc-overview.md)
