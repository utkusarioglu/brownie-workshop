from dotenv import load_dotenv
from os import environ
from celery import Celery

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
    "taskmeta_collection": "celery",
}

mongodb_result_backend = "".join(
    [
        "mongodb://",
        MONGODB_USERNAME,
        ":",
        MONGODB_PASSWORD,
        "@",
        MONGODB_URL,
        "/",
        MONGODB_CELERY_RESULTS_DB_NAME,
    ]
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
