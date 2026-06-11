# Subagent-Driven Development

**Summary** : Pattern d'exécution de Superpowers où chaque tâche est confiée à un sous-agent frais, dont le travail passe une revue en deux étapes (conformité au spec, puis qualité du code).

**Sources** : obra-superpowers-readme.md

**Last updated** : 2026-06-11

---

## Contenu

Le *subagent-driven-development* est le moteur d'exécution du [pipeline Superpowers](superpowers-workflow-pipeline.md). Une fois le plan approuvé et l'utilisateur ayant dit « go », l'orchestrateur ne code pas lui-même : il **dispatche un sous-agent frais pour chaque tâche** du plan, inspecte et revoit son travail, puis avance à la tâche suivante (source: obra-superpowers-readme.md).

### Pourquoi un sous-agent frais par tâche

Chaque tâche du plan ([writing-plans](superpowers-workflow-pipeline.md)) est auto-suffisante : chemins de fichiers exacts, code complet, étapes de vérification. Un sous-agent frais n'hérite donc pas du contexte encombré de l'orchestrateur — il reçoit un brief net et exécute. Cela limite le [problème de contexte des sous-agents](sub-agent-context-problem.md) : le contexte implicite manquant est compensé par un plan explicite.

### La revue en deux étapes

Le travail de chaque sous-agent passe deux contrôles séquentiels :

1. **Conformité au spec** — le code fait-il ce que la tâche demandait ?
2. **Qualité du code** — le code est-il propre, idiomatique, maintenable ?

Cette séparation des préoccupations recoupe directement deux concepts du wiki :

- [worker-checker-separation](worker-checker-separation.md) — même modèle, rôles séparés, biais réduit.
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md) — l'évaluateur distinct du générateur fait passer un projet de 1,6/5 à 4,9/5.

### Comparaison avec executing-plans

Superpowers propose deux moteurs d'exécution interchangeables à l'étape 4 du pipeline :

| | subagent-driven-development | executing-plans |
|---|---|---|
| **Unité** | un sous-agent frais par tâche | exécution par lots |
| **Contrôle humain** | revue automatique 2 étapes entre tâches | checkpoints humains entre lots |
| **Profil** | itération rapide, autonomie longue | supervision plus rapprochée |

### Lien avec l'orchestration générale

Ce pattern est une application disciplinée de l'[architecture par sous-agents](subagent-architecture.md) (déléguer au bon agent) et de la [boucle de récupération itérative](iterative-retrieval-pattern.md) (orchestrateur ↔ sous-agent). La nouveauté apportée par Superpowers est la **revue à deux étages systématique** entre chaque tâche.

## Related pages

- [superpowers-workflow-pipeline](superpowers-workflow-pipeline.md)
- [superpowers-framework-summary](superpowers-framework-summary.md)
- [subagent-architecture](subagent-architecture.md)
- [worker-checker-separation](worker-checker-separation.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [sub-agent-context-problem](sub-agent-context-problem.md)
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
