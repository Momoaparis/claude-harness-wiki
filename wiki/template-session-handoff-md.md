# Template — session-handoff.md

**Summary** : Document compact (~30 lignes) résumant l'état actuel, les changements de session, les blockers, la prochaine étape, et les commandes essentielles. Lu **au démarrage** d'une nouvelle session pour reprendre sans relire toute la documentation. Optionnel mais très utile pour les contextes denses.

**Sources** : `raw/ingested/template-session-handoff-md.txt` (https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/session-handoff)

**Last updated** : 2026-05-24

---

## Contenu

### Rôle

Différent de [[template-claude-progress-md|claude-progress.md]] :

| Document | Pour qui | Granularité | Quand |
|----------|----------|-------------|-------|
| `claude-progress.md` | Historique complet | Toutes sessions | Append à chaque session |
| `session-handoff.md` | "Lecture rapide" | Snapshot actuel **uniquement** | Updaté à chaque session, écrase l'ancien |

`session-handoff.md` est **éphémère** au sens où il ne garde que le snapshot courant. L'historique est dans `claude-progress.md`.

### Template verbatim (anglais)

À copier-coller dans `session-handoff.md` à la racine du repo et adapter.

```markdown
# Session Handoff

## Verified Now

**What is currently working**: [List of features with pass status]
- Feature 001 (registration): passing — verified 2026-05-22
- Feature 002 (login): passing — verified 2026-05-23

**What verification actually ran**: [Specific test command + output]
- `make verify` → 247/247 passing, lint clean, build OK
- Last run: 2026-05-24 14:30 UTC

## Changed This Session

**Code or behavior added**:
- [Feature description + files]
- Example: Added password validation in src/auth/password.ts

**Infrastructure or harness changes**:
- [Config, scripts, artifacts]
- Example: Added scripts/verify-003-reset.sh

## Broken Or Unverified

**Known defect**: [Description + reproduction steps if applicable]
- None.

**Unverified path**: [Features marked as implemented but not yet tested]
- Feature 003 (password reset): code written but E2E test pending

**Risk for the next session**: [Explicit warnings about what might fail]
- SMTP creds not yet available from infra team — feature 003 cannot be E2E tested

## Next Best Step

**Highest-priority unfinished feature**: [Feature name]
- Feature 003 (password reset email)

**Why it is next**: [Brief rationale]
- Unblocks feature 004 (reset confirm)
- SMTP creds expected by 2026-05-26

**What counts as passing**: [Acceptance criteria]
- `curl POST /api/reset-request` returns 202
- Email visible in MailHog inbox at localhost:1025
- Reset token stored in DB with 1h expiry

**What must not change during that step**: [Protected scope]
- Do not modify feature 001 or 002 implementations
- Do not change the User table schema (frozen until 005)

## Commands

**Startup**: `./init.sh`
**Verification**: `make verify`
**Focused debug command**: `make test-feature-003`
```

### Sections obligatoires

#### Verified Now

Snapshot **factuel** de ce qui marche actuellement. Pas de spéculation. Doit pouvoir être vérifié immédiatement.

#### Changed This Session

Diff de cette session : code + infrastructure. Vue compacte pour la session suivante.

#### Broken Or Unverified

**Critique**. Liste explicite des risques :
- Bugs connus
- Features implémentées mais pas testées
- Dépendances externes en attente

Sans cette section, la session suivante peut casser sans le savoir.

#### Next Best Step

Direction claire :
- Quelle feature
- Pourquoi
- Critère de passing
- Scope protégé

#### Commands

Les 3 commandes vitales :
- Startup (lance le projet)
- Verification (run tous les checks)
- Focused debug (test rapide de la feature courante)

### Workflow

#### Fin de session N

```
1. Update session-handoff.md (écrase le contenu précédent)
2. Update claude-progress.md (append la session entry)
3. Commit les deux
```

#### Début de session N+1

```
1. Read session-handoff.md (30 sec) ← document principal
2. Optionnel : read last claude-progress.md entry (1 min)
3. Run `make verify` pour confirmer
4. Start work
```

`session-handoff.md` économise du temps de lecture : la session N+1 a tout ce qu'il faut en 30 sec.

### Différence avec progress log

```
claude-progress.md :
  Session 040
  Session 041
  Session 042 ← actuelle

session-handoff.md :
  Snapshot post-session-042
```

Le handoff est une **vue cristallisée** du dernier état. Le progress log est l'**historique complet**.

### Quand l'utiliser

| Situation | Handoff nécessaire ? |
|-----------|---------------------|
| Projet solo, sessions quotidiennes | Optionnel |
| Multi-dev, sessions partagées | **Oui** |
| Contexte conversationnel dense (>50% window) | **Oui** |
| Tâches complexes multi-session | **Oui** |
| Quick fixes one-session | Non |

### Antipatterns

- ❌ Garder l'ancien contenu sans update → menteur, dangereux
- ❌ Section "Risk" vide quand il y a des risks → la N+1 trébuche
- ❌ "Commands" pas testées → la N+1 démarre dans le mur
- ❌ "Next best step" vague → la N+1 invente
- ❌ Skip le handoff "parce que rien d'important n'a changé" → toujours important

### Format compact = critique

Doit tenir en ~30-50 lignes. Si plus → le fichier devient une 2ème `claude-progress.md`, on perd la valeur "lecture rapide".

Astuce : si une section devient longue, c'est probablement à déplacer vers `claude-progress.md` (historique) ou `DECISIONS.md` (raison).

### Intégration avec hooks

SessionStart hook qui affiche le handoff :

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "cat session-handoff.md",
        "description": "Display handoff at session start"
      }
    ]
  }
}
```

Voir [[claude-code-hooks]].

### À retenir

1. **Snapshot du présent**, pas historique.
2. **5 sections** : Verified now / Changed / Broken / Next / Commands.
3. **Écrase** l'ancien contenu à chaque update.
4. Compact (~30-50 lignes max).
5. Optionnel pour solo, **obligatoire** pour multi-dev ou contextes denses.

## Related pages

- [[template-claude-progress-md]]
- [[template-claude-md]]
- [[template-clean-state-checklist]]
- [[session-clean-handoff]]
- [[progress-file-pattern]]
- [[the-harness-engineering-curriculum-summary]]
