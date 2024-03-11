
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from web.sdk.mrplato.get_options_dto import InputGetOptionDto, OutputGetOptionDto
from web.sdk.mrplato.prover_dto import InputProverDto, OutputProverDto


class ServiceMrplato(ServiceMrplatoInterface):

    def __init__(self, prover, get_option_method, get_current_status_prover_method):
        self.prover = prover
        self.get_option_method = get_option_method
        self.get_current_status_prover_method = get_current_status_prover_method

    def prover(self, prover_instance, data: InputProverDto, problem: str) -> OutputProverDto:
        return self.prover(data=data, problem=problem, prover_instance=prover_instance)

    def get_option(self, prover_instance, data: InputGetOptionDto, problem: str) -> OutputGetOptionDto:
        return self.get_option_method(prover_instance=prover_instance, data=data, problem=problem)
    
    def get_current_status_prover(self, prover_instance, problem):
        return self.get_current_status_prover_method(problem=problem, prover_instance=prover_instance)