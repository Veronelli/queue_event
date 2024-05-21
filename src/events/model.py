from pydantic import BaseModel, ConfigDict, Field
from src.common_models import CommonModel

class BaseEvent(BaseModel):
    """
    Represent a Event:
    
    Attribute:
        name: event name
        ticket: number of limit ticket to sale
    """
    name: str
    tickets_availables: int = Field(serialization_alias="ticketsAvailables", alias_priority="ticketsAvailables")
    

class CreatedEvent(BaseEvent, CommonModel):
    model_config = ConfigDict(from_attributes=True)
