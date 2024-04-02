from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

class Attendees(Base):
    __tablename__ = "attendees"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"))
    created_at = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"<Attendees(id={self.id}, name={self.name}, email={self.email}, event_id={self.event_id}, created_at={self.created_at})>"