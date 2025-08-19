from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    password: str
    age: int | None = None
    weight: int | None = None
    height: int | None = None
    goals: str | None = None

class Workouts(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    plan_name: str
    date: str
    exercises: str
    duration: str
    difficulty: str | None = None 
    target_muscle_groups: str | None = None

class Progress(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id") 
    workout_id: int | None = Field(default=None, foreign_key="workouts.id")
    date: str
    sets: str
    reps: str
    weights: str
    duration: str | None = None 
    notes: str | None = None

class Nutritions(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id") 
    date: str
    meals: str
    calories: str
    macros: str

class Exercises(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    category: str
    equipment: str | None = None
    difficulty: str
    instructions: str
    target_muscles: str