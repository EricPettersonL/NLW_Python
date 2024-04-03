import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, request: HttpRequest) -> HttpResponse:
        body = request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)
        
        return HttpResponse(
            200, 
            body = {"event_id": body["uuid"]}
            )
        
        
    def find_by_id(self, request: HttpRequest) -> HttpResponse:
        event_id = request.params.get("event_id")
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise Exception("Evento não encontrado")
        
        event_attendees_count = self.__events_repository.count_attendees_by_event_id(event_id)
        
        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "attendees_count" : event_attendees_count["attendees_count"]
                }
            },
            status_code=200
        )