from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from my_models import GEMINI_FLASH, GROQ_VISION_MODEL
from my_keys import GEMINI_API_KEY, GROQ_API_KEY
from my_helper import encode_reduced_image
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



llm = ChatGoogleGenerativeAI(
    model=GEMINI_FLASH,
    api_key=GEMINI_API_KEY
)

response = llm.invoke(["What Youtube channel is best for learning about investing?"])

print("Gemini Response:", response.content)

llm = ChatGroq(
    model=GROQ_VISION_MODEL,
    api_key=GROQ_API_KEY
)

response = llm.invoke(["What Youtube channel is best for learning about investing?"])

print("Groq Response:", response.content)

image = encode_reduced_image("data/chart_gold.png")


template_analyze = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert data analyst. Analyze the image provided and give detailed insights about the data shown.
            Your main goal is to help users understand trends, patterns, and significant points in the data.

            # Output Format
            Provide your analysis in a clear and structured format, including:
            1. Summary of Findings
            2. Key Trends
            3. Notable Data Points
            4. Recommendations (if applicable)
            """
        ),
        (
            "user",
            [
                {
                    "type": "text",
                    "text": "Analyze the following image and provide insights about the data presented in it."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/png;base64,{selected_image}"
                    }
                }
            ]
        )
    ]
)


chain = template_analyze | llm | StrOutputParser()
response = chain.invoke(
    {
        "selected_image": image
    }
)
