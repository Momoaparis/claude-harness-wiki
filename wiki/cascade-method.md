# Cascade Method

**Summary** : Pattern d'organisation des tabs de terminal quand on fait tourner plusieurs instances Claude Code en parallèle — flux gauche à droite, du plus ancien au plus récent.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Le principe

Quand plusieurs instances Claude tournent en parallèle, l'overhead mental peut tuer le gain de productivité. Le **cascade method** est une discipline d'organisation visuelle.

### Les règles

1. **Nouvelles tâches → tab à droite** : on ajoute toujours à droite
2. **Sweep gauche à droite** : on traite les tâches du plus ancien au plus récent
3. **Direction constante** : pas de retour arrière non nécessaire
4. **Check spécifiques au besoin** : on ne re-scan pas tout en boucle
5. **Limite 3-4 tâches simultanées** : au-delà, l'overhead mental grandit plus vite que la productivité

### Pourquoi

Le cerveau humain a une capacité limitée à suivre plusieurs threads d'exécution. Un flux directionnel constant réduit la charge cognitive.

### Combiné avec /rename

Chaque tab doit avoir un nom explicite via `/rename` pour pouvoir retrouver le contexte d'un coup d'œil sans lire l'historique.

### Anti-pattern

❌ Ouvrir 5+ instances "au cas où"  
❌ Sauter d'un tab à l'autre dans l'ordre aléatoire  
❌ Ne pas nommer les tabs

### Recommandation finale

L'auteur insiste : **commencer par une seule instance** et n'ajouter des instances que par nécessité réelle. Le but n'est pas le nombre de parallèles mais "combien tu peux faire avec le minimum viable de parallélisation".

### Lien avec git worktrees

Le cascade fonctionne mieux avec [[git-worktrees-parallel-claude]] : chaque tab Claude vit dans son propre worktree, ce qui rend les changements isolés et la cascade vraiment unidirectionnelle.

## Related pages

- [[git-worktrees-parallel-claude]]
- [[two-instance-kickoff]]
- [[claude-code-commands]]
- [[the-longform-guide-summary]]
