from app.web.core.routers import router
from app.web.lifetime import register_startup_event
from fastapi import FastAPI


def create_app():
    app = FastAPI()

    app.include_router(router, prefix='/api')

    register_startup_event(app)

    return app
