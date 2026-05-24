# Continuous Learning v2 (instinct-based)

**Summary** : Évolution du [[continuous-learning-skill|système v1]] (Stop-hook learned-skill). v2 introduit la notion d'**instincts** : patterns appris avec score de confidence, importables, exportables, et clusterables en skills via `/evolve`.

**Sources** : `raw/ingested/affaan-m-ecc-readme-part*.md`

**Last updated** : 2026-05-23

---

## Différence avec v1

v1 ([[continuous-learning-skill]]) écoutait le hook `Stop` pour extraire les patterns d'une session en fin de session.

v2 introduit un modèle plus riche :

- **Instinct** = pattern observé avec un **score de confidence**.
- Les instincts s'accumulent au fil des sessions.
- Ils peuvent être **importés / exportés** entre utilisateurs.
- Quand assez d'instincts liés s'accumulent, `/evolve` les **cluster en skills**.

## Commandes

| Commande | Effet |
|----------|-------|
| `/instinct-status` | Affiche les instincts appris avec leur confidence |
| `/instinct-import <file>` | Importe les instincts d'un autre utilisateur |
| `/instinct-export` | Exporte tes instincts pour les partager |
| `/evolve` | Cluster les instincts liés en skills réutilisables |

## Implications

### Mémoire persistée → vecteur d'attaque potentiel

Les instincts sont **persistés** entre sessions — ils sont donc soumis aux mêmes risques que tout autre canal de mémoire long-terme :

- [[agent-memory-hygiene|AI Recommendation Poisoning]] : un instinct injecté via une session compromise peut influencer toutes les sessions futures.
- L'import d'instincts tiers (`/instinct-import`) est un acte de supply chain — voir [[toxicskills-study]].

Recommandation : reset des instincts après tout run non fiable, et scanner les fichiers d'import via [[agentshield]] avant `/instinct-import`.

### Pas un remplacement systématique de v1

Le README ECC précise :

> Keep `continuous-learning/` only when you explicitly want the legacy v1 Stop-hook learned-skill flow.

v1 et v2 cohabitent — choisir selon le besoin.

## Lien avec le reste du wiki

- [[continuous-learning-skill]] — v1, parent.
- [[agent-memory-hygiene]] — risques mémoire long-terme.
- [[toxicskills-study]] — supply chain des artefacts partagés.
- [[ecc-overview]] — écosystème global.

## Related pages

- [[continuous-learning-skill]]
- [[agent-memory-hygiene]]
- [[toxicskills-study]]
- [[ecc-overview]]
