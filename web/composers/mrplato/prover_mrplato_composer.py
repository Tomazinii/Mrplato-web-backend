

from src.mrplato.usecase.prover_usecase import ProverUsecase
from src.problems.facade.problem_facade import ProblemFacade
from src.problems.usecase.get_list_problem_usecase import GetListProblemUsecase
from web.controllers.mrplato.prover_mrplato_controller import MrplatoController
from web.repository.problems.problem_repository import ProblemRepository
from web.sdk.mrplato.mrplato_service import ServiceMrplato
from web.session.mrplato_session import MrplatoSession
from web.sdk.mrplato.prover import prover as prover_method


def mrplato_composer():
    session = MrplatoSession()
    prover = prover_method
    service_prover = ServiceMrplato(prover=prover, get_option_method=None)
    problem_repository = ProblemRepository()
    problem_facade = ProblemFacade(get_by_id_usecase=GetListProblemUsecase(repository=problem_repository))
    usecase = ProverUsecase(service=service_prover, session=session, problem_facade=problem_facade)
    controller = MrplatoController(usecase=usecase)
    return controller