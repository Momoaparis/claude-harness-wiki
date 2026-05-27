# Context anxiety selon les modèles

**Summary** : Quand la fenêtre de contexte approche la limite, certains modèles (notamment Sonnet 4.5) exhibent un comportement de "rushed finish" — sauter la vérification, choisir des solutions simples au lieu d'optimales, déclarer victoire prématurément. Opus 4.5/4.6 le montre moins. Conséquence : la harness doit être tunée au modèle.

**Sources** : `raw/ingested/lecture-05-keeping-context-alive-across-sessions.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le phénomène

> "When agents sense context is running low, they exhibit a 'rushed finish' behavior — rushing to finish current work, skipping verification steps, or choosing a simple solution over the optimal one." — Lecture 05

Comme un humain en fin de quart : on bâcle pour clore. Sauf que le modèle ne *sait* pas qu'il est près de la limite — c'est un comportement émergent de l'entraînement.

### Symptômes observables

- L'agent saute des tests qu'il avait promis d'écrire
- Il choisit une solution "qui marche à peu près" au lieu d'investiguer la vraie cause
- Il déclare une tâche terminée alors qu'il sait qu'il y a un blocker
- Il ne met pas à jour les artefacts ([progress-file-pattern](progress-file-pattern.md), [decision-log-pattern](decision-log-pattern.md))
- Réponses plus courtes en fin de session, sans suivi

### Variations par modèle (Lecture 05)

| Modèle | Niveau de context anxiety | Stratégie recommandée |
|--------|---------------------------|-----------------------|
| **Claude Sonnet 4.5** | Forte | **Reset** (nouvelle session) avant la zone anxiety |
| **Claude Sonnet 4.6** | Modérée | Reset ou compaction selon tâche |
| **Claude Opus 4.5/4.6** | Faible | Compaction généralement viable |
| **Claude Opus 4.7** | Faible | Compaction viable, [self-verification-mechanism](self-verification-mechanism.md) aide |

Pour les autres modèles (GPT-5, Codex, etc.) — observer le comportement empirique avant de fixer la stratégie.

### Pourquoi c'est important pour la harness

> "Harness design needs specific understanding of the target model, not a one-size-fits-all template." — Lecture 05

Un harness conçu pour Opus 4.7 (où compaction marche bien) **cassera** sur Sonnet 4.5 (où il faut reset). Ce n'est pas un bug de la harness — c'est une variation modèle.

### Stratégies de mitigation

#### 1. Détection précoce

Déclencher le [clock-out](session-clean-handoff.md) à **70-80%** de la context window, pas à 95%. Garder une marge.

#### 2. Reset planifié

Pour les modèles à forte anxiety (Sonnet 4.5), planifier un reset de session toutes les N tâches (où N dépend de la tâche). Voir [compaction-vs-reset-strategie](compaction-vs-reset-strategie.md).

#### 3. Encoder la clôture en mécanique

Plutôt que de compter sur l'agent pour finir proprement, encoder un check :

```
PostToolUse hook → si context > 75% → forcer écriture PROGRESS.md
Stop hook → vérifier que clean state checklist passe
```

Voir [claude-code-hooks](claude-code-hooks.md) et [template-clean-state-checklist](template-clean-state-checklist.md).

#### 4. Profils par modèle

Dans la harness, documenter les profils :

```yaml
# harness/model-profiles.yaml
sonnet-4.5:
  context_anxiety: high
  reset_at_pct: 70
  compaction: avoid

opus-4.6:
  context_anxiety: low
  reset_at_pct: 90
  compaction: ok
```

### Pourquoi les modèles diffèrent

Sans accès aux poids ni à l'entraînement, hypothèses du cours :

- Différences dans le RLHF (récompense pour clore une tâche)
- Différences de taille (capacité de raisonner sous pression)
- Différences de fine-tuning (Opus aligné davantage sur "investigate before declaring")

L'important : **mesurer**, pas postuler.

### Comment mesurer chez soi

Test :
1. Donner une tâche qui prendra ~80% de la fenêtre de contexte
2. Observer les 20% finaux
3. Vérifier : tests run ? `PROGRESS.md` mis à jour ? Commit propre ?
4. Comparer entre modèles

Si la qualité dégrade significativement en fin de session → ton modèle a une anxiety notable.

### Lien avec self-verification

[La self-verification d'Opus 4.7](self-verification-mechanism.md) (relire et corriger autonome) **compense** partiellement l'anxiety. Modèles sans self-verification ont besoin de plus de structures externes (rubrics, evaluators).

### À retenir

1. Context anxiety = baisse de qualité dans la zone fin-de-fenêtre.
2. **Sonnet 4.5** : forte anxiety, préférer **reset**.
3. **Opus 4.6/4.7** : faible anxiety, compaction OK.
4. La harness doit être **tunée au modèle**, pas générique.
5. Déclencher le clock-out à 70-80%, pas à 95%.

## Related pages

- [cross-session-context-loss](cross-session-context-loss.md)
- [compaction-vs-reset-strategie](compaction-vs-reset-strategie.md)
- [session-clean-handoff](session-clean-handoff.md)
- [self-verification-mechanism](self-verification-mechanism.md)
- [strategic-compact](strategic-compact.md)
- [claude-opus-47](claude-opus-47.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
