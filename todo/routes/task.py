from typing import List

from fastapi import APIRouter, status
from sqlmodel import Session, select

from todo.auth import AuthenticatedUser
from todo.db import ActiveSession
from todo.models.task import Task, TaskRequest, TaskResponse, UpdateTaskRequest
from todo.models.user import User
from todo.routes.dependencies import ValidTaskId

router = APIRouter()


@router.get("/", response_model=List[TaskResponse])
async def list_all_tasks(*, session: Session = ActiveSession):
    """List all tasks"""
    tasks = session.exec(select(Task)).all()
    return tasks


@router.get("/me", response_model=List[TaskResponse])
async def list_all_tasks_by_user(
    *, session: Session = ActiveSession, user: User = AuthenticatedUser
):
    """List all tasks of authenticated user"""
    query = select(Task).where(Task.user_id == user.id)
    tasks = session.exec(query).all()
    return tasks


@router.get("/{task_id}", response_model=TaskResponse)
async def task_by_id(
    *,
    task: Task = ValidTaskId,
):
    """Get task by task id"""
    return task


@router.post(
    "/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED
)
async def create_task(
    *,
    session: Session = ActiveSession,
    user: User = AuthenticatedUser,
    task: TaskRequest,
):
    """Create new task"""
    task.user_id = user.id
    db_task = Task.from_orm(task)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(
    *,
    task: Task = ValidTaskId,
    session: Session = ActiveSession,
    task_body: UpdateTaskRequest,
):
    """Update Task"""
    # Remove unset fields of request.
    task_data = task_body.dict(exclude_unset=True)

    for key, value in task_data.items():
        setattr(task, key, value)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.delete("/{task_id}")
async def delete_task(
    *,
    session: Session = ActiveSession,
    task: Task = ValidTaskId,
):
    """Delete Task"""
    session.delete(task)
    session.commit()

    return {"msg": f"Task {task.id} Deleted", "task": task}
