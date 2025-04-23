from abc import ABC, abstractmethod

from src.presentation.htttp_types.http_request import HttpRequest
from src.presentation.htttp_types.http_response import HttpResponse

class IController(ABC):
    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse: pass
    