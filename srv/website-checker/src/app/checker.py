import datetime
import re

import httpx


class Checker:
    response_time: datetime.timedelta
    status_code: int
    page_contents: str
    is_pattern_found: bool | None
    url: str
    pattern: str
    datetime_checked: datetime.datetime

    def __init__(
        self, url: str, pattern: str | None, follow_redirects: bool = True
    ) -> None:
        self.url = url
        self.pattern = pattern
        self._check_url(url, follow_redirects)
        self._check_pattern(pattern, self.page_contents)

    def _check_url(self, url, follow_redirects) -> None:
        try:
            response = httpx.get(url, follow_redirects=follow_redirects)
        except Exception:  # broad exception to catch all network errors, not important which ones exactly
            pass
        else:
            self.status_code = response.status_code
            self.response_time = response.elapsed
            self.page_contents = response.content.decode("utf-8")
        finally:
            self.datetime_checked = datetime.datetime.now()

    def _check_pattern(self, pattern, content) -> None:
        if pattern:
            self.is_pattern_found = bool(re.search(pattern, content))
