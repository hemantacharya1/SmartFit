from fastapi import Depends,HTTPException,Query,APIRouter
from sqlmodel import Field, SQLModel, select
from database import SessionDep
router = APIRouter()

class Nutritions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id:int | None = Field(default=None, forgien_key = True)
    date:str
    meals:str
    calories:str
    macros:str


@router.post('/nutritions',tags=['nutritions'])
async def add_nutritions(nutrition:Nutritions,session:SessionDep) -> Nutritions:
    session.add(nutrition)
    session.commit()
    session.refresh(nutrition)
    return nutrition


@router.get('/nutritions',tags=['nutritions'])
async def get_nutritions(session:SessionDep) -> list[Nutritions]:
    res=session.exec(select(Nutritions).offset(0).limit(100).all())
    return res



