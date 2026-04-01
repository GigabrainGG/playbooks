# Morning Briefing — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Watchlist

> Which assets do you want in your daily briefing? (e.g., BTC, ETH, SOL, or "top 10 by market cap")

Store the watchlist in memory.md under `## Watchlist`.

## Step 2: Delivery Time

> What time should I deliver your morning briefing? (e.g., "8:00 AM UTC" or "7:30 AM EST")

Convert to UTC and store in memory.md.

## Step 3: Briefing Depth

> How detailed should the daily briefing be?
> 1. **Quick summary** — 3-5 bullet points, under 200 words. Just the essentials.
> 2. **Standard** — Full structure (macro, movers, levels, catalysts, bottom line). ~500 words.
> 3. **Deep dive** — Comprehensive analysis with charts context, historical comparisons, and detailed level analysis. ~1000 words.

## Step 4: Alert Preferences

> Should I send off-schedule alerts for major market events? (e.g., >5% moves, regime changes, breaking news)
> 1. **Yes — alert me for anything significant**
> 2. **Only for my watchlist assets**
> 3. **No — just the daily briefing**

## Step 5: Test Briefing

Run a test briefing now to show the user the format:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Provide a comprehensive market briefing covering: 1) Current macro regime (risk-on/risk-off with DXY, VIX, yields context), 2) Top movers in the last 24h and why they moved, 3) Key support/resistance levels for [WATCHLIST], 4) Upcoming catalysts in the next 48 hours. Format as a structured briefing."
```

Send the formatted briefing to the user via Telegram and ask:

> Here's a sample briefing. Does this format work for you, or would you like me to adjust anything?

## Step 6: Set Up Schedule

```python
schedule_recurring("morning briefing", "daily at [USER_TIME_UTC]")
```

## Step 7: Go Live

Write configuration to memory.md under `## Configuration`:
- Watchlist
- Delivery time (UTC)
- Briefing depth
- Alert preferences

Notify the user:

> Morning Briefing is set up. You'll get your first briefing tomorrow at [TIME]. I just sent you a sample so you know what to expect.
