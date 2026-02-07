import warnings
from typing import List, Optional, Sequence, Tuple

import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore", message="YF.download() has changed argument auto_adjust")

# Defaults
DEFAULT_START_DATE = "2014-01-01"
DEFAULT_END_DATE = "2019-01-01"

# Mutable state for optional reuse
tickers: List[str] = []
_closing_cache: Optional[Tuple[Tuple[str, ...], str, str, List[List[float]]]] = None


def collect_tickers() -> List[str]:
    """Collect ticker symbols from user input."""
    global tickers
    tickers = []
    num_tickers = int(input("How many tickers do you want to add? "))
    while len(tickers) < num_tickers:
        ticker = input(f"Enter ticker {len(tickers)+1}: ").strip().upper()
        try:
            ticker_obj = yf.Ticker(ticker)
            info = ticker_obj.info
            current_price = info.get("regularMarketPrice")
            if current_price is not None:
                tickers.append(ticker)
            else:
                print(f"Invalid ticker: {ticker} - No price data available")
        except Exception:
            print(f"Invalid ticker: {ticker}")
            continue
    return tickers


def _normalize_close_data(close: pd.DataFrame | pd.Series, tickers_list: Sequence[str]) -> List[List[float]]:
    """Normalize yfinance close data to a list-of-lists per ticker."""
    if isinstance(close, pd.Series):
        return [close.tolist()]
    return [close[ticker].tolist() for ticker in tickers_list]


def fetch_closing_data(
    tickers_list: Optional[Sequence[str]] = None,
    start_date: str = DEFAULT_START_DATE,
    end_date: str = DEFAULT_END_DATE,
) -> List[List[float]]:
    """Fetch closing price data for the provided tickers."""
    global tickers, _closing_cache

    if tickers_list is None:
        if not tickers:
            tickers = collect_tickers()
        tickers_list = tickers

    cache_key = (tuple(tickers_list), start_date, end_date)
    if _closing_cache and _closing_cache[0:3] == cache_key:
        return _closing_cache[3]

    data = yf.download(
        list(tickers_list),
        start=start_date,
        end=end_date,
        progress=False,
        auto_adjust=True,
    )
    closing_data = _normalize_close_data(data["Close"], tickers_list)
    _closing_cache = (cache_key[0], cache_key[1], cache_key[2], closing_data)
    return closing_data
 
