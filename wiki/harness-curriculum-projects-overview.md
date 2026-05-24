# Curriculum projects (P01-P06) — overview

**Summary** : 6 projets hands-on du cours Learn Harness Engineering. Progression : P01 baseline → P02 readable workspace → P03 multi-session continuity → P04 runtime feedback → P05 role separation → P06 capstone avec ablation study. Chaque projet ajoute une capacité orthogonale à la harness. À refaire chez soi pour internaliser.

**Sources** : `raw/ingested/project-01-prompt-only-vs-rules-first.txt` à `project-06-runtime-observability-and-debugging.txt`

**Last updated** : 2026-05-24

---

## Contenu

### Architecture pédagogique

Chaque projet a deux dossiers :

- `starter/` — état initial avec harness faible (à refaire toi-même)
- `solution/` — état cible avec harness complète (pour comparaison)

Tu lances un agent (Claude Code / Codex) sur le `starter/` et tu mesures combien de features il complète. Puis tu progresses vers la `solution/`.

### Projet 01 — Prompt-Only vs Rules-First

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-01-baseline-vs-minimal-harness/

**Objectif** : démontrer empiriquement que les harness artifacts améliorent les outcomes.

**Tâche concrète** : Electron knowledge-base app (window launch, doc list, Q&A panel, local data dir).

**Comparaison** :

| Setup | Artefacts |
|-------|-----------|
| `starter/` | Juste `task-prompt.md` |
| `solution/` | `AGENTS.md` + `init.sh` + `feature_list.json` + `CLAUDE.md` + `claude-progress.md` |

**Mesures** : taux de complétion des 4 features, durée totale.

**Takeaway** : harness artifacts **améliorent tangiblement** les outcomes même sur un projet petit.

**Concepts couverts** : [[five-subsystem-harness-architecture]], [[template-claude-md]], [[feature-list-as-primitive]].

**Estimation** : 1-2 heures.

---

### Projet 02 — Agent-Readable Workspace

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-02-agent-readable-workspace/

**Objectif** : transformer un workspace faiblement documenté en espace lisible par l'agent **sur plusieurs sessions**.

**Tâche concrète** : 3 features (document import, document detail view, local persistence).

**Artefacts clés ajoutés** :
- `ARCHITECTURE.md`
- `PRODUCT.md`
- `session-handoff.md`

**Critère de succès** : une **fresh session** peut reprendre depuis le repo seul ([[fresh-session-readability-test|fresh session test]]).

**Takeaway** : le repo peut être [[repository-as-system-of-record|single source of truth]].

**Concepts couverts** : [[repository-as-system-of-record]], [[fresh-session-readability-test]], [[template-session-handoff-md]].

**Estimation** : 2-3 heures.

---

### Projet 03 — Multi-Session Continuity

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-03-multi-session-continuity/

**Objectif** : ajouter mécanismes pour que l'agent continue entre restarts **sans dérive de features**.

**Tâche concrète** : 4 features (document chunking, metadata extraction, indexing status UI, grounded Q&A with citations).

**Artefacts clés ajoutés** :
- `clean-state-checklist.md` (voir [[template-clean-state-checklist]])
- Verification gates dans `feature_list.json`
- Scope control explicite

**Critère de succès** : "one feature at a time, no marking pass without verification evidence" ([[wip-limit-discipline]] + [[completion-evidence-executable]]).

**Takeaway** : la continuité multi-session demande des **gates structurels**, pas juste de la discipline.

**Concepts couverts** : [[cross-session-context-loss]], [[wip-limit-discipline]], [[completion-evidence-executable]].

**Estimation** : 3-4 heures.

---

### Projet 04 — Incremental Indexing & Runtime Feedback

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-04-incremental-indexing/

**Objectif** : focus sur **observabilité runtime** + contraintes architecturales.

**Tâche concrète** : continuer le knowledge-base, avec un bug seed dans le chunking large-file.

**Artefacts clés ajoutés** :
- `logger.ts` (structured logging service)
- `check-architecture.sh` (boundary validation)
- `ARCHITECTURE.md` enrichi

**Mesure** : temps pour résoudre le bug **avec** vs **sans** diagnostic infrastructure.

**Takeaway** : logs + guardrails permettent à l'agent de **self-correct** beaucoup plus vite que l'exploration brute.

**Concepts couverts** : [[observability-runtime-vs-process]], [[architectural-boundary-enforcement]], [[agent-observability]].

**Estimation** : 2-3 heures.

---

### Projet 05 — Role Separation & Self-Verification

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-05-grounded-qa-verification/

**Objectif** : démontrer l'impact de la **séparation des rôles** agent.

**Tâche concrète** : multi-turn Q&A conversation history.

**3 variants à comparer** :

| Variant | Score (sur 5) |
|---------|---------------|
| `single-role/` (agent seul) | **1.6** |
| `gen-eval/` (Generator + Evaluator) | **3.3** |
| `plan-gen-eval/` (Planner + Generator + Evaluator) | **4.9** |

**Takeaway** : role separation = **+3x** sur la qualité. La feature constante (Q&A) isole role separation comme **seule variable**.

**Concepts couverts** : [[planner-generator-evaluator-3-agent-architecture]], [[worker-checker-separation]], [[confidence-calibration-bias]].

**Estimation** : 2-3 heures.

---

### Projet 06 — Runtime Observability and Debugging (Capstone)

**Lien** : https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-06-runtime-observability-and-debugging/

**Objectif** : intégrer **tous les 5 projets précédents** en harness complète + faire une **ablation study**.

**Tâche concrète** : projet final reprenant la knowledge-base, avec full harness.

**Composants harness** :
- `AGENTS.md`, `CLAUDE.md`
- `feature_list.json`, `init.sh`
- `session-handoff.md`, `clean-state-checklist.md`
- docs/, evaluator rubrics
- Benchmark/cleanup scripts

**Ablation study** :

```
1. Run baseline (weak harness) → mesurer
2. Run full harness → mesurer
3. Désactiver feature_list.json → mesurer delta
4. Désactiver session-handoff.md → mesurer delta
5. Désactiver autres composants un par un
6. Identifier critical vs nice-to-have
```

Voir [[ablation-study-methodology]].

**Takeaway** : tu sais maintenant **lequel** de tes composants harness importe vraiment dans **ton** contexte.

**Concepts couverts** : tous les précédents + [[ablation-study-methodology]].

**Estimation** : 4-6 heures.

---

### Progression mapping

| Projet | Lecture(s) corollaire(s) | Capacité ajoutée |
|--------|--------------------------|------------------|
| P01 | L01, L02 | Artefacts de base (subsystèmes) |
| P02 | L03, L04 | Repo lisible (workspace as SSoT) |
| P03 | L05, L07, L08 | Continuité (WIP=1, feature lists) |
| P04 | L10, L11 | Observabilité + boundaries |
| P05 | L09 | Role separation |
| P06 | L02, L12 | Synthèse + ablation |

### Comment refaire chez soi

#### Setup

1. Cloner le repo du cours (lien à venir, ou récréer la structure)
2. Pour chaque projet :
   - Lire le brief
   - Travailler dans `starter/`
   - Comparer avec `solution/` après

#### Mesures à logger

- Temps total par projet
- Taux de features complétées
- Nombre d'iterations Generator ↔ Evaluator
- VCR final (voir [[verified-completion-rate-metric]])

#### Itération

Refaire un projet avec une harness customisée pour **ton** workflow. C'est le vrai apprentissage.

### Le pattern de progression

Chaque projet ajoute **une seule capacité** orthogonale :

```
P01 : structure
P02 : readability
P03 : continuity
P04 : observability
P05 : role separation
P06 : integration + ablation
```

Cette progression est **transférable** à n'importe quel projet : commencer par P01, puis ajouter une capacité par sprint.

### Concepts transverses

- [[five-subsystem-harness-architecture]] couvert sur les 6 projets
- [[feature-list-as-primitive]] dès P01
- [[worker-checker-separation]] introduit en P05
- [[ablation-study-methodology]] introduit en P06

### À retenir

1. **6 projets**, progression linéaire de capacités.
2. Chaque projet a `starter/` (faible) et `solution/` (cible) pour comparaison.
3. P05 démontre **+3x score** par role separation.
4. P06 est l'**ablation study** : tu sauras lesquels de tes composants importent vraiment.
5. À **refaire chez soi**, pas juste lire.

## Related pages

- [[ablation-study-methodology]]
- [[five-subsystem-harness-architecture]]
- [[planner-generator-evaluator-3-agent-architecture]]
- [[the-harness-engineering-curriculum-summary]]
