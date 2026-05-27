# Startup readiness checklist

**Summary** : Document explicite (~30 lignes) qui décrit les commandes de démarrage, l'état actuel des prérequis (deps, test framework, lint), et la structure du projet. Output canonique de la phase d'init. Permet à toute nouvelle session de démarrer en 3 minutes.

**Sources** : `raw/ingested/lecture-06-make-the-agent-initialize-before-every-work-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le rôle

C'est le **contrat** que la phase d'init signe avec toutes les sessions futures :

- Voici les commandes pour démarrer
- Voici ce qui est déjà installé / configuré
- Voici ce qui n'est pas encore en place

Sans ça, chaque session redevine les commandes et les états.

### Structure standard (Lecture 06)

```markdown
# Startup Readiness Checklist

## Start commands
- Setup: `make setup`
- Dev server: `make dev`
- Run tests: `make test`
- Full verification: `make verify`

## Current State (verified on 2026-05-24)
- [x] Dependencies installed and lockfile committed
- [x] Test framework configured (Vitest)
- [x] Example test passing (1/1)
- [x] Lint clean (0 errors, 0 warnings)
- [x] TypeScript compiles cleanly
- [x] Build succeeds (`make build`)

## Project Structure
- `src/` — application code
- `tests/` — unit and integration tests
- `docs/` — architecture, decisions, patterns
- `scripts/` — automation scripts
- `Makefile` — standardized commands

## Task Breakdown
See `docs/tasks/` for the ordered list.

## Known prerequisites NOT yet automated
- Manual `cp .env.example .env` after clone (TODO: add to make setup)
```

### Les 4 conditions obligatoires

> "4 conditions: can start, can test, can see progress, can pick up next steps." — Lecture 06

| Condition | Vérification |
|-----------|--------------|
| **Can start** | `make setup` + `make dev` fonctionnent |
| **Can test** | `make test` retourne pass/fail clair |
| **Can see progress** | `PROGRESS.md` lisible, à jour |
| **Can pick up next steps** | `task-breakdown.md` ou équivalent |

Si une seule manque → l'init phase n'est pas terminée.

### La section "Current State (verified on YYYY-MM-DD)"

Chaque ligne doit avoir une **preuve d'exécution récente** :

❌ `- [x] Tests configured` (vague)
✅ `- [x] Test framework configured (Vitest), example test passing (1/1) verified 2026-05-24`

La date est cruciale : on saura si l'état a vieilli.

### Le format des commandes

Privilégier les **commandes Make** (ou équivalent) plutôt que des commandes brutes :

❌ `npm run dev -- --port 3000 --host 0.0.0.0`
✅ `make dev`

Bénéfices :
- L'agent n'a pas à mémoriser les flags
- Si la commande change, on update le Makefile, pas tous les docs
- La même commande marche cross-platform

### Lien avec init.sh

Certains projets ont un `init.sh` qui combine setup + verify :

```bash
#!/bin/bash
set -e
make setup
make verify
echo "✅ Ready to work."
```

Idéal pour les agents : une seule commande à lancer en clock-in.

Voir aussi `claude-progress.md` lié à `init.sh` dans les [projets du curriculum](harness-curriculum-projects-overview.md).

### Le piège "ça marche sur ma machine"

L'init checklist doit avoir été **testée sur un clone propre** :

```bash
cd /tmp
git clone <repo>
cd <repo>
make setup
make verify
```

Si ça échoue → la checklist ment. Le test sur clone propre est non-négociable.

### Sous-sections optionnelles

#### Configuration optionnelle

Ce qui n'est pas requis mais améliore l'expérience :

```markdown
## Optional (recommended)
- Install pre-commit hooks: `make hooks-install`
- Enable VS Code workspace settings: `code .` then "Trust workspace"
```

#### Troubleshooting

Pour les erreurs récurrentes :

```markdown
## Troubleshooting

### Error: "EADDRINUSE: port 3000 in use"
Run `make stop` to kill orphan processes.

### Error: "Cannot find module 'X'"
Re-run `make setup`. If persistent, delete node_modules and retry.
```

### Mise à jour de la checklist

À chaque init phase (généralement une par release majeure ou par refactor structurel), la checklist est ré-écrite et re-vérifiée.

Critère : si quelqu'un change le `Makefile` ou ajoute une dependency, **il met à jour la checklist** dans le même PR.

### Lien avec le clean state

[Clean state checklist](template-clean-state-checklist.md) (fin de session) est différent :

| Document | Quand | Quoi |
|----------|-------|------|
| **Startup readiness** | Début (one-time, post-init) | Comment démarrer + état initial |
| **Clean state checklist** | Fin (chaque session) | Le repo est-il dans un état propre ? |

Les deux se complètent.

### Antipatterns

- ❌ Pas de checklist du tout → chaque session redécouvre
- ❌ Checklist obsolète → l'agent suit, échoue, perd la confiance
- ❌ "Run `npm install && npm start`" comme seule instruction → manque les détails (env vars, services externes)
- ❌ Checklist trop longue (>50 lignes) → noyée, [lost-in-the-middle-effect](lost-in-the-middle-effect.md)

### À retenir

1. **4 conditions** : can start / can test / can see progress / can pick up next.
2. Chaque check a une **date de vérification**.
3. Tester sur un **clone propre** avant de commit.
4. Utiliser **make commands** plutôt que commandes brutes.
5. Mise à jour à chaque changement structurel.

## Related pages

- [initialization-phase-separation](initialization-phase-separation.md)
- [task-breakdown-structure](task-breakdown-structure.md)
- [template-clean-state-checklist](template-clean-state-checklist.md)
- [fresh-session-readability-test](fresh-session-readability-test.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
