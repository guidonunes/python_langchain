from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image



llm = ChatGoogleGenerativeAI(
    model=GEMINI_FLASH,
    api_key=GEMINI_API_KEY
)


image = encode_image("data/chart_gold.png")

query = f"""Analyze the following image and provide insights about the data presented in it.
Image: {image}"""

message = HumanMessage(content=[
    {
        "type": "text",
        "text": query
    },
    {
        "type": "image_url",
        "image_url": f"data:image/png;base64,{image}"
    }
])

response = llm.invoke([message])

print(response.content)
