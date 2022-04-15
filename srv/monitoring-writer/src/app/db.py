from collections import namedtuple
import os

import psycopg


class Writer:

    def _connect(self) -> psycopg.connect:
        try:
            DATABASE_URL = os.environ["DATABASE_URL"]
        except KeyError:
            raise EnvironmentError("DATABASE_URL not set")
        return psycopg.connect(DATABASE_URL)

    def _create_table(self) -> None:
        self._cur.execute(
            """
            CREATE TABLE IF NOT EXISTS monitoring (
                url varchar,
                status_code smallint,
                response_time float,
                pattern varchar,
                is_pattern boolean,
                datetime_checked varchar(32)
            )
            """
        )

    def __init__(self):
        self._conn = self._connect()
        self._cur = self._conn.cursor()
        self._create_table()
        print("connected")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()

    # def insert_row(self, table: str, field_names: list, data: namedtuple):
    #     query = f"""INSERT INTO {table} ({', '.join(field_names)})
    #                 VALUES ({', '.join(len(field_names) * ['%s'])});"""
    #     self.cursor.execute(query, data)
    #     self.conn.commit()
