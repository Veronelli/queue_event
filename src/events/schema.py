from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.common_models import Base

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(30))
    tickets = Column(Integer)
    