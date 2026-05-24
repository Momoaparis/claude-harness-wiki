# Iterative Retrieval Pattern

**Summary** : Pattern où l'orchestrateur évalue le retour de chaque sub-agent et peut re-dispatcher des follow-up questions jusqu'à satisfaction (max 3 cycles).

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Vue d'ensemble

Le pattern résout le [[sub-agent-context-problem]] : au lieu d'accepter aveuglément le premier résumé du sub-agent, l'orchestrateur le challenge et fait du retrieval itératif.

### Le diagramme

```
┌─────────────────┐
│  ORCHESTRATOR   │
│  (has context)  │
└────────┬────────┘
         │ dispatch with query + objective
         ▼
┌─────────────────┐
│   SUB-AGENT     │
│ (lacks context) │
└────────┬────────┘
         │ returns summary
         ▼
┌─────────────────┐      ┌─────────────┐
│   EVALUATE      │─no──►│  FOLLOW-UP  │
│   Sufficient?   │      │  QUESTIONS  │
└────────┬────────┘      └──────┬──────┘
         │ yes                  │
         ▼                      │ sub-agent
    [ACCEPT]              fetches answers
                                │
         ◄──────────────────────┘
              (max 3 cycles)
```

### Les règles

1. **Dispatch avec query + objective** : voir [[sub-agent-context-problem]]
2. **Évaluer chaque retour** : le résumé répond-il à l'objectif ?
3. **Re-dispatcher si insuffisant** : avec follow-up précis
4. **Cap à 3 cycles** : pour éviter les boucles infinies

### Implémentation manuelle

En tant qu'utilisateur, on peut appliquer ce pattern soi-même :
- Lire le retour du sub-agent
- Si quelque chose manque, demander explicitement à l'orchestrateur de re-dispatch
- Préciser ce qui manquait dans le précédent retour

### Implémentation automatisée

Le pattern peut être codé dans un skill orchestrateur qui :
- Stocke l'objectif dans la conversation
- Évalue selon des critères pré-définis (longueur, mots-clés, structure)
- Re-dispatch si critères non remplis

### Lien avec orchestration séquentielle

L'iterative retrieval s'intègre dans le pattern d'**orchestrateur séquentiel** :

```
Phase 1: Research → Phase 2: Plan → Phase 3: Implement → Phase 4: Review → Phase 5: Verify
```

Chaque phase peut elle-même contenir une boucle d'iterative retrieval interne.

### Anti-pattern

Accepter le premier résumé sans le challenger. C'est la cause principale des "trous" dans les sorties de sub-agents.

## Related pages

- [[sub-agent-context-problem]]
- [[subagent-architecture]]
- [[agent-abstraction-tierlist]]
- [[the-longform-guide-summary]]
