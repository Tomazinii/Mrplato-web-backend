from abc import ABC, abstractmethod

from src.classroom.domain.entity.student import Student


class StudentRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: Student):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id) -> Student:
        raise NotImplementedError
    
    @abstractmethod
    def get(self):
        raise NotImplementedError
    
    def verify_create(self, input: Student):
        raise NotImplementedError