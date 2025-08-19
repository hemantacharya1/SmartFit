from fastapi import Depends,HTTPException,Query,APIRouter
from sqlmodel import Field, SQLModel, select
from database import SessionDep

router = APIRouter()

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: int | None = Field(default=None, index=True)
    password: str
    age: int
    weight:int
    height:int
    goals:str

@router.post('/users',tags=['users'])
async def add_users(user:Users, session:SessionDep) -> Users:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get('/users',tags=['users'])
async def get_users(session:SessionDep) -> list[Users]:
    res=session.exec(select(Users).offset(0).limit(100).all())
    return res



