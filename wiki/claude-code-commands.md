# Claude Code — Commandes utiles

**Summary** : Liste des commandes slash de Claude Code mentionnées dans la source — gestion des sessions, du contexte, des chats parallèles et de l'apprentissage.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Claude Code expose plusieurs commandes accessibles via `/<nom>` dans le chat. Cette page rassemble celles citées dans la source pour éviter de les répéter dans chaque page concept.

### `/rename <nom>`

Renomme le chat courant. Essentiel quand on fait tourner **plusieurs instances en parallèle** pour identifier chaque session d'un coup d'œil.

**Usage type** :

```
/rename feature-a-impl
/rename refactor-cleanup
/rename research-pricing
```

**Voir** : [[cascade-method]], [[git-worktrees-parallel-claude]], [[two-instance-kickoff]]

### `/fork`

Duplique un état de conversation pour partir explorer dans une direction sans polluer la session principale.

**Usage type** :
- Forker pour poser une question de recherche sans casser le contexte de coding
- Forker pour tester une approche alternative

**Voir** : [[two-instance-kickoff]]

### `/clear`

Réinitialise le contexte de la conversation. Recommandé entre les phases d'un orchestrateur séquentiel pour repartir sur une slate propre.

**Pattern recommandé** dans l'orchestration multi-phase :

```
Phase 1: Research → /clear → Phase 2: Plan → /clear → Phase 3: Implement
```

**Voir** : [[iterative-retrieval-pattern]], [[strategic-compact]]

### `/compact`

Déclenche manuellement un compactage du contexte (résumé de la conversation pour libérer de l'espace).

**Recommandation** : désactiver l'auto-compact et utiliser `/compact` **stratégiquement** :
- Après une phase d'exploration, avant l'exécution
- Après un milestone, avant le suivant

**Voir** : [[strategic-compact]]

### `/learn`

Extrait manuellement un pattern utile vers `~/.claude/skills/learned/` sans attendre la fin de session. Utile quand on vient de résoudre quelque chose de non-trivial.

**Workflow** :
1. Tu résous un problème délicat
2. Tu lances `/learn`
3. Claude propose un fichier skill draft
4. Tu confirmes avant sauvegarde

**Voir** : [[continuous-learning-skill]]

### `/rewind`

Retourner à un état antérieur de la conversation. Annule une série d'actions qui a mal tourné en restaurant un point précédent.

**Différence clé** : `/rewind` agit sur la conversation, `/checkpoints` agit sur les fichiers.

### `/statusline`

Personnaliser la barre de statut. Affichables : utilisateur, répertoire, branche git (+ dirty indicator), % context window restant, modèle, heure, todos.

**Voir** : [[claude-code-keyboard-shortcuts]]

### `/checkpoints`

Créer des points de restauration **au niveau fichier**, indépendamment de git. Permet de revenir à une version précise d'un fichier pour des expériences locales rapides.

**Différent de git** : ne pollue pas l'historique du dépôt.

---

### Vue d'ensemble — quand utiliser quoi

| Situation | Commande |
|-----------|----------|
| Nouvelle session parallèle | `/rename` |
| Explorer sans casser le contexte courant | `/fork` |
| Transition entre phases d'un workflow | `/clear` |
| Contexte gonflé, transition logique | `/compact` |
| Pattern non-trivial à capitaliser | `/learn` |
| Série d'actions à annuler | `/rewind` |
| Expérience fichier sans toucher git | `/checkpoints` |

### Combinaison classique

Le pattern courant dans une session productive :

```
/rename impl-feature-x
[... travail ...]
/compact         # libère contexte après exploration
[... implémentation ...]
/learn           # capitalise la solution trouvée
```

### À ne pas confondre

- `/compact` (manuel) ≠ auto-compact (déclenché par Claude Code à des points arbitraires)
- `/clear` (réinitialise) ≠ `/compact` (résume mais garde l'essentiel)
- `/fork` (duplique l'état) ≠ ouvrir un nouveau terminal (pas le même contexte)

## Related pages

- [[strategic-compact]]
- [[continuous-learning-skill]]
- [[cascade-method]]
- [[git-worktrees-parallel-claude]]
- [[two-instance-kickoff]]
- [[iterative-retrieval-pattern]]
- [[the-longform-guide-summary]]
