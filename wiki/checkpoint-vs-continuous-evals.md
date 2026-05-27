# Checkpoint-Based vs Continuous Evals

**Summary** : Deux patterns d'évaluation pour valider le travail de Claude — les checkpoints discrets (workflows linéaires) et les évaluations continues (sessions longues exploratoires).

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Checkpoint-Based Evals

Évaluations à des points définis dans le workflow.

- Set explicit checkpoints
- Verify against defined criteria à chaque checkpoint
- Si la vérification échoue, Claude doit fix avant de continuer

**Bon pour** : workflows linéaires avec jalons clairs (feature implementation par phases).

### Continuous Evals

Évaluations qui tournent à intervalles ou après chaque changement.

- Run every N minutes ou après un changement majeur
- Full test suite + build + lint
- Report regressions immédiatement
- Stop and fix avant de continuer

**Bon pour** : sessions longues, refactoring exploratoire, maintenance.

### Comparaison visuelle

```
CHECKPOINT-BASED                CONTINUOUS

  [Task 1]                        [Work]
     │                               │
     ▼                               ▼
  [Checkpoint #1] ◄── verify    [Timer/Change]
     │     pass?                     │
   ┌─┴─┐                              ▼
  yes  no ── fix                [Run Tests + Lint]
     │                               │
     ▼                          ┌────┴────┐
  [Task 2]                    pass     fail
                                │         │
                                ▼         ▼
                          [Continue] [Stop & Fix]
```

### Choisir entre les deux

Le critère de décision est la **nature du travail** :

| Type de travail | Pattern |
|----------------|---------|
| Feature implementation avec étapes claires | Checkpoint |
| Refactoring exploratoire | Continuous |
| Maintenance sans milestones | Continuous |
| Migration linéaire | Checkpoint |

### Combinaison avec hooks et tools

- Hooks `PostToolUse` : vérifications après chaque action (penche vers continuous)
- Skills de validation : utilisés aux checkpoints
- Codemap continuous : sert de source de vérité externe (voir [modular-codebase-tokens](modular-codebase-tokens.md))

## Related pages

- [grader-types](grader-types.md)
- [pass-at-k-metric](pass-at-k-metric.md)
- [eval-roadmap](eval-roadmap.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
