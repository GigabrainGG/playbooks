# Smart Copy — Bootstrap

Run these steps in order on first boot. Ask each question, wait for the user's answer, then proceed.

## Step 1: Whale Wallets

Ask the user which HyperLiquid wallet addresses to monitor.

> Which whale wallets do you want me to track? Paste the HyperLiquid addresses (one per line). If you're not sure, I can start with some well-known profitable wallets.

Store the addresses in memory.md under `## Whale Wallets`.

## Step 2: Trading Configuration

Ask these questions one at a time:

> What's the maximum position size per copied trade? (in USD, e.g., $500)

> What's your minimum confidence threshold for copying? (1-10, where 10 = only copy when analysis is extremely bullish)

> What's your maximum number of concurrent positions? (e.g., 3)

> What's your daily max drawdown before I stop copying? (in USD or %, e.g., $200 or 5%)

## Step 3: Trading Style

> How should I handle stop losses on copied trades?
> 1. **Mirror whale** — Exit when the whale exits (if detectable)
> 2. **Fixed percentage** — Always set a stop at X% below entry
> 3. **Brain-assisted** — Let Gigabrain analysis determine the invalidation level

## Step 4: Verify Wallet Funding

Check the user's HL account balance:

```
uv run "$SKILL_DIR/scripts/hl_client.py" account
```

If balance is insufficient, tell the user to fund their wallet and write `bootstrap_state: waiting_for_funding` to memory.md. Wait for them to confirm.

## Step 5: Start Whale Monitor

Write the whale wallet config to `scripts/whale_config.json`:
```json
{
  "addresses": ["0x...", "0x..."],
  "poll_interval_seconds": 30
}
```

Confirm the monitor script is available at `scripts/whale_monitor.py`.

## Step 6: Set Up Schedules

```python
schedule_recurring("whale trade check", "every 5 minutes")
schedule_recurring("daily copy summary", "daily at 20:00 UTC")
```

## Step 7: Go Live

Write all configuration to memory.md under `## Configuration`:
- Whale wallets
- Max position size
- Confidence threshold
- Max concurrent positions
- Max daily drawdown
- Stop loss style

Notify the user on Telegram:

> Smart Copy is live. Monitoring [N] whale wallets. I'll analyze every new trade through Gigabrain before copying. You'll get alerts for every copy and skip.

