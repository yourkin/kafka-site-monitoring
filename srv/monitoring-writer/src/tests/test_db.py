from datetime import datetime

from sitemonitor.db import Writer
from sitemonitor.settings import TEST_DB_URL


def test_db_writer():
    data_in = {
        "url": "https://google.com",
        "status_code": 200,
        "response_time": 0.1,
        "pattern": "[w]",
        "is_pattern_found": True,
        "datetime_checked": datetime.now(),
    }
    with Writer(database_url=TEST_DB_URL) as writer:
        writer.save_entry(data_in)
        data_out = writer.get_last_entry()
    del data_out["row_id"]
    assert data_in == data_out
