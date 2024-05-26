from typing import List
from uuid import UUID, uuid4
from pydantic import ConfigDict, field_validator, validate_email
from sqlalchemy import Engine, MetaData, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlmodel import Relationship, SQLModel, create_engine, Field

engine: Engine = create_engine(
    url=f"postgresql+psycopg2://root:root@postgres_queue_events/queue_events"
    )

class Event(SQLModel, table=True):
    __tablename__= "events"
    
    id: UUID = Field(default_factory=uuid4, unique=True, primary_key=True)
    name:str
    tickets_availables:int
    tickets: List["Ticket"] = Relationship(back_populates="tickets")

    model_config = ConfigDict(arbitrary_types_allowed=True)
    
class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=20)
    lastname: str = Field(max_length=20)
    email:str = Field(max_length=25)
    ticket_number:int
    event_id: UUID | None = Field(
        default=None,
        foreign_key="events.id"
        )
    event: Event = Relationship(back_populates="events")
    # email_validator = field_validator("email", mode="before")(validate_email)
    model_config = ConfigDict(arbitrary_types_allowed=True)


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

SQLModel.metadata.create_all(engine)

print_all_tables(engine)
print("Finish!!")