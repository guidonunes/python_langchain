from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH, GROQ_MODEL
from my_keys import GEMINI_API_KEY, GROQ_API_KEY
from langchain_core.globals import set_debug
set_debug(False)

from langchain import hub
from langchain.agents import create_react_agent
from langchain.tools import Tool
from market_data_tool import MarketDataTool


class Orchestrator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=GEMINI_FLASH,
            api_key=GEMINI_API_KEY
        )

        market_data_tool = MarketDataTool()

        self.tools = [
            Tool(
                name= market_data_tool.name,
                func= market_data_tool.run,
                description= market_data_tool.description,
                return_direct = market_data_tool.return_direct
            )
        ]

        prompt = hub.pull("hwchase17/react")

        self.agent = create_react_agent(self.llm, self.tools, prompt)
