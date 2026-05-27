# mgrep vs grep

**Summary** : `mgrep` est une alternative à `grep`/`ripgrep` (utilisé par défaut par Claude Code) qui réduit la consommation de tokens d'environ 50% sur les tâches de recherche.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Le problème

Claude Code utilise `grep`/`ripgrep` par défaut pour la recherche dans les fichiers. Ces outils produisent des sorties qui peuvent contenir beaucoup de contexte non-pertinent — chaque ligne match consomme des tokens d'input lors du retour de l'outil à Claude.

### La solution : mgrep

`mgrep` est un outil de recherche optimisé pour les LLMs développé par Mixedbread AI. Il réduit la sortie à ce qui est sémantiquement pertinent.

**Repo** : https://github.com/mixedbread-ai/mgrep

### Gain mesuré

- **Réduction tokens** : ~50% en moyenne sur diverses tâches
- Particulièrement impactant sur les codebases larges

### Pourquoi c'est important

Les coûts d'input dominent souvent les coûts d'output. Sur Opus à $5/M input tokens, économiser 50% sur les recherches accumulées sur une session représente une économie réelle.

### Comment l'intégrer

L'idée générale : identifier les outils les plus fréquemment appelés par Claude et chercher des alternatives plus économes en tokens. `mgrep` remplace `grep` pour la recherche textuelle.

### Pattern général

Cette optimisation s'inscrit dans une stratégie plus large d'**audit des outils fréquents** :
- Identifier les commandes que Claude appelle le plus
- Chercher des alternatives optimisées LLM
- Wrapper si besoin dans des skills ou commandes

## Related pages

- [modular-codebase-tokens](modular-codebase-tokens.md)
- [background-processes-tmux](background-processes-tmux.md)
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
