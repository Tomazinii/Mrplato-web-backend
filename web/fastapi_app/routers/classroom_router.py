

import datetime
from typing import List
from uuid import uuid4
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException,Response
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src.classroom.facade.classroom_facade import ClassroomFacade
from src.classroom.usecases.get_activity_by_id_usecase import GetActivityByIdUsecase
from src.classroom.usecases.get_student_classroom_usecase import GetStudentUsecase
from src.classroom.usecases.invite_usecase_dto import InputInviteStudentDto
from src.classroom.usecases.register_activity_by_insert_dto import InputRegisterActivityByInsertUsecaseDto
from src.classroom.usecases.register_activity_usecase_dto import InputRegisterActivityUsecaseDto
from src.classroom.usecases.register_classroom_usecase_dto import InputRegisterClassroomDto
from src.classroom.usecases.register_student_usecase_dto import InputRegisterStudentUsecaseDto
from src.classroom.usecases.update_activity_usecase_dto import InputUpdateActivityUsecaseDto
from src.statistic.usecase.register_result_activity_usecase import RegisterResultActivityUsecase
from src.statistic.usecase.register_result_activity_usecase_dto import InputRegisterResultActivityUsecaseDto
from web.adapters.http_adapter import http_adapter

from web.composers.classroom.check_invite_composer import check_invite_composer
from web.composers.classroom.classroom_composer import classroom_composer
from web.composers.classroom.delete_activity_composer import delete_activity_composer
from web.composers.classroom.get_activity_by_classroom_composer import get_activity_by_classroom_composer
from web.composers.classroom.get_classroom_composer import get_classroom_composer
from web.composers.classroom.get_invite_by_classroom_composer import get_invite_by_classroom_composer
from web.composers.classroom.invite_composer import invite_composer
from web.composers.classroom.register_acticity_by_insert_composer import register_activity_by_insert_composer
from web.composers.classroom.register_activity_composer import register_activity_composer
from web.composers.classroom.register_student_composer import register_student_composer
from web.composers.classroom.update_activity_composer import update_activity_composer
from web.repository.classroom.activity_repository import ActivityRepository
from web.repository.classroom.student_repository import StudentRepository
from web.repository.statistic.result_activity_repository import ResultActivityRepository
from web.session.user_session import cookie

from typing_extensions import Annotated
from fastapi import File, UploadFile

classroom_router= APIRouter()

class InputRegisterClassroomRoute(BaseModel):
    class_name: str
    teacher_email: str
    teacher_name: str
    user_id: str

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
            teacher_id=input.user_id,
            teacher_name=input.teacher_name,
            teacher_updated=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
        )
        response = http_adapter(controller=classroom_composer(), request=requests, input=input, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")

@classroom_router.get("/get_classroom/{teacher_id}", status_code=201)
def register(requests: Request, teacher_id: str):
    try:
        response = http_adapter(controller=get_classroom_composer(), request=requests, input=teacher_id, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")

class InputCheckInviteRouter(BaseModel):
    invite_id: str

@classroom_router.post("/check_invite", status_code=200)
def check_invite(requests: Request, input: InputCheckInviteRouter):
    try:
        response = http_adapter(controller=check_invite_composer(), request=requests, input=input.invite_id, response=None)
        return response

    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


class InputRegisterStudentRouter(BaseModel):
    enrollment: str
    username: str
    email: str
    password: str
    classroom_id: str
    invite_id: str



@classroom_router.post("/register_student", status_code=200)
def register_student(requests: Request, input: InputRegisterStudentRouter):
    try:
        input = InputRegisterStudentUsecaseDto(
                classroom_id=input.classroom_id,
                created_at=datetime.datetime.now(),
                email=input.email,
                username=input.username,
                enrollment=input.enrollment,
                id=str(uuid4()),
                password=input.password,
                updated_at=datetime.datetime.now(),
                invite_id=input.invite_id
        )

        response = http_adapter(controller=register_student_composer(), request=requests, input=input, response=None)
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
    



class InputRegisterActivitySelectRouter(BaseModel):
    time: datetime.datetime
    problem_id: str
    classroom_id: str
    category: str
    availability: bool



@classroom_router.post("/register_activity_select_problem", status_code=201)
async def register_activity_select_problem(requests: Request, input: InputRegisterActivitySelectRouter, response: Response):

    try:
        input = InputRegisterActivityUsecaseDto(
            category=input.category,
            classroom_id=input.classroom_id,
            created_at=datetime.datetime.now(),
            id=str(uuid4()),
            problem_id=input.problem_id,
            time=input.time,
            availability=input.availability
        )
        response = http_adapter(request=requests, controller=register_activity_composer(), response=response, input=input)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")






@classroom_router.post("/register_activity_insert_problem", status_code=201)
async def register_activity_insert_problem(requests: Request,availability: bool, problem_list_name: str, category: str, classroom_id: str,time: datetime.datetime, file: Annotated[UploadFile, File()], response: Response):
    try:
        input = InputRegisterActivityByInsertUsecaseDto(
            availability=availability,
            category=category,
            classroom_id=classroom_id,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            id=str(uuid4()),
            problem_comentary="",
            problem_created_at=datetime.datetime.now(),
            problem_id=str(uuid4()),
            problem_list_name=problem_list_name,
            problem_list_problem=file,
            problem_updated_at=datetime.datetime.now(),
            time=time
            
        )

  
        response = http_adapter(request=requests, controller=register_activity_by_insert_composer(), response=response, input=input)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


class InputUpdateActivityRouter(BaseModel):
    activity_id: str
    time: datetime.datetime
    category: str
    availability: bool


@classroom_router.put("/update_activity", status_code=200)
async def update_activity(requests: Request, input: InputUpdateActivityRouter):
    try:
        input = InputUpdateActivityUsecaseDto(
            activity_id=input.activity_id,
            availability=input.availability, 
            category=input.category,
            time=input.time,
        )

        response = http_adapter(request=requests, controller=update_activity_composer(), response=None, input=input)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
    

@classroom_router.delete("/delete_activity/{activity_id}", status_code=200)
async def update_activity(requests: Request, activity_id: str):
    try:
        response = http_adapter(request=requests, controller=delete_activity_composer(), response=None, input=activity_id)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")

import time

@classroom_router.get("/get_activity_by_classroom/{classroom_id}", status_code=200)
async def register_activity_select_problem(requests: Request, classroom_id: str, response: Response):
    try:
        response = http_adapter(request=requests, controller=get_activity_by_classroom_composer(), response=response, input=classroom_id)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")



@classroom_router.get("/get_invite_students/{classroom_id}", status_code=200)
async def get_invites(requests: Request, classroom_id: str, response: Response):
    try:
        response = http_adapter(request=requests, controller=get_invite_by_classroom_composer(), response=response, input=classroom_id)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")






@classroom_router.post("/result_acitivy/", status_code=200)
async def test_result(requests: Request, input: InputRegisterResultActivityUsecaseDto, response: Response):
    try:

        repository = ResultActivityRepository()
        activity_repository = ActivityRepository()
        activity_facade = ClassroomFacade(get_activity_by_id=GetActivityByIdUsecase(repository=activity_repository))
        student_facade = ClassroomFacade(get_student=GetStudentUsecase(repository=StudentRepository()))
        usecase = RegisterResultActivityUsecase(repository=repository, activity_facade=activity_facade, student_facade=student_facade,)

        result = usecase.execute(input=input)
        return result
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")
