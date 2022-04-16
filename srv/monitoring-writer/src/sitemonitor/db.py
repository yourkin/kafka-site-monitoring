import psycopg

from sitemonitor.settings import DATABASE_URL, MONITORING_TABLE


class Writer:

    def create_table(self, table=MONITORING_TABLE) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {table} (
            url varchar,
            status_code smallint,
            response_time float,
            pattern varchar,
            is_pattern_found boolean,
            datetime_checked varchar(32)
        )
        """
        with self.conn.cursor() as cur:
            cur.execute(query)


    def __init__(self, database_url=DATABASE_URL):
        self.conn = psycopg.connect(database_url)

    def insert_row(self, data: dict, table: str = MONITORING_TABLE) -> None:
        query = f"""INSERT INTO {table} ({', '.join(data.keys())}) 
                    VALUES ({', '.join(len(data.keys()) * ['%s'])});"""
        with self.conn.cursor() as cur:
            cur.execute(query, list(data.values()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

        # with Writer() as conn:
        #     with conn.cursor() as cur:
        #         cur.execute(

Writer().create_table()
