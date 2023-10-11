from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dao.base import BaseDAO
from models import Question


class QuestionDAO(BaseDAO[Question]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Question, session)

    async def get_by_ids(self, questions_id: list[int]) -> list[int]:
        stmt = select(Question.id).where(Question.id.in_(questions_id))
        result = await self.session.scalars(stmt)
        return result.all()

    async def create(self, questions_json: str, query_id: int) -> list[Question]:
        for question in questions_json:
            self.session.add(
                Question(
                    id=question["id"],
                    text=question["question"],
                    answer=question["answer"],
                    created_at=datetime.fromisoformat(question["created_at"]).replace(
                        tzinfo=None
                    ),
                    query_id=query_id,
                )
            )
        await self.session.flush()
