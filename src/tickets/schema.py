"""
Schema for ticket
"""

import uuid
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.common_models import Base


class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(UUID(as_uuid=True), primary_key=True, autoincrement=True,default=uuid.uuid4)
    name = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(25), )
    ticket_number = Column(Integer, autoincrement=True)    
    event_id = Column(Integer, ForeignKey('events.id'), nullable=True, unique=True)
    event = relationship('Event', )
