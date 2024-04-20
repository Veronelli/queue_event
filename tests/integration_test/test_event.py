"""
Event test declaration
"""

from httpx import AsyncClient
import pytest
from fastapi import status
from src.events.model import BaseEvent
from src.events.repository import delete, save

@pytest.mark.asyncio
async def test_create_event(client:AsyncClient)->None:
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
async def test_delete_event(client: AsyncClient)->None:
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
async def test_delete_event_not_found(client: AsyncClient)->None:
    """
    Test if the event exist and is deleted    
    """
    event_id = 23
    
    response = await client.delete(f"/events/{event_id}")
    assert status.HTTP_404_NOT_FOUND == response.status_code