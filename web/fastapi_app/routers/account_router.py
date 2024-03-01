import datetime
from uuid import uuid4
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException,Response
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.account.usecase.login_usecase_dto import InputLoginUsecase
from src.account.usecase.user_register_usecase_dto import InputUserRegisterUsecaseDto
from src.mrplato.usecase.get_options_usecase_dto import InputGetOptionsUsecaseDto
from src.mrplato.usecase.prover_usecase_dto import InputProverUsecaseDto
from web.adapters.http_adapter import http_adapter
from web.composers.account.check_composer import check_authentication_composer
from web.composers.account.login_composer import login_composer
from web.composers.account.register_compose import register_composer
from web.composers.mrplato.get_options_composer import get_options_composer
from web.composers.mrplato.prover_mrplato_composer import mrplato_composer
from web.session.user_session import cookie

account_router = APIRouter()


class InputRegisterRoute(BaseModel):
    email: str
    password: str
    username: str
    is_admin: bool



class InputLoginRoute(BaseModel):
    email: str
    password: str

@account_router.post("/register", status_code=201)
async def register(requests: Request, input: InputRegisterRoute, response: Response):
    try:
        input = InputUserRegisterUsecaseDto(
            created_at=datetime.datetime.now(),
            email=input.email,
            id=str(uuid4()),
            is_admin=False,
            password=input.password,
            updated_at=datetime.datetime.now(),
            username=input.username
        )
        response = http_adapter(request=requests, controller=register_composer(), response=response, input=input)
        
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



@account_router.post("/login", status_code=200)
async def login(requests: Request, input: InputLoginRoute, response: Response):

    try:

        input = InputLoginUsecase(
            email=input.email,
            password=input.password,
        )

        response = await http_adapter(request=requests, controller=login_composer(), response=response, input=input)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



@account_router.get("/verify", status_code=200)
async def verify(requests: Request):
    try:

        session_key = None
        if requests.cookies.get("user_cookie"):
            session_key = cookie(requests)
   
        response = await http_adapter(request=requests, controller=check_authentication_composer(), response=None, input=session_key)

        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



