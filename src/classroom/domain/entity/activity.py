
import datetime
from src._shared.entity.base_entity import Base
from src.classroom.domain.entity.classroom import Classroom


class Activity(Base):
    __problem: any
    __classroom: Classroom
    __category: str
    __time: datetime.datetime
    __availability: bool = True

    def __init__(self, id, created_at, updated_at):
        super().__init__(id, created_at, updated_at)

    def set_problem(self, problem):
        self.__problem = problem

    def get_problem(self):
        return self.__problem
    
    def set_classroom(self, classroom: Classroom):
        self.__classroom = classroom

    def get_classroom(self):
        return self.__classroom

    def set_category(self, category):
        self.__category = category
    
    def get_category(self):
        return self.__category

    def set_time(self, time):
        self.__time = time

    def verify_time_expired(self) -> bool:
        if datetime.datetime.now() > self.__time:
            self.__availability = False

    def make_availability(self):
        self.__availability = True
    
    def make_unavailability(self):
        self.__availability = False
    
    def get_availability(self):
        return self.__availability
        


    


