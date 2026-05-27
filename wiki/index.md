# Index du Wiki

**Summary** : Table des matières de la base de connaissances. Mise à jour à chaque ingestion ou création de page.

**Last updated** : 2026-05-27

---

## Sources résumées

- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md) — Claude Opus 4.7 + Lovart : pipeline brand design complet via Chrome MCP (Brand Kit, police, PSD, Skill, vidéo)

- [the-shorthand-guide-summary](the-shorthand-guide-summary.md) — Guide shorthand d'Affaan Mustafa sur Claude Code (sep 2025) — setup de base
- [the-longform-guide-summary](the-longform-guide-summary.md) — Guide longform d'Affaan Mustafa sur Claude Code (jan 2026) — techniques avancées
- [the-agentic-security-summary](the-agentic-security-summary.md) — Guide shorthand d'Affaan Mustafa sur la sécurité des agents (fév 2026) — CVEs Claude Code + standards opsec 2026
- [ecc-overview](ecc-overview.md) — Écosystème ECC (Affaan Mustafa) : skills, agents, hooks, rules + tooling (AgentShield, instincts)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md) — Cours Learn Harness Engineering : 12 lectures + 6 projets + 7 templates pour construire des harnesses Claude Code/Codex robustes
- [harness-creator-et-skill-creator-summary](harness-creator-et-skill-creator-summary.md) — harness-creator (walkinglabs) + skill-creator (Anthropic) : outils complémentaires pour scaffolding de harness et création de skills

## Pages par thème

### 🎨 Design IA & outils créatifs

- [ai-design-agent](ai-design-agent.md) — Design Agent vs text-to-image : pipeline complet (Brand Kit + police + PSD + Skill + vidéo)
- [lovart-brand-kit](lovart-brand-kit.md) — Brand Kit Lovart : PDF → schéma structuré de marque (couleurs, logos, philosophie)
- [ai-font-generator](ai-font-generator.md) — Font Generator Lovart : police typographique custom depuis description texte (~3 min)
- [prompt-as-asset](prompt-as-asset.md) — Prompt-as-asset vs prompt-as-craft : conversations réussies → skills réutilisables
- [seedance-video-gen](seedance-video-gen.md) — Seedance 2.0 : génération vidéo text-to-video courte intégrée à Lovart

### 🧠 Gestion mémoire & contexte

- [session-storage-pattern](session-storage-pattern.md) — Pattern de fichiers `.tmp` pour persister le contexte entre sessions
- [strategic-compact](strategic-compact.md) — Compactage manuel à des points logiques vs auto-compact
- [dynamic-system-prompt-injection](dynamic-system-prompt-injection.md) — Injection de contexte via `--system-prompt`
- [memory-persistence-hooks](memory-persistence-hooks.md) — Triplet PreCompact/SessionStart/Stop pour mémoire continue
- [continuous-learning-skill](continuous-learning-skill.md) — Auto-extraction des patterns en fin de session (v1)
- [continuous-learning-v2](continuous-learning-v2.md) — Système instinct-based avec confidence, import/export, clustering via `/evolve`

### 🪝 Hooks, commandes & interface

- [claude-code-hooks](claude-code-hooks.md) — Vue d'ensemble : PreToolUse, PostToolUse, PreCompact, SessionStart, Stop, UserPromptSubmit, Notification
- [claude-code-commands](claude-code-commands.md) — Commandes slash : `/rename`, `/fork`, `/clear`, `/compact`, `/learn`, `/rewind`, `/statusline`, `/checkpoints`
- [claude-code-keyboard-shortcuts](claude-code-keyboard-shortcuts.md) — Raccourcis clavier, préfixes !, @, /, intégration éditeurs (Zed, VSCode)

### 📁 Templates harness-creator (walkinglabs)

Fichiers bruts du repo `walkinglabs/learn-harness-engineering`, stockés tels quels.

- `wiki/templates/harness-creator/agents.md` — AGENTS.md / CLAUDE.md scaffold (instructions de workflow)
- `wiki/templates/harness-creator/progress.md` — Journal de session append-only
- `wiki/templates/harness-creator/session-handoff.md` — Snapshot compact pour passation de session
- `wiki/templates/harness-creator/feature-list.json` — Feature list exemple (5 features placeholder)
- `wiki/templates/harness-creator/feature-list.schema.json` — JSON Schema de feature-list.json
- `wiki/templates/harness-creator/init.sh` — Script d'init multi-stack (Node/Python/Go/Rust/Maven/Gradle/.NET)

### 🛠️ Skills — création & ingénierie

- [harness-creator-skill](harness-creator-skill.md) — Skill NPX walkinglabs : scaffold + validation structurelle d'un harness (5 subsystèmes : Instructions / State / Verification / Scope / Lifecycle)
- [skill-creator-meta-skill](skill-creator-meta-skill.md) — Meta-skill Anthropic pour créer et améliorer des skills : capture intention → SKILL.md → test → eval → iterate
- [skill-anatomy](skill-anatomy.md) — Anatomie d'un skill : SKILL.md + bundled resources, chargement progressif à 3 niveaux
- [skill-creation-workflow](skill-creation-workflow.md) — Cycle draft → test parallèle (with/without skill) → évaluation → amélioration
- [skill-eval-workflow](skill-eval-workflow.md) — Eval runner, grader, benchmark viewer, feedback loop pour valider un skill
- [skill-description-optimization](skill-description-optimization.md) — Mécanisme de triggering, design des eval queries, boucle d'optimisation automatisée

### 🔌 Plugins, MCPs & skills

- [claude-code-plugins](claude-code-plugins.md) — Plugins marketplace (LSP, hookify, mgrep), gestion du context window, auto-loading hooks v2.1+
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md) — Remplacer MCPs par CLI + skills pour optimiser tokens
- [llms-txt-pattern](llms-txt-pattern.md) — Pattern `/llms.txt` pour docs LLM-optimisées

### 💰 Optimisation tokens

- [subagent-architecture](subagent-architecture.md) — Déléguer au modèle le moins cher suffisant
- [model-selection-claude](model-selection-claude.md) — Quand choisir Haiku / Sonnet / Opus
- [mgrep-vs-grep](mgrep-vs-grep.md) — Réduction ~50% tokens sur la recherche
- [modular-codebase-tokens](modular-codebase-tokens.md) — Lien architecture modulaire ↔ coût tokens
- [background-processes-tmux](background-processes-tmux.md) — Offloading via tmux pour réduire l'input
- [ecc-token-optimization](ecc-token-optimization.md) — Settings ECC recommandés (`sonnet` default, MAX_THINKING_TOKENS=10000, autocompact=50)

### 🧪 Évaluations & vérification

- [checkpoint-vs-continuous-evals](checkpoint-vs-continuous-evals.md) — Deux patterns d'éval selon la nature du travail
- [grader-types](grader-types.md) — Code-based, model-based, human graders
- [pass-at-k-metric](pass-at-k-metric.md) — pass@k (au moins un succès) vs pass^k (tous succès)
- [eval-roadmap](eval-roadmap.md) — 8 étapes pour construire un système d'éval

### 🔀 Parallélisation

- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md) — Worktrees pour instances Claude parallèles
- [cascade-method](cascade-method.md) — Pattern d'organisation des tabs en parallèle
- [two-instance-kickoff](two-instance-kickoff.md) — Scaffolding agent + Deep research agent en kickoff

### 🤖 Modèles & comportements

- [claude-opus-47](claude-opus-47.md) — Claude Opus 4.7 : self-verification, visual benchmark 98.5%, comportement "codexy"
- [self-verification-mechanism](self-verification-mechanism.md) — Self-verification : relecture autonome et nouvelle tentative sans intervention humaine
- [claude-code-chrome-flag](claude-code-chrome-flag.md) — Flag `--chrome` : Claude Code pilote Chrome local via MCP (interfaces web authentifiées)

### 🤖 Agents & orchestration

- [sub-agent-context-problem](sub-agent-context-problem.md) — Problème du contexte implicite manquant
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md) — Boucle orchestrateur ↔ sub-agent (max 3 cycles)
- [agent-abstraction-tierlist](agent-abstraction-tierlist.md) — Tier 1 (faciles) vs Tier 2 (high skill floor)
- [metaprompting](metaprompting.md) — Investir dans la formulation du prompt pour gagner sur la tâche

### 🛡️ Sécurité des agents

- [lethal-trifecta](lethal-trifecta.md) — Simon Willison : private data + untrusted content + external comms = exfiltration possible
- [claude-code-cves-2026](claude-code-cves-2026.md) — CVE-2025-59536, CVE-2026-21852, MCP consent abuse (fév 2026)
- [agent-sandboxing](agent-sandboxing.md) — Docker `internal: true`, devcontainers, deny rules
- [agent-identity-separation](agent-identity-separation.md) — Compte agent dédié, tokens short-lived
- [least-agency](least-agency.md) — Politique entre modèle et action (pas le system prompt)
- [prompt-injection-sanitization](prompt-injection-sanitization.md) — Unicode invisible, attachements, liens externes
- [agent-observability](agent-observability.md) — Logging tool calls, network attempts, OpenTelemetry
- [agent-kill-switches](agent-kill-switches.md) — SIGTERM/SIGKILL, process group, dead-man heartbeat
- [agent-memory-hygiene](agent-memory-hygiene.md) — AI Recommendation Poisoning, mémoire narrow et jetable
- [agentshield](agentshield.md) — Scanner ECC : hooks, MCP, secrets, permissions
- [toxicskills-study](toxicskills-study.md) — Étude Snyk fév 2026 : 36% des skills publics contiennent du prompt injection

### 🧩 Écosystème ECC

- [ecc-overview](ecc-overview.md) — Bundle de patterns d'optimisation pour harnesses (Claude Code, Codex, OpenCode, Cursor)
- [ecc-hooks-autoloading](ecc-hooks-autoloading.md) — Convention v2.1+ : `hooks/hooks.json` auto-loadé

### 🏗️ Harness Engineering — Fondamentaux

- [harness-definition-et-philosophie](harness-definition-et-philosophie.md) — Harness = tout ce qui n'est pas les poids du modèle (Lec 01-02)
- [five-subsystem-harness-architecture](five-subsystem-harness-architecture.md) — Instructions / Tools / Environment / State / Feedback (Lec 02)
- [five-failure-modes-agents-en-prod](five-failure-modes-agents-en-prod.md) — 5 modes d'échec : specs vagues / conventions implicites / env / verif / state (Lec 01)
- [harness-rot-et-dette-technique](harness-rot-et-dette-technique.md) — Les harnesses pourrissent comme le code — entropie et maintenance

### 📚 Repository = Single Source of Truth

- [repository-as-system-of-record](repository-as-system-of-record.md) — Le repo est la spec ET le state. "Knowledge next to code" (Lec 03)
- [fresh-session-readability-test](fresh-session-readability-test.md) — 5 questions pour tester l'auto-suffisance du repo (Lec 03)
- [acid-principles-agent-state](acid-principles-agent-state.md) — Atomicity / Consistency / Isolation / Durability appliqués aux agents (Lec 03)

### ✂️ Instructions modulaires

- [modular-instruction-architecture](modular-instruction-architecture.md) — Entry file court + topic docs on-demand (Lec 04)
- [lost-in-the-middle-effect](lost-in-the-middle-effect.md) — Liu et al. 2023 : les contraintes au milieu sont ignorées (Lec 04)
- [instruction-design-patterns](instruction-design-patterns.md) — Hard vs soft, source/applicability/expiry, constrain don't micromanage

### 🔄 Continuité multi-session

- [cross-session-context-loss](cross-session-context-loss.md) — Sans persistance, chaque session redécouvre tout (Lec 05)
- [context-anxiety-modeles](context-anxiety-modeles.md) — Sonnet 4.5 vs Opus : tuning par modèle (Lec 05)
- [progress-file-pattern](progress-file-pattern.md) — PROGRESS.md / claude-progress.md : structure et workflow (Lec 05)
- [decision-log-pattern](decision-log-pattern.md) — DECISIONS.md append-only : capturer les "pourquoi" (Lec 05)
- [compaction-vs-reset-strategie](compaction-vs-reset-strategie.md) — Compaction vs reset : matrice de décision par modèle (Lec 05)

### 🚀 Phase d'initialisation

- [initialization-phase-separation](initialization-phase-separation.md) — Init et impl sont 2 problèmes incompatibles (Lec 06)
- [startup-readiness-checklist](startup-readiness-checklist.md) — Document canonique en sortie d'init (Lec 06)
- [task-breakdown-structure](task-breakdown-structure.md) — Behavior + verification + dependencies + state (Lec 06)

### 🎯 Contrôle de scope

- [wip-limit-discipline](wip-limit-discipline.md) — WIP=1 : +37% completion, moins de code, plus de features finies (Lec 07)
- [completion-evidence-executable](completion-evidence-executable.md) — "Done" = exit 0 sur verification command, jamais "ça a l'air bon" (Lec 07)
- [verified-completion-rate-metric](verified-completion-rate-metric.md) — VCR = passing / activated : métrique continue de discipline (Lec 07)
- [atomic-task-decomposition](atomic-task-decomposition.md) — Décomposer en ≥5 atomic units, chacune complétable en 1 session (Lec 07)

### 📋 Feature lists comme primitives

- [feature-list-as-primitive](feature-list-as-primitive.md) — Pas un mémo : primitive du harness, dépendances pipeline (Lec 08)
- [feature-state-machine](feature-state-machine.md) — 4 états contrôlés par harness, passing irréversible (Lec 08)
- [harness-pipeline-scheduler-verifier-handoff](harness-pipeline-scheduler-verifier-handoff.md) — Les 3 composants downstream de la feature list (Lec 08)

### ✅ Vérification multi-niveaux

- [three-layer-termination-validation](three-layer-termination-validation.md) — L1 static / L2 runtime / L3 system (Lec 09)
- [confidence-calibration-bias](confidence-calibration-bias.md) — Guo et al. 2017 : NN overconfident, ne pas faire confiance à l'auto-eval (Lec 09)
- [worker-checker-separation](worker-checker-separation.md) — Même modèle, rôles séparés = biais réduit (Lec 09)
- [end-to-end-verification-only](end-to-end-verification-only.md) — Tests unitaires aveugles aux boundary defects (Lec 10)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md) — Encoder les règles en checks mécaniques + Review Feedback Promotion (Lec 10)

### 👁️ Observabilité (runtime + process)

- [observability-runtime-vs-process](observability-runtime-vs-process.md) — Deux couches indispensables, design simultané (Lec 11)
- [sprint-contract-pattern](sprint-contract-pattern.md) — Scope / Verification / Exclusions avant le code (Lec 11)
- [planner-generator-evaluator-3-agent-architecture](planner-generator-evaluator-3-agent-architecture.md) — Single 1.6/5 → Full 4.9/5 (Lec 11 + P05)

### 🧹 Clean handoff & entropie

- [session-clean-handoff](session-clean-handoff.md) — 5 conditions non-négociables : build/tests/progress/artifacts/startup (Lec 12)
- [rebuild-cost-metric](rebuild-cost-metric.md) — Coût (temps + tokens) de reconstruction d'état from scratch — justification économique des artefacts de continuité
- [harness-entropy-management](harness-entropy-management.md) — Lehman's laws, dual-mode cleanup, audit mensuel (Lec 12)

### 📝 Templates concrets (Learn Harness Engineering)

- [template-claude-md](template-claude-md.md) — Root instructions (CLAUDE.md + variant AGENTS.md)
- [template-claude-progress-md](template-claude-progress-md.md) — Journal de session append-only
- [template-feature-list-json](template-feature-list-json.md) — Format machine-lisible canonique des tâches
- [template-session-handoff-md](template-session-handoff-md.md) — Snapshot compact pour reprise rapide
- [template-clean-state-checklist](template-clean-state-checklist.md) — 6-point checklist de clôture de session
- [template-evaluator-rubric](template-evaluator-rubric.md) — Grille 6 dimensions × scoring 0-2 + verdict

### 🎓 Projets pratiques

- [harness-curriculum-projects-overview](harness-curriculum-projects-overview.md) — Les 6 projets P01-P06 du curriculum (à refaire chez soi)
- [ablation-study-methodology](ablation-study-methodology.md) — Mesurer la valeur marginale de chaque composant harness

---

## Comment utiliser cet index

- Chaque page du wiki est référencée ici avec une description d'une ligne
- Organisé par thème pour faciliter la navigation
- Mis à jour automatiquement par Claude après chaque ingestion
- Pour explorer un thème, ouvrir la page et suivre les liens internes (syntaxe `[nom-de-page](nom-de-page.md)`)
