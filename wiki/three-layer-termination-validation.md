# Validation de complétion en 3 couches

**Summary** : Avant de déclarer une tâche "fait", elle doit passer 3 couches successives de vérification : (L1) syntaxe/static, (L2) comportement runtime, (L3) confirmation système-level. Sauter une couche = victoire prématurée.

**Sources** : `raw/ingested/lecture-09-preventing-agents-from-declaring-victory-too-early.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "All three layers of validation are essential: syntax passes, behavior passes, system passes." — Lecture 09

| Couche | Vérifie | Outils |
|--------|---------|--------|
| **L1 — Syntax / Static** | Le code est syntaxiquement valide et passe les checks statiques | Linter, typechecker, formatter |
| **L2 — Behavior runtime** | Les comportements unitaires marchent | Tests unitaires, tests d'intégration |
| **L3 — System-level** | Le système complet fonctionne en end-to-end | Tests E2E (Playwright, curl scripts) |

### Pourquoi 3 couches

Chaque couche capture des **catégories différentes** de bugs :

- L1 manque → le code ne compile même pas
- L2 manque → la logique métier est cassée
- L3 manque → l'intégration entre composants est cassée (le cas le plus subtil)

Voir [end-to-end-verification-only](end-to-end-verification-only.md) pour le focus sur L3.

### Le flow

```
Agent declares: "Task done"
          │
          ▼
   ┌─────────────┐
   │ L1: Static  │ ──── fail ──► refuser, fix, retry
   └─────────────┘
          │ pass
          ▼
   ┌─────────────┐
   │ L2: Runtime │ ──── fail ──► refuser, fix, retry
   └─────────────┘
          │ pass
          ▼
   ┌─────────────┐
   │ L3: System  │ ──── fail ──► refuser, fix, retry
   └─────────────┘
          │ pass
          ▼
   Task transitions to `passing`
```

### Layer 1 — Syntax / Static

**Commandes typiques** :

```bash
make lint        # ESLint, pylint, golangci-lint
make typecheck   # tsc, mypy
make format-check  # prettier --check, black --check
```

**Ce que ça attrape** :
- Erreurs de syntaxe
- Imports manquants
- Types incohérents
- Variables non utilisées
- Conventions de style

**Pas de coût d'exécution** : pas besoin de DB ou service externe.

### Layer 2 — Behavior runtime

**Commandes typiques** :

```bash
make test            # Tous les tests
make test-unit       # Spécifique unit
make test-integration  # Intégration entre modules
```

**Ce que ça attrape** :
- Logique métier cassée
- Edge cases mal gérés
- Régressions sur des fonctions existantes

**Limite** : les tests unitaires **isolent** les composants. Ils ne testent pas la **boundary** entre eux.

### Layer 3 — System-level

**Commandes typiques** :

```bash
make test-e2e        # Playwright, Cypress
./scripts/smoke-test.sh  # Curl scripts qui simulent un user flow
```

**Ce que ça attrape** (voir [end-to-end-verification-only](end-to-end-verification-only.md) pour le détail) :

- **Interface mismatch** entre couches (renderer passe relative path, service attend absolute)
- **State propagation** error (DB migration changée, ORM cache pas vidé)
- **Resource lifecycle** issue (fichiers, connexions DB, sockets)
- **Environment dependency** issue (config différente entre test et prod)

**Coût élevé** mais **valeur incomparable** : c'est la seule couche qui prouve que le système marche **vraiment**.

### Le piège "tests unitaires passent donc terminé"

> "Unit tests pass but the app didn't start." — Lecture 09

Pattern fréquent :

1. Agent code la feature
2. Agent écrit des tests unitaires avec mocks
3. Agent run les tests → ils passent
4. Agent déclare "terminé"
5. **Personne** ne lance l'app entière → l'app crashe au démarrage

L1 + L2 ne suffisent pas. L3 est obligatoire.

### Externaliser le jugement de complétion

> "Your harness must replace the agent's feelings with externalized, execution-based verification." — Lecture 09

Le sentiment de l'agent n'est pas une evidence. Voir [confidence-calibration-bias](confidence-calibration-bias.md) : les LLMs sont systématiquement overconfident.

Solution :
- L1, L2, L3 sont chacune une **commande exécutable**
- Le harness les run, pas l'agent (sinon il peut tricher)
- L'output (exit code, log) est la **seule** source de "done"

### Comment encoder dans la harness

#### Make targets

```makefile
verify-l1:
	@make lint typecheck

verify-l2:
	@make test

verify-l3:
	@make test-e2e

verify:
	@make verify-l1 && make verify-l2 && make verify-l3
.PHONY: verify-l1 verify-l2 verify-l3 verify
```

#### Hook Stop

Empêcher la session de finir si `make verify` échoue :

```json
{
  "hooks": {
    "Stop": [
      {
        "command": "make verify",
        "description": "Refuse la fin de session si une couche L1-L3 échoue"
      }
    ]
  }
}
```

#### CI bloquante

```yaml
on: pull_request
jobs:
  verify:
    steps:
      - run: make verify-l1
      - run: make verify-l2
      - run: make verify-l3
```

### Refactoring while verifying is poison

> "Refactoring shifts the boundary between verified and unverified code." — Lecture 09

Antipattern : pendant qu'on est en train de vérifier une feature, refactor du code adjacent "tant qu'on y est". Résultat : on déplace la frontière entre vérifié et non-vérifié sans le savoir.

Règle : **vérifier d'abord, refactor ensuite**. Jamais en même temps.

### Données Anthropic (Lecture 09)

| Setup | Runtime | Cost | Working |
|-------|---------|------|---------|
| Single agent | 20 min | $9 | **Non** |
| 3 agents (planner + generator + evaluator) avec L1-L3 | 6 heures | $200 | **Oui** |

Le setup multi-agent coûte plus mais **réussit** vs un setup mono-agent qui rate.

### Cas réel : Electron app (Lecture 09)

Tasks où `make test` passait (L2 OK) mais L3 échouait :

- App ne démarrait pas (config manquante)
- Renderer crashait après login (interface mismatch avec preload)
- DB locked après migration (resource lifecycle)
- Test fixtures différents de prod config

Sans L3, on aurait merge → bug en prod.

### Actionable error feedback

Quand L1/L2/L3 échoue, le message d'erreur doit être **utilisable par l'agent** :

❌ `Test failed`
✅ `Test failed: tests/integration/auth.test.ts:42. Expected 201, got 500. Stack: ConnectionRefused on localhost:5432. FIX: ensure DB is running via 'make db-up'.`

Format **What / Why / Fix**.

### À retenir

1. **3 couches** : L1 static, L2 runtime, L3 system.
2. Sauter une couche = victoire prématurée.
3. **L'agent ne juge pas**. C'est le harness qui run.
4. L3 est ce qui capture les **boundary defects**.
5. Refactor pendant vérif = poison. Vérifier d'abord.

## Related pages

- [confidence-calibration-bias](confidence-calibration-bias.md)
- [worker-checker-separation](worker-checker-separation.md)
- [end-to-end-verification-only](end-to-end-verification-only.md)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
