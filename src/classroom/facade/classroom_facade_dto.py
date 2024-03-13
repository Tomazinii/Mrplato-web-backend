

import datetime
from typing import Any
from pydantic import BaseModel


class InputGetStudentFacadeDto(BaseModel):
    id: str

class OutputGetStudentFacadeDto(BaseModel):
    enrollment: str
    classroom_id: str