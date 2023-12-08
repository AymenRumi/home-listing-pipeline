from .celery_app import run_etl_worker
from .pipe import Extract


def run(dev: bool = False):

    workload = Extract.get_workload()

    action = {True: run_etl_worker, False: run_etl_worker.delay}

    return [action[dev](pages) for pages in workload]


def run_local(dev: bool = False):

    # workload = Extract.get_total_pages()
    pages = list(range(2, 4))

    action = {True: run_etl_worker, False: run_etl_worker.delay}

    return action[dev](pages)
