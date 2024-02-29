from src._shared.entity.invite_base import InviteBase
from src._shared.value_object.email import Email


class InviteStudent(InviteBase):
    __classroom_id: str
    __to: Email
    __message: str
    __link: str

    def __init__(self, id, time_expires):
        super().__init__(id, time_expires)




    