---
title: "affaan-m/ECC: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond."
source: "https://github.com/affaan-m/ECC/blob/main/README.md"
author:
published:
created: 2026-06-11
description: "The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond. - affaan-m/ECC"
tags:
  - "clippings"
---
### v2.0.0-rc.1 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha (Apr 2026)- **Dashboard GUI** — New Tkinter-based desktop application (`ecc_dashboard.py` or `npm run dashboard`) with dark/light theme toggle, font customization, and project logo in header and taskbar.
- **Public surface synced to the live repo** — metadata, catalog counts, plugin manifests, and install-facing docs now match the actual OSS surface: 64 agents, 262 skills, and 84 legacy command shims.
- **Operator and outbound workflow expansion** — `brand-voice`, `social-graph-ranker`, `connections-optimizer`, `customer-billing-ops`, `ecc-tools-cost-audit`, `google-workspace-ops`, `project-flow-ops`, and `workspace-surface-audit` round out the operator lane.
- **Media and launch tooling** — `manim-video`, `remotion-video-creation`, and upgraded social publishing surfaces make technical explainers and launch content part of the same system.
- **Framework and product surface growth** — `nestjs-patterns`, richer Codex/OpenCode install surfaces, and expanded cross-harness packaging keep the repo usable beyond Claude Code alone.
- **Itô prediction-market skill pack** — `ito-market-intelligence`, `ito-basket-compare`, `ito-trade-planner`, `ito-data-atlas-agent`, `prediction-market-oracle-research`, and `prediction-market-risk-review` add public, non-advisory market/basket workflows while keeping live Itô API access gated and separate from ECC Tools billing.
- **Optimization skill pack** — `parallel-execution-optimizer`, `benchmark-optimization-loop`, `data-throughput-accelerator`, `latency-critical-systems`, and `recursive-decision-ledger` turn repeated speed/recursion prompts into bounded benchmark, throughput, and decision-ledger workflows.
- **ECC 2.0 alpha is in-tree** — the Rust control-plane prototype in `ecc2/` now builds locally and exposes `dashboard`, `start`, `sessions`, `status`, `stop`, `resume`, and `daemon` commands. It is usable as an alpha, not yet a general release.
- **Operator status snapshots** — `ecc status --markdown --write status.md` turns the local state store into a portable handoff covering readiness, active sessions, skill-run health, install health, pending governance events, and linked work items from Linear/GitHub/handoffs. Use `ecc work-items upsert ...` for manual entries, `ecc work-items sync-github --repo owner/repo` for PR/issue queue state, and `ecc status --exit-code` to fail automation when readiness needs attention.
- **Ecosystem hardening** — AgentShield, ECC Tools cost controls, billing portal work, and website refreshes continue to ship around the core plugin instead of drifting into separate silos.