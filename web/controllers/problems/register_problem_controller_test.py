

import datetime
from io import StringIO
from unittest.mock import Mock
from tools.src._shared.controller.https.http_response import HttpResponse
from tools.src._shared.repository.repository_interface import RepositoryInterface
from tools.src.problems.domain.value_object.file import File
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase
from tools.web.controllers.problems.register_problem_controller import RegisterProblemController

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "first_name": "meuTeste" }


def test_register_problem_test():
    repository = Mock(spec=RepositoryInterface)
    usecase = RegisterProblemUsecase(repository_service=repository)
    register_controller = RegisterProblemController(usecase)
    request = HttpRequestMock()

    file_content = "problem1\nproblem2\nproblem3"
    file = StringIO(file_content)
    file.name = "test.txt"
    file = File(file=file, name=file.name)
    created_at = datetime.datetime.now()
    data = InputRegisterListProblemDto(comentary="lista teste comentary",created_at=created_at, id="id", list_name="lista teste", list_problem=file,updated_at=created_at)
    response = register_controller.execute(request, data)


    assert isinstance(response, HttpResponse)
    assert response.status_code == 201
    assert response.body["data"] is not None
    assert response.body["file"] is not None