# Template — evaluator-rubric.md

**Summary** : Grille d'évaluation 6 dimensions × scoring 0-2, opérée par un evaluator (humain ou agent) **distinct** du worker. Produit un verdict Accept / Revise / Block + liste d'issues actionables. Cœur du [worker-checker-separation](worker-checker-separation.md) et de la couche **process observability** (Lecture 11).

**Sources** : `raw/ingested/template-evaluator-rubric.txt` (https://walkinglabs.github.io/learn-harness-engineering/en/resources/templates/evaluator-rubric)

**Last updated** : 2026-05-24

---

## Contenu

### Rôle

Voir [worker-checker-separation](worker-checker-separation.md) et [confidence-calibration-bias](confidence-calibration-bias.md) pour le pourquoi. Cette page = le format concret.

### Template verbatim (anglais)

À copier-coller dans `docs/evaluator-rubric.md`. À utiliser **par un evaluator distinct** (sub-agent ou humain) à chaque feature completion.

```markdown
# Evaluator Rubric

Use this rubric when reviewing a completed feature. Score each dimension 0-2.

Scoring scale:
- **0** = not addressed / failed
- **1** = partially addressed / acceptable with caveats
- **2** = fully addressed / passes cleanly

---

## Feature evaluated: [FEATURE_ID]
## Sprint contract: [SPRINT_CONTRACT_ID or N/A]
## Evaluator: [evaluator name or agent role]
## Date: [YYYY-MM-DD]

---

## 1. Correctness (Score: __ / 2)

**Question**: Does the implemented behavior match the requested feature exactly?

**Evidence to check**:
- Verification command from sprint contract: did it pass?
- Manual test of the user-facing behavior
- Edge cases mentioned in the sprint contract

**Score**:
- 0 — Behavior does not match or verification command fails
- 1 — Partial match, edge cases missed but happy path works
- 2 — Full match, edge cases handled

**Notes**: [evidence captured, specific examples]

---

## 2. Verification (Score: __ / 2)

**Question**: Is there runnable evidence the feature works?

**Evidence to check**:
- Test files written for this feature
- Test execution log
- E2E test if applicable (see `[[end-to-end-verification-only]]`)
- All 3 layers (static, runtime, system) addressed

**Score**:
- 0 — No tests, or "tests pass" with no new tests covering this feature
- 1 — Unit tests present but missing integration/E2E
- 2 — Full coverage: static + unit + integration + E2E

**Notes**: [test files, commands, output]

---

## 3. Scope Discipline (Score: __ / 2)

**Question**: Did the agent stay within the assigned feature boundary?

**Evidence to check**:
- Compare actual diff to sprint contract scope
- Check exclusions list — any violations?
- Code lines added vs estimated (excessive = scope creep)

**Score**:
- 0 — Major scope creep (touched 2+ exclusion items, refactored unrelated code)
- 1 — Minor scope creep (justified expansions, but not strictly in scope)
- 2 — Strict scope adherence

**Notes**: [git diff stats, files changed]

---

## 4. Reliability (Score: __ / 2)

**Question**: Can a fresh session continue work from repo artifacts only?

**Evidence to check**:
- `claude-progress.md` updated with this session's entry
- `feature_list.json` reflects the new state correctly
- `session-handoff.md` updated (if used)
- No silent WIP or undocumented blockers

**Score**:
- 0 — Critical artifacts missing or incoherent
- 1 — Artifacts present but partial (e.g., progress log written but `Next best step` vague)
- 2 — Full handoff readiness — [fresh-session-readability-test](fresh-session-readability-test.md) would pass

**Notes**: [specific gaps]

---

## 5. Maintainability (Score: __ / 2)

**Question**: Is the code readable, tested, and documented?

**Evidence to check**:
- Naming and structure follow project conventions
- No dead code, no `console.log`, no undocumented TODOs
- Functions appropriately sized
- Comments where non-obvious decisions are made

**Score**:
- 0 — Code is hard to read, magic numbers, no docs
- 1 — Acceptable but improvements possible
- 2 — Clean, idiomatic, self-documenting where appropriate

**Notes**: [specific examples]

---

## 6. Handoff Readiness (Score: __ / 2)

**Question**: Is the next session set up to proceed smoothly?

**Evidence to check**:
- `Next best step` in `claude-progress.md` is clear and actionable
- Dependencies for next task are met
- Any blockers explicitly noted
- `make verify` passes from clean state

**Score**:
- 0 — Next session will struggle to identify what to do next
- 1 — Direction clear but missing context or commands
- 2 — Next session can start immediately with full context

**Notes**: [Next best step content]

---

## Total Score: __ / 12

## Verdict

- **Accept** (10-12) — Work meets all standards, transition feature state to `passing`
- **Revise** (6-9) — Work has issues requiring corrections before advancing
- **Block** (0-5) — Critical issues, must be resolved before any further progress

**Verdict**: [Accept | Revise | Block]

---

## Issues Found (if any)

List each issue with severity, location, description, suggested fix:

- **CRITICAL** — src/auth/password.ts:42 — Bcrypt cost is 4 (should be ≥12 per OWASP). Fix: change to 12.
- **HIGH** — Missing E2E test for password reset flow. Fix: add tests/e2e/reset-flow.spec.ts.
- **MEDIUM** — Function `validatePassword` is 80 lines, hard to maintain. Fix: split into rule-specific helpers.
- **LOW** — Variable `tmpData` could be named `pendingResetTokens`. Fix: rename.

---

## Required corrections (for Revise verdict)

1. [Specific action item with file:line + expected behavior]
2. [Action item]

## Trigger for next review

- After corrections committed
- After [SPECIFIC_TEST] passes
```

### Les 6 dimensions

| # | Dimension | Question |
|---|-----------|----------|
| 1 | **Correctness** | Behavior match la spec ? |
| 2 | **Verification** | Evidence runnable existe ? |
| 3 | **Scope discipline** | Reste dans le scope du sprint contract ? |
| 4 | **Reliability** | Une fresh session peut reprendre ? |
| 5 | **Maintainability** | Code lisible et testé ? |
| 6 | **Handoff readiness** | Direction claire pour la suivante ? |

### Le scoring 0-2

Choix volontaire de 3 niveaux (pas 5 ou 10) :

- **0** = échec
- **1** = partiel / acceptable avec réserves
- **2** = passing clean

Plus de granularité = plus d'arbitraire. 3 niveaux force des décisions tranchées.

### Total et verdict

| Total | Verdict |
|-------|---------|
| 10-12 / 12 | **Accept** |
| 6-9 / 12 | **Revise** |
| 0-5 / 12 | **Block** |

Le verdict détermine la transition d'état :

- Accept → feature transitionne à `passing`
- Revise → reste `active`, generator corrige
- Block → escalade humaine ou redesign

### Lien avec sprint contract

L'evaluator rubric **score** la conformité au [sprint contract](sprint-contract-pattern.md). Sans sprint contract clair, le scoring est arbitraire (chaque evaluator a sa propre idée).

### Workflow

```
Generator finishes feature
    ↓
Trigger evaluator (sub-agent ou humain)
    ↓
Evaluator runs rubric — fills each dimension
    ↓
Compute total → verdict
    ↓
If Accept → mark feature passing
If Revise → feedback to generator → next iteration
If Block → escalate
```

### Implementation comme sub-agent

```yaml
# .claude/agents/evaluator.md
---
name: evaluator
description: Scores completed features using 6-dimension rubric
tools: [Read, Grep, Glob, Bash]
model: opus
---

You are an evaluator. Your mission: rigorously score completed features.

Process:
1. Read the sprint contract for the feature
2. Read all relevant files (code, tests, docs)
3. Run the verification command
4. For each of 6 dimensions, score 0/1/2 with evidence
5. Compute total and verdict
6. List issues found (severity + location + description + fix)
7. Output structured rubric markdown

Be nitpicky. Trust nothing. Verify everything.
```

### Le nitpicky checker

Voir [worker-checker-separation](worker-checker-separation.md) : le evaluator doit être **mandaté** pour trouver des défauts, pas pour confirmer. Le prompt ci-dessus le précise.

### Antipatterns

- ❌ Scoring 2/2 partout sans evidence → evaluator complaisant
- ❌ Pas de feedback actionable pour Revise → generator ne sait pas quoi corriger
- ❌ Même agent que generator → biais maximal ([confidence-calibration-bias](confidence-calibration-bias.md))
- ❌ Rubric figée sans audit → ne s'adapte pas aux apprentissages
- ❌ Verdict ignoré ("Revise mais on merge quand même") → la harness perd sa valeur

### Mise à jour de la rubric

Si le projet a des spécificités, ajouter des dimensions :

```markdown
## 7. Security (Score: __ / 2)
- Auth flows reviewed
- No secrets in logs
- Input validation
```

Ou ajuster les seuils :

```markdown
## Adjusted Scoring (for high-criticality projects)
- Accept: 12/12 strictement (pas de score 1)
- Revise: 8-11
- Block: 0-7
```

### À retenir

1. **6 dimensions**, scoring **0-2**, total /12.
2. Verdict **Accept / Revise / Block** par seuils.
3. Opéré par **evaluator distinct** (sub-agent ou humain).
4. **Issues actionables** : severity + location + fix.
5. Prompt nitpicky obligatoire pour éviter complaisance.

## Related pages

- [worker-checker-separation](worker-checker-separation.md)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md)
- [sprint-contract-pattern](sprint-contract-pattern.md)
- [confidence-calibration-bias](confidence-calibration-bias.md)
- [three-layer-termination-validation](three-layer-termination-validation.md)
- [observability-runtime-vs-process](observability-runtime-vs-process.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
