# Session clean handoff — les 5 conditions

**Summary** : "Clean state" en fin de session = 5 conditions simultanées : build passe, tests passent, progress enregistré, pas d'artefacts stales, startup path standard fonctionnel. Manquer une seule = session incomplète. Avec discipline : 100%→97% build maintenance sur 12 semaines. Sans : 100%→68%.

**Sources** : `raw/ingested/lecture-12-leave-a-clean-handoff-at-the-end-of-every-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "The quality of state at the end of each session directly determines the next session's efficiency." — Lecture 12

Une session qui termine "à peu près" laisse la suivante en mode diagnostic. Une session qui termine **propre** permet à la suivante de coder en 3 min.

### Les 5 conditions non-négociables

```
       ┌─────────────────────────────────────┐
       │  CLEAN STATE = TOUTES les 5 :       │
       │                                     │
       │  1. ☐ Build passes                  │
       │  2. ☐ Tests pass                    │
       │  3. ☐ Progress recorded             │
       │  4. ☐ No stale artifacts            │
       │  5. ☐ Startup path works            │
       └─────────────────────────────────────┘
```

#### 1. Build passes

```bash
make build  # ou npm run build, cargo build, etc.
# Exit 0 obligatoire
```

Pas "build runs", **passes**. Si la build est cassée, la session suivante doit fixer **avant** de bosser sur la feature.

#### 2. Tests pass

```bash
make test  # tous, pas juste les nouveaux
# Exit 0 obligatoire
```

Inclut :
- Unit tests
- Integration tests
- E2E tests (si pas trop lents)

Si on a temporairement skippé un test → c'est un **blocker à logger**, pas un "on verra".

#### 3. Progress recorded

- `PROGRESS.md` updaté avec l'entrée de la session
- `feature_list.json` à jour (transitions d'état)
- `Next best step` clair pour la prochaine session

Voir [[progress-file-pattern]].

#### 4. No stale artifacts

À supprimer/nettoyer :

- `console.log`, `print()`, `debugger;` parasites
- TODOs sans format (`TODO:` sans contexte vs `TODO(deferred): explanation`)
- Fichiers temporaires (`/tmp/debug-*`, `*.bak`)
- Code commenté (sauf si documenté pourquoi)
- Branches locales abandonnées

#### 5. Startup path works

```bash
# Cloner sur autre machine (mentalement) :
git clone <repo>
cd <repo>
make setup
make dev
# Doit marcher sans intervention
```

Si `make dev` casse → la session N+1 commence dans le mur.

### Le test "transaction integrity"

> "Session integrity, analogue to DB transactions — commit or rollback, no middle ground." — Lecture 12

Une session :
- **Commit complet + clean state** ✅
- **Rollback (rien committé)** ✅
- ❌ "demi-commit" — code écrit, tests cassés, progress pas updaté → **dangereux**

Voir [[acid-principles-agent-state]] pour le full ACID mapping.

### Cas réel : 12 semaines (Lecture 12)

#### Sans discipline

| Semaine | Build pass | Tests pass | Startup time |
|---------|------------|------------|--------------|
| W1 | 100% | 100% | 5 min |
| W4 | 95% | 92% | 15 min |
| W8 | 82% | 78% | 35 min |
| **W12** | **68%** | **61%** | **60+ min** |

Le projet devient impraticable.

#### Avec discipline

| Semaine | Build pass | Tests pass | Startup time |
|---------|------------|------------|--------------|
| W1 → W12 | 100% → 97% | 100% → 95% | 5 → 9 min |

**Différence** : +29% build, +34% tests, -85% startup. Même équipe, même nombre de sessions, **seule la discipline change**.

### Le template clean state checklist

Voir [[template-clean-state-checklist]] pour le format complet à copier-coller. Format minimal :

```markdown
## Session Exit Checklist

- [ ] `make build` passes
- [ ] `make test` passes (all tests, including pre-existing)
- [ ] `feature_list.json` is up to date
- [ ] `PROGRESS.md` has today's session entry with "Next best step"
- [ ] No `console.log`, `debugger`, or undocumented TODOs in `src/`
- [ ] `make dev` starts cleanly from a fresh terminal
- [ ] All changes committed (`git status` is clean)
```

### Le "clean up later = never"

> "'Clean up later' means never clean up." — Lecture 12

Si la session N termine avec des artefacts stales :

- Session N+1 ne sait pas ce qui est intentionnel ou pas
- Session N+1 ajoute ses propres artefacts
- Session N+2 reçoit un repo en cumulant les deux
- Cycle vicieux

Solution : **chaque** session paie sa dette. Pas de "dette différée".

### Idempotent cleanup scripts

Pour faciliter le respect de la checklist, des scripts **idempotents** :

```bash
#!/bin/bash
# scripts/cleanup.sh — safe à run plusieurs fois

set -e

# Remove debug logs
rm -f /tmp/debug-*.log /tmp/*.bak

# Reset local-only files
git checkout -- .env.local 2>/dev/null || true

# Format check
make format-check

# Verify
make build
make test

# Update progress
echo "Run after: $(date)" >> .last-cleanup
```

Idempotent = retry-safe (run plusieurs fois = même résultat).

### Le Stop hook automatique

Encoder la checklist en hook Stop pour qu'elle soit **forcée** :

```json
{
  "hooks": {
    "Stop": [
      {
        "command": "./scripts/clean-state-check.sh",
        "description": "Block session end if clean state not achieved"
      }
    ]
  }
}
```

Voir [[claude-code-hooks]].

### Lien avec context anxiety

Quand l'agent sent la fin de contexte arriver ([[context-anxiety-modeles]]), il peut sauter la clôture propre. Solution : déclencher la checklist **à 70%** du contexte, pas à 95%. Garder de la marge.

### High-throughput merge philosophy (cas particulier)

> "When agent output >> human review capacity, minimize blocking gates." — Lecture 12

OpenAI cite : 3.5 PRs/jour, short-lived, fast merge. Coût fix < coût attendre review → merge rapide, fix vite.

**Mais** : cette philosophie n'élimine pas le clean state. Elle assume **encore plus fortement** un clean state pour permettre les fast merges. Si le clean state n'est pas garanti, fast merge = chaos.

### Antipatterns

- ❌ "Tests cassés, je fix demain" → 3 sessions plus tard, plus personne ne sait quels tests
- ❌ "Build cassée mais on continue" → drift exponentiel
- ❌ Pas de PROGRESS update → la session suivante perd 20 min à diagnostiquer
- ❌ "Le `console.log` est important pour le debug" → committer = laisser pourrir
- ❌ Skip la checklist "juste cette fois" → norme glissante

### À retenir

1. **5 conditions non-négociables**. Manquer une = session incomplète.
2. **Transaction integrity** : commit ou rollback, pas de middle ground.
3. **12 semaines** sans discipline → 68% build, 61% tests. Avec → 97/95%.
4. **Hook Stop** force la checklist mécaniquement.
5. "Clean up later = never". Chaque session paie sa dette.

## Related pages

- [[template-clean-state-checklist]]
- [[harness-entropy-management]]
- [[progress-file-pattern]]
- [[acid-principles-agent-state]]
- [[context-anxiety-modeles]]
- [[claude-code-hooks]]
- [[the-harness-engineering-curriculum-summary]]
