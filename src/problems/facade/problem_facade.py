from src._shared.usecase.usecase_interface import UsecaseInterface
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface


class ProblemFacade(ProblemFacadeInterface):

    def __init__(self, get_by_id_usecase: UsecaseInterface):
        self.get_by_id_usecase = get_by_id_usecase

    def get_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:

        result = self.get_by_id_usecase.execute(input)

        return result

