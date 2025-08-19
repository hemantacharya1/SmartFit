from fastapi import APIRouter, HTTPException
from sqlmodel import select
from database import SessionDep
from ..models.schemas import Workouts 

router = APIRouter()

@router.post('/workout', tags=['workout'], response_model=Workouts)
async def add_workout(workout: Workouts, session: SessionDep) -> Workouts:
    session.add(workout)
    session.commit()
    session.refresh(workout)
    return workout

@router.get('/workout', tags=['workout'], response_model=list[Workouts])
async def get_workouts(session: SessionDep) -> list[Workouts]:
    statement = select(Workouts)
    workouts = session.exec(statement).all() 
    return workouts

@router.get("/workout/{workout_id}", tags=['workout'], response_model=Workouts)
def get_workout(workout_id: int, session: SessionDep):
    workout = session.get(Workouts, workout_id)
    if not workout:
        return None
    return workout

@router.put("/workout/{workout_id}", tags=['workout'], response_model=Workouts)
def update_workout(workout_id: int, updated_workout: Workouts, session: SessionDep):
    workout = session.get(Workouts, workout_id)
    if not workout:
        return None
    
    workout_data = updated_workout.model_dump(exclude_unset=True)
    for key, value in workout_data.items():
        setattr(workout, key, value)
    
    session.add(workout)
    session.commit()
    session.refresh(workout)
    return workout

@router.delete("/workout/{workout_id}", tags=['workout'])
def delete_workout(workout_id: int, session: SessionDep):
    workout = session.get(Workouts, workout_id)
    if not workout:
        return None
    session.delete(workout)
    session.commit()
    return {"message": "Workout deleted successfully"}