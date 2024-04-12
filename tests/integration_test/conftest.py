import pytest
from sqlalchemy import Connection, Engine

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
    from src.database.postgres import PostgresConnection
    
    return PostgresConnection(engine).connection