# CoinLackey Python SDK

[![PyPI version](https://img.shields.io/pypi/v/coinlackey.svg)](https://pypi.org/project/coinlackey/)
[![Python Versions](https://img.shields.io/pypi/pyversions/coinlackey.svg)](https://pypi.org/project/coinlackey/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Terminal](https://img.shields.io/badge/Terminal-coinlackey.com-blue)](https://coinlackey.com)

Official Python SDK for the [CoinLackey Terminal](https://coinlackey.com) — real-time cryptocurrency derivatives intelligence, sub-second funding rates, open interest, liquidation cascades, and macro market telemetry.

Designed for algorithmic traders, quantitative analysts, AI agents, and crypto developers seeking clean, normalized telemetry across Binance, Bybit, OKX, Deribit, Gate, Hyperliquid, and dYdX.

---

## Installation

```bash
pip install coinlackey
```

*(Requires Python 3.8+)*

---

## Quickstart

```python
from coinlackey import CoinLackey

# Connect to the live terminal
client = CoinLackey()

# 1. Fetch live market pulse & funding squeeze outliers
pulse = client.get_market_pulse(limit=10)
print(f"Total Market Open Interest: ${pulse['total_open_interest_usd']:,}")
for asset in pulse.get("top_assets", [])[:5]:
    print(f"- {asset['symbol']}: ${asset['price']:,.2f} | Avg Funding APR: {asset['avg_funding_apr']}%")

# 2. Get normalized funding rates across exchanges for Bitcoin
btc_funding = client.get_funding_rates(symbol="BTC")
print(btc_funding)

# 3. Get real-time aggregated Open Interest for Ethereum
eth_oi = client.get_open_interest(symbol="ETH")
print(eth_oi)

# 4. Fetch the top 200 tracked perpetual symbols
symbols = client.get_top_symbols(limit=50)
print(f"Tracked perpetual markets: {len(symbols)}")
```

---

## Key Features

- **Sub-Second Normalization**: Direct normalized feeds from Redis-backed streaming engines.
- **Funding Squeeze Detection**: Instant identification of negative funding anomalies and extreme spread dislocations.
- **Liquidation Cascades**: Real-time USD notional liquidation tape and 24h aggregated statistics.
- **Cross-Exchange Coverage**: Binance, Bybit, OKX, Gate, Deribit, Hyperliquid, and dYdX.
- **Zero Configuration**: Ready out of the box with zero API keys required for public telemetry endpoints.

---

## Links & Ecosystem

- **Live Web Terminal**: [https://coinlackey.com](https://coinlackey.com)
- **Asset Intelligence**: [https://coinlackey.com/assets](https://coinlackey.com/assets)
- **Interactive Documentation**: [https://coinlackey.com/docs](https://coinlackey.com/docs)
- **GitHub Repository**: [https://github.com/smilingbuddhaextracts-eng/coinlackey-coinlackey-python](https://github.com/smilingbuddhaextracts-eng/coinlackey-coinlackey-python)

---

## License

MIT License. Free for retail developers, quantitative researchers, and automated trading bots.
