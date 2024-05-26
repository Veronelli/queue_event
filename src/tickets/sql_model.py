from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship,SQLModel
from pydantic import field_validator, validate_email
from uuid import uuid4, UUID

if TYPE_CHECKING:
    from src import Event

class Ticket(SQLModel, table=True):
    __tablename__ = "tickets"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=20)
    lastname: str = Field(max_length=20)
    email: str = Field(max_length=25)
    ticket_number:int
    event_id: UUID | None = Field(
        default=None,
        foreign_key="events.id"
        )
    event: "Event" = Relationship(back_populates="event ")

    email_validator = field_validator("email", mode="before")(validate_email)