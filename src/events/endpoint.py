"""
Declaration of Event routes
"""

from typing import Annotated
from fastapi import APIRouter

from src.events.model import BaseEvent, CreatedEvent

router = APIRouter(prefix="/event")

@router.post()
async def create(event: BaseEvent)->CreatedEvent:
    ...