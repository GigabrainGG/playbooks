# Smart Copy

Monitors whale wallets on HyperLiquid, runs Gigabrain analysis before copying, skips when conditions don't align.

## What This Agent Does

- Tracks a configurable list of whale HyperLiquid wallets in the background
- When a whale opens a new position, runs full Gigabrain intel analysis (macro, microstructure, price action)
- Copies the trade only if analysis confirms — macro aligns, confidence meets your threshold
- Skips and logs reasoning when conditions don't support the trade
- Sends Telegram alerts for every copy and every skip

## How It Works

A background script (`scripts/whale_monitor.py`) polls whale wallet positions via the HyperLiquid public API. New trades are written to `whale_trades.json`. The agent checks this file on a schedule, and for each new whale trade:

1. Runs `brain ask` for confluence check (macro regime + microstructure + price action)
2. If confidence >= your threshold and macro aligns → copies on HL with your position sizing
3. If not → logs the skip with full reasoning

## Onboarding Flow

1. Configure whale wallet addresses to monitor
2. Set max position size, confidence threshold, max concurrent positions
3. Choose stop loss strategy (mirror whale, fixed %, or brain-assisted)
4. Verify wallet funding
5. Agent starts monitoring and copying

## Prerequisites

- A Gigabrain SuperAgent
- USDC funded on HyperLiquid
- Telegram bot token (for notifications)
- Whale wallet addresses to track

## Required Skills

- `hyperliquid` — Trade execution and account management
- `brain` — Market analysis for trade confirmation
