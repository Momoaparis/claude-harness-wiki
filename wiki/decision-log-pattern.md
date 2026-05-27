# Decision log pattern (DECISIONS.md)

**Summary** : Journal append-only des décisions prises pendant le projet, avec leur raison et les alternatives rejetées. Capture le "pourquoi" qui sinon disparaît à la compaction de session. Permet aux sessions futures de ne pas re-débattre les mêmes choix.

**Sources** : `raw/ingested/lecture-05-keeping-context-alive-across-sessions.md`

**Last updated** : 2026-05-24

---

## Contenu

### Le problème résolu

Le code écrit pendant une session reste dans git. Mais le **pourquoi** disparaît :

- "Pourquoi avons-nous choisi Postgres et pas DynamoDB ?"
- "Pourquoi cette API renvoie un 202 et pas un 200 ?"
- "Pourquoi le tarif premium est plafonné à 99€ ?"

Sans log durable, la session N+5 va proposer de "refactorer" cette décision sans connaître ses contraintes, et probablement la casser.

### Le format standard (Lecture 05)

```markdown
# Decision Log

Append-only. Toute décision architecturale, produit, ou opérationnelle est tracée ici.

---

## 2026-05-24 — Use Postgres for user storage

**Decision**: Postgres comme DB primaire pour users.

**Reason**: Relations complexes (orgs, teams, permissions) + besoins de joins. Notre charge est < 10K writes/s, Postgres suffit largement.

**Rejected alternatives**:
- DynamoDB : équipe pas formée, pricing model coûteux pour les joins fréquents
- MongoDB : pas de transactions ACID au moment de la décision

**Constraints**:
- Doit supporter row-level security
- Doit fonctionner en Aurora (managed)

---

## 2026-05-23 — Auth tokens valid 15 min

**Decision**: Access tokens JWT, expiration 15 min. Refresh tokens 30j.

**Reason**: Compromis entre sécurité (revocation rapide) et UX (pas re-login toutes les minutes). Bench OWASP recommends 15-30 min.

**Rejected alternatives**:
- Tokens longs (24h) : risque sécurité trop élevé
- Tokens courts (5 min) : pression DDoS sur l'auth service

**Constraints**:
- Refresh token doit être révocable
- Pas de stockage côté serveur (stateless)

---
```

### Les champs essentiels

| Champ | Pourquoi |
|-------|----------|
| **Date** | Contextualiser dans le temps |
| **Decision** | Une phrase, pas un essai |
| **Reason** | Le "pourquoi" — c'est ça qu'on capture |
| **Rejected alternatives** | Pour éviter qu'on les re-propose plus tard |
| **Constraints** | Ce qui doit rester vrai pour que la décision tienne |

### Append-only — pourquoi

Une décision peut être **remplacée** mais pas **réécrite** :

```markdown
## 2026-05-24 — Use Postgres for user storage
[décision originale]

---

## 2026-08-15 — SUPERSEDES 2026-05-24 : Migrate to CockroachDB

**Decision**: Migrate user storage Postgres → CockroachDB.
**Reason**: Charge a quadruplé, sharding Postgres devient compliqué.
**Note**: Supersedes décision du 2026-05-24.
```

Conserver l'historique permet de comprendre la trajectoire et d'éviter les régressions.

### Quand ajouter une entrée

| Type de décision | Logger ? |
|------------------|----------|
| Choix de techno (DB, framework, language) | **Oui** |
| Choix d'architecture (monolith vs microservices) | **Oui** |
| Trade-off produit (feature A vs feature B) | **Oui** |
| Politique sécurité (TTL tokens, rate limits) | **Oui** |
| Convention de nommage | Plutôt en topic doc |
| Refactor mineur | Non |
| Bug fix simple | Non |

Critère : "si on supprime cette décision du log, quelqu'un dans 6 mois pourrait la re-proposer en pensant qu'elle n'a jamais été considérée ?"

### Le piège de la "spec inline"

Tentation : mettre le pourquoi dans les commentaires de code.

```js
// We chose Postgres because... [3 paragraphs]
const db = new PostgresClient(...)
```

Problèmes :
- Le commentaire vit dans **un seul fichier**, mais la décision concerne tout le système
- Lors d'un refactor, le commentaire est supprimé avec le code → décision perdue
- Pas découvrable par recherche globale

`DECISIONS.md` au root = lieu unique, durable, recherchable.

### Workflow

**Pendant une session** : quand une décision non-triviale est prise, l'agent (ou l'humain) ajoute une entrée au log avant de continuer.

**Fin de session** : check que toutes les décisions prises ont été tracées (voir [template-clean-state-checklist](template-clean-state-checklist.md)).

**Démarrage de session N+1** : l'agent lit `DECISIONS.md` (au moins les dernières N entrées) pour comprendre le terrain.

### ADR (Architecture Decision Records)

`DECISIONS.md` est une version simplifiée des ADRs (Architecture Decision Records, proposé par Michael Nygard 2011). Si le projet veut plus de structure :

- 1 fichier par décision : `docs/adr/0001-use-postgres.md`
- Format ADR standard (Context / Decision / Status / Consequences)
- Tooling : `adr-tools`

`DECISIONS.md` monolithique est suffisant pour démarrer. Migrer vers ADR par fichier quand le log dépasse ~30 entrées.

### Lien avec progress file

| Fichier | Granularité | Contenu |
|---------|-------------|---------|
| [PROGRESS.md](progress-file-pattern.md) | Par session | Quoi fait, quoi prévu |
| `DECISIONS.md` | Par décision | Pourquoi tel choix |

Les deux sont complémentaires. Une session peut générer 0 ou plusieurs décisions ; la session change toujours le PROGRESS, mais pas toujours le DECISIONS.

### À retenir

1. **Append-only**. On ne réécrit jamais une décision passée.
2. **Decision / Reason / Rejected / Constraints** = format minimal.
3. Capturer le **pourquoi**, pas le quoi (le code dit le quoi).
4. Logger les décisions **non-triviales**, pas les choix mineurs.
5. Une décision remplacée → nouvelle entrée "SUPERSEDES YYYY-MM-DD".

## Related pages

- [progress-file-pattern](progress-file-pattern.md)
- [cross-session-context-loss](cross-session-context-loss.md)
- [acid-principles-agent-state](acid-principles-agent-state.md)
- [session-clean-handoff](session-clean-handoff.md)
- [the-harness-engineering-curriculum-summary](the-harness-engineering-curriculum-summary.md)
