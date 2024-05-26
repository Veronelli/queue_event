"""
Ticket test declaration
"""

import asyncio
from httpx import AsyncClient
import pytest
from fastapi import status
from src.events.model import BaseEvent, CreatedEvent
from src.events.repository import save as save_event, delete as delete_event
from src.tickets.model import BaseTicket
from src.tickets.repository import delete as delete_ticket, save as save_ticket


@pytest.mark.asyncio
async def test_create_ticket(client: AsyncClient) -> None:
    """
    Create a ticket and store to postgres, then remove event.
    Compare if the data stored is correctly saved
    """
    
    event = BaseEvent(name="Event", tickets_availables=120)
    event_created = await save_event(event)
    ticket = {
        "name": "John",
        "lastname": "Broew",
        "email": "jbroew@veronelli.com",
        "event_id": str(event_created.id),
    }
    # TODO: Create a function to obtain tickets
    try:
        response = await client.post("/tickets/", json=ticket)
    finally:
        assert status.HTTP_201_CREATED == response.status_code
        content = response.json().copy()
        assert isinstance(content["ticket_number"], int)
        assert ticket["event_id"] == content["eventId"]
        
        del content["eventId"]
        del ticket["event_id"]
        del content["ticket_number"]
        del content["id"]
        
        assert ticket == content
        await delete_ticket(response.json()["id"])
        await delete_event(event_created.id)


@pytest.mark.asyncio
async def test_list_tickets(client)->None:
    """
    Create a new ticket and remove from endpoint the created ticket
    """
    event = BaseEvent(name="Event 3", tickets_availables=250)
    event_created = await save_event(event) 
    tickets = [{
        "name": "John",
        "lastname": "Broew",
        "email": "jbroew@veronelli.com",
        "event_id": str(event_created.id),
    },{
        "name": "Fran",
        "lastname": "Smith",
        "email": "fsmith@veronelli.com",
        "event_id": str(event_created.id),
    },{
        "name": "Mark",
        "lastname": "Stone",
        "email": "mstore@veronelli.com",
        "event_id": str(event_created.id),
    }
    ]
    created_tickets = [await save_ticket(BaseTicket(**ticket)) for ticket in tickets]
    try:
        response = await client.get("/tickets/")
        breakpoint()
    finally:
        [
            await delete_ticket(
                created_ticket.id
            ) for created_ticket in created_tickets
        ]
        await delete_event(event_created.id)        

