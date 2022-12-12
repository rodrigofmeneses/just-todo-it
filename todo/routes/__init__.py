from fastapi import APIRouter

from .auth import router as auth_router
from .task import router as task_router
from .user import router as user_router

main_router = APIRouter()

main_router.include_router(auth_router, prefix="/api", tags=["auth"])
main_router.include_router(task_router, prefix="/api/task", tags=["task"])
main_router.include_router(user_router, prefix="/api/user", tags=["user"])