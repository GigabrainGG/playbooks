# Portfolio Manager — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Current Portfolio

Pull the user's current positions:

```
uv run "$SKILL_DIR/scripts/hl_client.py" positions
```

```
uv run "$SKILL_DIR/scripts/hl_client.py" account
```

Present the current state:

> Here's your current portfolio. Let me know if this looks right — I'll use this as my starting baseline.

## Step 2: Assets to Manage

> Which assets should I actively manage and monitor? (e.g., BTC, ETH, SOL, or "everything in my account")

## Step 3: Risk Limits

> What's your maximum acceptable portfolio drawdown? (e.g., 15%)
> If the portfolio hits this level, I'll reduce positions and alert you.

> What's the maximum allocation for any single position? (as % of portfolio, e.g., 30%)

## Step 4: Target Allocation (Optional)

> Do you have a target portfolio allocation?
> 1. **Yes** — I'll tell you what it is (e.g., 50% BTC, 30% ETH, 20% SOL)
> 2. **No target** — Just monitor and advise on what I'm holding
>
> If yes, provide your target allocation.

## Step 5: Operating Mode

> How should I handle rebalancing?
> 1. **Autonomous** — I rebalance within your limits when drift exceeds thresholds
> 2. **Advisory** — I recommend rebalances, you approve before execution (Recommended)
> 3. **Monitor only** — I track and report, but never suggest trades

## Step 6: Review Time

> What time should I deliver the morning review? (e.g., "8:00 AM UTC")

## Step 7: Initial Portfolio Review

Run a full portfolio assessment:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Analyze the current crypto market conditions for portfolio management. Include: macro regime, sector rotation trends, correlation between major assets, and recommended portfolio exposure level (1-10). Consider positions in [USER_ASSETS]."
```

Present the analysis:

> Here's my initial assessment of your portfolio in the current market context. I'll track this daily going forward.

Write the baseline to memory.md.

## Step 8: Set Up Schedules

```python
schedule_recurring("morning review", "daily at [USER_TIME_UTC]")
schedule_recurring("position monitor", "every 2 hours")
schedule_recurring("weekly review", "weekly on Sunday at 18:00 UTC")
```

## Step 9: Go Live

Write configuration to memory.md under `## Configuration`:
- Managed assets
- Max portfolio drawdown
- Max single position %
- Target allocation (if any)
- Operating mode
- Review time
- Current portfolio snapshot

Notify the user:

> Portfolio Manager is live. Managing [ASSETS]. Morning review at [TIME], monitoring every 2 hours, weekly deep review on Sundays. Mode: [MODE]. Max drawdown: [DD%].

Write `.bootstrapped` marker.
