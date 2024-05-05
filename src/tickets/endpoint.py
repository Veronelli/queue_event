from typing import Annotated
from fastapi import APIRouter, Body, status
from src.tickets.repository import save
from src.tickets.model import BaseTicket, TicketCreated

router = APIRouter(prefix="/tickets")

@router.post("/", response_model=TicketCreated, status_code=status.HTTP_201_CREATED)
async def create(ticket: Annotated[BaseTicket, Body()]) -> TicketCreated:
    ticket_saved = save(ticket)
    return ticket_saved