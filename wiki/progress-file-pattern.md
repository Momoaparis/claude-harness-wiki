# Progress file pattern (PROGRESS.md / claude-progress.md)

**Summary** : Artefact machine-lisible qui capture l'état courant du projet : ce qui est fait, ce qui est en cours, ce qui est bloqué. Lu au début de chaque session, mis à jour avant chaque clôture. Réduit le rebuild cost de 78% selon les données du cours.

**Sources** : `raw/ingested/lecture-05-keeping-context-alive-across-sessions.md`, `raw/ingested/template-claude-progress-md.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le rôle

Un fichier qui répond à la question : **"Where are we right now?"** (question #5 du [fresh session test](fresh-session-readability-test.md)).

Sans lui, chaque session redémarre en mode "deviner". Avec lui, 3 minutes pour reprendre le travail.

### Le nommage

| Nom | Contexte |
|-----|----------|
| `PROGRESS.md` | Format générique cross-tool (Codex, Cursor, etc.) |
| `claude-progress.md` | Variant Claude Code spécifique (voir [template-claude-progress-md](template-claude-progress-md.md)) |

Choisir un seul et s'y tenir. Le contenu est essentiellement identique.

### Structure standard (Lecture 05)

```markdown
# Progress Log

## Current Verified State
- Repository root: /path/to/repo
- Standard startup path: ./init.sh
- Standard verification path: make verify
- Current highest-priority unfinished feature: auth-module
- Current blocker: waiting for db migration review

## Session Log

### Session 003 — 2026-05-24
- Goal: implement password validation
- Completed: 
  - Added validatePassword() with regex rules
  - Wrote 8 unit tests, all passing
- Verification run: `make test` → 247/247 passing
- Evidence captured: commit abc123
- Files updated: src/auth/password.ts, src/auth/__tests__/password.test.ts
- Known risk: regex doesn't cover unicode edge cases (deferred)
- Next best step: integrate validatePassword into POST /api/register

### Session 002 — 2026-05-23
- Goal: ...
- ...
```

### Les sections obligatoires

#### Current Verified State (tête)

Snapshot machine-lisible de l'état actuel :

- Repository root
- Standard startup path (commande)
- Standard verification path (commande)
- Current highest-priority unfinished feature
- Current blocker

Cette section est **toujours en haut**, **toujours à jour**. Une nouvelle session lit ça en premier.

#### Session log (chronologique)

Une entrée par session, append-only :

- **Date**
- **Goal** — objectif de la session
- **Completed tasks** — avec preuves
- **Verification run** — commande + résultat
- **Evidence captured** — commits, test outputs, screenshots
- **Files or artifacts updated**
- **Known risks or unresolved issues**
- **Next best step** — direction claire pour la session suivante

### Le critère "Next best step"

C'est le champ le plus important. Sans direction explicite pour la prochaine session, celle-ci va inventer sa propre priorité (souvent fausse).

Format efficace :

```
Next best step: Add integration test for password endpoint
  - Why: validatePassword is unit-tested but endpoint isn't
  - Where: tests/integration/auth.test.ts
  - Verification: curl POST returns 400 on weak password
```

### Workflow

#### Au début de chaque session (clock-in)

1. Lire `Current Verified State`
2. Lire la dernière entrée de `Session log`
3. Run la verification command pour confirmer
4. Démarrer sur `Next best step`

#### À la fin de chaque session (clock-out)

1. Mettre à jour `Current Verified State`
2. Append une nouvelle entrée dans `Session log`
3. Remplir tous les champs (notamment `Next best step`)
4. Commit le fichier

### Lien avec git

Le progress file vit dans le repo. Chaque update = commit dédié, par exemple :

```
chore(progress): close session 003 — password validation done
```

L'historique du fichier = traçabilité complète des décisions de prog.

### Antipatterns

- **Pas de "Next best step"** → la session suivante invente
- **"Completed" sans evidence** → on ne peut pas vérifier
- **Sections "Notes" vagues** → bruit, pas signal
- **Mettre à jour seulement le summary** → la session log perd sa valeur historique
- **Ne pas committer** → state volatile, à quoi bon

### Cas réel (Lecture 05)

> "Good progress records reduce session startup diagnostic time by 60-80%." — Lecture 08

| Sans progress file | Avec progress file complet |
|---------------------|----------------------------|
| 15-20 min rebuild | 3 min rebuild |
| Defects cachés ~43% | Defects cachés ~8% |
| Completion rate 58% | Completion rate 100% |

### Lien avec session-storage-pattern

[session-storage-pattern](session-storage-pattern.md) décrit le pattern `.tmp` côté Claude Code (mémoire externe). `PROGRESS.md` est l'équivalent **dans le repo**, donc :

- Durable (git)
- Lisible par tout agent (pas que Claude Code)
- Auditable

Les deux sont compatibles : `.tmp` pour notes informelles intra-session, `PROGRESS.md` pour state durable inter-session.

### À retenir

1. Une entrée par session, append-only.
2. **"Current Verified State"** au top, mis à jour à chaque fin.
3. Le champ **"Next best step"** sauve la session suivante.
4. Toute "Completed" doit avoir une evidence vérifiable.
5. Committer le fichier après chaque update.

## Related pages

- [decision-log-pattern](decision-log-pattern.md)
- [cross-session-context-loss](cross-session-context-loss.md)
- [session-clean-handoff](session-clean-handoff.md)
- [template-claude-progress-md](template-claude-progress-md.md)
- [session-storage-pattern](session-storage-pattern.md)
- [fresh-session-readability-test](fresh-session-readability-test.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
