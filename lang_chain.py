from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from my_models import GEMINI_FLASH, GROQ_MODEL
from my_keys import GEMINI_API_KEY, GROQ_API_KEY
from my_helper import encode_reduced_image
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from model_details import ModelDetails
from langchain_core.globals import set_debug
set_debug(True)




llm_fast = ChatGroq(
    model=GROQ_MODEL,
    api_key=GROQ_API_KEY
)

llm_smart = ChatGoogleGenerativeAI(
    model=GEMINI_FLASH,
    api_key=GEMINI_API_KEY
)

headline = "Tech stocks soar as new AI advancements promise to revolutionize the industry"
parser_json = JsonOutputParser(pydantic_object=ModelDetails)

# CASE: GROQ for sensing, Gemini for reasoning
sentiment_template = PromptTemplate(
    template="""
    You are a high-frequency trading algorithm.
    Analyze the following financial headline.

    Headline: "{headline}"

    Output ONLY a Python dictionary with:
    - "sentiment": "BULLISH", "BEARISH", or "NEUTRAL"
    - "tickers": [List of companies affected]
    - "urgency": 1-10 scale

    Do not add any conversational text.

    # Output format
    {output_format}
    """,
    input_variables=["headline"],
    partial_variables={
        "output_format": parser_json.get_format_instructions()
    }
)


analysis_template = ChatPromptTemplate.from_messages([
    ("system", "You are a senior portfolio manager writing a daily update for wealthy clients."),
    ("human", """
    We just received a signal from our trading algo:
    {signal_data}

    The original news was: "{headline}"

    Write a short paragraph (5 sentences max) explaining what this means for their portfolio.
    Focus on the "Why", not just the "What".
    """)
])




summary_chain = sentiment_template | llm_fast | StrOutputParser()

analysis_chain = analysis_template | llm_smart | StrOutputParser()

raw_signal = summary_chain.invoke({"headline": headline})

final_analysis = analysis_chain.invoke({
    "signal_data": raw_signal,
    "headline": headline
})

print("Final Analysis:")
print(final_analysis)
