import uvicorn
from fastapi import FastAPI

from mail_app.src.routers import ROUTERS
from mail_app.src.settings import SERVER_ADDRESS, SERVER_PORT, APP_NAME


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

if __name__ == '__main__':
    run()