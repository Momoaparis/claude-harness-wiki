# Verified Completion Rate (VCR) — métrique

**Summary** : VCR = (nombre de tâches en état `passing` avec evidence vérifiable) / (nombre de tâches activées). Métrique continue de qualité de la harness. Si VCR < 1.0, bloquer les nouvelles activations.

**Sources** : `raw/ingested/lecture-07-draw-clear-task-boundaries-for-agents.md`

**Last updated** : 2026-05-24

---

## Contenu

### La formule

```
VCR = tasks_verified_passing / tasks_activated
```

| | Définition |
|---|------------|
| `tasks_activated` | Toutes les tâches qui ont été marquées `active` au moins une fois |
| `tasks_verified_passing` | Sous-ensemble qui a une evidence exécutable de complétude |

VCR = 1.0 → toutes les tâches démarrées ont été finies proprement.
VCR < 1.0 → on a démarré plus que ce qu'on a fini.

### Pourquoi cette métrique

C'est le **proxy mécanique** de la discipline d'agent :

- Code lines / day → mesure le **volume** (mauvais proxy)
- Features completed → mesure les **résultats**, mais binaire et tardif
- **VCR** → mesure la **discipline en continu**, à chaque session

### Cas réel (Lecture 07)

Sur un projet 8-features API :

| Session | Tasks activated | Tasks passing | VCR |
|---------|----------------|---------------|-----|
| 1 (WIP=5) | 5 | 1 | 0.20 |
| 2 (WIP=5) | 5 | 1 | 0.20 |
| 3 (WIP=1) | 1 | 1 | **1.00** |

Quand VCR reste < 0.5 sur plusieurs sessions → signal fort que la harness est cassée.

### Bloquer les nouvelles activations

Règle : **si VCR < 1.0 (il existe des tâches non-finies)**, bloquer toute transition `not_started → active` jusqu'à ce que toutes les `active` deviennent `passing` ou `blocked`.

Concrètement, dans la harness :

```json
{
  "rules": {
    "block_new_activation_if_vcr_below": 1.0
  }
}
```

Le scheduler refuse de proposer une nouvelle tâche tant qu'il y en a une en cours.

### Implémentation

#### Côté `feature_list.json`

```json
{
  "tasks": [
    {"id": "001", "status": "passing", "evidence": "test_001.log"},
    {"id": "002", "status": "active", "evidence": null},
    {"id": "003", "status": "not_started"}
  ]
}
```

Calcul VCR :

```bash
TOTAL=$(jq '[.tasks[] | select(.status != "not_started")] | length' feature_list.json)
PASSING=$(jq '[.tasks[] | select(.status == "passing")] | length' feature_list.json)
VCR=$(bc <<< "scale=2; $PASSING / $TOTAL")
echo "VCR: $VCR"
```

#### Côté CI

Bloquer le merge si VCR < 1.0 :

```bash
if [ "$(./scripts/vcr.sh)" != "1.00" ]; then
  echo "❌ VCR < 1.0 — there are tasks active but not verified"
  exit 1
fi
```

### Lien avec evidence executable

VCR n'a de valeur que si la transition `active → passing` est **gardée par une evidence executable** (voir [[completion-evidence-executable]]). Sinon l'agent peut auto-marquer `passing` et VCR=1.0 est faux.

### Tracking dans le temps

Logger VCR à chaque fin de session :

```
2026-05-22: VCR=1.00 (3/3 tasks passing)
2026-05-23: VCR=0.66 (2/3 — task 004 still active)
2026-05-24: VCR=1.00 (4/4)
```

Trends :
- VCR stable à 1.0 → discipline saine
- VCR oscille → certaines sessions overreach
- VCR < 0.7 sur la moyenne → harness ne contraint pas assez

### Lien avec verified completion vs "done"

| Notion | Sens |
|--------|------|
| "Done" subjectif | L'agent pense que c'est fini |
| `status: passing` | Le système a une evidence exécutable |
| VCR | Le taux de tâches qui ont vraiment atteint `passing` |

VCR rend visible l'écart entre "ce que l'agent pense fini" et "ce qui est réellement vérifié".

### Antipatterns détectés par VCR

#### Le "marathonien"

Agent active 5 tâches, finit la première, déclare les 4 autres "presque finies" → VCR=0.20.

Solution : WIP=1 strict + evidence gate.

#### Le "menteur statistique"

Tâches marquées `passing` sans evidence (evidence: null). VCR semble 1.0 mais c'est du vent.

Solution : refuser de calculer VCR si `evidence` est null, et logger l'incident.

#### Le "stagnant"

VCR reste à 0.0 longtemps → personne ne ferme rien. Probablement parce que les tâches sont trop grosses ([[atomic-task-decomposition]] manquant).

### Quel VCR cible ?

- **VCR cible** : 1.0 strict, en fin de session
- **VCR moyen acceptable** : > 0.85 sur les 10 dernières sessions
- **VCR alarme** : < 0.5 → revoir la harness

### À retenir

1. **VCR = tasks_passing / tasks_activated.**
2. Bloquer les nouvelles activations si VCR < 1.0.
3. `passing` doit être gardé par **evidence executable**, pas auto-claim.
4. Logger VCR par session pour voir les trends.
5. VCR < 0.5 prolongé = signal pour revoir le harness.

## Related pages

- [[wip-limit-discipline]]
- [[completion-evidence-executable]]
- [[atomic-task-decomposition]]
- [[feature-state-machine]]
- [[feature-list-as-primitive]]
- [[the-harness-engineering-curriculum-summary]]
