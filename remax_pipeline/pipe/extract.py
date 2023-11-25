from remax_pipeline.plugins.web_crawler import RemaxExecutor


class Extract:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_listing_data(self, pages: list, multithreaded: bool) -> dict:
        RemaxExecutor(multithreaded=multithreaded).get_multipage_listing(
            pages=pages, output=True, filename="output_1.json"
        )
