# Signal Trader

Scans for high-impact alpha signals, cross-references with Brain API analysis, trades only when multiple signals align.

## What This Agent Does

- Scans every 2 hours for alpha signals: funding anomalies, liquidation clusters, whale movements, narrative shifts
- Filters by your configured signal types and minimum impact rating
- For qualifying signals, runs full trade setup analysis through Gigabrain
- Trades only when signal + macro + confidence all align
- Supports autonomous, confirm, and paper trading modes

## Signal Types

| Signal | What It Catches |
|--------|----------------|
| Funding anomalies | Extreme funding rates that precede reversals |
| Liquidation clusters | Large liquidation levels acting as price magnets |
| Whale movements | Significant position changes by smart money |
| Narrative shifts | Emerging themes gaining momentum |

## Onboarding Flow

1. Choose which signal types to monitor
2. Set minimum impact rating threshold
3. Configure position sizing and max concurrent positions
4. Set confidence threshold for execution
5. Choose trading mode (autonomous, confirm, or paper)
6. Verify wallet funding
7. See an initial signal scan

## Prerequisites

- A Gigabrain SuperAgent (daemon)
- USDC funded on HyperLiquid
- Telegram bot token (for notifications)

## Required Skills

- `hyperliquid` — Trade execution and account management
- `gigabrain-intel` — Signal scanning and trade analysis
