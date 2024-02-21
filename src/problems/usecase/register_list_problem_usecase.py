
from tools.src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from tools.src._shared.usecase.usecase_interface import UsecaseInterface
from tools.src.problems.domain.entity.problem import Problem
from tools.src.problems.domain.factory.problem_factory import ProblemFactory
from tools.src.problems.domain.value_object.list import ListProblem
from tools.src.problems.domain.value_object.slug import Slug
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto, OutputRegisterListProblemDto


class RegisterProblemUsecase(UsecaseInterface):

    def __init__(self, repository_service: ProblemRepositoryInterface):
        self.repository = repository_service

    def execute(self, input: InputRegisterListProblemDto) -> OutputRegisterListProblemDto:

        problem = ProblemFactory.create(
            id=input.id,
            list_name=input.list_name,
            comentary=input.comentary,
            created_at=input.created_at,
            list_problem=ListProblem(input.list_problem),
            slug=Slug(input.list_name),
            updated_at=input.updated_at,
        )

        self.repository.create(input=problem)

        output = OutputRegisterListProblemDto(
            comentary=problem.get_comentary(),
            created_at=problem.get_updated_at(),
            id=problem.get_id(),
            list_name=problem.get_list_name(),
            list_problem=problem.get_list_problem().get_list(),
            slug=problem.get_slug().get_slug(),
            updated_at=problem.get_updated_at(),
        )

        return output
