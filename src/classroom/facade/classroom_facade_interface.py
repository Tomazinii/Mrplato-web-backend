
from abc import ABC, abstractmethod
from src.classroom.facade.classroom_facade_dto import InputGetStudentFacadeDto, OutputGetStudentFacadeDto



class ClassroomFacadeInterface(ABC):

    @abstractmethod
    def get_student_by_id(self, input: InputGetStudentFacadeDto) -> OutputGetStudentFacadeDto:
        raise NotImplementedError
