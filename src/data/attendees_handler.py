import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_conflict import HttpConflictError
class AttendeesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def register(self, request: HttpRequest) -> HttpResponse:
        body = request.body
        event_id = request.params.get("event_id")
        
        event_attendees_count = self.__events_repository.count_attendees_by_event_id(event_id)
        if (
            event_attendees_count["maximum_attendees"] < 
            event_attendees_count["attendees_count"] 
        ): raise HttpConflictError("O evento ultrapassou o limite de presença")
        
        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        
        
        self.__attendees_repository.insert_attendees(body)

        return HttpResponse(201,body=None)
    
    def find_attendee_badge(self, request: HttpRequest) -> HttpResponse:
        attendee_id = request.params.get("attendee_id")
        attendee = self.__attendees_repository.get_attendees_by_event_id(attendee_id)
        if not attendee: raise HttpNotFoundError("Participante não encontrado")
        
        return HttpResponse(
            body={
                "badge": {
                    "name": attendee.name,
                    "email": attendee.email,
                    "event_title": attendee.title
                }
            },
            status_code=200
        )
        
        
    def find_attendees_from_event(self, request: HttpRequest) -> HttpResponse:
        event_id = request.params.get("event_id")
        attendees = self.__attendees_repository.get_attendees_by_id(event_id)
        if not attendees: raise HttpNotFoundError("Participantes não encontrados")
        
        
        formatted_attendees =[]
        for attendee in attendees:
            formatted_attendees.append(
                {
                    "id": attendee.id,
                    "name": attendee.name,
                    "email": attendee.email,
                    "checkin_at": attendee.checkin_at,
                    "created_at": attendee.created_at
                }
            )
        
        
        return HttpResponse(
            body={
                "attendees": formatted_attendees
            },
            status_code=200
        )