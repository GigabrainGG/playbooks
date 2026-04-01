# Narrative Trader — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Sector Focus

> Which narrative sectors should I monitor?
> 1. **AI / AI Agents** — Artificial intelligence tokens and infrastructure
> 2. **DeFi** — Decentralized finance protocols and yield
> 3. **L2 / Infrastructure** — Layer 2s, rollups, modular stack
> 4. **Memes / Culture** — Memecoins and cultural tokens
> 5. **RWA** — Real-world asset tokenization
> 6. **All sectors** — I'll scan everything
>
> Pick one or more.

## Step 2: Risk Configuration

> What's the maximum allocation per narrative? (in USD, e.g., $2,000)
> Remember: all tokens within a narrative are correlated, so this is effectively your max exposure to one theme.

> What's the maximum number of concurrent narratives? (e.g., 3)

> What's your risk tolerance?
> 1. **Conservative** — Only enter "building" stage narratives with confirmed catalysts. Tighter stops.
> 2. **Moderate** — Enter "building" and "early momentum" with validated catalysts.
> 3. **Aggressive** — Willing to enter on strong momentum even with softer catalyst validation. Wider stops.

## Step 3: Position Sizing

> What's your max position size per individual token? (in USD)

> This should be less than your per-narrative allocation since you might hold multiple tokens in one narrative.

## Step 4: Trading Mode

> How should I handle narrative entries?
> 1. **Autonomous** — I enter and exit within your limits, notify you after
> 2. **Confirm** — I present the narrative thesis and wait for your approval
> 3. **Alert only** — I identify narratives but don't trade. Pure research.

## Step 5: Verify Wallet

Check the user's HL account balance:

```
uv run "$SKILL_DIR/scripts/hl_client.py" account
```

## Step 6: Initial Narrative Scan

Run a narrative scan to show the user what's currently active:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Identify the top 5 crypto narratives right now. For each, provide: narrative_name, sector, sentiment_stage (building/early_momentum/peak_attention/euphoria/overcooked), momentum_score (1-10), top_3_tokens, and key_catalyst. Return as structured JSON."
```

Present results:

> Here's the current narrative landscape. I'll be tracking these and scanning for new ones every 6 hours.

## Step 7: Set Up Schedules

```python
schedule_recurring("narrative scan", "every 6 hours")
schedule_recurring("position sentiment check", "every 4 hours")
schedule_recurring("weekly narrative recap", "weekly on Sunday at 18:00 UTC")
```

## Step 8: Go Live

Write configuration to memory.md under `## Configuration`:
- Sectors
- Max allocation per narrative
- Max concurrent narratives
- Risk tolerance
- Max position size per token
- Trading mode

Notify the user:

> Narrative Trader is live. Monitoring [SECTORS] for emerging narratives. I'll scan every 6 hours and check sentiment on open positions every 4 hours. Mode: [MODE].

Write `.bootstrapped` marker.
