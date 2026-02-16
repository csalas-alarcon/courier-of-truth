# Generic Imports
import os
import requests
# FastAPI Imports
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# We instanciate It
app = FastAPI()

# We mount directories
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# Constants
LLAMA_URL = "http://llama_server:8080"
MODEL_NAME = "qwen" 
PETITION = "Give a speech against some assasin robots called 'Automatons'. They're very dangerous."

# FUNCTIONS
def query(prompt: str):
    # Design the Petition
    payload = {
        "model": MODEL_NAME,
        "prompt": f"\nUser: {prompt}\nAssistant:",
        "n_predict": 200,
        "temperature": 0.8,
        "stop": ["User:", "Assistant:", "\nUser:", "<|im_end|>", "<|endoftext|>"],
        "cache_prompt": False
    }
    # Send the Petition
    response = requests.post(
        f"{LLAMA_URL}/completion",
        json=payload,
        timeout=60
    )
    # Interpret the Response
    response.raise_for_status()
    return response.json()["content"].strip()

# ENDPOINTS
@app.get("/", response_class=HTMLResponse)
def normal(request: Request):
    # We try to get an Speech
    llama_text: str= 'Example'
    try:
        llama_text = query(PETITION)
    except Exception as e:
        llama_text = f"LLAMA ERROR: {e}"

    # Return the Page
    return templates.TemplateResponse("index.html",{"request": request, "llama_output": llama_text})
