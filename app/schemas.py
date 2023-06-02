from datetime import datetime

from pydantic import BaseModel


class Request(BaseModel):
    questions_num: int


class Response(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
    created_on_server_at: datetime

    class Config:
        orm_mode = True
