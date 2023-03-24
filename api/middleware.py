import redis
import time
import os
import json
from uuid import uuid4

REDIS_QUEUE = "service_queue"
API_SLEEP = 0.05
db = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

def predict_sentiment(review):
    job_id = str(uuid4())
    job_data = {
        "id": job_id,
        "review": review
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
            return output
        else:
            time.sleep(API_SLEEP)