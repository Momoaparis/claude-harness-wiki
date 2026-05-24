# Les 5 subsystèmes d'une harness

**Summary** : Cadre fondateur du cours Learn Harness Engineering. Une harness complète = Instructions + Tools + Environment + State + Feedback. Chaque subsystème a une responsabilité distincte, et l'absence d'un seul casse l'ensemble.

**Sources** : `raw/ingested/lecture-02-what-a-harness-actually-is.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le modèle

```
              ┌──────────────────────────────────────┐
              │       1. Instructions (AGENTS.md)    │
              └──────────────┬───────────────────────┘
                             │
              ┌──────────────▼───────────────────────┐
              │       2. Tools (shell, tests, files) │
              └──────────────┬───────────────────────┘
                             │
              ┌──────────────▼───────────────────────┐
              │       3. Environment (deps, runtime) │
              └──────────────┬───────────────────────┘
                             │
              ┌──────────────▼───────────────────────┐
              │       4. State (PROGRESS.md, git)    │
              └──────────────┬───────────────────────┘
                             │
              ┌──────────────▼───────────────────────┐
              │       5. Feedback (verification cmd) │
              └──────────────────────────────────────┘
```

### Détail des 5 subsystèmes

#### 1. Instructions

**Rôle** : dire à l'agent *quoi* faire et *comment*.

- Fichier root : `AGENTS.md` (Codex/OpenAI) ou `CLAUDE.md` (Claude Code) — voir [[template-claude-md]]
- Format : ~50-200 lignes en entry file, le reste en topic documents (`docs/`)
- Contenu obligatoire : overview, stack, commandes first-run, hard constraints, liens vers docs détaillées
- Anti-pattern : **instruction bloat** (voir [[modular-instruction-architecture]])

#### 2. Tools

**Rôle** : donner à l'agent les capacités d'exécution.

- Accès shell, lecture/écriture fichiers, exécution tests
- Principe : **least privilege mais pas zero privilege** — ne pas désactiver le shell "pour la sécurité"
- Pour Claude Code : voir [[claude-code-hooks]] pour le filtrage fin via PreToolUse

#### 3. Environment

**Rôle** : rendre l'état d'exécution reproductible et transparent.

Fichiers clés :
- `pyproject.toml` / `package.json` — dépendances pinées
- `.nvmrc` / `.python-version` — version d'exécution
- `Dockerfile` / `devcontainer.json` — runtime complet isolé
- `Makefile` — commandes standardisées (`make setup`, `make test`)

> "Self-describing state" — l'agent doit pouvoir reconstruire l'env sans demander.

#### 4. State

**Rôle** : faire survivre l'information entre sessions et entre runs.

Voir [[progress-file-pattern]], [[decision-log-pattern]] :
- `PROGRESS.md` ou `claude-progress.md` — état actuel, tâches faites/en cours/bloquées
- `DECISIONS.md` — log append-only des décisions et leurs raisons
- Commits git — snapshot versionné gratuit, atomique
- Voir aussi [[acid-principles-agent-state]] : Atomicity / Consistency / Isolation / Durability

#### 5. Feedback

**Rôle** : permettre à l'agent (et à la harness) de vérifier que le travail est correct.

> "Among the five subsystems, the feedback subsystem usually has the lowest investment and highest return." — Lecture 02

- Commandes explicites listées dans les instructions : `pytest`, `mypy`, `ruff check`, `make verify`
- Evaluators automatiques (voir [[planner-generator-evaluator-3-agent-architecture]])
- Tests E2E qui prouvent que le système marche réellement (voir [[end-to-end-verification-only]])

### Le case study fondateur (Lecture 02)

Équipe TypeScript, même modèle, 4 stages d'amélioration de la harness :

| Stage | Ajouts | Taux de succès |
|-------|--------|----------------|
| Stage 1 | Prompt-only (rien d'autre) | **20%** |
| Stage 2 | + `AGENTS.md` (Instructions) | **60%** |
| Stage 3 | + verification commands (Feedback) | **80%** |
| Stage 4 | + `PROGRESS.md` (State) | **80-100%** |

**Modèle constant. Seule la harness change.** Voir aussi [[ablation-study-methodology]] pour la méthodologie de mesure.

### Le principe de "least privilege but sufficient"

L'agent a besoin de **suffisamment d'accès** pour faire son travail. Désactiver le shell pour des raisons de sécurité = casser le subsystème Tools = l'agent ne peut plus rien vérifier. La sécurité passe par [[agent-sandboxing]] et [[agent-observability]], pas par la mutilation.

### Antipatterns d'absence

| Subsystème manquant | Symptôme typique |
|---------------------|------------------|
| Instructions | L'agent invente conventions, drift entre sessions |
| Tools | L'agent écrit du code qu'il ne peut pas tester |
| Environment | "Works on my machine", builds qui ne reproduisent pas |
| State | Chaque session redécouvre tout → [[cross-session-context-loss]] |
| Feedback | L'agent déclare victoire trop tôt → [[three-layer-termination-validation]] |

### À retenir

1. Une harness incomplète = celle où **un** des 5 subsystèmes manque.
2. Le subsystème **Feedback** a le meilleur ROI marginal.
3. Le subsystème **State** est ce qui rend possible les sessions longues / multiples.
4. Tester en désactivant un subsystème à la fois ([[ablation-study-methodology]]) révèle la valeur réelle de chacun.

## Related pages

- [[harness-definition-et-philosophie]]
- [[modular-instruction-architecture]]
- [[progress-file-pattern]]
- [[end-to-end-verification-only]]
- [[ablation-study-methodology]]
- [[the-harness-engineering-curriculum-summary]]
