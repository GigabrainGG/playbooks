# Macro Monitor — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Notification Preferences

> When should I alert you?
> 1. **All changes** — Any meaningful shift in macro indicators, even if the regime hasn't fully changed
> 2. **Major only** — Only when the overall regime changes (e.g., risk-on → risk-off)
> 3. **Daily summary only** — Just the daily recap, no intraday alerts

## Step 2: Asset Context

> Which assets should I contextualize in my analysis? (e.g., BTC, ETH, SOL)
> I'll explain what macro shifts mean specifically for these assets.

Store the assets in memory.md under `## Watched Assets`.

## Step 3: Actionable Recommendations

> Should I include actionable recommendations, or just report the data?
> 1. **Include recommendations** — "Consider reducing leverage" or "Conditions support adding risk"
> 2. **Data only** — Just the regime, indicators, and context. No advice.

## Step 4: Summary Time

> What time should I send the daily summary? (e.g., "9:00 AM UTC")

## Step 5: Initial Macro Assessment

Run the first macro check to establish a baseline:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Provide a comprehensive macro risk assessment for crypto markets. Include: risk_regime (risk-on/risk-off/neutral), DXY level and trend, VIX level and context, US 10Y yield and implications, upcoming macro events in next 7 days, BTC dominance trend, and overall recommended exposure level (1-10). Return as structured JSON."
```

Present the results:

> Here's the current macro landscape. This is my baseline — I'll alert you whenever conditions change from here.

Write the baseline regime to memory.md under `## Current Regime`.

## Step 6: Set Up Schedules

```python
schedule_recurring("macro check", "every 4 hours")
schedule_recurring("daily macro summary", "daily at [USER_TIME_UTC]")
```

## Step 7: Go Live

Write configuration to memory.md under `## Configuration`:
- Notification level
- Watched assets
- Include recommendations (yes/no)
- Daily summary time
- Current regime baseline

Notify the user:

> Macro Monitor is live. Checking every 4 hours. Current regime: [REGIME]. I'll alert you on [NOTIFICATION_LEVEL] changes. Daily summary at [TIME].

Write `.bootstrapped` marker.
