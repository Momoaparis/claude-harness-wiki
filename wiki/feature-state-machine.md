# Feature state machine

**Summary** : 4 états (`not_started`, `active`, `blocked`, `passing`), transitions contrôlées par le harness — jamais par l'agent. Le passage à `passing` est **irréversible** et conditionné à l'exécution réussie de la commande de vérification.

**Sources** : `raw/ingested/lecture-08-use-feature-lists-to-constrain-what-the-agent-does.md`

**Last updated** : 2026-05-24

---

## Contenu

### Les 4 états

| État | Sens | Qui peut transitionner ? |
|------|------|--------------------------|
| `not_started` | La tâche n'a jamais été touchée | Harness (scheduler) → `active` |
| `active` | Une session est en train de la faire (WIP=1 implique : 1 seule à la fois) | Harness → `blocked` ou `passing` |
| `blocked` | Empêchement externe (review, dépendance externe) | Harness → `active` ou ... `not_started` ? |
| `passing` | Vérifiée passing par exécution de la verification command | **Irréversible** — pas de retour en arrière |

### Le diagramme

```
            ┌─────────────────┐
            │   not_started   │
            └────────┬────────┘
                     │  (scheduler picks)
                     ▼
            ┌─────────────────┐
            │     active      │◄──────┐
            └────────┬────────┘       │
                     │                │
        ┌────────────┼────────────┐   │
        │            │            │   │
        ▼            ▼            │   │
   ┌─────────┐  ┌──────────┐     │   │
   │ blocked │  │ verifier │     │   │
   └────┬────┘  │  fails   │─────┘   │
        │       └──────────┘         │
        │           ▲                │
        │           │                │
        └───────────┘                │
                                     │
                ┌────────────────────┘
                ▼
        ┌─────────────────┐
        │     passing     │  (terminal — irréversible)
        └─────────────────┘
```

### La règle clé : pass-state gating

> "Only successful execution of the verification command allows transition to `passing` — and that transition is irreversible." — Lecture 08

Conséquences :

1. L'agent **ne peut pas** s'auto-déclarer `passing`. Seul l'exécutable juge.
2. Une tâche `passing` ne peut **plus** redevenir `active`. Si bug découvert → nouvelle tâche correctrice.
3. Pas de "marqué passing à 90%, on verra le reste plus tard".

### Qui contrôle les transitions

> "State transitions are controlled by the harness, never by the agent itself." — Lecture 08

Le **harness** (scheduler + verifier) :

- Marque `active` quand l'agent commence
- Marque `blocked` si l'agent signale un blocker
- Marque `passing` après avoir run la verification command

L'**agent** ne touche jamais directement au state. Il :

- Demande au scheduler "donne-moi la prochaine"
- Demande au verifier "vérifie cette tâche"
- Signale un blocker au harness

### L'irréversibilité de `passing`

Pourquoi `passing` est terminal :

- Si une tâche `passing` redeviendrait `active`, ça crée de l'ambiguïté ("c'était fini ou pas ?")
- Si une régression apparaît, c'est une **nouvelle tâche** (avec sa propre verification)
- L'historique reste clean : on voit que la tâche X était passing en date Y

```markdown
## Task 005 — Login endpoint
**State**: passing
**Evidence**: tests/test_login.py::test_login_valid OK at 2026-05-22

## Task 005-regression — Fix login regression introduced by Task 010
**State**: not_started
**Note**: Task 005 was passing but Task 010 broke it. Create a new task to fix.
```

### Le state `blocked`

Quand l'agent **ne peut pas** finir la tâche pour raison externe :

- Attente d'un code review
- Dépendance d'une API externe non disponible
- Décision humaine requise (souvent : ambiguïté dans le behavior)

`blocked` ≠ `failing`. La tâche est correcte, mais bloquée. Documentation :

```json
{
  "id": "007",
  "state": "blocked",
  "blocker": "Waiting for API key from third-party service (requested 2026-05-22)",
  "blocked_since": "2026-05-22"
}
```

L'agent peut alors démarrer une autre tâche (WIP=1 strict relâché en cas de blocked).

### Implementation dans `feature_list.json`

```json
{
  "tasks": [
    {
      "id": "001",
      "state": "passing",
      "transitions": [
        {"from": "not_started", "to": "active", "at": "2026-05-20T10:00:00Z"},
        {"from": "active", "to": "passing", "at": "2026-05-20T11:30:00Z", "evidence": "test_001.log"}
      ]
    }
  ]
}
```

Logger les transitions = traçabilité complète. Quand quelqu'un demande "depuis quand la feature 001 est passing ?", la réponse est dans le fichier.

### Lien avec WIP=1

[[wip-limit-discipline|WIP=1]] dit : "un seul `active` à la fois". La state machine **enforce** cette règle :

- Scheduler refuse de transitionner `not_started → active` si une autre tâche est déjà `active`
- Sauf si la précédente est `blocked`

### Lien avec verified completion rate

[[verified-completion-rate-metric|VCR]] = ratio `passing` / `activated`. La state machine donne le **dénominateur** (toutes les tâches qui ont été `active` au moins une fois) et le **numérateur** (celles qui ont atteint `passing`).

### Les transitions interdites

| Transition | Pourquoi interdite |
|------------|--------------------|
| `passing` → tout | `passing` est terminal |
| `not_started` → `passing` | Bypasse l'exécution (jamais d'active = jamais de verif) |
| Self-transition de l'agent | Le state appartient au harness, pas à l'agent |

### Antipatterns

- ❌ Marquer `passing` sans exécuter la verif → faux signal de complétude
- ❌ Retour de `passing` à `active` → ambiguïté, créer une nouvelle tâche
- ❌ Pas d'état `blocked` → agent fait semblant que tout va, drift
- ❌ État stocké dans la conversation et pas dans le repo → perdu à la session N+1

### À retenir

1. **4 états** : not_started / active / blocked / passing.
2. **Passing = irréversible.** Régression → nouvelle tâche.
3. Le **harness** contrôle les transitions, pas l'agent.
4. `active → passing` n'est possible **qu'après exécution réussie** de la verification.
5. Logger les transitions pour traçabilité.

## Related pages

- [[feature-list-as-primitive]]
- [[harness-pipeline-scheduler-verifier-handoff]]
- [[wip-limit-discipline]]
- [[verified-completion-rate-metric]]
- [[completion-evidence-executable]]
- [[the-harness-engineering-curriculum-summary]]
