"""
Repository for Event endpoint oprations
"""

from pydantic import NonNegativeInt
from src.events.model import BaseEvent, CreatedEvent
from src.events.schema import Event
from src.contexts.main import global_context

async def save(event: BaseEvent)->CreatedEvent:
    """
    Save new event
    
    Returns:
        event created
    """
    
    event_schema = Event(**event.model_dump())
    global_context['sql_session'].add(event_schema)
    global_context["sql_session"].commit()
    global_context["sql_session"].refresh(event_schema)
    return event_schema

async def delete(id: NonNegativeInt)->int:
    """
    Delete an event
    
    Returns:
        id of event deleted
    """
    first_event = global_context['sql_session'].query(Event).filter(Event.id == id).first()
    global_context['sql_session'].delete(first_event)
    global_context['sql_session'].commit()
    return id
