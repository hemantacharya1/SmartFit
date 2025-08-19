from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from ..models.schemas import Users 

router = APIRouter()

@router.post('/users', tags=['users'], response_model=Users)
async def add_user(user: Users, session: SessionDep) -> Users:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get('/users', tags=['users'], response_model=list[Users])
async def get_users(session: SessionDep) -> list[Users]:
    statement = select(Users)
    users = session.exec(statement).all() 
    return users

@router.get("/users/{user_id}", tags=['users'], response_model=Users)
def get_user(user_id: int, session: SessionDep):
    user = session.get(Users, user_id)
    if not user:
       return None
    return user

@router.put("/users/{user_id}", tags=['users'], response_model=Users)
def update_user(user_id: int, updated_user: Users, session: SessionDep):
    user = session.get(Users, user_id)
    if not user:
       return None
    
    user_data = updated_user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete("/users/{user_id}", tags=['users'])
def delete_user(user_id: int, session: SessionDep):
    user = session.get(Users, user_id)
    if not user:
        return None
    session.delete(user)
    session.commit()
    return {"message": "User deleted successfully"}