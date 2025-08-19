from fastapi import APIRouter
from sqlmodel import select
from ..database import SessionDep
from ..models.schemas import Nutritions 

router = APIRouter()

@router.post('/nutritions', tags=['nutritions'], response_model=Nutritions)
async def add_nutrition(nutrition: Nutritions, session: SessionDep) -> Nutritions:
    session.add(nutrition)
    session.commit()
    session.refresh(nutrition)
    return nutrition

@router.get('/nutritions', tags=['nutritions'], response_model=list[Nutritions])
async def get_nutritions(session: SessionDep) -> list[Nutritions]:
    statement = select(Nutritions)
    nutritions = session.exec(statement).all() 
    return nutritions

@router.get("/nutritions/{nutrition_id}", tags=['nutritions'], response_model=Nutritions)
def get_nutrition(nutrition_id: int, session: SessionDep):
    nutrition = session.get(Nutritions, nutrition_id)
    if not nutrition:
        return None
    return nutrition

@router.put("/nutritions/{nutrition_id}", tags=['nutritions'], response_model=Nutritions)
def update_nutrition(nutrition_id: int, updated_nutrition: Nutritions, session: SessionDep):
    nutrition = session.get(Nutritions, nutrition_id)
    if not nutrition:
        return None
    
    nutrition_data = updated_nutrition.model_dump(exclude_unset=True)
    for key, value in nutrition_data.items():
        setattr(nutrition, key, value)
    
    session.add(nutrition)
    session.commit()
    session.refresh(nutrition)
    return nutrition

@router.delete("/nutritions/{nutrition_id}", tags=['nutritions'])
def delete_nutrition(nutrition_id: int, session: SessionDep):
    nutrition = session.get(Nutritions, nutrition_id)
    if not nutrition:
        return None
    session.delete(nutrition)
    session.commit()
    return {"message": "Nutrition log deleted successfully"}