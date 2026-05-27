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

Ce guide est la **suite avancée** du Shorthand Guide (sep 2025, [the-shorthand-guide-summary](the-shorthand-guide-summary.md)). Il assume que tu as déjà :
- Skills configurés
- Agents configurés
- Hooks configurés
- MCPs configurés

Il couvre les **techniques qui séparent les sessions productives des sessions gaspilleuses**, refinées sur 10+ mois d'usage quotidien.

### Les 8 thèmes du guide

1. **[Context & Memory Management](session-storage-pattern.md)** — Persister le contexte entre sessions
2. **[Continuous Learning / Memory](continuous-learning-skill.md)** — Auto-extraire les apprentissages
3. **[Token Optimization](subagent-architecture.md)** — Réduire le coût en tokens
4. **[Verification Loops and Evals](checkpoint-vs-continuous-evals.md)** — Valider le travail
5. **[Parallelization](git-worktrees-parallel-claude.md)** — Plusieurs instances en parallèle
6. **[Groundwork](two-instance-kickoff.md)** — Démarrer un projet correctement
7. **[Best Practices for Agents](sub-agent-context-problem.md)** — Orchestration et sub-agents
8. **[Tips and Tricks](mcp-vs-cli-skills.md)** — MCPs et alternatives

### Concepts extraits dans le wiki

#### Gestion mémoire & contexte
- [session-storage-pattern](session-storage-pattern.md)
- [strategic-compact](strategic-compact.md)
- [dynamic-system-prompt-injection](dynamic-system-prompt-injection.md)
- [memory-persistence-hooks](memory-persistence-hooks.md)
- [continuous-learning-skill](continuous-learning-skill.md)

#### Hooks
- [claude-code-hooks](claude-code-hooks.md)

#### Optimisation tokens
- [subagent-architecture](subagent-architecture.md)
- [model-selection-claude](model-selection-claude.md)
- [mgrep-vs-grep](mgrep-vs-grep.md)
- [modular-codebase-tokens](modular-codebase-tokens.md)
- [background-processes-tmux](background-processes-tmux.md)

#### Évaluations
- [checkpoint-vs-continuous-evals](checkpoint-vs-continuous-evals.md)
- [grader-types](grader-types.md)
- [pass-at-k-metric](pass-at-k-metric.md)
- [eval-roadmap](eval-roadmap.md)

#### Parallélisation
- [git-worktrees-parallel-claude](git-worktrees-parallel-claude.md)
- [cascade-method](cascade-method.md)
- [two-instance-kickoff](two-instance-kickoff.md)

#### Agents & orchestration
- [sub-agent-context-problem](sub-agent-context-problem.md)
- [iterative-retrieval-pattern](iterative-retrieval-pattern.md)
- [agent-abstraction-tierlist](agent-abstraction-tierlist.md)

#### MCPs & tips
- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [llms-txt-pattern](llms-txt-pattern.md)

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

Voir l'index complet : [index](index.md)
