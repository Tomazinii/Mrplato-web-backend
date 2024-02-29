from src._shared.entity.base_entity import Base
from src._shared.value_object.email import Email
from src.account.domain.value_object.password import Password


class User(Base):
    __username: str
    __email: Email
    __is_admin: bool = False
    __password: Password
    __is_super_user: bool = False

    def __init__(self, id, created_at, updated_at, username, email, password):
        super().__init__(id, created_at, updated_at)
        self.__username = username

    def set_password(self, password: Password):
        self.__password = password.get_password()

    def set_email(self, email: Email):
        self.__email = email.get_email()

    def change_password(self, new_password: Password):
        new_password.change_password(new_password=new_password)
        self.__password = new_password.get_password()

    def set_is_admin(self):
        self.__is_admin = True

    def set_super_user(self):
        self.__is_super_user = True

    def verify_is_admin(self) -> bool:
        return self.__is_admin == True
    
    def verify_is_super_user(self) -> bool:
        return self.__is_super_user == True

    def get_username(self):
        return self.__username
    
    def get_email(self):
        return self.__email.get_email()
    
    def get_password(self):
        return self.__password.get_password()
    