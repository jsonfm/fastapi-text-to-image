from fastapi import FastAPI
from app.router import router


app: FastAPI = None


def get_app() -> FastAPI:
    global app
    if app is None:
        app = FastAPI(tags=["API"])
        app.include_router(router)
    return app
