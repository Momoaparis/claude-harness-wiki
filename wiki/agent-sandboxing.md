# Sandboxing des agents

**Summary** : Si l'agent est compromis, le rayon d'explosion doit rester petit. Sandboxing = containers / VMs / devcontainers avec réseau interne et permissions minimales. Anthropic et OpenAI convergent sur cette pratique.

**Sources** : `raw/ingested/the-shorthand-guide-to-everything-agentic-security.md`

**Last updated** : 2026-05-23

---

## Pourquoi isoler

Root access est dangereux. Accès large au filesystem local est dangereux. Credentials long-lived sur la même machine que l'agent sont dangereux. La règle :

> If the agent gets compromised, the blast radius needs to be small.

C'est la mise en œuvre concrète du [[least-agency|principe de moindre agence]] au niveau infrastructure.

## Docker Compose avec réseau interne

```yaml
services:
  agent:
    build: .
    user: "1000:1000"
    working_dir: /workspace
    volumes:
      - ./workspace:/workspace:rw
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    networks:
      - agent-internal

networks:
  agent-internal:
    internal: true
```

`internal: true` est la pièce critique. Sans route vers l'extérieur, un agent compromis ne peut pas « phoner home » — ce qui casse le 3ᵉ pilier du [[lethal-trifecta]].

## Container ponctuel pour repo review

```bash
docker run -it --rm \
  -v "$(pwd)":/workspace \
  -w /workspace \
  --network=none \
  node:20 bash
```

`--network=none` + montage limité au workspace = même un repo poisonné ne peut rien faire de pire que casser son propre workspace.

## Restrictions de permissions

Dans `~/.claude/settings.json`, deny-rules au minimum :

```json
{
  "permissions": {
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(**/.env*)",
      "Write(~/.ssh/**)",
      "Write(~/.aws/**)",
      "Bash(curl * | bash)",
      "Bash(ssh *)",
      "Bash(scp *)",
      "Bash(nc *)"
    ]
  }
}
```

Pas une politique complète, mais une bonne baseline « ROI maxxé out » selon le guide.

## Convergence de l'industrie

- **Anthropic** recommande explicitement containers / devcontainers.
- **OpenAI Codex** : per-task sandboxes avec network approval explicite.
- **GitHub Copilot coding agent** : firewall allowlistable.

Tout le monde admet désormais que l'isolation est la défense baseline, pas une option avancée.

## Related pages

- [[lethal-trifecta]]
- [[least-agency]]
- [[agent-identity-separation]]
- [[claude-code-cves-2026]]
- [[the-agentic-security-summary]]
