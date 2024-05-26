from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Body, Path, Response, status
from src.tickets.repository import delete, get_tickets, save
from src.tickets.model import BaseTicket, TicketCreated
from sqlalchemy.orm.exc import UnmappedInstanceError

router = APIRouter(prefix="/tickets")

@router.get("/", response_model=list[TicketCreated], status_code=status.HTTP_200_OK)
async def list()->list[TicketCreated]:
    ticket_list = await get_tickets()
    return ticket_list
    
@router.post("/", response_model=TicketCreated, status_code=status.HTTP_201_CREATED)
async def create(ticket: Annotated[BaseTicket, Body()]) -> TicketCreated:
    ticket_saved = await save(ticket)
    return ticket_saved

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove(id: Annotated[UUID, Path()])->Response:
    try:
        await delete(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except UnmappedInstanceError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    