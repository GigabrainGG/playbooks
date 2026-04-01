# Signal Trader — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Signal Types

> Which signal types should I monitor? (pick all that apply)
> 1. **Funding rate anomalies** — Extreme funding that precedes reversals
> 2. **Liquidation clusters** — Large liquidation levels acting as magnets
> 3. **Whale movements** — Significant position changes by smart money
> 4. **Narrative shifts** — Emerging themes gaining momentum
> 5. **All of the above**

## Step 2: Impact Threshold

> What's your minimum impact rating for a signal to qualify? (1-10, where 10 = only act on the highest-impact signals)

> Recommended: 7 for most users. Lower means more trades but lower average quality.

## Step 3: Position Sizing

> What's your maximum position size per trade? (in USD, e.g., $1,000)

> What's the maximum number of concurrent positions? (e.g., 5)

## Step 4: Confidence Threshold

> What's the minimum confidence score needed to execute a trade? (1-10)

> Recommended: 7. This means macro must align AND the signal must be strong.

## Step 5: Trading Mode

> How should I handle qualified signals?
> 1. **Autonomous** — I trade within your limits, notify you after
> 2. **Confirm** — I present the setup and wait for your approval before trading
> 3. **Paper** — I log what I would trade but don't execute (good for testing)

## Step 6: Verify Wallet

Check the user's HL account balance:

```
uv run "$SKILL_DIR/scripts/hl_client.py" account
```

If balance is insufficient for the configured position sizes, flag it and wait.

## Step 7: Initial Scan

Run an initial signal scan to show the user the format:

```
uv run "$SKILL_DIR/scripts/intel_client.py" ask --question "Scan for high-impact alpha signals across crypto markets. For each signal, provide: signal_type, asset, direction, impact_rating (1-10), description, and suggested timeframe. Focus on: funding anomalies, liquidation clusters, whale movements, and narrative shifts. Return as structured JSON."
```

Present the results and ask:

> Here's what the current signal landscape looks like. Any adjustments to the configuration?

## Step 8: Set Up Schedules

```python
schedule_recurring("alpha scan", "every 2 hours")
schedule_recurring("daily signal summary", "daily at 20:00 UTC")
```

## Step 9: Go Live

Write configuration to memory.md under `## Configuration`:
- Signal types
- Min impact rating
- Max position size
- Max concurrent positions
- Confidence threshold
- Trading mode

Notify the user:

> Signal Trader is live. Scanning every 2 hours for [SIGNAL_TYPES]. Trading mode: [MODE]. I'll notify you on every qualified signal.

Write `.bootstrapped` marker.
