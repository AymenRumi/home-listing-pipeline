import os
import sys

import psycopg2

from ..config.settings import PostegresSettings


def database_exists(conn, dbname):
    pass


def create_database(conn, dbname):
    pass


def connect():

    settings = PostegresSettings()

    conn = psycopg2.connect(
        dbname=settings.dbname,
        user=settings.user,
        password=settings.password,
        host=settings.password,
        port=settings.port,
    )

    return conn


if __name__ == "__main__":
    if sys.argv[1] == "db-ready":
        try:
            connect()
        except psycopg2.OperationalError as e:
            print(e)
            sys.exit(-1)
    elif sys.argv[1] == "create-if-noexist":
        conn = connect()
        conn.autocommit = True
        db_name = os.environ["POSTGRES_DB"]
        try:
            if not database_exists(conn, db_name):
                print(f"Database {db_name} does not exist! Will create it.")
                create_database(conn, db_name)
                print(f"Created {db_name}.")
            else:
                print(f"Database {db_name} already exists, nothing to do.")
        finally:
            conn.close()
