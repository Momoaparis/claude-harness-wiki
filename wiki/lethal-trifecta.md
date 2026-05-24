# Lethal Trifecta

**Summary** : Cadre conceptuel de Simon Willison pour identifier quand un agent devient exploitable. Une fois que **données privées + contenu non fiable + communication externe** coexistent dans le même runtime, le prompt injection devient exfiltration de données.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`, séries Simon Willison sur le prompt injection

**Last updated** : 2026-05-23

---

## Les trois ingrédients

| # | Ingrédient | Exemple |
|---|------------|---------|
| 1 | **Private data** | accès au home, secrets, mails, repos privés, mémoire long-terme |
| 2 | **Untrusted content** | PDF d'un mail, page web, issue GitHub, output d'un MCP, attachement |
| 3 | **External communication** | n'importe quelle capacité d'I/O sortant (HTTP, push git, webhook, mail) |

Tant qu'un seul est absent, l'exfiltration ne fonctionne pas. Quand les trois sont réunis, le [[prompt-injection-sanitization|prompt injection]] cesse d'être une démo amusante et devient un vecteur de fuite.

## Utilité opérationnelle

Le cadre sert d'**outil de diagnostic** avant tout workflow :

1. Lister ce que l'agent peut **lire** (privé ou pas ?).
2. Lister d'où vient le **contenu** qu'il va ingérer (de confiance ou non ?).
3. Lister ce qu'il peut **émettre** vers l'extérieur.

Si la réponse est « les trois », l'agent doit tourner en [[agent-sandboxing|sandbox isolé]], ou bien la pipeline doit être scindée (cf. ci-dessous).

## Pattern de scission

Une parade classique : séparer la phase d'**extraction** (sur contenu non fiable, sans permissions) de la phase d'**action** (avec permissions, mais sur entrée déjà nettoyée).

> One agent can parse a document in a restricted environment. Another agent, with stronger approvals, can act only on the cleaned summary.

C'est l'application du [[least-agency|principe de moindre agence]] à l'architecture d'un workflow.

## Pourquoi c'est plus utile que « least privilege »

« Least privilege » se pense en permissions techniques (read/write/exec). Le lethal trifecta se pense en **flux de confiance** : qui parle à qui, qui traite quoi. C'est ce niveau qu'attaquent réellement les exploits de 2026.

## Related pages

- [[prompt-injection-sanitization]]
- [[least-agency]]
- [[agent-sandboxing]]
- [[agent-memory-hygiene]]
- [[the-agentic-security-summary]]
