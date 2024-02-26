

from src.mrplato.usecase.prover_usecase import ProverUsecase
from web.controllers.mrplato.prover_mrplato_controller import MrplatoController
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession
from web.sdk.mrplato.prover import prover as prover_method


def mrplato_composer():
    session = MrplatoSession()
    prover = prover_method
    service_prover = ServiceMrplato(prover=prover)
    usecase = ProverUsecase(service=service_prover, session=session)
    controller = MrplatoController(usecase=usecase)
    return controller