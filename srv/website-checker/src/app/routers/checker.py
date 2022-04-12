from fastapi import APIRouter

from ..checker import Checker
from ..models import Input, Output

router = APIRouter()


@router.post("/website-checker", response_model=Output)
async def website_checker(input: Input):
    """
    The website checker should perform the checks periodically and collect the HTTP response time, status code returned,
    as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the
    page.
    """
    checker = Checker(url=input.url, pattern=input.pattern)
    checker.get_url()
    output = Output(status_code=checker.status_code, response_time=checker.response_time, is_pattern_found=None)
    return output
