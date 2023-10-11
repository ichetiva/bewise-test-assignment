from typing import Annotated

from fastapi import APIRouter, Body, Depends

from schemes.questions import QuestionIn, QuestionOut
from dependencies.services import get_services
from services import ServicesFactory

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/", response_model=list[QuestionOut])
async def create_questions(
    data: Annotated[QuestionIn, Body()],
    services: Annotated[ServicesFactory, Depends(get_services)],
):
    query = await services.query_service.create()
    questions_json = await services.question_integration_service.get_questions(
        data.questions_num
    )
    questions_json = await services.question_service.replace_duplicates(questions_json)
    await services.question_service.create(questions_json, query.id)

    if query.id == 1:
        return []
    else:
        return await services.question_service.get_by_query_id(query.id - 1)
