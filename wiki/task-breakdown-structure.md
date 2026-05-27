# Task breakdown — structure

**Summary** : Split d'un projet entier en liste ordonnée de tâches atomiques. Chaque tâche = description du comportement attendu + critères d'acceptation + commande de vérification. Pas de directive vague, du structuré exécutable.

**Sources** : `raw/ingested/lecture-06-make-the-agent-initialize-before-every-work-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le rôle

Output canonique de la phase d'init : un fichier qui dit à toute session future "voici la prochaine tâche, voici comment savoir qu'elle est faite".

Sans ça, chaque session :
- Choisit sa propre priorité (drift)
- Définit sa propre "done" condition (incohérence)
- Re-fait potentiellement du travail déjà fait

### Le format

```markdown
# Task Breakdown

## Task 001 — User registration endpoint

**Behavior**: Endpoint `POST /api/register` accepte email + password, crée un user, retourne `{success: true, userId}`.

**Acceptance criteria**:
- Email validation (RFC 5322 compliant)
- Password validation (≥8 chars, ≥1 number, ≥1 symbol)
- Email unique constraint enforced
- Password hashed with bcrypt cost 12
- Returns 201 on success, 400 on validation error, 409 on email exists

**Verification command**:
```bash
curl -X POST http://localhost:3000/api/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"Pass1234!"}' \
  | jq -e '.success == true'
```

**Dependencies**: None (Task 001)

**Status**: not_started

---

## Task 002 — Login endpoint

**Behavior**: Endpoint `POST /api/login` accepte email + password, retourne JWT.

**Acceptance criteria**:
- 200 + JWT on valid credentials
- 401 on invalid
- 429 after 5 failed attempts in 15 min (rate limit)

**Verification command**:
```bash
curl -X POST .../api/login -d '...' | jq -e '.token != null'
```

**Dependencies**: Task 001

**Status**: not_started
```

### Les champs obligatoires

| Champ | Pourquoi |
|-------|----------|
| **Behavior** | Description en une phrase de ce que la tâche produit |
| **Acceptance criteria** | Liste explicite — pas de "make it work" |
| **Verification command** | Exécutable, observable — pas "tests should pass" |
| **Dependencies** | Quelles tâches doivent être passing avant |
| **Status** | not_started / active / blocked / passing |

Voir aussi [feature-state-machine](feature-state-machine.md) pour la machine d'état complète.

### Le critère "verification command exécutable"

Trop vague :
- "Login should work"
- "Validation should be strict"

Exécutable :
- `curl POST .../login | jq -e '.token != null'` → returns 0 ou non-zero
- `pytest tests/test_validation.py::test_password_strict` → pass/fail

Voir [completion-evidence-executable](completion-evidence-executable.md).

### Le critère "atomic"

Chaque tâche doit être **complétable en une session**. Si une tâche est trop large :

```
Task 001: Build authentication system
```

→ split :

```
Task 001a: User registration endpoint
Task 001b: Login endpoint with JWT
Task 001c: Token refresh endpoint
Task 001d: Password reset flow
```

Voir [atomic-task-decomposition](atomic-task-decomposition.md).

### Le critère "ordonné"

Les dépendances doivent former un **DAG** (Directed Acyclic Graph) :

```
Task 001 (registration)
        ↓
Task 002 (login) — depends on 001
        ↓
Task 003 (refresh) — depends on 002
```

Pas de cycle, pas d'ambiguïté sur l'ordre.

Voir [harness-pipeline-scheduler-verifier-handoff](harness-pipeline-scheduler-verifier-handoff.md).

### Le format JSON (machine-lisible)

Pour un usage maximal par la harness, dupliquer en `feature_list.json` :

```json
{
  "tasks": [
    {
      "id": "001",
      "behavior": "User registration endpoint",
      "verification": "curl -X POST ... | jq -e '.success'",
      "dependencies": [],
      "status": "not_started",
      "evidence": null
    },
    {
      "id": "002",
      "behavior": "Login endpoint",
      "verification": "...",
      "dependencies": ["001"],
      "status": "not_started",
      "evidence": null
    }
  ]
}
```

Voir [template-feature-list-json](template-feature-list-json.md).

L'agent peut alors :
- Lire le JSON pour savoir la prochaine tâche
- Update le `status` à `active` au démarrage
- Update à `passing` après vérification

### WIP limite

[WIP=1](wip-limit-discipline.md) : une seule tâche `active` à la fois. Le task breakdown contient des dizaines de tâches, mais une seule est en cours.

### Granularité — combien de tâches ?

| Taille du projet | Nombre de tâches breakdown |
|------------------|----------------------------|
| Petit (< 1 sem) | 5-10 |
| Moyen (1-4 sem) | 15-40 |
| Gros (1-3 mois) | 50-100 |
| Très gros | Découper en milestones, chaque milestone a son breakdown |

Si une tâche prend plus d'une session → split.
Si une tâche prend < 30 min → peut-être fusionner avec la suivante.

### Antipatterns

- ❌ Tâches sans verification command → on ne saura jamais si "done"
- ❌ Tâches sans status structuré → drift inévitable
- ❌ Tâches énormes ("build the frontend") → impossible à completer en 1 session
- ❌ Ordre non-spécifié → l'agent choisit, et choisit mal
- ❌ Mélange tâches + commentaires explicatifs longs → bruit

### Cas réel (Lecture 08)

> "45% higher feature completion rate than free-form tracking." — Lecture 08

Projets avec task breakdown structuré vs free-form ("juste une todo list") : +45% de features complètement terminées.

### Lien avec feature_list

`task-breakdown.md` (humain-lisible) et `feature_list.json` (machine-lisible) capturent la même info dans deux formats. Idéalement les deux sont synchronisés (script de génération de l'un vers l'autre).

Voir [feature-list-as-primitive](feature-list-as-primitive.md).

### À retenir

1. Format : **Behavior + Acceptance + Verification + Dependencies + Status**.
2. **Atomique** : 1 tâche = 1 session.
3. **Verification exécutable**, pas vague.
4. **DAG ordonné** des dépendances.
5. Dupliquer en **`feature_list.json`** pour usage machine.

## Related pages

- [feature-list-as-primitive](feature-list-as-primitive.md)
- [atomic-task-decomposition](atomic-task-decomposition.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [wip-limit-discipline](wip-limit-discipline.md)
- [template-feature-list-json](template-feature-list-json.md)
- [initialization-phase-separation](initialization-phase-separation.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
