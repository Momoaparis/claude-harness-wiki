# Claude Opus 4.7 + Lovart : Pipeline Brand Design Complet

**Summary** : Retour d'expérience sur l'utilisation de Claude Opus 4.7 via `--chrome` MCP pour piloter Lovart et produire une identité visuelle complète (Brand Kit, police, PSD, Skill, vidéo) de manière autonome.

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contexte

Auteur : J0hn (compte WeChat "AGI Hunt"), 17 avril 2026. Projet : créer une identité visuelle pour "国宝回家" (National Treasure Homecoming), une initiative publique de numérisation de pièces culturelles chinoises perdues à l'étranger.

Contrainte : l'auteur est développeur, pas designer. Après 7 tentatives infructueuses avec d'autres outils, il teste [claude-opus-47](claude-opus-47.md) couplé à Lovart.

## Workflow

### Setup

Claude Code avec le flag `--chrome` connecte [claude-opus-47](claude-opus-47.md) au Chrome local (déjà authentifié sur Lovart) via MCP. L'auteur fournit un dossier de contexte projet et donne une instruction générale. Il va boire du thé.

### Étape 1 — Brand Kit

[lovart-brand-kit](lovart-brand-kit.md) parse un PDF de 47 Mo (IP手册 de *Black Myth: Wukong*) et en extrait :
- Design philosophy : "Oriental Epic, UE5 réalisme + calligraphie + symboles bouddhistes/taoïstes"
- Couleurs nommées : `Brand Deep Black`, `Calligraphy White`, `Stamp Red`
- Assets : logos, visuels personnages, images d'ambiance

Opus 4.7 choisit lui-même ce PDF parmi plusieurs options disponibles, jugeant que le thème culturel et la palette (encre noire, rouge cinabre, blanc papier de riz) correspondaient parfaitement au projet.

### Étape 2 — Poster principal

Opus 4.7 rédige le prompt Lovart sans intervention humaine. Résultat : poster vertical 3:4 avec calligraphie, gardien en armure, architecture classique, bronze, lumière dorée. Seul écart : le sceau rouge placé en haut à droite (tradition calligraphique) plutôt qu'en bas à droite (comme demandé) — décision autonome de Lovart, culturellement plus correcte.

### Étape 3 — Font Generator

[ai-font-generator](ai-font-generator.md) génère la police **Bronze Calligraphy** (~2min30) : serif épais à texture pinceau, inspiré des inscriptions sur bronzes rituels. La police est sauvegardée dans "My Fonts" et réutilisable sur tous les projets.

### Étape 4 — Create Skill

Lovart propose de convertir la conversation en [Skill](prompt-as-asset.md) réutilisable. Nommé automatiquement : **Game IP Charity Campaign Design**. Stocké dans Skill Book pour usages futurs.

### Étape 5 — Export PSD

[Export PSD](ai-design-agent.md) produit un fichier Photoshop avec couches éditables et nommage sémantique (ex: "国宝回家公益海报", "Text: LOVART"), pas un PNG aplati.

### Étape 6 — Vidéo Seedance 2.0

[seedance-video-gen](seedance-video-gen.md) génère un plan de 5 secondes. Première version jugée insuffisante par Opus 4.7 lui-même ([self-verification-mechanism](self-verification-mechanism.md)) — trop "temple dramatique", pas assez sobre. Deuxième version : ding en bronze sur fond lavis d'encre, lumière dorée, pétales tombant. Approuvée.

## Bilan

**Résultat** : Brand Kit, poster, police custom, Skill, PSD éditable, vidéo 5 sec — tout produit en une session autonome.

**Qualité estimée** : ~80/100. Pas directement livrable (sceau illisible, quelques ajustements de composition), mais base solide pour 15-20 min de retouche par un designer.

**Coût humain** : 2 interactions — décrire la tâche + approuver la version finale.

**Concept clé** : la chaîne Brand Kit → visuel → police → Skill → PSD constitue un **pipeline d'ingénierie de marque** (brand-config schema), pas une succession d'outils isolés.

## Related pages

- [claude-opus-47](claude-opus-47.md)
- [claude-code-chrome-flag](claude-code-chrome-flag.md)
- [lovart-brand-kit](lovart-brand-kit.md)
- [ai-font-generator](ai-font-generator.md)
- [prompt-as-asset](prompt-as-asset.md)
- [ai-design-agent](ai-design-agent.md)
- [self-verification-mechanism](self-verification-mechanism.md)
- [seedance-video-gen](seedance-video-gen.md)
