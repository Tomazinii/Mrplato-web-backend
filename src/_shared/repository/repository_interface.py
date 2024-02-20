


from abc import ABC, abstractmethod


class RepositoryInterface(ABC):

    @abstractmethod
    def create(self, input) -> any:
        raise Exception("method not implemented")