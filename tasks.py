from celery import Celery
from local_settings import BROKER_URL
# BROKER_URL = 'mongodb://localhost:27017/helloCelery'

app = Celery('tasks', broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y

@app.task
def prod(x, y):
    return x*y