import uuid
from sqlalchemy import UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.common_models import Base

class BaseEventSchema(Base):
    __tablename__ = "events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(30))
    tickets_availables = Column(Integer)

class Event(BaseEventSchema):
    tickets = relationship(
        "Ticket", back_populates="event"
    )