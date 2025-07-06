import os
from fastapi import FastAPI
from pydantic import BaseModel
from mistralai import Mistral

app = FastAPI()

class TextInput(BaseModel):
    text: str

# Prompt for API key if not set
if "MISTRAL_API_KEY" not in os.environ:
    os.environ["MISTRAL_API_KEY"] = input("Enter your Mistral API key: ")

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]
MISTRAL_MODEL = "mistral-large-latest"
client = Mistral(api_key=MISTRAL_API_KEY)

# Define the FastAPI application and the endpoint for processing text input
@app.post("/process")
async def process_text(data: TextInput):
    prompt = (
        "Extract the most important information from the following text and "
        "transform it into Anki flashcards in Q&A format. "
        "Format the answers in a JSON array containing front, back and tags fields.\n\n"
        f"Text:\n{data.text}"
    )
    chat_response = client.chat.complete(
        model = MISTRAL_MODEL,
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that extracts key information from text and formats it into Anki flashcards. Please format the answers in a JSON array containing front, back and tags fields.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    print("Processed text:", chat_response.choices[0].message.content)
    return chat_response.choices[0].message.content
