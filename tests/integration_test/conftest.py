from typing import AsyncGenerator
from fastapi import FastAPI
import pytest
import pytest_asyncio
from sqlalchemy import Connection, Engine
from httpx import AsyncClient, ASGITransport

@pytest.fixture(name="engine")
def import_engine()->Engine:
    """
    Import encapsuled Engine
    """
    from src.database.postgres import engine
    return engine

@pytest.fixture(name="db_connection")
def import_connection(engine: Engine)->Connection:
    """
    Instance Sigleton to return connection
    """
    
    return engine.connect()

@pytest.fixture(name="app")
def application()->FastAPI:
    from src.main import app
    return app

@pytest_asyncio.fixture(name="client")
async def app_client(app: FastAPI)->AsyncGenerator[AsyncClient, None]:
    transport = ASGITransport(app=app, )
    async with AsyncClient(transport=transport, base_url="http://localhost:8000") as client:
        yield client