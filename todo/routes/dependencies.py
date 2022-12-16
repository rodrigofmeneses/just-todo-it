from fastapi import Depends, HTTPException, status

from todo.auth import AuthenticatedUser
from todo.db import ActiveSession, Session
from todo.models import Task, User


async def get_task(task_id: int, session: Session = ActiveSession) -> Task:
    """Get a task by id"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


async def valid_task_id(
    user: User = AuthenticatedUser, task: Task = Depends(get_task)
) -> Task:
    """Checks if the task belongs to the user"""
    if task.user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No Permission to access another user task",
        )
    return task


ValidTaskId = Depends(valid_task_id)
