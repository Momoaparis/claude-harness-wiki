# pass@k vs pass^k

**Summary** : Deux métriques d'évaluation pour les agents — `pass@k` mesure "au moins un essai sur k réussit", `pass^k` mesure "tous les k essais réussissent".

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Définitions formelles

| Métrique | Définition | Effet de k croissant |
|----------|-----------|----------------------|
| **pass@k** | Au moins **un** des k essais réussit | Plus k augmente, plus la métrique augmente |
| **pass^k** | **Tous** les k essais doivent réussir | Plus k augmente, plus la métrique diminue |

### Illustration avec un modèle à 70% de succès par essai

```
pass@k: Au moins UN essai sur k réussit
  k=1 : 70%
  k=3 : 91%
  k=5 : 97%
  → Plus de chances = meilleur score

pass^k: TOUS les k essais réussissent
  k=1 : 70%
  k=3 : 34%
  k=5 : 17%
  → Plus dur = consistance requise
```

### Quand utiliser pass@k

- Le résultat final est ce qui compte, pas la fiabilité par essai
- Tu peux retry et tu vas valider toi-même
- Exemple : trouver une solution à un bug — un seul essai correct suffit

### Quand utiliser pass^k

- La consistance est critique
- L'output doit être déterministe (qualité, style, résultat)
- Exemple : génération de code en production — chaque sortie doit être correcte

### Lien avec le choix de modèle

Un modèle à 90% pass@1 a un pass^5 = 59%. Pour les workflows critiques, le pass^k pousse à utiliser des modèles plus fiables ou à ajouter des vérifications (voir [[grader-types]]).

### Stratégie hybride

On peut viser un fort pass@k en production (avec retry automatique) tout en mesurant pass^k pour identifier les régressions.

## Related pages

- [[grader-types]]
- [[checkpoint-vs-continuous-evals]]
- [[eval-roadmap]]
- [[the-longform-guide-summary]]
