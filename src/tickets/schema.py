"""
Schema for ticket
"""

from sqlalchemy import Column, Integer, String
from src.common_models import Base


class Ticket(Base):
    __tablename__ = "tickets"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    lastname = Column(String(20))
    email = Column(String(25), unique=True)
    ticket_number = Column()