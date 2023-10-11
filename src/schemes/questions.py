from datetime import datetime

from pydantic import BaseModel


class QuestionIn(BaseModel):
    questions_num: int


class QuestionOut(BaseModel):
    id: int
    text: str
    answer: str
    created_at: datetime

    class Config:
        from_attributes = True
