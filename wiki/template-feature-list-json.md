# Template — feature_list.json

**Summary** : Format machine-lisible canonique de la feature list. Structure JSON avec id, behavior, verification, dependencies, state, evidence pour chaque tâche atomique. Lu par scheduler / verifier / handoff reporter. C'est la primitive du harness (voir [[feature-list-as-primitive]]).

**Sources** : `raw/ingested/lecture-08-use-feature-lists-to-constrain-what-the-agent-does.md`, projets P01-P06 du curriculum

**Last updated** : 2026-05-24

---

## Contenu

### Rôle

Voir [[feature-list-as-primitive]] pour la théorie. Cette page = le format concret à utiliser.

### Template verbatim (JSON)

À copier-coller dans `feature_list.json` à la racine du repo et adapter.

```json
{
  "schema_version": "1.0",
  "project": "[PROJECT_NAME]",
  "last_updated": "[YYYY-MM-DDTHH:MM:SSZ]",

  "tasks": [
    {
      "id": "001",
      "behavior": "[Single-sentence description of what this task produces]",
      "verification": "[Executable shell command that returns exit 0 on success]",
      "dependencies": [],
      "state": "not_started",
      "evidence": null,
      "transitions": [],
      "notes": ""
    },
    {
      "id": "002",
      "behavior": "[Description of task 002]",
      "verification": "[Verification command for 002]",
      "dependencies": ["001"],
      "state": "not_started",
      "evidence": null,
      "transitions": [],
      "notes": ""
    }
  ]
}
```

### Schema fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema_version` | string | yes | Version du schéma (ici "1.0") |
| `project` | string | yes | Nom du projet |
| `last_updated` | ISO 8601 timestamp | yes | Dernière modification du fichier |
| `tasks` | array | yes | Liste des tâches atomiques |
| `tasks[].id` | string | yes | Identifiant unique (ex: "001", "auth-001") |
| `tasks[].behavior` | string | yes | Single behavior description |
| `tasks[].verification` | string | yes | Commande exécutable (voir [[completion-evidence-executable]]) |
| `tasks[].dependencies` | array of ids | yes | Tâches qui doivent être `passing` avant |
| `tasks[].state` | enum | yes | `not_started` / `active` / `blocked` / `passing` |
| `tasks[].evidence` | string \| null | optional | Path vers log/commit prouvant la complétion |
| `tasks[].transitions` | array | optional | Historique des state changes |
| `tasks[].notes` | string | optional | Contexte additionnel (blockers, exceptions) |

### Les 4 états

Voir [[feature-state-machine]] :

```
not_started → active → passing (terminal)
                ↓
              blocked → active
```

- `not_started` : jamais touchée
- `active` : une session est en train (WIP=1 : une seule à la fois)
- `blocked` : empêchement externe documenté dans `notes`
- `passing` : verification command a retourné 0, **irréversible**

### Exemple concret

```json
{
  "schema_version": "1.0",
  "project": "myapp-auth",
  "last_updated": "2026-05-24T15:30:00Z",

  "tasks": [
    {
      "id": "001",
      "behavior": "POST /api/register endpoint accepts email+password, creates user, returns {success, userId}",
      "verification": "curl -X POST localhost:3000/api/register -H 'Content-Type: application/json' -d '{\"email\":\"test@example.com\",\"password\":\"Pass1234!\"}' | jq -e '.success == true'",
      "dependencies": [],
      "state": "passing",
      "evidence": "tests/logs/001_test_output_2026-05-22.log",
      "transitions": [
        {"from": "not_started", "to": "active", "at": "2026-05-22T09:00:00Z"},
        {"from": "active", "to": "passing", "at": "2026-05-22T11:30:00Z"}
      ],
      "notes": ""
    },
    {
      "id": "002",
      "behavior": "POST /api/login endpoint accepts email+password, returns JWT on valid creds",
      "verification": "bash scripts/verify-002-login.sh",
      "dependencies": ["001"],
      "state": "active",
      "evidence": null,
      "transitions": [
        {"from": "not_started", "to": "active", "at": "2026-05-24T14:00:00Z"}
      ],
      "notes": ""
    },
    {
      "id": "003",
      "behavior": "Password reset email sending",
      "verification": "bash scripts/verify-003-reset.sh",
      "dependencies": ["001"],
      "state": "blocked",
      "evidence": null,
      "transitions": [
        {"from": "not_started", "to": "active", "at": "2026-05-22T15:00:00Z"},
        {"from": "active", "to": "blocked", "at": "2026-05-22T16:00:00Z"}
      ],
      "notes": "Waiting for SMTP credentials from infra team (requested 2026-05-22)"
    }
  ]
}
```

### Scripts utiles

#### Calculer le VCR

```bash
TOTAL=$(jq '[.tasks[] | select(.state != "not_started")] | length' feature_list.json)
PASSING=$(jq '[.tasks[] | select(.state == "passing")] | length' feature_list.json)
echo "VCR: $(bc <<< "scale=2; $PASSING / $TOTAL")"
```

Voir [[verified-completion-rate-metric]].

#### Lister les next tasks

```bash
jq '[.tasks[] | select(.state == "not_started")] | .[0]' feature_list.json
```

Le scheduler peut être un simple script.

#### Vérifier WIP=1

```bash
ACTIVE=$(jq '[.tasks[] | select(.state == "active")] | length' feature_list.json)
if [ "$ACTIVE" -gt 1 ]; then
  echo "❌ WIP violation: $ACTIVE active tasks"; exit 1
fi
```

Voir [[wip-limit-discipline]].

### Update workflow

```bash
# Marquer une tâche active
jq '(.tasks[] | select(.id == "002") | .state) |= "active" |
    (.tasks[] | select(.id == "002") | .transitions) += [{"from": "not_started", "to": "active", "at": now | strftime("%Y-%m-%dT%H:%M:%SZ")}]' \
  feature_list.json > tmp.json && mv tmp.json feature_list.json
```

Plus simple : utiliser un script `harness-cli` dédié si le projet le justifie.

### Génération depuis Markdown

Pour les humains, c'est plus agréable d'écrire en markdown. Un script peut générer le JSON :

```bash
# scripts/gen-feature-list.sh
# Parse task-breakdown.md, output feature_list.json
```

Voir [[task-breakdown-structure]].

### Antipatterns

- ❌ `state` mis à jour manuellement à la main → drift garanti
- ❌ Pas de `verification` → impossible de transitionner vers `passing` proprement
- ❌ Dépendances cachées → blocages au runtime
- ❌ Modifier l'historique de `transitions` → perte de traçabilité
- ❌ Plus d'une tâche `active` simultanément → WIP=1 violé

### Versionning

Le fichier est committé. Les changements de state se voient en `git log`. C'est une fonctionnalité, pas un bug — on peut auditer l'évolution du projet via git.

### Intégration avec hooks

PostToolUse hook qui re-calcule VCR et bloque si > 0 active :

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "bash scripts/check-feature-list.sh",
        "description": "Verify feature_list.json consistency after each edit"
      }
    ]
  }
}
```

### À retenir

1. **Format JSON** strict, schema versionné.
2. **6 champs par task** : id, behavior, verification, dependencies, state, evidence.
3. **4 états** : not_started / active / blocked / passing.
4. **Transitions logged** pour traçabilité.
5. Scripts simples (jq) suffisent pour l'usage de base.

## Related pages

- [[feature-list-as-primitive]]
- [[feature-state-machine]]
- [[harness-pipeline-scheduler-verifier-handoff]]
- [[task-breakdown-structure]]
- [[wip-limit-discipline]]
- [[verified-completion-rate-metric]]
- [[the-harness-engineering-curriculum-summary]]
