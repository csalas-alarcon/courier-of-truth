from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount("/static", StaticFiles(directory = "src/static"), name = "static")
templates = Jinja2Templates(directory = "src/templates")

@app.get("/", response_class = HTMLResponse)
def normal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})