from fastapi import FastAPI
from ml import sentiment_analysis

app = FastAPI()

@app.get("/")
def root():
    return "Holo bolo"

@app.get("/sentiment")
def return_sentiment_analysis(prompt: str):
    return sentiment_analysis(prompt) 