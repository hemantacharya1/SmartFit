from fastapi import APIRouter
from sqlmodel import select
from ..database import SessionDep
from ..models.schemas import Progress

router = APIRouter()

@router.post('/progress', tags=['progress'], response_model=Progress)
async def add_progress(progress: Progress, session: SessionDep) -> Progress:
    session.add(progress)
    session.commit()
    session.refresh(progress)
    return progress

@router.get('/progress', tags=['progress'], response_model=list[Progress]) 
async def get_all_progress(session: SessionDep) -> list[Progress]:
    statement = select(Progress)
    progress_list = session.exec(statement).all() 
    return progress_list

@router.get("/progress/{progress_id}", tags=['progress'], response_model=Progress)
def get_progress(progress_id: int, session: SessionDep):
    progress = session.get(Progress, progress_id)
    if not progress:
       return None
    return progress

@router.put("/progress/{progress_id}", tags=['progress'], response_model=Progress)
def update_progress(progress_id: int, updated_progress: Progress, session: SessionDep):
    progress = session.get(Progress, progress_id)
    if not progress:
        return None
    
    progress_data = updated_progress.model_dump(exclude_unset=True)
    for key, value in progress_data.items():
        setattr(progress, key, value)
    
    session.add(progress)
    session.commit()
    session.refresh(progress)
    return progress

@router.delete("/progress/{progress_id}", tags=['progress'])
def delete_progress(progress_id: int, session: SessionDep):
    progress = session.get(Progress, progress_id)
    if not progress:
       return None
    session.delete(progress)
    session.commit()
    return {"message": "Progress log deleted successfully"}