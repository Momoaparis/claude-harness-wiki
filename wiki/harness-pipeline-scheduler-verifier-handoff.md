# Harness pipeline — scheduler, verifier, handoff reporter

**Summary** : Une harness mature contient 3 composants qui dépendent tous de la [feature list](feature-list-as-primitive.md) : le scheduler (pick la prochaine tâche), le verifier (exécute la verification command), le handoff reporter (résume l'état de session). Sans ces 3 maillons, la feature list est inutilisée.

**Sources** : `raw/ingested/lecture-08-use-feature-lists-to-constrain-what-the-agent-does.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le pipeline

```
feature_list.json
        │
        ├──► SCHEDULER ──► "Next task: 004"
        │
        ├──► VERIFIER ──► "Task 004 passing / failing"
        │
        └──► HANDOFF REPORTER ──► "Session summary"
```

Les 3 composants **lisent** la feature list. Le verifier **écrit** dedans (transitions d'état).

### 1. Scheduler

**Rôle** : décider quelle tâche faire ensuite.

**Logique** :
- Lire `feature_list.json`
- Filter sur `state == not_started` ET `dependencies all passing`
- Trier par priorité (ordre dans la liste = ordre par défaut)
- Retourner le premier

**Output** : id de la tâche à démarrer.

**Pseudo-code** :
```python
def next_task(feature_list):
    candidates = [
        t for t in feature_list.tasks
        if t.state == "not_started"
        and all(dep.state == "passing" for dep in t.dependencies)
    ]
    return candidates[0] if candidates else None
```

Le scheduler peut être :
- Un script bash run manuellement
- Une commande slash custom dans Claude Code (voir [claude-code-commands](claude-code-commands.md))
- Un hook SessionStart qui auto-propose

### 2. Verifier

**Rôle** : exécuter la verification command d'une tâche et mettre à jour son état.

**Logique** :
- Lire la verification command de la tâche
- L'exécuter (idéalement dans un sandbox, voir [agent-sandboxing](agent-sandboxing.md))
- Si exit code 0 → transition `active → passing` + record evidence
- Si exit code non-0 → record l'erreur, garder `active`

**Output** : binary (passing / failing) + log.

**Exemple** :
```bash
#!/bin/bash
TASK_ID=$1
VERIF_CMD=$(jq -r ".tasks[] | select(.id == \"$TASK_ID\") | .verification" feature_list.json)

if eval "$VERIF_CMD"; then
  jq ".tasks[] |= if .id == \"$TASK_ID\" then .state = \"passing\" else . end" feature_list.json > tmp.json
  mv tmp.json feature_list.json
  echo "✅ $TASK_ID passing"
else
  echo "❌ $TASK_ID failing"
  exit 1
fi
```

Le verifier doit être **séparé de l'agent qui code** ([worker-checker-separation](worker-checker-separation.md)).

### 3. Handoff reporter

**Rôle** : générer un résumé de l'état pour la prochaine session.

**Logique** :
- Lire les transitions récentes du `feature_list.json`
- Lire les dernières entrées du `PROGRESS.md`
- Générer un résumé court : "5 tasks done, 1 active (004), 0 blocked"
- Identifier le `Next best step`

**Output** : section à append dans `claude-progress.md` (voir [progress-file-pattern](progress-file-pattern.md)).

**Exemple** :
```markdown
## Session 042 — 2026-05-24 (Handoff)

**State**:
- Passing: 001, 002, 003, 004, 005 (5/10)
- Active: 006
- Blocked: 007 (waiting for API key)
- Not started: 008, 009, 010

**Last verified**: 2026-05-24 18:30 — VCR = 5/6 = 0.83

**Next best step**: Finish task 006 (POST /api/profile). Verification command in feature_list.json.

**Risks for next session**:
- Task 007 blocker not resolved
- Task 006 has dependency on task 005 — confirmed passing
```

### Pourquoi ces 3 composants

> "The scheduler, the verifier, and the handoff reporter all depend on the feature list." — Lecture 08

C'est **précisément** ce qui rend la feature list une primitive et pas un mémo. Casser la feature list = casser les 3.

### Implémentation minimale

Tu n'as **pas besoin** de 3 services distincts. Pour un projet solo, ce peut être :

- 3 scripts shell : `scripts/next.sh`, `scripts/verify.sh`, `scripts/handoff.sh`
- 1 commande Make qui orchestre : `make session-end` = `verify + handoff`
- Hooks Claude Code : SessionStart → run `next.sh` ; Stop → run `handoff.sh`

L'important n'est pas la sophistication, c'est que **les 3 logiques existent** et soient automatisables.

### Implémentation moyenne

Pour un team ou un projet plus gros :

- `feature_list.json` versionné
- Un CLI dédié : `harness next`, `harness verify`, `harness handoff`
- CI qui run `harness verify-all` à chaque PR
- Dashboard qui affiche l'état (cf. Lecture 11 sur [observability-runtime-vs-process](observability-runtime-vs-process.md))

### Implémentation avancée

Pour un setup multi-agent (Anthropic [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)) :

- Planner agent → écrit la feature list
- Generator agent → implémente, signal au verifier
- Evaluator agent → run verification, update state
- Handoff reporter → résumé pour la session humaine de revue

### Lien avec Claude Code

Tu peux brancher chaque composant à un mécanisme Claude Code :

| Composant | Mécanisme |
|-----------|-----------|
| Scheduler | Slash command `/next-task` |
| Verifier | Hook PostToolUse + commande `make verify-XXX` |
| Handoff reporter | Hook Stop |

Voir [claude-code-hooks](claude-code-hooks.md) et [claude-code-commands](claude-code-commands.md).

### Antipatterns

- ❌ Avoir une feature list mais aucun des 3 composants → elle pourrit
- ❌ Verifier auto-cliqueteur (passe sans vraiment exécuter) → état faux
- ❌ Scheduler qui ignore les dépendances → tâches faites dans le mauvais ordre
- ❌ Handoff manuel uniquement → la session N+1 redécouvre tout

### À retenir

1. **3 composants** : scheduler, verifier, handoff reporter.
2. Tous **lisent** la feature list. Le verifier **écrit**.
3. Implémentation **minimale** = 3 scripts shell. C'est suffisant.
4. Hooks Claude Code = excellent point d'attache.
5. Casser la feature list = casser le pipeline = casser la harness.

## Related pages

- [feature-list-as-primitive](feature-list-as-primitive.md)
- [feature-state-machine](feature-state-machine.md)
- [worker-checker-separation](worker-checker-separation.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [claude-code-hooks](claude-code-hooks.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
