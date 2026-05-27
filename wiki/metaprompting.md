# Metaprompting

**Summary** : Pratique consistant à investir du temps à construire un prompt précis et complet avant de lancer une tâche, pour améliorer la stabilité du résultat et tester les hypothèses sous-jacentes.

**Sources** : The Longform Guide to Everything Claude Code.md (citant @menhguin)

**Last updated** : 2026-05-22

---

## Contenu

### La citation fondatrice

> "I take 3 minutes to prompt a 20-minute task"  
> — *@menhguin*

L'idée : passer **3 minutes** à bien formuler un prompt qui fait économiser des dizaines de minutes de re-prompts, corrections, et résultats incorrects.

### Pourquoi c'est un "direct buff"

Le metaprompting figure dans le **Tier 1** de l'[agent-abstraction-tierlist](agent-abstraction-tierlist.md) — facile à adopter, gain immédiat, peu de risque.

Bénéfices mesurables :
- **Stabilité** : moins de variance dans les résultats
- **Sanity-check** : formuler le prompt force à clarifier ses propres hypothèses
- **Tokens économisés** : moins de re-prompts = moins de tokens gaspillés
- **Premier essai correct** : pass@1 amélioré (voir [pass-at-k-metric](pass-at-k-metric.md))

### Anatomie d'un bon prompt (metaprompting)

Un prompt bien construit explicite :

1. **L'objectif final** (le pourquoi)
2. **La tâche immédiate** (le quoi)
3. **Les contraintes** (ce qui est interdit ou imposé)
4. **Le format de sortie** (markdown, code, liste, etc.)
5. **Les exemples** (si le pattern est ambigu)
6. **Les pièges connus** (ce que les essais précédents ont raté)

### Anti-pattern

❌ Un prompt court et générique du type :  
> "fix the bug"

✅ Le même besoin en metaprompting :  
> "Le test `auth.test.ts:42` échoue depuis le commit `abc123`. Le test attend un code HTTP 401 sur token expiré. Implémente le check d'expiration dans `middleware/auth.ts`. Ne modifie pas le test. Vérifie que les autres tests d'auth passent toujours."

### Lien avec le sub-agent context problem

Le metaprompting résout en partie le [sub-agent-context-problem](sub-agent-context-problem.md) : en explicitant l'objectif et les contraintes dans le prompt initial, le sub-agent reçoit le contexte qu'il n'a pas implicitement.

C'est aussi un **prérequis** pour [iterative-retrieval-pattern](iterative-retrieval-pattern.md) — sans un bon prompt initial, l'orchestrateur ne peut pas évaluer si le retour du sub-agent est satisfaisant.

### Quand sur-investir dans le metaprompting

Plus la tâche est :
- **Longue** (4h vs 15 min)
- **Critique** (security, production)
- **Coûteuse en modèle** (Opus)

→ Plus l'investissement en metaprompting paie.

À l'inverse, pour des tâches répétitives et bien cadrées, un prompt court suffit (et un modèle Haiku, voir [model-selection-claude](model-selection-claude.md)).

### Pratiques associées

- **Plan Mode** : utilise un prompt initial structuré
- **Asking the user more at the beginning** : autre Tier 1 buff complémentaire
- **CLAUDE.md / system-prompt injection** : metaprompting "permanent" pour un projet (voir [dynamic-system-prompt-injection](dynamic-system-prompt-injection.md))

## Related pages

- [agent-abstraction-tierlist](agent-abstraction-tierlist.md)
- [sub-agent-context-problem](sub-agent-context-problem.md)
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
- [pass-at-k-metric](pass-at-k-metric.md)
- [dynamic-system-prompt-injection](dynamic-system-prompt-injection.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
