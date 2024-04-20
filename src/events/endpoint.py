"""
Declaration of Event routes
"""

from typing import Annotated
from fastapi import APIRouter, status, Path, Response
from pydantic import NonNegativeInt
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.events.model import BaseEvent, CreatedEvent
from src.events.repository import delete, save

router = APIRouter(prefix="/events")



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(event: BaseEvent)->CreatedEvent:
    return await save(event)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove(id:Annotated[NonNegativeInt, Path()])->Response:
    try:
        await delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except UnmappedInstanceError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    