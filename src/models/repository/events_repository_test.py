from .events_repository import EventsRepository
from src.models.settings.connection import db_DBConnectionHandler



db_DBConnectionHandler.connect_to_db()
def test_insert_event():
    events_repository = EventsRepository()
    
    eventsInfo = {
        "uuid": "uuid",
        "title": "title",
        "details": "details",
        "slug": "slug",
        "maximum_attendees": 10
    }
    resposta =events_repository.insert_event(eventsInfo)
    
    print(resposta)