# harness-creator (skill)

**Summary** : Skill NPX du repo `walkinglabs/learn-harness-engineering` qui scaffolde et valide un harness complet autour d'un agent IA en évaluant 5 subsystèmes structurels.

**Sources** :
- `raw/ingested/Learn-Harness-Engineering.md`
- `raw/ingested/learn-harness-engineering_skills_harness-creator-at-main.md`

**Last updated** : 2026-05-27

---

## Contenu

### Rôle

`harness-creator` aide un repo à fournir les cinq choses dont un agent a besoin :

| Subsystème | Ce qu'il fournit |
|---|---|
| Instructions | `AGENTS.md` ou `CLAUDE.md` — règles et contexte |
| State | `progress.md`, `feature_list.json` — état persistant |
| Verification | Commandes de vérification par stack (npm/Python/Go/Rust…) |
| Scope | `feature_list.json` + limites explicites |
| Lifecycle | `init.sh`, `session-handoff.md` — bootstrap et passation |

Cette taxonomie diffère de celle du cours ([five-subsystem-harness-architecture](five-subsystem-harness-architecture.md) : Instructions / Tools / Environment / State / Feedback) — le harness-creator opérationnalise le concept avec des composants concrets et validables.

### Installation

```bash
npx skills add walkinglabs/learn-harness-engineering --skill harness-creator
# ou : copier skills/harness-creator/ dans le skill path du projet
```

### Scripts CLI

```bash
# Créer un harness depuis zéro
node skills/harness-creator/scripts/create-harness.mjs --target /path/to/project

# Valider et scorer un harness existant
node skills/harness-creator/scripts/validate-harness.mjs --target /path/to/project

# Générer un rapport HTML de benchmark
node skills/harness-creator/scripts/run-benchmark.mjs --target /path/to/project --html /path/to/report.html
```

Les scripts utilisent uniquement des modules Node.js built-in (aucune dépendance externe).

`create-harness.mjs` détecte le type de projet et le package manager (Node/npm/pnpm/yarn/bun, Python, Go, Rust, Maven, Gradle, .NET).

### Templates générés

- `AGENTS.md` / `CLAUDE.md` — scaffold d'instructions avec règles fonctionnelles
- `feature_list.json` — JSON Schema + exemple de feature list (→ [feature-list-as-primitive](feature-list-as-primitive.md))
- `progress.md` — journal de session append-only (→ [progress-file-pattern](progress-file-pattern.md))
- `init.sh` — script d'initialisation standard (→ [initialization-phase-separation](initialization-phase-separation.md))
- `session-handoff.md` — snapshot compact pour reprise (→ [template-session-handoff-md](template-session-handoff-md.md))

### Validation structurelle

`validate-harness.mjs` score les 5 subsystèmes : il vérifie que le harness est **présent et cohérent**, mais ne remplace pas de vrais tests avant/après session agent. Le score est structurel, pas fonctionnel.

10 cas d'éval inclus dans le skill (`evals/evals.json`).

### Références intégrées (7 patterns)

| Pattern | Quand l'utiliser |
|---|---|
| Memory Persistence | L'agent oublie entre sessions |
| Skill Runtime | Packager des workflows réutilisables |
| Context Engineering | Budget de contexte, chargement JIT |
| Tool Registry | Sécurité des outils, contrôle de la concurrence |
| Multi-Agent Coordination | Parallélisme, workflows de spécialisation |
| Lifecycle & Bootstrap | Hooks, tâches en arrière-plan, initialisation |
| Gotchas | 15 modes d'échec non-évidents avec corrections |

### Développement du skill

`harness-creator` a été développé avec la méthodologie [skill-creator-meta-skill](skill-creator-meta-skill.md) (draft → test → eval → iterate), ce qui en fait un exemple concret d'application du meta-skill.

## Related pages

- [harness-creator-et-skill-creator-summary](harness-creator-et-skill-creator-summary.md)
- [skill-creator-meta-skill](skill-creator-meta-skill.md)
- [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md)
- [feature-list-as-primitive](feature-list-as-primitive.md)
- [progress-file-pattern](progress-file-pattern.md)
- [initialization-phase-separation](initialization-phase-separation.md)
- [template-session-handoff-md](template-session-handoff-md.md)
- [session-clean-handoff](session-clean-handoff.md)
