from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel

from todo.security import HashedPassword

if TYPE_CHECKING:
    from todo.models import Task


class User(SQLModel, table=True):
    """Represents the User Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    password: HashedPassword = Field(nullable=False)

    tasks: List["Task"] = Relationship(back_populates="user")


class UserBase(BaseModel):
    """Base User serializer"""

    username: str


class UserResponse(UserBase):
    """Serializer for User Response"""

    id: int


class UserRequest(UserBase):
    """Serializer for User Request payload"""

    password: str
