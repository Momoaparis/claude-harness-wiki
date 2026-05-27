# ECC — Everything Claude Code

**Summary** : Système d'optimisation des performances du harness Claude Code (et autres : Codex, OpenCode, Cursor) par Affaan Mustafa. Bundle de skills, instincts, mémoire, sécurité, et développement research-first. Repo : `github.com/affaan-m/ECC`.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

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

- [ecc-token-optimization](ecc-token-optimization.md)
- [ecc-hooks-autoloading](ecc-hooks-autoloading.md)
- [continuous-learning-v2](continuous-learning-v2.md)
- [agentshield](agentshield.md)
- [the-shorthand-guide-summary](the-shorthand-guide-summary.md)
- [the-longform-guide-summary](the-longform-guide-summary.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
