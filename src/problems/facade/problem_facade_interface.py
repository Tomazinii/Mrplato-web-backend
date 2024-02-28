
from abc import ABC, abstractmethod

from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto


class ProblemFacadeInterface(ABC):

    @abstractmethod
    def get_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:
        raise NotImplementedError
