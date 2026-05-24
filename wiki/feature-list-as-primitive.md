# Feature list as primitive

**Summary** : Une feature list n'est pas un mémo humain ni un document optionnel. C'est une **primitive architecturale** dont dépendent le scheduler, le verifier, et le handoff reporter. Sans elle, agent et humain n'ont pas de consensus partagé sur ce que "fait" signifie.

**Sources** : `raw/ingested/lecture-08-use-feature-lists-to-constrain-what-the-agent-does.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le changement de paradigme

| Vue traditionnelle | Vue Lecture 08 |
|--------------------|----------------|
| Feature list = todo list informelle | Feature list = primitive du harness |
| Document optionnel | Structure de données obligatoire |
| Mis à jour à la main occasionnellement | Source unique de vérité, lue à chaque session |
| Humain-lisible | Machine-lisible **et** humain-lisible |

> "Feature lists are the foundational structure the entire harness is built on." — Lecture 08

### La triple structure obligatoire

Chaque entrée de la feature list contient **trois éléments** :

1. **Behavior** — description du comportement attendu (1 phrase)
2. **Verification** — commande exécutable qui prouve que ça marche
3. **State** — `not_started` / `active` / `blocked` / `passing` (voir [[feature-state-machine]])

Sans un des trois → l'item n'est pas utilisable par la harness.

### Pourquoi "primitive" et pas "document"

> "Memos can be ignored; primitives cannot be bypassed." — Lecture 08

Un mémo : on peut l'oublier, l'ignorer, ne pas le mettre à jour.
Une primitive : c'est la source de données dont dépendent les composants du système. Si tu la casses, le système se bloque.

Dans une harness mature :

- Le **scheduler** lit la feature list pour proposer la prochaine tâche
- Le **verifier** exécute les commandes de vérification
- Le **handoff reporter** génère le résumé de session à partir des transitions d'état

Les trois deviennent **inutilisables** sans feature list à jour. C'est précisément ça qui la rend "primitive" plutôt qu'"option".

### Le format minimal

JSON pour usage machine, Markdown pour humains. Voir [[template-feature-list-json]] pour le format complet :

```json
{
  "tasks": [
    {
      "id": "001",
      "behavior": "User registration endpoint",
      "verification": "curl -X POST .../register | jq -e '.success'",
      "state": "passing",
      "evidence": "test_001_output.log"
    }
  ]
}
```

### Externaliser le state

> "Artifacts must be externalized." — Anthropic + OpenAI

L'état des features doit vivre dans **un fichier machine-lisible** du repo, **pas** dans le texte conversationnel ou la mémoire de l'agent.

Pourquoi ?

- Conversation = volatile, perdue à la fin de session
- Fichier dans repo = durable, lisible par toute session future
- Machine-lisible = parsable par scripts, hooks, CI

### Single source of truth

La feature list est **la** source pour répondre à "que reste-t-il à faire ?". Pas le commit log, pas les issues GitHub, pas les notes Slack.

| Question | Source | Notes |
|----------|--------|-------|
| Que doit faire le projet ? | `feature_list.json` | Le **quoi** |
| Pourquoi telle décision ? | `DECISIONS.md` ([[decision-log-pattern]]) | Le **pourquoi** |
| Où en est-on ? | `PROGRESS.md` ([[progress-file-pattern]]) | Le **état session** |
| Quelles features passent ? | `feature_list.json` | Le **état tâche** |

### Granularité calibrée

> "Completable in one session." — Lecture 08

Une feature trop large → jamais finie.
Une feature trop étroite → overhead de gestion supérieur à la valeur.

Pour calibrer, voir [[atomic-task-decomposition]].

### Cas réel : 10-feature e-commerce (Lecture 08)

| Mode | Diagnostic time (new session) | Feature completion |
|------|-------------------------------|---------------------|
| Memo (todo informelle) | 20 min | 30% des features re-implémentées par accident |
| Structured feature list | 3 min | **+45%** de feature completion rate |

L'écart est massif. La cause : sans state machine externalisé, les sessions futures se trompent sur ce qui est déjà fait.

### Les 3 dépendances downstream

```
feature_list.json
        │
        ├──→ Scheduler (pick next not_started)
        │
        ├──→ Verifier (run commands, update state)
        │
        └──→ Handoff Reporter (summarize state for next session)
```

Casser une de ces 3 dépendances → casser la harness. Donc maintenir la feature list **est** maintenir la harness.

### Knowledge loss at boundaries

Sans feature list structurée, à chaque fin de session :

- L'humain doit raconter à l'agent où on en est (~10-20 min)
- L'agent invente (drift) si l'humain n'est pas là
- Conflits possibles entre ce que l'agent croit fini et la réalité

Feature list = **information continuity** entre sessions. Voir aussi [[cross-session-context-loss]].

### Antipatterns

- ❌ Feature list en Slack / Notion / fichier hors-repo → invisible pour l'agent
- ❌ Feature list sans verification command → on ne sait pas quand "fini"
- ❌ État maintenu manuellement dans le markdown sans format strict → drift entre humain et agent
- ❌ Feature list où l'agent peut transitionner `passing` sans evidence → bypass du gate

### Lien avec WIP=1

[[wip-limit-discipline|WIP=1]] s'enforce **via** la feature list : un seul item avec state `active`. La feature list rend cette discipline mécaniquement vérifiable.

### À retenir

1. Feature list = **primitive**, pas document.
2. Triple structure : **Behavior + Verification + State**.
3. Externaliser dans un **fichier machine-lisible** (JSON + Markdown).
4. **Single source of truth** pour le "à faire" et le "fait".
5. C'est la base du scheduler / verifier / handoff reporter.

## Related pages

- [[feature-state-machine]]
- [[harness-pipeline-scheduler-verifier-handoff]]
- [[completion-evidence-executable]]
- [[template-feature-list-json]]
- [[atomic-task-decomposition]]
- [[wip-limit-discipline]]
- [[the-harness-engineering-curriculum-summary]]
