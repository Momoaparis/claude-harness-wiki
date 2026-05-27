# Harness rot et dette technique

**Summary** : Les harnesses pourrissent comme le code. Sans maintenance active, les instructions deviennent obsolètes, les feature lists divergent du repo, les commandes de vérification cassent. La dette technique de harness produit des intérêts composés très rapidement.

**Sources** : `raw/ingested/lecture-02-what-a-harness-actually-is.md`, `raw/ingested/lecture-12-leave-a-clean-handoff-at-the-end-of-every-session.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le constat

> "Out-of-date documentation is more dangerous than no documentation at all." — Lecture 03

> "Technical debt is a high-interest loan." — Lecture 12

Une instruction obsolète envoie l'agent dans la **mauvaise** direction. Mieux vaut pas de doc qu'une doc périmée — l'absence laisse l'agent demander, la doc périmée le fait agir avec confiance sur des hypothèses fausses.

### Cas réel : 12 semaines sans cleanup (Lecture 12)

| Semaine | Build pass | Tests pass | Startup time |
|---------|------------|------------|--------------|
| W1 | 100% | 100% | 5 min |
| W4 | 95% | 92% | 15 min |
| W8 | 82% | 78% | 35 min |
| W12 | **68%** | **61%** | **60+ min** |

Avec discipline de cleanup :

| Semaine | Build pass | Tests pass | Startup time |
|---------|------------|------------|--------------|
| W1 → W12 | 100% → 97% | 100% → 95% | 5 → 9 min |

**Delta** : +29% build, +34% tests, -85% startup time. Pour le même nombre de sessions agent.

### Les sources de rot

1. **Knowledge decay** : décisions du passé qui ne s'appliquent plus, mais restent écrites
2. **Maintenance decay** : instructions accumulées que personne n'ose supprimer (peur de casser)
3. **Contradiction accumulation** : règles ajoutées à des moments différents qui se contredisent ("strict mode" + "legacy allowed")
4. **Coffee cup phenomenon** (Lehman's laws) : l'agent copie les patterns existants — même mauvais — et amplifie la dérive
5. **Stale artifacts** : debug logs, TODO commentés, code commenté → bruit qui dilue le signal

### Le "coffee cup" effect

> "A week later the table is buried under cups. A codebase works the same way." — Lecture 12

Sans intervention, l'entropie augmente. L'agent ne nettoie pas — il accumule. Si un mauvais pattern existe dans le repo, l'agent le **réplique** (cohérence apparente) au lieu de le corriger.

Conséquence : un harness sans discipline de nettoyage **forme l'agent à produire de la dette**.

### Les deux modes de cleanup (Lecture 12)

#### Immediate cleanup (fin de chaque session)

Reference counting — l'agent qui a touché un truc le nettoie.

- Artefacts temporaires de la session
- Update du `feature_list.json`
- `make build` + `make test` verts
- Pas de `console.log`, `debugger`, `TODO` parasites

Voir [session-clean-handoff](session-clean-handoff.md) et [template-clean-state-checklist](template-clean-state-checklist.md).

#### Periodic cleanup (hebdomadaire)

Tracing — scan global du repo.

- Détection d'incohérences structurelles
- Mise à jour des quality docs
- Drift benchmarks (a-t-on perdu en perf ?)
- Suppression de docs obsolètes

Voir [harness-entropy-management](harness-entropy-management.md).

### Les "golden rules" mécaniquement vérifiables

Plutôt que d'accumuler des "best practices" textuelles, encoder les invariants comme **checks exécutables** :

- Lint customs (ex: `grep -r "require('fs')" src/renderer/` → fail)
- Tests architecturaux (`check-architecture.sh`)
- CI rules sur la structure de fichiers

Voir [architectural-boundary-enforcement](architectural-boundary-enforcement.md).

### Le harness audit mensuel (Lecture 12)

Une fois par mois :

1. Pick un composant de la harness
2. Disable temporairement
3. Run benchmarks (voir [ablation-study-methodology](ablation-study-methodology.md))
4. Si **pas** de dégradation → supprimer le composant (obsolète)
5. Si dégradation → garder ou remplacer par alternative plus légère

Les modèles s'améliorent. Des composants nécessaires hier ne le sont plus aujourd'hui. Anthropic cite : `sprint-splitter` indispensable pour Sonnet 4.5, inutile pour Opus 4.6.

> "As models improve, the interesting combinations in a harness don't shrink — they shift." — Lecture 12

### "Clean up later" = never

> "'Clean up later' means never clean up." — Lecture 12

La prochaine session ne sait pas ce que la précédente a laissé. Elle ignore le chaos, et y ajoute le sien. Positive feedback loop sur la dette.

### À retenir

1. Une harness non maintenue **dégrade** en quelques semaines (68% build, 61% tests à W12).
2. Pas de doc > doc périmée.
3. Cleanup en **deux modes** : immédiat (par session) + périodique (hebdo).
4. Encoder les golden rules en **checks exécutables**, pas en commentaires.
5. **Audit mensuel** de la harness : désactiver un composant, mesurer, simplifier si possible.

## Related pages

- [session-clean-handoff](session-clean-handoff.md)
- [harness-entropy-management](harness-entropy-management.md)
- [architectural-boundary-enforcement](architectural-boundary-enforcement.md)
- [ablation-study-methodology](ablation-study-methodology.md)
- [harness-definition-et-philosophie](harness-definition-et-philosophie.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
