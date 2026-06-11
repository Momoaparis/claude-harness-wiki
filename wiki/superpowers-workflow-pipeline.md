# Superpowers — Pipeline de workflow en 7 étapes

**Summary** : Le pipeline de développement auto-déclenché de Superpowers — sept skills obligatoires qui s'enchaînent de l'idée floue jusqu'à la branche fusionnée.

**Sources** : obra-superpowers-readme.md

**Last updated** : 2026-06-11

---

## Contenu

Le cœur opérationnel de [Superpowers](superpowers-framework-summary.md) est une séquence de sept skills qui se déclenchent **automatiquement** au fil du travail. Chaque étape est un workflow obligatoire, pas une suggestion : l'agent vérifie les skills pertinents avant chaque tâche (source: obra-superpowers-readme.md).

### Les 7 étapes

1. **brainstorming** — *Se déclenche avant d'écrire du code.* Raffine les idées brutes par questions, explore les alternatives, présente le design par sections pour validation, puis sauvegarde un document de design.

2. **using-git-worktrees** — *Se déclenche après approbation du design.* Crée un espace de travail isolé sur une nouvelle branche, lance le setup projet, vérifie une baseline de tests propre. Voir [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md).

3. **writing-plans** — *Se déclenche avec le design approuvé.* Découpe le travail en tâches de 2 à 5 minutes chacune. Chaque tâche a des chemins de fichiers exacts, du code complet et des étapes de vérification. Rejoint la logique de [task-breakdown-structure](task-breakdown-structure.md) et [atomic-task-decomposition](atomic-task-decomposition.md).

4. **subagent-driven-development** ou **executing-plans** — *Se déclenche avec le plan.* Dispatche un sous-agent frais par tâche avec revue en deux étapes (conformité au spec, puis qualité du code), ou exécute par lots avec checkpoints humains. Détail : [subagent-driven-development](subagent-driven-development.md).

5. **test-driven-development** — *Se déclenche pendant l'implémentation.* Impose RED-GREEN-REFACTOR : écrire un test qui échoue, le regarder échouer, écrire le code minimal, le regarder passer, commiter. **Supprime le code écrit avant les tests.**

6. **requesting-code-review** — *Se déclenche entre les tâches.* Revoit le travail par rapport au plan, rapporte les problèmes par sévérité. Les problèmes critiques bloquent la progression.

7. **finishing-a-development-branch** — *Se déclenche quand les tâches sont finies.* Vérifie les tests, présente les options (merge / PR / garder / abandonner), nettoie le worktree.

### Ce qui rend le pipeline robuste

- **Déclenchement automatique** : pas d'invocation manuelle, donc pas d'oubli d'étape.
- **Validation humaine aux points clés** : design (étape 1), checkpoints (étape 4), décision de fin (étape 7).
- **Discipline TDD non négociable** : l'étape 5 supprime le code écrit hors cycle test-first — c'est la matérialisation du principe « evidence over claims ». Voir [completion-evidence-executable](completion-evidence-executable.md).
- **Autonomie longue** : la combinaison plan détaillé + sous-agents permet à l'agent de travailler « quelques heures d'affilée sans dévier du plan » (source: obra-superpowers-readme.md).

### Articulation avec le harness engineering

Ce pipeline est une instance concrète des principes formalisés ailleurs dans le wiki : séparation init/implémentation ([initialization-phase-separation](initialization-phase-separation.md)), vérification de fin exécutable ([end-to-end-verification-only](end-to-end-verification-only.md)), et handoff propre entre étapes ([session-clean-handoff](session-clean-handoff.md)).

## Related pages

- [superpowers-framework-summary](superpowers-framework-summary.md)
- [subagent-driven-development](subagent-driven-development.md)
- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [end-to-end-verification-only](end-to-end-verification-only.md)
- [atomic-task-decomposition](atomic-task-decomposition.md)
