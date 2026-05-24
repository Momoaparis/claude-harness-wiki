---
title: "affaan-m/ECC: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond."
source: "https://github.com/affaan-m/ECC"
author:
published:
created: 2026-05-23
description: "The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. - affaan-m/ECC"
tags:
  - "clippings"
---
#### Install hooksDo not copy the raw repo `hooks/hooks.json` into `~/.claude/settings.json` or `~/.claude/hooks/hooks.json`. That file is plugin/repo-oriented and is meant to be installed through the ECC installer or loaded as a plugin, so raw copying is not a supported manual install path.

Use the installer to install only the Claude hook runtime so command paths are rewritten correctly:

# macOS / Linux
bash ./install.sh --target claude --modules hooks-runtime

# Windows PowerShell
pwsh \-File .\\install.ps1 \--target claude \--modules hooks\-runtime

That writes resolved hooks to `~/.claude/hooks/hooks.json` and leaves any existing `~/.claude/settings.json` untouched.

If you installed ECC via `/plugin install`, do not copy those hooks into `settings.json`. Claude Code v2.1+ already auto-loads plugin `hooks/hooks.json`, and duplicating them in `settings.json` causes duplicate execution and cross-platform hook conflicts.

Windows note: the Claude config directory is `%USERPROFILE%\\.claude`, not `~/claude`.

#### Configure MCPsClaude plugin installs intentionally do not auto-enable ECC's bundled MCP server definitions. This avoids overlong plugin MCP tool names on strict third-party gateways while keeping manual MCP setup available.

Use Claude Code's `/mcp` command or CLI-managed MCP setup for live Claude Code server changes. Use `/mcp` for Claude Code runtime disables; Claude Code persists those choices in `~/.claude.json`.

For repo-local MCP access, copy desired MCP server definitions from `mcp-configs/mcp-servers.json` into a project-scoped `.mcp.json`.

If you already run your own copies of ECC-bundled MCPs, set:

export ECC\_DISABLED\_MCPS="github,context7,exa,playwright,sequential-thinking,memory"

ECC-managed install and Codex sync flows will skip or remove those bundled servers instead of re-adding duplicates. `ECC_DISABLED_MCPS` is an ECC install/sync filter, not a live Claude Code toggle.

**Important:** Replace `YOUR_*_HERE` placeholders with your actual API keys.

---

## Key Concepts### AgentsSubagents handle delegated tasks with limited scope. Example:

\---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: \["Read", "Grep", "Glob", "Bash"\]
model: opus
\---

You are a senior code reviewer...

### SkillsSkills are the primary workflow surface. They can be invoked directly, suggested automatically, and reused by agents. ECC still ships maintained `commands/` during migration, while retired short-name shims live under `legacy-command-shims/` for explicit opt-in only. New workflow development should land in `skills/` first.

\# TDD Workflow

1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage

### HooksHooks fire on tool events. Example - warn about console.log:

{
  "matcher": "tool == \\"Edit\\" && tool\_input.file\_path matches \\"\\\\\\\\.(ts|tsx|js|jsx)$\\"",
  "hooks": \[{
    "type": "command",
    "command": "#!/bin/bash\\ngrep -n 'console\\\\.log' \\"$file\_path\\" && echo '\[Hook\] Remove console.log' >&2"
  }\]
}

### RulesRules are always-follow guidelines, organized into `common/` (language-agnostic) + language-specific directories:

```
rules/
  common/          # Universal principles (always install)
  typescript/      # TS/JS specific patterns and tools
  python/          # Python specific patterns and tools
  golang/          # Go specific patterns and tools
  swift/           # Swift specific patterns and tools
  php/             # PHP specific patterns and tools
  arkts/           # HarmonyOS / ArkTS patterns and constraints
```

See [`rules/README.md`](/affaan-m/ECC/blob/main/rules/README.md) for installation and structure details.

---

## Which Agent Should I Use?Not sure where to start? Use this quick reference. Skills are the canonical workflow surface; maintained slash entries stay available for command-first workflows.

| I want to... | Use this surface | Agent used |
| --- | --- | --- |
| Plan a new feature | `/ecc:plan "Add auth"` | planner |
| Design system architecture | `/ecc:plan` + architect agent | architect |
| Write code with tests first | `tdd-workflow` skill | tdd-guide |
| Review code I just wrote | `/code-review` | code-reviewer |
| Fix a failing build | `/build-fix` | build-error-resolver |
| Run end-to-end tests | `e2e-testing` skill | e2e-runner |
| Find security vulnerabilities | `/security-scan` | security-reviewer |
| Remove dead code | `/refactor-clean` | refactor-cleaner |
| Update documentation | `/update-docs` | doc-updater |
| Review Go code | `/go-review` | go-reviewer |
| Review Python code | `/python-review` | python-reviewer |
| Review F# code | *(invoke `fsharp-reviewer` directly)* | fsharp-reviewer |
| Review TypeScript/JavaScript code | *(invoke `typescript-reviewer` directly)* | typescript-reviewer |
| Develop HarmonyOS apps | *(invoke `harmonyos-app-resolver` directly)* | harmonyos-app-resolver |
| Audit database queries | *(auto-delegated)* | database-reviewer |
| Review production ML changes | `mle-workflow` skill + `mle-reviewer` agent | mle-reviewer |

### Common WorkflowsSlash forms below are shown where they remain part of the maintained command surface. Retired short-name shims such as `/tdd` and `/eval` live in `legacy-command-shims/` for explicit opt-in only.

**Starting a new feature:**

```
/ecc:plan "Add user authentication with OAuth"
                                              → planner creates implementation blueprint
tdd-workflow skill                            → tdd-guide enforces write-tests-first
/code-review                                  → code-reviewer checks your work
```

**Fixing a bug:**

```
tdd-workflow skill                            → tdd-guide: write a failing test that reproduces it
                                              → implement the fix, verify test passes
/code-review                                  → code-reviewer: catch regressions
```

**Preparing for production:**

```
/security-scan                                → security-reviewer: OWASP Top 10 audit
e2e-testing skill                             → e2e-runner: critical user flow tests
/test-coverage                                → verify 80%+ coverage
```