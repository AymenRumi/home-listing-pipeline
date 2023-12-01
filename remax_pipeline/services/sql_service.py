from typing import List

from db import connect_db
from psycopg2 import sql

from ..models import HomeListing


def scd():
    pass


@connect_db
def insert_listings(listings: List[HomeListing]):

    with conn.cursor() as cursor:
        for listing in listings:
            query = sql.SQL(
                """
            INSERT INTO {}
            (id, full_address, street_name, city, province, postal_code, lat, lon, home_price, bed, bath, property_type, description, listing_date)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            ).format(sql.Identifier("home_listings"))

            data = (
                listing.id,
                listing.full_address,
                listing.street_name,
                listing.city,
                listing.province,
                listing.postal_code,
                listing.lat,
                listing.lon,
                listing.home_price,
                listing.bed,
                listing.bath,
                listing.property_type,
                listing.description,
                listing.listing_date,
            )
        cursor.execute(query, data)


def insert_run_log():
    pass
