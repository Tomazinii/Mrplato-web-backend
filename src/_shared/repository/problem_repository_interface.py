
from abc import ABC, abstractmethod


class ProblemRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input) -> any:
        raise Exception("method not implemented")