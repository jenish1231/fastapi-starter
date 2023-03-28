import typing as ty

from app.postgres.database import setup_db

from fastapi import FastAPI


def register_startup_event(app: FastAPI) -> ty.Callable[[], ty.Awaitable[None]]:

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        await setup_db(app)

    return _startup
