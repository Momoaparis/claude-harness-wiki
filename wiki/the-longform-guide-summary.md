# The Longform Guide to Everything Claude Code — Résumé

**Summary** : Résumé du guide longform d'Affaan Mustafa (jan 2026) sur les techniques avancées de Claude Code — gestion mémoire, optimisation tokens, évaluations, parallélisation, agents.

**Sources** : The Longform Guide to Everything Claude Code.md

**Last updated** : 2026-05-22

---

## Contenu

### Métadonnées de la source

- **Auteur** : Affaan Mustafa (@affaanmustafa)
- **Publication** : 17 janvier 2026
- **URL** : https://x.com/affaanmustafa/status/2014040193557471352
- **Repo associé** : [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- **Article frère** : "The Shorthand Guide to Everything Claude Code" (setup de base — skills, agents, hooks, MCPs)

### Positionnement

Ce guide est la **suite avancée** du Shorthand Guide (sep 2025, [[the-shorthand-guide-summary]]). Il assume que tu as déjà :
- Skills configurés
- Agents configurés
- Hooks configurés
- MCPs configurés

Il couvre les **techniques qui séparent les sessions productives des sessions gaspilleuses**, refinées sur 10+ mois d'usage quotidien.

### Les 8 thèmes du guide

1. **[[session-storage-pattern|Context & Memory Management]]** — Persister le contexte entre sessions
2. **[[continuous-learning-skill|Continuous Learning / Memory]]** — Auto-extraire les apprentissages
3. **[[subagent-architecture|Token Optimization]]** — Réduire le coût en tokens
4. **[[checkpoint-vs-continuous-evals|Verification Loops and Evals]]** — Valider le travail
5. **[[git-worktrees-parallel-claude|Parallelization]]** — Plusieurs instances en parallèle
6. **[[two-instance-kickoff|Groundwork]]** — Démarrer un projet correctement
7. **[[sub-agent-context-problem|Best Practices for Agents]]** — Orchestration et sub-agents
8. **[[mcp-vs-cli-skills|Tips and Tricks]]** — MCPs et alternatives

### Concepts extraits dans le wiki

#### Gestion mémoire & contexte
- [[session-storage-pattern]]
- [[strategic-compact]]
- [[dynamic-system-prompt-injection]]
- [[memory-persistence-hooks]]
- [[continuous-learning-skill]]

#### Hooks
- [[claude-code-hooks]]

#### Optimisation tokens
- [[subagent-architecture]]
- [[model-selection-claude]]
- [[mgrep-vs-grep]]
- [[modular-codebase-tokens]]
- [[background-processes-tmux]]

#### Évaluations
- [[checkpoint-vs-continuous-evals]]
- [[grader-types]]
- [[pass-at-k-metric]]
- [[eval-roadmap]]

#### Parallélisation
- [[git-worktrees-parallel-claude]]
- [[cascade-method]]
- [[two-instance-kickoff]]

#### Agents & orchestration
- [[sub-agent-context-problem]]
- [[iterative-retrieval-pattern]]
- [[agent-abstraction-tierlist]]

#### MCPs & tips
- [[mcp-vs-cli-skills]]
- [[llms-txt-pattern]]

### Citations et personnes

- **Andrej Karpathy** : inspirateur du pattern LLM Wiki
- **Boris Cherny** (@bcherny) : créateur de Claude Code, recommandations sur la parallélisation
- **@PerceptualPeak** : a formulé le sub-agent context problem
- **@menhguin** : a proposé l'agent abstraction tierlist
- **@omarsar0** : philosophie des reusable patterns ("compound effects")
- **@RLanceMartin** : pattern de session reflection
- **@alexhillman** : self-improving memory system
- **Anthropic Engineering** : article "Demystifying Evals for AI Agents" (Jan 2026)

### Philosophie centrale (citation @omarsar0)

> "Early on, I spent time building reusable workflows/patterns. Tedious to build, but this had a wild compounding effect as models and agent harnesses improved."

> "The best part is that all these workflows are transferable to other agents like Codex."

**Investissement dans les patterns > investissement dans les astuces spécifiques à un modèle.**

### Recommandations clés à retenir

1. Le **strategic compact** vaut mieux que l'auto-compact
2. Pour les tokens, le combo **Haiku + Opus** est plus impactant que d'utiliser Sonnet partout
3. La **modularité du code** = économies de tokens directes
4. Toujours considérer le **sub-agent context problem** avant de dispatcher
5. **Tier 1 d'abord** : maîtriser sub-agents et metaprompting avant le multi-agent parallèle
6. Pour les MCPs, **CLI + skills** reste pertinent même avec le lazy loading

## Related pages

Voir l'index complet : [[index]]
