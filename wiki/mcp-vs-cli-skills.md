# MCP vs CLI + Skills

**Summary** : Pattern d'optimisation du contexte consistant à remplacer certains MCPs (voir [model-context-protocol](model-context-protocol.md)) par des skills/commandes qui wrappent les CLI natives correspondantes.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-06-11

---

## Contenu

### Le constat

Beaucoup de MCPs sont essentiellement des wrappers autour de CLIs existantes :
- GitHub MCP wrap `gh`
- Supabase MCP wrap `supabase`
- Vercel/Railway MCPs wrap leurs CLIs respectives

Le MCP est pratique mais **mange du contexte** dès qu'il est chargé.

### La stratégie

Remplacer les MCPs par des **skills/commandes Claude** qui appellent directement la CLI.

**Exemple GitHub** :
- Avant : GitHub MCP chargé en permanence
- Après : commande `/gh-pr` qui wrap `gh pr create` avec les options préférées

**Avantage** : même fonctionnalité, contexte libéré pour le travail réel.

### Lazy loading des MCPs

Avec les progrès récents de Claude Code (équipe Boris Cherny), les MCPs sont désormais **lazy-loaded** — ils ne consomment plus de contexte à l'init. Cela résout partiellement le problème du contexte mais **pas celui du coût en tokens**.

### CLI + skills reste pertinent pour les tokens

Même avec lazy loading :
- Les opérations MCP heavy (database queries, deployments) consomment beaucoup de tokens
- Les exécuter via CLI **hors contexte** (output non-streamé) puis re-feeder le résumé à Claude économise massivement
- Voir [background-processes-tmux](background-processes-tmux.md) pour le pattern

### Cas où le MCP est irremplaçable : `--chrome`

Le flag [`--chrome`](claude-code-chrome-flag.md) de Claude Code est un MCP browser qui permet à Claude de piloter Chrome local. Il ne peut pas être remplacé par une CLI car les interfaces web (Lovart, Figma, etc.) n'exposent pas d'API CLI.

C'est le cas d'usage où le MCP apporte une valeur exclusive : accès à une session navigateur déjà authentifiée, interaction avec des interfaces uniquement web. Documenté avec [claude-opus-47](claude-opus-47.md) pilotant Lovart de bout en bout (Brand Kit → poster → police → PSD → vidéo).

### Quand utiliser MCP vs CLI+skill

| Cas | Approche |
|-----|----------|
| Opération légère, fréquente | MCP (lazy-loaded) |
| Opération heavy en output | CLI + skill |
| Opération non-interactive | CLI + skill (peut tourner en background) |
| Opération nécessitant feedback temps réel | MCP |

### Lien avec optimisation tokens

Ce pattern s'inscrit dans la stratégie globale d'**optimisation des tokens** :
- [mgrep-vs-grep](mgrep-vs-grep.md) pour la recherche
- [modular-codebase-tokens](modular-codebase-tokens.md) pour l'architecture
- [background-processes-tmux](background-processes-tmux.md) pour les longs jobs
- CLI+skills pour les MCPs

## Related pages

- [background-processes-tmux](background-processes-tmux.md)
- [mgrep-vs-grep](mgrep-vs-grep.md)
- [modular-codebase-tokens](modular-codebase-tokens.md)
- [llms-txt-pattern](llms-txt-pattern.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
