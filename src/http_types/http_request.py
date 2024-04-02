from typing import Dict

class HttpRequest:
    def __init__(self, params: Dict = None, body: Dict = None) -> None: 
        self.params: Dict= params
        self.body: Dict = body