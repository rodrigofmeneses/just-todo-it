from typing import Optional
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

from todo.security import HashedPassword


class User(SQLModel, table=True):
    '''Represents the User Model'''
    
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False)
    password: HashedPassword = Field(nullable=False)


class UserResponse(BaseModel):
    '''Serializer for User Response'''
    
    id: int
    username: str


class UserRequest(BaseModel):
    '''Serializer for User Request payload'''
    
    username: str
    password: str