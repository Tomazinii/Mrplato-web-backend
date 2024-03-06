import datetime

from src._shared.errors.bad_request import BadRequestError


class InviteBase:
    __id: str
    __time_expires: datetime.datetime

    def __init__(self, id, time_expires):
        self.__id = id
        self.__time_expires = time_expires


    def get_id(self):
        return self.__id
    
    def get_time_expires(self):
        return self.__time_expires

    def verify_time_expires(self):
        if datetime.datetime.now() > self.__time_expires:
            raise BadRequestError("invitation time has expired")