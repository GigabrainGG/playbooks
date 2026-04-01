# Macro Monitor

Persistent macro risk monitor. Alerts you when the regime shifts — no trades, just intelligence.

## What This Agent Does

- Checks macro conditions every 4 hours (DXY, VIX, yields, BTC dominance, stablecoin flows)
- Classifies the current regime as risk-on, risk-off, or neutral
- Compares with the previous regime and alerts you on changes
- Contextualizes macro shifts for your specific assets
- Sends a daily summary regardless of changes

## Alert Levels

| Level | When | Notification |
|-------|------|--------------|
| Regime Change | Risk-on ↔ risk-off | Always notified |
| Significant Shift | Key indicator moved meaningfully | Based on your preference |
| Monitoring | Minor changes noted | Daily summary only |

## Onboarding Flow

1. Choose notification level (all changes, major only, or daily summary only)
2. Set which assets to contextualize
3. Choose whether to include actionable recommendations
4. Set daily summary time
5. See the initial macro baseline

## Prerequisites

- A Gigabrain SuperAgent (daemon)
- Telegram bot token (for notifications)

## Required Skills

- `gigabrain-intel` — Macro analysis and risk assessment
