"""
FastAPI main file to run project
"""

from contextlib import asynccontextmanager
from typing import TypedDict
from fastapi import FastAPI
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from src.database.postgres import SQLSession, engine

class APIContext(TypedDict):
    engine: Engine
    sql_session: Session

context:APIContext = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    context["engine"] = engine
    sql_session = SQLSession(engine)
    context["engine"].connect()
    context["sql_session"] = sql_session
    yield
    context["engine"].close()
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}