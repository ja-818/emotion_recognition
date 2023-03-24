import os
import json
import time
import redis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


REDIS_IP = os.getenv("REDIS_IP", "redis")
REDIS_PORT = 6379
REDIS_DB_ID = 0
REDIS_QUEUE = "service_queue"
SERVER_SLEEP = 0.05

# db = redis.Redis(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB_ID)
# db = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

db = redis.Redis(
  host="redis",
  port=6379
  )

def predict(user_input):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(user_input)
    prediction = ""
    
    if sentiment_dict['compound'] >= 0.05 :
        prediction = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        prediction = "Negative"

    else :
        prediction = "Neutral"  

    return prediction

def classify_process():
    while True:
        _, msg = db.brpop(REDIS_QUEUE)
        job_data = json.loads(msg)
        user_input = job_data["user_input"]
        job_id = job_data["id"]
        prediction = predict(user_input)
        db.set(job_id, json.dumps(prediction))
        time.sleep(SERVER_SLEEP)

if __name__ == "__main__":
    classify_process()