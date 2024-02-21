

from pydantic import BaseModel
from fastapi import APIRouter,Request
from tools.src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from tools.web.adapters.http_adapter import http_adapter
from tools.web.composers.problems.register_problem_composer import register_problem_composer

problem_router = APIRouter()



@problem_router.post("/create_test")
def register_problem(request: Request):
    
    input = InputRegisterListProblemDto(

    )

    http_adapter(request, register_problem_composer(), input=input, response=response)


    return {
        "name": "name",
        "file":"file",
        "output": "output"
    }


