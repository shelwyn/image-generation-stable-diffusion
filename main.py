from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
import uuid
from pathlib import Path

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create images directory if it doesn't exist
IMAGES_DIR = Path("generated_images")
IMAGES_DIR.mkdir(exist_ok=True)

# Initialize the HuggingFace client
client = InferenceClient(
    model="runwayml/stable-diffusion-v1-5",
    token=os.getenv("HF_TOKEN")
)

class ImagePrompt(BaseModel):
    prompt: str

@app.post("/generate-image")
async def generate_image(prompt_data: ImagePrompt):
    try:
        # Generate unique filename
        filename = f"{uuid.uuid4()}.png"
        filepath = IMAGES_DIR / filename

        # Generate image
        image = client.text_to_image(prompt_data.prompt)
        
        # Save image
        image.save(filepath)
        
        return {"filename": filename}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/images/{filename}")
async def get_image(filename: str):
    filepath = IMAGES_DIR / filename
    if not filepath.exists():
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(filepath)
