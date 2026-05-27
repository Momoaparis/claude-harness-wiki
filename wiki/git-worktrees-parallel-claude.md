# Git Worktrees pour Claude en parallèle

**Summary** : Utilisation des git worktrees pour faire tourner plusieurs instances Claude Code en parallèle sans conflits de fichiers ni de branches.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Le problème

Plusieurs instances Claude qui éditent le même repo simultanément :
- Conflits de fichiers
- Working directories sales mélangés
- Difficile de savoir qui a fait quoi
- Difficile de comparer les sorties

### La solution : git worktrees

Un worktree git permet d'avoir **plusieurs branches checked out simultanément** dans des dossiers séparés, partageant le même `.git`.

### Setup

```bash
# Créer trois worktrees pour trois travaux parallèles
git worktree add ../project-feature-a feature-a
git worktree add ../project-feature-b feature-b
git worktree add ../project-refactor refactor-branch

# Une instance Claude par worktree
cd ../project-feature-a && claude
```

### Bénéfices

- **Pas de conflits git** entre instances
- **Working directory propre** par instance
- **Comparaison facile** des sorties (diff entre worktrees)
- **Benchmarking** : même tâche, approches différentes, comparaison du résultat

### Combine avec /rename

Pour ne pas se perdre, nommer chaque chat Claude :

```
/rename feature-a-impl
/rename feature-b-impl
/rename refactor-cleanup
```

### Lien avec le benchmarking

Pattern utilisé pour comparer modèles ou configurations :

```
[Task]
   │
   ├──► [Worktree A : Sonnet]
   ├──► [Worktree B : Opus]
   └──► [Worktree C : Haiku]
   
   ↓
[git diff + tests = benchmark]
```

Voir [subagent-architecture](subagent-architecture.md) pour le benchmarking méthodique.

### Précaution

Le multi-instance n'est utile que si les tâches sont **orthogonales** (peu de chevauchement). Sinon le coût de merge dépasse le gain.

## Related pages

- [cascade-method](cascade-method.md)
- [two-instance-kickoff](two-instance-kickoff.md)
- [subagent-architecture](subagent-architecture.md)
- [claude-code-commands](claude-code-commands.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
