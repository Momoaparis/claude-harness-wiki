# Cross-session context loss

**Summary** : Sans mécanisme de persistance, chaque nouvelle session redécouvre tout. Décisions perdues, hypothèses re-faites, mêmes erreurs reproduites. C'est le mode d'échec #5 du curriculum, le plus insidieux car il rend les longues tâches statistiquement impossibles.

**Sources** : `raw/ingested/lecture-05-keeping-context-alive-across-sessions.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le constat (Lecture 05)

> "Context windows are finite. This isn't a problem that model upgrades can solve — even if window sizes grow to 1M tokens, complex tasks will still exhaust them."

> "Discoveries from previous sessions disappear; tasks exceeding 30 minutes show sharp failure rate increases." — Lecture 01

**Trois forces convergent** :

1. La fenêtre de contexte est finie (même à 1M tokens, ça s'épuise)
2. Une session ne survit pas à un redémarrage
3. Le travail réel dépasse souvent une session

Sans contre-mesure → l'agent travaille en cercles.

### Le problème de l'information non uniforme

Tout ce que produit l'agent en cours de session n'a pas la même valeur durable :

| Type | Valeur durable | Survit à la compaction ? |
|------|----------------|--------------------------|
| Code écrit (le "quoi") | Haute | Oui (dans git) |
| Décisions et raisons (le "pourquoi") | Très haute | **Non** (perdu) |
| Étapes intermédiaires de raisonnement | Faible | Non |
| Hypothèses validées/rejetées | Haute | **Non** (perdu) |

Sans persistance dédiée, **les "pourquoi" disparaissent**. Le code reste, mais la session suivante ne comprend plus l'intention.

### Le drift accumulé

À chaque limite de session :

```
écart compréhension agent ↔ état réel du repo
        +
écart à chaque session suivante
        =
drift exponentiel si pas de remise à zéro
```

Sans contre-mesure, après N sessions, l'agent travaille avec une vision profondément divergente du repo.

### Les deux flux possibles

#### Sans persistance

```
Session 1 finit → Session 2 démarre fresh →
agent guess l'état → agent drift → 
écart amplifié → travail perdu
```

#### Avec persistance

```
Session 1 finit + écrit PROGRESS.md, DECISIONS.md, git commits →
Session 2 démarre → lit les artefacts → 
état exécutable en 3 min → travail repris
```

### Le rebuild cost

Métrique clé : temps qu'une nouvelle session met pour atteindre un état exécutable.

| Sans artefacts | Avec artefacts complets |
|----------------|-------------------------|
| 15-20 min | 3 min |

Pour une équipe qui démarre 5 sessions / jour → économie de **1h+ / jour / agent**.

### Les artefacts requis

Le minimum vital pour qu'une session N+1 reprenne sans interroger un humain :

1. **`PROGRESS.md`** ou **`claude-progress.md`** — voir [progress-file-pattern](progress-file-pattern.md)
2. **`DECISIONS.md`** — voir [decision-log-pattern](decision-log-pattern.md)
3. **Git commits** — granulaires, messages explicatifs (voir [acid-principles-agent-state](acid-principles-agent-state.md))
4. **`session-handoff.md`** — note compacte de transition (voir [template-session-handoff-md](template-session-handoff-md.md))

### Le handoff protocol

> "Treat the agent like an engineer whose short-term memory gets wiped at every session. Before it 'clocks out,' it must write down critical information so the next 'shift' agent can pick up quickly." — Lecture 05

Discipline "clock-in / clock-out" :

**Clock-in (début de session)** :
- Lire `PROGRESS.md`
- Lire `DECISIONS.md` (dernières entrées)
- Run `make verify` pour confirmer baseline
- Continuer la tâche listée

**Clock-out (fin de session)** :
- Update `PROGRESS.md`
- Append à `DECISIONS.md` si nouvelles décisions
- Commit tout
- Verifier que l'état est clean ([session-clean-handoff](session-clean-handoff.md))

### Lien avec la context anxiety

L'agent qui sent le contexte se remplir [panique](context-anxiety-modeles.md) et termine vite mal — il saute la mise à jour des artefacts. Solution : déclencher le "clock-out" **avant** la zone d'anxiety, pas au dernier moment.

### Compaction vs reset

[Compaction](compaction-vs-reset-strategie.md) (résumer dans la même session) garde la "psychologie" de l'agent mais perd les "pourquoi". Reset (nouvelle session) part propre mais demande des artefacts complets. Le choix dépend du modèle (Sonnet 4.5 vs Opus 4.6) et de la nature de la tâche.

### Cas réel (Lecture 05)

| Approche | Completion rate | Defects cachés | Rebuild time |
|----------|-----------------|----------------|--------------|
| Baseline (no artifacts) | 58% | 43% | — |
| Avec artifacts complets | **100%** | **8%** | **−78%** |

### À retenir

1. La perte de context **n'est pas** un problème de modèle. Aucune fenêtre n'est assez large.
2. Les artefacts (`PROGRESS.md`, `DECISIONS.md`, commits) **sont** la solution.
3. Discipline clock-in / clock-out à chaque session.
4. Mesurer le rebuild cost = signal de qualité harness.
5. Le drift accumulé est exponentiel sans contre-mesure.

## Related pages

- [progress-file-pattern](progress-file-pattern.md)
- [decision-log-pattern](decision-log-pattern.md)
- [compaction-vs-reset-strategie](compaction-vs-reset-strategie.md)
- [context-anxiety-modeles](context-anxiety-modeles.md)
- [session-clean-handoff](session-clean-handoff.md)
- [acid-principles-agent-state](acid-principles-agent-state.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
