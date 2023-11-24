import os

from celery import Celery

from remax_pipeline.utils.logging import logger

app = Celery("app", broker="pyamqp://myuser:mypassword@localhost:5672//")


@app.task
def run_etl_worker(instance: int):
    logger.task(f"Running Task: {os.getcwd()} {instance}....")
