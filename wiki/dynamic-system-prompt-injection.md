# Dynamic System Prompt Injection

**Summary** : Pattern consistant à injecter du contexte dans le system prompt de Claude via `--system-prompt` au lieu de tout mettre dans `CLAUDE.md` ou `.claude/rules/`.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Au lieu de charger tout le contexte à chaque session via `CLAUDE.md`, on peut injecter du contexte spécifique selon le besoin :

```bash
claude --system-prompt "$(cat memory.md)"
```

### Différence avec les `@file references` ou `.claude/rules/`

| Approche | Où va le contenu | Autorité |
|----------|------------------|----------|
| `@file.md` ou `.claude/rules/` | Tool output (lu pendant la conversation) | Plus faible |
| `--system-prompt` | System prompt avant la conversation | Plus forte |

L'**instruction hierarchy** de Claude : system > user message > tool result. Donc une instruction injectée via `--system-prompt` est plus respectée.

### Cas d'usage

- Règles comportementales strictes
- Contraintes spécifiques au projet
- Contexte que Claude doit absolument prioriser

### Setup pratique avec alias

```bash
alias claude-dev='claude --system-prompt "$(cat ~/.claude/contexts/dev.md)"'
alias claude-review='claude --system-prompt "$(cat ~/.claude/contexts/review.md)"'
alias claude-research='claude --system-prompt "$(cat ~/.claude/contexts/research.md)"'
```

Chaque alias charge un contexte différent — dev focus implementation, review focus quality, research focus exploration.

### Avantages vs `.claude/rules/`

- **Plus rapide** : pas de tool call
- **Plus fiable** : autorité system-level
- **Légèrement plus efficient en tokens**

### Limite

Pour la majorité du travail quotidien, la différence est marginale. C'est une optimisation à considérer pour les cas critiques.

## Related pages

- [strategic-compact](strategic-compact.md)
- [session-storage-pattern](session-storage-pattern.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
