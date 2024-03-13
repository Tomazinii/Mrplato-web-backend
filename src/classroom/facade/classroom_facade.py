from src._shared.usecase.usecase_interface import UsecaseInterface
from src.classroom.facade.classroom_facade_interface import ClassroomFacadeInterface
from src.problems.facade.problem_facade_dto import InputProblemFacadeDto, OutputProblemFacadeDto
from src.problems.facade.problem_facade_interface import ProblemFacadeInterface


class ClassroomFacade(ClassroomFacadeInterface):

    def __init__(self, get_student: UsecaseInterface):
        self.get_student = get_student

    def get_student_by_id(self, input: InputProblemFacadeDto) -> OutputProblemFacadeDto:
        result = self.get_student.execute(input)
        return result

