# Harness — Définition et philosophie

**Summary** : Une harness = tout ce qui n'est pas les poids du modèle. Instructions, tools, environnement, state, feedback. Elle détermine combien de la capacité du modèle se traduit en travail réel.

**Sources** : `raw/ingested/lecture-01-strong-models-dont-mean-reliable-execution.txt`, `raw/ingested/lecture-02-what-a-harness-actually-is.md`

**Last updated** : 2026-05-24

---

## Contenu

### Définition opérationnelle

> "Harness = Everything in the engineering infrastructure outside the model weights."
> — Lecture 02

Concrètement : les fichiers d'instructions (`AGENTS.md`, `CLAUDE.md`), les tools disponibles (shell, tests, accès fichiers), la config environnement (`pyproject.toml`, `.nvmrc`, Docker), les artefacts de state (`PROGRESS.md`, commits git), et les boucles de feedback (commandes de vérification, evaluators).

Une bonne harness est aussi distincte du *prompt* que des poids du modèle. Le prompt vit dans une session ; la harness vit dans le repo et survit aux sessions.

### Le constat fondateur (Lecture 01)

| Contexte | Taux de succès |
|----------|----------------|
| Benchmark SWE-bench | ~60% |
| Projets réels (specs floues, pas de tests) | ~40% |

L'écart n'est pas un problème de capacité du modèle — c'est un problème d'**infrastructure d'exécution**. Anthropic a démontré expérimentalement qu'à modèle constant, la qualité de la harness peut faire varier le taux de succès de 20% à 100%.

> "One `AGENTS.md` file might be more effective than upgrading to a more expensive model." — Lecture 01

### Principe-clé

> "If it is not model weights, it is harness. Your harness determines how much of the model's capability gets realized." — Lecture 02

Conséquence : l'investissement dans la harness a un meilleur ROI que l'investissement dans un modèle plus cher, jusqu'à un certain plafond.

### Pourquoi c'est une discipline d'ingénierie

La harness se décompose en [[five-subsystem-harness-architecture|5 subsystèmes]] aux responsabilités distinctes. Chaque subsystème est testable (via [[ablation-study-methodology|ablation]]) et peut [[harness-rot-et-dette-technique|pourrir]] s'il n'est pas maintenu.

Les deux écoles (OpenAI et Anthropic) convergent sur le même message :

- **OpenAI** : "The repo IS the spec." Le dépôt est la spécification de fait.
- **Anthropic** : "Separate the person who does the work from the person who checks the work."

### Le double gap (Norman, repris par le cours)

Inspiré de la psychologie de Don Norman :

| Gap | Description | Solution dans la harness |
|-----|-------------|--------------------------|
| **Gulf of Execution** | L'agent veut faire X mais ne peut pas | Subsystème Tools + Environment |
| **Gulf of Evaluation** | L'agent ne sait pas si ça a marché | Subsystème Feedback |

Une harness incomplète laisse au moins un des deux gulfs ouvert.

### Lien avec ECC et l'écosystème

[[ecc-overview]] est un bundle qui opérationnalise ces concepts en composants installables (skills, hooks, rules). Le curriculum Learn Harness Engineering donne la **théorie sous-jacente** ; ECC fournit une **implémentation** packagée. Voir aussi [[the-longform-guide-summary]] pour les techniques avancées Claude Code.

### À retenir

1. La harness n'est pas un fichier — c'est une **architecture**.
2. Investir dans la harness > upgrader le modèle (jusqu'à un plafond).
3. Une harness se mesure, se teste, se maintient.
4. Sans harness = le modèle redécouvre tout à chaque session = perte massive.

## Related pages

- [[five-subsystem-harness-architecture]]
- [[five-failure-modes-agents-en-prod]]
- [[harness-rot-et-dette-technique]]
- [[the-harness-engineering-curriculum-summary]]
- [[ecc-overview]]
