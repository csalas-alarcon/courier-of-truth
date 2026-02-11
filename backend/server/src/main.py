from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import os
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

LLAMA_URL = "http://llama_server:8080"
MODEL_NAME = "qwen"  # change if you want another model

def query(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": f"\nUser: {prompt}\nAssistant:",
        "n_predict": 200,
        "temperature": 0.2,
        "stop": ["User:", "Assistant:", "\nUser:", "<|im_end|>", "<|endoftext|>"],
        "cache_prompt": True
    }
    response = requests.post(
        f"{LLAMA_URL}/completion",
        json=payload,
        timeout=60
    )
    response.raise_for_status()
    return response.json()["content"].strip()

@app.get("/", response_class=HTMLResponse)
def normal(request: Request):
    try:
        text = query("Give a speech against some assasin robots called 'Automatons'. They're very dangerous.")
    except Exception as e:
        text = f"LLAMA ERROR: {e}"
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "llama_output": text}
    )
