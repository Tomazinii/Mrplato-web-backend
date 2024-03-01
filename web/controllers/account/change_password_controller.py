

from src._shared.controller.controller_interface import ControllerInterface
from src._shared.controller.https.http_request import HttpRequest
from src._shared.controller.https.http_response import HttpResponse
from src.account.usecase.change_password_usecase import ChangePasswordUsecase


class ChangePasswordController(ControllerInterface):

    def __init__(self, usecase: ChangePasswordUsecase):
        self.usecase = usecase


    async def execute(self, request: HttpRequest, **kwargs) -> HttpResponse:
        
        data = kwargs["data"]
        await self.usecase.execute(data)

        return HttpResponse(
            status_code=201,
            body={}
        )
