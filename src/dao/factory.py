from sqlalchemy.ext.asyncio import AsyncSession

from dao.query import QueryDAO
from dao.question import QuestionDAO


class DAOFactory:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @property
    def query_dao(self) -> QueryDAO:
        return QueryDAO(self.session)

    @property
    def question_dao(self) -> QuestionDAO:
        return QuestionDAO(self.session)
