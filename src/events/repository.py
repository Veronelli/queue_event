"""
Repository for Event endpoint oprations
"""

from asyncio import Event

from src.events.model import CreatedEvent


async def save(event: Event)->CreatedEvent:
    