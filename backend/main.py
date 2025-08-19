from fastapi import FastAPI
from .api import users, progress, nutrition, workout, exercises, chat 
from .database import create_db_and_tables
from . import models 

app = FastAPI(
    title="SmartFit API",
    description="Smartfit backend"
)

app.include_router(users.router)
app.include_router(progress.router)
app.include_router(nutrition.router)
app.include_router(workout.router)
app.include_router(exercises.router) 
app.include_router(chat.router) 

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get('/')
def hello():
    return {'Response': "Hello Smartfit"}