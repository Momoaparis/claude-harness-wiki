# Confidence calibration bias

**Summary** : Guo et al. (2017) ont montré que les réseaux neuronaux modernes sont systématiquement overconfident — leur confiance auto-rapportée dépasse la précision réelle. Les agents LLMs héritent du biais. Conséquence : ne jamais utiliser la confiance subjective de l'agent comme signal de complétion.

**Sources** : `raw/ingested/lecture-09-preventing-agents-from-declaring-victory-too-early.md` (citant Guo et al. 2017)

**Last updated** : 2026-05-24

---

## Contenu

### Le résultat scientifique

**Guo et al. 2017** ("On Calibration of Modern Neural Networks") :

> "Modern neural networks are systematically overconfident."

Empirique : sur des tâches de classification, les modèles deep learning rapportent une confiance significativement supérieure à leur précision réelle. Le biais est **systématique** et augmente avec la complexité de la tâche.

### Application aux LLMs et agents

Le biais s'observe directement chez les agents codeurs :

- L'agent dit "this should work" avec haute confiance → seulement 60% des cas marchent vraiment
- L'agent dit "I'm done" → l'app crashe au démarrage dans X% des cas
- L'agent dit "all tests pass" → mais ses tests ne couvrent pas la nouvelle feature

L'écart entre **confiance perçue** et **précision réelle** explose dès qu'on monte en complexité.

### Pourquoi ce biais

Hypothèses (Guo et al. + interprétations du cours) :

1. **Loss function** : entraînement minimise la cross-entropy → encourage des distributions de probabilité piquées (confiance haute)
2. **Selection bias** : les exemples d'entraînement sont les "bonnes réponses", donc le modèle apprend qu'être confiant = répondre
3. **RLHF** : feedback humain récompense l'assertivité, pas l'incertitude calibrée
4. **Pas d'incentive à dire "je ne sais pas"** dans la majorité des prompts

### Conséquence : l'auto-évaluation n'est pas un signal

Demander à l'agent "tu es sûr que c'est fini ?" produit un signal **inutilisable** :

- "Yes I'm sure" → ne corrèle pas avec correctness réelle
- "I think so" → l'agent peut dire ça pour des trucs en fait corrects
- Aucune granularité fiable

> "Your harness must replace the agent's feelings with externalized, execution-based verification." — Lecture 09

### La solution : externaliser le jugement

Au lieu de demander à l'agent, **mesurer** :

| Approche | Source du jugement |
|----------|-------------------|
| ❌ "Agent, is it done?" | Agent (biaisé) |
| ✅ `make verify-feature-001` retourne 0 | Exécutable (objectif) |
| ✅ Evaluator agent indépendant avec rubric | Autre agent (séparation rôle) |
| ✅ E2E test passing | Système réel |

### Worker-checker separation

> "The solution is to separate the worker from the checker. Same model, but separation of roles." — Lecture 09

Pattern documenté : un agent **fait** le travail, un agent **vérifie**. Même modèle (Sonnet, Opus), mais **rôles différents** = biais réduit.

L'evaluator avec une rubric structurée :
- Cherche les manques (pas les confirmations)
- A pour mission de produire un score, pas de plaire
- Calibre mieux parce qu'il n'a pas écrit le code

Voir [worker-checker-separation](worker-checker-separation.md) et [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md).

### Données Anthropic (Lecture 09)

| Setup | Verdict de l'agent | Vérification externe | Concordance |
|-------|---------------------|----------------------|-------------|
| Single agent (self-eval) | "Done" | 20% vraiment fini | 20% |
| Generator + Evaluator | Generator: "Done" / Eval: "Issues found" | 80% concordance avec eval | 80% |
| Full 3-agent | Final verdict après itération | 100% sur la tâche DAW | 100% |

L'évaluateur indépendant **corrige** le biais du generator.

### Comment encoder dans la harness

#### 1. Banir l'auto-claim de complétion

Dans `CLAUDE.md` :

```markdown
## CRITICAL RULE

The agent NEVER marks a task as `passing`. Only the verifier does.
The agent's job is to produce code + signal "ready for verification".
```

#### 2. Pas de "I think it works" comme evidence

Bannir les formules du progress log :

❌ "Looks complete to me"
✅ "Verification command output: exit 0, tests 247/247"

#### 3. Evaluator rubric

Voir [template-evaluator-rubric](template-evaluator-rubric.md) : grille de scoring sur 6 dimensions, opérée par un agent ou humain **différent** du worker.

### Lien avec self-verification d'Opus 4.7

[Self-verification d'Opus 4.7](self-verification-mechanism.md) = l'agent relit son propre code et corrige. Ce n'est **pas** de l'auto-évaluation de complétion — c'est une boucle de raffinement interne. Le signal final "done" reste externalisé.

### Le cas particulier des LLMs récents

Les modèles 4.x sont **meilleurs calibrés** que les modèles 3.x (selon données internes Anthropic), mais le biais persiste. Surtout sur :

- Tâches en bout de session ([context anxiety](context-anxiety-modeles.md))
- Tâches complexes multi-étapes
- Tâches où l'agent a investi beaucoup d'effort (sunk cost)

Conclusion : pas de modèle qui peut s'auto-évaluer fiablement. Toujours externaliser.

### Auto-detection des cas à risque

Signaux que l'agent est probablement overconfident :

- Long monologue avant de déclarer "done"
- Phrases comme "should work", "looks good", "I'm pretty sure"
- Absence de mention de tests run
- Pas de log d'exécution dans le progress file

Ces signaux → re-vérifier externe systématiquement.

### À retenir

1. **Biais documenté** (Guo 2017) : NN overconfident.
2. Les agents LLM **héritent** du biais.
3. **L'auto-évaluation n'est pas une evidence.** Externaliser.
4. **Worker-checker separation** réduit le biais.
5. Toujours encoder la verif en commande exécutable, jamais "demander à l'agent".

## Related pages

- [worker-checker-separation](worker-checker-separation.md)
- [three-layer-termination-validation](three-layer-termination-validation.md)
- [completion-evidence-executable](completion-evidence-executable.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [self-verification-mechanism](self-verification-mechanism.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
