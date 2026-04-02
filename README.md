# Gigabrain Playbooks

Ready-to-go agent configurations for [Gigabrain](https://gigabrain.gg) SuperAgents. Each playbook is a complete agent product — pick one, launch it, and the agent onboards itself through an interactive conversation.

## Playbooks

| Playbook | Category | Description |
|---|---|---|
| `degen-claw-competitor` | virtuals | Trade perps in the Virtuals Degen Claw competition via ACP |
| `smart-copy` | trading | Monitors whale wallets on HyperLiquid, copies trades after Brain API confirmation |
| `morning-briefing` | research | Daily market intel briefing delivered to your Telegram |
| `signal-trader` | trading | Scans for alpha signals, trades only when multiple signals align |
| `narrative-trader` | trading | Identifies emerging narratives early, exits when sentiment peaks |
| `macro-monitor` | risk | Persistent macro risk monitor — alerts on regime shifts |
| `polymarket-researcher` | polymarket | Deep thesis building on prediction markets |
| `portfolio-manager` | portfolio | Daily reviews, position monitoring, and rebalancing recommendations |
| `smart-dca` | accumulation | Regime-aware DCA — buys heavy on dips, skips when overextended |

## How It Works

Each playbook is a folder with:

- `playbook.yaml` — Manifest with metadata and skill dependencies
- `README.md` — What the agent does, example output, prerequisites
- `soul.md` — Agent identity and personality
- `bootstrap.md` — Interactive onboarding conversation the agent runs on first boot

Some playbooks also include:

- `scripts/` — Playbook-specific scripts for complex logic

### playbook.yaml

```yaml
name: degen-claw-competitor
description: Trade perps in the Virtuals Degen Claw competition via ACP
category: virtuals
icon: "🎮"
author: gigabrain
version: "1.0"

skills:
  - brain
  - https://github.com/Virtual-Protocol/openclaw-acp
  - https://github.com/Virtual-Protocol/dgclaw-skill
```

Skills are resolved at boot:
- **Plain name** (e.g., `brain`) — loaded from [`GigabrainGG/skills`](https://github.com/GigabrainGG/skills)
- **URL** (e.g., `https://github.com/Virtual-Protocol/dgclaw-skill`) — cloned from GitHub on first boot

### Launch Modes

| Mode | Input | What happens |
|------|-------|--------------|
| **Playbook** | Pick from the UI or paste a GitHub URL | Agent gets soul.md + bootstrap.md, runs interactive onboarding |
| **Custom soul.md** | Write your own | No bootstrap — you drive the agent |
| **Blank** | Nothing | Empty agent, full control |

## Relationship to Skills

Playbooks reference [skills](https://github.com/GigabrainGG/skills) but don't bundle them. Skills are building blocks (tools). Playbooks are finished products that compose skills together.

## Using a Playbook

1. Browse playbooks in this repo
2. Pick one — read its README for details
3. Launch a SuperAgent with the playbook URL (or pick from the curated list in the UI)
4. The agent boots up and walks you through setup via chat

## Custom Playbooks

Anyone can create a playbook:

1. Create a folder with `soul.md` + `bootstrap.md`
2. Push to any GitHub repo
3. Paste the URL when launching a SuperAgent

Fork an existing playbook to customize it. Version-pin with a branch, tag, or commit.

## Contributing

1. Create a folder with your playbook name
2. Add `playbook.yaml`, `README.md`, `soul.md`, and `bootstrap.md`
3. Open a PR
