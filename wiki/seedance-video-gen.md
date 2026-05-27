# Seedance 2.0 — Génération Vidéo Text-to-Video

**Summary** : Modèle de génération vidéo text-to-video intégré à Lovart, capable de produire des clips de 5 secondes depuis un prompt en langage naturel (~5 min de génération).

**Sources** : `raw/ingested/claude-opus-47-lovart-brand-design.md`

**Last updated** : 2026-05-23

---

## Contenu

### Principe

Seedance 2.0 est un modèle vidéo accessible directement dans le canvas Lovart. Il accepte un prompt textuel en chinois ou anglais (traduction automatique si nécessaire) et génère un clip court (~5 sec).

### Workflow documenté

1. Rédiger un prompt décrivant la scène, le mouvement de caméra, la lumière, l'ambiance
2. Lovart traduit automatiquement en anglais si le prompt est en chinois
3. Génération (~5 min, parfois plus en cas de charge serveur)
4. Visionner le résultat directement dans le canvas
5. Si insatisfaisant : [Opus 4.7 peut relancer](self-verification-mechanism.md) avec un prompt affiné

### Exemple de prompt (version finale retenue)

> "Un ensemble de vases en bronze de la Chine ancienne (ding, gui, jue) se dressent tranquillement au centre d'une composition de paysage à l'encre. Le fond est une silhouette de montagnes lointaines et une brume qui monte lentement. La caméra avance très lentement depuis un angle en plongée. Une lumière dorée et chaude descend en diagonale depuis le haut du cadre, tombant sur la surface des bronzes. Une fine brume flotte lentement au sol. Quelques pétales tombent doucement dans l'air. Palette de couleurs : noir encre, or chaud, blanc papier de riz, touches de rouge cinabre."

Résultat : plan unique en plongée progressive, bronzes rituels sur fond lavis, lumière dorée, pétales tombant, sceaux rouges en coin.

### Contraintes connues

- **Durée fixe** : environ 5 secondes par génération
- **Personnages connus** : les personnages de marques déposées (ex: Sun Wukong de *Black Myth*) déclenchent une modération — utiliser des archétypes génériques à la place
- **Temps de génération** : 5 min en conditions normales, plus en cas de congestion

### Cas d'usage typique

Clips d'ambiance pour :
- Splash screens d'applications mobiles
- Introductions de présentations
- Stories réseaux sociaux
- Habillages vidéo courts

### Comparaison avec la production traditionnelle

Avant Seedance 2.0 (type de contenu identique) :
- Équipe tournage : plusieurs semaines, décors, lumière, postproduction
- Template After Effects : plusieurs heures, design + animation
- **Avec Seedance 2.0** : prompt texte + 5 minutes d'attente

Qualité estimée : suffisante pour prototype/MVP, pas encore pour livrable final broadcast.

## Related pages

- [ai-design-agent](ai-design-agent.md)
- [self-verification-mechanism](self-verification-mechanism.md)
- [lovart-brand-kit](lovart-brand-kit.md)
- [claude-opus-47-lovart-brand-design-summary](claude-opus-47-lovart-brand-design-summary.md)
