# Model Context Protocol (MCP)

**Summary** : Protocole standardisé qui permet à un agent comme Claude de se connecter à des outils et sources de données externes (serveurs MCP) exposant des tools, schémas et ressources. Pratique mais coûteux en tokens et partie intégrante de la surface d'attaque de l'agent.

**Sources** : The Longform Guide to Everything Claude Code.md, affaan-m-ecc-readme-part4-token-optimization.md, the-shorthand-guide-to-everything-agentic-security.md, lecture-11-making-the-agents-runtime-observable.md

**Last updated** : 2026-06-11

---

## Contenu

### Définition

Un **serveur MCP** expose à l'agent un ensemble de *tools* (fonctions appelables), de *schémas* et de *ressources* via un protocole commun. Une fois connecté, l'agent traite les descriptions de tools, leurs schémas et leurs sorties comme du **contexte de confiance** (source: the-shorthand-guide-to-everything-agentic-security.md).

C'est le mécanisme standard pour brancher Claude sur des systèmes externes : contrôle de version, bases de données, déploiement, navigateur, outils de test.

### Coût en contexte et en tokens

Chaque description de tool MCP **consomme des tokens** de la fenêtre de 200k. Activer trop de MCPs peut la réduire à ~70k tokens utiles (source: affaan-m-ecc-readme-part4-token-optimization.md).

Bonnes pratiques de gestion (source: affaan-m-ecc-readme-part4-token-optimization.md) :
- Garder **moins de 10 MCPs** activés par projet
- `/mcp` pour désactiver les serveurs inutilisés ; les choix runtime persistent dans `~/.claude.json`
- `ECC_DISABLED_MCPS` pour filtrer les configs MCP générées par ECC lors de l'install/sync

Voir [ecc-token-optimization](ecc-token-optimization.md) pour le tableau complet des leviers.

### Lazy loading

Les progrès récents de Claude Code (équipe Boris Cherny) rendent les MCPs **lazy-loaded** : ils ne consomment plus de contexte dès l'init (source: The Longform Guide to Everything Claude Code.md). Cela résout en grande partie le problème de **fenêtre de contexte**, mais **pas** celui du **coût en tokens** lors des opérations heavy.

### MCP vs CLI + skills

Beaucoup de MCPs ne sont que des wrappers autour de CLIs existantes (GitHub → `gh`, Supabase, Vercel, Railway). Les remplacer par des skills/commandes qui appellent la CLI directement libère du contexte (source: The Longform Guide to Everything Claude Code.md). C'est le pattern détaillé dans [mcp-vs-cli-skills](mcp-vs-cli-skills.md).

Arbitrage rapide :

| Cas | Approche |
|-----|----------|
| Opération légère, fréquente | MCP (lazy-loaded) |
| Opération heavy en output (DB, deploy) | CLI + skill hors contexte |
| Interface uniquement web (pas de CLI) | MCP irremplaçable |

### Cas où le MCP est irremplaçable

Quand aucune CLI n'existe — par exemple piloter un navigateur authentifié via le flag [`--chrome`](claude-code-chrome-flag.md), ou interagir avec une app web qui n'expose pas d'API. Les agents évaluateurs utilisent aussi **Playwright MCP** pour tester une app en cours d'exécution comme un vrai utilisateur (source: lecture-11-making-the-agents-runtime-observable.md). Voir [agent-observability](agent-observability.md).

### MCP comme surface d'attaque

Dès que l'agent traite les descriptions, schémas et sorties de tools comme du contexte de confiance, **la toolchain elle-même devient une surface d'attaque** (source: the-shorthand-guide-to-everything-agentic-security.md). OWASP maintient désormais un **MCP Top 10** couvrant : tool poisoning, prompt injection via payloads contextuels, command injection, *shadow MCP servers*, exposition de secrets.

Risques structurels :
- Les serveurs MCP project-scoped vivent dans `.mcp.json`, partagés via le source control → frontière de confiance attaquable (source: the-shorthand-guide-to-everything-agentic-security.md)
- **MCP consent abuse** : config repo-controlled pouvant auto-approuver des serveurs avant que l'utilisateur ait réellement fait confiance au répertoire

Ces vecteurs s'articulent avec la [lethal-trifecta](lethal-trifecta.md) (données privées + contenu non fiable + communication externe) et le principe de [least-agency](least-agency.md). Voir [the-agentic-security-summary](the-agentic-security-summary.md) et [prompt-injection-sanitization](prompt-injection-sanitization.md).

## Related pages

- [mcp-vs-cli-skills](mcp-vs-cli-skills.md)
- [claude-code-chrome-flag](claude-code-chrome-flag.md)
- [ecc-token-optimization](ecc-token-optimization.md)
- [claude-code-plugins](claude-code-plugins.md)
- [lethal-trifecta](lethal-trifecta.md)
- [the-agentic-security-summary](the-agentic-security-summary.md)
