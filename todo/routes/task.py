from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from todo.auth import AuthenticatedUser
from todo.db import ActiveSession
from todo.models.task import (
    Task,
    TaskRequest,
    TaskResponse
)
from todo.models.user import User

router = APIRouter()


@router.get('/', response_model=List[TaskResponse])
async def list_all_tasks(*, session: Session = ActiveSession):
    '''List all tasks'''
    tasks = session.exec(select(Task)).all()
    return tasks

@router.post('/', response_model=TaskResponse, status_code=201)
async def create_task(
    *,
    session: Session = ActiveSession,
    user: User = AuthenticatedUser,
    task: TaskRequest,
):
    '''Create new task'''
    task.user_id = user.id
    
    db_task = Task.from_orm(task)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task
