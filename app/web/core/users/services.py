
from app.web.core.users.protocols import IUserRepository


class UserService:

    async def get_users(self, repository: IUserRepository):
        results = await repository.get_users()
        return results

    async def get_user(self, repository: IUserRepository, *, id: int):
        return await repository.get_user(id)
