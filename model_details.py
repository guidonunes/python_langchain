from typing import List
from pydantic import BaseModel, Field


class ModelDetails(BaseModel):
    sentiment: str = Field(description="The market sentiment: BULLISH, BEARISH, or NEUTRAL")
    tickers: List[str] = Field(description="List of stock ticker symbols mentioned (e.g. ['AAPL'])")
    urgency: int = Field(description="A score from 1-10 indicating how important this news is")
