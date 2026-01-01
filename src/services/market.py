import logging
from typing import List

import yfinance as yf

logger = logging.getLogger(__name__)


def _try_ticker(ticker: str):
    """Attempt to fetch data from yfinance for the given ticker.

    Args:
        ticker: A symbol string understood by yfinance (e.g. "^KS11", "005930.KS").

    Returns:
        dict containing `ticker`, `name`, and `price`. `price` will be None on failure.
    """
    try:
        t = yf.Ticker(ticker)
        info = t.info
        price = info.get("regularMarketPrice") or info.get("previousClose")
        return {
            "ticker": ticker,
            "name": info.get("shortName") or info.get("longName") or ticker,
            "price": price,
        }
    except Exception:
        logger.exception("Error fetching ticker %s", ticker)
        return {"ticker": ticker, "name": ticker, "price": None}


def get_stock_price(tickers: List[str]):
    """Fetch price information for multiple tickers.

    Args:
        tickers: A list of symbol strings.

    Returns:
        List[dict]: A list of dicts containing `ticker`, `name`, and `price` for each symbol.
    """
    results = []
    for t in tickers:
        res = _try_ticker(t)
        results.append(res)
    return results
