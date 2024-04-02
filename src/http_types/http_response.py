from typing import Dict

class HttpResponse:
    def __init__(self, status_code: int, body: Dict) -> None: 
        self.status_code: int = status_code
        self.body: Dict = body