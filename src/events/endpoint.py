"""
Declaration of Event routes
"""

from fastapi import APIRouter

from src.events.model import BaseEvent, CreatedEvent
from src.events.repository import save

router = APIRouter(prefix="/events")

@router.post("/")
async def create(event: BaseEvent)->CreatedEvent:
    return await save(event)