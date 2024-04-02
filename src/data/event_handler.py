import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.events_repository = EventsRepository()

    def register(self, request: HttpRequest) -> HttpResponse:
        body = request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)
        
        return HttpResponse(
            200, 
            body = {"event_id": body["uuid"]}
            )