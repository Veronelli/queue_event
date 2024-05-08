"""
Declation of all models related to Ticket
"""

from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from src.common_models import CommonModel
from src.events.model import CreatedEvent


class BaseTicket(BaseModel):
    """
    Class represent a ticket
    
    Attributes:
        name: name of buyer
        lastname: of buyer
        email: of buyer
        eventId: id of event that will be appointemnt
    """
    name: str
    lastname: str
    email: str
    event_id: Optional[UUID] = Field(serialization_alias="eventId")

class TicketCreated(BaseTicket, CommonModel):
    """
    Class that represent a ticket created
    
    Attributes:
        ticket_number: is a number to identificate the number of ticket
    """
    ticket_number: int

class NestedTicket(CommonModel):
    """
    Class represent a ticket, with event related
    
    Attributes:
        name: name of buyer
        lastname: of buyer
        email: of buyer
        eventId: id of event that will be appointemnt
    """
    name: str
    lastname: str
    email: str
    event: CreatedEvent
    ticket_number:int = Field(alias="ticketNumber")
