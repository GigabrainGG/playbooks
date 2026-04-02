# Portfolio Manager

Active portfolio management with daily reviews, position monitoring, and rebalancing recommendations.

## What This Agent Does

- **Morning review** — Daily market overview + portfolio state + plan for the day
- **Position monitoring** — Every 2 hours, checks P&L and reassesses any position with >5% move
- **Weekly review** — Full performance analysis, attribution, exposure review, and recommendations
- Thinks at the portfolio level: correlation, concentration, risk-adjusted returns
- Supports autonomous rebalancing, advisory mode, or monitor-only

## Review Cadence

| Review | Frequency | What It Covers |
|--------|-----------|----------------|
| Morning | Daily | Market overview, overnight changes, portfolio state |
| Position check | Every 2 hours | P&L, stop/TP levels, concentration risk |
| Weekly deep dive | Weekly | Performance, attribution, exposure, recommendations |

## Onboarding Flow

1. Pull current portfolio (automatic)
2. Set which assets to manage
3. Configure risk limits (max drawdown, max single position %)
4. Optionally set target allocation
5. Choose operating mode (autonomous, advisory, or monitor-only)
6. Set morning review time
7. See initial portfolio assessment

## Prerequisites

- A Gigabrain SuperAgent
- Existing HyperLiquid positions (or fund to start)
- Telegram bot token (for notifications)

## Required Skills

- `hyperliquid` — Position management and trading
- `portfolio-tracker` — Portfolio overview and P&L tracking
- `brain` — Market analysis for portfolio decisions
