import datetime

from pydantic import BaseModel, HttpUrl


class Input(BaseModel):
    url: HttpUrl
    pattern: str | None


class Output(BaseModel):
    response_time: datetime.timedelta
    status_code: int
    is_pattern_found: bool | None