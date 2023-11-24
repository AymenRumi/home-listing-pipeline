from src.main import run_etl_worker

if __name__ == "__main__":

    [run_etl_worker.delay(i) for i in range(20)]
