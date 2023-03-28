from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class GenericResponse(GenericModel, Generic[DataT]):
    data: Optional[DataT]
    success: bool = Field(True)


class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
