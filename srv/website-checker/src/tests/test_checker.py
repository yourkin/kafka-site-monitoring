import datetime

from src.app.checker import Checker


def test_checker():
    url = "https://google.com/"
    pattern = "sometext"
    checker = Checker(url=url, pattern=pattern)
    checker.get_url()
    assert checker.url == url
    assert checker.pattern == pattern
    assert type(checker.status_code) is int
    assert type(checker.response_time) is datetime.timedelta
    assert type(checker.page_contents) is str
    # assert type(checker.is_pattern_found) is bool