# Les 5 modes d'échec des agents en production

**Summary** : Lecture 01 du curriculum identifie 5 modes d'échec récurrents qui transforment un modèle benchmark à 60% en agent réel à 40%. Tous sont des défauts de harness, pas de modèle.

**Sources** : `raw/ingested/lecture-01-strong-models-dont-mean-reliable-execution.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Le diagnostic en une ligne

> "Discoveries from previous sessions disappear; tasks exceeding 30 minutes show sharp failure rate increases." — Lecture 01

### Les 5 failure modes

#### 1. Specs vagues

L'agent reçoit "implémente la feature X" sans définition observable de "fait". Sans [[completion-evidence-executable|completion evidence]], il code jusqu'à ce que le code "ait l'air" complet, puis déclare victoire.

**Solution harness** : [[feature-list-as-primitive|feature lists structurées]] avec critères de vérification.

#### 2. Conventions implicites

Le projet a des conventions (formatage, naming, layering) que les humains connaissent mais qui ne sont écrites nulle part. L'agent invente ses propres conventions à chaque session.

**Solution harness** : `AGENTS.md` (voir [[template-claude-md]]) + [[repository-as-system-of-record|repo comme SSoT]].

#### 3. Environnement incomplet

Build cassé, deps non pinées, tests qui ne passent pas localement. L'agent passe la session à diagnostiquer l'environnement au lieu de coder.

**Solution harness** : [[initialization-phase-separation|phase d'initialisation dédiée]] qui produit un environnement runnable.

#### 4. Aucune méthode de vérification

Pas de tests E2E, pas de commande `make verify`, pas de critère objectif. L'agent ne peut pas savoir s'il a réussi, donc il triche en se basant sur son sentiment.

**Solution harness** : subsystème Feedback (voir [[five-subsystem-harness-architecture]]) + [[end-to-end-verification-only]].

#### 5. Perte de state multi-session

Chaque nouvelle session redémarre à zéro. Décisions oubliées, hypothèses re-faites, mêmes erreurs reproduites.

**Solution harness** : [[progress-file-pattern]] + [[decision-log-pattern]] + [[session-clean-handoff]].

### Pourquoi un meilleur modèle ne résout pas

Le piège classique : "Sonnet 4.5 a un problème → on attend Opus 5". Mais :

- Un meilleur modèle ne **récupère pas** un environnement cassé (Failure 3).
- Un meilleur modèle ne **devine pas** des conventions non écrites (Failure 2).
- Un meilleur modèle **ne se souvient pas** des décisions passées sans state persistant (Failure 5).

> "Discoveries from previous sessions disappear" — Lecture 01

Un modèle plus capable amplifie même les failure modes 1, 2, 5 : il fait *plus* de travail avant de découvrir que la spec était vague, donc le coût d'erreur est plus élevé.

### Le diagnostic loop

Pour chaque échec observé, attribuer à une couche :

```
Exécuter → Observer → Attribuer à une couche → Fixer la couche → Re-exécuter
```

Couches possibles : Instructions / Tools / Environment / State / Feedback (voir [[five-subsystem-harness-architecture]]).

### Cas réels cités

- **FastAPI team** : passage de prompt-only à `AGENTS.md` structuré → reproductibilité multi-session.
- **OpenAI million-line code experiment** (2025) : démontre que les repos agent-first surperforment les repos human-first sur les benchmarks agent.

### À retenir

1. Les 5 modes ne s'additionnent pas — ils **se multiplient**. Un projet qui en cumule 3 est dans un état proche d'inutilisable.
2. Failure 4 (vérification) est le plus subtil : l'agent semble réussir mais produit du code non-fonctionnel.
3. Failure 5 (state) devient critique dès qu'une tâche dépasse 30 minutes.
4. La harness se construit pour adresser **chaque mode**, dans l'ordre où ils bloquent.

## Related pages

- [[harness-definition-et-philosophie]]
- [[five-subsystem-harness-architecture]]
- [[feature-list-as-primitive]]
- [[initialization-phase-separation]]
- [[cross-session-context-loss]]
- [[the-harness-engineering-curriculum-summary]]
