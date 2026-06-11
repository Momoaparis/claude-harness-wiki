# 🧠 LLM Wiki — AI Knowledge Base

> A structured, graph-based knowledge base about AI, Claude Code, and agentic systems — maintained by Claude Code itself.
> **110+ pages in French** | Built with Obsidian | Powered by Claude

---

## 🌍 Language note

All wiki pages are written in **French**. You do not need to speak French to use this knowledge base:

- Open any page in **Chrome**, click the three dots (⋮) → **Translate to English**
- Or paste the content into any AI and ask it to translate

The AI-centric usage patterns described below work in any language.

---

## 🤔 What is this?

This is a personal knowledge base inspired by [Andrej Karpathy's LLM Wiki pattern](https://karpathy.ai), built and maintained with **Claude Code** as the knowledge engineer.

It covers:

- 🤖 **Agentic AI systems** — harnesses, agents, orchestration
- 🧩 **Claude Code** — hooks, commands, plugins, memory, optimization
- 🔐 **Agentic security** — CVEs, sandboxing, prompt injection
- 🏗️ **Harness engineering** — pipeline design, session continuity, verification
- 🧪 **Evaluation methodology** — graders, pass@k, ablation studies
- 🎨 **AI creative tools** — design agents, video generation

---

## 🗂️ Structure

```
llm-wiki/
├── wiki/                    ← 110+ knowledge pages (the core)
│   ├── index.md             ← table of contents — start here
│   ├── templates/           ← ready-to-use harness templates
│   └── *.md                 ← one file = one atomic concept
├── raw/
│   └── ingested/            ← original source documents (open-source)
├── CLAUDE.template.md       ← Claude Code instructions (rename to CLAUDE.md)
└── README.md                ← this file
```

---

## 📊 Knowledge Graph

This is not a flat list of files. Every concept links to others via standard Markdown links (`[concept](concept.md)`):

```
harness-definition
    ↓
five-subsystem-harness-architecture ←→ harness-entropy-management
    ↓                                          ↓
session-clean-handoff            agent-memory-hygiene
    ↓
progress-file-pattern ←→ strategic-compact ←→ cross-session-context-loss
```

Best explored visually in **Obsidian Graph View** — see [USAGE.md](USAGE.md).

---

## 🚀 Three ways to use this

### 1. 📖 Study mode
Open in Obsidian, click the graph icon, navigate concepts visually. Use Chrome translation for French pages.

### 2. 🤖 AI-context mode (recommended)
Give the wiki pages to an AI as context. Instead of reading yourself:
> *"Read wiki/index.md and the relevant pages, then answer: what is a harness in Claude Code?"*

### 3. 🛠️ Work tool mode (most powerful)
Feed wiki pages to an AI to perform real tasks:
> *"Read wiki/five-subsystem-harness-architecture.md and wiki/harness-definition-et-philosophie.md, then set up a minimum viable harness structure for my project."*

The AI reads → understands → acts. You don't need to read anything.

---

## 📚 Topics at a glance

| Theme | Pages | Example concepts |
|---|---|---|
| 🏗️ Harness Engineering | 15+ | `five-subsystem-harness-architecture`, `harness-rot-et-dette-technique`, `session-clean-handoff` |
| 🔧 Skills | 8+ | `skill-anatomy`, `skill-creation-workflow`, `skill-creator-meta-skill`, `skill-description-optimization`, `skill-eval-workflow` |
| 🧠 Memory & Context | 10+ | `session-storage-pattern`, `strategic-compact`, `cross-session-context-loss` |
| 🪝 Hooks & Commands | 8+ | `claude-code-hooks`, `claude-code-commands`, `memory-persistence-hooks` |
| 🔐 Agentic Security | 10+ | `claude-code-cves-2026`, `agent-sandboxing`, `prompt-injection-sanitization` |
| 🧪 Evaluation | 8+ | `grader-types`, `pass-at-k-metric`, `checkpoint-vs-continuous-evals` |
| 💰 Token Optimization | 6+ | `ecc-token-optimization`, `modular-codebase-tokens`, `mgrep-vs-grep` |
| 🤖 Agent Architecture | 12+ | `subagent-architecture`, `planner-generator-evaluator-3-agent-architecture`, `agent-identity-separation` |
| 🧰 Agentic Frameworks | 6+ | `superpowers-framework-summary`, `superpowers-workflow-pipeline`, `subagent-driven-development`, `ecc-overview`, `ecc-control-pane-substrate`, `ecc-orchestrator-family` |

---

## ⚙️ Evolve your own copy

This wiki is designed to grow. See [USAGE.md → Evolving the Wiki](USAGE.md#-evolving-your-own-copy) for:
- How to set up Claude Code as your wiki maintainer
- How to ingest new documents (articles, YouTube videos, PDFs)
- How to run audits and detect broken links

---

## 📖 Sources

This knowledge base was built from the following open-source resources:

- **Affaan Mustafa** — *The Shorthand Guide to Everything Claude Code* (Sep 2025)
- **Affaan Mustafa** — *The Longform Guide to Everything Claude Code* (Jan 2026)
- **Affaan Mustafa** — *The Shorthand Guide to Everything Agentic Security* (Feb 2026)
- **Affaan Mustafa** — *ECC Ecosystem Documentation* (ecosystem, hooks, skills, agents) — incl. *ECC v2.0.0 release notes* (the agent harness operating system, Jun 2026)
- **obra (Jesse Vincent)** — *[Superpowers](https://github.com/obra/superpowers)* — agentic skills framework & software development methodology
- **Learn Harness Engineering** — *12 Lectures + 6 Projects + 7 Templates* ([walkinglabs](https://github.com/walkinglabs/learn-harness-engineering))
- **Lovart** — AI design pipeline documentation (brand kit, video generation)

---

## ⚠️ Disclaimer

> All content in this knowledge base was compiled from **publicly available open-source resources** on the internet. It is provided as-is, for educational and productivity purposes only.
>
> Information may be incomplete, outdated, or inaccurate. Always verify critical information against official documentation. **The author declines all responsibility** for any use made of this content.
>
> This repository does not claim ownership of the original source materials. All credits go to their respective authors.

---

## 📄 License

Content is compiled from open-source materials. See [Disclaimer](#️-disclaimer) above.
