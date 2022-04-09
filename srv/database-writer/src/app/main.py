import logging

from fastapi import FastAPI

from .routers import heartbeat

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    fastapi_app = FastAPI(
        title="Database Writer API",
        description="API to write to DB",
        version="0.1.0"
    )
    fastapi_app.include_router(heartbeat.router)
    return fastapi_app


def additional_setup(fastapi_app: FastAPI) -> FastAPI:
    return fastapi_app


application = additional_setup(create_application())


@application.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@application.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
