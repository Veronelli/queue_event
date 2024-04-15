"""
Repository for Event endpoint oprations
"""

from src.events.model import BaseEvent, CreatedEvent
from src.events.schema import Event
from src.contexts.main import global_context

async def save(event: BaseEvent)->CreatedEvent:
    breakpoint()
    event_schema = Event(**event.model_dump())
    global_context['sql_session'].add(event_schema)
    global_context["sql_session"].commit()
    global_context["sql_session"].refresh(event_schema)
    return event_schema