from tools.src._shared.controller.controller_interface import ControllerInterface
from tools.src._shared.controller.https.http_response import HttpResponse
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto
from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase


class RegisterProblemController(ControllerInterface):

    def __init__(self, usecase: RegisterProblemUsecase):
        self.register_usecase = usecase

    def execute(self, requests, data: InputRegisterListProblemDto) -> HttpResponse:
        #usecaseauthentication
        #usecaseauthorization
        
        output:OutputRegisterListProblemDto = self.register_usecase.execute(data)
        file = output.list_problem
        output.list_problem = None

        response = HttpResponse(
            status_code=201,
            body={"data":output, "file":file}
        )
        return response
