"""
Event test declaration
"""

import asyncio
from httpx import AsyncClient
import pytest
from fastapi import status
from src.events.model import BaseEvent
from src.events.repository import delete, save
from src.events.model import CreatedEvent


@pytest.mark.asyncio
async def test_get_all_event(client: AsyncClient) -> None:
    """
    Create some events, after that make a request to the endpoint,
    and then  remove all created users.
    We will compare of the data created is the same with Event obtained from
    the service.
    """
    event_list = [
        BaseEvent(name="Event 1", tickets=150),
        BaseEvent(name="Event 2", tickets=200),
        BaseEvent(name="Event 3", tickets=250),
    ]
    event_created: list[CreatedEvent] = await asyncio.gather(
        *(save(event) for event in event_list)
    )
    response = await client.get("/events/")
    
    assert status.HTTP_200_OK == response.status_code
    assert [CreatedEvent(**result.__dict__).model_dump(mode="json") for result in event_created] == response.json() 
    await asyncio.gather(*[delete(event.id) for event in event_created])


@pytest.mark.asyncio
async def test_create_event(client: AsyncClient) -> None:
    """
    Test if the event is created in postgres DB without any error
    and compare with expected event created.
    """
    event_payload = {
        "name": "Event for test",
        "tickets": 128,
    }
    response = await client.post(url="/events/", json=event_payload)
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
        "tickets": 128,
    }

    event_created = await save(BaseEvent(**event_payload))
    response = await client.delete(f"/events/{event_created.id}")
    assert status.HTTP_204_NO_CONTENT == response.status_code


@pytest.mark.asyncio
async def test_delete_event_not_found(client: AsyncClient) -> None:
    """
    Test if the event exist and is deleted
    """
    event_id = 23

    response = await client.delete(f"/events/{event_id}")
    assert status.HTTP_404_NOT_FOUND == response.status_code
