# ECC — Everything Claude Code

**Summary** : Système d'optimisation des performances du harness Claude Code (et autres : Codex, OpenCode, Cursor) par Affaan Mustafa. Bundle de skills, instincts, mémoire, sécurité, et développement research-first. Repo : `github.com/affaan-m/ECC`.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Positionnement

ECC n'est pas un produit, c'est un **bundle de patterns d'optimisation** pour les harnesses d'agents — packagé sous forme de plugin Claude Code, mais portable vers Codex, OpenCode, Cursor.

Il opérationnalise les concepts décrits dans [[the-longform-guide-summary|Longform Guide]] et [[the-shorthand-guide-summary|Shorthand Guide]] (même auteur) en composants installables.

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

Voir aussi [[subagent-architecture]], [[sub-agent-context-problem]].

### 3. Hooks

Réagissent aux événements de tool. Cf. [[claude-code-hooks]] et le détail spécifique au plugin : [[ecc-hooks-autoloading]].

### 4. Rules

Guidelines toujours appliquées, organisées en `common/` (universel) + `typescript/`, `python/`, `golang/`, `swift/`, `php/`, `arkts/` (langage-spécifique). Voir [[ecc-token-optimization]] pour l'impact sur le coût.

## Ecosystem tools

- **Skill Creator** (`/skill-create`) — génère des SKILL.md depuis l'historique git du repo. Option locale ou via GitHub App.
- **[[agentshield]]** — scanner de sécurité (hooks, MCP, permissions, secrets).
- **[[continuous-learning-v2]]** — système instinct-based : `/instinct-status`, `/evolve`, etc.

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

- [[the-shorthand-guide-summary]] et [[the-longform-guide-summary]] donnent les fondations conceptuelles.
- [[the-agentic-security-summary]] cadre les risques que ECC ([[agentshield]]) cherche à mitiger.
- [[ecc-token-optimization]] détaille les settings recommandés.

## Related pages

- [[ecc-token-optimization]]
- [[ecc-hooks-autoloading]]
- [[continuous-learning-v2]]
- [[agentshield]]
- [[the-shorthand-guide-summary]]
- [[the-longform-guide-summary]]
- [[the-agentic-security-summary]]
