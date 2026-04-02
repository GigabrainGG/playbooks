# Polymarket Researcher

Deep thesis building on prediction markets. Researches, scores, and recommends — trades only with your approval.

## What This Agent Does

- Daily scan of Polymarket for high-quality opportunities in your interest areas
- Builds structured theses: bull/bear cases, catalysts, conviction score, recommended sizing
- Presents recommendations with clear reasoning
- Trades only with your explicit approval (or autonomously if you configure it)
- Tracks calibration — are conviction scores accurate over time?

## Research Framework

1. **Base rate analysis** — What historically happens in similar situations?
2. **Catalyst identification** — What specific event resolves this market?
3. **Timeline mapping** — When does the catalyst hit?
4. **Consensus check** — Where is the crowd wrong?
5. **Counter-thesis** — What would make the thesis wrong?

## Onboarding Flow

1. Choose interest areas (crypto, politics, economics, tech, sports)
2. Set max bet size and risk tolerance
3. Choose trading mode (approval required, autonomous, or research only)
4. Set daily scan time
5. Verify USDC funding (if trading)
6. See initial market scan

## Prerequisites

- A Gigabrain SuperAgent
- USDC on Polymarket (for trading — optional for research-only mode)
- Telegram bot token (for notifications)

## Required Skills

- `polymarket` — Market interaction and bet placement
- `polymarket-deep-research` — Deep thesis building and market comparison
- `brain` — Cross-market context and analysis
