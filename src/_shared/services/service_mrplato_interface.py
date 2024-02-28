


from abc import ABC, abstractmethod


class ServiceMrplatoInterface(ABC):

    @abstractmethod
    def prover(self, prover_instance, data, problem: str) -> any:
        raise NotImplementedError
    

    @abstractmethod
    def get_option(self,prover_instance, data, problem) -> any:
        raise NotImplementedError
