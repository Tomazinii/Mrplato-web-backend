
from src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from src.problems.domain.entity.problem import Problem
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from web.repository.db.config.connection import DBConnectionHandler
from web.repository.problems.problem_model import ProblemModel
import json

class ProblemRepository(ProblemRepositoryInterface):

    @classmethod
    def create(self, input: Problem) -> any:
        with DBConnectionHandler() as db:
            try:
                print("TESTE", input.get_id(), input.get_list_name())
                list_problem = input.get_list_problem().get_list()
                problem = ProblemModel(id=input.get_id(),list_name=input.get_list_name(), comentary=input.get_comentary(), list_problem=list_problem, created_at=input.get_created_at(), updated_at=input.get_updated_at(),slug=input.get_slug().get_slug() )
                db.session.add(problem)
                db.session.commit()


            except Exception as error:
                db.session.rollback()
                raise error
                
    
    @classmethod
    def get_by_id(self, id) -> Problem:
        pass
    
    @classmethod
    def delete(self, id):
        pass
    
    @classmethod
    def update(self, input) -> Problem:
        pass