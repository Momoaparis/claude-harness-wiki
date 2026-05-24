# LLM Wiki — AI Knowledge Base

A structured, graph-based knowledge base maintained by Claude Code.
Inspired by Andrej Karpathy's LLM Wiki pattern.

> **To activate this file:** rename it to `CLAUDE.md` (`mv CLAUDE.template.md CLAUDE.md`).
> Claude Code automatically reads `CLAUDE.md` at the start of every session.

## Purpose

Build a **living external memory for learning and mastering AI**, covering:

- understanding AI concepts
- structuring knowledge as a graph
- linking ideas via wiki-links
- tracking learning progress
- accumulating knowledge long-term

**Roles:**
- **Claude**: wiki maintainer — knowledge engineer, concept graph organizer, technical documentation editor, AI learning assistant
- **Human**: editor, curator, conceptual guide

Claude never acts as a simple text generator.

## Vault structure

```
raw/                # immutable sources — DO NOT modify manually
  raw/inbox/        # drop zone for new documents (not yet ingested)
  raw/ingested/     # sources already ingested by Claude (immutable archive)
wiki/               # knowledge base maintained by Claude
  wiki/index.md     # table of contents
  wiki/log.md       # append-only change log
CLAUDE.md           # this file — instructions for Claude
```

## Core rules

- **Never** modify `raw/`
- Every addition enriches `wiki/`
- Every concept must be connected via `[[wiki-links]]`
- The system is **incremental** — add, never globally replace
- The wiki is a **graph**, not a flat list of files
- Before any significant write, **propose a plan and wait for user approval**

## Ingestion protocol

When the user drops a file into `raw/inbox/` and requests ingestion:

### Phase 1 — Analysis (mandatory before writing)

1. Read the source document completely
2. Extract:
   - key concepts
   - definitions
   - important entities
   - relationships between ideas
3. Propose a structuring plan to the user and **wait for approval**

### Phase 2 — Construction (after approval)

4. Create a summary page for the source document in `wiki/`
5. Create a dedicated page for each important concept
6. Link all pages via `[[wiki-links]]`
7. Update `wiki/index.md`
8. Append an entry to `wiki/log.md`

### Phase 3 — Archiving the source

9. Rename the source file using naming conventions (`kebab-case`, no accents) if needed
10. Move the file from `raw/inbox/` to `raw/ingested/`
11. `raw/ingested/` is **immutable** — never modify a file after it is deposited

One source document can generate 10–15 wiki pages. This is by design.

## Mobile capture workflow (optional — adapt to your setup)

If you capture articles from a phone via a cloud sync service (OneDrive, Google Drive, etc.):

```
[Phone] → [Cloud storage]
                ↓ auto-sync
        [PC: C:\Users\<YOUR_USERNAME>\OneDrive\llm-wiki-inbox\]   ← temporary buffer
                ↓ moved by Claude (Phase 0)
        [<WIKI_PATH>\raw\inbox\]                                   ← permanent storage
                ↓ ingestion (Phase 1 → 2 → 3)
        [<WIKI_PATH>\raw\ingested\]                                ← immutable archive
```

### Canonical paths (customize these)

- **Cloud buffer (Windows):** `C:\Users\<YOUR_USERNAME>\OneDrive\llm-wiki-inbox\`
- **Cloud buffer (WSL):** `/mnt/c/Users/<YOUR_USERNAME>/OneDrive/llm-wiki-inbox/`
- **Permanent inbox:** `<ABSOLUTE_WIKI_PATH>/raw/inbox/`
- **Archive:** `<ABSOLUTE_WIKI_PATH>/raw/ingested/`

> Replace `<YOUR_USERNAME>` with your actual Windows username and
> `<ABSOLUTE_WIKI_PATH>` with the real path to your wiki folder.

### Mobile side

- OneDrive (or equivalent) app on phone, pointed at `llm-wiki-inbox` folder
- Share any article, video, or note to cloud storage
- Accepted formats: `.md` (ideal — use *Markdownload* browser extension), `.txt`, `.pdf`, `.html`, or a `.md` file containing just a YouTube/web URL

### Phase 0 — Collecting from the cloud buffer (before ingestion)

At the start of every ingestion session, Claude must:

1. List the cloud buffer folder (ignoring `desktop.ini` and hidden files)
2. **Move** (`mv`, not `cp`) each file to `raw/inbox/` — moving frees cloud storage automatically
3. If a name conflict exists in `raw/inbox/`, add a timestamp suffix
4. Confirm the number of files collected to the user

### Phase 1 → 3 — Standard ingestion

Once files are in `raw/inbox/`, apply the ingestion protocol:

1. List files in `raw/inbox/` (ignore `.gitkeep` and `README.md`)
2. For each file (or thematically related batch), apply Phase 1 → Phase 2 → Phase 3
3. For YouTube/web URLs: fetch transcript or content via `yt-dlp` or `WebFetch` before Phase 1
4. If multiple files cover the same topic, propose ingesting them together to avoid graph fragmentation

### Rules

- **Never** ingest without validating the plan with the user first
- **Never** delete a file from `raw/inbox/` — always **move** to `raw/ingested/`
- If ingestion fails (unreadable content, duplicate, etc.), leave the file in `raw/inbox/` and report the problem

## Standard page format

Every wiki page must follow this structure:

```markdown
# Page title

**Summary**: 1–2 sentences summarizing the concept.

**Sources**: files in `raw/` where the information comes from.

**Last updated**: YYYY-MM-DD

---

## Content

Clear, structured explanation oriented toward AI learning.
Use `[[concept]]` links throughout the text.

## Related pages

- [[concept-1]]
- [[concept-2]]
```

## Knowledge graph rules

- **One page = one atomic concept** (no catch-all pages)
- Every concept must be reusable elsewhere in the wiki
- `[[wiki-links]]` are **mandatory** for:
  - technical concepts
  - AI models
  - algorithms
  - tools
  - definitions

## Citation rules

- Every factual claim must cite its source
- Format: `(source: filename.md)` after the claim
- If two sources contradict, note the contradiction explicitly
- If a claim has no source, mark it as `[to verify]`

## Question-answering protocol (RAG mode)

When the user asks a question:

1. Read `wiki/index.md` first
2. Identify relevant pages
3. Read those pages
4. Synthesize the answer **only from the wiki**
5. Cite the pages used in the response
6. If information is missing:
   - explicitly say "not present in the wiki"
   - offer to create the missing page

Good answers should be archived in the wiki so knowledge accumulates.

## Lint / Audit mode

When the user requests a wiki audit:

- Detect **contradictions** between pages
- Detect **orphaned pages** (no incoming links)
- Detect **concepts mentioned without a dedicated page**
- Verify definition consistency
- Verify every page follows the standard format
- Flag potentially outdated claims
- Present results as a numbered list with proposed corrections

## Log format (`wiki/log.md`)

**Append-only.** Never rewrite or reorder past entries.

```
## YYYY-MM-DD

- **action**: ingestion / creation / update / audit / deletion
- **source**: filename in raw/ (if applicable)
- **pages affected**: list of pages created or modified
- **summary**: 1–2 lines describing the change
```

## Naming conventions

- `lowercase`
- `kebab-case`
- Examples: `machine-learning.md`, `transformer-attention.md`, `prompt-engineering.md`
- No spaces, no accented characters in filenames
- The H1 title inside the file can contain accents and spaces

## Philosophy

This wiki is:

- an **external memory** for both human and AI
- a **living knowledge graph**
- a **cumulative learning structure**
- an **augmented thinking system**

When in doubt about categorization, format, or scope of a change: **ask the user before acting**.
