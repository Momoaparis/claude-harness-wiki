# Anatomie d'un skill

**Summary** : Un skill est composé d'un `SKILL.md` obligatoire et de ressources bundlées optionnelles (scripts, références, assets), avec un système de chargement progressif à 3 niveaux.

**Sources** :
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Structure de fichiers

```
skill-name/
├── SKILL.md                  (requis)
│   ├── YAML frontmatter      (name, description requis)
│   └── Corps Markdown        (instructions)
└── Ressources bundlées       (optionnel)
    ├── scripts/              Code exécutable pour tâches déterministes/répétitives
    ├── references/           Docs chargées en contexte selon besoin
    └── assets/               Fichiers utilisés en sortie (templates, icônes, polices)
```

### Chargement progressif (3 niveaux)

| Niveau | Contenu | Quand chargé | Taille cible |
|---|---|---|---|
| 1 — Metadata | `name` + `description` | Toujours en contexte | ~100 mots |
| 2 — SKILL.md body | Instructions complètes | Quand le skill se déclenche | < 500 lignes idéal |
| 3 — Bundled resources | Scripts, références, assets | À la demande | Illimité |

Les scripts peuvent s'exécuter **sans être chargés en contexte** — avantage fort pour les opérations lourdes.

Ce pattern de chargement progressif est la même logique que [modular-instruction-architecture](modular-instruction-architecture.md) appliquée aux skills (entry file court + topic docs on-demand).

### SKILL.md — Frontmatter

```yaml
---
name: skill-identifier
description: |
  Quand utiliser ce skill (contextes déclencheurs spécifiques).
  Ce que le skill fait. Légèrement "pushy" pour éviter l'undertriggering.
compatibility:   # optionnel — outils requis, dépendances
---
```

La `description` est **le mécanisme de déclenchement principal**. Claude décide d'invoquer un skill uniquement sur la base du `name` + `description`. Les infos "quand utiliser" vont dans `description`, pas dans le corps.

### Principes de rédaction du SKILL.md

- Mode impératif pour les instructions
- Expliquer le *pourquoi* plutôt qu'empiler des MUST (les LLMs comprennent les raisons)
- Pour de grandes familles de domaines, organiser par variante avec fichiers de référence séparés :

```
cloud-deploy/
├── SKILL.md     (workflow + sélection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

Claude ne charge que le fichier de référence pertinent.

- Si > 300 lignes dans un fichier de référence, inclure une table des matières

### Bundler des scripts

Quand plusieurs runs de test produisent indépendamment le même script helper (`create_docx.py`, `build_chart.py`…), c'est un signal fort que ce script devrait être bundlé dans `scripts/` — économisant chaque invocation future de la redécouverte.

### Packaging

```bash
python -m scripts.package_skill <path/to/skill-folder>
# → produit un fichier .skill installable
```

## Related pages

- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [skill-creation-workflow](skill-creation-workflow.md)
- [modular-instruction-architecture](modular-instruction-architecture.md)
- [prompt-as-asset](prompt-as-asset.md)
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [lost-in-the-middle-effect](lost-in-the-middle-effect.md)
