# Optimisation de la description d'un skill (triggering)

**Summary** : Le champ `description` du frontmatter SKILL.md est le mécanisme principal de déclenchement. Une boucle d'optimisation automatisée génère des eval queries, mesure le taux de déclenchement, et améliore la description itérativement.

**Sources** :
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Comment fonctionne le triggering

Claude voit les skills sous forme d'une liste `available_skills` (name + description). La décision d'invoquer un skill repose **uniquement** sur cette description.

Comportement clé : Claude invoque un skill seulement pour des tâches **qu'il ne peut pas traiter facilement seul**. Les requêtes simples en une étape ne déclenchent pas les skills même si la description correspond parfaitement. Les requêtes multi-étapes ou spécialisées déclenchent fiablement les skills quand la description correspond.

Conséquence : les eval queries de test doivent être **substantielles** (pas "lire ce PDF" mais un scénario détaillé où Claude bénéficierait d'un skill).

### Problème d'undertriggering

Claude a une tendance à ne pas déclencher un skill quand il serait utile. Pour compenser, la description doit être **légèrement pushy** :

> ❌ "How to build a simple fast dashboard."
> ✅ "How to build a simple fast dashboard. Use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, **even if they don't explicitly ask for a 'dashboard'**."

### Étape 1 — Générer les eval queries

Créer 20 queries — mix de should-trigger et should-not-trigger :

```json
[
  {"query": "le prompt utilisateur", "should_trigger": true},
  {"query": "autre prompt", "should_trigger": false}
]
```

**Qualités requises** :
- Réalistes (ce qu'un vrai utilisateur de Claude Code ou Claude.ai écrirait)
- Concrètes et spécifiques : noms de fichiers, contexte personnel, noms de colonnes, URLs
- Mix de longueurs, abréviations, fautes, langage familier
- Focus sur les **edge cases** plutôt que les cas évidents

**Should-trigger** (8-10) : couverture diverse — différentes formulations d'un même besoin, cas où l'utilisateur ne nomme pas explicitement le skill mais en a besoin, usages peu courants, cas où le skill est en compétition avec un autre.

**Should-not-trigger** (8-10) : les plus précieux sont les **near-misses** — queries qui partagent des mots-clés avec le skill mais ont besoin d'autre chose. Domaines adjacents, ambiguïtés. Éviter les négatifs évidents (ex: "écrire une fonction fibonacci" comme négatif pour un skill PDF).

### Étape 2 — Review avec l'utilisateur

Présenter les queries pour validation via le template HTML (`assets/eval_review.html`). L'utilisateur peut modifier, ajouter, supprimer, puis "Export Eval Set" → `feedback.json`.

Cette étape est critique : de mauvaises eval queries mènent à de mauvaises descriptions.

### Étape 3 — Boucle d'optimisation automatisée

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-de-la-session-courante> \
  --max-iterations 5 \
  --verbose
```

La boucle :
1. Split 60% train / 40% test (held-out pour éviter l'overfitting)
2. Évalue la description courante (3 runs par query pour fiabilité)
3. Claude propose des améliorations sur les failures
4. Ré-évalue sur train + test
5. Répète jusqu'à 5 itérations
6. Retourne `best_description` — sélectionnée sur le **score test** (pas train)

### Étape 4 — Appliquer le résultat

Prendre `best_description` du JSON output et mettre à jour le frontmatter du `SKILL.md`. Montrer avant/après + scores à l'utilisateur.

### Disponibilité

- **Claude Code** : workflow complet disponible (nécessite `claude -p` via subprocess)
- **Claude.ai** : `run_loop.py` non disponible (dépend du CLI `claude`)
- **Cowork** : disponible, à lancer après avoir finalisé le skill

### Parallèle avec l'évaluation générale

Cette optimisation est une forme spécialisée d'[eval-roadmap](eval-roadmap.md) appliquée non pas aux *outputs* du skill mais à sa *condition de déclenchement*. Le split train/test évite le même problème d'overfitting que dans les ML classiques.

## Related pages

- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [skill-anatomy](skill-anatomy.md)
- [skill-eval-workflow](skill-eval-workflow.md)
- [skill-creation-workflow](skill-creation-workflow.md)
- [eval-roadmap](eval-roadmap.md)
- [confidence-calibration-bias](confidence-calibration-bias.md)
