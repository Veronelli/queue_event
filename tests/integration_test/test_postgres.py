from sqlalchemy import Connection, Engine
from sqlalchemy_utils import database_exists
from src.tickets.sql_model import Ticket
from src.events.sql_models import Event

def test_created_database_is_success(
    engine:Engine)->None:
    """
    Verify if the database is created
    """
    is_created = database_exists(engine.url)
    assert is_created == True


def test_created_tables_is_success(
    engine:Engine,
    db_connection: Connection)->None:
    """
    Verify if the table is created
    """
    connection = db_connection
    
    tickets_table_is_created = engine.dialect.has_table(connection, Ticket.__tablename__)
    events_table_is_created = engine.dialect.has_table(connection, Event.__tablename__)
    
    assert tickets_table_is_created == True
    assert events_table_is_created == True
    
    connection.close()
    
    