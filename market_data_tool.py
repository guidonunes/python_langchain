# market_data_tool.py
from langchain.tools import BaseTool
from typing import Optional, Type
import yfinance as yf

class MarketDataTool(BaseTool):
    name: str = "MarketDataTool"
    description: str = "Use this tool to get the latest stock price and news for a given ticker symbol (e.g. 'AAPL', 'NVDA'). Returns a summary string."

    def _run(self, ticker: str) -> str:
        """
        The 'ticker' argument comes from the Agent.
        It will be something like 'AAPL' or 'BTC-USD'.
        """
        print(f"\n   [TOOL] 📡 Fetching data for: {ticker}...")

        try:
            stock = yf.Ticker(ticker)

            price = stock.fast_info.last_price

            news_title = "No news found"
            if stock.news:
                news_title = stock.news[0]['title']

            return f"Data for {ticker}: Price is ${price:.2f}. Latest News: '{news_title}'"

        except Exception as e:
            return f"Error fetching data for {ticker}: {e}"

    def _arun(self, ticker: str):
        raise NotImplementedError("Async not implemented")
