import datetime

import httpx


class Checker:
    follow_redirects: bool
    url: str
    pattern: str | None
    response_time: datetime.timedelta
    status_code: int
    page_contents: str
    is_pattern_found: bool | None

    def __init__(self, url: str, pattern: str, follow_redirects: bool = True) -> None:
        self.follow_redirects = follow_redirects
        self.url = url
        self.pattern = pattern

    def get_url(self):
        response = httpx.get(self.url, follow_redirects=self.follow_redirects)
        self.status_code = response.status_code
        self.response_time = response.elapsed
        self.page_contents = response.content.decode("utf-8")
