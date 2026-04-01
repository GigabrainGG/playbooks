# Polymarket Researcher — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Interest Areas

> Which Polymarket categories interest you?
> 1. **Crypto** — Token prices, ETF approvals, protocol events
> 2. **Politics** — Elections, policy decisions, regulatory actions
> 3. **Economics** — Rate decisions, inflation, employment data
> 4. **Tech** — Product launches, company earnings, AI milestones
> 5. **Sports** — Game outcomes, championships, player events
> 6. **All categories**
>
> Pick one or more.

## Step 2: Risk Configuration

> What's your maximum bet size per market? (in USDC, e.g., $100)

> What's your risk tolerance?
> 1. **Conservative** — Only high-conviction (8+/10) bets with clear catalysts and good odds
> 2. **Moderate** — Conviction 6+/10 with reasonable risk/reward
> 3. **Aggressive** — Willing to take lower-conviction bets if the odds are significantly mispriced

## Step 3: Trading Mode

> How should I handle recommendations?
> 1. **Approval required** — I research and present a thesis, you decide whether to bet (Recommended)
> 2. **Autonomous** — I bet within your limits when conviction is high enough
> 3. **Research only** — I build theses and track markets but never place bets

## Step 4: Scan Time

> What time should I run the daily market scan? (e.g., "10:00 AM UTC")

## Step 5: Verify Wallet

If trading mode is not "research only", verify the user has USDC available:

> Do you have USDC funded on Polymarket? If not, you'll need to deposit before I can place bets. I can still research and recommend in the meantime.

## Step 6: Initial Market Scan

Run an initial scan to show the user what's available:

```
uv run "$SKILL_DIR/scripts/pm_deep_research.py" compare --categories "[USER_CATEGORIES]"
```

Present the top opportunities:

> Here are the most interesting markets right now in your interest areas. I'll do deep research on the top ones daily.

## Step 7: Set Up Schedules

```python
schedule_recurring("market scan", "daily at [USER_TIME_UTC]")
schedule_recurring("position monitor", "every 6 hours")
schedule_recurring("weekly pm summary", "weekly on Friday at 18:00 UTC")
```

## Step 8: Go Live

Write configuration to memory.md under `## Configuration`:
- Interest areas
- Max bet size
- Risk tolerance
- Trading mode
- Scan time

Notify the user:

> Polymarket Researcher is live. Scanning [CATEGORIES] daily at [TIME]. Mode: [MODE]. I'll present structured theses with conviction scores for every opportunity.

Write `.bootstrapped` marker.
