"""
Quick test script for CoinLackey Python SDK
Run with: python example.py
"""

from coinlackey import CoinLackey

def main():
    print("Connecting to CoinLackey Terminal (https://coinlackey.com)...")
    client = CoinLackey()

    # 1. Market pulse
    pulse = client.get_market_pulse(limit=5)
    print("\n--- Live Market Pulse ---")
    print(f"Total Market Open Interest: ${pulse.get('total_open_interest_usd', 0):,.2f}")
    print(f"Active Venues: {pulse.get('active_exchanges_count', 0)}")
    
    print("\nTop Active Assets:")
    for asset in pulse.get("top_assets", [])[:5]:
        sym = asset.get("symbol")
        px = asset.get("price", 0)
        chg = asset.get("change_24h_pct", 0)
        oi = asset.get("open_interest_usd", 0)
        apr = asset.get("avg_funding_apr", 0)
        print(f"  {sym:<8} Price: ${px:<10,.2f} 24h: {chg:>+5.2f}% | OI: ${oi:<12,.0f} | Avg APR: {apr:>+6.2f}%")

    # 2. Funding squeeze radar
    squeezes = pulse.get("squeeze_outliers", [])
    if squeezes:
        print("\nFunding Squeeze Radar:")
        for s in squeezes[:3]:
            print(f"  {s.get('symbol'):<8} Avg APR: {s.get('avg_funding_apr'):>+6.2f}% | Spread: {s.get('funding_spread_apr'):>6.2f}%")

    print("\nSUCCESS: CoinLackey SDK operational!")

if __name__ == "__main__":
    main()
