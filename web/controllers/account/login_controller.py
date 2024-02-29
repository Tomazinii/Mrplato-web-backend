


from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.account.usecase.login_usecase import LoginUsecase
from src.account.usecase.login_usecase_dto import InputLoginUsecase


class LoginController(ControllerInterface):

    def __init__(self, usecase: LoginUsecase):
        self.usecase = usecase

    def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        usecase = self.usecase.execute(kwargs["data"])
        
        response = HttpResponse(
            status_code=200,
            body={"data":usecase}
        )

        return response