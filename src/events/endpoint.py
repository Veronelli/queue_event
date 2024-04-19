"""
Declaration of Event routes
"""

from typing import Annotated
from fastapi import APIRouter, status, Query, Response
from pydantic import NonNegativeInt

from src.events.model import BaseEvent, CreatedEvent
from src.events.repository import delete, save

router = APIRouter(prefix="/events")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(event: BaseEvent)->CreatedEvent:
    return await save(event)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remove(id:Annotated[NonNegativeInt, Query])->None:
    event_deleted = await delete(id)
    if event_deleted:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return Response(status_code=status.HTTP_404_NOT_FOUND)