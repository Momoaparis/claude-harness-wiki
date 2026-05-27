# Hygiène mémoire des agents

**Summary** : La mémoire persistante est utile — et c'est aussi de l'essence. Les attaques de poisoning n'ont plus besoin de gagner d'un coup : elles plantent des fragments, attendent, et s'assemblent plus tard. Garder la mémoire narrow, jetable, et compartimentée.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`, Microsoft *AI Recommendation Poisoning* (10 fév 2026)

**Last updated** : 2026-05-23

---

## L'attaque mémoire (Microsoft, fév 2026)

Microsoft a documenté en février 2026 une attaque baptisée **AI Recommendation Poisoning** : un attaquant cache des instructions dans du contenu (blog post, doc). L'utilisateur clique « Résumer avec IA ». L'instruction cachée passe en mémoire de l'agent. **Plus tard**, l'agent ressort cette instruction sous forme de recommandation, biaisant le comportement.

Documenté sur 31 entreprises, 14 industries.

## Pourquoi c'est plus dangereux qu'un prompt injection one-shot

- Le payload **n'a plus besoin** de réussir dans la conversation où il est injecté.
- Il survit aux compactages, aux resets de session, aux changements d'utilisateur.
- Personne ne va auditer ces vieux fichiers `.md` dans la knowledge base.
- L'attaque devient **silencieuse et différée**.

## Lien direct avec Claude Code

Claude Code charge la mémoire au démarrage de session (`CLAUDE.md`, fichiers de projet, mémoire globale, etc.). C'est aussi vrai pour [le triplet PreCompact/SessionStart/Stop](memory-persistence-hooks.md) côté pattern, et pour [les fichiers .tmp persistés](session-storage-pattern.md).

Toute persistance est un canal de poisoning potentiel.

## Règles minimales

- **Pas de secrets** dans les fichiers mémoire — ils peuvent fuiter via le contexte.
- **Séparer la mémoire projet de la mémoire user-global** — ne pas laisser un repo non fiable polluer ta mémoire perso.
- **Reset ou rotation** après tout run non fiable (repo externe, document tiers).
- **Désactiver la mémoire long-lived** entièrement pour les workflows à haut risque (review de PRs étrangers, traitement d'attachements).

## Pattern courant à éviter

Un workflow qui traite des docs externes toute la journée **avec mémoire long-lived partagée** → c'est de la persistance offerte gratuitement à n'importe quel attaquant.

## Lien avec les autres défenses

- [prompt-injection-sanitization](prompt-injection-sanitization.md) : si tu nettoies l'input à l'entrée, le payload n'arrive pas en mémoire.
- [lethal-trifecta](lethal-trifecta.md) : la mémoire long-lived **est** une forme de "private data" — sa simple existence aggrave le trifecta.
- [continuous-learning-v2](continuous-learning-v2.md) : système instinct-based, à concevoir avec ces contraintes.

## Related pages

- [prompt-injection-sanitization](prompt-injection-sanitization.md)
- [lethal-trifecta](lethal-trifecta.md)
- [memory-persistence-hooks](memory-persistence-hooks.md)
- [session-storage-pattern](session-storage-pattern.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
