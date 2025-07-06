from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/process")
async def process_text(data: TextInput):
    # TODO: Clean and prepare the text
    cleaned = data.text.strip().replace("\n", " ").replace("  ", " ")
    return cleaned
