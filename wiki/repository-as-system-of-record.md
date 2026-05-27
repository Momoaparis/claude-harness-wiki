# Repository comme système d'enregistrement

**Summary** : Pour un agent, le repo est la seule source de vérité accessible. Tout ce qui vit ailleurs — Slack, Confluence, têtes des engineers — est invisible. Mettre la connaissance critique *à côté du code* (pas dans des silos externes) est l'investissement harness le plus fondamental.

**Sources** : `raw/ingested/lecture-03-making-the-repository-the-single-source-of-truth.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe en une phrase

> "Information that doesn't exist in the repo, doesn't exist for the agent." — Lecture 03

L'agent a exactement **trois sources d'input** :

1. System prompts et task descriptions
2. Contenu des fichiers du repo
3. Output des tool calls

Tout le reste (Confluence, Slack, Jira, têtes des engineers) est **noir** pour l'agent.

### Le knowledge visibility gap

Estimer la proportion de la connaissance projet *qui n'est pas dans le repo* :

- Compter ce qui vit dans les têtes des seniors → ?
- Compter ce qui vit dans les threads Slack → ?
- Compter ce qui vit dans des Confluence pages outdated → ?

Différence avec ce qui est réellement dans le repo = **visibility gap**. Plus le gap est large, plus l'agent va deviner — donc se tromper.

### Le double rôle du repo

| Rôle | Ce que ça signifie |
|------|-------------------|
| **Spec** | Le repo *décrit* ce que le projet doit être (intentions, contraintes) |
| **State** | Le repo *prouve* où le projet en est (commits, tests qui passent) |

OpenAI : "The repo IS the spec." Pas "le repo *contient* la spec". L'agent doit pouvoir reconstruire l'intention à partir du repo seul.

### Quoi mettre dans le repo

| Type d'info | Où | Pourquoi |
|-------------|---|----------|
| Overview projet | `AGENTS.md` / `CLAUDE.md` (root) | Landing page, voir [template-claude-md](template-claude-md.md) |
| Décisions d'architecture | `docs/architecture/` ou `ARCHITECTURE.md` per module | Proximité = découvrabilité |
| Contraintes hard | `docs/CONSTRAINTS.md` ou inline dans modules | Doit pouvoir être ignoré difficilement |
| Décisions passées | `DECISIONS.md` (append-only) | Voir [decision-log-pattern](decision-log-pattern.md) |
| État courant | `PROGRESS.md` / `claude-progress.md` | Voir [progress-file-pattern](progress-file-pattern.md) |
| Commandes standards | `Makefile` ou scripts/ | "How to run", reproductible |

### Le pattern "knowledge next to code"

> "A 50-line ARCHITECTURE.md in src/api/ is more useful than a 500-page design doc in Confluence." — Lecture 03

Règle : **proximité > exhaustivité**. L'agent ne lit que ce qui est à portée de main immédiate.

Concrètement :

- API REST → doc des conventions API dans `src/api/ARCHITECTURE.md`
- Module DB → contraintes schéma dans `src/db/CONSTRAINTS.md`
- Frontend → guidelines composants dans `src/components/README.md`

### Cas réel : e-commerce, 30 microservices (Lecture 03)

**Avant** :
- Décisions dispersées (Confluence outdated, Slack unsearchable, têtes seniors)
- Comments sparses dans le code
- Onboarding = 2 semaines avec un senior
- Agent en mode "deviner" sur chaque service

**Après** :
- `AGENTS.md` (root) : overview du monorepo
- `ARCHITECTURE.md` (par service) : design + boundaries
- `CONSTRAINTS.md` (centralisé) : MUST / MUST NOT explicites
- `PROGRESS.md` (par service) : état actuel

**Résultat** : taux de succès agent multi-session passé de ~30% à ~75%.

### Antipatterns

- **Confluence comme source primaire** → agent ne peut pas accéder, drift inévitable
- **Slack pour décisions** → introuvable, agent ne sait pas que ça existe
- **Comments sparses** → "knowledge in heads" reste invisible
- **Giant root README** → l'agent doit lire 600 lignes pour trouver l'info pertinente (voir [modular-instruction-architecture](modular-instruction-architecture.md))

### Comment tester si le repo est suffisant

[fresh-session-readability-test](fresh-session-readability-test.md) : 5 questions à poser à une session fresh. Si la session ne peut pas répondre à partir du repo seul → le repo est incomplet.

### Minimum viable repo

> "Each rule must have a clear use case. If removing it doesn't degrade quality, it shouldn't exist. But the fresh session test is must-pass." — Lecture 03

Équilibre : minimum mais complet. Pas de doc speculative ; chaque doc doit avoir un cas d'usage actif.

### À retenir

1. L'agent ne voit que le repo. Tout le reste est noir.
2. "Knowledge next to code" — proximité bat exhaustivité.
3. Le repo joue deux rôles : spec (intention) et state (où on en est).
4. Pas de doc obsolète : pire que pas de doc.
5. Tester via [fresh session test](fresh-session-readability-test.md).

## Related pages

- [fresh-session-readability-test](fresh-session-readability-test.md)
- [acid-principles-agent-state](acid-principles-agent-state.md)
- [modular-instruction-architecture](modular-instruction-architecture.md)
- [progress-file-pattern](progress-file-pattern.md)
- [decision-log-pattern](decision-log-pattern.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
