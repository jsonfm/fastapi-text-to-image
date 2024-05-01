import os
from fastapi import FastAPI
from app.router import router

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_PATH = os.path.join(CURRENT_PATH, "static")

app: FastAPI = None


def get_app() -> FastAPI:
    global app
    if app is None:
        app = FastAPI(tags=["API"], title="Text To Image API")
        app.include_router(router)
    return app
