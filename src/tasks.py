from dotenv import load_dotenv
from os import environ
from celery import Celery
from src.deploy import deploy_contract
from src.get_value import get_value
from src.set_value import set_value

PYTHONPATH = environ.get("PYTHONPATH")

load_dotenv(f"{PYTHONPATH}/.env")

REDIS_URL = environ.get("REDIS_URL", "")
MONGODB_URL = environ.get("MONGODB_URL", "")
MONGODB_USERNAME = environ.get("MONGODB_USERNAME", "")
MONGODB_PASSWORD = environ.get("MONGODB_PASSWORD", "")
MONGODB_CELERY_RESULTS_DB_NAME = environ.get(
    "MONGODB_CELERY_RESULTS_DB_NAME", ""
)

MONGODB_BACKEND_SETTINGS = {
    "database": MONGODB_CELERY_RESULTS_DB_NAME,
    "taskmeta_collection": "sample_contract",
}

mongodb_result_backend = "".join(
    ["mongodb://", MONGODB_USERNAME, ":", MONGODB_PASSWORD, "@", MONGODB_URL]
)

app = Celery(
    "tasks",
    broker=f"redis://{REDIS_URL}",
    result_backend=mongodb_result_backend,
    mongodb_backend_settings=MONGODB_BACKEND_SETTINGS,
    broker_connection_retry_on_startup=True,
)


@app.task
def add(x, y):
    return x + y


@app.task
def deploy_sample_contract():
    return deploy_contract()


@app.task
def get_sample_value():
    return get_value()


@app.task
def set_sample_value(val: int):
    return set_value(val)
