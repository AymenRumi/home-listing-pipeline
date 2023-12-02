from .celery_app import run_etl_worker
from .db import init_db


@init_db
def run(dev: bool = False):

    # workload = Extract.get_total_pages()
    pages = list(range(1, 30))

    action = {True: run_etl_worker, False: run_etl_worker.delay}

    return action[dev](pages)
