# Two-Instance Kickoff Pattern

**Summary** : Pattern de démarrage d'un nouveau projet avec deux instances Claude Code en parallèle — l'une pour le scaffolding, l'autre pour la recherche approfondie.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Le pattern

À l'amorce d'un repo vide, ouvrir **deux instances Claude** ayant des rôles distincts.

### Instance 1 : Scaffolding Agent (terminal gauche)

Met en place la structure et les conventions.

**Responsabilités** :
- Créer l'arborescence du projet
- Setup les configs (`CLAUDE.md`, rules, agents)
- Établir les conventions de code, naming, commits
- Poser le squelette

### Instance 2 : Deep Research Agent (terminal droit)

Compile la connaissance externe nécessaire.

**Responsabilités** :
- Connecté aux services et au web search
- Crée le PRD détaillé
- Produit les diagrammes mermaid d'architecture
- Compile les références avec extraits de la documentation officielle

### Disposition recommandée

```
┌──────────────────────────┬──────────────────────────┐
│   Terminal gauche        │   Terminal droit         │
│                          │                          │
│   Scaffolding            │   Research               │
│   - Project structure    │   - PRD                  │
│   - Configs              │   - Architecture diagrams│
│   - Conventions          │   - Docs extracts        │
│                          │                          │
│   Use /fork, /rename     │   Use /fork, /rename     │
└──────────────────────────┴──────────────────────────┘
```

### Pourquoi deux ?

- Scaffolding et research demandent des **mindsets différents**
- Si Claude fait les deux dans la même session, le contexte se pollue
- En parallèle, chacun peut nourrir l'autre (research → scaffolding ajuste sa structure)

### Quand passer en mode single instance

Une fois le kickoff fait, retourner à une seule instance pour le développement courant. Le pattern est spécifique à la **phase de démarrage**.

### Anti-pattern

Forcer ce pattern sur un projet déjà existant — il est conçu pour la phase fondatrice.

### Lien avec les commandes

- `/fork` pour dupliquer un état de conversation
- `/rename` pour identifier chaque instance

## Related pages

- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md)
- [cascade-method](cascade-method.md)
- [llms-txt-pattern](llms-txt-pattern.md)
- [claude-code-commands](claude-code-commands.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
