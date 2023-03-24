from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middleware import predict_sentiment
import redis

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def send_review(request: Request, review:str = Form(...)):
    sentiment = "Sentiment:" + predict_sentiment(review)
    return templates.TemplateResponse("index.html", {"request": request, "sentiment": sentiment})