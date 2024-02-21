import datetime
from fastapi import Cookie, Request, Respo
from fastapi import Response
from tools.src._shared.controller.controller_interface import ControllerInterface
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto
from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase


class RegisterProblemController(ControllerInterface):

    def __init__(self, usecase: RegisterProblemUsecase):
        self.register_usecase = usecase

    def execute(self, requests: Request, data: InputRegisterListProblemDto, response: Response) -> OutputRegisterListProblemDto:
        
        output = self.register_usecase.execute(data)

        return output
