


from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src.account.usecase.user_register_usecase import UserRegisterUsecase


class RegisterController(ControllerInterface):

    def __init__(self, usecase: UserRegisterUsecase):
        self.usecase = usecase

    def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        usecase = self.usecase.execute(kwargs["data"])
        
        response = HttpResponse(
            status_code=200,
            body={"data":usecase}
        )

        return response