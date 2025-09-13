from fastapi import FastAPI

from app.web.core.routers import router
from app.web.lifetime import register_startup_event


def create_app():
    app = FastAPI()

    app.include_router(router, prefix="/api")

    register_startup_event(app)

    return app
