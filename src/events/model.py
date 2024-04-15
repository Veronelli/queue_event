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
    
    model_config = ConfigDict(orm_mode=True)

class CreatedEvent(BaseEvent, CommonModel):
    ...