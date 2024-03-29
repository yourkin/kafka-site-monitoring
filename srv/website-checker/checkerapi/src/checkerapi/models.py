import datetime

from pydantic import BaseModel, HttpUrl


class WebsiteParams(BaseModel):
    url: HttpUrl
    pattern: str | None


class WebsiteStatus(WebsiteParams):
    response_time: datetime.timedelta
    status_code: int
    is_pattern_found: bool | None
    datetime_checked: datetime.datetime

    class Config:
        orm_mode = True  # this allows to load data from a class, unrelated to database operations
