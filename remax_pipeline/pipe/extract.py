from ..plugins.web_crawler import RemaxExecutor


class Extract:
    @staticmethod
    def get_listing_data(pages: list, multithreaded: bool) -> list:
        return RemaxExecutor(multithreaded=multithreaded).get_multipage_listing(pages=pages, output=False)

    @staticmethod
    def get_total_pages() -> int:
        return RemaxExecutor().get_total_pages()
