

# from unittest.mock import Mock
# from tools.src._shared.controller.https.http_response import HttpResponse
# from tools.src._shared.repository.repository_interface import RepositoryInterface
# from tools.src.problems.usecase.register_list_problem_usecase import RegisterProblemUsecase
# from tools.web.controllers.problems.register_problem_controller import RegisterProblemController

# class HttpRequestMock():
#     def __init__(self) -> None:
#         self.query_params = { "first_name": "meuTeste" }


# def test_register_problem_test():
#     repository = Mock(spec=RepositoryInterface)
#     usecase = RegisterProblemUsecase(repository_service=repository)
#     register_controller = RegisterProblemController(usecase)
#     request = HttpRequestMock()
#     response = register_controller.execute(request)


#     assert isinstance(response, HttpResponse)
#     assert response.status_code == 200
#     assert response.body["data"] is not None