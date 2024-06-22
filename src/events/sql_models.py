from typing import TYPE_CHECKING, Optional
from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from uuid import uuid4, UUID

if TYPE_CHECKING:
    from src import Ticket

class Event(SQLModel, table=True):
    __tablename__= "events"
    
    id: UUID = Field(default_factory=uuid4, unique=True, primary_key=True)
    name:str
    tickets_availables:int
    tickets: Optional[list['Ticket']] = Relationship(back_populates="event",)
    model_config = ConfigDict(arbitrary_types_allowed=True)
