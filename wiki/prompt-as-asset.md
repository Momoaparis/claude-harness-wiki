# Prompt-as-Asset (vs Prompt-as-Craft)

**Summary** : Pattern consistant à persister une conversation AI réussie en tant que skill réutilisable, passant du "prompt artisanal" (recréé à chaque fois) au "prompt capitalisé" (versionné, réutilisable, transmissible).

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Le problème : prompt-as-craft

Dans le mode par défaut d'utilisation d'un LLM, chaque session repart de zéro :
- L'utilisateur reconstruit mentalement le contexte
- Le prompt est retapé ou légèrement modifié à la main
- Les "bonnes formulations" restent dans la mémoire humaine, pas dans le système

C'est le **prompt-as-craft** : une compétence tacite, personnelle, non-transmissible.

### La solution : prompt-as-asset

Une conversation réussie devient un **asset persisté** :
- Sauvegardée comme Skill (Lovart), template, ou preset
- Nommée de manière sémantique
- Réutilisable sur d'autres projets similaires
- Potentiellement partageable avec d'autres utilisateurs

**Analogie développeur** : comme sauvegarder une requête SQL complexe dans un fichier `queries/`, plutôt que la reconstruire à chaque fois depuis la mémoire.

### Implémentation dans Lovart (Create Skill)

Après une session de design satisfaisante, Lovart propose "Créer un Skill à partir de cette conversation". Le système :
1. Analyse la conversation
2. Extrait les intentions, le contexte, les paramètres clés
3. Génère un nom sémantique en 3 mots
4. Pré-remplit un template de prompt pour usage futur

Exemple documenté : **Game IP Charity Campaign Design**
- "Game IP" ← source du Brand Kit (Black Myth: Wukong)
- "Charity Campaign" ← nature du projet (公益)
- "Design" ← type de tâche

### Comparaison avec les Skills Claude Code

Ce pattern est identique à la notion de [skills](continuous-learning-v2.md) dans les systèmes d'agents :
- Claude Code : skills = fichiers `.md` dans `.claude/skills/` décrivant un workflow
- Lovart : skills = conversations sérialisées dans un Skill Book

La logique sous-jacente est la même : **capitaliser le chemin de réussite, pas seulement le résultat**.

### Valeur économique

> "Économiser du temps de 'remise en route' et des tokens de réexploration."

Quand un utilisateur reprend un projet similaire, invoquer le Skill pré-remplit le contexte au lieu de le reconstruire — économie directe en tokens et en temps cognitif.

### Lien avec [metaprompting](metaprompting.md)

[metaprompting](metaprompting.md) consiste à investir dans la qualité du prompt initial pour maximiser la qualité de la tâche. Le prompt-as-asset est la suite logique : une fois le "bon prompt" trouvé, le persister plutôt que de le reconstruire à chaque fois.

## Related pages

- [metaprompting](metaprompting.md)
- [continuous-learning-v2](continuous-learning-v2.md)
- [lovart-brand-kit](lovart-brand-kit.md)
- [ai-design-agent](ai-design-agent.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
