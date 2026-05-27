# Claude Opus 4.7

**Summary** : Modèle Claude de génération 4.7, caractérisé par un mécanisme de self-verification, un benchmark de perception visuelle fortement amélioré et un comportement d'exécution autonome dit "codexy".

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Améliorations clés vs Opus 4.6

| Dimension | Opus 4.6 | Opus 4.7 |
|-----------|----------|----------|
| Perception visuelle (benchmark) | 54.5% | **98.5%** |
| Taux d'erreur long-task (outil calls enchaînés) | référence | **−1/3** |

La perception visuelle bondit de ~45 points : le modèle peut lire, analyser et juger des images (screenshots d'interface, exports visuels) avec une fiabilité radicalement supérieure.

### Mécanisme de self-verification

Voir [self-verification-mechanism](self-verification-mechanism.md). Après chaque tâche longue, Opus 4.7 se relit et réévalue le résultat avant de rendre la main. S'il juge la sortie insuffisante, il relance une nouvelle tentative sans attendre l'utilisateur.

Exemple documenté : génération de vidéo Seedance → première version jugée "trop dramatique, pas assez sobre" → deuxième version produite autonomement → validée.

### Comportement "codexy"

Terme utilisé par des ingénieurs OpenAI pour décrire un style d'exécution très autonome, procédural et déterminé : Opus 4.7 enchaîne les actions comme un script, sans demander confirmation à chaque étape. Adapté aux tâches de type "agent long-running".

Implications :
- Moins d'interruptions pour validation intermédiaire
- Meilleure tolérance aux obstacles (retry automatique)
- Risque : peut prendre des décisions autonomes inattendues (ex: placer un sceau en haut plutôt qu'en bas — décision culturellement fondée mais non demandée)

### Utilisation via Chrome MCP

Voir [claude-code-chrome-flag](claude-code-chrome-flag.md). Opus 4.7 peut piloter un navigateur Chrome local via MCP pour interagir avec des interfaces web (ex: Lovart, Figma) sans que l'utilisateur manipule l'interface.

Améliorations Computer Use vs 4.6 :
- Les tentatives précédentes (Opus 4.6 + browser extension, Computer Use, browser MCP) étaient systématiquement insuffisantes
- Avec Opus 4.7, le pipeline brand design complet via Lovart a fonctionné sans intervention

### Positionnement dans la hiérarchie

Voir [model-selection-claude](model-selection-claude.md).
- **Haiku** : tâches répétitives, worker agents
- **Sonnet** : défaut coding (90% des cas)
- **Opus 4.7** : tâches visuelles, long-running agents, décisions architecturales

## Related pages

- [self-verification-mechanism](self-verification-mechanism.md)
- [claude-code-chrome-flag](claude-code-chrome-flag.md)
- [model-selection-claude](model-selection-claude.md)
- [ai-design-agent](ai-design-agent.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
