

import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException,Response
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.account.usecase.change_password_usecase_dto import InputChangePasswordDto
from src.account.usecase.login_usecase_dto import InputLoginUsecase
from src.classroom.usecases.invite_usecase_dto import InputInviteStudentDto
from src.classroom.usecases.register_classroom_usecase_dto import InputRegisterClassroomDto
from web.adapters.http_adapter import http_adapter
from web.composers.account.change_password_composer import change_password_composer
from web.composers.account.check_composer import check_authentication_composer
from web.composers.account.login_composer import login_composer
from web.composers.account.logout_composer import logout_composer
from web.composers.classroom.classroom_composer import classroom_composer
from web.composers.classroom.invite_composer import invite_composer
from web.session.user_session import cookie

classroom_router= APIRouter()

class InputRegisterClassroomRoute(BaseModel):
    class_name: str
    teacher_email: str
    teacher_name: str

class InputInviteRouter(BaseModel):
    students_email: List
    classroom_id: str


@classroom_router.post("/register_classroom", status_code=201)
def register(requests: Request, input: InputRegisterClassroomRoute):
    try:
        input = InputRegisterClassroomDto(
            class_name= input.class_name,
            created_at=datetime.datetime.now(),
            id=str(uuid4()),
            teacher_created=datetime.datetime.now(),
            teacher_email=input.teacher_email,
            teacher_id=str(uuid4()),
            teacher_name=input.teacher_name,
            teacher_updated=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        response = http_adapter(controller=classroom_composer(), request=requests, input=input, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


@classroom_router.post("/create_invite", status_code=201)
def create_invite(requests: Request, input: InputInviteRouter):
    try:
        input = InputInviteStudentDto(
                classroom_id=input.classroom_id,
                students_email=input.students_email
        )
        response = http_adapter(controller=invite_composer(), request=requests, input=input, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")