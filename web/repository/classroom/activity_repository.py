from src.classroom.domain.entity.activity import Activity
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from web.repository.classroom.activity_models import ActivityModel
from web.repository.db.config.connection import DBConnectionHandler


class ActivityRepository(ActivityRepositoryInterface):

    @classmethod
    def create(self, input: Activity):
        with DBConnectionHandler() as db:
            try:
                activity = ActivityModel(
                    id=input.get_id(),
                    category=input.get_category(),
                    time=input.get_time(),
                    availability=input.get_availability(),
                    created_at=input.get_created_at(),
                    updated_at=input.get_updated_at(),
                    list_problem=input.get_problem().get_list_problem(),
                    problem_id=input.get_problem().get_id(),
                    problem_name=input.get_problem().get_name(),
                    problem_slug=input.get_problem().get_slug(),
                    classroom_id=input.get_classroom(),
                )

                db.session.add(activity)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error

    @classmethod
    def delete(self, id):
        raise NotImplementedError
    
    @classmethod
    def get_by_classroom(self, classroom_id):
        raise NotImplementedError
    
    @classmethod
    def get(self, teacher_id):
        try:
            with DBConnectionHandler() as db:
              pass

                
        except Exception as error:
            db.session.rollback()
            raise error
        
    
    def get_by_id(self, id):
        raise NotImplementedError
    
