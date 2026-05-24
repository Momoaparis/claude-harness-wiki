# The Shorthand Guide to Everything Claude Code — Résumé

**Summary** : Résumé du guide shorthand d'Affaan Mustafa (sep 2025) sur la configuration de base de Claude Code — skills, hooks, subagents, MCPs, plugins, éditeurs.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-claude-code.md`

**Last updated** : 2026-05-23

---

## Contenu

### Métadonnées de la source

- **Auteur** : Affaan Mustafa (@affaanmustafa)
- **Publication** : 16 septembre 2025
- **URL** : https://x.com/affaanmustafa/status/2012378465664745795
- **Article frère** : [[the-longform-guide-summary]] — suite avancée (jan 2026), assume ce setup de base acquis

### Positionnement

Ce guide couvre la **configuration initiale** pour utiliser Claude Code efficacement : l'outillage de base avant d'aborder les techniques avancées du Longform Guide. Il documente le retour d'expérience après 10 mois d'usage quotidien.

### Les 7 thèmes du guide

1. **Skills & Commands** — workflows réutilisables via slash commands
2. **Hooks** — automations déclenchées par événements (voir [[claude-code-hooks]])
3. **Subagents** — délégation de tâches à portée limitée (voir [[subagent-architecture]])
4. **Rules & Memory** — CLAUDE.md et dossier `.rules/` pour les conventions permanentes
5. **MCPs** — connecteurs vers services externes (voir [[mcp-vs-cli-skills]])
6. **Plugins** — outils packagés installables via marketplace (voir [[claude-code-plugins]])
7. **Tips** — raccourcis, parallélisation, éditeurs (voir [[claude-code-keyboard-shortcuts]])

### Setup de référence de l'auteur

**Plugins installés** (4-5 actifs à la fois) :
- `ralph-wiggum` — loop automation
- `frontend-design` — UI/UX patterns
- `typescript-lsp` / `pyright-lsp` — intelligence LSP
- `hookify` — création de hooks conversationnellement
- `context7` — documentation en temps réel
- `mgrep@Mixedbread-Grep` — recherche sémantique (voir [[mgrep-vs-grep]])

**MCPs configurés** : 14 au total, ~5-6 actifs par projet — voir [[claude-code-plugins]] pour la gestion du context window.

**Hooks clés** :
- `PreToolUse` : reminder tmux pour commandes longues, blocage fichiers `.md` non essentiels
- `PostToolUse` : Prettier auto, tsc --noEmit, warning console.log
- `Stop` : audit console.log sur fichiers modifiés

**Éditeur préféré** : Zed (Rust, léger, agent panel, Ctrl+G pour ouvrir le fichier courant)

### Principes retenus

1. Ne pas sur-compliquer — traiter la configuration comme un fine-tuning, pas une architecture
2. Le context window est précieux — désactiver MCPs et plugins inutilisés
3. Exécution parallèle — `/fork` + git worktrees (voir [[git-worktrees-parallel-claude]])
4. Automatiser le répétitif — hooks pour formatting, linting, reminders
5. Scoper les subagents — outils limités = exécution focused

## Related pages

- [[the-longform-guide-summary]]
- [[claude-code-hooks]]
- [[claude-code-commands]]
- [[claude-code-plugins]]
- [[claude-code-keyboard-shortcuts]]
- [[subagent-architecture]]
- [[mcp-vs-cli-skills]]
- [[git-worktrees-parallel-claude]]
- [[mgrep-vs-grep]]
