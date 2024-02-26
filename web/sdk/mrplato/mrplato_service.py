
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from web.sdk.mrplato.prover_dto import InputProverDto, OutputProverDto


class ServiceMrplato(ServiceMrplatoInterface):

    def __init__(self, prover):
        self.prover = prover

    def prover(self, prover_instance, data: InputProverDto, problem: str) -> OutputProverDto:
        return self.prover(data=data, problem=problem, prover_instance=prover_instance)

    
    def get_option(self, input) -> any:
        return super().get_option(input)