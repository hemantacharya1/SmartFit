from typing import Union
from fastapi import FastAPI
from .api import users,progress,nutrition,workout
app=FastAPI()
app.include_router(users.router)
app.include_router(progress.router)
app.include_router(nutrition.router)
app.include_router(workout.router)


@app.on_event("startup")
def on_startup():
    users.create_db_and_tables()

@app.get('/')
def hello():
    return {'Response':"Hello Smartfit"}