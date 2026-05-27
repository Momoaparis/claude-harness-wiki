# Self-Verification (mécanisme Opus 4.7)

**Summary** : Capacité d'Opus 4.7 à évaluer de manière autonome le résultat d'une tâche qu'il vient de produire, et à se relancer si l'output est jugé insuffisant — sans attendre l'intervention de l'utilisateur.

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Définition

Le mécanisme de **self-verification** (自我验证) introduit dans [claude-opus-47](claude-opus-47.md) est une boucle d'auto-évaluation post-tâche :

1. L'agent produit un output (image, vidéo, code, etc.)
2. Il "relit" cet output avec son propre jugement
3. Si l'output répond aux critères → rend la main
4. Si l'output est insuffisant → produit une nouvelle tentative, explique pourquoi, sans demander à l'utilisateur

### Exemple documenté

Génération vidéo Seedance — première version :

Après analyse autonome de la première vidéo, Opus 4.7 a conclu :

> "Cette version penche trop vers 'temple dramatique', forte en tension mais pas assez sobre, en décalage avec le ton civique et solennel de 'National Treasure Homecoming'. Je recommande une nouvelle version : fond lavis d'encre épuré, bronzes rituels comme seul sujet, pour une narration culturelle orientale plus aérée."

→ Deuxième tentative lancée sans validation humaine → résultat approuvé.

### Implications pratiques

**Avantages :**
- Réduit les allers-retours utilisateur pour les corrections évidentes
- Permet au modèle d'apprendre de l'itération précédente dans la même session
- Améliore la qualité finale sans coût cognitif humain supplémentaire

**Limites :**
- La self-evaluation reste subjective (le modèle juge selon ses propres critères)
- Peut diverger des préférences réelles de l'utilisateur
- Augmente le temps total (deux tentatives au lieu d'une)

**Exemple de décision autonome** : Lovart a placé le sceau en haut à droite (tradition calligraphique) plutôt qu'en bas à droite (comme demandé). Ce n'est pas de la self-verification stricto sensu, mais illustre la même tendance vers l'autonomie décisionnelle culturellement fondée.

### Relation avec la perception visuelle

La self-verification sur des outputs visuels (images, vidéos) dépend directement du benchmark de perception visuelle du modèle. Avec un saut de 54.5% → 98.5% pour [claude-opus-47](claude-opus-47.md), le modèle peut réellement évaluer la qualité esthétique et la cohérence thématique d'un visuel.

### Comportement "codexy"

La self-verification contribue au comportement dit "codexy" : le modèle se comporte comme un script autonome qui vérifie ses propres assertions avant de terminer — analogue à une assertion `assert` ou un test unitaire intégré au workflow de production.

## Related pages

- [claude-opus-47](claude-opus-47.md)
- [ai-design-agent](ai-design-agent.md)
- [seedance-video-gen](seedance-video-gen.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
