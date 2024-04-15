from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Engine, ForeignKey, Integer, MetaData, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database


engine: Engine = create_engine(
    url=f"postgresql+psycopg2://root:root@postgres_queue_events/queue_events", )


Base = declarative_base()

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(30))
    tickets = Column(Integer)
     

class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(25), unique=True)
    ticket_number = Column(Integer, autoincrement=True)
    
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', back_populates='tickets')
    
def print_all_tables(engine):
    # To load metdata and existing database schema
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    tables = metadata.tables.keys()
    
    print("List of tables:")
    for table in tables:
        print(table)

if not database_exists(engine.url):
    print("Creating Database")
    create_database(engine.url)
    print("Creating Tables")
Base.metadata.create_all(engine)

print_all_tables(engine)
print("Finish!!")