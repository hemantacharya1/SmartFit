from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from ..models.schemas import Exercises

router = APIRouter()

@router.post('/exercises', tags=['exercises'], response_model=Exercises)
async def add_exercise(exercise: Exercises, session: SessionDep) -> Exercises:
    session.add(exercise)
    session.commit()
    session.refresh(exercise)
    return exercise

@router.get('/exercises', tags=['exercises'], response_model=list[Exercises])
async def get_exercises(session: SessionDep) -> list[Exercises]:
    statement = select(Exercises)
    exercises = session.exec(statement).all()
    return exercises

@router.get("/exercises/{exercise_id}", tags=['exercises'], response_model=Exercises)
def get_exercise(exercise_id: int, session: SessionDep):
    exercise = session.get(Exercises, exercise_id)
    if not exercise:
        return None
    return exercise

@router.put("/exercises/{exercise_id}", tags=['exercises'], response_model=Exercises)
def update_exercise(exercise_id: int, updated_exercise: Exercises, session: SessionDep):
    exercise = session.get(Exercises, exercise_id)
    if not exercise:
        return None
    
    exercise_data = updated_exercise.model_dump(exclude_unset=True)
    for key, value in exercise_data.items():
        setattr(exercise, key, value)
    
    session.add(exercise)
    session.commit()
    session.refresh(exercise)
    return exercise

@router.delete("/exercises/{exercise_id}", tags=['exercises'])
def delete_exercise(exercise_id: int, session: SessionDep):
    exercise = session.get(Exercises, exercise_id)
    if not exercise:
        return None
    session.delete(exercise)
    session.commit()
    return {"message": "Exercise deleted successfully"}