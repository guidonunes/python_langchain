# market_data_tool.py
from langchain.tools import BaseTool
from typing import Optional, Type
import yfinance as yf
from langchain_community.tools import DuckDuckGoSearchRun

class MarketDataTool(BaseTool):
    name: str = "MarketDataTool"
    description: str = "Use this tool to get the latest stock price and news for a given ticker symbol (e.g. 'AAPL', 'NVDA'). Returns a summary string."

    def _run(self, ticker: str) -> str:
        print(f"\n   [TOOL] 📡 Fetching data for: {ticker}...")

        if ticker.upper() in ["BTC", "ETH", "SOL"]:
            ticker = f"{ticker.upper()}-USD"

        try:
            stock = yf.Ticker(ticker)
            history = stock.history(period="1d")
            price = "Unknown"
            if not history.empty:
                price = f"${history['Close'].iloc[-1]:.2f}"

            news_title = "No news found"

            try:
                if stock.news:
                    news_title = stock.news[0]['title']
            except:
                pass

            if news_title == "No news found":
                print(f"   [TOOL] 🦆 Yahoo failed. Searching DuckDuckGo for {ticker} news...")
                search = DuckDuckGoSearchRun()
                news_title = search.run(f"latest financial news for {ticker} today")
            return f"Data for {ticker}: Price is {price}. Latest News: '{news_title}'"
        except Exception as e:
            return f"Error fetching data for {ticker}: {e}"

    def _arun(self, ticker: str):
        raise NotImplementedError("Async not implemented")
