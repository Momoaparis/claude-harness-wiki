# 📖 Usage Guide — LLM Wiki

> How to read, navigate, and work with this knowledge base — and how to evolve your own copy.

---

## Table of Contents

1. [Opening with Obsidian](#-opening-with-obsidian-recommended)
2. [Reading in your browser (Chrome translation)](#-reading-without-obsidian)
3. [Using as AI context](#-using-as-ai-context-the-power-move)
4. [Using as a work tool](#-using-as-a-work-tool)
5. [Evolving your own copy](#-evolving-your-own-copy)
6. [Ingesting new documents](#-ingesting-new-documents)

---

## 🟣 Opening with Obsidian (recommended)

[Obsidian](https://obsidian.md) is a free markdown editor that understands `[[wiki-links]]` and can display the knowledge graph visually.

### Setup (2 minutes)

1. Download and install [Obsidian](https://obsidian.md) (free, Windows/Mac/Linux)
2. Open Obsidian → **Open folder as vault**
3. Select the `llm-wiki` folder you cloned
4. Click the graph icon (🕸️) in the left sidebar → **Graph View**

### What you get

```
┌─────────────────────────────────────────────────┐
│  🕸️ Graph View                                  │
│                                                  │
│    ● harness-definition                          │
│         ↓                                        │
│    ● five-subsystem-harness ←→ ● session-handoff │
│         ↓                          ↓             │
│    ● agent-memory    ←→    ● progress-file       │
│                                                  │
│  Click any node → opens the page                 │
│  Zoom/pan to explore the full graph              │
└─────────────────────────────────────────────────┘
```

**Tip:** Start with `wiki/index.md` — it's the table of contents, organized by theme.

### Navigation shortcuts

| Action | Shortcut |
|---|---|
| Open a linked page | Click the `[[link]]` |
| Back | Alt + ← |
| Open graph view | Ctrl + G |
| Quick search | Ctrl + O |

---

## 🌐 Reading without Obsidian

Any markdown file can be read in Chrome directly:

1. Open Chrome
2. Drag and drop any `.md` file into Chrome (or use File → Open)
3. Click the **three dots** (⋮) in the top right corner
4. Click **Translate to English** (or your language)

> **Note:** `[[wiki-links]]` won't be clickable in the browser. For navigation, use Obsidian or any markdown editor.

---

## 🤖 Using as AI context (the power move)

**You don't need to read this wiki yourself.** The real power is giving it to an AI.

### Pattern 1 — Ask a question

```
You: Read wiki/index.md and identify the relevant pages,
     then answer: What is a harness in Claude Code
     and why does it matter?

AI: [reads index, reads harness-definition-et-philosophie.md,
     reads five-subsystem-harness-architecture.md]
    → gives you a precise answer with citations
```

### Pattern 2 — Get a summary of a theme

```
You: Read all pages under the "Harness Engineering" section
     of wiki/index.md and give me a 5-bullet executive summary.
```

### Pattern 3 — Feed pages as system prompt

Copy the content of one or several wiki pages into your AI's system prompt or first message. The AI then has specialized knowledge for your session:

```
[Paste content of wiki/five-subsystem-harness-architecture.md]
[Paste content of wiki/harness-definition-et-philosophie.md]

Now: help me design the harness for my Python project.
```

---

## 🛠️ Using as a work tool

This is **not just a study resource**. It's operational knowledge that AI can act on.

### Real-world example

> Instead of reading harness documentation yourself and manually setting up files, you can:

```
You: Read wiki/five-subsystem-harness-architecture.md,
     wiki/template-claude-md.md, wiki/template-session-handoff-md.md,
     and wiki/startup-readiness-checklist.md.

     Then create a minimum viable harness structure for my project
     at /path/to/my/project, following the patterns described.

AI: [reads → understands → creates CLAUDE.md, session-handoff template,
     checklist, folder structure — all based on the wiki's knowledge]
```

### More examples

| Goal | Wiki pages to provide |
|---|---|
| Set up Claude Code hooks | `claude-code-hooks.md`, `memory-persistence-hooks.md` |
| Optimize token usage | `ecc-token-optimization.md`, `modular-codebase-tokens.md`, `mgrep-vs-grep.md` |
| Design a multi-agent pipeline | `subagent-architecture.md`, `planner-generator-evaluator-3-agent-architecture.md` |
| Secure an agentic system | `claude-code-cves-2026.md`, `agent-sandboxing.md`, `prompt-injection-sanitization.md` |
| Run evaluations | `grader-types.md`, `pass-at-k-metric.md`, `eval-roadmap.md` |

**The workflow:** AI reads → AI understands → AI does the work → you review.

---

## 🌱 Evolving your own copy

This wiki is designed to grow with you. You can add new pages, ingest new documents, and run audits — all using Claude Code.

### Step 1 — Activate Claude Code as wiki maintainer

The file `CLAUDE.template.md` contains the instructions that tell Claude how to maintain this wiki. To activate it:

1. **Rename** `CLAUDE.template.md` → `CLAUDE.md`
   ```bash
   mv CLAUDE.template.md CLAUDE.md
   ```

2. **Customize the paths** inside `CLAUDE.md`:
   - If you use OneDrive for mobile capture: replace `<YOUR_USERNAME>` with your actual Windows username
   - If you don't use OneDrive: you can ignore the "Workflow mobile" section and drop files directly into `raw/inbox/`

3. Open Claude Code in the `llm-wiki` folder:
   ```bash
   cd /path/to/llm-wiki
   claude
   ```

Claude will automatically read `CLAUDE.md` and understand its role as wiki maintainer.

### Step 2 — Explore what's there

Ask Claude:
```
Read wiki/index.md and give me an overview of what topics are covered.
```

### Step 3 — Start adding your own knowledge

See [Ingesting new documents](#-ingesting-new-documents) below.

---

## 📥 Ingesting new documents

When you find a useful article, video, or document, you can add it to the wiki using Claude Code.

### Supported formats

| Format | How to capture |
|---|---|
| `.md` | Save with [Markdownload](https://chromewebstore.google.com/detail/markdownload/pcmpcfapbekmbjjkdalcgopdkipoggdi) Chrome extension |
| `.txt` | Copy-paste the text |
| `.pdf` | Save the PDF directly |
| YouTube URL | Paste the URL into a `.md` file |
| Web article URL | Paste the URL into a `.md` file |

### Ingestion workflow

1. **Drop the file** into `raw/inbox/`

2. **Open Claude Code** in the wiki folder and say:
   ```
   Ingest the new file in raw/inbox/
   ```

3. **Claude will:**
   - Read the document completely
   - Extract key concepts, definitions, entities, and relationships
   - **Propose a structuring plan — and wait for your approval**
   - Create 5–15 wiki pages from a single document (this is normal)
   - Link all new pages to existing concepts via `[[wiki-links]]`
   - Update `wiki/index.md`
   - Archive the source to `raw/ingested/`

4. **You review and approve** at each step — Claude never writes without asking first.

### Tips

- **One document = multiple pages.** A 20-page article might generate 10–15 wiki pages. Each page covers one atomic concept. This is by design.
- **Batch thematic documents.** If you have 3 articles on the same topic, ingest them together to avoid fragmentation.
- **YouTube works.** Claude can fetch transcripts. Just paste the URL into a `.md` file and drop it in `raw/inbox/`.

---

## 🔍 Auditing the wiki

Over time, pages can become orphaned or inconsistent. Claude can audit the wiki:

```
Audit the wiki and find:
- orphaned pages (no links pointing to them)
- broken [[wiki-links]]
- concepts mentioned without a dedicated page
- pages that don't follow the standard format
```

Claude will return a numbered report with corrections proposed — but will not auto-fix without your approval.

---

## 💡 Philosophy

> This wiki is not a book to read from cover to cover.
> It is a **living memory** that grows with you — and that AI can access on your behalf.
>
> The goal: when you need to know something or do something, you ask an AI to consult the wiki and act. You stay in control; the AI does the reading and the work.

---

*For sources and disclaimer, see [README.md](README.md#-sources).*
