from remax_pipeline.pipe import Extract, Validate, Load


def start_worker(pages: list):
    return Extract.get_listing_data(pages=pages, multithreaded=True)
