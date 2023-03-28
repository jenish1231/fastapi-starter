from app.postgres.dependencies import get_db

from app.postgres.models import User
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class SQLUserRepository:

    def __init__(
        self,
        session: AsyncSession = Depends(get_db),
    ):
        self.session = session

    async def get_users(self):

        q = select(User)
        result = await self.session.execute(q)
        return result.scalars().all()

    async def get_user(self, id: int):

        q = select(User).where(User.id == id)
        result = await self.session.execute(q)
        return result.scalars().first()

    async def create_user(self, user: User):
        self.session.add(user)
        await self.session.commit()
        return user
