from remax_pipeline.celery_app import run_etl_worker


def run(dev: bool = False):

    pages = [1, 2]

    action = {True: run_etl_worker, False: run_etl_worker.delay}

    return action[dev](pages)
