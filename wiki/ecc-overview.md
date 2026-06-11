# ECC — Everything Claude Code

**Summary** : Système d'optimisation des performances du harness Claude Code (et autres : Codex, OpenCode, Cursor, Gemini, Zed) par Affaan Mustafa. Depuis **v2.0.0 (juin 2026)**, repositionné comme « agent harness operating system » cross-harness : ~261-262 skills, 64 agents, 84 commandes legacy. Repo : `github.com/affaan-m/ECC`.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`, `raw/ingested/affaan-m-ecc-2-0-0-release-notes.md`, `raw/ingested/affaan-m-ecc-2-0-0-rc1-notes.md`

**Last updated** : 2026-06-11

---

## Positionnement

ECC n'est pas un produit, c'est un **bundle de patterns d'optimisation** pour les harnesses d'agents — packagé sous forme de plugin Claude Code, mais portable vers Codex, OpenCode, Cursor.

Il opérationnalise les concepts décrits dans [Longform Guide](the-longform-guide-summary.md) et [Shorthand Guide](the-shorthand-guide-summary.md) (même auteur) en composants installables.

## Les 4 surfaces de l'écosystème

### 1. Skills

Surface principale du workflow. Skills = workflows réutilisables, invocables directement ou suggérés. `skills/` est la cible des nouveaux développements (les `commands/` legacy migrent vers cette structure).

### 2. Agents

Subagents pour les tâches déléguées à scope limité. Définis via frontmatter YAML :

```yaml
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---
```

Voir aussi [subagent-architecture](subagent-architecture.md), [sub-agent-context-problem](sub-agent-context-problem.md).

### 3. Hooks

Réagissent aux événements de tool. Cf. [claude-code-hooks](claude-code-hooks.md) et le détail spécifique au plugin : [ecc-hooks-autoloading](ecc-hooks-autoloading.md).

### 4. Rules

Guidelines toujours appliquées, organisées en `common/` (universel) + `typescript/`, `python/`, `golang/`, `swift/`, `php/`, `arkts/` (langage-spécifique). Voir [ecc-token-optimization](ecc-token-optimization.md) pour l'impact sur le coût.

## Nouveautés v2.0.0

La graduation stable de la ligne 2.0 fait d'ECC un **OS cross-harness** : Claude Code reste first-class, mais Codex, OpenCode, Cursor, Gemini, Zed et les workflows terminal-only partagent les mêmes skills, rules, hooks, conventions MCP et release gates (source: affaan-m-ecc-2-0-0-release-notes.md). Composants neufs notables :

- **Control-pane substrate** — adapters de session harness-neutres (`ecc.session.v1`). Détail : [ecc-control-pane-substrate](ecc-control-pane-substrate.md).
- **Famille d'orchestrateurs `orch-*`** — orchestration dynamique d'équipes de workflow. Détail : [ecc-orchestrator-family](ecc-orchestrator-family.md).
- **MCP inventory** (`ecc.mcp.v1`) — vue normalisée des configs MCP cross-harness, détection de drift, redaction de secrets. Complète [mcp-vs-cli-skills](mcp-vs-cli-skills.md).
- **Worktree-lifecycle service** — prédiction déterministe de conflits + garbage collection sûr des worktrees parallèles. Relié à [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md) et [harness-entropy-management](harness-entropy-management.md).
- **Optimization pack** — `parallel-execution-optimizer`, `benchmark-optimization-loop`, `data-throughput-accelerator`, `latency-critical-systems`, `recursive-decision-ledger` (source: affaan-m-ecc-2-0-0-release-notes.md).
- **Dashboard GUI** Tkinter + **alpha Rust `ecc2/`** (control-plane) + **operator status snapshots** (`ecc status --markdown --write status.md`) (source: affaan-m-ecc-2-0-0-rc1-notes.md).

### À savoir pour l'install

- **Node 21+** : un bug (#2184) rendait les plugin hooks silencieusement no-op — mettre à jour si concerné (source: affaan-m-ecc-2-0-0-release-notes.md).
- **Defaults plus légers** : `rules/zh` sorti de l'install default toujours-chargée ; surface OpenCode réduite avec hooks-runtime gated (source: affaan-m-ecc-2-0-0-release-notes.md).

## Ecosystem tools

- **Skill Creator** (`/skill-create`) — génère des SKILL.md depuis l'historique git du repo. Option locale ou via GitHub App.
- **[agentshield](agentshield.md)** — scanner de sécurité (hooks, MCP, permissions, secrets).
- **[continuous-learning-v2](continuous-learning-v2.md)** — système instinct-based : `/instinct-status`, `/evolve`, etc.

## Quick reference « which agent ? »

| Tâche | Surface | Agent |
|------|---------|-------|
| Planifier une feature | `/ecc:plan "Add auth"` | planner |
| Design d'architecture | `/ecc:plan` + architect | architect |
| TDD | skill `tdd-workflow` | tdd-guide |
| Code review | `/code-review` | code-reviewer |
| Fix de build | `/build-fix` | build-error-resolver |
| Tests E2E | skill `e2e-testing` | e2e-runner |
| Audit sécurité | `/security-scan` | security-reviewer |
| Dead code | `/refactor-clean` | refactor-cleaner |

## Lien avec le wiki existant

- [the-shorthand-guide-summary](the-shorthand-guide-summary.md) et [the-longform-guide-summary](the-longform-guide-summary.md) donnent les fondations conceptuelles.
- [the-agentic-security-summary](the-agentic-security-summary.md) cadre les risques que ECC ([agentshield](agentshield.md)) cherche à mitiger.
- [ecc-token-optimization](ecc-token-optimization.md) détaille les settings recommandés.

## Related pages

- [ecc-control-pane-substrate](ecc-control-pane-substrate.md)
- [ecc-orchestrator-family](ecc-orchestrator-family.md)
- [ecc-token-optimization](ecc-token-optimization.md)
- [ecc-hooks-autoloading](ecc-hooks-autoloading.md)
- [continuous-learning-v2](continuous-learning-v2.md)
- [agentshield](agentshield.md)
- [the-shorthand-guide-summary](the-shorthand-guide-summary.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
