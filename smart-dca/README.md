# Smart DCA

Regime-aware accumulation. Buys heavy on dips in risk-on, skips when macro is overextended.

## What This Agent Does

- Runs a dollar-cost averaging strategy that adjusts sizing based on macro conditions
- Before each buy, checks the macro regime and price condition via Gigabrain
- **Buy heavy (2x)** — Risk-on + dip
- **Buy normal (1x)** — Neutral conditions
- **Skip** — Risk-off or overextended
- Tracks a full DCA ledger: date, action, price, amount, cumulative stats, average cost

## Regime-to-Action Matrix

| Macro Regime | Price Condition | Action |
|---|---|---|
| Risk-on | Dip | Buy heavy (2x) |
| Risk-on | Neutral | Buy (1x) |
| Risk-on | Overextended | Buy (0.5x) |
| Neutral | Dip | Buy (1.5x) |
| Neutral | Neutral | Buy (1x) |
| Neutral | Overextended | Skip |
| Risk-off | Dip | Buy (0.5x) |
| Risk-off | Neutral | Skip |
| Risk-off | Overextended | Skip |

## Onboarding Flow

1. Choose asset(s) to accumulate
2. Set DCA amount and frequency (daily/weekly)
3. Set total budget (optional)
4. Choose DCA time
5. Verify wallet funding
6. See initial regime check and first buy recommendation

## Prerequisites

- A Gigabrain SuperAgent (daemon)
- USDC funded on HyperLiquid
- Telegram bot token (for notifications)

## Required Skills

- `hyperliquid` — Trade execution
- `gigabrain-intel` — Macro regime assessment
