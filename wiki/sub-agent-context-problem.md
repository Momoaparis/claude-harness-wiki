# Sub-Agent Context Problem

**Summary** : Problème fondamental des sub-agents — ils n'ont accès qu'à la query littérale, pas au contexte sémantique et au "pourquoi" de la demande, ce qui produit des résumés incomplets.

**Sources** : The Longform Guide to Everything Claude Code.md (citant @PerceptualPeak)

**Last updated** : 2026-05-22

---

## Contenu

### Le constat

Les sub-agents existent pour **économiser le contexte** : ils retournent un résumé au lieu d'inonder l'orchestrateur de détails. Mais ce design crée un problème.

### L'analogie

> "Ton boss t'envoie à une réunion et te demande un résumé. Tu reviens avec le rundown. Neuf fois sur dix, il aura des questions de suivi. Ton résumé ne contiendra pas tout ce dont il a besoin parce que tu n'as pas le contexte implicite qu'il a."  
> — *@PerceptualPeak*

### Le problème en détail

| L'orchestrateur a... | Le sub-agent a... |
|---------------------|-------------------|
| Le **pourquoi** | Juste la **query** |
| Le contexte du projet | Pas ce contexte |
| Les contraintes implicites | Pas ces contraintes |
| L'historique de la session | Une fresh slate |

Résultat : le résumé du sub-agent **manque des détails que l'orchestrateur jugerait critiques**, parce que le sub-agent ne sait pas ce qui est critique.

### Symptômes

- L'orchestrateur reprend la conversation et veut re-dispatcher pour des détails
- Le résumé "manque le point"
- L'orchestrateur doit faire des hypothèses ou re-poser des questions

### Les solutions

Deux approches discutées dans le guide :

1. **[iterative-retrieval-pattern](iterative-retrieval-pattern.md)** : l'orchestrateur évalue chaque retour et peut renvoyer des follow-ups (max 3 cycles)
2. **Pass objective context** : ne pas envoyer juste la query mais aussi l'objectif global et les raisons de la demande

### Pattern d'envoi recommandé

```
Query: "Trouve les fichiers qui utilisent X"
+ Objective: "Je refactor X et je veux savoir l'impact"
+ Constraints: "Ignore les fichiers de test"
```

Plus le sub-agent comprend le **but**, mieux il filtre son résumé.

## Related pages

- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
- [subagent-architecture](subagent-architecture.md)
- [agent-abstraction-tierlist](agent-abstraction-tierlist.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
