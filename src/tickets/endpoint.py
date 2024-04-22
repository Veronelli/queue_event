from fastapi import APIRouter,Path, status
from src.events.repository import save
from src.tickets.model import BaseTicket, TicketCreated

router = APIRouter("/tickets")

@router.post("/", response_model=TicketCreated, status_code=status.HTTP_201_CREATED)
async def create(ticket: BaseTicket) -> TicketCreated:
    return save(ticket)