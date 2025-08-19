from fastapi import Depends,HTTPException,Query,APIRouter
from sqlmodel import Field, SQLModel, select
from database import SessionDep
router = APIRouter()

class Workouts(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id:int | None = Field(default=None, forgien_key = True)
    plan_name:str
    date:str
    exercises:str
    duration:str


@router.post('/workout',tags=['workout'])
async def add_workout(workout:Workouts,session:SessionDep) -> Workouts:
    session.add(workout)
    session.commit()
    session.refresh(workout)
    return workout


@router.get('/workout',tags=['workout'])
async def get_workout(session:SessionDep) -> list[Workouts]:
    res=session.exec(select(Workouts).offset(0).limit(100).all())
    return res



