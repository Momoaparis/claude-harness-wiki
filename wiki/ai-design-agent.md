# AI Design Agent vs Text-to-Image

**Summary** : Distinction entre un "design agent" (pipeline structuré produisant des assets éditables et réutilisables) et un simple outil de génération d'image (sortie morte, non modifiable).

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### La limite du text-to-image classique

Les outils de génération d'images (Midjourney, DALL·E, Stable Diffusion) produisent un **PNG aplati** :
- Pas de couches éditables
- Pas de gestion des assets de marque
- Pas de cohérence entre générations
- Le designer ne peut pas "continuer le travail" — il doit tout refaire depuis le prompt

Résultat : la collaboration humain-IA s'arrête à la sortie de l'image. L'IA produit un point de départ, mais le chemin jusqu'au livrable final reste entièrement humain.

### Ce que fait un design agent

Un **AI Design Agent** produit une chaîne complète d'assets exploitables :

| Étape | Output | Réutilisabilité |
|-------|--------|----------------|
| [Brand Kit](lovart-brand-kit.md) | Schéma de marque structuré | Projet entier |
| Poster / visuel | Image générée cohérente avec le Brand Kit | — |
| [Font Generator](ai-font-generator.md) | Police custom stockée dans My Fonts | Tous projets |
| [Create Skill](prompt-as-asset.md) | Workflow sérialisé dans Skill Book | Tous projets |
| Export PSD | Fichier Photoshop avec couches éditables | Designer |
| [Vidéo Seedance](seedance-video-gen.md) | Clip animé 5 sec | Application |

### Le PSD comme marqueur clé

L'export PSD illustre la différence fondamentale. Structure obtenue :

```
PSD — 1276x1200 px, RGB 8-bit
├── [0] '国宝回家公益海报'  — kind: pixel
└── [1] 'Text: LOVART'       — kind: type  ← couche texte éditable
```

- `kind: type` = couche texte Photoshop éditable (double-clic → modification directe)
- Nommage sémantique (pas "Layer 1 / Layer 2")
- Un designer peut ouvrir le fichier et affiner sans repartir de zéro

### Le modèle de collaboration

> "AI génère à 80%, designer affine à 95%, 15-20 min de retouche."

L'AI Design Agent déplace la contribution humaine : de "tout faire" à "valider et affiner". La valeur économique se retrouve dans la réduction du temps de production, pas dans l'élimination du designer.

### Lien avec [`--chrome` MCP](claude-code-chrome-flag.md)

[claude-opus-47](claude-opus-47.md) pilote Lovart via Chrome MCP : c'est l'agent qui orchestre le pipeline. Sans ce pilotage autonome, chaque étape nécessiterait une intervention humaine dans l'interface web.

## Related pages

- [lovart-brand-kit](lovart-brand-kit.md)
- [ai-font-generator](ai-font-generator.md)
- [prompt-as-asset](prompt-as-asset.md)
- [seedance-video-gen](seedance-video-gen.md)
- [claude-code-chrome-flag](claude-code-chrome-flag.md)
- [claude-opus-47](claude-opus-47.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
