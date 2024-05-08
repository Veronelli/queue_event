from random import randint
from uuid import UUID
from src.tickets.model import BaseTicket, TicketCreated
from src.contexts.main import global_context
from src.tickets.schema import Ticket
from pydantic import NonNegativeInt

async def save(ticket:BaseTicket)->TicketCreated:
    """
    Save ticket and set event relationship
    
    Args:
        ticket: ticket to save
        
    Returns
        A created ticket
    """
    random_number = randint(0,1000)
    ticket_schema = Ticket(**ticket.model_dump(), ticket_number=random_number)
    global_context["sql_session"].add(ticket_schema)
    global_context["sql_session"].commit()
    global_context["sql_session"].refresh(ticket_schema)
    return ticket_schema

async def delete(id: UUID)->int:
    """
    Remove an ticket, if it does not exist throws an error
    
    Args:
        id: of ticket event
        
    Returns:
        int of id ticket event
    """
    first_ticket = (
        global_context["sql_session"].query(Ticket).filter(Ticket.id == id).first()
    )
    global_context["sql_session"].delete(first_ticket)
    global_context["sql_session"].commit()
    return id
