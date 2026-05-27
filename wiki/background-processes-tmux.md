# Background Processes via tmux

**Summary** : Offloader les processus longs en arrière-plan via tmux pour éviter que Claude ne consomme des tokens en streamant tout l'output.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Le problème

Quand Claude lance un processus long (build, test suite, deployment), tout l'output streamé en live entre dans son contexte. Pour Opus à $5/M input tokens, un build verbeux peut consommer beaucoup.

### La solution

Faire tourner le processus dans un autre terminal (tmux), puis nourrir à Claude **uniquement** :
- Un résumé de la sortie
- Ou la partie spécifique qui pose problème

### Workflow type

```bash
# Dans tmux, terminal séparé
tmux new -s build
npm run build 2>&1 | tee build.log

# Une fois fini, dans Claude
"Voici les erreurs du build (extrait de build.log) : ..."
```

### Pourquoi c'est efficace

- Les coûts d'**input** dominent la facture
- Streamer 5000 lignes de logs verbeux = 5000+ tokens d'input
- Streamer 20 lignes pertinentes = ~20 tokens

### Cas d'usage typiques

- Builds longs (Webpack, Rust cargo, gradle)
- Suites de tests complètes
- Déploiements
- Logs de services (`docker logs`, journalctl)
- Long-running scripts d'analyse

### Référence

Voir le Tmux Cheatsheet pour les commandes : https://tmuxcheatsheet.com/

### Lien avec parallélisation

Ce pattern combine bien avec [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md) : un worktree par instance Claude, chaque instance utilise tmux pour ses processus longs.

## Related pages

- [modular-codebase-tokens](modular-codebase-tokens.md)
- [mgrep-vs-grep](mgrep-vs-grep.md)
- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
