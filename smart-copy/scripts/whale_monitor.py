# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "hyperliquid-python-sdk>=0.4.0",
# ]
# ///
"""
Whale wallet monitor for HyperLiquid.

Polls configured whale addresses for new positions and appends
detected trades to whale_trades.json. Designed to run as a
background process alongside the Smart Copy agent.

Usage:
    uv run whale_monitor.py --config whale_config.json

Config format (whale_config.json):
    {
        "addresses": ["0xabc...", "0xdef..."],
        "poll_interval_seconds": 30
    }
"""

import argparse
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from hyperliquid.info import Info


def load_config(config_path: str) -> dict:
    with open(config_path) as f:
        return json.load(f)


def load_known_positions(state_path: str) -> dict[str, dict]:
    """Load the last known positions for each address."""
    if os.path.exists(state_path):
        with open(state_path) as f:
            return json.load(f)
    return {}


def save_known_positions(state_path: str, positions: dict[str, dict]):
    with open(state_path, "w") as f:
        json.dump(positions, f, indent=2)


def append_trade(trades_path: str, trade: dict):
    """Append a new trade to the whale_trades.json file."""
    trades = []
    if os.path.exists(trades_path):
        with open(trades_path) as f:
            trades = json.load(f)
    trades.append(trade)
    with open(trades_path, "w") as f:
        json.dump(trades, f, indent=2)


def get_positions(info: Info, address: str) -> dict[str, dict]:
    """Get current positions for an address as {coin: position_info}."""
    state = info.user_state(address)
    positions = {}
    for pos in state.get("assetPositions", []):
        item = pos.get("position", {})
        coin = item.get("coin")
        if coin and float(item.get("szi", 0)) != 0:
            positions[coin] = {
                "coin": coin,
                "size": float(item.get("szi", 0)),
                "entry_price": float(item.get("entryPx", 0)),
                "unrealized_pnl": float(item.get("unrealizedPnl", 0)),
                "leverage": item.get("leverage", {}),
            }
    return positions


def detect_new_trades(
    address: str,
    old_positions: dict[str, dict],
    new_positions: dict[str, dict],
) -> list[dict]:
    """Compare old and new positions to detect new or changed trades."""
    trades = []
    now = datetime.now(timezone.utc).isoformat()

    for coin, new_pos in new_positions.items():
        old_pos = old_positions.get(coin)

        if old_pos is None:
            # New position opened
            trades.append({
                "timestamp": now,
                "address": address,
                "type": "open",
                "coin": coin,
                "side": "long" if new_pos["size"] > 0 else "short",
                "size": abs(new_pos["size"]),
                "entry_price": new_pos["entry_price"],
                "leverage": new_pos["leverage"],
                "processed": False,
            })
        elif abs(new_pos["size"]) > abs(old_pos["size"]) * 1.1:
            # Position increased by >10%
            trades.append({
                "timestamp": now,
                "address": address,
                "type": "increase",
                "coin": coin,
                "side": "long" if new_pos["size"] > 0 else "short",
                "old_size": abs(old_pos["size"]),
                "new_size": abs(new_pos["size"]),
                "entry_price": new_pos["entry_price"],
                "leverage": new_pos["leverage"],
                "processed": False,
            })

    # Detect closed positions
    for coin, old_pos in old_positions.items():
        if coin not in new_positions:
            trades.append({
                "timestamp": now,
                "address": address,
                "type": "close",
                "coin": coin,
                "side": "long" if old_pos["size"] > 0 else "short",
                "size": abs(old_pos["size"]),
                "processed": False,
            })

    return trades


def main():
    parser = argparse.ArgumentParser(description="Monitor whale wallets on HyperLiquid")
    parser.add_argument(
        "--config",
        default="whale_config.json",
        help="Path to whale config JSON file",
    )
    parser.add_argument(
        "--trades",
        default="whale_trades.json",
        help="Path to output trades JSON file",
    )
    parser.add_argument(
        "--state",
        default=".whale_state.json",
        help="Path to position state file",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    addresses = config["addresses"]
    interval = config.get("poll_interval_seconds", 30)

    print(f"Monitoring {len(addresses)} whale wallet(s), polling every {interval}s")

    info = Info(skip_ws=True)
    known_positions = load_known_positions(args.state)

    while True:
        for address in addresses:
            try:
                current = get_positions(info, address)
                previous = known_positions.get(address, {})
                new_trades = detect_new_trades(address, previous, current)

                for trade in new_trades:
                    append_trade(args.trades, trade)
                    action = trade["type"]
                    coin = trade["coin"]
                    side = trade.get("side", "")
                    print(f"[{trade['timestamp']}] {address[:10]}... {action} {side} {coin}")

                known_positions[address] = current
                save_known_positions(args.state, known_positions)

            except Exception as e:
                print(f"Error polling {address[:10]}...: {e}")

        time.sleep(interval)


if __name__ == "__main__":
    main()
