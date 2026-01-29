from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser

from my_models import GEMINI_FLASH, GROQ_MODEL
from my_keys import GEMINI_API_KEY, GROQ_API_KEY
from model_details import ModelDetails



class ReasoningTool(BaseTool):
    name: str = "Financial_Analyst_Tool"
    description: str = "Use this tool to perform a deep technical and sentimental analysis on a specific "
    "news headline. Input should be the news headline text found by the MarketDataTool."


    def _run(self, headline: str) -> str:
        """
        Input: A raw string containing the news headline.
        Output: A strategic portfolio update paragraph.
        """

        print(f"\n   [TOOL] 🤖 Analyzing headline: {headline[:20]}...")
