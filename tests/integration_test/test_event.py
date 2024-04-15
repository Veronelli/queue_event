"""
Event test declaration
"""

from httpx import AsyncClient
import pytest

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
    