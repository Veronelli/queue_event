"""
Event test declaration
"""

import asyncio
import uuid
from httpx import AsyncClient
import pytest
from fastapi import status
from src.events.model import BaseEvent
from src.events.repository import delete, save
from src.events.model import CreatedEvent
from src.tickets.model import BaseTicket
from src.tickets.repository import save as save_ticket, delete as delete_ticket


@pytest.mark.asyncio
async def test_get_all_event(client: AsyncClient) -> None:
    """
    Create some events, after that make a request to the endpoint,
    and then  remove all created users.
    We will compare of the data created is the same with Event obtained from
    the service.
    """
    try:
        event_list = [
            BaseEvent(name="Event 1", tickets_availables=150),
            BaseEvent(name="Event 2", tickets_availables=200),
            BaseEvent(name="Event 3", tickets_availables=250),
        ]

        event_created0 = await asyncio.gather(
            save(event_list[0]),
            save(event_list[1]),
            save(event_list[2])
        )
        ticket = BaseTicket(
            name= "John",
            lastname= "Broew",
            email= "jbroew@veronelli.com",
            event_id=str(event_created0.id),
        )
        ticket_created = await save_ticket(ticket)
        event_created0.id = ticket_created.id
        response = await client.get("/events/")
    finally:
        breakpoint()
        assert status.HTTP_200_OK == response.status_code
        assert [CreatedEvent(**result.__dict__).model_dump(mode="json", by_alias=True) for result in event_created] == response.json() 
        
        await asyncio.gather(
            delete(event_created0.id),
            delete(event_created1.id),
            delete(event_created2.id)
        )
        await delete_ticket(ticket_created.id)


@pytest.mark.asyncio
async def test_create_event(client: AsyncClient) -> None:
    """
    Test if the event is created in postgres DB without any error
    and compare with expected event created.
    """
    try:
        event_payload = {
            "name": "Event for test",
            "tickets_availables": 128,
        }
        response = await client.post(url="/events/", json=event_payload)

    finally:
        content = response.json()
        assert response.status_code == status.HTTP_201_CREATED
        await delete(content["id"])


@pytest.mark.asyncio
async def test_delete_event(client: AsyncClient) -> None:
    """
    Test if the event exist and is deleted
    """
    event_payload = {
        "name": "Event for test",
        "tickets_availables": 128,
    }

    event_created = await save(BaseEvent(**event_payload))
    response = await client.delete(f"/events/{event_created.id}")
    assert status.HTTP_204_NO_CONTENT == response.status_code


@pytest.mark.asyncio
async def test_delete_event_not_found(client: AsyncClient) -> None:
    """
    Test if the event exist and is deleted
    """
    event_id = str(uuid.uuid4())
    response = await client.delete(f"/events/{event_id}")
    assert status.HTTP_404_NOT_FOUND == response.status_code

@pytest.mark.asyncio
async def test_get_event(client: AsyncClient) -> None:
    """
    get event created and find by id into obtained in endpoint
    """
    event_list = [
        BaseEvent(name="Event 1", tickets_availables=150),
        BaseEvent(name="Event 2", tickets_availables=200),
        BaseEvent(name="Event 3", tickets_availables=250),
    ]
    event_created: list[CreatedEvent] = await asyncio.gather(
        *(save(event) for event in event_list)
    )
    response = await client.get(f"/events/{str(event_created[1].id)}")
    
    assert status.HTTP_200_OK == response.status_code
    assert CreatedEvent(
                **event_created[1].__dict__
            ).model_dump(mode="json", by_alias=True) == response.json()
    await asyncio.gather(*[delete(event.id) for event in event_created])
