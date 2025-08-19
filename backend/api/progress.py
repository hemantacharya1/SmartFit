from fastapi import Depends,HTTPException,Query,APIRouter
from sqlmodel import Field, SQLModel, select
from database import SessionDep
router = APIRouter()

class Progress(Base):
    id: int | None = Field(default=None, primary_key=True)
    user_id:int | None = Field(default=None, forgien_key = True)
    workout_id:int | None = Field(default=None, forgien_key = True)
    sets:str
    reps:str
    weights:str
    notes:str


@router.post('/progress',tags=['progress'])
async def add_progress(progress:Progress,session:SessionDep) -> Progress:
    session.add(progress)
    session.commit()
    session.refresh(progress)
    return progress


@router.get('/progress',tags=['workout'])
async def get_progress(session:SessionDep) -> list[Progress]:
    res=session.exec(select(Progress).offset(0).limit(100).all())
    return res



