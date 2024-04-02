import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_attendees():
    event_id = "uuid"
    attendeesInfo = {
        "uuid": "uuid_attendee",
        "name": "name attendee",
        "email": "email@attendee.com",
        "event_id": event_id
    }
    
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendees(attendeesInfo)
    print(response)
    
@pytest.mark.skip(reason="Integração dos dados no banco de dados")   
def test_get_attendees_by_event_id():
    event_id = "uuid_attendee"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendees_by_event_id(event_id)
    print(response)