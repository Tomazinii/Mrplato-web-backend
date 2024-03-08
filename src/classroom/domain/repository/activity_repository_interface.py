

from abc import ABC, abstractmethod

from src.classroom.domain.entity.activity import Activity


class ActivityRepositoryInterface(ABC):

    @abstractmethod
    def create(self, input: Activity):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_classroom(self, classroom_id):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id):
        raise NotImplementedError