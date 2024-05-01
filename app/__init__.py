import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.router import router

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.join(CURRENT_PATH, "static")

app: FastAPI = None


def get_app() -> FastAPI:
    global app
    if app is None:
        app = FastAPI(tags=["API"])
        app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
        app.include_router(router)
    return app
