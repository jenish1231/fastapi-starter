from typing import List

from fastapi import APIRouter, Depends

from app.postgres.repository.user_repo import SQLUserRepository
from app.web.core.users.protocols import IUserRepository
from app.web.core.users.schemas import GenericResponse, UserSchema
from app.web.core.users.services import UserService

router = APIRouter()


@router.get(
    "/users",
    description="Get all users",
    include_in_schema=True,
    tags=["users"],
    status_code=200,
    response_model=GenericResponse[List[UserSchema]],
)
async def get_users(
    service: UserService = Depends(),
    repository: IUserRepository = Depends(SQLUserRepository),
):
    users_from_sql = await service.get_users(repository)

    return GenericResponse(data=users_from_sql)


@router.get("/users/{id}", response_model=GenericResponse[UserSchema])
async def get_user(
    id: int,
    service: UserService = Depends(),
    repository: IUserRepository = Depends(SQLUserRepository),
):
    user_from_sql = await service.get_user(repository, id=id)
    return GenericResponse(data=user_from_sql)
