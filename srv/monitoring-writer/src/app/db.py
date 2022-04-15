import os

import psycopg


def connect():
    try:
        DATABASE_URL = os.environ["DATABASE_URL"]
    except KeyError:
        raise EnvironmentError("DATABASE_URL not set")
    return psycopg.connect(DATABASE_URL)


with connect() as conn:
    with conn.cursor() as cur:
        cur.execute(
        """
        CREATE TABLE IF NOT EXISTS monitoring (
            url varchar,
            status_code smallint,
            response_time float,
            pattern varchar,
            is_pattern_found boolean,
            datetime_checked varchar(32)
        )
        """
    )


def insert_row(data, table: str = "monitoring"):
    query = f"""INSERT INTO {table} ({', '.join(data.keys())}) 
                VALUES ({', '.join(len(data.keys()) * ['%s'])});"""
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(query, list(data.values()))

# class Writer:
#
#     def __init__(self):
#         self._conn = connect()
#         self._cur = self._conn.cursor()
#         print("connected")
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self._conn.close()

    # def insert_row(self, table: str, field_names: list, data: namedtuple):
    #     query = f"""INSERT INTO {table} ({', '.join(field_names)})
    #                 VALUES ({', '.join(len(field_names) * ['%s'])});"""
    #     self.cursor.execute(query, data)
    #     self.conn.commit()
