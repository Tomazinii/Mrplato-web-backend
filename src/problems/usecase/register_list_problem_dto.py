
import datetime
from typing import  Any, List
from uuid import uuid4
from pydantic import BaseModel


class InputRegisterListProblemDto(BaseModel):
    id: str = str(uuid4())
    list_name: str
    list_problem: Any
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()
    comentary: str = ""

class OutputRegisterListProblemDto(BaseModel):
    id: str
    list_name: str
    slug: str
    list_problem: List
    created_at: datetime.datetime
    updated_at: datetime.datetime
    comentary: str
