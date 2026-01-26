from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from langchain_core.globals import set_debug
set_debug(False)

from langchain_classic import hub
from langchain_classic.agents import create_react_agent
from market_data_tool import MarketDataTool


class Orchestrator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=GEMINI_FLASH,
            api_key=GEMINI_API_KEY
        )
        self.tools = [
            MarketDataTool()
        ]

        prompt = hub.pull("hwchase17/react")

        self.agent = create_react_agent(self.llm, self.tools, prompt)
