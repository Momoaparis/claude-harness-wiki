# Phase d'initialisation séparée

**Summary** : Initialisation et implémentation sont deux problèmes d'optimisation incompatibles. Les mélanger produit une infrastructure faible et du business code inachevé. Une phase init dédiée, qui produit un environnement runnable + tests vérifiés + checklist + task list, élimine le coût de redécouverte pour toutes les sessions suivantes.

**Sources** : `raw/ingested/lecture-06-make-the-agent-initialize-before-every-work-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le principe

> "Initialization and implementation have completely different optimization targets. When you mix initialization and implementation, the agent faces a multi-objective optimization problem." — Lecture 06

| Phase | Output cible | Métrique |
|-------|--------------|----------|
| **Phase 1 — Init** | Infrastructure runnable + tests vérifiés + task list | Time-to-first-passing-test, multi-session success rate |
| **Phase 2+ — Implementation** | Features livrées | Verified completion rate |

Mélanger = perdre les deux.

### Les 4 conditions de sortie d'init

À la fin de la phase d'init, le repo doit avoir :

1. **Runnable environment** — `make setup` réussit sans intervention
2. **Verifiable test framework** — au moins 1 test exemple passe (preuve que le framework marche)
3. **Startup readiness checklist** — listée explicitement (voir [[startup-readiness-checklist]])
4. **Task breakdown** — découpage en tâches ordonnées et vérifiables (voir [[task-breakdown-structure]])

Si une seule manque, l'init n'est pas terminée.

### Pourquoi ne pas mélanger

Si on commence l'implémentation alors que l'init est incomplète :

```
Session 1 : commence feature A → découvre que tests cassent → fixe tests → reprend A 
→ découvre deps manquantes → fixe → reprend A → context bouffé → bâcle A
Session 2 : redécouvre que A n'est pas finie + nouvelle config trouvée → drift
```

Symétriquement, si on fait l'init en plein milieu d'une feature :

- Le contexte est partagé entre 2 objectifs incompatibles
- L'agent n'a pas un "succès" propre à célébrer (ni infra ni feature complète)
- Les artefacts d'init sont sales (faits sous pression de la feature)

### Le pattern correct

```
Session 1 : Init phase (4 conditions ci-dessus) → commit dedicated → end session
Session 2 : Pick task #1 from task breakdown → implement → verify → commit → end session
Session 3 : Pick task #2 → ...
```

Init est **une session entière** (ou plus). Sortie = commit propre, état exécutable.

### Cas réel (Lecture 06)

Anthropic a mesuré sur des projets multi-session :

> "Projects using a dedicated initialization phase showed 31% higher feature completion rates in multi-session scenarios compared to mixed approaches."

| Approche | Rebuild time S2 | Total extra time |
|----------|----------------|------------------|
| Mixed (init + impl mélangés) | 20 min | +60% |
| Dedicated init | 3 min | recovered in 3-4 sessions |

### Composants concrets de l'init

#### Make setup

```makefile
setup:
	npm install
	cp .env.example .env
	docker-compose up -d db
	npm run db:migrate
	npm run db:seed
.PHONY: setup
```

#### Make dev, test, verify

```makefile
dev:
	npm run dev

test:
	npm test

verify:
	npm run lint
	npm run typecheck
	npm test
.PHONY: dev test verify
```

#### Example test passing

Au moins **un** test qui prouve que le framework marche :

```js
// tests/example.test.ts
test('framework works', () => {
  expect(1 + 1).toBe(2)
})
```

Trivial mais essentiel : sans ça, "test framework installed" ≠ "test framework verified".

### Template bootstrapping

> "Don't start from scratch (empty dir) but from template." — Lecture 06

Plutôt qu'init from-scratch, démarrer d'un template :

- React : `create-react-app`, `vite create`, `next-app`
- Python : `cookiecutter`, `fastapi-template`
- TypeScript Node : `tsdx`, custom starter
- Codex/Claude Code : voir [[harness-curriculum-projects-overview|projects starter/ folders]]

Bénéfice : 80% de l'init est déjà fait. On adapte les 20% project-specific.

### Implicit assumption landmines

Sans phase d'init disciplinée, des décisions implicites sont prises silencieusement :

- "Test framework = Vitest" (ou Jest ? ou ts-jest ?) → sessions suivantes proposent une autre
- "DB migrations dans `migrations/`" → l'agent en crée une dans `db/` → divergence
- "Lint config = strict" → un agent loosen → l'autre re-strict

L'init phase **documente** ces choix explicitement (voir [[decision-log-pattern]]).

### Lien avec fresh session test

[[fresh-session-readability-test|Le fresh session test]] est le **critère de validation** de l'init phase. Si une session démarre fresh et peut répondre aux 5 questions → init est OK.

### Comment savoir si l'init est complète

Checklist :

- [ ] `make setup` réussit en partant d'un clone propre
- [ ] `make test` retourne au moins 1 test passing
- [ ] Le fresh session test passe (5 questions répondues depuis le repo)
- [ ] Le task breakdown existe avec ≥3 tâches
- [ ] Tout est committé sur main
- [ ] Aucun fichier non-tracké important

Voir [[template-clean-state-checklist]] pour le format complet.

### À retenir

1. Init et implémentation sont **deux problèmes d'optimisation incompatibles**.
2. Init produit : **runnable + tested + checklist + task list**.
3. Init est une **session dédiée** (au moins une), pas un pré-traitement avant la première feature.
4. Démarrer d'un **template** plutôt que from-scratch.
5. Valider via le [[fresh-session-readability-test|fresh session test]].

## Related pages

- [[startup-readiness-checklist]]
- [[task-breakdown-structure]]
- [[fresh-session-readability-test]]
- [[five-failure-modes-agents-en-prod]]
- [[decision-log-pattern]]
- [[the-harness-engineering-curriculum-summary]]
