# Rebuild Cost Metric

**Summary** : Coût mesuré (temps + tokens) pour reconstruire l'état d'une session depuis zéro, faute d'artefacts de continuité. Métrique inverse de la valeur des progress records — plus le rebuild cost est élevé, plus les artefacts de handoff sont critiques.

**Sources** : `raw/ingested/lecture-03-making-the-repository-the-single-source-of-truth.md`, `raw/ingested/lecture-11-making-the-agents-runtime-observable.md`

**Last updated** : 2026-05-24

---

## Contenu

### Définition

Le rebuild cost est le **temps perdu à diagnostiquer l'état du projet** au lieu de produire de la valeur. Il se déclenche à chaque démarrage de session quand le contexte n'est pas persisté.

> "Good progress records reduce session startup diagnostic time by 60-80%." — Lecture 08

### Mesure empirique

| Scénario | Durée de diagnostic | Première action productive |
|----------|---------------------|---------------------------|
| Sans artefacts (baseline) | **15-20 min** | ~20 min |
| Avec `claude-progress.md` seul | ~5 min | ~5 min |
| Avec stack complet (progress + handoff + feature list) | **~3 min** | ~3 min |

Source : études de cas curriculum Harness Engineering (Lectures 03, 08, 11).

### Composants du coût

1. **Diagnostic d'état** : lire le code pour deviner où en était la session précédente
2. **Re-découverte des décisions** : pourquoi tel choix technique a été fait
3. **Re-vérification de la baseline** : est-ce que les tests passent toujours ?
4. **Drift risqué** : sans contexte, l'agent invente des conventions → erreurs silencieuses

### Pourquoi c'est une métrique de harness

Le rebuild cost est **invisible dans les métriques standard** (tests passent, code compile) mais représente 15-30% du temps total sur les projets multi-session sans harness.

C'est le pendant économique du [fresh-session-readability-test](fresh-session-readability-test.md) : le test détecte l'absence d'information, la métrique chiffre le coût de cette absence.

### Lien avec les artefacts de continuité

| Artefact | Rebuild cost évité |
|----------|---------------------|
| [`claude-progress.md`](progress-file-pattern.md) | Diagnostic d'état (15 → 5 min) |
| [`session-handoff.md`](template-session-handoff-md.md) | Re-découverte des décisions |
| [`feature_list.json`](feature-list-as-primitive.md) | Choix de la prochaine tâche |
| [startup-readiness-checklist](startup-readiness-checklist.md) | Re-vérification baseline |

### Lien avec l'observabilité

[L'observabilité process](observability-runtime-vs-process.md) (sprint contracts, task traces, rubrics) réduit directement le rebuild cost du point de vue évaluateur : sans elle, la session N+1 diagnostique from scratch.

> "Session handoff information cliff. When incomplete work is handed to the next session, missing observability means the new session has to diagnose the system state from scratch." — Lecture 11

### Antipattern

❌ "L'agent peut retrouver le contexte en lisant le code" → vrai pour l'état final, faux pour les décisions intermédiaires, les impasses explorées, et les choix délibérément rejetés.

## Related pages

- [progress-file-pattern](progress-file-pattern.md)
- [fresh-session-readability-test](fresh-session-readability-test.md)
- [cross-session-context-loss](cross-session-context-loss.md)
- [session-clean-handoff](session-clean-handoff.md)
- [observability-runtime-vs-process](observability-runtime-vs-process.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
