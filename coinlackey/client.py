"""
CoinLackey API Client
https://coinlackey.com
"""

from typing import Any, Dict, Optional
import requests


class CoinLackey:
    """
    Client for interacting with the CoinLackey public and pro telemetry endpoints.
    Visit https://coinlackey.com for live terminal charts, heatmaps, and documentation.
    """

    def __init__(self, base_url: str = "https://coinlackey.com", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "coinlackey-python/0.1.0 (https://coinlackey.com)",
            "Accept": "application/json",
        })
        if self.api_key:
            self.session.headers["X-API-Key"] = self.api_key

    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        response = self.session.get(url, params=params, timeout=12)
        response.raise_for_status()
        return response.json()

    def get_market_pulse(self, limit: int = 24) -> Dict[str, Any]:
        """
        Fetch unauthenticated real-time market summary: aggregated Open Interest,
        24h liquidation statistics, top derivatives assets, and funding squeeze outliers.
        """
        return self._get("/api/v1/public/market-pulse", params={"limit": limit})

    def get_top_symbols(self, limit: int = 200) -> Dict[str, Any]:
        """
        Fetch active perpetual & high-volatility symbols ranked by Open Interest,
        volume, and funding rate dispersion.
        """
        return self._get("/api/v1/public/top-symbols", params={"limit": limit})

    def get_funding_rates(
        self, symbol: Optional[str] = None, exchange: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Fetch normalized real-time funding rates across all major exchanges.
        Filter by base symbol (e.g. 'BTC') or exchange (e.g. 'binance', 'bybit').
        """
        params = {}
        if symbol:
            params["symbol"] = symbol.upper()
        if exchange:
            params["exchange"] = exchange.lower()
        return self._get("/api/v1/crypto/funding-rates", params=params)

    def get_open_interest(
        self, symbol: Optional[str] = None, exchange: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Fetch normalized open interest in USD across major perpetual exchanges.
        Filter by base symbol (e.g. 'ETH') or exchange.
        """
        params = {}
        if symbol:
            params["symbol"] = symbol.upper()
        if exchange:
            params["exchange"] = exchange.lower()
        return self._get("/api/v1/crypto/open-interest", params=params)

    def get_liquidations(
        self, symbol: Optional[str] = None, limit: int = 50
    ) -> Dict[str, Any]:
        """
        Fetch real-time liquidation tape feed.
        """
        params = {"limit": limit}
        if symbol:
            params["symbol"] = symbol.upper()
        return self._get("/api/v1/crypto/liquidations", params=params)

    def get_overview(self) -> Dict[str, Any]:
        """
        High-level dashboard overview: Total aggregated OI, 24h liquidations,
        and top positive/negative funding rate spreads.
        """
        return self._get("/api/v1/crypto/overview")
