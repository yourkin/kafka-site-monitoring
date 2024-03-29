from fastapi import APIRouter

from sitechecker.checker import Checker
from sitechecker.sender import SendData

from ..models import WebsiteParams, WebsiteStatus

router = APIRouter()


@router.get("/website-checker", response_model=WebsiteStatus)
async def website_checker(params: WebsiteParams):
    """
    The website checker should perform the checks periodically and collect the HTTP response time, status code returned,
    as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the
    page.
    """
    checker = Checker(url=params.url, pattern=params.pattern)
    return WebsiteStatus.from_orm(checker)


@router.post("/send-website-data")
async def send_website_data(website_status: WebsiteStatus):
    SendData.send_data("users", website_status.json())
    return None
