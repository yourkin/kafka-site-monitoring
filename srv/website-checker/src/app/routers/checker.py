from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .models import Input, Output

router = APIRouter()


@router.post("/website-checker")
async def website_checker(input: Input):
    """
    The website checker should perform the checks periodically and collect the HTTP response time, status code returned,
    as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on the
    page.
    """
    content = {
        "input": input.dict(),
    }
    return JSONResponse(content)
