
from abc import ABC, abstractmethod

from tools.src._shared.controller.https.http_request import HttpRequest
from tools.src._shared.controller.https.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def execute(self, request: HttpRequest) -> HttpResponse:
        pass