from asyncio import current_task

from app.postgres.models import Base

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


async def setup_db(app: FastAPI):
    engine = create_async_engine(DATABASE_URL, future=True, echo=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Creating database")

    session_factory = async_scoped_session(
        sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        ),
        scopefunc=current_task,
    )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory
