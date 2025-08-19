from sqlalchemy.orm import DeclarativeBase
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
class Base(DeclarativeBase):
    pass


class Workouts(Base):
    __tablename__ = 'workouts'
    id:Mapped[int] =  mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    plan_name:Mapped[str] = mapped_column(String(50))
    date:Mapped[str] = mapped_column(String(50))
    exercises:Mapped[str] = mapped_column(String(50))
    duration:Mapped[str] = mapped_column(String(50))
    
class Nutritions(Base):
    __tablename__ = 'nutritions'
    id:Mapped[int] =  mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    date:Mapped[str] = mapped_column(String(50))
    meals:Mapped[str] = mapped_column(String(50))
    calories:Mapped[str] = mapped_column(String(50))
    macros:Mapped[str] = mapped_column(String(50))

class Progress(Base):
    __tablename__ = 'progress'
    id:Mapped[int] =  mapped_column(primary_key=True)
    user_id:Mapped[int] =  mapped_column(ForeignKey('users.id'))
    workout_id:Mapped[int] = mapped_column(ForeignKey('workouts.id'))
    sets:Mapped[str] = mapped_column(String(50))
    reps:Mapped[str] = mapped_column(String(50))
    weights:Mapped[str] = mapped_column(String(50))
    notes:Mapped[str] = mapped_column(String(50))
