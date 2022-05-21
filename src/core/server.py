import uvicorn
from fastapi import FastAPI

from src.core.routers import ROUTERS
from src.core.settings import SERVER_ADDRESS, SERVER_PORT, APP_NAME


def add_routers(app: FastAPI, routers: list):
    for route in routers:
        app.include_router(route)


def create_app() -> FastAPI:
    app = FastAPI(
        title=APP_NAME
    )
    add_routers(app, ROUTERS)
    return app


app: FastAPI = create_app()


def run() -> None:
    uvicorn.run(app, host=SERVER_ADDRESS, port=SERVER_PORT)
