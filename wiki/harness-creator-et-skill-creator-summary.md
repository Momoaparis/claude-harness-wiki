# Harness Creator & Skill Creator — Résumé des sources

**Summary** : Deux outils complémentaires pour l'ingénierie de harnesses : `harness-creator` (walkinglabs) scaffold et valide un harness en 5 subsystèmes ; `skill-creator` (Anthropic) est le meta-skill pour créer, tester et améliorer des skills agent.

**Sources** :
- `raw/ingested/Learn-Harness-Engineering.md`
- `raw/ingested/learn-harness-engineering_skills_harness-creator-at-main.md`
- `raw/ingested/skills_skills_skill-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### harness-creator

Skill NPX du repo `walkinglabs/learn-harness-engineering`. Sert à scaffolder et auditer un harness autour d'un agent IA (Claude Code, Codex, Cursor…).

**Installation** :
```bash
npx skills add walkinglabs/learn-harness-engineering --skill harness-creator
```

Il génère les fichiers canoniques d'un harness (`AGENTS.md` / `CLAUDE.md`, `feature_list.json`, `progress.md`, `init.sh`, `session-handoff.md`) et les valide via un score structurel sur les [5 subsystèmes](five-subsystem-harness-architecture.md) : Instructions / State / Verification / Scope / Lifecycle.

→ Voir [harness-creator-skill](harness-creator-skill.md) pour le détail des scripts et templates.

### skill-creator

Meta-skill officiel Anthropic (`anthropics/skills`). Fournit un workflow complet pour créer de nouveaux skills ou améliorer des skills existants :

1. **Capture d'intention** → interview de l'utilisateur
2. **Rédaction du SKILL.md** (frontmatter name + description + corps)
3. **Test** : prompts réalistes lancés en parallèle (avec skill vs sans skill)
4. **Évaluation** : grading quantitatif + review humaine via eval viewer
5. **Itération** jusqu'à satisfaction
6. **Optimisation du triggering** : boucle d'optimisation de la description

→ Voir [skill-creator-meta-skill](skill-creator-meta-skill.md), [skill-anatomy](skill-anatomy.md), [skill-creation-workflow](skill-creation-workflow.md), [skill-eval-workflow](skill-eval-workflow.md), [skill-description-optimization](skill-description-optimization.md).

### Relation entre les deux

`harness-creator` a lui-même été développé avec la méthodologie `skill-creator` (draft → test → eval → iterate). Les deux partagent le concept d'[évaluation](eval-roadmap.md) et de vérification, et s'appuient sur la même notion de [skill-as-reusable-asset](prompt-as-asset.md).

## Related pages

- [harness-creator-skill](harness-creator-skill.md)
- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [skill-anatomy](skill-anatomy.md)
- [skill-creation-workflow](skill-creation-workflow.md)
- [skill-eval-workflow](skill-eval-workflow.md)
- [skill-description-optimization](skill-description-optimization.md)
- [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md)
- [prompt-as-asset](prompt-as-asset.md)
- [eval-roadmap](eval-roadmap.md)
