# Architectural boundary enforcement

**Summary** : Plutôt qu'écrire "ne mets pas X dans Y" dans `AGENTS.md`, encoder l'invariant comme **check mécanique** (lint custom, CI rule, script). L'agent ne peut pas violer une règle qui fait échouer le build. Pattern complémentaire : Review Feedback Promotion — chaque commentaire récurrent de review devient une rule auto.

**Sources** : `raw/ingested/lecture-10-only-a-full-pipeline-run-counts-as-real-verification.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "Enforce invariants; don't micromanage implementation." — Lecture 10

> "Every time you discover a new category of agent error during code review, turn it into an automated check." — Lecture 10

Deux applications :

1. **Pre-encoded boundaries** : avant même que l'agent commence, encoder les contraintes architecturales en checks
2. **Review Feedback Promotion** : à chaque code review, si un comment se répète, le promouvoir en check auto

### Pourquoi mécanique > textuel

Comparaison :

| Approche textuelle | Approche mécanique |
|--------------------|---------------------|
| `AGENTS.md` : "Don't import `fs` in renderer code" | Linter custom : `grep -r "require('fs')" src/renderer/ && exit 1` |
| Risque : l'agent ignore la règle ([lost-in-the-middle-effect](lost-in-the-middle-effect.md)) | Garantie : le build échoue immédiatement |
| Mise à jour : modifier la doc | Mise à jour : modifier le script |
| Traçabilité : Aucune ("est-ce que l'agent a lu ?") | Traçabilité : exit code, log |

### Exemples concrets

#### Boundary : pas d'accès DB direct hors `src/db/`

```bash
# scripts/check-db-boundary.sh
#!/bin/bash
VIOLATIONS=$(grep -r "import.*from.*'@/db'" src/ --include="*.ts" | grep -v "^src/db/")
if [ -n "$VIOLATIONS" ]; then
  echo "❌ DB access outside src/db/:"
  echo "$VIOLATIONS"
  echo "Fix: route through src/db/repository functions instead"
  exit 1
fi
```

#### Boundary : Electron renderer ne peut pas utiliser Node APIs

```bash
# scripts/check-renderer-isolation.sh
#!/bin/bash
FORBIDDEN_IMPORTS=("require('fs')" "require('os')" "require('child_process')" "require('path')")
for imp in "${FORBIDDEN_IMPORTS[@]}"; do
  if grep -r "$imp" src/renderer/ ; then
    echo "❌ Forbidden in renderer: $imp"
    echo "Fix: use IPC to call main process instead"
    exit 1
  fi
done
```

#### Boundary : layered architecture (forward dependencies only)

```bash
# scripts/check-layering.sh
#!/bin/bash
# Service ne doit pas importer de Runtime ou UI
if grep -r "from '@/runtime'" src/service/ ; then
  echo "❌ Service importing from Runtime layer"; exit 1
fi
if grep -r "from '@/ui'" src/service/ ; then
  echo "❌ Service importing from UI layer"; exit 1
fi
```

### Intégration dans la harness

#### Make target

```makefile
check-architecture:
	@bash scripts/check-db-boundary.sh
	@bash scripts/check-renderer-isolation.sh
	@bash scripts/check-layering.sh
.PHONY: check-architecture

verify: check-architecture test-unit test-integration test-e2e
```

#### Hook PostToolUse

À chaque Write/Edit, run check-architecture :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "make check-architecture",
        "description": "Verify architectural boundaries after each file modification"
      }
    ]
  }
}
```

L'agent qui viole une boundary se voit immédiatement signaler l'erreur.

### Review Feedback Promotion

> "Every time you discover a new category of agent error during code review, turn it into an automated check." — Lecture 10

Workflow :

```
1. Reviewer commente : "Don't use console.log in production code"
2. Agent fix le PR
3. **Mais** : c'est la 3ème fois que le reviewer fait ce commentaire
   → Promotion : `grep -r 'console.log' src/ | grep -v 'src/test' && exit 1`
4. Add check to make verify
5. Future agent runs ne peuvent plus introduire ce bug
```

Le harness **grandit** à chaque review. Chaque commentaire = potentiel check auto.

### Cycle de croissance

```
Bug réel → Code review comment → Comment récurrent → Check auto → Harness plus forte
```

Sur 1 an de discipline, le harness peut accumuler des dizaines de checks qui éliminent des classes entières de bugs.

### Format du message d'erreur

Quand un check échoue, le message **doit être actionable** :

❌ `Lint error in renderer/auth.ts`

✅ ```
❌ Renderer cannot import 'fs' (line 12)
  Why: Electron renderer runs in browser context, no Node APIs available
  Fix: Use IPC to call src/main/files.ts:exportFile() instead
  Reference: docs/architecture/electron-ipc.md
```

Format **What / Why / Fix / Reference**. Voir [agent-oriented error messages](end-to-end-verification-only.md).

### Lien avec instruction design patterns

C'est l'application directe de "constrain, don't micromanage" (voir [instruction-design-patterns](instruction-design-patterns.md)). Plutôt qu'accumuler des règles textuelles ([instruction bloat](modular-instruction-architecture.md)), encoder les invariants en checks.

### Coût de mise en place

Bonne nouvelle : un check architectural prend généralement **5-20 lignes de shell**. Bénéfice : protège tous les futurs runs.

ROI : très favorable même pour des règles "petites".

### Antipatterns

- ❌ Régulariser via review comments uniquement, sans promotion → mêmes bugs reviendront
- ❌ Checks trop stricts qui bloquent les vrais cas → bypass généralisé
- ❌ Checks sans message Fix → l'agent ne sait pas quoi faire
- ❌ Checks dans le commit hook **et** la CI **et** local → friction

Bonne stratégie : run en **PostToolUse** (signal immédiat) + **CI** (gate final). Pas en pre-commit (trop friction).

### Exemples étendus

#### Pas de TODO en main

```bash
grep -r "TODO" src/ --include="*.ts" | grep -v "TODO(deferred)" && exit 1
# Format imposé : TODO(deferred): explanation
```

#### Imports triés

```bash
# Run eslint avec rule "import/order"
npx eslint --rule '{"import/order": "error"}' src/
```

#### Pas de any en TypeScript

```bash
grep -r ": any" src/ --include="*.ts" && {
  echo "❌ ':any' forbidden — use unknown or define type"; exit 1
}
```

### Lien avec OpenAI / Anthropic

> "For agent-generated codebases, architectural constraints must be established as early prerequisites on day one." — OpenAI

Justification : les agents **copient** les patterns existants ([coffee cup effect](harness-rot-et-dette-technique.md)). Si un pattern non-désiré apparaît une fois, il se reproduit. Donc encoder les boundaries dès le jour 1.

### À retenir

1. **Encoder les boundaries en checks**, pas en règles textuelles.
2. **Review Feedback Promotion** : chaque comment récurrent → check auto.
3. Message d'erreur **What / Why / Fix / Reference**.
4. Intégration via **Make target + PostToolUse hook + CI**.
5. Le harness **grandit** au fil des reviews. C'est gratuit en compoundé.

## Related pages

- [end-to-end-verification-only](end-to-end-verification-only.md)
- [instruction-design-patterns](instruction-design-patterns.md)
- [modular-instruction-architecture](modular-instruction-architecture.md)
- [claude-code-hooks](claude-code-hooks.md)
- [harness-rot-et-dette-technique](harness-rot-et-dette-technique.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
