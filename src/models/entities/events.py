from src.models.settings.base import Base
from sqlalchemy import Column, Integer, String

class Events(Base):
    __tablename__ = "events"

    id = Base.Column(Base.String(255), primary_key=True)
    title = Base.Column(Base.String(255), nullable=False)
    details = Base.Column(Base.String)
    slug = Base.Column(Base.String(255), nullable=False)
    maximum_attendees = Base.Column(Base.Integer)