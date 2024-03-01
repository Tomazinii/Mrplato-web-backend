

from src.account.usecase.login_usecase import LoginUsecase
from web.controllers.account.login_controller import LoginController
from web.repository.account.user_repository import UserRepository
from web.sdk.jwt.jwt_service import JwtService
from web.session.user_session import UserSession


def login_composer():
    repository = UserRepository()
    service = JwtService()
    session = UserSession()
    usecase = LoginUsecase(repository=repository, service=service, session=session)
    controller = LoginController(usecase=usecase)
    return controller