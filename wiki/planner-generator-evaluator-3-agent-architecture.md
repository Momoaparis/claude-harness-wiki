# Architecture 3-agents : Planner + Generator + Evaluator

**Summary** : Pattern documenté par Anthropic (mars 2026) et validé par Project 05 du curriculum. Trois rôles séparés — Planner (spec), Generator (implémentation), Evaluator (vérification) — produisent un score 4.9/5 vs 1.6/5 pour un agent seul. La séparation des rôles **mesurablement** réduit le biais et augmente la qualité.

**Sources** : `raw/ingested/lecture-09-preventing-agents-from-declaring-victory-too-early.md`, `raw/ingested/lecture-11-making-the-agents-runtime-observable.md`, `raw/ingested/project-05-grounded-qa-verification.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Les 3 rôles

```
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│     Planner      │───────►│    Generator     │───────►│    Evaluator     │
│                  │        │                  │        │                  │
│  Output: sprint  │        │  Output: code    │        │  Output: rubric  │
│  contracts +     │        │  + tests +       │        │  scoring +       │
│  feature list    │        │  artefacts       │        │  issues list     │
└──────────────────┘        └──────────────────┘        └──────────────────┘
        │                            │                            │
        └────────────────────────────┴────────────────────────────┘
                            Iteration loop
                  (Evaluator → back to Generator)
```

### Planner

**Mission** : transformer un besoin haut-niveau en plan exécutable.

**Outputs** :
- Feature list ([feature-list-as-primitive](feature-list-as-primitive.md)) avec atomic tasks
- Sprint contracts ([sprint-contract-pattern](sprint-contract-pattern.md)) pour chaque feature
- Decision log entries pour les choix d'architecture
- Estimation : sessions / coûts

**Prompt type** :
```
You are a planner. Read the high-level goal and produce:
1. A feature_list.json with atomic tasks (each completable in 1 session)
2. A sprint contract per atomic task (scope, verification, exclusions)
3. Decision log entries for architectural choices
4. NO code. NO implementation. Just structure.
```

**Modèle recommandé** : Opus (raisonnement long) ou Sonnet+thinking étendu.

### Generator

**Mission** : implémenter les features une par une, en respectant les sprint contracts.

**Outputs** :
- Code dans le repo
- Tests (unit + integration)
- Mise à jour de `feature_list.json` (state transitions)
- Mise à jour de `progress-file.md`

**Prompt type** :
```
You are a generator. For sprint contract X:
1. Read the scope, verification, exclusions
2. Implement strictly within scope
3. Write tests covering verification items
4. Run tests, ensure they pass
5. Update feature_list.json state to "active" then "passing"
6. NO over-engineering. NO scope creep.
```

**Modèle recommandé** : Sonnet (équilibre vitesse/qualité) ou Haiku pour les tâches simples.

### Evaluator

**Mission** : vérifier que le travail du generator passe les 3 couches de validation (voir [three-layer-termination-validation](three-layer-termination-validation.md)).

**Outputs** :
- Rubric scoring 6 dimensions (voir [template-evaluator-rubric](template-evaluator-rubric.md))
- Liste d'issues si défauts trouvés
- Verdict : Accept / Revise / Block
- Recommandation pour generator si Revise

**Prompt type** :
```
You are an evaluator. The generator claims feature X is done.
1. Run all verification commands from sprint contract X
2. Score on 6 dimensions (correctness, verification, scope, reliability, maintainability, handoff)
3. List ALL issues found, no matter how small
4. Verdict: Accept / Revise / Block
5. If Revise, provide actionable steps for generator
```

**Modèle recommandé** : Opus (rigueur > vitesse) ou Sonnet. **Pas le même que generator** (séparation).

### Données empiriques

#### Project 05 (curriculum)

Feature constante : multi-turn Q&A conversation history. Trois variants mesurées :

| Setup | Score (sur 5) |
|-------|---------------|
| Single role (agent seul) | **1.6** |
| Gen + Eval (2 rôles) | **3.3** |
| Plan + Gen + Eval (3 rôles) | **4.9** |

**3x amélioration** entre single-role et full architecture.

#### Anthropic DAW (mars 2026)

| Setup | Runtime | Coût | Working features |
|-------|---------|------|-------------------|
| Single agent | 20 min | $9 | **Non** |
| 3-agent + harness | 3h 50 | $124.70 | **Oui (full DAW)** |

Le multi-agent coûte ~14x plus, mais c'est la **différence entre 0 et 1** sur "marche / marche pas".

### Pourquoi ça marche

#### 1. Pas de sunk cost

L'evaluator n'a pas écrit le code → pas d'attachement. Détecte les défauts froidement.

#### 2. Missions claires

- Planner = pense
- Generator = fait
- Evaluator = critique

Chaque agent a **un seul** objectif d'optimisation. Pas de multi-objectif (voir [initialization-phase-separation](initialization-phase-separation.md) pour le principe).

#### 3. Calibration mutuelle

Si planner produit des sprint contracts vagues → evaluator score bas → feedback → planner s'améliore.

Si generator over-engineer → evaluator détecte les violations d'exclusions → generator apprend.

### Implémentation pratique

#### Setup minimal (1 dev, Claude Code)

3 sub-agents distincts :

```yaml
# .claude/agents/planner.md
---
name: planner
description: Generates feature lists, sprint contracts, decision logs
tools: [Read, Write, Glob]
model: opus
---

# .claude/agents/generator.md
---
name: generator
description: Implements features per sprint contract
tools: [Read, Write, Edit, Bash]
model: sonnet
---

# .claude/agents/evaluator.md
---
name: evaluator
description: Verifies completed features per sprint contract
tools: [Read, Bash]
model: opus
---
```

Workflow : dispatch planner → dispatch generator → dispatch evaluator → si Revise, retour generator.

Voir [subagent-architecture](subagent-architecture.md) et [sub-agent-context-problem](sub-agent-context-problem.md) pour les bonnes pratiques de dispatch.

#### Setup orchestrateur (avancé)

Un script ou tool qui orchestre :

```python
def harness_pipeline(goal):
    plan = dispatch("planner", goal)
    for task in plan.tasks:
        for attempt in range(3):
            code = dispatch("generator", task)
            eval = dispatch("evaluator", code, task.sprint_contract)
            if eval.verdict == "Accept":
                break
            task.feedback = eval.issues
        if eval.verdict != "Accept":
            mark_blocked(task)
```

Anthropic a built des frameworks internes pour ça. Pour solo dev, scripting suffisant.

### Itération loop

```
Generator finit task
    ↓
Evaluator score
    ↓
Score < threshold ? → feedback to Generator
    ↓                          ↓
Score ≥ threshold        Re-implement
    ↓                          ↓
Mark passing            (back to top)
```

Max 3 itérations typique. Si pas de convergence après 3 → tâche flagged pour review humain.

### Coût

Multi-agent coûte plus en tokens (3 modèles à invoquer) et en temps (séquentiel). Mais :

- Le **coût total** est souvent < le coût de débugger un mono-agent qui sort du fonctionnel partiel
- Sur les tâches **critiques**, le ROI est massif (0→1)
- Sur les tâches **triviales**, mono-agent suffit

Règle empirique : utiliser 3-agent pour tâche >2h ou critique. Mono-agent pour tâche <30 min.

### Lien avec worker-checker separation

Cette architecture est l'opérationnalisation à 3 niveaux du [worker-checker-separation](worker-checker-separation.md). Le planner ajoute une **3ème séparation** : celui qui planifie n'est pas non plus celui qui code, donc la spec n'est pas biaisée par l'écriture.

### Antipatterns

- ❌ Même agent qui plan + code + eval → biais maximal
- ❌ Evaluator complaisant ("looks good") → bénéfice nul
- ❌ Pas de boucle d'itération → le pattern devient one-shot pipeline (perd la valeur)
- ❌ Planner produit du code → outrepasse son rôle
- ❌ Generator évalue son propre travail → on perd la séparation

### À retenir

1. **3 rôles** : Planner / Generator / Evaluator.
2. Données : Single 1.6/5 → Gen+Eval 3.3/5 → Full 4.9/5.
3. Modèles : Opus pour Planner/Evaluator, Sonnet pour Generator.
4. **Itération** Gen ↔ Eval, max 3 cycles.
5. ROI sur tâches **complexes** ou **critiques**, overkill sur trivial.

## Related pages

- [worker-checker-separation](worker-checker-separation.md)
- [sprint-contract-pattern](sprint-contract-pattern.md)
- [observability-runtime-vs-process](observability-runtime-vs-process.md)
- [template-evaluator-rubric](template-evaluator-rubric.md)
- [subagent-architecture](subagent-architecture.md)
- [sub-agent-context-problem](sub-agent-context-problem.md)
- [harness-curriculum-projects-overview](harness-curriculum-projects-overview.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
