import datetime
from tools.src.problems.domain.value_object import ListProblem
from tools.src._shared.entity import Base


class PropsProblemType:
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comentary: str
    list_name: str
    list_problem_input: ListProblem

class Problem(Base):
    __list_name: str
    __comentary: str = ""
    __list_problem: ListProblem

    def __init__(self, props: PropsProblemType):
        super().__init__(props.id, props.created_at, props.updated_at)
        self.__list_name = props.list_name
        self.__comentary = props.comentary
        list_problem = ListProblem(props.list_problem_input)
        self.__list_problem = list_problem
        

    def get_list_name(self):
        return self.__list_name
    
    def get_comentary(self):
        return self.__comentary
    
    def get_list_problem(self):
        return self.__list_problem

        