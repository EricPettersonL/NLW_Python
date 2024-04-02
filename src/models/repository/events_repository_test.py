import pytest
from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler



db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro no banco de dados")
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
    
    
@pytest.mark.skip(reason="Busca de registro no banco de dados")
def test_get_event_by_id():
    event_id = "uuid"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)