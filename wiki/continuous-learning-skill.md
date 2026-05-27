# Continuous Learning Skill

**Summary** : Skill qui évalue automatiquement chaque session via le `Stop` hook et extrait les patterns réutilisables (debugging, workarounds, conventions) dans `~/.claude/skills/learned/`.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Problème résolu

Tokens gaspillés, contexte gaspillé, frustration : on doit re-prompter Claude pour des erreurs qu'il a déjà faites dans une session précédente. La solution est d'extraire automatiquement ces apprentissages.

### Mécanisme

Quand Claude découvre quelque chose de non-trivial (technique de debug, workaround, pattern projet spécifique), il le sauvegarde comme nouveau skill. La prochaine fois qu'un problème similaire survient, le skill est chargé automatiquement.

### Pourquoi le `Stop` hook (et pas `UserPromptSubmit`)

| Hook | Latence | Fréquence | Utilisation |
|------|---------|-----------|-------------|
| `UserPromptSubmit` | Ajoute latence à **chaque** prompt | Trop fréquent | Overkill |
| `Stop` | Aucune latence pendant la session | Une fois en fin de session | Idéal |

`Stop` évalue la session complète plutôt que par petits morceaux.

### Installation

```bash
# Cloner tout le repo
git clone https://github.com/affaan-m/everything-claude-code.git ~/.claude/skills/everything-claude-code

# Ou juste le skill
mkdir -p ~/.claude/skills/continuous-learning
curl -sL https://raw.githubusercontent.com/affaan-m/everything-claude-code/main/skills/continuous-learning/evaluate-session.sh \
  > ~/.claude/skills/continuous-learning/evaluate-session.sh
chmod +x ~/.claude/skills/continuous-learning/evaluate-session.sh
```

### Configuration hook

```json
{
  "hooks": {
    "Stop": [{
      "matcher": "*",
      "hooks": [{"type": "command", "command": "~/.claude/skills/continuous-learning/evaluate-session.sh"}]
    }]
  }
}
```

### Extraction manuelle : commande `/learn`

Pas besoin d'attendre la fin de session — la commande `/learn` permet d'extraire un pattern immédiatement après l'avoir résolu, avec confirmation avant sauvegarde.

## Related pages

- [memory-persistence-hooks](memory-persistence-hooks.md)
- [claude-code-hooks](claude-code-hooks.md)
- [session-storage-pattern](session-storage-pattern.md)
- [claude-code-commands](claude-code-commands.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
