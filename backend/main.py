from typing import Union
from fastapi import FastAPI
from .api import users
app=FastAPI()
app.include_router(users.router)

@app.on_event("startup")
def on_startup():
    users.create_db_and_tables()

@app.get('/')
def hello():
    return {'Response':"Hello world"}