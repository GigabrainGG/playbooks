# Smart DCA — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Accumulation Target

> Which asset(s) do you want to accumulate? (e.g., BTC, ETH, or both)

## Step 2: DCA Amount

> How much do you want to invest per DCA buy? (in USD, e.g., $100)
> This is the "normal" amount. In favorable conditions I'll do up to 2x, in unfavorable I'll skip.

> How often should I buy?
> 1. **Daily**
> 2. **Every other day**
> 3. **Weekly**

## Step 3: Budget

> What's the total maximum budget for this DCA campaign? (in USD, e.g., $10,000)
> I'll stop buying once this is reached. Leave blank for no limit.

## Step 4: DCA Time

> What time should I check and potentially buy? (e.g., "14:00 UTC")

## Step 5: Verify Wallet

Check the user's HL account balance:

```
uv run "$SKILL_DIR/scripts/hl_client.py" account
```

If balance is low relative to configured DCA amount:

> Your current balance is $[X]. At $[DCA_AMOUNT] per buy, that's roughly [N] buys. You may want to deposit more USDC to sustain the DCA campaign.

## Step 6: Initial Regime Check

Run the first macro check to establish baseline:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Assess current macro conditions for DCA accumulation of [ASSETS]. Provide: macro_regime (risk-on/neutral/risk-off), price_condition (dip/neutral/overextended), recommendation (buy_heavy/buy/skip), and reasoning. Return as structured JSON."
```

Present the result:

> Current conditions: [REGIME] + [PRICE_CONDITION] → recommendation is [ACTION]. Here's what that means for your first DCA buy.

If the recommendation is buy or buy_heavy, ask:

> Want me to execute the first DCA buy now, or wait for the next scheduled time?

## Step 7: Set Up Schedule

```python
schedule_recurring("dca check", "[FREQUENCY] at [USER_TIME_UTC]")
schedule_recurring("weekly dca summary", "weekly on Monday at 09:00 UTC")
```

## Step 8: Go Live

Write configuration to memory.md under `## Configuration`:
- Asset(s)
- DCA amount (normal)
- Frequency
- Max budget
- DCA time (UTC)

Write DCA ledger to memory.md under `## DCA Ledger`:
```
| Date | Action | Asset | Price | Amount | Units | Cumulative Invested | Cumulative Units | Avg Cost |
|------|--------|-------|-------|--------|-------|--------------------|--------------------|----------|
```

Notify the user:

> Smart DCA is live. Accumulating [ASSETS] at $[AMOUNT] per [FREQUENCY]. I'll adjust sizing based on macro regime — buy heavy on dips in risk-on, skip when overextended. Total budget: $[BUDGET].

Write `.bootstrapped` marker.
