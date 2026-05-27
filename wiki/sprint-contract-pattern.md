# Sprint contract pattern

**Summary** : Accord court-terme négocié **avant** le code, spécifiant scope, standards de vérification, et exclusions explicites. Cœur de l'observabilité de process (Lecture 11). Sans sprint contract, l'évaluation devient "mysticism" — chacun a sa propre idée de ce qui était attendu.

**Sources** : `raw/ingested/lecture-11-making-the-agents-runtime-observable.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le rôle

Un sprint contract est un document qui répond à 3 questions **avant** que l'agent commence :

1. **Scope** : qu'est-ce qui est dans la tâche ?
2. **Verification** : comment saura-t-on que c'est fait ?
3. **Exclusions** : qu'est-ce qui est **explicitement** hors-scope ?

Sans ces 3 réponses pré-définies, l'évaluation à la fin sera arbitraire.

### Le format

```yaml
sprint: dark-mode-toggle
agent: generator-r1
date: 2026-05-24

scope:
  - theme toggle button in header
  - CSS variables globales pour dark/light
  - localStorage persistence du choix utilisateur
  - tests visuels de régression

verification:
  - regression tests pass (all existing tests)
  - new E2E test: "user can toggle theme"
  - no FOUC (flash of unstyled content) au reload
  - localStorage value persisted across refresh

exclusions:
  - print styles (out of scope, future sprint)
  - third-party component theming (out of scope, vendor lock)
  - automatic OS-preference detection (out of scope, future sprint)

acceptance criteria:
  - All scope items implemented
  - All verification items passing
  - Zero violations of exclusions
```

### Pourquoi ce format

#### Scope clair

L'agent sait exactement où s'arrêter. Pas d'over-engineering ("tant qu'on y est, je vais aussi faire X").

#### Verification pré-définie

L'agent connaît la barre. Il peut auto-vérifier avant de remettre. L'evaluator a les critères clairs.

#### Exclusions explicites

Crucial. Sans exclusions, l'agent peut over-do et l'evaluator peut sous-évaluer en disant "il manque X" (alors que X n'a jamais été dans le scope).

Anti-pattern : "Bah, c'est implicite". Non. Lister.

### Le piège du scope implicite

Sans sprint contract :

```
Demande : "implement dark mode"
Agent : implémente tout, y compris print styles + third-party theming
Eval : "scope creep, code spaghetti"
Agent : "mais tu m'as dit dark mode"
```

Avec sprint contract :

```
Demande : "implement dark mode per sprint contract DM-001"
Agent : reste dans le scope
Eval : score sur scope + exclusions respect → calibré
```

### Quand créer un sprint contract

- **Toujours** pour les features non-triviales (>1 session)
- **Toujours** pour les tâches sensibles (sécurité, payment, data)
- Idéalement pour **chaque** atomic task de la feature list
- Souvent généré par un planner agent (voir [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md))

### Sprint contract vs feature list

| Document | Granularité | Détail |
|----------|-------------|--------|
| `feature_list.json` | Macro (1 entrée = 1 atomic task) | Behavior + verification + state |
| Sprint contract | Micro (1 sprint = 1 task in flight) | Scope + verification details + exclusions + acceptance |

Le sprint contract est **plus détaillé** : il est généré au moment de démarrer la tâche, avec tout le contexte courant.

### Cas réel Anthropic DAW (Lecture 11)

Pour le DAW build, le planner a généré ~12 sprint contracts (un par feature majeure). Exemple :

```
sprint: synth-knobs-ui
scope:
  - 3 rotary knobs (volume, attack, decay)
  - SVG-based rendering
  - touch + mouse interaction
verification:
  - knob values map correctly to synth params
  - touch events work on mobile viewport
  - keyboard accessibility (arrow keys adjust)
exclusions:
  - presets system (future)
  - MIDI input mapping (future)
```

Le generator a implémenté **exactement** ces 3 knobs, pas plus, pas moins. L'evaluator a scoré par rapport aux verification items.

### Format machine-lisible

Pour usage par la harness automatisée, format YAML ou JSON :

```json
{
  "sprint_id": "DM-001",
  "scope": [...],
  "verification": [{"id": "v1", "command": "make test-e2e -- --grep dark-mode"}, ...],
  "exclusions": [...],
  "agent": "generator-r1",
  "status": "active"
}
```

Le verifier peut alors run automatiquement les verification commands.

### Sprint contract vs rubric

| Artefact | Rôle |
|----------|------|
| **Sprint contract** | Spec d'entrée — "voici ce qu'on demande" |
| **[Evaluator rubric](template-evaluator-rubric.md)** | Grille de sortie — "voici comment on score" |

Les deux s'articulent : la rubric **score** la conformité au contract.

### Antipatterns

- ❌ "Verbal sprint contract" → perdu à la fin de session
- ❌ Pas d'exclusions → scope creep garanti
- ❌ Verification trop vague ("works correctly") → eval arbitraire
- ❌ Contract changé en cours de sprint sans le marquer → traçabilité perdue
- ❌ Pas de contract du tout pour les tâches >1h → confusion d'eval

### Lien avec acceptance criteria

Le sprint contract **inclut** les acceptance criteria. La différence avec un user story standard (Agile) :

- User story : "As a user I want X so that Y" (orientation utilisateur)
- Sprint contract : ajoute **scope explicite**, **exclusions**, et **verification commands exécutables** (orientation agent)

Les deux peuvent coexister : user story pour comprendre le **pourquoi**, sprint contract pour exécuter le **comment**.

### À retenir

1. **3 sections obligatoires** : Scope / Verification / Exclusions.
2. Créé **avant** le code, pas après.
3. **Exclusions explicites** = anti-scope-creep.
4. Format YAML ou JSON pour usage machine.
5. Articulé avec [evaluator rubric](template-evaluator-rubric.md) pour la boucle complète.

## Related pages

- [observability-runtime-vs-process](observability-runtime-vs-process.md)
- [template-evaluator-rubric](template-evaluator-rubric.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [feature-list-as-primitive](feature-list-as-primitive.md)
- [atomic-task-decomposition](atomic-task-decomposition.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
