# Subagent Architecture

**Summary** : Stratégie d'optimisation des tokens consistant à déléguer chaque tâche au modèle Claude le moins cher capable de la traiter correctement.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Au lieu d'utiliser Sonnet ou Opus pour tout, on définit des sub-agents spécialisés assignés à des modèles différents selon la complexité de leur tâche.

### Principe

Chaque sub-agent a un rôle bien défini et utilise le modèle minimum suffisant. Cela peut être déterminé par :

1. **Trial and error** : tester et adapter au fil du temps
2. **Benchmarking systématique** : voir section dédiée

### Déclaration du modèle dans un sub-agent

Dans le frontmatter YAML du fichier `.md` de l'agent :

```yaml
---
name: quick-search
description: Fast file search
tools: Glob, Grep
model: haiku
---
```

### Benchmarking approach (avancé)

Méthodologie pour mesurer objectivement quel modèle suffit :

1. Créer un repo avec des goals/tasks bien définis et un plan
2. Pour chaque worktree git, assigner un seul modèle à tous les sub-agents
3. Logger les tâches au fur et à mesure
4. Utiliser chaque sub-agent au moins une fois
5. Une fois la passe complète, auditer via diffs et tests
6. Si tout passe partout : ajouter des edge cases ou augmenter la complexité

Résultat : benchmark numérique cases passés/échoués par modèle.

### Lien avec l'orchestration

L'orchestrateur (Sonnet ou Opus) dispatche aux sub-agents (Haiku pour repétitif, Sonnet pour standard, Opus pour critique). Voir [[iterative-retrieval-pattern]] et [[model-selection-claude]].

## Related pages

- [[model-selection-claude]]
- [[sub-agent-context-problem]]
- [[iterative-retrieval-pattern]]
- [[agent-abstraction-tierlist]]
- [[the-longform-guide-summary]]
