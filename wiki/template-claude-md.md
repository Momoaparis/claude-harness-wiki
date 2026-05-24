# Template — CLAUDE.md (root instructions)

**Summary** : Fichier d'instructions racine pour Claude Code. Définit les séquences de démarrage, les contraintes d'opération (single-feature focus, complétude avant clôture), les artefacts requis, et le protocole de clôture. Variant équivalent : `AGENTS.md` pour Codex/OpenAI.

**Sources** : `raw/ingested/template-claude-md.txt` (https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/CLAUDE), `raw/ingested/template-agents-md.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Rôle dans la harness

Voir [[five-subsystem-harness-architecture|subsystème Instructions]]. C'est le fichier que l'agent lit en premier, en **chaque** session. Doit être **court** (50-200 lignes max — voir [[modular-instruction-architecture]]).

### Template verbatim (anglais)

À copier-coller dans `CLAUDE.md` à la racine du repo et adapter aux placeholders `[YOUR_*]`.

```markdown
# CLAUDE.md

## Key Operating Principles

Confirm location, review progress notes, check feature lists, examine recent commits,
run initialization, validate baseline functionality.

## Startup Sequence

1. Verify working directory: `pwd` should match `[ROOT_DIRECTORY]`
2. Read `claude-progress.md` for current state and last session summary
3. Read `feature_list.json` to identify active feature
4. Examine recent commits: `git log --oneline -10`
5. Run initialization: `[STARTUP_PATH]` (e.g., `./init.sh` or `make setup`)
6. Validate baseline: `[VERIFICATION_PATH]` (e.g., `make verify`)

## Core Work Methodology

**One active feature at a time.**

Work must include runnable evidence rather than claims alone.
Tests should be preserved, not weakened to appear complete.

- Pick a single task from `feature_list.json` (status: `not_started` → `active`)
- Implement strictly within scope
- Write/update tests covering the verification command
- Run verification: must exit 0
- Transition state to `passing` only after verification succeeds
- Commit atomically

## Documentation Requirements

Four critical files must exist and be kept up to date:

- `feature_list.json` — machine-readable task list with states
- `claude-progress.md` — session log (append-only entries)
- `init.sh` — standardized startup procedures
- `session-handoff.md` — condensed handoff (optional, when context dense)

## Handoff Protocol (End of Session)

Before stopping work:

- Update `claude-progress.md` with today's session entry
- Document feature states in `feature_list.json`
- Record remaining issues / known risks
- Commit all changes (git status must be clean)
- Establish clear restart conditions in `Next best step`

## Framework Emphasis

Reliable completion, continuity across sessions, and explicit verification over speed.
Repository artifacts serve as the authoritative record, not claims or rewritten documentation.

## Hard Constraints (NEVER violate)

1. Never mark a task as `passing` without exiting 0 on the verification command.
2. Never start a new task while another is `active` (WIP=1).
3. Never commit broken tests or failing builds.
4. Never modify `feature_list.json` to bypass verification gates.
5. [ADD PROJECT-SPECIFIC CONSTRAINTS HERE]

## Topic Documents

For details, see:

- `docs/architecture.md` — system layers and boundaries
- `docs/conventions.md` — naming, formatting, style
- `docs/[YOUR_TOPIC_DOC].md`
```

### Placeholders à remplir

| Placeholder | Remplacer par |
|-------------|---------------|
| `[ROOT_DIRECTORY]` | Chemin absolu du repo |
| `[STARTUP_PATH]` | Commande d'init (`./init.sh`, `make setup`, etc.) |
| `[VERIFICATION_PATH]` | Commande de vérif (`make verify`, `npm run check`) |
| `[CURRENT_FEATURE]` | Optionnel, peut être en `feature_list.json` à la place |
| `[ADD PROJECT-SPECIFIC CONSTRAINTS HERE]` | 3-5 hard constraints spécifiques |

### Variant Codex/OpenAI : AGENTS.md

Pour les workflows Codex / Cursor / autres outils non-Claude, le même contenu va dans `AGENTS.md`. Les deux peuvent coexister dans un même repo si l'équipe utilise plusieurs outils.

Différence pratique : Claude Code lit `CLAUDE.md` par défaut, les outils OpenAI lisent `AGENTS.md`. Le **contenu** est essentiellement identique.

### Articulation avec les autres templates

```
CLAUDE.md
├─ référence ─► feature_list.json (machine-readable tasks)
├─ référence ─► claude-progress.md (session log)
├─ référence ─► init.sh (startup script)
└─ référence ─► session-handoff.md (optional condensed handoff)
```

CLAUDE.md = entry point. Les autres = artefacts spécifiques.

### Critère de qualité du CLAUDE.md

Si une **session fresh** ne peut pas répondre aux [[fresh-session-readability-test|5 questions]] (What / How org / How run / How verify / Where now) après avoir lu seulement le `CLAUDE.md` + les fichiers référencés → le `CLAUDE.md` est incomplet.

### Antipatterns

- ❌ `CLAUDE.md` à 600 lignes → [[lost-in-the-middle-effect]] garanti
- ❌ Mélange hard constraints + soft guidelines sans distinction
- ❌ Pas de référence à `feature_list.json` → l'agent invente sa todo
- ❌ Pas de startup sequence claire → diagnostic à chaque session
- ❌ Hard constraints vagues ("write good code") → pas applicable

### Évolution

Le `CLAUDE.md` doit être versionné comme du code :

- Updates committés avec message explicite
- Review en code review comme le code
- Pas de "tweak pendant la session" sans commit

### À retenir

1. Court (**50-200 lignes max**), routing-oriented.
2. **Startup + Methodology + Documentation + Handoff** = 4 sections-clés.
3. **Hard constraints** explicites, **soft guidelines** dans topic docs.
4. Variant `AGENTS.md` pour Codex — même contenu, autre nom.
5. Audit via [[fresh-session-readability-test]].

## Related pages

- [[template-claude-progress-md]]
- [[template-feature-list-json]]
- [[template-session-handoff-md]]
- [[template-clean-state-checklist]]
- [[modular-instruction-architecture]]
- [[fresh-session-readability-test]]
- [[the-harness-engineering-curriculum-summary]]
