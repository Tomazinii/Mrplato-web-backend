

from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.repository.classroom_repository_interface import ClassroomRepositoryInterface
from web.repository.classroom.classroom_models import ClassroomModel
from web.repository.db.config.connection import DBConnectionHandler


class ClassroomRepository(ClassroomRepositoryInterface):

    @classmethod
    def create(self, input: Classroom):
        with DBConnectionHandler() as db:
            try:
                classroom = ClassroomModel(
                id = input.get_id(),
                class_name = input.get_name_class(),
                teacher_name = input.get_teacher().get_name(),
                teacher_id = input.get_teacher().get_id(),
                teacher_created = input.get_teacher().get_created_at(),
                teacher_updated = input.get_teacher().get_updated_at(),
                teacher_email = input.get_teacher().get_email(),
                created_at = input.get_created_at(),
                updated_at = input.get_updated_at()
                )
                db.session.add(classroom)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            

    @classmethod
    def delete(self, id):
        raise NotImplementedError
    
    @classmethod
    def get_by_id(self, id):
        raise NotImplementedError
    
