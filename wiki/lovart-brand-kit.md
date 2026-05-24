# Lovart — Brand Kit

**Summary** : Fonctionnalité de Lovart qui parse un PDF de charte graphique existante et en extrait un schéma structuré de marque (couleurs, logos, philosophie design) utilisable sur tous les projets.

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Principe

Lovart Brand Kit résout le problème du "brand context" : comment faire en sorte qu'un outil de génération visuelle respecte une identité de marque cohérente sur l'ensemble d'un projet ?

La solution : **extraire la marque sous forme de schéma structuré** depuis un document existant (PDF de charte, brand handbook, rapport annuel), puis **attacher ce schéma à un projet**. Toute génération ultérieure hérite automatiquement du schéma.

### Analogie développeur

> "Comme un fichier brand-config.json : typage, réutilisabilité, une définition → effets globaux."

Le Brand Kit est l'équivalent d'un schéma de configuration de marque — typed, versionnable, applicable à l'échelle du projet.

### Ce que le parsing extrait

Exemple documenté (PDF de 47 Mo, *Black Myth: Wukong* IP handbook) :

| Catégorie | Contenu extrait |
|-----------|----------------|
| **Design philosophy** | Résumé en anglais : "Oriental Epic, UE5 réalisme + calligraphie + symboles bouddhistes/taoïstes" |
| **Logos** | Logo principal, version texte, sous-marques |
| **Couleurs** | `Brand Deep Black`, `Calligraphy White`, `Stamp Red` |
| **Assets visuels** | Environment Mood, Character Key Visual, Combat Action Shot |

Point notable : Lovart a nommé `Stamp Red` (印章红) en analysant les sceaux apparaissant dans les posters — pas une simple extraction de valeur hexadécimale, mais une **inférence sémantique** du rôle culturel de la couleur.

### Workflow

1. Uploader un PDF de marque connu **ou** partir d'une marque inconnue (Brand Kit vierge)
2. Lovart parse (~1 min pour 47 Mo)
3. Panel de résultats : vérifier les extractions
4. "Utiliser ce kit pour créer un projet" → schéma attaché au niveau projet
5. Toutes les générations suivantes dans ce projet héritent du schéma

### Limites connues

- Pas de support de marques inconnues sans document de référence (ou alors création manuelle)
- La fidélité de l'extraction dépend de la qualité du PDF source
- Ne remplace pas une charte graphique finalisée — c'est un point de départ pour l'idéation

### Lien avec l'identité de marque globale

Le Brand Kit est la première étape du pipeline complet :
Brand Kit → Poster → [[ai-font-generator|Font]] → [[prompt-as-asset|Skill]] → PSD → [[seedance-video-gen|Vidéo]]

Voir [[ai-design-agent]] pour la vision d'ensemble.

## Related pages

- [[ai-design-agent]]
- [[ai-font-generator]]
- [[prompt-as-asset]]
- [[claude-opus-47-lovart-brand-design-summary]]
