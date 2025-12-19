from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.auth import validate_login
from app.models import LoginRequest

app = FastAPI(title="Gemini AI Orbit")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()

@app.post("/login")
def login(data: LoginRequest):
    return validate_login(data)
