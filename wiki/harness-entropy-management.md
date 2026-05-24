# Harness entropy management

**Summary** : Les systèmes logiciels sous changement continu **gagnent en complexité** par défaut (Lehman's laws). Sans intervention, la harness elle-même pourrit. Solution : dual-mode cleanup (immediate par session + periodic hebdo), golden rules mécaniques, audit mensuel pour simplifier ce qui n'est plus utile.

**Sources** : `raw/ingested/lecture-12-leave-a-clean-handoff-at-the-end-of-every-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le constat (Lehman's laws)

Lehman (1980, "Programs, Life Cycles, and Laws of Software Evolution") :

> "Software systems under continuous change grow in complexity unless actively managed."

Pour la harness :

- Instructions s'accumulent
- Tests deviennent obsolètes
- Scripts cessent de marcher
- Boundaries s'érodent

Sans gestion active, **chaque semaine**, la harness est plus faible.

### Le coffee cup phenomenon

> "A week later the table is buried under cups. A codebase works the same way." — Lecture 12

Spécificité agent : les agents **copient** les patterns existants. Si un mauvais pattern apparaît une fois, il se reproduit.

Cycle :
```
1. Bad pattern dans le repo (par accident)
2. Agent voit → reproduit (cohérence apparente)
3. Pattern devient dominant
4. Agent ne sait plus que c'est mauvais
```

Le repo **forme l'agent** à produire de la dette technique.

### Voir aussi [[harness-rot-et-dette-technique]]

Cette page est complémentaire : [[harness-rot-et-dette-technique]] explique le *pourquoi* du rot, cette page la *gestion* concrète.

### Dual-mode cleanup

#### Mode 1 : Immediate (fin de chaque session)

Reference counting — l'agent qui a touché un truc le nettoie.

À faire **à chaque** clock-out :
- Artefacts temporaires de la session
- Update `feature_list.json`
- Build + tests verts
- Pas de `console.log`, `debugger`, `TODO` parasites
- 5 conditions de [[session-clean-handoff]]

Coût : 2-5 min par session.

#### Mode 2 : Periodic (hebdomadaire)

Tracing — scan global du repo.

À faire **chaque semaine** (ou bimensuel) :
- Détecter incohérences structurelles
- Mettre à jour quality docs
- Drift benchmarks (perf, taux de tests)
- Suppression de docs obsolètes
- Audit des dépendances inutilisées

Coût : 30 min - 2h hebdo.

### Quality document

Artefact actif qui **continuellement** score chaque module :

```markdown
# Quality Document

## Auth Module
- Quality grade: **A**
- Verification: yes
- Agent-understandable: yes
- Test stability: stable
- Boundaries: compliant
- Conventions: followed

## Payment Module
- Quality grade: **C**
- Verification: partial (E2E missing for refund flow)
- Agent-understandable: difficult (complex state machine)
- Test stability: unstable (flaky tests)
- Boundaries: violated (DB access from controller)
- Conventions: partial

### Action items
1. Add E2E test for refund flow
2. Refactor state machine to be explicit
3. Move DB access to repository layer
```

Updaté chaque mois. **Visible** dans le repo.

### Golden rules mécaniques

Plutôt qu'accumuler des "best practices" textuelles, encoder les invariants en **checks exécutables** :

- Lint customs
- CI rules
- Pre-commit hooks (légers)

Voir [[architectural-boundary-enforcement]].

Exemple :

```bash
# rules/check-no-direct-db.sh
grep -r "import.*from.*'@/db'" src/ | grep -v "^src/db/" && {
  echo "❌ Direct DB access outside src/db/"; exit 1
}
```

Effet : règle imposée, pas oubliable.

### Periodic cleanup workflow (Codex fleet pattern)

Anthropic et OpenAI utilisent des **fleet de tâches background** qui :

1. Scannent le repo pour déviations
2. Updatent quality scores
3. Ouvrent des PRs de refactoring auto-reviewables et mergeable

C'est de l'**auto-maintenance** continue. Pour les setups avec budget, super-utile.

Pour solo dev : un cronjob hebdo qui run un script de health check.

### Monthly harness audit

Une fois par mois :

1. **Pick un composant** de la harness (un hook, une règle, un script, une instruction)
2. **Disable** temporairement
3. **Run benchmarks** (voir [[ablation-study-methodology]])
4. Si pas de dégradation → **supprimer** (obsolète)
5. Si dégradation → **garder** ou remplacer par alternative plus légère

### Harness simplification over time

> "As models improve, the interesting combinations in a harness don't shrink — they shift." — Lecture 12

Exemple Anthropic : `sprint-splitter` indispensable pour Sonnet 4.5, **inutile** pour Opus 4.6 (overhead pour rien).

Conséquence : la harness évolue avec les modèles. Ce qui était nécessaire hier ne l'est plus aujourd'hui. **Audit régulier** pour détecter.

| Audit fréquence | Quand |
|------------------|-------|
| Mensuel | Cadence standard |
| Après upgrade modèle majeur | Toujours |
| Si benchmark dégrade | Investiguer |

### High-throughput merge philosophy

> "When agent output >> human review capacity, minimize blocking gates." — Lecture 12

Cas particulier : OpenAI cite 3.5 PRs/jour, short-lived, fast merge.

**Coût fix < coût attendre review** → fast merge + fast fix si bug. Mais ça assume :
- Cleanup auto efficace
- Boundary checks en CI
- Test suite rapide

Cette philosophie n'est valide qu'avec une harness **mature**. Sans, c'est du chaos.

### Idempotent cleanup

Les scripts de cleanup doivent être **safe à run plusieurs fois** :

```bash
rm -f /tmp/debug-*.log    # -f = pas d'erreur si absent
git checkout -- .env.local  # safe même si rien à reset
npm run test --silent      # idempotent
```

Sans idempotence, le cleanup devient lui-même source de bugs.

### Lien avec quality document

Le quality document **mesure** l'entropy. Plus de modules en grade C/D → la harness fait moins bien son travail.

Trend mensuel :
- Tous modules à A → discipline saine
- Glissement vers B/C → revoir cleanup
- Apparition de D → urgence d'audit

### Antipatterns

- ❌ Cleanup uniquement en immediate (manque la vision globale)
- ❌ Cleanup uniquement en periodic (les sessions individuelles cumulent du sale)
- ❌ Pas de quality document → on ne sait pas où on va
- ❌ Pas d'audit mensuel → la harness garde du legacy inutile
- ❌ Scripts cleanup non-idempotents → peur de les run

### À retenir

1. **Lehman** : entropy par défaut. Gestion **active** obligatoire.
2. **Dual-mode** : immediate (par session) + periodic (hebdo).
3. **Quality document** continuellement updaté.
4. **Golden rules** mécaniquement enforced.
5. **Audit mensuel** : disable component, mesurer, simplifier si possible.

## Related pages

- [[session-clean-handoff]]
- [[harness-rot-et-dette-technique]]
- [[architectural-boundary-enforcement]]
- [[ablation-study-methodology]]
- [[the-harness-engineering-curriculum-summary]]
