from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/heartbeat")
async def heartbeat():
    content = {
        "heartbeat": "OK",
    }
    return JSONResponse(content)
