

from src.account.usecase.user_register_usecase import UserRegisterUsecase
from web.controllers.account.register_controller import RegisterController
from web.repository.account.user_repository import UserRepository


def register_composer():
    repository = UserRepository()
    usecase = UserRegisterUsecase(repository=repository)
    controller = RegisterController(usecase=usecase)
    return controller