from typing import TypedDict

from pytest import Session
from sqlalchemy import Engine
from src.database.postgres import SQLSession, engine

class APIContext(TypedDict):
    engine: Engine
    sql_session: Session

global_context: APIContext = {
    "engine": engine,
    "sql_session": SQLSession(engine).session()
}