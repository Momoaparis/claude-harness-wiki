# Seul l'end-to-end vérifie vraiment

**Summary** : Les tests unitaires isolent et mockent → ils sont **aveugles** aux défauts de boundary entre composants. Seul l'end-to-end teste l'intégration réelle. Quand l'agent **sait** qu'il sera validé en E2E, il code différemment : il anticipe les interfaces, respecte les boundaries, gère les erreurs.

**Sources** : `raw/ingested/lecture-10-only-a-full-pipeline-run-counts-as-real-verification.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le constat

> "Only end-to-end testing can prove the absence of system-level defects." — Lecture 10

Les tests unitaires testent des **morceaux**. Mais beaucoup de bugs vivent **entre** les morceaux :

| Type de bug | Détectable par unit tests ? |
|-------------|------------------------------|
| Logique métier dans une fonction | ✅ |
| Type mismatch dans une fonction | ✅ |
| Interface mismatch entre 2 modules | ❌ |
| State propagation incohérent (DB / cache / ORM) | ❌ |
| Resource lifecycle (file handles, DB connections) | ❌ |
| Environment dependency (config, network, latence) | ❌ |
| Error propagation cross-couches | ❌ |

### Les 5 catégories de boundary defects

#### 1. Interface mismatch

Module A passe une donnée. Module B attend autre chose. Tests unitaires : chacun mocké, chacun passe. Réalité : crash.

**Exemple Lecture 10** : renderer Electron passe un chemin relatif. Service attend un chemin absolu. Unit tests OK. Run réel = `ENOENT`.

#### 2. State propagation error

Migration DB change le schéma. Cache ORM garde l'ancien. Tests unitaires : mockent la DB. Réalité : queries cassent.

**Exemple** : ajout colonne `created_at`. Migration appliquée. Cache TypeORM pas vidé. Les inserts crashent en prod.

#### 3. Resource lifecycle

Fichiers, connections DB, sockets — leur lifecycle span plusieurs composants. Unit tests jamais.

**Exemple** : un endpoint ouvre une connection, oublie de la fermer. 1000 requests plus tard → DB connection pool épuisé.

#### 4. Environment dependency

Code marche en test (tout mocké), casse en prod (config différente, latence réseau, services down).

**Exemple** : test passe avec mock S3. Prod utilise vraie S3 → latence inattendue → timeout d'un caller.

#### 5. Error propagation

Erreur lancée dans le module bas, "swallowée" dans le middle, surface comme 500 vide en haut. Unit tests : chacun seul, OK.

**Exemple** : DB timeout → repo throw → service catch + log → endpoint return 500 "internal error". L'utilisateur ne sait rien.

### Le E2E behavior change

> "Agents code differently when they know they'll be E2E-validated." — Lecture 10

Observable empiriquement :

| Sans E2E required | Avec E2E required |
|-------------------|-------------------|
| Mock generously, focus sur la logique interne | Considère les interfaces externes |
| Pas de gestion d'erreurs "soft" | Gère les cas dégradés |
| Pas d'idempotence pour POST | Pense à la retry strategy |
| Ignore les latences | Met des timeouts |

L'**existence** d'un test E2E qui sera run force l'agent à intégrer ces préoccupations.

### Pattern : verification = E2E command

Dans [le task breakdown](task-breakdown-structure.md), la verification command doit être E2E quand possible :

❌ `pytest tests/unit/test_register.py` (unit)
✅ `make test-e2e -- --grep "user registration flow"` (E2E)

L'unit test reste utile pour le debug. Mais le **gate de complétion** est le E2E.

### Le testing pyramid

Modèle classique (Google) :

```
        /\
       /E2E\        ← peu nombreux, lents, valeur max
      /─────\
     /Integr.\      ← couches intermédiaires
    /─────────\
   /   Unit    \    ← nombreux, rapides, valeur isolée
  /─────────────\
```

**Important** : la pyramide n'élimine pas E2E, elle dit "moins nombreux **mais** existants". Zéro E2E = pyramide cassée.

### Layered Domain Architecture

OpenAI recommande un layering strict avec **dépendances forward seulement** :

```
Types → Config → Repo → Service → Runtime → UI
```

Chaque couche dépend **uniquement** des couches en amont. Pas de retour en arrière.

Avec ce layering, les boundary defects sont **localisés** : entre chaque paire de couches. Tests E2E = traverse toutes les couches.

### Architectural boundary enforcement

Pour empêcher les violations de boundary, encoder en check mécanique :

```bash
# Custom lint : interdire `require('fs')` dans le code renderer Electron
grep -r "require('fs')" src/renderer/ && {
  echo "❌ fs not allowed in renderer"; exit 1
}
```

Voir [architectural-boundary-enforcement](architectural-boundary-enforcement.md).

### Tools E2E recommandés

| Stack | Outil |
|-------|-------|
| Web frontend | Playwright, Cypress |
| API REST | curl scripts, supertest, httpx |
| CLI | bats, expect |
| Electron | Playwright via spectron |
| Mobile | Detox, Appium |
| Background jobs | Run avec real broker (rabbitmq/redis), assert side effects |

### Agent-oriented error messages

Quand E2E échoue, le message d'erreur doit être actionable :

❌ `Test failed.`

✅ ```
E2E test failed: tests/e2e/auth.spec.ts:42
  Expected: registration form succeeds
  Actual: form crashed with "ENOENT path /relative"
  Likely cause: relative path being passed where absolute expected
  Fix: in src/renderer/forms.ts line 87, use path.resolve(...)
```

Le format **What / Why / Fix** rend l'erreur exploitable par l'agent. Voir [architectural-boundary-enforcement](architectural-boundary-enforcement.md) pour le Review Feedback Promotion pattern.

### Cas réel : Electron file export (Lecture 10)

5 défauts dans une feature "export file" :

| Défaut | Détecté par unit ? | Détecté par E2E ? |
|--------|---------------------|--------------------|
| Interface mismatch (relative vs absolute path) | ❌ | ✅ |
| State propagation (file extension stored old) | ❌ | ✅ |
| Resource leak (file handle non-closed) | ❌ | ✅ |
| Permission issue (writes to read-only dir) | ❌ | ✅ |
| Error propagation (no user feedback on fail) | ❌ | ✅ |

**0 sur 5 unit, 5 sur 5 E2E.** L'absence de E2E aurait laissé tous les bugs passer.

### Antipatterns

- ❌ "Tests pass = feature done" (sans préciser unit vs E2E)
- ❌ Mocker tellement qu'il ne reste plus de système à tester
- ❌ E2E sans CI bloquante → développeurs les skip
- ❌ E2E trop lents (>10 min) → développeurs les skip aussi
- ❌ Pas de test E2E pour les flows critiques (login, payment)

### Coût et stratégie

E2E coûte plus :

- Lent (10x à 100x unit)
- Plus fragile (flaky)
- Setup d'environment plus complexe

**Stratégie** : E2E sur les **flows utilisateur critiques** (login, achat, signup, données critiques). Pas E2E sur tout.

Mais : **toute nouvelle feature critique** doit avoir au moins un E2E.

### À retenir

1. Tests unitaires sont **aveugles** aux boundary defects.
2. **5 catégories de bugs** invisibles aux unit : interface / state / resource / env / error.
3. L'agent **code mieux** quand il sait qu'il sera E2E-validé.
4. La verification command de chaque tâche critique doit être E2E.
5. E2E lent mais **incomparable** sur les flows utilisateur.

## Related pages

- [three-layer-termination-validation](three-layer-termination-validation.md)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [task-breakdown-structure](task-breakdown-structure.md)
- [checkpoint-vs-continuous-evals](checkpoint-vs-continuous-evals.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
