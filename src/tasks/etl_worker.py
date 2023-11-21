from src import app
from src.pipe import Extract, Load, Validate


@app.task
def run_etl_worker(pages: list):
    Load().push_to_db(Validate().run_data_contract(Extract().get_listing_data()))
