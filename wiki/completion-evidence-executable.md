# Completion evidence (exécutable)

**Summary** : "Done" n'est jamais "le code a l'air complet". "Done" est "la commande de vérification retourne 0 / le test passe / le curl renvoie 201". L'evidence de complétion doit être **exécutable et observable**, jamais subjective.

**Sources** : `raw/ingested/lecture-07-draw-clear-task-boundaries-for-agents.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "Completion evidence must be executable — 'the code looks fine' doesn't count; 'curl returns 201' does." — Lecture 07

Trois exigences :

1. **Exécutable** : peut être lancé par n'importe qui (ou par la harness automatiquement)
2. **Observable** : produit un output binaire ou comparable (pass/fail, code de retour, valeur)
3. **Reproductible** : même input → même output

### Pourquoi pas la subjective "ça marche"

L'agent qui auto-évalue son travail souffre de [[confidence-calibration-bias|confidence calibration bias]] : il se sent fini bien avant d'avoir réellement fini.

> "Modern neural networks are systematically overconfident." — Guo et al. 2017

Solution : remplacer le sentiment par un signal d'exécution objectif.

### Bonnes evidences

| Evidence | Pourquoi c'est exécutable |
|----------|---------------------------|
| `curl POST /api/register \| jq -e '.success == true'` | Code de retour 0/1 observable |
| `pytest tests/test_auth.py::test_login_valid` | Pass/fail clair |
| `npm run build && [ -f dist/app.js ]` | Combinaison exécutable |
| `playwright test --grep "user can sign up"` | Comportement E2E observable |
| Screenshot diff via Puppeteer | Output binaire (match/no match) |

### Mauvaises evidences

| "Evidence" | Pourquoi c'est insuffisant |
|------------|---------------------------|
| "Code review approved" | Subjectif, dépend du reviewer |
| "Tests pass" (sans préciser lesquels) | Trop vague, ne dit pas si la *nouvelle* feature est couverte |
| "Manual test OK" | Pas reproductible |
| "It works on my machine" | Voir Lecture 02 sur reproductibilité |
| "Implementation complete" | C'est exactement le sentiment qu'on veut éviter |

### Le format dans une feature list

Chaque tâche dans `task-breakdown.md` ou `feature_list.json` doit déclarer sa verification command :

```json
{
  "id": "001",
  "behavior": "User registration",
  "verification": "curl -X POST localhost:3000/api/register -d '{...}' | jq -e '.success == true'",
  "status": "not_started"
}
```

Voir [[template-feature-list-json]].

### Les 3 couches de vérification (Lecture 09)

Voir [[three-layer-termination-validation]] :

1. **Syntaxe / static** : lint clean, typecheck clean
2. **Behavior runtime** : tests unitaires, intégration
3. **System-level** : E2E avec scénario user complet

Une evidence "executable" doit couvrir au moins la couche 2. Idéalement la couche 3.

### Pattern : verification command dans feature

Format recommandé pour chaque feature :

```markdown
## Feature: User registration

**Verification**:
```bash
# 1. Run the endpoint
RESPONSE=$(curl -s -X POST http://localhost:3000/api/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"Pass1234!"}')

# 2. Assert response shape
echo "$RESPONSE" | jq -e '.success == true' || { echo "FAIL: success != true"; exit 1; }
echo "$RESPONSE" | jq -e '.userId | length > 0' || { echo "FAIL: no userId"; exit 1; }

# 3. Assert side effect (user exists in DB)
psql -c "SELECT COUNT(*) FROM users WHERE email = 'test@example.com'" | grep -q '1' || { echo "FAIL: user not in DB"; exit 1; }

echo "✅ Registration OK"
```
```

C'est plus long qu'un "test should pass", mais c'est **reproductible et observable**.

### Le piège "tests pass" sans nouveau test

Pattern fréquent :
1. Agent code la feature
2. Agent lance `npm test` → 247/247 passent (mais aucun ne couvre la nouvelle feature)
3. Agent déclare "tests pass, feature complete"

Faute : il n'y a **pas de test pour la nouvelle feature**. La verification doit forcer l'existence d'un test spécifique :

```bash
pytest tests/test_registration.py -v --tb=short
# Must include test_register_valid, test_register_duplicate, test_register_invalid_password
```

### Tests unitaires ne sont pas assez (Lecture 10)

Voir [[end-to-end-verification-only]] : les tests unitaires testent des morceaux isolés. Les défauts de **limites** (interface mismatch, state propagation) ne sont visibles qu'en E2E.

Pour qu'une feature soit "passing" en sens strict, il faut idéalement :
- Test unitaire de la logique
- Test d'intégration des couches
- Test E2E du flow complet

### Lien avec WIP=1

[[wip-limit-discipline|WIP=1]] dit "finir avant de démarrer une autre". Mais "finir" doit avoir un critère **objectif** — c'est exactement le rôle de completion evidence.

Sans evidence executable :
- Agent peut auto-déclarer `passing`
- WIP=1 devient WIP=N de fait (parce que rien ne finit vraiment)
- On perd le bénéfice

### Pratique : encoder dans la harness

#### `make verify-feature-001`

Un target par feature, qui exécute la verification :

```makefile
verify-feature-001:
	@bash scripts/verify-001.sh

verify-feature-002:
	@bash scripts/verify-002.sh

verify-all:
	@for i in 001 002 003; do make verify-feature-$$i; done
```

L'agent run `make verify-feature-001` avant de marquer `passing`. La harness peut le run automatiquement (PostToolUse, ou hook Stop).

### À retenir

1. **"Done" = verification command retourne 0**, jamais "ça a l'air bon".
2. Exécutable + observable + reproductible.
3. Chaque feature dans le breakdown a **sa propre** verification command.
4. Méfiance des "tests pass" qui ne couvrent pas la nouvelle feature.
5. Idéal : verification = E2E, pas juste unitaire.

## Related pages

- [[verified-completion-rate-metric]]
- [[wip-limit-discipline]]
- [[three-layer-termination-validation]]
- [[end-to-end-verification-only]]
- [[confidence-calibration-bias]]
- [[feature-list-as-primitive]]
- [[the-harness-engineering-curriculum-summary]]
