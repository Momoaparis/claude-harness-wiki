# AI Font Generator (Lovart)

**Summary** : Fonctionnalité de Lovart permettant de générer une police typographique latine custom en ~3 min depuis une description texte ou une image de référence, stockée dans une bibliothèque réutilisable.

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Principe

Le Font Generator est accessible depuis la barre d'outils de Lovart (icône discrète, bas droite). Il accepte :
- Une **description textuelle** du style souhaité
- Une **image de référence** (optionnel)

Durée de génération : ~3 minutes. La police générée est automatiquement sauvegardée dans "My Fonts" et disponible dans tous les projets futurs.

### Exemple documenté

Prompt utilisé par [[claude-opus-47]] :

> "A serif typeface with subtle brush-stroke texture. Heavy weight, with elegant tapered serifs that hint at Chinese stone-rubbing calligraphy. Like inscriptions on bronze ware or stone steles. Inspired by Black Myth: Wukong — oriental epic, dignified, weighty."

Police générée : **Bronze Calligraphy**
- Serif épais
- Texture pinceau subtile
- Brun-noir chaud (pas un noir pur)
- Terminaisons avec légère irrégularité "rouille"

Le nom **Bronze Calligraphy** a été choisi automatiquement par Lovart en extrayant les termes sémantiquement forts du prompt (`bronze ware` → `Bronze`, `calligraphy` → `Calligraphy`).

### Limites actuelles (avril 2026)

- **Latine uniquement** : pas de support CJK (chinois, japonais, coréen)
- Pour un projet nécessitant une police chinoise custom, il faut encore faire appel à un typographe

### Valeur produite

Pour un développeur ou non-designer :
- Avant : trouver une police "assez proche", payer une licence, ou faire appel à un typographe (~plusieurs semaines)
- Après : décrire l'intention en langage naturel, obtenir une police sur-mesure en 3 min

### Intégration dans le pipeline

Le Font Generator s'insère dans le pipeline [[ai-design-agent]] après le [[lovart-brand-kit|Brand Kit]] :
1. Brand Kit → philosophie + palette
2. **Font Generator** → typographie alignée avec la philosophie
3. Poster → utilise la police + la palette
4. PSD export → police incluse comme asset éditable

## Related pages

- [[lovart-brand-kit]]
- [[ai-design-agent]]
- [[claude-opus-47-lovart-brand-design-summary]]
