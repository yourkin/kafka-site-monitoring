import psycopg

from sitemonitor.settings import DATABASE_URL, MONITORING_TABLE


class Writer:
    def _create_table(self, table: str) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id SERIAL PRIMARY KEY, 
            url varchar,
            status_code smallint,
            response_time float,
            pattern varchar,
            is_pattern_found boolean,
            datetime_checked TIMESTAMP
        );
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(query)
                self.conn.commit()
        except Exception as e:  # broad exception because we need to catch all errors, except keyboard interrupt.
            print(f'Table creation for "{table}" failed with error: {e}.')

    def __init__(self, database_url: str = DATABASE_URL, table: str = MONITORING_TABLE) -> None:
        self.conn = psycopg.connect(database_url)
        self._create_table(table)

    def save_entry(self, data: dict, table: str = MONITORING_TABLE) -> None:
        query = f"""INSERT INTO {table} ({', '.join(data.keys())}) 
                    VALUES ({', '.join(len(data.keys()) * ['%s'])});"""
        with self.conn.cursor() as cur:
            cur.execute(query, list(data.values()))

    def get_last_entry(self, table: str = MONITORING_TABLE) -> dict:
        query = f"SELECT * FROM {table} ORDER BY id DESC LIMIT 1;" ""
        with self.conn.cursor() as cur:
            cur.execute(query)
            d = {}
            (
                d["row_id"],
                d["url"],
                d["status_code"],
                d["response_time"],
                d["pattern"],
                d["is_pattern_found"],
                d["datetime_checked"],
            ) = cur.fetchone()
        return d

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
