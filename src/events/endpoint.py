"""
Declaration of Event routes
"""

from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, status, Path, Response
from pydantic import NonNegativeInt
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.events.model import BaseEvent, CreatedEvent
from src.events.repository import delete, get_events, save

router = APIRouter(prefix="/events")

@router.get("/", status_code=status.HTTP_200_OK)
async def list()->list[CreatedEvent]:
    return get_events()

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get(id:Annotated[UUID, Path])->CreatedEvent:
    return  get_events(id=id)[0]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreatedEvent)
async def create(event: BaseEvent)->CreatedEvent:
    return await save(event)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove(id:Annotated[UUID, Path()])->Response:
    try:
        await delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except UnmappedInstanceError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    