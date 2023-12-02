from celery import Celery

from .config.settings import CelerySettings
from .tasks.etl_worker import start_worker

celery_app = Celery("app", broker=CelerySettings().rabbitmq_broker)


@celery_app.task
def run_etl_worker(pages: list):
    print(start_worker(pages))
