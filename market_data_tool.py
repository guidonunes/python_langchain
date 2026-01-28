# market_data_tool.py
from langchain.tools import BaseTool
from typing import Optional, Type
import yfinance as yf

class MarketDataTool(BaseTool):
    name: str = "MarketDataTool"
    description: str = "Use this tool to get the latest stock price and news for a given ticker symbol (e.g. 'AAPL', 'NVDA'). Returns a summary string."

    def _run(self, ticker: str) -> str:
        print(f"\n   [TOOL] 📡 Fetching data for: {ticker}...")

        try:
            stock = yf.Ticker(ticker)

            # 1. Safer Price Check
            try:
                price = stock.fast_info.last_price
            except:
                # Fallback if fast_info fails
                price = stock.info.get('regularMarketPrice', 'Unknown')

            # 2. Safer News Check (The part that broke)
            news_title = "No news found"
            try:
                if stock.news and len(stock.news) > 0:
                    # Use .get() so it never crashes on missing keys
                    news_title = stock.news[0].get('title', stock.news[0].get('uuid', 'News found but no title'))
            except Exception:
                pass # Ignore news errors, just return price

            return f"Data for {ticker}: Price is ${price}. Latest News: '{news_title}'"

        except Exception as e:
            return f"Error fetching data for {ticker}: {e}"
