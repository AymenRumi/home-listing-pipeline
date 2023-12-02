import time
from typing import List

from ..models import HomeListing
from ..services.sql_service import insert_listings


class Load:
    @classmethod
    def push_to_db(cls, listings: List[HomeListing], start_time: float) -> dict:
        response = insert_listings(listings)
        response["time"] = time.time() - start_time
        return response
