from sqlalchemy import Engine, create_engine, Connection
from src.common_models import SingletonMeta

db_user = "root"
db_password = "root"
db_name = "queue_events"

class PostgresConnection(metaclass=SingletonMeta):
    """
    Connection class using SQLAlchemy
    """
    connection: Connection

    def __init__(self, engine: Engine):
        self.connection = engine.connect()
    
engine: Engine = create_engine(
    url=f"postgresql+psycopg2://root:root@postgres_queue_events/queue_events", )

