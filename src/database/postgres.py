from sqlalchemy import Engine, create_engine, Connection
from sqlalchemy.orm import Session, sessionmaker
from src.common_models import SingletonMeta

db_user = "root"
db_password = "root"
db_name = "queue_events"

class SQLSession(metaclass=SingletonMeta):
    """
    Session class using SQLAlchemy
    """
    session: Session

    def __init__(self, engine: Engine):
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
engine: Engine = create_engine(
    url=f"postgresql+psycopg2://root:root@postgres_queue_events/queue_events", )
