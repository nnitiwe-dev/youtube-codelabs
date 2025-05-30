from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.openai_helper import get_math_response 
from dotenv import load_dotenv
from datetime import datetime
import os

# Load .env variables
load_dotenv()


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def ask_math(request: Request, question: str = Form(...)):
    
    

    result = get_math_response(question)
    if result is not None:
        # Store the result 
        user_query={"type": "user", "message": question, "timestamp": datetime.utcnow()}

        # Store user query
        agent_query={"type": "agent", "message": result, "timestamp": datetime.utcnow()}

        response=[user_query, agent_query]


    return templates.TemplateResponse("index.html", {"request": request, "response": response})
