from src.models.repository.check_ins_repository import CheckInsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckInHandler:
    def __init__(self):
        self.__check_ins_repository = CheckInsRepository()

    def register(self, request: HttpRequest) -> HttpResponse:
        check_in_info = request.params.get("attendee_id")
        self.__check_ins_repository.insert_check_ins(check_in_info)
        
        return HttpResponse(
            body=None,
            status_code=201
        )