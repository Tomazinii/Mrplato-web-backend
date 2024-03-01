

from uuid import uuid4
from src._shared.services.jwt_service_interface import JwtServiceInterface
from src._shared.session.user_session_interface import UserSessionInterface
from src._shared.usecase.usecase_interface import UsecaseInterface
from src._shared.value_object.email import Email
from src.account.domain.entity.user import User
from src.account.domain.repository.user_repository_interface import UserRepositoryInterface
from src.account.domain.value_object.password import Password
from src.account.usecase.login_usecase_dto import InputLoginUsecase


class LoginUsecase(UsecaseInterface):

    def __init__(self, repository: UserRepositoryInterface, service: JwtServiceInterface, session: UserSessionInterface):
        self.repository = repository
        self.service = service
        self.session = session


    async def execute(self, input: InputLoginUsecase, response):
        validate_email = Email(email=input.email)
        user: User = self.repository.get_by_email(email=validate_email.get_email())

        password_login = Password(password=input.password)
        user.verify_password_login(password_login=password_login)
        user.authenticate_user(status=True)

        jwt, jwt_secret = self.service.encode(
            data={
            "user_id": f"{user.get_id()}",
            "email": f"{user.get_email()}",
            "username": f"{user.get_username()}",
            "is_authenticated": f"{user.get_is_authenticated()}"

        }
        )
        
        await self.session.create(jwt=jwt, jwt_secret=jwt_secret, response=response)





