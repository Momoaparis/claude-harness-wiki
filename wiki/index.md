# Index du Wiki

**Summary** : Table des matières de la base de connaissances. Mise à jour à chaque ingestion ou création de page.

**Last updated** : 2026-05-24

---

## Sources résumées

- [[claude-opus-47-lovart-brand-design-summary]] — Claude Opus 4.7 + Lovart : pipeline brand design complet via Chrome MCP (Brand Kit, police, PSD, Skill, vidéo)

- [[the-shorthand-guide-summary]] — Guide shorthand d'Affaan Mustafa sur Claude Code (sep 2025) — setup de base
- [[the-longform-guide-summary]] — Guide longform d'Affaan Mustafa sur Claude Code (jan 2026) — techniques avancées
- [[the-agentic-security-summary]] — Guide shorthand d'Affaan Mustafa sur la sécurité des agents (fév 2026) — CVEs Claude Code + standards opsec 2026
- [[ecc-overview]] — Écosystème ECC (Affaan Mustafa) : skills, agents, hooks, rules + tooling (AgentShield, instincts)
- [[the-harness-engineering-curriculum-summary]] — Cours Learn Harness Engineering : 12 lectures + 6 projets + 7 templates pour construire des harnesses Claude Code/Codex robustes

## Pages par thème

### 🎨 Design IA & outils créatifs

- [[ai-design-agent]] — Design Agent vs text-to-image : pipeline complet (Brand Kit + police + PSD + Skill + vidéo)
- [[lovart-brand-kit]] — Brand Kit Lovart : PDF → schéma structuré de marque (couleurs, logos, philosophie)
- [[ai-font-generator]] — Font Generator Lovart : police typographique custom depuis description texte (~3 min)
- [[prompt-as-asset]] — Prompt-as-asset vs prompt-as-craft : conversations réussies → skills réutilisables
- [[seedance-video-gen]] — Seedance 2.0 : génération vidéo text-to-video courte intégrée à Lovart

### 🧠 Gestion mémoire & contexte

- [[session-storage-pattern]] — Pattern de fichiers `.tmp` pour persister le contexte entre sessions
- [[strategic-compact]] — Compactage manuel à des points logiques vs auto-compact
- [[dynamic-system-prompt-injection]] — Injection de contexte via `--system-prompt`
- [[memory-persistence-hooks]] — Triplet PreCompact/SessionStart/Stop pour mémoire continue
- [[continuous-learning-skill]] — Auto-extraction des patterns en fin de session (v1)
- [[continuous-learning-v2]] — Système instinct-based avec confidence, import/export, clustering via `/evolve`

### 🪝 Hooks, commandes & interface

- [[claude-code-hooks]] — Vue d'ensemble : PreToolUse, PostToolUse, PreCompact, SessionStart, Stop, UserPromptSubmit, Notification
- [[claude-code-commands]] — Commandes slash : `/rename`, `/fork`, `/clear`, `/compact`, `/learn`, `/rewind`, `/statusline`, `/checkpoints`
- [[claude-code-keyboard-shortcuts]] — Raccourcis clavier, préfixes !, @, /, intégration éditeurs (Zed, VSCode)

### 🔌 Plugins, MCPs & skills

- [[claude-code-plugins]] — Plugins marketplace (LSP, hookify, mgrep), gestion du context window, auto-loading hooks v2.1+
- [[mcp-vs-cli-skills]] — Remplacer MCPs par CLI + skills pour optimiser tokens
- [[llms-txt-pattern]] — Pattern `/llms.txt` pour docs LLM-optimisées

### 💰 Optimisation tokens

- [[subagent-architecture]] — Déléguer au modèle le moins cher suffisant
- [[model-selection-claude]] — Quand choisir Haiku / Sonnet / Opus
- [[mgrep-vs-grep]] — Réduction ~50% tokens sur la recherche
- [[modular-codebase-tokens]] — Lien architecture modulaire ↔ coût tokens
- [[background-processes-tmux]] — Offloading via tmux pour réduire l'input
- [[ecc-token-optimization]] — Settings ECC recommandés (`sonnet` default, MAX_THINKING_TOKENS=10000, autocompact=50)

### 🧪 Évaluations & vérification

- [[checkpoint-vs-continuous-evals]] — Deux patterns d'éval selon la nature du travail
- [[grader-types]] — Code-based, model-based, human graders
- [[pass-at-k-metric]] — pass@k (au moins un succès) vs pass^k (tous succès)
- [[eval-roadmap]] — 8 étapes pour construire un système d'éval

### 🔀 Parallélisation

- [[git-worktrees-parallel-claude]] — Worktrees pour instances Claude parallèles
- [[cascade-method]] — Pattern d'organisation des tabs en parallèle
- [[two-instance-kickoff]] — Scaffolding agent + Deep research agent en kickoff

### 🤖 Modèles & comportements

- [[claude-opus-47]] — Claude Opus 4.7 : self-verification, visual benchmark 98.5%, comportement "codexy"
- [[self-verification-mechanism]] — Self-verification : relecture autonome et nouvelle tentative sans intervention humaine
- [[claude-code-chrome-flag]] — Flag `--chrome` : Claude Code pilote Chrome local via MCP (interfaces web authentifiées)

### 🤖 Agents & orchestration

- [[sub-agent-context-problem]] — Problème du contexte implicite manquant
- [[iterative-retrieval-pattern]] — Boucle orchestrateur ↔ sub-agent (max 3 cycles)
- [[agent-abstraction-tierlist]] — Tier 1 (faciles) vs Tier 2 (high skill floor)
- [[metaprompting]] — Investir dans la formulation du prompt pour gagner sur la tâche

### 🛡️ Sécurité des agents

- [[lethal-trifecta]] — Simon Willison : private data + untrusted content + external comms = exfiltration possible
- [[claude-code-cves-2026]] — CVE-2025-59536, CVE-2026-21852, MCP consent abuse (fév 2026)
- [[agent-sandboxing]] — Docker `internal: true`, devcontainers, deny rules
- [[agent-identity-separation]] — Compte agent dédié, tokens short-lived
- [[least-agency]] — Politique entre modèle et action (pas le system prompt)
- [[prompt-injection-sanitization]] — Unicode invisible, attachements, liens externes
- [[agent-observability]] — Logging tool calls, network attempts, OpenTelemetry
- [[agent-kill-switches]] — SIGTERM/SIGKILL, process group, dead-man heartbeat
- [[agent-memory-hygiene]] — AI Recommendation Poisoning, mémoire narrow et jetable
- [[agentshield]] — Scanner ECC : hooks, MCP, secrets, permissions
- [[toxicskills-study]] — Étude Snyk fév 2026 : 36% des skills publics contiennent du prompt injection

### 🧩 Écosystème ECC

- [[ecc-overview]] — Bundle de patterns d'optimisation pour harnesses (Claude Code, Codex, OpenCode, Cursor)
- [[ecc-hooks-autoloading]] — Convention v2.1+ : `hooks/hooks.json` auto-loadé

### 🏗️ Harness Engineering — Fondamentaux

- [[harness-definition-et-philosophie]] — Harness = tout ce qui n'est pas les poids du modèle (Lec 01-02)
- [[five-subsystem-harness-architecture]] — Instructions / Tools / Environment / State / Feedback (Lec 02)
- [[five-failure-modes-agents-en-prod]] — 5 modes d'échec : specs vagues / conventions implicites / env / verif / state (Lec 01)
- [[harness-rot-et-dette-technique]] — Les harnesses pourrissent comme le code — entropie et maintenance

### 📚 Repository = Single Source of Truth

- [[repository-as-system-of-record]] — Le repo est la spec ET le state. "Knowledge next to code" (Lec 03)
- [[fresh-session-readability-test]] — 5 questions pour tester l'auto-suffisance du repo (Lec 03)
- [[acid-principles-agent-state]] — Atomicity / Consistency / Isolation / Durability appliqués aux agents (Lec 03)

### ✂️ Instructions modulaires

- [[modular-instruction-architecture]] — Entry file court + topic docs on-demand (Lec 04)
- [[lost-in-the-middle-effect]] — Liu et al. 2023 : les contraintes au milieu sont ignorées (Lec 04)
- [[instruction-design-patterns]] — Hard vs soft, source/applicability/expiry, constrain don't micromanage

### 🔄 Continuité multi-session

- [[cross-session-context-loss]] — Sans persistance, chaque session redécouvre tout (Lec 05)
- [[context-anxiety-modeles]] — Sonnet 4.5 vs Opus : tuning par modèle (Lec 05)
- [[progress-file-pattern]] — PROGRESS.md / claude-progress.md : structure et workflow (Lec 05)
- [[decision-log-pattern]] — DECISIONS.md append-only : capturer les "pourquoi" (Lec 05)
- [[compaction-vs-reset-strategie]] — Compaction vs reset : matrice de décision par modèle (Lec 05)

### 🚀 Phase d'initialisation

- [[initialization-phase-separation]] — Init et impl sont 2 problèmes incompatibles (Lec 06)
- [[startup-readiness-checklist]] — Document canonique en sortie d'init (Lec 06)
- [[task-breakdown-structure]] — Behavior + verification + dependencies + state (Lec 06)

### 🎯 Contrôle de scope

- [[wip-limit-discipline]] — WIP=1 : +37% completion, moins de code, plus de features finies (Lec 07)
- [[completion-evidence-executable]] — "Done" = exit 0 sur verification command, jamais "ça a l'air bon" (Lec 07)
- [[verified-completion-rate-metric]] — VCR = passing / activated : métrique continue de discipline (Lec 07)
- [[atomic-task-decomposition]] — Décomposer en ≥5 atomic units, chacune complétable en 1 session (Lec 07)

### 📋 Feature lists comme primitives

- [[feature-list-as-primitive]] — Pas un mémo : primitive du harness, dépendances pipeline (Lec 08)
- [[feature-state-machine]] — 4 états contrôlés par harness, passing irréversible (Lec 08)
- [[harness-pipeline-scheduler-verifier-handoff]] — Les 3 composants downstream de la feature list (Lec 08)

### ✅ Vérification multi-niveaux

- [[three-layer-termination-validation]] — L1 static / L2 runtime / L3 system (Lec 09)
- [[confidence-calibration-bias]] — Guo et al. 2017 : NN overconfident, ne pas faire confiance à l'auto-eval (Lec 09)
- [[worker-checker-separation]] — Même modèle, rôles séparés = biais réduit (Lec 09)
- [[end-to-end-verification-only]] — Tests unitaires aveugles aux boundary defects (Lec 10)
- [[architectural-boundary-enforcement]] — Encoder les règles en checks mécaniques + Review Feedback Promotion (Lec 10)

### 👁️ Observabilité (runtime + process)

- [[observability-runtime-vs-process]] — Deux couches indispensables, design simultané (Lec 11)
- [[sprint-contract-pattern]] — Scope / Verification / Exclusions avant le code (Lec 11)
- [[planner-generator-evaluator-3-agent-architecture]] — Single 1.6/5 → Full 4.9/5 (Lec 11 + P05)

### 🧹 Clean handoff & entropie

- [[session-clean-handoff]] — 5 conditions non-négociables : build/tests/progress/artifacts/startup (Lec 12)
- [[rebuild-cost-metric]] — Coût (temps + tokens) de reconstruction d'état from scratch — justification économique des artefacts de continuité
- [[harness-entropy-management]] — Lehman's laws, dual-mode cleanup, audit mensuel (Lec 12)

### 📝 Templates concrets (Learn Harness Engineering)

- [[template-claude-md]] — Root instructions (CLAUDE.md + variant AGENTS.md)
- [[template-claude-progress-md]] — Journal de session append-only
- [[template-feature-list-json]] — Format machine-lisible canonique des tâches
- [[template-session-handoff-md]] — Snapshot compact pour reprise rapide
- [[template-clean-state-checklist]] — 6-point checklist de clôture de session
- [[template-evaluator-rubric]] — Grille 6 dimensions × scoring 0-2 + verdict

### 🎓 Projets pratiques

- [[harness-curriculum-projects-overview]] — Les 6 projets P01-P06 du curriculum (à refaire chez soi)
- [[ablation-study-methodology]] — Mesurer la valeur marginale de chaque composant harness

---

## Comment utiliser cet index

- Chaque page du wiki est référencée ici avec une description d'une ligne
- Organisé par thème pour faciliter la navigation
- Mis à jour automatiquement par Claude après chaque ingestion
- Pour explorer un thème, ouvrir la page et suivre les liens internes (syntaxe `[[nom-de-page]]`)
