import os
import json
import time
from ml import predict

REDIS_IP = os.getenv("REDIS_IP", "redis")
REDIS_PORT = 6379
REDIS_DB_ID = 0
REDIS_QUEUE = "service_queue"
SERVER_SLEEP = 0.05

db = redis.Redis(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB_ID)

def get_sentiment():
    while True:
        _, msg = db.brpop(REDIS_QUEUE)
        job_data = json.loads(msg)
        review = job_data["review"]
        job_id = job_data["id"]
        sentiment = predict(review)
        db.set(job_id, json.dumps(sentiment))
        time.sleep(SERVER_SLEEP)