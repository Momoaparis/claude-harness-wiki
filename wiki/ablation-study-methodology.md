# Méthodologie : ablation study pour harness

**Summary** : Méthode empirique pour mesurer la valeur marginale de chaque composant d'une harness. Désactiver un composant à la fois, mesurer la dégradation, attribuer la valeur. Output : un benchmark numérique qui dit lesquels composants importent vraiment dans **ton** contexte.

**Sources** : `raw/ingested/lecture-02-what-a-harness-actually-is.md`, `raw/ingested/project-06-runtime-observability-and-debugging.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

Inspiré de la science : pour mesurer l'effet d'une variable, varier **une seule** à la fois.

Appliqué à la harness :

```
1. Setup baseline : harness complète + benchmark tasks
2. Pour chaque composant H₁, H₂, H₃ ... :
   2.1. Désactiver Hᵢ
   2.2. Re-run le benchmark
   2.3. Mesurer la dégradation = baseline_score - score_sans_Hᵢ
3. Trier par dégradation décroissante
   → composants en haut = critiques
   → composants en bas = potentiellement supprimables
```

### Pourquoi ablation > intuition

Sans données, on garde une harness "parce que ça paraît important". Avec ablation, on **mesure** :

- Composants qui valent leur coût → garder
- Composants qui ne changent rien → supprimer
- Composants qui aident **peu** → remplacer par alternative légère

### Cas réel : Project 06 (curriculum)

Setup :
- 8 features à implémenter dans une knowledge-base Electron
- Modèle constant (ex: Sonnet 4.5)
- 5 sessions par config

Mesure :
- Taux de features complétées (VCR)
- Temps par feature
- Issues détectées en review

Ablation typique :

> Données illustratives — à remplacer par vos mesures réelles.

| Config | VCR | Temps moy | Notes |
|--------|-----|-----------|-------|
| Full harness | 87% | 35 min/feat | Baseline |
| Sans `feature_list.json` | **42%** | 60 min/feat | **−45pts**, critique |
| Sans `session-handoff.md` | 72% | 45 min/feat | −15pts, important |
| Sans `clean-state-checklist` | 81% | 38 min/feat | −6pts, modéré |
| Sans `evaluator-rubric.md` | 65% | 40 min/feat | −22pts, important |
| Sans `ARCHITECTURE.md` | 78% | 42 min/feat | −9pts, modéré |
| Sans `init.sh` | 80% | 50 min/feat | −7pts modéré + +15min startup |

Conclusion : `feature_list.json` est **non-négociable**. `evaluator-rubric` aussi. Les autres ont des valeurs variables.

### Protocole détaillé

#### Étape 1 : Définir le benchmark

- Tasks bien définies (idéal : feature list existante)
- Critère de succès objectif (VCR, completion rate, temps)
- Modèle constant (sinon variables confondues)

#### Étape 2 : Run baseline

- Harness complète activée
- Mesurer N fois (réduire bruit)
- Calculer baseline_score, écart-type

#### Étape 3 : Ablation séquentielle

Pour chaque composant Hᵢ :

- Désactiver (renommer fichier, vider config, etc.)
- Re-run le benchmark
- Calculer score_sans_Hᵢ et écart-type
- Comparer

#### Étape 4 : Analyse

```
delta(Hᵢ) = baseline - score_sans_Hᵢ
```

Si `delta` négligeable (dans l'écart-type) → composant probablement inutile.
Si `delta` significatif → composant a une valeur réelle.

#### Étape 5 : Décision

| Delta | Action |
|-------|--------|
| 0% (intra écart-type) | Supprimer ou simplifier |
| 5-15% | Garder, considérer alternatives plus légères |
| > 15% | Garder, critique |

### Variantes

#### Ablation par groupe

Si trop de composants : grouper et ablate par groupe (state mgmt, observability, verification).

```
Groupe State : feature_list.json, claude-progress.md, session-handoff.md
Groupe Observability : evaluator-rubric.md, logger.ts, check-architecture.sh
Groupe Verification : verify scripts, E2E tests, hooks
```

Si un groupe a un fort impact → décomposer pour identifier le composant pivot.

#### Ablation incrémentale (forward selection)

Inverse : partir d'une harness vide, ajouter un composant à la fois, mesurer le gain.

```
Empty harness → score baseline_low
+ AGENTS.md → mesurer
+ feature_list.json → mesurer
+ ...
```

Permet de construire la harness "minimum viable".

### Limites de la méthode

#### 1. Effets d'interaction

Deux composants peuvent **interagir** : ablate l'un = faible impact ; ablate l'autre = faible impact ; ablate les deux = effondrement.

Solution : faire aussi des ablations par paires/groupes pour détecter les couplages.

#### 2. Variance entre runs

LLMs sont non-déterministes. Un run peut être chanceux. **Toujours** moyenner sur N runs (N ≥ 3, idéal 5+).

#### 3. Dépendance au benchmark

L'ablation mesure la valeur des composants **pour ce benchmark**. Un composant inutile sur les knowledge-base apps peut être critique sur des web apps.

Solution : multiplier les benchmarks ou choisir un benchmark représentatif.

#### 4. Dépendance au modèle

Anthropic cite : `sprint-splitter` indispensable pour Sonnet 4.5, **inutile** pour Opus 4.6 (voir [harness-entropy-management](harness-entropy-management.md)).

Conséquence : **re-ablate** après chaque upgrade modèle majeur.

### Quand faire une ablation

| Fréquence | Cas |
|-----------|-----|
| Trimestriellement | Cadence "santé" générale |
| Après upgrade modèle | Réévaluer toute la harness |
| Si la harness pèse | Identifier ce qui peut être supprimé |
| Avant gros refactor | Comprendre la valeur de l'existant |
| Si benchmarks dégradent | Investiguer (un composant nouveau a cassé ?) |

### Outils

#### Setup minimal

- Git branches/worktrees pour isoler les configs (voir [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md))
- Script de benchmark (run les tasks, calcule le score)
- Spreadsheet pour collecter les données

#### Setup avancé

- CI dédié qui run les ablations automatiquement
- Dashboard de tracking dans le temps
- Détection d'alarme si un composant nouveau dégrade

### Lien avec fresh session test

[fresh-session-readability-test](fresh-session-readability-test.md) est **complémentaire** :

| Test | Mesure |
|------|--------|
| Ablation | Valeur **marginale** de chaque composant |
| Fresh session | **Complétude** de la carte (manque-t-il quelque chose ?) |

Les deux ensemble couvrent : "quoi est trop / quoi manque".

### Exemple complet : projet perso (illustration)

Setup :
- Mon projet React : 5 features TODO
- Harness : AGENTS.md (150 lines), feature_list.json, claude-progress.md, evaluator-rubric, check-architecture.sh
- Modèle : Sonnet 4.6, 3 runs par config

Résultats (fictifs pour illustration) :

```
Baseline (full) : VCR 92%
Sans feature_list.json : VCR 50% (-42pts) ← critique
Sans claude-progress.md : VCR 75% (-17pts) ← important
Sans evaluator-rubric : VCR 80% (-12pts) ← important
Sans check-architecture.sh : VCR 90% (-2pts) ← probablement supprimable
AGENTS.md court (50 lines) au lieu de 150 : VCR 91% (-1pt) ← OK simplifier
```

Conclusion : feature_list + progress + rubric sont core. Le reste peut être simplifié.

### Antipatterns

- ❌ 1 seul run par config → conclusion par chance
- ❌ Pas de modèle constant → variables confondues
- ❌ Ablation sur un benchmark non-représentatif → faux verdict
- ❌ Garder un composant "au cas où" sans le mesurer
- ❌ Ne pas re-ablate après upgrade modèle

### À retenir

1. **Désactiver un composant à la fois**, mesurer la dégradation.
2. **N runs par config** (≥3) pour réduire le bruit.
3. **Composants critiques** = ceux qui dégradent fort.
4. Faire des **ablations par paire** pour détecter les couplages.
5. **Re-ablate** après upgrade modèle ou changement majeur.

## Related pages

- [fresh-session-readability-test](fresh-session-readability-test.md)
- [harness-curriculum-projects-overview](harness-curriculum-projects-overview.md)
- [harness-entropy-management](harness-entropy-management.md)
- [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md)
- [verified-completion-rate-metric](verified-completion-rate-metric.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
