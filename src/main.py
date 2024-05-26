"""
FastAPI main file to run project
"""

from contextlib import asynccontextmanager
from typing import TypedDict
from fastapi import FastAPI
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from src.database.postgres import SQLSession, engine
from src.events.endpoint import router as event_router
from src.tickets.endpoint import router as ticket_router
from src.contexts.main import global_context

@asynccontextmanager
async def lifespan(app: FastAPI):
    global_context["engine"] = engine
    sql_session = SQLSession(engine)
    global_context["engine"].connect()
    global_context["sql_session"] = sql_session
    yield
    global_context["engine"].close()
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(event_router, tags=["Events"])
app.include_router(ticket_router, tags=["Tickets"])