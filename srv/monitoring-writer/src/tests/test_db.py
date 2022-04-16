from datetime import datetime

from sitemonitor.db import Writer


def test_db_writer():
    data = {"url": "https://google.com", "status_code": 200, "response_time": 0.1, "pattern": "[w]",
            "is_pattern_found": True, "datetime_checked": datetime.now()}
    with Writer() as writer:
        writer.insert_row(data)