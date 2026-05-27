# Least Agency

**Summary** : Reformulation du « least privilege » pour les agents : le modèle ne doit jamais être l'autorité finale pour shell, network egress, writes hors workspace, lecture de secrets, ou workflow dispatch. La frontière de sécurité est la politique entre modèle et action — pas le system prompt.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## L'erreur classique

> Beaucoup de gens pensent que la safety boundary est le system prompt. **C'est faux.**

Le system prompt est un input parmi d'autres pour le modèle. Il est ignorable, contournable, écrasable par n'importe quel autre input avec assez de poids (cf. [prompt-injection-sanitization](prompt-injection-sanitization.md)). La vraie frontière est la **politique d'autorisation** qui s'interpose entre la décision du modèle et l'exécution.

## Le template GitHub Coding Agent

Le guide cite GitHub comme exemple concret de design défensif :

- Seuls les utilisateurs avec write access peuvent assigner du travail à l'agent.
- Les commentaires de privilège inférieur sont **exclus** du contexte.
- Les pushs de l'agent sont contraints.
- L'accès Internet peut être firewall-allowlisté.
- Les workflows requièrent quand même une approbation humaine pour s'exécuter.

C'est le modèle à copier localement.

## Ce que ça donne en pratique

Requérir une approbation avant :

- toute commande shell hors sandbox
- toute sortie réseau (egress)
- toute lecture de chemin contenant des secrets
- toute écriture hors du repo
- tout déclenchement de workflow ou déploiement

Si un workflow auto-approuve l'un de ces points, **il n'y a plus d'autonomie sûre** — juste une absence de frein. Le guide le formule durement :

> You're cutting your own brake lines and hoping for the best.

## Pourquoi « agency » plutôt que « privilege »

Le vocabulaire « least privilege » d'OWASP se focalise sur les permissions techniques. « Least agency » insiste sur la **marge de manœuvre** : combien de décisions autonomes l'agent peut prendre sans humain dans la boucle. C'est plus large — ça couvre aussi le scope, la mémoire, la durée de session, le nombre d'outils enabled.

## Anti-pattern

`claude --dangerously-skip-permissions` sur un loop. Comme noté dans [agent-kill-switches](agent-kill-switches.md), c'est aussi le moment où le mécanisme d'arrêt cesse de fonctionner.

## Related pages

- [lethal-trifecta](lethal-trifecta.md)
- [agent-sandboxing](agent-sandboxing.md)
- [agent-observability](agent-observability.md)
- [agent-kill-switches](agent-kill-switches.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
