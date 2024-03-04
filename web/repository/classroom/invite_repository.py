

from src.account.domain.entity.invite import InviteStudent
from src.classroom.domain.repository.invite_repository_interface import InviteStudentRepositoryInterface
from web.repository.classroom.invite_models import InviteModel
from web.repository.db.config.connection import DBConnectionHandler


class InviteStudentRepository(InviteStudentRepositoryInterface):

    @classmethod
    def create(self, input: InviteStudent):
        with DBConnectionHandler() as db:
            try:
                invite = InviteModel(
                    id = input.get_id(),
                    to = input.get_to(),
                    time_expires = input.get_time_expires(),
                    classroom_id = input.get_classroom_id(),
                )
                db.session.add(invite)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error
            
