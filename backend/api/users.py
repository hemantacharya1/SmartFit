from typing import Annotated
from fastapi import Depends,HTTPException,Query,APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select

router = APIRouter()

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: int | None = Field(default=None, index=True)
    password: str
    age: int
    weight:int
    height:int
    goals:str

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@router.post('/users',tags=['users'])
async def add_users(user:Users, session:SessionDep) -> Users:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get('/users',tags=['users'])
async def add_users(session:SessionDep) -> list[Users]:
    res=session.exec(select(Users).offset(0).limit(100).all())
    return res



