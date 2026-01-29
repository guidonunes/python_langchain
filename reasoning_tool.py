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

    # GROQ: THE SCALPER
    def _run(self, headline: str) -> str:
        """
        Input: A raw string containing the news headline.
        Output: A strategic portfolio update paragraph.
        """

        print(f"\n   [TOOL] 🤖 Analyzing headline: {headline[:20]}...")

        try:
            llm_groq = ChatGroq(model=GROQ_MODEL, api_key=GROQ_API_KEY, temperature=0)
            parser = PydanticOutputParser(pydantic_object=ModelDetails)

            groq_prompt = PromptTemplate(
                template ="""
                Analyze the following financial headline.
                Headline: "{headline}"
                {format_instructions}
                """,
                input_variables=["headline"],
                partial_variables={"format_instructions": parser.get_format_instructions()}
            )

            scalper_chain = groq_prompt | llm_groq | parser
            signal_data: ModelDetails = scalper_chain.invoke({"headline": headline})
            print(f"  [TOOL] Sentiment Detected: {signal_data.sentiment} (Urgency: {signal_data.urgency}/10)")



        except Exception as e:
            return f"Error during analysis (Groq): {e}"

        # GEMINI: THE STRATEGIST
        try:
            llm_gemini = ChatGoogleGenerativeAI(model=GEMINI_FLASH, api_key=GEMINI_API_KEY)
            gemini_prompt = PromptTemplate(
                template="""
                You are a senior portfolio manager.

                MARKET SIGNAL DATA:
                - Sentiment: {sentiment}
                - Urgency Score: {urgency}/10
                - Affected Tickers: {tickers}

                ORIGINAL NEWS:
                "{headline}"

                TASK:
                Write a concise, professional daily update for a wealthy client explaining
                what this news means for their portfolio. Focus on the strategy ("Why"), not just the news ("What").
                """
                input_variables=["sentiment", "urgency", "tickers", "headline"]
            )
        except Exception as e:
            return f"Error initializing Gemini LLM: {e}"

        # Run Gemini Chain
        strategist_chain = gemini_prompt | llm_gemini | StrOutputParser()
        final_advice = strategist_chain.invoke({
            "sentiment": signal_data.sentiment,
            "urgency": signal_data.urgency,
            "tickers": signal_data.tickers,
            "headline": headline
        })

        return final_advice
