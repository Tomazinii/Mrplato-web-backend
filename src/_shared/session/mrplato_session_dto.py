
import datetime
from typing import Any
from uuid import UUID
from pydantic import BaseModel


class MrplatoSessionDto(BaseModel):
    id: UUID 
    prover: Any
    time_session: Any
 