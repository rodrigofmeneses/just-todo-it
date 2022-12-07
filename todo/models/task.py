"""Post related data models"""

import enum
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, Extra
from sqlmodel import Field, Relationship, SQLModel, Column, Enum

if TYPE_CHECKING:
    from todo.models import User

class TaskStatus(str, enum.Enum):
    '''Takes a plain text and valid if enum type
    class Task(SQLModel, table=True):
        status: TaskStatus
    '''
    TODO = 'TODO'
    DOING = 'DOING'
    DONE = 'DONE'
    
    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate
    
    @classmethod
    def validate(cls, value):
        '''Accepts a plain text'''
        if not isinstance(value, str):
            raise TypeError('string required')

        if value not in (TaskStatus.TODO, TaskStatus.DOING, TaskStatus.DONE):
            raise ValueError('must be value TODO, DOING or DONE')

        return cls(value)

    def __repr__(self):
        return self.value


class Task(SQLModel, table=True):
    """Represents the Task Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    status: TaskStatus = Field(default='TODO', sa_column=Column(Enum(TaskStatus)), nullable=False)
    user_id: int = Field(foreign_key="user.id")

    # It populates a `.posts` attribute to the `User` model.
    user: Optional['User'] = Relationship(back_populates="tasks")


class TaskResponse(BaseModel):
    """Serializer for Post Response"""

    id: int
    text: str
    date: datetime
    user_id: int
    parent_id: Optional[int]


class TaskRequest(BaseModel):
    """Serializer for Post request payload"""
    
    text: str

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True
