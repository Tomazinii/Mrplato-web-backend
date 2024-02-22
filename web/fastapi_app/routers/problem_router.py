
from typing_extensions import Annotated
from pydantic import BaseModel
from fastapi import APIRouter,Request,HTTPException
from fastapi import File, UploadFile
from src._shared.controller.errors.types.handle_http_error import handle_errors
from src._shared.errors.bad_request import BadRequestError
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from web.adapters.http_adapter import http_adapter
from web.composers.problems.register_problem_composer import register_problem_composer

problem_router = APIRouter()



@problem_router.post("/create_test", status_code=201)
def register_problem(request: Request,list_name:str, file: Annotated[UploadFile, File()], comentary:str=""):
    
    try:
        input = InputRegisterListProblemDto(
            comentary=comentary,
            list_name=list_name,
            list_problem=file
        )
        response = http_adapter(request, register_problem_composer(), input=input, response=None)
        return response
    
    except Exception as error:
        http_response  = handle_errors(error)
        raise HTTPException(status_code=http_response.status_code, detail=f"{http_response.body}")


