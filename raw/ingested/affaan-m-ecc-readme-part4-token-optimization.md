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
## Token OptimizationClaude Code usage can be expensive if you don't manage token consumption. These settings significantly reduce costs without sacrificing quality.

### Recommended SettingsAdd to `~/.claude/settings.json`:

{
  "model": "sonnet",
  "env": {
    "MAX\_THINKING\_TOKENS": "10000",
    "CLAUDE\_AUTOCOMPACT\_PCT\_OVERRIDE": "50"
  }
}

| Setting | Default | Recommended | Impact |
| --- | --- | --- | --- |
| `model` | opus | **sonnet** | ~60% cost reduction; handles 80%+ of coding tasks |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | ~70% reduction in hidden thinking cost per request |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | Compacts earlier — better quality in long sessions |
| `ECC_CONTEXT_MONITOR_COST_WARNINGS` | on | **off for subscription users** | Suppresses agent-facing API-rate estimate warnings while keeping context/scope/loop warnings |

Switch to Opus only when you need deep architectural reasoning:

```
/model opus
```

### Daily Workflow Commands| Command | When to Use |
| --- | --- |
| `/model sonnet` | Default for most tasks |
| `/model opus` | Complex architecture, debugging, deep reasoning |
| `/clear` | Between unrelated tasks (free, instant reset) |
| `/compact` | At logical task breakpoints (research done, milestone complete) |
| `/cost` | Monitor token spending during session |

If you use a Claude subscription and the context monitor's API-rate estimates are not useful, set `ECC_CONTEXT_MONITOR_COST_WARNINGS=off`. This only suppresses the agent-facing cost warnings; it does not disable context exhaustion, scope, or loop warnings.

### Strategic CompactionThe `strategic-compact` skill (included in this plugin) suggests `/compact` at logical breakpoints instead of relying on auto-compaction at 95% context. See `skills/strategic-compact/SKILL.md` for the full decision guide.

**When to compact:**

- After research/exploration, before implementation
- After completing a milestone, before starting the next
- After debugging, before continuing feature work
- After a failed approach, before trying a new one

**When NOT to compact:**

- Mid-implementation (you'll lose variable names, file paths, partial state)

### Context Window Management**Critical:** Don't enable all MCPs at once. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

- Keep under 10 MCPs enabled per project
- Keep under 80 tools active
- Use `/mcp` to disable unused Claude Code MCP servers; those runtime choices persist in `~/.claude.json`
- Use `ECC_DISABLED_MCPS` only to filter ECC-generated MCP configs during install/sync flows

### Agent Teams Cost WarningAgent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

---

## WARNING: Important Notes### Token OptimizationHitting daily limits? See the **[Token Optimization Guide](/affaan-m/ECC/blob/main/docs/token-optimization.md)** for recommended settings and workflow tips.

Quick wins:

// ~/.claude/settings.json
{
  "model": "sonnet",
  "env": {
    "MAX\_THINKING\_TOKENS": "10000",
    "CLAUDE\_AUTOCOMPACT\_PCT\_OVERRIDE": "50",
    "CLAUDE\_CODE\_SUBAGENT\_MODEL": "haiku"
  }
}

Use `/clear` between unrelated tasks, `/compact` at logical breakpoints, and `/cost` to monitor spending.

### CustomizationThese configs work for my workflow. You should:

1. Start with what resonates
2. Modify for your stack
3. Remove what you don't use
4. Add your own patterns