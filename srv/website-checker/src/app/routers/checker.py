from fastapi import APIRouter

from .models import Input, Output

router = APIRouter()


@router.post("/website-checker", response_model=Output)
async def website_checker(input: Input):
    """
    The website checker should perform the checks periodically and collect the HTTP response time, status code returned,
    as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the
    page.
    """
    status_code = 200
    response_time = 0
    output = Output(status_code=status_code, response_time=response_time, is_pattern_found=None)
    return output
