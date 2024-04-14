"""
FastAPI main file to run project
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database.postgres import PostgresConnection, engine


context = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    context["sql_connection_1"] = PostgresConnection(engine=engine) 
    yield
    context["sql_connection_1"].connection.close()
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}