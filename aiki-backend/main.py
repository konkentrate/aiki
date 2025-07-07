import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mistralai import Mistral
from dotenv import load_dotenv

app = FastAPI()

class TextInput(BaseModel):
    text: str

# Load the Mistral API key from environment variables
load_dotenv("api_key.env")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise ValueError("MISTRAL_API_KEY not set")

MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]
MISTRAL_MODEL = "mistral-small-latest"
client = Mistral(api_key=MISTRAL_API_KEY)

# Define the FastAPI application and the endpoint for processing text input
@app.post("/process")
async def process_text(data: TextInput):
    prompt = (
        "Extract the most important information from the following text and "
        "transform it into Anki flashcards in Q&A format.\n"
        "Format the answers in a JSON array without new lines - containing front, back and tags fields.\n\n"
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

    try:
        # Clean up response content and parse as JSON
        content = chat_response.choices[0].message.content
        content = content.replace("```json", "").replace("```", "").strip()
        aiki_cards = json.loads(content)
        return aiki_cards
    except json.JSONDecodeError:
        # If the response is not valid JSON, return raw content
        raise HTTPException(status_code=422, detail = "Invalid JSON format in response")

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)