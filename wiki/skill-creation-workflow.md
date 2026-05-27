# Workflow de création d'un skill

**Summary** : Cycle itératif en 5 étapes pour créer un skill robuste : capture d'intention → rédaction SKILL.md → test parallèle → évaluation → itération.

**Sources** :
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Vue d'ensemble

```
Capture d'intention
      ↓
Interview & recherche
      ↓
Rédaction SKILL.md  ←──────────────┐
      ↓                             │
Test (runs parallèles)              │ Itération
      ↓                             │
Évaluation (human + quantitatif)    │
      ↓                             │
Amélioration ───────────────────────┘
      ↓
Optimisation description (triggering)
      ↓
Packaging
```

### Étape 1 — Capture d'intention

Si la conversation courante contient déjà un workflow à capturer, extraire les étapes, outils, corrections, formats depuis l'historique — avant de poser des questions.

Questions clés :
1. Que doit faire ce skill ?
2. Quand se déclenche-t-il ? (phrases/contextes utilisateur)
3. Quel est le format de sortie ?
4. Faut-il des cas de test vérifiables ?

Les skills à sorties objectives (transformations de fichiers, extraction de données, génération de code) bénéficient de cas de test. Les skills subjectifs (style d'écriture, design) en ont moins besoin.

### Étape 2 — Interview & recherche

Clarifier les edge cases, exemples, dépendances, critères de succès **avant** d'écrire les prompts de test. Rechercher en parallèle via subagents si disponibles.

### Étape 3 — Rédaction SKILL.md

Rédiger le `SKILL.md` avec frontmatter complet (→ [[skill-anatomy]]). La description doit inclure les contextes de déclenchement ET être "légèrement pushy" pour compenser la tendance à l'undertriggering de Claude.

Relire avec des yeux frais après rédaction initiale — améliorer avant de tester.

### Étape 4 — Test

2-3 prompts réalistes, représentatifs de ce qu'un vrai utilisateur écrirait.

**Lancer en parallèle dans le même tour** : run "avec skill" + run "sans skill" (baseline). Ne pas faire les runs with-skill d'abord puis les baselines ensuite.

Structure des résultats :
```
skill-workspace/
└── iteration-1/
    ├── eval-nom-descriptif/
    │   ├── with_skill/outputs/
    │   └── without_skill/outputs/
    └── eval_metadata.json
```

→ Voir [[skill-eval-workflow]] pour le détail complet.

### Étape 5 — Évaluation

1. **Assertions quantitatives** — drafted pendant que les runs tournent (ne pas attendre)
2. **Grading** — subagent grader ou inline, résultats dans `grading.json`
3. **Benchmark** — `aggregate_benchmark.py` → `benchmark.json` + `benchmark.md`
4. **Eval viewer** — ouvrir AVANT d'évaluer soi-même (GENERATE THE EVAL VIEWER FIRST)
5. **Feedback humain** — review par l'utilisateur via le viewer

### Étape 6 — Amélioration

Règles d'amélioration :
- **Généraliser depuis le feedback**, ne pas overfitter sur les exemples de test
- **Garder le prompt lean** : supprimer les parties qui font perdre du temps sans valeur
- **Expliquer le pourquoi** : préférer la compréhension aux MUST/NEVER en majuscules
- **Factoriser les scripts répétés** : si tous les runs écrivent le même helper, le bundler dans `scripts/`

Reboucler : appliquer → relancer tous les cas de test → nouveau workspace `iteration-N+1/` → reviewer avec `--previous-workspace` → attendre feedback → répéter.

Critères d'arrêt :
- L'utilisateur est satisfait
- Feedback vide (tout est bon)
- Pas de progrès marginal détectable

### Considération multi-exemples

Le skill sera utilisé des millions de fois sur des prompts variés. L'itération sur 2-3 exemples fixes est utile pour la vitesse, mais le risque est de créer un skill qui ne marche que pour ces exemples. Si un problème persiste, essayer des métaphores différentes ou de nouveaux patterns de travail — plutôt que des contraintes de plus en plus rigides.

## Related pages

- [[skill-creator-meta-skill]]
- [[skill-anatomy]]
- [[skill-eval-workflow]]
- [[skill-description-optimization]]
- [[eval-roadmap]]
- [[pass-at-k-metric]]
- [[checkpoint-vs-continuous-evals]]
