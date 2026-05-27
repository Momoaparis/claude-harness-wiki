# Memory Persistence Hooks

**Summary** : Triplet de hooks (`PreCompact`, `SessionStart`, `Stop`) qui chaînent la persistance et le rechargement automatique de la mémoire entre sessions Claude Code.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Trois hooks ciblent le cycle de vie de la session pour automatiser la mémoire continue.

### Les trois hooks

| Hook | Rôle |
|------|------|
| `PreCompact` | Sauvegarde l'état important avant compactage du contexte |
| `SessionStart` | Charge le contexte des sessions précédentes au démarrage |
| `Stop` | Persiste les apprentissages en fin de session |

### Configuration `settings.json`

```json
{
  "hooks": {
    "PreCompact": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/memory-persistence/pre-compact.sh"
      }]
    }],
    "SessionStart": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/memory-persistence/session-start.sh"
      }]
    }],
    "Stop": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/hooks/memory-persistence/session-end.sh"
      }]
    }]
  }
}
```

### Ce que font les scripts

- **`pre-compact.sh`** : log les événements de compactage, met à jour le fichier de session active avec timestamp
- **`session-start.sh`** : cherche les sessions récentes (7 derniers jours), notifie le contexte disponible et les skills appris
- **`session-end.sh`** : crée/met à jour le fichier de session du jour avec template, track start/end

### Bénéfice

Mémoire continue **sans intervention manuelle** — chaque session démarre informée des précédentes. Combine bien avec [session-storage-pattern](session-storage-pattern.md) qui fournit le format des fichiers.

## Related pages

- [claude-code-hooks](claude-code-hooks.md)
- [session-storage-pattern](session-storage-pattern.md)
- [strategic-compact](strategic-compact.md)
- [continuous-learning-skill](continuous-learning-skill.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
