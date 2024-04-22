"""
Schema for ticket
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.common_models import Base


class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(25), unique=True)
    ticket_number = Column(Integer, autoincrement=True)    
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship('Event', )
