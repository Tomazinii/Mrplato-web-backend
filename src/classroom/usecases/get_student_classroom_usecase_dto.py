


from pydantic import BaseModel


class OutputGetStudentDto(BaseModel):
    enrollment: str
    classroom_id: str