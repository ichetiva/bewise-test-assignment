from typing import TYPE_CHECKING, TypeAlias

from models import Question
from dao import DAOFactory

if TYPE_CHECKING:
    from services import ServicesFactory

QuestionList: TypeAlias = list[dict[str, int | str]]


class QuestionService:
    def __init__(self, daos: DAOFactory, services: "ServicesFactory") -> None:
        self.daos = daos
        self.services = services

    async def replace_duplicates(self, questions_json: QuestionList) -> QuestionList:
        duplicated_questions = await self.daos.question_dao.get_by_ids(
            [q["id"] for q in questions_json]
        )
        while len(duplicated_questions):
            for idx, question in enumerate(questions_json):
                if question["id"] in duplicated_questions:
                    del questions_json[idx]
            new_questions_json = (
                await self.services.question_integration_service.get_questions(
                    len(duplicated_questions)
                )
            )
            questions_json.extend(new_questions_json)
            duplicated_questions = await self.daos.question_dao.get_by_ids(
                [q["id"] for q in new_questions_json]
            )
        return questions_json

    async def create(self, questions_json: QuestionList, query_id: int):
        await self.daos.question_dao.create(questions_json, query_id)
        await self.daos.session.commit()

    async def get_by_query_id(self, query_id: int) -> list[Question]:
        questions = await self.daos.question_dao.get_list(query_id=query_id)
        return questions
