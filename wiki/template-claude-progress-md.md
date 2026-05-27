# Template — claude-progress.md (session log)

**Summary** : Journal append-only des sessions, avec un snapshot de l'état vérifié en tête et une entrée détaillée par session. Lu au clock-in, mis à jour au clock-out. Permet à la session N+1 de reprendre en 3 min au lieu de 20.

**Sources** : `raw/ingested/template-claude-progress-md.md` (https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/claude-progress)

**Last updated** : 2026-05-24

---

## Contenu

### Rôle dans la harness

C'est l'implémentation concrète du [progress-file-pattern](progress-file-pattern.md). Vit dans le repo, committé à chaque session. Référencé depuis [CLAUDE.md](template-claude-md.md).

### Template verbatim (anglais)

À copier-coller dans `claude-progress.md` à la racine du repo.

```markdown
---
title: "Progress Log | [PROJECT_NAME]"
source: "https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/claude-progress"
created: [YYYY-MM-DD]
description: "Append-only progress log for [PROJECT_NAME]."
tags:
  - harness
  - progress-log
---

## Progress Log

## Current Verified State

- Repository root: [ROOT_DIRECTORY]
- Standard startup path: [STARTUP_PATH]
- Standard verification path: [VERIFICATION_PATH]
- Current highest-priority unfinished feature: [FEATURE_ID or "none"]
- Current blocker: [BLOCKER_DESCRIPTION or "none"]

## Session Log

### Session 001

- Date: [YYYY-MM-DD]
- Goal: [Feature or objective for this session]
- Completed:
  - [Task 1 description with evidence]
  - [Task 2 description with evidence]
- Verification run: [VERIFICATION_COMMAND] → [pass/fail summary]
- Evidence captured: [commit hashes, test output paths, screenshots]
- Commits: [list git commit hashes from this session]
- Files or artifacts updated: [list specific paths]
- Known risk or unresolved issue: [explicit blockers or risks]
- Next best step: [clear direction for next session]

### Session 002

- Date:
- Goal:
- Completed:
- Verification run:
- Evidence captured:
- Commits:
- Files or artifacts updated:
- Known risk or unresolved issue:
- Next best step:

### Session 003

- Date:
- Goal:
...
```

### Sections obligatoires

#### En-tête `Current Verified State`

Toujours **en haut**. Updaté **à chaque fin de session**. Contient l'état "instantané" courant. Une nouvelle session lit ça en premier.

#### `Session Log` append-only

Chaque entrée représente une session. **Ne jamais réécrire** une entrée passée. Si correction nécessaire → ajouter une nouvelle entrée qui réfère à la précédente.

### Champs de chaque entrée

| Champ | Pourquoi | Format |
|-------|----------|--------|
| **Date** | Contextualiser dans le temps | YYYY-MM-DD |
| **Goal** | Ce qu'on visait | 1 phrase |
| **Completed** | Ce qui est fait avec evidence | Liste avec preuves |
| **Verification run** | Commande + résultat binaire | `make verify` → 247/247 passing |
| **Evidence captured** | Pointeurs vers preuves durables | Commits, logs, screenshots |
| **Commits** | Hashes git de la session | `abc123, def456` |
| **Files or artifacts updated** | Liste explicite | Paths absolus ou relatifs |
| **Known risk** | Ce qui peut casser | 1-3 phrases |
| **Next best step** | Direction pour N+1 | 1 paragraphe |

### Le champ `Next best step` est critique

Sans direction explicite pour la prochaine session, elle invente. Format efficace :

```
Next best step: Add integration test for password endpoint
  - Why: validatePassword is unit-tested but endpoint isn't
  - Where: tests/integration/auth.test.ts
  - Verification: curl POST returns 400 on weak password
  - Estimated: 1 session
```

### Workflow

#### Clock-in (début de session)

```
1. Open claude-progress.md
2. Read Current Verified State (3 sec)
3. Read last Session entry (30 sec)
4. Run verification: make verify (1 min)
5. Continue Next best step (start work)
```

Total : ~3 minutes.

#### Clock-out (fin de session)

```
1. Update Current Verified State (current commit, blocker, etc.)
2. Append new Session entry (5-10 min de rigueur)
3. git add claude-progress.md
4. git commit -m "chore(progress): close session N — [topic]"
```

### Articulation avec [template-session-handoff-md](template-session-handoff-md.md)

| Document | Granularité | Quand utiliser |
|----------|-------------|----------------|
| `claude-progress.md` | Tout le projet, toutes sessions | Toujours |
| `session-handoff.md` | Snapshot compact de l'état actuel | Sessions denses, contexte chargé |

`session-handoff.md` est optionnel. `claude-progress.md` est **obligatoire**.

### Antipatterns

- ❌ "Completed: Did some work on auth" → vague, pas d'evidence
- ❌ Pas de Next best step → session N+1 invente
- ❌ Réécrire une entrée passée → perte de traçabilité
- ❌ Pas commit après update → state volatile
- ❌ Sections vides ("Verification run: -") → silence ≠ pass

### Exemple complet

```markdown
## Current Verified State

- Repository root: /home/dev/myapp
- Standard startup path: ./init.sh
- Standard verification path: make verify
- Current highest-priority unfinished feature: 004-password-reset
- Current blocker: Waiting for SMTP creds from infra team

## Session Log

### Session 042

- Date: 2026-05-24
- Goal: Implement password validation (feature 003)
- Completed:
  - Added validatePassword() function in src/auth/password.ts
  - Wrote 8 unit tests covering all rules (RFC compliant)
  - All tests passing on first run
- Verification run: `make verify` → 247/247 passing, lint clean
- Evidence captured:
  - Commit: abc123def
  - Test output: tests/test_validation_2026-05-24.log
- Commits: abc123def
- Files or artifacts updated:
  - src/auth/password.ts (new file)
  - src/auth/__tests__/password.test.ts (new file)
  - feature_list.json (state: 003 → passing)
- Known risk or unresolved issue: Regex doesn't cover full Unicode edge cases (deferred to v2)
- Next best step: Start feature 004 (password reset flow)
  - Why: next in feature_list order, depends on 003 (now passing)
  - Where: src/auth/password-reset.ts (new module)
  - Verification: curl POST /api/reset-request returns 200, email sent
  - Blocker: SMTP creds from infra team (ETA 2026-05-26)
```

### À retenir

1. **Append-only**. Jamais réécrire.
2. `Current Verified State` toujours **en haut**, **à jour**.
3. Chaque entrée a **Date / Goal / Completed / Verification / Evidence / Commits / Files / Risks / Next**.
4. **Next best step** = champ le plus important (sauve la session suivante).
5. Committer le fichier à chaque update.

## Related pages

- [progress-file-pattern](progress-file-pattern.md)
- [template-claude-md](template-claude-md.md)
- [template-session-handoff-md](template-session-handoff-md.md)
- [template-clean-state-checklist](template-clean-state-checklist.md)
- [decision-log-pattern](decision-log-pattern.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
