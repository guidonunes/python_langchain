# market_data_tool.py
from langchain.tools import BaseTool
from typing import Optional, Type
import requests
import yfinance as yf
from duckduckgo_search import DDGS

class MarketDataTool(BaseTool):
    name: str = "MarketDataTool"
    description: str = "Use this tool to get the latest stock price and news for a given ticker symbol (e.g. 'AAPL', 'NVDA'). Returns a summary string."

    def _run(self, ticker: str) -> str:
        print(f"\n   [TOOL] 📡 Fetching data for: {ticker}...")

        if ticker.upper() in ["BTC", "ETH", "SOL"]:
            ticker = f"{ticker.upper()}-USD"

        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })

        try:
            stock = yf.Ticker(ticker, session=session)
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
                try:
                    ddgs = DDGS()
                    results = list(ddgs.text(f"latest financial news for {ticker} today", max_results=1))

                    if results:
                        news_title = results[0]['title']
                except Exception as e:
                    print(f"   [WARNING] DuckDuckGo failed (likely Rate Limit): {e}")
                    news_title = "News currently unavailable due to search limits."

            return f"Data for {ticker}: Price is {price}. Latest News: '{news_title}'"
        except Exception as e:
            return f"Error fetching data for {ticker}: {e}"


    def _arun(self, ticker: str):
        raise NotImplementedError("Async not implemented")
