from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import redis
import time
import json
from uuid import uuid4

REDIS_QUEUE = "service_queue"
API_SLEEP = 0.05

app = FastAPI()
templates = Jinja2Templates(directory="/api/templates")
db = redis.StrictRedis(host="redis", port=6379)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
def send_review(request: Request, user_input:str = Form(...)):
    prediction = get_prediction(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "prediction": prediction})

def get_prediction(user_input):
    job_id = str(uuid4())
    job_data = {
        "id": job_id,
        "user_input": user_input
    }
    db.lpush(
        REDIS_QUEUE,
        json.dumps(job_data)
    )
    
    while True:
        # Attempt to get model predictions using job_id
        output = db.get(job_id)
        if output is not None:
            db.delete(job_id)
            # To return just a string with the prediction
            output = output.decode("utf-8").replace('"', '')
            return output
        else:
            time.sleep(API_SLEEP)