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

Il génère les fichiers canoniques d'un harness (`AGENTS.md` / `CLAUDE.md`, `feature_list.json`, `progress.md`, `init.sh`, `session-handoff.md`) et les valide via un score structurel sur les [[five-subsystem-harness-architecture|5 subsystèmes]] : Instructions / State / Verification / Scope / Lifecycle.

→ Voir [[harness-creator-skill]] pour le détail des scripts et templates.

### skill-creator

Meta-skill officiel Anthropic (`anthropics/skills`). Fournit un workflow complet pour créer de nouveaux skills ou améliorer des skills existants :

1. **Capture d'intention** → interview de l'utilisateur
2. **Rédaction du SKILL.md** (frontmatter name + description + corps)
3. **Test** : prompts réalistes lancés en parallèle (avec skill vs sans skill)
4. **Évaluation** : grading quantitatif + review humaine via eval viewer
5. **Itération** jusqu'à satisfaction
6. **Optimisation du triggering** : boucle d'optimisation de la description

→ Voir [[skill-creator-meta-skill]], [[skill-anatomy]], [[skill-creation-workflow]], [[skill-eval-workflow]], [[skill-description-optimization]].

### Relation entre les deux

`harness-creator` a lui-même été développé avec la méthodologie `skill-creator` (draft → test → eval → iterate). Les deux partagent le concept d'[[eval-roadmap|évaluation]] et de vérification, et s'appuient sur la même notion de [[prompt-as-asset|skill-as-reusable-asset]].

## Related pages

- [[harness-creator-skill]]
- [[skill-creator-meta-skill]]
- [[skill-anatomy]]
- [[skill-creation-workflow]]
- [[skill-eval-workflow]]
- [[skill-description-optimization]]
- [[five-subsystem-harness-architecture]]
- [[prompt-as-asset]]
- [[eval-roadmap]]
