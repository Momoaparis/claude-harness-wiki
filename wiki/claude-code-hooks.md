# Claude Code Hooks

**Summary** : Vue d'ensemble des hooks disponibles dans Claude Code et leur rôle dans le cycle de vie d'une session ou d'un appel d'outil.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

Les hooks sont des scripts shell qui s'exécutent automatiquement en réponse à des événements de Claude Code. Ils sont configurés dans `settings.json`.

### Hooks de cycle d'outil

| Hook | Déclenchement | Usage typique |
|------|--------------|---------------|
| `PreToolUse` | Avant l'exécution d'un outil | Validation, modification des paramètres, comptage |
| `PostToolUse` | Après l'exécution d'un outil | Auto-format, vérification, logging |

### Hooks de cycle de session

| Hook | Déclenchement | Usage typique |
|------|--------------|---------------|
| `SessionStart` | Au démarrage d'une session | Chargement de contexte précédent |
| `PreCompact` | Avant un compactage de contexte | Sauvegarde de l'état important |
| `Stop` | À la fin de la session | Persistance des apprentissages |

### Hook de prompt

| Hook | Déclenchement | Coût |
|------|--------------|------|
| `UserPromptSubmit` | À chaque message envoyé | Ajoute latence à chaque prompt — usage à doser |

### Hook de permission

| Hook | Déclenchement | Usage typique |
|------|--------------|---------------|
| `Notification` | Lors d'une demande de permission | Logger, notifier, décider d'auto-accepter ou bloquer |

### Format de configuration

```json
{
  "hooks": {
    "NomDuHook": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "/chemin/vers/script.sh"
      }]
    }]
  }
}
```

### Patterns recommandés

- **`PreToolUse` sur Edit/Write** : suggérer un compact stratégique (voir [strategic-compact](strategic-compact.md))
- **`PostToolUse`** : auto-format, lint, tests rapides
- **`Stop`** : extraction d'apprentissage (voir [continuous-learning-skill](continuous-learning-skill.md))
- **Triplet `PreCompact`/`SessionStart`/`Stop`** : persistance mémoire (voir [memory-persistence-hooks](memory-persistence-hooks.md))

### Règle de coût

Préférer les hooks de cycle de session aux hooks par-prompt — leur coût est amorti sur toute la session.

## Related pages

- [strategic-compact](strategic-compact.md)
- [memory-persistence-hooks](memory-persistence-hooks.md)
- [continuous-learning-skill](continuous-learning-skill.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
