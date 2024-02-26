import pickle
from src._shared import session
from src._shared.services.service_mrplato_interface import ServiceMrplatoInterface
from src._shared.session.mrplato_session_dto import MrplatoSessionDto
from src._shared.session.mrplato_session_interface import MrplatoSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.mrplato.usecase.prover_usecase_dto import InputProverUsecaseDto, OutpuProverUsecaseDto
from web.sdk.mrplato.prover_dto import InputProverDto, OutputProverDto


class ProverUsecase(UsecaseInterface):
    
    def __init__(self, service: ServiceMrplatoInterface, session: MrplatoSessionInterface):
        self.service = service
        self.session = session


    async def execute(self, input: InputProverUsecaseDto, response) -> OutpuProverUsecaseDto:

        session_data: MrplatoSessionDto = await self.session.verify(session_key=input.session_key, response=response)


        input_prover = InputProverDto(
            input_formula=input.input_formula,
            sel_rule=input.sel_rule,
            selected_proof_line_indexes=input.selected_proof_line_indexes,
            selection=input.selection,
            total_or_partial=input.total_or_partial,
            type_selected=input.type_selected,
        )

        # provisory = '0 - p  → q , p ⊢ (q v p)'
        provisory = '13 - ∼p(a) ⊢ ∼∀xp(x)'
        prover_instance = pickle.loads(session_data.prover)

        prover: OutputProverDto = self.service.prover(prover_instance=prover_instance, data=input_prover, problem=provisory)

        serialized_instance = pickle.dumps(prover.prover_instance)
        session_data.prover = serialized_instance

        await self.session.update(session_key=session_data.id, data_session=session_data)



        output = OutpuProverUsecaseDto(
            lines=prover.lines,
            message=str(prover.message),
            type_output=str(prover.type_output)
        )
        return output