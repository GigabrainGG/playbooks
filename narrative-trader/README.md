# Narrative Trader

Identifies emerging crypto narratives early, enters tokens before they run, exits when sentiment peaks.

## What This Agent Does

- Scans every 6 hours for crypto narratives across sectors (AI, DeFi, L2, memes, RWA)
- Tracks narrative lifecycle: building → early momentum → peak attention → euphoria → overcooked
- Enters during "building" or "early momentum" stages with validated catalysts
- Monitors sentiment progression on open positions every 4 hours
- Exits at "euphoria" or "overcooked" — doesn't try to catch the top
- Validates catalysts via web search before entering

## Sentiment Stages

| Stage | Action |
|-------|--------|
| Building | Best entry — few talking, catalyst upcoming |
| Early Momentum | Good entry with tighter stops |
| Peak Attention | Take profit zone (50%) |
| Euphoria | Exit remaining position |
| Overcooked | Do not enter |

## Onboarding Flow

1. Choose sectors to monitor (AI, DeFi, L2, memes, RWA, or all)
2. Set max allocation per narrative and max concurrent narratives
3. Choose risk tolerance (conservative, moderate, aggressive)
4. Set max position size per token
5. Choose trading mode (autonomous, confirm, or alert only)
6. See the current narrative landscape

## Prerequisites

- A Gigabrain SuperAgent
- USDC funded on HyperLiquid
- Telegram bot token (for notifications)

## Required Skills

- `hyperliquid` — Trade execution and account management
- `brain` — Narrative scanning and sentiment analysis
