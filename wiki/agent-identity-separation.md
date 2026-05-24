# Séparation des identités d'agent

**Summary** : Ne jamais donner à un agent les mêmes comptes que toi. Compte dédié, token scopé court-lived, bot user — pour qu'un agent compromis ne devienne pas toi.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## La règle

> If your agent has the same accounts you do, a compromised agent is you.

L'agent doit avoir une identité propre, séparée :

- Pas le Gmail perso → `agent@yourdomain.com`
- Pas le Slack perso → bot user ou bot channel dédié
- Pas le token GitHub perso → token scopé, court-lived, ou compte bot
- Pas la même clé SSH → clé dédiée à l'agent, déployable et révocable

## Pourquoi c'est différent du sandboxing

[[agent-sandboxing|Sandboxing]] limite ce que l'agent peut **faire localement** quand il est compromis. La séparation d'identités limite ce qu'il peut **faire à distance** via les services tiers auxquels il est connecté.

Les deux sont nécessaires. Ils ne se remplacent pas.

## Application concrète

- **Credentials short-lived** : tokens de 1h plutôt que des PAT GitHub permanents. AWS STS plutôt qu'access keys.
- **Scope minimal** : un repo, pas l'org. Un canal Slack, pas le workspace. Une boîte mail, pas tous tes contacts.
- **Révocation rapide** : un agent compromis se neutralise par révocation côté serveur — pas par confiance dans `Ctrl+C`.
- **Audit log distinct** : les actions de l'agent doivent apparaître séparément dans tes logs (mailbox, GitHub audit log, Slack admin). Cf. [[agent-observability]].

## Anti-pattern courant

Cloner un repo tiers et le laisser tourner avec son propre `git` configuré sur ton compte personnel. Si le repo contient des [[claude-code-cves-2026|hooks malveillants]], ton compte personnel est immédiatement exposé.

## Related pages

- [[agent-sandboxing]]
- [[least-agency]]
- [[lethal-trifecta]]
- [[the-agentic-security-summary]]
