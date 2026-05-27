# Agent Abstraction Tierlist

**Summary** : Classement des techniques d'abstraction d'agents en deux tiers — Tier 1 (easy wins) et Tier 2 (high skill floor), pour guider l'ordre d'adoption.

**Sources** : The Longform Guide to Everything Claude Code.md (citant @menhguin)

**Last updated** : 2026-05-22

---

## Contenu

Tierlist pour décider quelles abstractions d'agents adopter en premier.

### Tier 1 — Direct Buffs (faciles à utiliser)

Gain net dès l'adoption, peu de risque.

#### Subagents
- Prévient le **context rot** et permet la spécialisation ad-hoc
- "Half as useful as multi-agent but MUCH less complexity"
- À adopter en premier

#### Metaprompting
- "I take 3 minutes to prompt a 20-minute task"
- Améliore la stabilité et sanity-check les hypothèses
- Direct buff sur la qualité

#### Asking the user more at the beginning
- Plus de questions au début = moins de re-prompts
- Bémol : il faut répondre aux questions du plan mode

### Tier 2 — High Skill Floor (durs à bien utiliser)

Gain potentiel mais nécessite expérience.

#### Long-running agents
- Il faut comprendre la *shape* d'une tâche 15 min vs 1.5h vs 4h
- Beaucoup de tweaking et trial-and-error
- Cycles d'apprentissage longs

#### Parallel multi-agent
- "Very high variance" — utile seulement sur tâches très complexes ou bien segmentées
- "If 2 tasks take 10 minutes and you spend an arbitrary amount of time prompting or god forbid, merging changes, it's counterproductive"

#### Role-based multi-agent
- "Les modèles évoluent trop vite pour des heuristiques hardcodées"
- Difficile à tester
- Utile si l'arbitrage est très haut, sinon over-engineering

#### Computer use agents
- Paradigme très récent
- Nécessite beaucoup de wrangling
- "You're getting models to do something they were not even meant to do a year ago"

### Le takeaway

**Commencer par Tier 1**. Ne graduer vers Tier 2 que :
1. Quand les bases sont maîtrisées
2. Et qu'il y a un besoin réel (pas par fascination technologique)

### Lien avec parallel work

La Tier 2 inclut le multi-agent parallèle — voir [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md) et [cascade-method](cascade-method.md) pour les patterns pratiques quand on s'y aventure.

## Related pages

- [subagent-architecture](subagent-architecture.md)
- [sub-agent-context-problem](sub-agent-context-problem.md)
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
