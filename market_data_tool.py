from langchain.tools import BaseTool

class MarketDataTool(BaseTool):
    name:str = "MarketDataTool"
    description:str = """
    Use this tool to get the latest market data including stock prices, indices, and financial news.

    # Inputs
    - "symbol": Stock ticker symbol (e.g. "AAPL" for Apple Inc.)
    - "data_type": Type of data requested ("price", "news", "indices")
    - "date_range": Date range for historical data (e.g. "2023-01-01 to 2023-01-31")
    """

    return_direct: bool = False

    def _run(self, action):
        return ""