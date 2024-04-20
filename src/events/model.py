from pydantic import BaseModel, ConfigDict

from src.common_models import CommonModel

class BaseEvent(BaseModel):
    """
    Represent a Event:
    
    Attribute:
        name: event name
        ticket: number of limit ticket to sale
    """
    name: str
    tickets: int
    

class CreatedEvent(BaseEvent, CommonModel):
    model_config = ConfigDict(from_attributes=True)
