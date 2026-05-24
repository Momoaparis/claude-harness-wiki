# Template — clean-state-checklist.md

**Summary** : Checklist 6-points à exécuter en fin de session pour garantir un repo "redémarrable" sans intervention manuelle. Encode les 5 conditions de [[session-clean-handoff]] + 1 vérification supplémentaire d'absence de WIP non-documenté.

**Sources** : `raw/ingested/template-clean-state-checklist.txt` (https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/clean-state-checklist)

**Last updated** : 2026-05-24

---

## Contenu

### Rôle

Document à parcourir **à chaque clock-out**. Si une case ne peut pas être cochée → la session n'est pas finie. Voir [[session-clean-handoff]] pour la théorie.

### Template verbatim (anglais)

À copier-coller dans `docs/clean-state-checklist.md` ou directement dans le `CLAUDE.md`.

```markdown
# Clean State Checklist

Run this at the end of every session. ALL 6 boxes must be checked before stopping work.
If any cannot be checked, the session is not yet complete.

---

## 1. ☐ The standard startup path still works

**Command**: `./init.sh` (or equivalent — `make setup`, `npm install && npm run dev`)
**Evidence required**: Successful execution from a clean state, no errors.
**How to test**:
```bash
cd /tmp && rm -rf test-clone && \
  git clone <repo-url> test-clone && \
  cd test-clone && \
  ./init.sh
```

## 2. ☐ The standard verification path still runs

**Command**: `make verify` (or equivalent — `npm run check`, `cargo test`)
**Evidence required**: Test output, pass/fail status clearly visible, exit code 0.

## 3. ☐ Current progress is recorded in the progress log

**File**: `claude-progress.md`
**Check**: Latest session entry exists with ALL required fields:
- Date
- Goal
- Completed (with evidence)
- Verification run + result
- Evidence captured
- Commits
- Files updated
- Known risk
- Next best step

## 4. ☐ Feature state reflects actual verification results

**File**: `feature_list.json`
**Check**: For each task:
- `state == "passing"` ⟹ has non-null `evidence`
- `state == "active"` ⟹ exactly one task in this state (WIP=1)
- `state == "blocked"` ⟹ has `notes` explaining the blocker
- `state == "not_started"` ⟹ no `evidence`, no `transitions`

## 5. ☐ No incomplete work is left undocumented

**Check**:
- All blockers logged in `claude-progress.md` Known Risk
- Known risks explicitly noted with mitigation or workaround
- No silent WIP files (e.g., `.draft.ts`, `.bak`, uncommitted changes you forgot)

## 6. ☐ The next session can proceed without manual intervention

**Test**: From a clean shell:
```bash
git pull
./init.sh
# Read session-handoff.md or claude-progress.md last entry
# Pick next task from feature_list.json
# Start work
```
**Expectation**: Repo reaches known-good state immediately, no questions to ask.

---

## On failure

If any box cannot be checked:

1. Document why in `claude-progress.md` Known Risk section
2. If fixable in 15 min → fix it before ending session
3. If not → explicitly mark the session as **incomplete** in progress log
4. Note the blocker so the next session prioritizes the cleanup

## Why this matters

Skipping the checklist accumulates technical debt that compounds across sessions.
See `[[harness-rot-et-dette-technique]]` and 12-week case study (Lecture 12).
```

### Les 6 points expliqués

#### 1. Startup path works

Test ultime : cloner sur autre machine et démarrer. Si ça casse → la harness ment.

#### 2. Verification runs

`make verify` retourne 0. Tous les tests passent (pas seulement les nouveaux).

#### 3. Progress recorded

Voir [[template-claude-progress-md]] pour les champs obligatoires.

#### 4. Feature state coherent

Voir [[template-feature-list-json]] pour le schema. La cohérence inclut : WIP=1, evidence sur passing, notes sur blocked.

#### 5. No silent WIP

Tout ce qui est temporaire doit être :
- soit committé proprement
- soit supprimé
- soit documenté comme blocker

Pas de "j'ai laissé le fichier .draft.ts traîner, c'est pour la prochaine fois".

#### 6. Next session proceeds

Test mental : "si je quittais maintenant et qu'un autre dev devait reprendre, démarrerait-il sans questions ?"

### Intégration avec Stop hook

Le checklist peut être **forcé** mécaniquement :

```bash
#!/bin/bash
# scripts/clean-state-check.sh

set -e

# 1. Startup path
cd /tmp && rm -rf clone-test && git clone "$REPO_PATH" clone-test
cd clone-test && ./init.sh > /dev/null 2>&1 || { echo "❌ Startup fails"; exit 1; }
cd "$REPO_PATH"

# 2. Verification
make verify > /dev/null 2>&1 || { echo "❌ Verification fails"; exit 1; }

# 3. Progress recorded
LAST_ENTRY_DATE=$(grep -oP "### Session \d+.*\K\d{4}-\d{2}-\d{2}" claude-progress.md | tail -1)
TODAY=$(date +%Y-%m-%d)
[ "$LAST_ENTRY_DATE" = "$TODAY" ] || { echo "❌ No progress entry today"; exit 1; }

# 4. Feature state coherent
ACTIVE=$(jq '[.tasks[] | select(.state == "active")] | length' feature_list.json)
[ "$ACTIVE" -le 1 ] || { echo "❌ More than 1 active task"; exit 1; }

# 5. No silent WIP
git status --porcelain | grep -E "^\?\?" && { echo "❌ Untracked files"; exit 1; }

# 6. Git clean
git diff --quiet && git diff --cached --quiet || { echo "❌ Uncommitted changes"; exit 1; }

echo "✅ Clean state verified"
```

Hook :

```json
{
  "hooks": {
    "Stop": [
      {
        "command": "bash scripts/clean-state-check.sh",
        "description": "Refuse to end session if clean state not achieved"
      }
    ]
  }
}
```

Voir [[claude-code-hooks]].

### Antipatterns

- ❌ Checklist "vague" : "tests run" (sans pass) → faux signal
- ❌ Checklist sur 30+ points → personne ne la suit
- ❌ Pas de mécanique d'enforcement → checklist optionnelle = checklist ignorée
- ❌ Cases cochées sans vraiment vérifier → confiance erronée
- ❌ Cases ignorées "juste cette fois" → norme glissante (voir [[harness-entropy-management]])

### Cas réel : 12 semaines (Lecture 12)

| Discipline | W1 | W12 |
|------------|----|----|
| Sans checklist | 100% build | **68%** |
| Avec checklist | 100% build | **97%** |

29 points d'écart. **Même équipe**, seule la discipline change.

### À retenir

1. **6 points obligatoires** à chaque fin de session.
2. Si une case ne peut pas être cochée → session **incomplète**.
3. **Hook Stop mécanique** = enforcement sans dépendre de la discipline humaine.
4. Test ultime : "un nouveau dev peut-il reprendre en 3 min ?"
5. **29 points d'écart** sur 12 semaines avec vs sans.

## Related pages

- [[session-clean-handoff]]
- [[template-claude-md]]
- [[template-claude-progress-md]]
- [[template-feature-list-json]]
- [[harness-entropy-management]]
- [[claude-code-hooks]]
- [[the-harness-engineering-curriculum-summary]]
