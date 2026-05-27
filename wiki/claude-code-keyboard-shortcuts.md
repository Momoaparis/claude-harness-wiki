# Claude Code — Raccourcis clavier et interface

**Summary** : Référence des raccourcis clavier, préfixes de commande et commandes de navigation de Claude Code. Inclut aussi les commandes utilitaires souvent méconnues.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-claude-code.md`

**Last updated** : 2026-05-23

---

## Contenu

### Raccourcis clavier

| Raccourci | Action |
|-----------|--------|
| `Ctrl+U` | Supprimer toute la ligne de saisie (plus rapide que backspace répété) |
| `Shift+Enter` | Saut de ligne dans la saisie (multi-line input) |
| `Tab` | Afficher/masquer le raisonnement interne (thinking display) |
| `Esc Esc` | Interrompre Claude / restaurer le code à l'état précédent |
| `Alt+T` (macOS : `Option+T`) | Activer/désactiver le extended thinking |
| `Ctrl+O` | Mode verbose — affiche le thinking dans le terminal |

### Préfixes dans la saisie

| Préfixe | Effet |
|---------|-------|
| `!` | Exécuter une commande bash directement (ex : `! git status`) |
| `@` | Rechercher et référencer un fichier dans la conversation |
| `/` | Lancer une slash command (skill ou commande built-in) |

### Commandes utilitaires

Ces commandes complètent celles documentées dans [claude-code-commands](claude-code-commands.md) :

#### `/rewind`

Retourner à un état précédent de la conversation. Utile quand une série d'actions a mal tourné et qu'on veut repartir d'un point antérieur propre.

#### `/statusline`

Personnaliser la barre de statut de Claude Code. On peut y afficher :
- l'utilisateur
- le répertoire courant
- la branche git + indicateur de dirty state
- le pourcentage de context window restant
- le modèle actif
- l'heure
- le nombre de todos

```
# Exemple statusline avec ces infos
user@/projet (main*) [78% ctx] [sonnet] 14:32 [3 todos]
```

#### `/checkpoints`

Créer des points de restauration au niveau fichier. Permet de revenir à une version précise d'un fichier sans passer par git.

- Différent de `/rewind` (qui restaure la conversation)
- Différent de `git` (qui gère le dépôt)
- Utile pour des expériences locales rapides sans polluer l'historique git

### Intégration éditeurs

#### Zed (recommandé par l'auteur du guide)

- `Ctrl+G` — ouvre dans Zed le fichier sur lequel Claude travaille actuellement
- `CMD+Shift+R` — palette de commandes (accès aux slash commands, debuggers, outils)
- Agent Panel — tracking des modifications fichier en temps réel
- Following mode — suivi visuel des éditions de Claude

**Pourquoi Zed** : écrit en Rust, léger, n'entre pas en compétition avec Claude pour les ressources système lors des opérations lourdes.

#### VSCode / Cursor

- Extension `/ide` — active la synchronisation avec l'éditeur + LSP (partiellement redondant avec les LSP plugins)
- Extension dédiée Claude Code disponible avec UI intégrée

### Parallélisation rapide

```bash
# Fork de conversation sans quitter le contexte courant
/fork

# Instances parallèles avec git worktrees
git worktree add ../feature-branch feature-branch
# Lancer une instance Claude Code distincte dans chaque worktree
```

**Voir** : [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md), [cascade-method](cascade-method.md)

### GitHub Actions — review automatique de PR

Claude peut être configuré pour reviewer automatiquement les PRs via GitHub Actions. Il approuve ou commente les PRs selon les règles définies.

Configuration dans `.github/workflows/` — non détaillée dans la source.

### Sandboxing

Mode restreint pour les opérations risquées — Claude tourne dans un environnement isolé sans toucher le système réel.

Le flag `--dangerously-skip-permissions` fait l'opposé : supprime toutes les restrictions. Usage réservé aux contextes de confiance totale.

## Related pages

- [claude-code-commands](claude-code-commands.md)
- [claude-code-hooks](claude-code-hooks.md)
- [claude-code-plugins](claude-code-plugins.md)
- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md)
- [cascade-method](cascade-method.md)
- [the-shorthand-guide-summary](the-shorthand-guide-summary.md)
