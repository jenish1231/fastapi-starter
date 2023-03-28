
from typing import List, Protocol

from app.postgres.models import User


class IUserRepository(Protocol):
    async def get_users(self) -> List[str]:
        ...

    async def get_user(self, id: int) -> dict:
        ...

    async def create_user(self, user: User) -> User:
        ...

    async def get_user_by_name(self, name: str) -> dict:
        ...


__all__ = ["IUserRepository"]
