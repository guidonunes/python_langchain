# market_data_tool.py
import os
from langchain.tools import BaseTool
from curl_cffi import requests as crequests
import yfinance as yf
from duckduckgo_search import DDGS
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

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
        except Exception as e:
            price = "Error fetching price"

        print(f"   [TOOL] 🔍 Searching news via Tavily for {ticker}...")

        try:
            client = TavilyClient(api_key=TAVILY_API_KEY)
            response = client.search(query=f"latest financial news for {ticker} today", limit=1)

            if response['results']:
                r = response['results'][0]
                news_title = f"{r['title']} - {r['content'][:100]}..."
            else:
                news_title = "No recent news found."
        except Exception as e:
            print(f"   [TOOL] ❌ Tavily failed: {e}")
            news_title = "News unavailable."

        return f"Data for {ticker}: Price is {price}. Latest News: '{news_title}'"


    def _arun(self, ticker: str):
        raise NotImplementedError("Async not implemented")
