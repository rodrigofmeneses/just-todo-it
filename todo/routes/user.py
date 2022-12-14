from typing import List

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from psycopg2.errors import UniqueViolation
from sqlmodel import Session, select

from todo.db import ActiveSession
from todo.models.user import User, UserRequest, UserResponse

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
async def list_users(*, session: Session = ActiveSession):
    """List all users."""

    """
    * : detalhe legal da doc, isso é apenas para o editor não reclamar com os
        parâmetros obrigatórios.
    Devido a injeção de dependência session: Session = ActiveSession, 
    não é necessário a utilização do bloco with. É apenas uma mudança estética.
    
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        
    """
    users = session.exec(select(User)).all()
    return users


@router.get("/{username}/", response_model=UserResponse)
async def get_user_by_username(
    *, session: Session = ActiveSession, username: str
):
    """Get user by username"""
    query = select(User).where(User.username == username)
    user = session.exec(query).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(*, session: Session = ActiveSession, user: UserRequest):
    """Creates new user"""
    db_user = User.from_orm(user)  # transform UserRequest in User
    try:
        session.add(db_user)
        session.commit()
    except UniqueViolation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    return db_user
