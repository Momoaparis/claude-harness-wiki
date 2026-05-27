# Modular Codebase = Cheaper Tokens

**Summary** : Une architecture modulaire (fichiers <500 lignes, modules isolés) réduit le coût en tokens et augmente le taux de succès au premier essai de Claude Code.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Lien direct entre architecture et coût

Quand Claude doit éditer ou comprendre une fonction dans un fichier de 2000 lignes :
- Il fait plusieurs tool calls pour lire le fichier morceau par morceau
- Il peut perdre de l'information entre les lectures
- Il doit potentiellement re-lire des sections déjà vues
- Chaque re-lecture coûte des tokens d'input

À l'inverse, des fichiers de quelques centaines de lignes :
- Lus en une seule passe
- Pas de risque de perdre du contexte
- Pas de re-lectures

### Architecture recommandée

```
root/
├── docs/
├── scripts/
├── src/
│   ├── apps/                  # Entry points (API, CLI, Workers)
│   ├── modules/               # Cœur du système
│   │   ├── ordering/          # Module auto-contenu
│   │   │   ├── api/           # Interface publique
│   │   │   ├── domain/        # Logique métier pure
│   │   │   ├── infrastructure/ # DB, clients externes
│   │   │   ├── use-cases/     # Orchestration
│   │   │   └── tests/
│   │   ├── catalog/
│   │   └── identity/
│   ├── shared/                # Code partagé entre modules
│   │   ├── kernel/
│   │   ├── events/
│   │   └── utils/
│   └── main.ts
├── tests/                     # Tests E2E globaux
└── package.json
```

### Bénéfices cumulatifs

1. **Tokens** : moins de lectures, moins de re-lectures
2. **Qualité** : tâches finies du premier coup plus souvent
3. **Maintenance** : refactoring localisé sans impact transverse

### Hygiène associée

- **Identifier le dead code** régulièrement via skills automatisés
- **Skim manuel périodique** : repérer ce qui paraît répétitif, le feed à Claude avec un skill de refactor
- Combiner avec [mgrep-vs-grep](mgrep-vs-grep.md) pour optimiser encore les recherches

## Related pages

- [mgrep-vs-grep](mgrep-vs-grep.md)
- [subagent-architecture](subagent-architecture.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
