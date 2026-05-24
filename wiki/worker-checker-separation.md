# Worker-checker separation

**Summary** : Le même modèle qui écrit du code ne doit pas valider son propre travail. Séparer le rôle "worker" (génère le code) du rôle "checker" (évalue) — même avec le même modèle Claude/Opus — réduit drastiquement le [[confidence-calibration-bias|biais d'auto-évaluation]].

**Sources** : `raw/ingested/lecture-09-preventing-agents-from-declaring-victory-too-early.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "Separate the person who does the work from the person who checks the work." — Anthropic

Pattern emprunté à l'ingénierie logicielle classique (code review). Pour les agents :

| Rôle | Tâche | Outils possibles |
|------|-------|------------------|
| **Worker / Generator** | Écrit le code | Edit, Write, Bash |
| **Checker / Evaluator** | Lit le code, run les tests, score | Read, Bash (lecture seule), grading rubric |

**Même modèle**, **rôles différents** → biais réduit.

### Pourquoi ça marche

Trois mécanismes :

#### 1. Pas de sunk cost

Le checker n'a pas écrit le code. Il n'a pas l'attachement émotionnel ("j'ai bossé là-dessus 2h, ça doit marcher"). Il évalue à froid.

#### 2. Mission différente

- Worker prompt : "fais cette tâche"
- Checker prompt : "trouve les défauts, sois nitpicky"

Le second prompt **incite** à chercher les manques, pas à confirmer.

#### 3. Pas le même contexte conversationnel

Le checker démarre fresh (ou avec un contexte minimal). Il ne porte pas les décisions implicites du worker. Il pose des questions que le worker oublierait.

### Le "nitpicky checker" prompt

```markdown
You are an evaluator. Your mission: find defects in the implementation provided.

Be nitpicky. For each issue:
- Severity (CRITICAL / HIGH / MEDIUM / LOW)
- Location (file:line)
- Issue description
- Suggested fix

Do not summarize positives. Focus only on issues.

Output: structured list of issues.
```

Comparer à un "review" classique qui dirait : "Code looks good, just some minor suggestions". Le nitpicky checker **trouve** systématiquement plus de problèmes parce qu'on lui en donne le mandat.

### Architecture concrète

#### Setup minimal

1 session Claude Code, mais avec un sub-agent dédié "evaluator" :

```yaml
# .claude/agents/evaluator.md
---
name: evaluator
description: Reviews completed feature implementations
tools: [Read, Grep, Glob, Bash]
model: sonnet
---

You are an evaluator. ...
```

Workflow :
1. Worker (agent principal) finit la tâche
2. Worker dispatch sub-agent `evaluator` avec contexte ciblé
3. Evaluator retourne une liste d'issues
4. Worker corrige ou justifie

Voir [[subagent-architecture]] et [[sub-agent-context-problem]] pour les bonnes pratiques de dispatch.

#### Setup multi-agent (Anthropic)

Voir [[planner-generator-evaluator-3-agent-architecture]] pour le full pattern à 3 rôles (planner + generator + evaluator).

### La rubric

L'evaluator utilise une grille structurée pour scorer. Voir [[template-evaluator-rubric]] :

| Dimension | Score 0-2 |
|-----------|-----------|
| Correctness | Le comportement match-t-il la feature ? |
| Verification | Y a-t-il une evidence exécutable ? |
| Scope discipline | L'agent est-il resté dans le scope ? |
| Reliability | Une nouvelle session peut-elle continuer ? |
| Maintainability | Le code est-il lisible, testé, documenté ? |
| Handoff readiness | La session suivante peut-elle reprendre ? |

Score total → verdict : **Accept / Revise / Block**.

### Cas réel Anthropic (Lecture 09)

| Setup | Auto-claim worker | Verdict checker | Réalité |
|-------|-------------------|-----------------|---------|
| 1 agent (self-eval) | "Done" | — | 20% vrai |
| 2 agents (worker + checker) | "Done" | "Issues found" | 80% checker correct |
| 3 agents (planner + gen + eval) | — | Final after iteration | 100% sur tâche DAW |

L'evaluator **détecte** systématiquement ce que le worker se cache à lui-même.

### Quand utiliser

| Situation | Worker-checker utile ? |
|-----------|------------------------|
| Tâche complexe (>2h) | **Oui** |
| Tâche critique (prod, sécurité) | **Oui** |
| Tâche de refactor | **Oui** (le checker voit ce qui a bougé) |
| Tâche triviale (renommer un var) | Non, overhead inutile |
| Bug fix avec test prévu | Marginal (le test sert de checker) |

### Anti-pattern : checker complaisant

Si le checker est mal prompté ("review this code"), il va dire "looks good" et c'est inutile. Le mandat doit être **nitpicky** ou structuré (rubric).

Test : si le checker dit "no issues" sur ~50%+ des reviews, le prompt est trop gentil.

### Anti-pattern : worker = checker

Tentation : un seul agent qui "code puis review". Ça ne marche pas — c'est exactement l'auto-évaluation que le pattern vise à éviter.

Pour avoir une séparation effective :

- **Soit** : sub-agent dédié (recommandé)
- **Soit** : 2 sessions séparées (manuelle)
- **Soit** : evaluator humain (toujours valide)

### Implémentation Claude Code

#### Option 1 : sub-agent dispatch

```
[worker context] → finish feature X → dispatch evaluator subagent → review →
[worker reads review] → fix issues → verify
```

#### Option 2 : hook Stop

À la fin de session, un hook Stop run un evaluator sub-agent automatiquement. Voir [[claude-code-hooks]].

#### Option 3 : /code-review command

Custom slash command qui dispatch un evaluator. Voir [[claude-code-commands]].

### Lien avec confidence calibration bias

Worker-checker separation est la **solution pratique** au [[confidence-calibration-bias|biais documenté de Guo 2017]]. C'est l'opérationnalisation du principe "ne jamais faire confiance à l'auto-évaluation".

### À retenir

1. **Worker ≠ Checker**, même si même modèle.
2. **Checker prompt = nitpicky**, mission = trouver des défauts.
3. **Rubric structurée** (6 dimensions, score 0-2).
4. Pattern utile sur tâches **complexes** ou **critiques**, overkill sur trivial.
5. Implémenter via **sub-agent dédié** ou **hook Stop**.

## Related pages

- [[confidence-calibration-bias]]
- [[planner-generator-evaluator-3-agent-architecture]]
- [[three-layer-termination-validation]]
- [[template-evaluator-rubric]]
- [[subagent-architecture]]
- [[sub-agent-context-problem]]
- [[the-harness-engineering-curriculum-summary]]
