from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from my_models import GEMINI_FLASH, GROQ_VISION_MODEL
from my_keys import GEMINI_API_KEY, GROQ_API_KEY
from my_helper import encode_reduced_image



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

query = f"""Analyze the following image and provide insights about the data presented in it.
Image: {image}"""

message = HumanMessage(content=[
    {
        "type": "text",
        "text": query
    },
    {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{image}"
        }
    }
])

response = llm.invoke([message])

print(response.content)
