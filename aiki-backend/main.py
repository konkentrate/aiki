import os
from fastapi import FastAPI
from pydantic import BaseModel
from mistralai import Mistral

app = FastAPI()

class TextInput(BaseModel):
    text: str

os.environ["MISTRAL_API_KEY"] = "your_mistral_api_key_here"  # Replace with your actual Mistral API key

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]
MISTRAL_MODEL = "mistral-large-latest"

client = Mistral(api_key=MISTRAL_API_KEY)

# Initialize the Mistral client
chat_response = client.chat.complete(
    model = MISTRAL_MODEL,
    messages=[
        # {
        #     "role": "system",
        #     "content": "You are a helpful assistant that extracts key information from text and formats it into Anki flashcards.",
        # },
        {
            "role": "user",
            "content": "Extract the most important information from the following text and transform it into Anki flashcards in Q&A format.",
        },
    ],
)

#@app.post("/process")
#async def process_text(data: TextInput):


print("Processed text:", chat_response)